"""Benchmark test fixtures with respx-mocked HTTP responses."""

import httpx
import pytest
import respx

import meraki

BASE = "https://api.meraki.com/api/v1"
ORG_ID = "123456"
NETWORK_ID = "N_123456"

# Canned response payloads (realistic sizes)
ORGS_RESPONSE = [{"id": ORG_ID, "name": "Test Org", "url": f"https://n1.meraki.com/o/{ORG_ID}/manage/organization/overview"}]
NETWORKS_RESPONSE = [{"id": NETWORK_ID, "organizationId": ORG_ID, "name": "Test Net", "productTypes": ["appliance", "switch"]}]
IDENTITY_RESPONSE = {"name": "Test User", "email": "test@example.com", "authentication": {"api": {"key": {"created": True}}}}


@pytest.fixture
def mock_routes():
    """Set up respx routes for benchmark tests."""
    with respx.mock(assert_all_mocked=True, assert_all_called=False) as rsps:
        rsps.get(f"{BASE}/organizations").mock(return_value=httpx.Response(200, json=ORGS_RESPONSE))
        rsps.get(f"{BASE}/organizations/{ORG_ID}/networks").mock(return_value=httpx.Response(200, json=NETWORKS_RESPONSE))
        rsps.get(f"{BASE}/administered/identities/me").mock(return_value=httpx.Response(200, json=IDENTITY_RESPONSE))
        yield rsps


@pytest.fixture
def benchmark_dashboard(mock_routes):
    """DashboardAPI client for benchmarking (mocked HTTP)."""
    return meraki.DashboardAPI(
        "fake_key_1234567890123456789012345678901234567890",
        suppress_logging=True,
        maximum_retries=1,
        smart_flow_enabled=False,
    )
