"""Memory benchmarks with leak detection thresholds.

Run: pytest tests/benchmarks/test_memory_benchmark.py --benchmark-json=memory.json
"""

import tracemalloc

import httpx
import pytest
import respx

import meraki

BASE = "https://api.meraki.com/api/v1"

MAX_SINGLE_REQUEST_BYTES = 512 * 1024
MAX_BATCH_BYTES_PER_REQUEST = 64 * 1024


@pytest.fixture
def fresh_mock_routes():
    """Fresh respx routes for memory isolation."""
    with respx.mock(assert_all_mocked=True, assert_all_called=False) as rsps:
        rsps.get(f"{BASE}/organizations").mock(return_value=httpx.Response(200, json=[{"id": "123456", "name": "Test Org"}]))
        yield rsps


@pytest.fixture
def fresh_dashboard(fresh_mock_routes):
    """Fresh DashboardAPI for memory measurement."""
    return meraki.DashboardAPI(
        "fake_key_1234567890123456789012345678901234567890",
        suppress_logging=True,
        maximum_retries=1,
    )


def test_memory_single_request(fresh_dashboard):
    """Memory peak for a single request stays under ceiling."""
    tracemalloc.start()
    fresh_dashboard.organizations.getOrganizations()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    assert peak < MAX_SINGLE_REQUEST_BYTES, f"Single request peak {peak} bytes exceeds {MAX_SINGLE_REQUEST_BYTES} ceiling"


def test_memory_batch_no_leak(fresh_dashboard):
    """Memory growth is sub-linear over 50 requests (no leak)."""
    batch_size = 50
    tracemalloc.start()
    for _ in range(batch_size):
        fresh_dashboard.organizations.getOrganizations()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    per_request = current / batch_size
    assert per_request < MAX_BATCH_BYTES_PER_REQUEST, (
        f"Avg {per_request:.0f} bytes/request suggests memory leak (ceiling: {MAX_BATCH_BYTES_PER_REQUEST})"
    )


def test_connection_pool_reuse(benchmark, fresh_dashboard):
    """Steady-state requests reuse pool (benchmark only, no threshold)."""
    fresh_dashboard.organizations.getOrganizations()
    result = benchmark(fresh_dashboard.organizations.getOrganizations)
    assert result is not None
