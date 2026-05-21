"""Tests for meraki.smart_limiter module."""

import asyncio
import json
import time
from unittest.mock import MagicMock, patch

import pytest

from meraki.smart_limiter import (
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

    def test_on_rate_limited_noop_for_unknown_org(self):
        limiter = OrgRateLimiter()
        limiter.on_rate_limited("/organizations/ghost/networks")

    def test_on_success_noop_for_unknown_org(self):
        limiter = OrgRateLimiter()
        limiter.on_success("/organizations/ghost/networks")

    def test_on_success_noop_for_unresolvable_url(self):
        limiter = OrgRateLimiter()
        limiter.on_success("/admin/something")

    def test_on_rate_limited_noop_for_unresolvable_url(self):
        limiter = OrgRateLimiter()
        limiter.on_rate_limited("/admin/something")


class TestOrgAcquire:
    def test_acquire_with_org_url(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.acquire("/organizations/org_1/networks")
        assert "org_1" in limiter._org_buckets

    def test_acquire_with_cached_network(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.register_network("N_1", "org_1")
        limiter.acquire("/networks/N_1/ssids")
        assert "org_1" in limiter._org_buckets

    def test_acquire_unknown_url_uses_unknown_bucket(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.acquire("/admin/something")

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

    def test_acquire_resolver_returns_none_uses_unknown(self):
        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(lambda id_type, ident: None)
        limiter.acquire("/networks/N_mystery/ssids")
        assert "N_mystery" not in limiter._network_to_org

    def test_acquire_resolver_exception_uses_unknown(self):
        def bad_resolver(id_type, ident):
            raise RuntimeError("boom")

        limiter = OrgRateLimiter(rate=10.0)
        limiter.set_resolver(bad_resolver)
        limiter.acquire("/networks/N_err/ssids")

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
        logger.debug.assert_called_once_with("smart_limiter, test message")

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
    async def test_acquire_no_resolver_uses_unknown_bucket(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        await limiter.acquire("/networks/N_mystery/ssids")

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
    async def test_on_rate_limited_noop_unknown(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.on_rate_limited("/organizations/ghost/x")

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
    async def test_on_success_noop_unknown(self):
        limiter = AsyncOrgRateLimiter(rate=10.0)
        limiter.on_success("/organizations/ghost/x")

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
        logger.debug.assert_called_with("smart_limiter, hello")

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
