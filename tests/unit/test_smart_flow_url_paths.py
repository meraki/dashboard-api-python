"""Resource routing must use URL paths rather than query or fragment text."""

import asyncio

import pytest

from meraki.smart_flow import AsyncOrgRateLimiter, OrgRateLimiter


@pytest.mark.parametrize("limiter_class", [OrgRateLimiter, AsyncOrgRateLimiter])
@pytest.mark.parametrize("resource", ["organizations/org_1", "networks/N_1", "devices/Q123"])
@pytest.mark.parametrize("suffix", ["?perPage=10", "#details", "?next=/organizations/other/networks"])
def test_resolve_org_ignores_query_and_fragment(limiter_class, resource, suffix):
    limiter = limiter_class()
    limiter.register_network("N_1", "org_1")
    limiter.register_device("Q123", "org_1")
    assert limiter.resolve_org(f"https://api.meraki.com/api/v1/{resource}{suffix}") == "org_1"


@pytest.mark.parametrize("limiter_class", [OrgRateLimiter, AsyncOrgRateLimiter])
def test_query_paths_do_not_create_resource_matches(limiter_class):
    limiter = limiter_class()
    assert limiter.resolve_org("/admin?redirect=/organizations/org_1/networks") is None


@pytest.mark.parametrize("resource, id_type, identifier", [("networks", "network", "N_1"), ("devices", "device", "Q123")])
def test_sync_resolver_receives_only_resource_identifier(resource, id_type, identifier):
    calls = []
    limiter = OrgRateLimiter()
    limiter.set_resolver(lambda kind, value: calls.append((kind, value)) or "org_1")
    limiter.acquire(f"/{resource}/{identifier}?perPage=10")
    assert calls == [(id_type, identifier)]
    assert limiter.resolve_org(f"/{resource}/{identifier}") == "org_1"


@pytest.mark.asyncio
async def test_async_resolver_receives_only_resource_identifier():
    calls = []

    async def resolver(kind, value):
        calls.append((kind, value))
        return "org_1"

    limiter = AsyncOrgRateLimiter()
    limiter.set_resolver(resolver)
    await limiter.acquire("/networks/N_1?perPage=10")
    await asyncio.gather(*limiter._bg_tasks)
    assert calls == [("network", "N_1")]
    assert limiter.resolve_org("/networks/N_1") == "org_1"


def test_response_learning_uses_path_identifiers():
    limiter = OrgRateLimiter()
    limiter.learn_from_response("/networks/N_1?perPage=10", {"organizationId": "org_1"})
    assert limiter.resolve_org("/networks/N_1") == "org_1"
