"""Tests for meraki.smart_limiter module."""

import asyncio
import json
import time
from unittest.mock import patch

import pytest

from meraki.smart_limiter import (
    AsyncOrgRateLimiter,
    AsyncTokenBucket,
    OrgRateLimiter,
    TokenBucket,
)


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
