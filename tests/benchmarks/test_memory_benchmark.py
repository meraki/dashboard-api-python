"""Memory and connection pool benchmarks.

Per D-03: Measure memory usage (RSS via tracemalloc) and connection pool
efficiency (reuse rate, warmup cost).
Run: pytest tests/benchmarks/test_memory_benchmark.py --benchmark-json=memory.json
"""

import tracemalloc

import httpx
import pytest
import respx

import meraki

BASE = "https://api.meraki.com/api/v1"


@pytest.fixture
def fresh_mock_routes():
    """Fresh respx routes for memory isolation."""
    with respx.mock(assert_all_mocked=False, assert_all_called=False) as rsps:
        rsps.get(f"{BASE}/organizations").mock(
            return_value=httpx.Response(
                200, json=[{"id": "123456", "name": "Test Org"}]
            )
        )
        yield rsps


@pytest.fixture
def fresh_dashboard(fresh_mock_routes):
    """Fresh DashboardAPI for memory measurement (no prior allocations)."""
    return meraki.DashboardAPI(
        "fake_key_1234567890123456789012345678901234567890",
        suppress_logging=True,
        maximum_retries=1,
    )


def test_memory_single_request(benchmark, fresh_dashboard):
    """Memory RSS for a single request cycle."""

    def measure():
        tracemalloc.start()
        result = fresh_dashboard.organizations.getOrganizations()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return result, current, peak

    result, current, peak = benchmark(measure)
    benchmark.extra_info["memory_current_bytes"] = current
    benchmark.extra_info["memory_peak_bytes"] = peak
    assert result is not None


def test_memory_batch_requests(benchmark, fresh_dashboard):
    """Memory RSS for 20 sequential requests (detect leaks)."""
    batch_size = 20

    def measure():
        tracemalloc.start()
        for _ in range(batch_size):
            fresh_dashboard.organizations.getOrganizations()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return current, peak

    current, peak = benchmark(measure)
    benchmark.extra_info["memory_current_bytes"] = current
    benchmark.extra_info["memory_peak_bytes"] = peak
    benchmark.extra_info["batch_size"] = batch_size
    benchmark.extra_info["bytes_per_request"] = current // batch_size


def test_connection_pool_warmup(benchmark, fresh_mock_routes):
    """Connection pool warmup cost: first request vs subsequent."""

    def measure_warmup():
        # Fresh client each iteration to measure pool warmup
        dashboard = meraki.DashboardAPI(
            "fake_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            maximum_retries=1,
        )
        # First request (cold pool)
        dashboard.organizations.getOrganizations()
        return dashboard

    benchmark(measure_warmup)
    benchmark.extra_info["measures"] = "cold_pool_initialization"


def test_connection_pool_reuse(benchmark, fresh_dashboard):
    """Connection pool reuse: measure steady-state after warmup."""

    # Warm up the pool
    fresh_dashboard.organizations.getOrganizations()

    def measure_reuse():
        # Subsequent requests reuse existing connection
        return fresh_dashboard.organizations.getOrganizations()

    result = benchmark(measure_reuse)
    benchmark.extra_info["measures"] = "warm_pool_reuse"
    assert result is not None
