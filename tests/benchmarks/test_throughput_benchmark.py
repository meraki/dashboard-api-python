"""Throughput benchmarks: requests/second.

Run: pytest tests/benchmarks/test_throughput_benchmark.py --benchmark-json=throughput.json
"""

BATCH_SIZE = 50
MIN_RPS = 20


def test_throughput_sequential_batch(benchmark, benchmark_dashboard):
    """Throughput: N sequential requests."""

    def batch_requests():
        for _ in range(BATCH_SIZE):
            benchmark_dashboard.organizations.getOrganizations()

    benchmark.pedantic(batch_requests, iterations=1, rounds=5)
    elapsed = benchmark.stats.stats.mean
    rps = BATCH_SIZE / elapsed if elapsed > 0 else 0
    benchmark.extra_info["effective_rps"] = rps
    assert rps > MIN_RPS, f"RPS {rps:.0f} below minimum {MIN_RPS}"


def test_throughput_mixed_endpoints(benchmark, benchmark_dashboard):
    """Throughput: mixed endpoint calls."""

    def mixed_requests():
        for i in range(BATCH_SIZE):
            if i % 3 == 0:
                benchmark_dashboard.administered.getAdministeredIdentitiesMe()
            elif i % 3 == 1:
                benchmark_dashboard.organizations.getOrganizations()
            else:
                benchmark_dashboard.organizations.getOrganizationNetworks("123456")

    benchmark.pedantic(mixed_requests, iterations=1, rounds=5)
    elapsed = benchmark.stats.stats.mean
    rps = BATCH_SIZE / elapsed if elapsed > 0 else 0
    benchmark.extra_info["effective_rps"] = rps
    assert rps > MIN_RPS, f"RPS {rps:.0f} below minimum {MIN_RPS}"
