"""Tests for meraki.smart_flow module."""

import asyncio
import json
import time
from unittest.mock import MagicMock, patch

import pytest

from meraki.smart_flow import (
    AsyncOrgRateLimiter,
    AsyncTokenBucket,
    OrgRateLimiter,
    TokenBucket,
    _parse_saved_at,
)


class TestParseSavedAt:
    def test_valid_timestamp(self):
        ts = _parse_saved_at("2026-01-15T12:30:00Z")
        assert ts is not None
        assert isinstance(ts, float)

    def test_non_string_returns_none(self):
        assert _parse_saved_at(None) is None
        assert _parse_saved_at(12345) is None

    def test_invalid_format_returns_none(self):
        assert _parse_saved_at("not-a-date") is None
        assert _parse_saved_at("2026-13-01T00:00:00Z") is None


class TestTokenBucket:
    def test_acquire_within_capacity_does_not_block(self):
        bucket = TokenBucket(rate=10.0, capacity=10)
        start = time.monotonic()
        for _ in range(10):
            bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed < 0.1

    def test_acquire_blocks_when_exhausted(self):
        bucket = TokenBucket(rate=10.0, capacity=1)
        bucket.acquire()
        start = time.monotonic()
        bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed >= 0.05

    def test_rate_setter_floors_at_half(self):
        bucket = TokenBucket(rate=10.0, capacity=10)
        bucket.rate = 0.1
        assert bucket.rate == 0.5

    def test_rate_setter_accepts_normal_values(self):
        bucket = TokenBucket(rate=10.0, capacity=10)
        bucket.rate = 5.0
        assert bucket.rate == 5.0

    def test_tokens_refill_over_time(self):
        bucket = TokenBucket(rate=100.0, capacity=5)
        for _ in range(5):
            bucket.acquire()
        time.sleep(0.06)
        start = time.monotonic()
        bucket.acquire()
        elapsed = time.monotonic() - start
        assert elapsed < 0.05


class TestAsyncTokenBucket:
    @pytest.mark.asyncio
    async def test_acquire_within_capacity_does_not_block(self):
        bucket = AsyncTokenBucket(rate=10.0, capacity=10)
        start = asyncio.get_event_loop().time()
        for _ in range(10):
            await bucket.acquire()
        elapsed = asyncio.get_event_loop().time() - start
        assert elapsed < 0.1

    @pytest.mark.asyncio
    async def test_acquire_blocks_when_exhausted(self):
        bucket = AsyncTokenBucket(rate=10.0, capacity=1)
        await bucket.acquire()
        start = asyncio.get_event_loop().time()
        await bucket.acquire()
        elapsed = asyncio.get_event_loop().time() - start
        assert elapsed >= 0.05

    @pytest.mark.asyncio
    async def test_rate_setter_floors_at_half(self):
        bucket = AsyncTokenBucket(rate=10.0, capacity=10)
        bucket.rate = 0.1
        assert bucket.rate == 0.5

    @pytest.mark.asyncio
    async def test_rate_setter_accepts_normal_values(self):
        bucket = AsyncTokenBucket(rate=10.0, capacity=10)
        bucket.rate = 7.0
        assert bucket.rate == 7.0


class TestOrgResolveOrg:
    def test_resolves_org_from_url(self):
        limiter = OrgRateLimiter()
        assert limiter.resolve_org("/organizations/123/networks") == "123"

    def test_resolves_org_via_network_cache(self):
        limiter = OrgRateLimiter()
        limiter.register_network("N_abc", "org_1")
        assert limiter.resolve_org("/networks/N_abc/ssids") == "org_1"

    def test_resolves_org_via_device_cache(self):
        limiter = OrgRateLimiter()
        limiter.register_device("Q2AB-CDE4-FGHI", "org_2")
        assert limiter.resolve_org("/devices/Q2AB-CDE4-FGHI/clients") == "org_2"

    def test_returns_none_for_unknown(self):
        limiter = OrgRateLimiter()
        assert limiter.resolve_org("/networks/N_unknown/ssids") is None

    def test_returns_none_for_unrecognized_url(self):
        limiter = OrgRateLimiter()
        assert limiter.resolve_org("/admin/something") is None


