"""Throughput benchmarks: requests/second under concurrent load.

Per D-03: Measure throughput (req/sec) with batched sequential calls
simulating concurrent load patterns.
Run: pytest tests/benchmarks/test_throughput_benchmark.py --benchmark-json=throughput.json
"""

import time


BATCH_SIZE = 50


def test_throughput_sequential_batch(benchmark, benchmark_dashboard):
    """Throughput: N sequential requests measuring req/sec."""

    def batch_requests():
        start = time.perf_counter()
        results = []
        for _ in range(BATCH_SIZE):
            results.append(benchmark_dashboard.organizations.getOrganizations())
        elapsed = time.perf_counter() - start
        return results, elapsed

    results, elapsed = benchmark(batch_requests)
    assert len(results) == BATCH_SIZE
    benchmark.extra_info["batch_size"] = BATCH_SIZE
    benchmark.extra_info["effective_rps"] = BATCH_SIZE / elapsed if elapsed > 0 else 0


def test_throughput_mixed_endpoints(benchmark, benchmark_dashboard):
    """Throughput: mixed endpoint calls simulating real workload."""

    def mixed_requests():
        start = time.perf_counter()
        results = []
        for i in range(BATCH_SIZE):
            if i % 3 == 0:
                results.append(benchmark_dashboard.administered.getAdministeredIdentitiesMe())
            elif i % 3 == 1:
                results.append(benchmark_dashboard.organizations.getOrganizations())
            else:
                results.append(benchmark_dashboard.organizations.getOrganizationNetworks("123456"))
        elapsed = time.perf_counter() - start
        return results, elapsed

    results, elapsed = benchmark(mixed_requests)
    assert len(results) == BATCH_SIZE
    benchmark.extra_info["batch_size"] = BATCH_SIZE
    benchmark.extra_info["effective_rps"] = BATCH_SIZE / elapsed if elapsed > 0 else 0
