"""Request latency benchmarks: mean, p95, p99.

Per D-03: Measure request latency characteristics of httpx backend.
Run: pytest tests/benchmarks/test_latency_benchmark.py --benchmark-json=latency.json
"""


def test_latency_get_organizations(benchmark, benchmark_dashboard):
    """Single GET /organizations latency."""
    result = benchmark(benchmark_dashboard.organizations.getOrganizations)
    assert isinstance(result, list)


def test_latency_get_networks(benchmark, benchmark_dashboard):
    """Single GET /organizations/{id}/networks latency."""
    result = benchmark(
        benchmark_dashboard.organizations.getOrganizationNetworks, "123456"
    )
    assert isinstance(result, list)


def test_latency_get_identity(benchmark, benchmark_dashboard):
    """Single GET /administered/identities/me latency."""
    result = benchmark(benchmark_dashboard.administered.getAdministeredIdentitiesMe)
    assert isinstance(result, dict)