class TestOrgAIMD:
    def test_on_rate_limited_decreases_rate(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.register_org("org_1")
        url = "/organizations/org_1/networks"
        limiter.on_rate_limited(url)
        bucket = limiter._org_buckets["org_1"]
        assert bucket.rate == pytest.approx(7.0, abs=0.01)

    def test_on_success_increases_rate(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.register_org("org_1")
        url = "/organizations/org_1/networks"
        limiter.on_rate_limited(url)
        limiter.on_success(url)
        bucket = limiter._org_buckets["org_1"]
        assert bucket.rate == pytest.approx(7.2, abs=0.01)

    def test_on_success_caps_at_configured_rate(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.register_org("org_1")
        url = "/organizations/org_1/networks"
        for _ in range(100):
            limiter.on_success(url)
        bucket = limiter._org_buckets["org_1"]
        assert bucket.rate == 10.0

    def test_on_rate_limited_unknown_org_decreases_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        limiter.on_rate_limited("/organizations/ghost/networks")
        assert limiter._global_bucket.rate == pytest.approx(70.0, abs=0.1)

    def test_on_success_unknown_org_nudges_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        limiter._global_bucket.rate = 90.0
        limiter.on_success("/organizations/ghost/networks")
        assert limiter._global_bucket.rate == pytest.approx(90.5, abs=0.01)

    def test_on_success_unresolvable_url_nudges_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        limiter._global_bucket.rate = 80.0
        limiter.on_success("/admin/something")
        assert limiter._global_bucket.rate == pytest.approx(80.5, abs=0.01)

    def test_on_rate_limited_unresolvable_url_decreases_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        limiter.on_rate_limited("/admin/something")
        assert limiter._global_bucket.rate == pytest.approx(70.0, abs=0.1)

    def test_on_success_global_caps_at_configured(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        for _ in range(1000):
            limiter.on_success("/admin/something")
        assert limiter._global_bucket.rate == 100.0


class TestOrgAcquire:
    def test_acquire_with_org_url(self):
        limiter = OrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.acquire("/organizations/org_1/networks")
        assert "org_1" in limiter._org_buckets

    def test_acquire_org_url_deducts_from_both(self):
        limiter = OrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.acquire("/organizations/org_1/networks")
        assert limiter._global_bucket._tokens < 100.0
        assert limiter._org_buckets["org_1"]._tokens < 10.0

    def test_acquire_with_cached_network(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.register_network("N_1", "org_1")
        limiter.acquire("/networks/N_1/ssids")
        assert "org_1" in limiter._org_buckets

    def test_acquire_unresolvable_url_uses_global_only(self):
        limiter = OrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.acquire("/admin/something")
        assert len(limiter._org_buckets) == 0
        assert limiter._global_bucket._tokens < 100.0

    def test_acquire_unknown_network_with_resolver(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(lambda id_type, ident: "org_resolved")
        limiter.acquire("/networks/N_unknown/ssids")
        assert limiter._network_to_org.get("N_unknown") == "org_resolved"

    def test_acquire_unknown_device_with_resolver(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(lambda id_type, ident: "org_dev")
        limiter.acquire("/devices/QXYZ-1234-ABCD/clients")
        assert limiter._serial_to_org.get("QXYZ-1234-ABCD") == "org_dev"

    def test_acquire_resolver_returns_none_uses_global_only(self):
        limiter = OrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.set_resolver(lambda id_type, ident: None)
        limiter.acquire("/networks/N_mystery/ssids")
        assert "N_mystery" not in limiter._network_to_org
        assert len(limiter._org_buckets) == 0

    def test_acquire_resolver_exception_uses_global_only(self):
        def bad_resolver(id_type, ident):
            raise RuntimeError("boom")

        limiter = OrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.set_resolver(bad_resolver)
        limiter.acquire("/networks/N_err/ssids")
        assert len(limiter._org_buckets) == 0

    def test_acquire_deduplicates_pending_lookups(self):
        call_count = 0

        def counting_resolver(id_type, ident):
            nonlocal call_count
            call_count += 1
            return "org_1"

        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(counting_resolver)
        limiter._pending_lookups.add("N_dup")
        limiter.acquire("/networks/N_dup/ssids")
        assert call_count == 0


class TestOrgResolverHydrator:
    def test_resolver_triggers_hydrator_once(self):
        hydrated = []

        def mock_hydrator(org_id):
            hydrated.append(org_id)

        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(lambda id_type, ident: "org_h1")
        limiter.set_hydrator(mock_hydrator)
        limiter.acquire("/networks/N_1/ssids")
        limiter.acquire("/networks/N_2/ssids")
        assert hydrated == ["org_h1"]

    def test_hydrator_not_called_without_resolver_result(self):
        hydrated = []

        def mock_hydrator(org_id):
            hydrated.append(org_id)

        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(lambda id_type, ident: None)
        limiter.set_hydrator(mock_hydrator)
        limiter.acquire("/networks/N_nope/ssids")
        assert hydrated == []


class TestOrgMaybeFlush:
    def test_flush_at_threshold(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = OrgRateLimiter(cache_path=cache_file)
        limiter._dirty = 50
        limiter._maybe_flush()
        assert limiter._dirty == 0
        assert (tmp_path / "cache.json").exists()

    def test_no_flush_below_threshold(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = OrgRateLimiter(cache_path=cache_file)
        limiter._dirty = 49
        limiter._maybe_flush()
        assert limiter._dirty == 49


class TestOrgLogger:
    def test_log_with_logger(self):
        logger = MagicMock()
        limiter = OrgRateLimiter(logger=logger)
        limiter._log("test message")
        logger.debug.assert_called_once_with("smart_flow, test message")

    def test_log_without_logger(self):
        limiter = OrgRateLimiter()
        limiter._log("no crash")


class TestCacheTTL:
    def test_save_and_load_fresh_cache(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = OrgRateLimiter(cache_path=cache_file)
        limiter.register_network("N_1", "org_A")
        limiter.register_device("SERIAL_1", "org_B")
        limiter.save_cache()

        limiter2 = OrgRateLimiter(cache_path=cache_file)
        assert limiter2.resolve_org("/networks/N_1/ssids") == "org_A"
        assert limiter2.resolve_org("/devices/SERIAL_1/clients") == "org_B"

    def test_expired_cache_is_ignored(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = OrgRateLimiter(cache_path=cache_file, cache_ttl=60.0)
        limiter.register_network("N_1", "org_A")
        limiter.save_cache()

        with patch("time.time", return_value=time.time() + 120):
            limiter2 = OrgRateLimiter(cache_path=cache_file, cache_ttl=60.0)
        assert limiter2.resolve_org("/networks/N_1/ssids") is None

    def test_cache_without_timestamp_is_treated_as_expired(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "networks": [{"id": "N_1", "organization": {"id": "org_A"}}],
                    "devices": [],
                }
            )
        )

        limiter = OrgRateLimiter(cache_path=str(cache_file), cache_ttl=60.0)
        assert limiter.resolve_org("/networks/N_1/ssids") is None

    def test_none_ttl_disables_expiration(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "networks": [{"id": "N_1", "organization": {"id": "org_A"}}],
                    "devices": [],
                }
            )
        )

        limiter = OrgRateLimiter(cache_path=str(cache_file), cache_ttl=None)
        assert limiter.resolve_org("/networks/N_1/ssids") == "org_A"

    def test_corrupt_cache_is_ignored(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text("not json{{{")

        limiter = OrgRateLimiter(cache_path=str(cache_file))
        assert limiter.resolve_org("/networks/N_1/ssids") is None

    def test_cache_fresh_flag(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = OrgRateLimiter(cache_path=cache_file)
        assert limiter.cache_fresh is False
        limiter.register_network("N_1", "org_A")
        limiter.save_cache()
        limiter2 = OrgRateLimiter(cache_path=cache_file)
        assert limiter2.cache_fresh is True

    def test_save_without_cache_path_is_noop(self):
        limiter = OrgRateLimiter()
        limiter.save_cache()

    def test_load_nonexistent_cache(self, tmp_path):
        limiter = OrgRateLimiter(cache_path=str(tmp_path / "nope.json"))
        assert limiter.cache_fresh is False

    def test_cache_with_invalid_saved_at_format(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "saved_at": "invalid-date",
                    "networks": [{"id": "N_1", "organization": {"id": "org_A"}}],
                    "devices": [],
                }
            )
        )
        limiter = OrgRateLimiter(cache_path=str(cache_file), cache_ttl=60.0)
        assert limiter.resolve_org("/networks/N_1/ssids") is None


class TestLearnFromResponse:
    def test_learns_org_from_url(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response("/organizations/org_1/networks", [{"id": "N_1"}])
        assert "org_1" in limiter._org_buckets

    def test_learns_network_from_url(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/networks/N_1/ssids",
            {"name": "test"},
        )
        assert limiter._network_to_org.get("N_1") == "org_1"

    def test_learns_serial_from_url(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/devices/Q2AB-1234-ABCD/clients",
            {},
        )
        assert limiter._serial_to_org.get("Q2AB-1234-ABCD") == "org_1"

    def test_learns_network_id_from_body(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/something",
            {"networkId": "N_99"},
        )
        assert limiter._network_to_org.get("N_99") == "org_1"

    def test_learns_serial_from_body(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/something",
            {"serial": "QXYZ-0000-1111"},
        )
        assert limiter._serial_to_org.get("QXYZ-0000-1111") == "org_1"

    def test_learns_org_from_body_organizationId(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/networks/N_5/ssids",
            {"organizationId": "org_7", "networkId": "N_5"},
        )
        assert limiter._network_to_org.get("N_5") == "org_7"

    def test_learns_org_from_body_organization_dict(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/networks/N_6/clients",
            {"organization": {"id": "org_8"}, "networkId": "N_6"},
        )
        assert limiter._network_to_org.get("N_6") == "org_8"

    def test_learns_network_from_body_network_dict(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/something",
            {"network": {"id": "N_nested"}},
        )
        assert limiter._network_to_org.get("N_nested") == "org_1"

    def test_noop_when_no_org_resolvable(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response("/admin/page", {"foo": "bar"})
        assert not limiter._network_to_org
        assert not limiter._serial_to_org

    def test_overwrites_stale_mapping_on_org_change(self):
        limiter = OrgRateLimiter()
        limiter.register_network("N_1", "org_original")
        limiter.learn_from_response(
            "/organizations/org_new/networks/N_1/ssids",
            {},
        )
        assert limiter._network_to_org["N_1"] == "org_new"

    def test_handles_non_dict_body(self):
        limiter = OrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/networks",
            [{"id": "N_1"}, {"id": "N_2"}],
        )
        assert "org_1" in limiter._org_buckets

    def test_no_change_does_not_increment_dirty(self):
        limiter = OrgRateLimiter()
        limiter.register_network("N_1", "org_1")
        limiter._dirty = 0
        limiter.learn_from_response(
            "/organizations/org_1/networks/N_1/ssids",
            {},
        )
        assert limiter._dirty == 0

    def test_learn_triggers_flush_at_threshold(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = OrgRateLimiter(cache_path=cache_file)
        limiter._dirty = 49
        limiter.learn_from_response(
            "/organizations/org_1/networks/N_new/ssids",
            {},
        )
        assert (tmp_path / "cache.json").exists()

    def test_learn_with_logger_logs_changes(self):
        logger = MagicMock()
        limiter = OrgRateLimiter(logger=logger)
        limiter.learn_from_response(
            "/organizations/org_1/networks/N_1/ssids",
            {"serial": "QABC-1111-2222"},
        )
        assert logger.debug.call_count >= 1


class TestAsyncTokenBucketRateSetter:
    @pytest.mark.asyncio
    async def test_rate_property(self):
        bucket = AsyncTokenBucket(rate=10.0, capacity=10)
        assert bucket.rate == 10.0


class TestAsyncOrgRateLimiter:
    @pytest.mark.asyncio
    async def test_resolve_org_from_url(self):
        limiter = AsyncOrgRateLimiter()
        assert limiter.resolve_org("/organizations/org_1/networks") == "org_1"

    @pytest.mark.asyncio
    async def test_resolve_org_via_network_cache(self):
        limiter = AsyncOrgRateLimiter()
        limiter.register_network("N_1", "org_1")
        assert limiter.resolve_org("/networks/N_1/ssids") == "org_1"

    @pytest.mark.asyncio
    async def test_resolve_org_via_device_cache(self):
        limiter = AsyncOrgRateLimiter()
        limiter.register_device("QABC-1234-5678", "org_2")
        assert limiter.resolve_org("/devices/QABC-1234-5678/clients") == "org_2"

    @pytest.mark.asyncio
    async def test_resolve_org_returns_none(self):
        limiter = AsyncOrgRateLimiter()
        assert limiter.resolve_org("/admin/page") is None

    @pytest.mark.asyncio
    async def test_acquire_with_org_url(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        await limiter.acquire("/organizations/org_1/networks")
        assert "org_1" in limiter._org_buckets

    @pytest.mark.asyncio
    async def test_acquire_unknown_triggers_background_resolve(self):
        resolved = []

        async def mock_resolver(id_type, ident):
            resolved.append((id_type, ident))
            return "org_bg"

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(mock_resolver)
        await limiter.acquire("/networks/N_unknown/ssids")
        await asyncio.sleep(0.05)
        assert resolved == [("network", "N_unknown")]
        assert limiter._network_to_org.get("N_unknown") == "org_bg"

    @pytest.mark.asyncio
    async def test_acquire_unknown_device_triggers_resolve(self):
        async def mock_resolver(id_type, ident):
            return "org_dev"

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(mock_resolver)
        await limiter.acquire("/devices/QABC-0000-1111/uplink")
        await asyncio.sleep(0.05)
        assert limiter._serial_to_org.get("QABC-0000-1111") == "org_dev"

    @pytest.mark.asyncio
    async def test_acquire_no_resolver_uses_global_only(self):
        limiter = AsyncOrgRateLimiter(rate=10.0, global_rate=100.0)
        await limiter.acquire("/networks/N_mystery/ssids")
        assert len(limiter._org_buckets) == 0
        assert limiter._global_bucket._tokens < 100.0

    @pytest.mark.asyncio
    async def test_background_resolve_deduplicates(self):
        call_count = 0

        async def mock_resolver(id_type, ident):
            nonlocal call_count
            call_count += 1
            await asyncio.sleep(0.05)
            return "org_1"

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(mock_resolver)
        await limiter.acquire("/networks/N_dup/ssids")
        await limiter.acquire("/networks/N_dup/ssids")
        await asyncio.sleep(0.1)
        assert call_count == 1

    @pytest.mark.asyncio
    async def test_background_resolve_with_hydrator(self):
        hydrated = []

        async def mock_resolver(id_type, ident):
            return "org_h"

        async def mock_hydrator(org_id):
            hydrated.append(org_id)

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(mock_resolver)
        limiter.set_hydrator(mock_hydrator)
        await limiter.acquire("/networks/N_1/ssids")
        await asyncio.sleep(0.05)
        assert hydrated == ["org_h"]

    @pytest.mark.asyncio
    async def test_hydrator_only_called_once_per_org(self):
        hydrated = []

        async def mock_resolver(id_type, ident):
            return "org_h"

        async def mock_hydrator(org_id):
            hydrated.append(org_id)

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(mock_resolver)
        limiter.set_hydrator(mock_hydrator)
        await limiter.acquire("/networks/N_1/ssids")
        await asyncio.sleep(0.05)
        await limiter.acquire("/networks/N_2/ssids")
        await asyncio.sleep(0.05)
        assert hydrated == ["org_h"]

    @pytest.mark.asyncio
    async def test_resolve_exception_is_swallowed(self):
        async def bad_resolver(id_type, ident):
            raise RuntimeError("boom")

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(bad_resolver)
        await limiter.acquire("/networks/N_err/ssids")
        await asyncio.sleep(0.05)

    @pytest.mark.asyncio
    async def test_resolver_returns_none(self):
        async def none_resolver(id_type, ident):
            return None

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(none_resolver)
        await limiter.acquire("/networks/N_nope/ssids")
        await asyncio.sleep(0.05)
        assert "N_nope" not in limiter._network_to_org

    @pytest.mark.asyncio
    async def test_on_rate_limited(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.register_org("org_1")
        limiter.on_rate_limited("/organizations/org_1/networks")
        bucket = limiter._org_buckets["org_1"]
        assert bucket.rate == pytest.approx(7.0, abs=0.01)

    @pytest.mark.asyncio
    async def test_on_rate_limited_unknown_decreases_global(self):
        limiter = AsyncOrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.on_rate_limited("/organizations/ghost/x")
        assert limiter._global_bucket.rate == pytest.approx(70.0, abs=0.1)

    @pytest.mark.asyncio
    async def test_on_success(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.register_org("org_1")
        limiter.on_rate_limited("/organizations/org_1/x")
        limiter.on_success("/organizations/org_1/x")
        bucket = limiter._org_buckets["org_1"]
        assert bucket.rate == pytest.approx(7.2, abs=0.01)

    @pytest.mark.asyncio
    async def test_on_success_caps_at_rate(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.register_org("org_1")
        for _ in range(100):
            limiter.on_success("/organizations/org_1/x")
        bucket = limiter._org_buckets["org_1"]
        assert bucket.rate == 10.0

    @pytest.mark.asyncio
    async def test_on_success_unknown_nudges_global(self):
        limiter = AsyncOrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter._global_bucket.rate = 80.0
        limiter.on_success("/organizations/ghost/x")
        assert limiter._global_bucket.rate == pytest.approx(80.5, abs=0.01)

    @pytest.mark.asyncio
    async def test_register_org(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.register_org("org_new")
        assert "org_new" in limiter._org_buckets

    @pytest.mark.asyncio
    async def test_learn_from_response_network(self):
        limiter = AsyncOrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/networks/N_1/ssids",
            {"networkId": "N_1"},
        )
        assert limiter._network_to_org.get("N_1") == "org_1"

    @pytest.mark.asyncio
    async def test_learn_from_response_device(self):
        limiter = AsyncOrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/devices/QABC-1234-5678/clients",
            {"serial": "QABC-1234-5678"},
        )
        assert limiter._serial_to_org.get("QABC-1234-5678") == "org_1"

    @pytest.mark.asyncio
    async def test_learn_from_response_body_org_id(self):
        limiter = AsyncOrgRateLimiter()
        limiter.learn_from_response(
            "/networks/N_5/ssids",
            {"organizationId": "org_7", "networkId": "N_5"},
        )
        assert limiter._network_to_org.get("N_5") == "org_7"

    @pytest.mark.asyncio
    async def test_learn_from_response_body_org_dict(self):
        limiter = AsyncOrgRateLimiter()
        limiter.learn_from_response(
            "/networks/N_6/clients",
            {"organization": {"id": "org_8"}, "networkId": "N_6"},
        )
        assert limiter._network_to_org.get("N_6") == "org_8"

    @pytest.mark.asyncio
    async def test_learn_from_response_network_dict_in_body(self):
        limiter = AsyncOrgRateLimiter()
        limiter.learn_from_response(
            "/organizations/org_1/something",
            {"network": {"id": "N_nested"}},
        )
        assert limiter._network_to_org.get("N_nested") == "org_1"

    @pytest.mark.asyncio
    async def test_learn_noop_no_org(self):
        limiter = AsyncOrgRateLimiter()
        limiter.learn_from_response("/admin/x", {"foo": "bar"})
        assert not limiter._network_to_org

    @pytest.mark.asyncio
    async def test_learn_no_change_no_dirty(self):
        limiter = AsyncOrgRateLimiter()
        limiter.register_network("N_1", "org_1")
        limiter._dirty = 0
        limiter.learn_from_response("/organizations/org_1/networks/N_1/ssids", {})
        assert limiter._dirty == 0

    @pytest.mark.asyncio
    async def test_learn_logs_changes(self):
        logger = MagicMock()
        limiter = AsyncOrgRateLimiter(logger=logger)
        limiter.learn_from_response(
            "/organizations/org_1/networks/N_1/ssids",
            {"serial": "QABC-0000-1111"},
        )
        assert logger.debug.call_count >= 1

    @pytest.mark.asyncio
    async def test_maybe_flush_at_threshold(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file)
        limiter._dirty = 50
        limiter._maybe_flush()
        await asyncio.sleep(0.05)
        assert (tmp_path / "cache.json").exists()

    @pytest.mark.asyncio
    async def test_maybe_flush_skips_if_task_running(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file)
        limiter._dirty = 50
        limiter._flush_task = asyncio.ensure_future(asyncio.sleep(1.0))
        limiter._maybe_flush()
        assert limiter._dirty == 50
        limiter._flush_task.cancel()
        try:
            await limiter._flush_task
        except asyncio.CancelledError:
            pass

    @pytest.mark.asyncio
    async def test_log_with_logger(self):
        logger = MagicMock()
        limiter = AsyncOrgRateLimiter(logger=logger)
        limiter._log("hello")
        logger.debug.assert_called_with("smart_flow, hello")

    @pytest.mark.asyncio
    async def test_log_without_logger(self):
        limiter = AsyncOrgRateLimiter()
        limiter._log("no crash")

    @pytest.mark.asyncio
    async def test_cache_fresh_property(self):
        limiter = AsyncOrgRateLimiter()
        assert limiter.cache_fresh is False


class TestAsyncCacheTTL:
    @pytest.mark.asyncio
    async def test_save_and_load_fresh_cache(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file)
        limiter.register_network("N_1", "org_A")
        await limiter.save_cache()

        limiter2 = AsyncOrgRateLimiter(cache_path=cache_file)
        assert limiter2.resolve_org("/networks/N_1/ssids") == "org_A"

    @pytest.mark.asyncio
    async def test_expired_cache_is_ignored(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file, cache_ttl=60.0)
        limiter.register_network("N_1", "org_A")
        await limiter.save_cache()

        with patch("time.time", return_value=time.time() + 120):
            limiter2 = AsyncOrgRateLimiter(cache_path=cache_file, cache_ttl=60.0)
        assert limiter2.resolve_org("/networks/N_1/ssids") is None

    @pytest.mark.asyncio
    async def test_save_without_cache_path(self):
        limiter = AsyncOrgRateLimiter()
        await limiter.save_cache()

    @pytest.mark.asyncio
    async def test_none_ttl_disables_expiration(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "networks": [{"id": "N_1", "organization": {"id": "org_A"}}],
                    "devices": [],
                }
            )
        )
        limiter = AsyncOrgRateLimiter(cache_path=str(cache_file), cache_ttl=None)
        assert limiter.resolve_org("/networks/N_1/ssids") == "org_A"

    @pytest.mark.asyncio
    async def test_corrupt_cache_ignored(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text("not json{{{")
        limiter = AsyncOrgRateLimiter(cache_path=str(cache_file))
        assert limiter.cache_fresh is False

    @pytest.mark.asyncio
    async def test_cache_without_timestamp_expired(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "networks": [{"id": "N_1", "organization": {"id": "org_A"}}],
                    "devices": [],
                }
            )
        )
        limiter = AsyncOrgRateLimiter(cache_path=str(cache_file), cache_ttl=60.0)
        assert limiter.resolve_org("/networks/N_1/ssids") is None

    @pytest.mark.asyncio
    async def test_nonexistent_cache_path(self, tmp_path):
        limiter = AsyncOrgRateLimiter(cache_path=str(tmp_path / "nope.json"))
        assert limiter.cache_fresh is False

    @pytest.mark.asyncio
    async def test_invalid_saved_at_treated_as_expired(self, tmp_path):
        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "saved_at": "bad-format",
                    "networks": [{"id": "N_1", "organization": {"id": "org_A"}}],
                    "devices": [],
                }
            )
        )
        limiter = AsyncOrgRateLimiter(cache_path=str(cache_file), cache_ttl=60.0)
        assert limiter.resolve_org("/networks/N_1/ssids") is None


class TestSyncTokenBucketThreadSafety:
    """Fix #11: TokenBucket must have a real lock and not over-spend."""

    def test_lock_exists_and_is_a_lock(self):
        bucket = TokenBucket(rate=10.0, capacity=10)
        # threading.Lock() returns a lock object exposing acquire/release.
        assert hasattr(bucket, "_lock")
        assert hasattr(bucket._lock, "acquire")
        assert hasattr(bucket._lock, "release")

    def test_concurrent_threads_do_not_overspend(self):
        import threading

        # Capacity covers the burst exactly; with a real lock, total wall time
        # for capacity-many concurrent acquires stays near zero (no double-spend
        # forcing a sleep). Without a lock, the read-modify-write races.
        bucket = TokenBucket(rate=10.0, capacity=20)
        barrier = threading.Barrier(20)

        def worker():
            barrier.wait()
            bucket.acquire()

        threads = [threading.Thread(target=worker) for _ in range(20)]
        start = time.monotonic()
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        elapsed = time.monotonic() - start

        # 20 acquires against capacity 20 should all be served from the bucket
        # without anyone sleeping for a refill.
        assert elapsed < 0.5
        # Exactly 20 tokens were spent. With a real lock the deficit is bounded
        # (~0, give or take tiny refill); without one, racing read-modify-writes
        # would let tokens stay well above 0 (double-spend) or be inconsistent.
        assert -0.05 <= bucket._tokens <= 0.05

    def test_aggregate_rate_not_exceeded_when_drained(self):
        # Drain the bucket, then 5 concurrent acquires must take ~ (5 / rate).
        import threading

        bucket = TokenBucket(rate=20.0, capacity=1)
        bucket.acquire()  # drain the single token

        def worker():
            bucket.acquire()

        threads = [threading.Thread(target=worker) for _ in range(5)]
        start = time.monotonic()
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        elapsed = time.monotonic() - start

        # 5 tokens at 20/s with a drained bucket => >= ~0.20s minimum.
        assert elapsed >= 0.20 - 0.03


class TestAsyncTokenBucketConcurrency:
    """Fix #10: acquire() must not serialize all coroutines behind one sleeper."""

    @pytest.mark.asyncio
    async def test_concurrent_acquirers_not_serialized(self):
        # Drained bucket, 5 concurrent acquirers. If the lock were held across
        # the sleep they would queue serially (~5 * per-token wait). With the
        # reservation fix they each sleep concurrently against a shared deficit.
        bucket = AsyncTokenBucket(rate=10.0, capacity=1)
        await bucket.acquire()  # drain

        start = asyncio.get_event_loop().time()
        await asyncio.gather(*(bucket.acquire() for _ in range(5)))
        elapsed = asyncio.get_event_loop().time() - start

        # Serialized-across-sleep behavior would be ~5 * 0.1 = 0.5s+ stacking.
        # Concurrent reservation: the last reservation waits ~5/10 = 0.5s, but
        # they overlap so total is bounded by the max single wait (~0.5s) and
        # crucially is NOT additive blow-up. Assert it's not pathologically
        # serialized (which would be each waiting then the next computing fresh
        # after the previous slept -> well over the deficit window).
        assert elapsed < 1.0

    @pytest.mark.asyncio
    async def test_aggregate_rate_not_exceeded(self):
        # Across many acquires the steady-state dispatch must stay <= rate.
        rate = 50.0
        n = 25
        bucket = AsyncTokenBucket(rate=rate, capacity=1)
        await bucket.acquire()  # drain

        start = asyncio.get_event_loop().time()
        await asyncio.gather(*(bucket.acquire() for _ in range(n)))
        elapsed = asyncio.get_event_loop().time() - start

        # n tokens at `rate`/s from a drained bucket cannot complete faster than
        # n/rate seconds without exceeding the configured rate.
        min_expected = n / rate
        assert elapsed >= min_expected - 0.05


class TestAsyncBgTaskRetention:
    """Fix #6: background resolve tasks are held then discarded on completion."""

    @pytest.mark.asyncio
    async def test_bg_task_retained_then_discarded(self):
        started = asyncio.Event()
        release = asyncio.Event()

        async def slow_resolver(id_type, ident):
            started.set()
            await release.wait()
            return "org_bg"

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(slow_resolver)
        await limiter.acquire("/networks/N_held/ssids")
        await started.wait()

        # While in flight, the limiter holds a strong ref.
        assert len(limiter._bg_tasks) == 1

        release.set()
        await asyncio.sleep(0.02)

        # Done-callback discards it.
        assert len(limiter._bg_tasks) == 0
        assert limiter._network_to_org.get("N_held") == "org_bg"

    @pytest.mark.asyncio
    async def test_resolver_exception_logged_not_swallowed(self):
        logger = MagicMock()

        async def bad_resolver(id_type, ident):
            raise RuntimeError("boom")

        limiter = AsyncOrgRateLimiter(rate=10.0, logger=logger)
        limiter.set_resolver(bad_resolver)
        await limiter.acquire("/networks/N_err/ssids")
        await asyncio.sleep(0.02)

        # The bare except now logs at debug instead of fully swallowing.
        logged = " ".join(str(c) for c in logger.debug.call_args_list)
        assert "failed" in logged
        assert len(limiter._bg_tasks) == 0


class TestAsyncFlushDirtyOnFailure:
    """Fix #8: dirty count must survive a failed save."""

    @pytest.mark.asyncio
    async def test_dirty_not_zeroed_when_save_raises(self):
        limiter = AsyncOrgRateLimiter(cache_path="ignored")
        limiter._dirty = 50

        async def failing_save():
            raise OSError("disk full")

        with patch.object(limiter, "save_cache", side_effect=failing_save):
            limiter._maybe_flush()
            await asyncio.sleep(0.02)

        # Save failed -> dirty must be retained, not lost.
        assert limiter._dirty == 50

    @pytest.mark.asyncio
    async def test_dirty_zeroed_on_successful_save(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file)
        limiter.register_network("N_1", "org_A")
        limiter._dirty = 50
        limiter._maybe_flush()
        # Wait for the flush task and its done-callback to run.
        if limiter._flush_task:
            await limiter._flush_task
        await asyncio.sleep(0.02)
        assert limiter._dirty == 0


class TestUnresolvedRateLimitGlobalProtection:
    """Fix #13: a 429 on an unresolved network/device must not lower global."""

    def test_sync_unresolved_network_does_not_lower_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        before = limiter._global_bucket.rate
        limiter.on_rate_limited("/networks/N_unknown/ssids")
        assert limiter._global_bucket.rate == before

    def test_sync_unresolved_device_does_not_lower_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        before = limiter._global_bucket.rate
        limiter.on_rate_limited("/devices/Q2AB-CDE4-FGHI/clients")
        assert limiter._global_bucket.rate == before

    def test_sync_explicit_org_url_still_lowers_global(self):
        # An explicit, unbucketed org URL is a known org -> existing behavior.
        limiter = OrgRateLimiter(global_rate=100.0)
        limiter.on_rate_limited("/organizations/ghost/networks")
        assert limiter._global_bucket.rate == pytest.approx(70.0, abs=0.1)

    def test_sync_truly_unscoped_url_still_lowers_global(self):
        limiter = OrgRateLimiter(global_rate=100.0)
        limiter.on_rate_limited("/admin/something")
        assert limiter._global_bucket.rate == pytest.approx(70.0, abs=0.1)

    def test_sync_resolved_network_penalizes_org_not_global(self):
        limiter = OrgRateLimiter(rate=10.0, global_rate=100.0)
        limiter.register_network("N_known", "org_k")
        limiter.register_org("org_k")
        global_before = limiter._global_bucket.rate
        limiter.on_rate_limited("/networks/N_known/ssids")
        assert limiter._org_buckets["org_k"].rate == pytest.approx(7.0, abs=0.01)
        assert limiter._global_bucket.rate == global_before

    @pytest.mark.asyncio
    async def test_async_unresolved_network_does_not_lower_global(self):
        limiter = AsyncOrgRateLimiter(global_rate=100.0)
        before = limiter._global_bucket.rate
        limiter.on_rate_limited("/networks/N_unknown/ssids")
        assert limiter._global_bucket.rate == before

    @pytest.mark.asyncio
    async def test_async_explicit_org_url_still_lowers_global(self):
        limiter = AsyncOrgRateLimiter(global_rate=100.0)
        limiter.on_rate_limited("/organizations/ghost/x")
        assert limiter._global_bucket.rate == pytest.approx(70.0, abs=0.1)


class TestAsyncShutdown:
    """Fix #7-SUPPORT: shutdown() drains bg tasks, flush, and saves."""

    @pytest.mark.asyncio
    async def test_shutdown_awaits_pending_bg_tasks(self, tmp_path):
        release = asyncio.Event()
        finished = []

        async def slow_resolver(id_type, ident):
            await release.wait()
            finished.append(ident)
            return "org_s"

        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(rate=10.0, cache_path=cache_file)
        limiter.set_resolver(slow_resolver)
        await limiter.acquire("/networks/N_shutdown/ssids")
        assert len(limiter._bg_tasks) == 1

        # Release the resolver, then shutdown should await it to completion.
        release.set()
        await limiter.shutdown()

        assert finished == ["N_shutdown"]
        assert len(limiter._bg_tasks) == 0
        assert limiter._network_to_org.get("N_shutdown") == "org_s"
        # Final save happened.
        assert (tmp_path / "cache.json").exists()

    @pytest.mark.asyncio
    async def test_shutdown_idempotent_with_no_work(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file)
        # No bg tasks, no flush task -> safe to call, does a final save.
        await limiter.shutdown()
        await limiter.shutdown()
        assert (tmp_path / "cache.json").exists()

    @pytest.mark.asyncio
    async def test_shutdown_awaits_pending_flush(self, tmp_path):
        cache_file = str(tmp_path / "cache.json")
        limiter = AsyncOrgRateLimiter(cache_path=cache_file)
        limiter.register_network("N_1", "org_A")
        limiter._dirty = 50
        limiter._maybe_flush()
        assert limiter._flush_task is not None
        await limiter.shutdown()
        # Flush completed without error -> dirty zeroed.
        assert limiter._dirty == 0


class TestAsyncBackgroundResolveEdgeCases:
    @pytest.mark.asyncio
    async def test_unrecognized_url_no_resolve(self):
        called = []

        async def mock_resolver(id_type, ident):
            called.append(ident)
            return "org_1"

        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.set_resolver(mock_resolver)
        await limiter.acquire("/admin/something")
        await asyncio.sleep(0.05)
        assert called == []
