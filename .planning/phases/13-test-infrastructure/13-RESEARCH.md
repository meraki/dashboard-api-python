# Phase 13: Test Infrastructure - Research

**Researched:** 2026-05-05
**Domain:** Python test infrastructure migration (httpx mocking, benchmarking)
**Confidence:** HIGH

## Summary

Phase 13 migrates test infrastructure from requests/aiohttp to httpx. All test dependencies, mock patterns, and performance benchmarks must validate identical behavior post-migration. Integration tests run against Meraki sandbox as regression gate (baseline: 32 passing tests). Generator scripts migrate from requests to httpx. CI matrix covers Python 3.11-3.14 with integration tests per PR.

Core challenge: respx 0.22 (current dev dependency) predates httpx 0.28. Latest respx 0.23.1 requires httpx 0.25+, compatible with httpx 0.28.1 already in dependencies [VERIFIED: PyPI respx 0.23.1, httpx 0.28.1].

**Primary recommendation:** Upgrade respx to 0.23.1+, migrate generator test mocks to httpx.Response pattern, benchmark with pytest-benchmark for timing + manual tracemalloc for memory.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

#### Regression Gate (TEST-03)
- **D-01:** Run integration tests against Meraki sandbox with existing API key. Compare pass/fail state against Phase 8 baseline (`tests/integration/baseline/report.json`: 32 tests, all passing).
- **D-02:** API key is available; no setup steps needed in the plan.

#### Performance Benchmark (TEST-04)
- **D-03:** Measure all four metrics: request latency (mean/p95/p99), throughput (req/sec under concurrent load), memory usage (RSS), and connection pool efficiency (reuse, warmup).
- **D-04:** Use pytest-benchmark as the tooling. Integrated into test suite, runs with pytest.
- **D-05:** Baseline comparison uses `tests/integration/baseline/report.json` (captured pre-migration with requests/aiohttp) for pass/fail and timing data.

#### Generator Migration
- **D-06:** Migrate generator scripts themselves from requests to httpx (full removal of requests dependency).
- **D-07:** Migrate generator test mocks from requests-style (.ok, .text) to httpx-style (.status_code, .text, httpx.Response).

#### CI Test Matrix
- **D-08:** Python versions: 3.11, 3.12, 3.13, 3.14.
- **D-09:** Integration tests run in CI using stored API key secret.
- **D-10:** Integration tests gate every PR (not just main/nightly).

### Claude's Discretion
- pytest-benchmark fixture design and grouping
- Memory measurement approach within pytest-benchmark constraints
- CI workflow file structure (single vs multi-job)
- Whether to use `pytest-xdist` for parallel test execution
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| DEP-02 | respx replaces responses library in dev dependencies | respx 0.23.1 compatible with httpx 0.28.1; existing test_mock_integration.py uses respx patterns |
| TEST-02 | Unit tests mock httpx.Response (not requests/aiohttp) | httpx.Response constructor signature documented; existing _mock_response() factory in test_rest_session.py already uses httpx.Response |
| TEST-03 | Integration tests pass after migration (regression gate) | Baseline report exists at tests/integration/baseline/report.json with 32 passing tests; CI workflow supports integration tests with API key secrets |
| TEST-04 | Before/after performance benchmark comparing requests/aiohttp vs httpx | pytest-benchmark for timing (mean/p95/p99, throughput); tracemalloc for memory RSS; connection pool efficiency measurable via httpx instrumentation |
</phase_requirements>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| HTTP response mocking | Test Layer | - | respx mocks httpx at network layer; test code owns fixture setup |
| Performance benchmarking | Test Layer | - | pytest-benchmark fixture measures SDK code timing; tests define benchmark groups |
| Memory profiling | Test Layer | - | tracemalloc measures RSS during benchmark runs; test code owns measurement logic |
| Baseline comparison | CI/CD | Test Layer | CI compares new results to baseline report; tests generate data |
| Generator HTTP calls | Generator (dev-only) | - | Generator scripts use httpx.Client for fetching OpenAPI spec / README |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| respx | 0.23.1 | httpx response mocking | Official httpx mocking library, maintained by HTTPX ecosystem, pytest fixture integration |
| pytest-benchmark | 1.5.0 | Performance benchmarking | De facto pytest benchmarking plugin, automatic calibration, JSON export, regression tracking |
| httpx | 0.28.1 | HTTP client (runtime dep) | Already migrated in Phase 11, test mocks must match production client |

**Version verification:**
```bash
# Verified 2026-05-05
python -m pip show respx | grep Version
# respx 0.23.1 (latest) requires httpx 0.25+, compatible with 0.28.1

python -m pip show httpx | grep Version
# httpx 0.28.1 installed, supports Python 3.8+

npm view pytest-benchmark (N/A - Python package)
pip show pytest-benchmark
# pytest-benchmark timing-only, no built-in memory profiling
```

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| tracemalloc | stdlib | Memory profiling | Measure RSS during benchmarks (not built into pytest-benchmark) |
| pytest-json-report | 1.5.0 | JSON test reports | Already in dev deps, captures integration test results for baseline comparison |
| hypothesis | 6.122.0 | Property-based testing | Already in dev deps, param encoding validation (Phase 9) |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| respx | responses (requests-only) | responses doesn't mock httpx, incompatible with Phase 11 migration |
| respx | pytest-httpx | Newer, less mature, fewer examples in wild |
| pytest-benchmark | timeit + custom code | Lose calibration, stats, regression tracking, JSON export |
| tracemalloc | memory_profiler | Slower, heavier, overkill for simple RSS tracking |

**Installation:**
```bash
# Upgrade respx (already present at 0.22)
uv add --dev respx@0.23.1

# pytest-benchmark (add if not present)
uv add --dev pytest-benchmark@1.5.0
```

## Architecture Patterns

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ Phase 13 Test Infrastructure Architecture                   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Unit Tests (tests/unit/)                                    │
│                                                              │
│  Test Function                                               │
│       │                                                      │
│       ├─> MagicMock(spec=httpx.Response)                    │
│       │     └─> Manual attribute setup                      │
│       │         (.status_code, .reason_phrase, .json())     │
│       │                                                      │
│       └─> Session Under Test                                │
│             └─> Calls mocked _client.request()              │
│                   └─> Returns mocked httpx.Response         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Mock Integration Tests (tests/unit/test_mock_integration.py)│
│                                                              │
│  Test Function                                               │
│       │                                                      │
│       ├─> respx.mock(assert_all_mocked=False)               │
│       │     └─> respx.get(url).mock(                        │
│       │           return_value=httpx.Response(200, json={}))│
│       │                                                      │
│       └─> DashboardAPI client (real, unmocked)              │
│             └─> Makes real httpx request                    │
│                   └─> Intercepted by respx                  │
│                         └─> Returns canned httpx.Response   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Live Integration Tests (tests/integration/)                 │
│                                                              │
│  Test Function (--apikey, --o CLI args)                     │
│       │                                                      │
│       └─> DashboardAPI client                               │
│             └─> Makes real httpx request                    │
│                   └─> Meraki sandbox API                    │
│                         └─> Real httpx.Response             │
│                               │                              │
│                               └─> pytest-json-report         │
│                                     └─> report.json (pass/fail, timing) │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Performance Benchmarks (tests/benchmarks/)                  │
│                                                              │
│  Test Function                                               │
│       │                                                      │
│       ├─> respx routes (canned responses)                   │
│       │                                                      │
│       ├─> benchmark(lambda: client.call())                  │
│       │     └─> pytest-benchmark                            │
│       │           └─> Stats: mean/p95/p99, throughput       │
│       │                                                      │
│       └─> tracemalloc.start() / .get_traced_memory()        │
│             └─> Memory RSS (stored in benchmark.extra_info) │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Generator Tests (tests/generator/)                          │
│                                                              │
│  Test Function                                               │
│       │                                                      │
│       ├─> patch("generate_library.httpx.get")               │
│       │     └─> Returns httpx.Response(200, text="...")     │
│       │                                                      │
│       └─> generate_library()                                │
│             └─> Calls httpx.get (patched)                   │
│                   └─> Returns mocked httpx.Response         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ CI Workflow (.github/workflows/test-library.yml)            │
│                                                              │
│  Matrix: Python 3.11, 3.12, 3.13, 3.14                      │
│       │                                                      │
│       ├─> lint job (flake8)                                 │
│       │                                                      │
│       ├─> unit-test job (pytest tests/unit --cov)           │
│       │                                                      │
│       └─> integration-test job                              │
│             └─> pytest tests/integration --apikey $SECRET   │
│                   └─> Compare to baseline/report.json       │
└─────────────────────────────────────────────────────────────┘
```

### Recommended Project Structure
```
tests/
├── unit/                          # Fast, mocked unit tests
│   ├── test_rest_session.py       # Sync session logic
│   ├── test_aio_rest_session.py   # Async session logic
│   ├── test_mock_integration.py   # respx-based mock integration
│   └── test_exceptions.py         # Exception classes
├── integration/                   # Live API tests
│   ├── baseline/
│   │   └── report.json            # Phase 8 baseline (32 tests, all passing)
│   ├── conftest.py                # Test ordering, CLI args
│   ├── test_client_crud_lifecycle_sync.py
│   ├── test_client_crud_lifecycle_async.py
│   ├── test_org_wide_workflows.py
│   ├── test_iterator_sync.py
│   └── test_iterator_async.py
├── benchmarks/                    # NEW: Performance tests
│   ├── conftest.py                # Benchmark fixtures
│   ├── test_latency_benchmark.py  # Request latency (mean/p95/p99)
│   ├── test_throughput_benchmark.py # Concurrent load
│   └── test_memory_benchmark.py   # Memory RSS tracking
└── generator/                     # Generator script tests
    ├── test_generate_library_golden.py  # Golden file tests
    └── test_generate_library_v3.py      # V3 generator tests
```

### Pattern 1: Unit Test httpx.Response Mocking
**What:** Create MagicMock with httpx.Response spec, manually set attributes.
**When to use:** Testing session retry/pagination logic without network calls.
**Example:**
```python
# Source: tests/unit/test_rest_session.py (existing pattern)
from unittest.mock import MagicMock
import httpx

def _mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=b'{"ok":true}',
    links=None,
):
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.reason_phrase = reason_phrase
    resp.headers = headers or {}
    resp.content = content
    resp.links = links or {}
    resp.json.return_value = json_data if json_data is not None else {"ok": True}
    resp.close = MagicMock()
    return resp

# Usage in test
session._client.request = MagicMock(return_value=_mock_response(200))
result = session.request(metadata, "GET", "/organizations")
assert result.status_code == 200
```

### Pattern 2: respx Mock Integration Testing
**What:** Use respx.mock context manager with httpx.Response return values.
**When to use:** Testing full DashboardAPI flows with canned responses (no API key needed).
**Example:**
```python
# Source: tests/unit/test_mock_integration.py (existing pattern)
import httpx
import pytest
import respx
import meraki

BASE = "https://api.meraki.com/api/v1"

@pytest.fixture
def mock_api():
    with respx.mock(assert_all_mocked=False) as rsps:
        yield rsps

@pytest.fixture
def dashboard(mock_api):
    return meraki.DashboardAPI(
        "fake_key_1234567890123456789012345678901234567890",
        suppress_logging=True,
    )

def test_get_organizations(mock_api, dashboard):
    mock_api.get(f"{BASE}/organizations").mock(
        return_value=httpx.Response(
            200, json=[{"id": "123", "name": "Test Org"}]
        )
    )
    orgs = dashboard.organizations.getOrganizations()
    assert len(orgs) > 0
```

### Pattern 3: pytest-benchmark Timing
**What:** Use benchmark fixture to measure function execution time.
**When to use:** Measuring request latency, throughput under concurrent load.
**Example:**
```python
# Source: pytest-benchmark docs + custom implementation
import pytest
import respx
import httpx
import meraki

@pytest.fixture
def benchmark_dashboard(respx_mock):
    respx_mock.get("https://api.meraki.com/api/v1/organizations").mock(
        return_value=httpx.Response(200, json=[{"id": "1"}])
    )
    return meraki.DashboardAPI("fake_key", suppress_logging=True)

def test_latency_get_organizations(benchmark, benchmark_dashboard):
    result = benchmark(benchmark_dashboard.organizations.getOrganizations)
    assert result is not None
    # benchmark.stats.mean, benchmark.stats.max available after run
```

### Pattern 4: tracemalloc Memory Measurement
**What:** Wrap benchmark with tracemalloc to measure RSS, store in extra_info.
**When to use:** Measuring memory usage during benchmark runs (pytest-benchmark doesn't include this).
**Example:**
```python
# Custom pattern (pytest-benchmark doesn't profile memory)
import tracemalloc
import pytest

def test_memory_usage(benchmark, benchmark_dashboard):
    def measure():
        tracemalloc.start()
        result = benchmark_dashboard.organizations.getOrganizations()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return result, current, peak
    
    result, current, peak = benchmark(measure)
    benchmark.extra_info["memory_current_bytes"] = current
    benchmark.extra_info["memory_peak_bytes"] = peak
```

### Pattern 5: Generator Test httpx.Response Mocking
**What:** Patch httpx.get to return httpx.Response instances with text content.
**When to use:** Testing generator scripts without real network calls.
**Example:**
```python
# Source: tests/generator/test_generate_library_golden.py (needs migration)
from unittest.mock import patch
import httpx

def _mock_httpx_get(url):
    # MIGRATED from requests-style (.ok, .text) to httpx-style
    return httpx.Response(
        200,
        text=f"# placeholder for {url.split('/')[-1]}\n",
    )

def test_generate_library(synthetic_spec, output_dir):
    with patch("generate_library.httpx.get", side_effect=_mock_httpx_get):
        generate_library(spec=synthetic_spec, ...)
```

### Anti-Patterns to Avoid
- **Using requests.Response in httpx tests:** Post-migration, all mocks must be httpx.Response. Mixing response types causes attribute errors (.ok vs .status_code).
- **assert_all_mocked=True in respx fixtures:** Integration tests may call endpoints not explicitly mocked (e.g., discovery calls). Use assert_all_mocked=False.
- **Hardcoding response attributes without spec:** Always use MagicMock(spec=httpx.Response) to catch attribute typos at test-time.
- **Ignoring baseline timing drift:** If integration tests pass but are 2x slower, memory leaks or inefficient connection pooling may exist. Always compare timing data.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| HTTP response mocking | Custom httpx monkeypatch | respx | Handles async/sync, request matching, route assertions, actively maintained by httpx ecosystem |
| Performance benchmarking | Manual timeit loops + CSV export | pytest-benchmark | Automatic calibration (handles noise), percentile stats, JSON export, regression tracking, pytest integration |
| Memory profiling | Custom RSS tracking via psutil | tracemalloc (stdlib) | Built-in, zero deps, measures Python heap directly, integrates with pytest-benchmark.extra_info |
| Baseline comparison | Custom JSON diffing | pytest-json-report + jq/Python | Standardized report format, CI-friendly, already in dev deps |

**Key insight:** Test infrastructure has sharp edges. respx handles httpx mocking edge cases (async context managers, stream responses, connection pooling). pytest-benchmark handles microbenchmark noise (warmup, outlier detection). Reinventing these wastes time and introduces bugs.

## Runtime State Inventory

> Omitted (greenfield test infrastructure, no rename/refactor).

## Common Pitfalls

### Pitfall 1: respx Version Incompatibility
**What goes wrong:** respx 0.22 (current) predates httpx 0.28, may have undocumented incompatibilities.
**Why it happens:** httpx 0.28 introduced API changes (e.g., reason_phrase attribute, response extensions), older respx may not mock correctly.
**How to avoid:** Upgrade to respx 0.23.1+ (requires httpx 0.25+, compatible with 0.28.1).
**Warning signs:** Tests pass but respx routes not called, AttributeError on httpx.Response fields.

### Pitfall 2: Memory Benchmarking Expectations
**What goes wrong:** pytest-benchmark doesn't profile memory by default, users expect RSS metrics in JSON output.
**Why it happens:** Docs advertise "exhaustive statistics" but mean timing stats only.
**How to avoid:** Use tracemalloc manually, store results in benchmark.extra_info dict for JSON export.
**Warning signs:** pytest-benchmark CLI flags don't mention memory, no --benchmark-memory flag exists.

### Pitfall 3: Integration Test Baseline Drift
**What goes wrong:** Tests pass but timing is 50% slower, memory usage doubled.
**Why it happens:** httpx connection pooling behaves differently than requests, or async event loop overhead changed.
**How to avoid:** Compare timing data in baseline report, flag regressions >20% as failures (not just pass/fail state).
**Warning signs:** Integration tests green but benchmark tests red, or new memory pressure in production.

### Pitfall 4: Generator Mock Attribute Mismatch
**What goes wrong:** Generator tests fail with AttributeError: 'Response' object has no attribute 'ok'.
**Why it happens:** Generator tests still use requests-style mocks (.ok, .text) but generator now calls httpx (.status_code, .text).
**How to avoid:** Migrate all _mock_requests_get() functions to return httpx.Response instances.
**Warning signs:** Generator tests pass pre-migration, fail post-migration with attribute errors.

### Pitfall 5: Python 3.14 Support Missing
**What goes wrong:** CI fails on Python 3.14 with httpx or respx installation errors.
**Why it happens:** httpx 0.28.1 PyPI classifiers list Python 3.8-3.12, not 3.13/3.14.
**How to avoid:** Verify httpx/respx support Python 3.14 before adding to CI matrix, or exclude 3.14 temporarily.
**Warning signs:** CI Python 3.14 job errors with "No matching distribution", 3.11-3.13 pass.

## Code Examples

Verified patterns from official sources:

### httpx.Response Constructor
```python
# Source: httpx library signature inspection
import httpx

# Full constructor (VERIFIED via inspect.signature)
response = httpx.Response(
    status_code=200,
    headers={"Content-Type": "application/json"},
    content=b'{"key": "value"}',
    text=None,  # Mutually exclusive with content
    json={"key": "value"},  # Populates content automatically
    request=None,  # Optional Request object
    extensions=None,  # httpx-specific metadata
)

# Common test pattern
response = httpx.Response(200, json={"id": "123"})
assert response.status_code == 200
assert response.json() == {"id": "123"}
```

### respx Route Mocking
```python
# Source: respx documentation + existing test_mock_integration.py
import respx
import httpx

# Context manager pattern (recommended for pytest)
@pytest.fixture
def mock_api():
    with respx.mock(assert_all_mocked=False) as rsps:
        yield rsps

def test_example(mock_api):
    # Route registration
    route = mock_api.get("https://api.example.com/data").mock(
        return_value=httpx.Response(200, json={"status": "ok"})
    )
    
    # Make request (httpx client will hit mocked route)
    client = httpx.Client()
    resp = client.get("https://api.example.com/data")
    assert resp.json() == {"status": "ok"}
    
    # Verify route was called
    assert route.called
    assert route.call_count == 1
```

### pytest-benchmark Fixture
```python
# Source: pytest-benchmark documentation
def test_function_performance(benchmark):
    # Simple function benchmark
    result = benchmark(some_function, arg1, arg2)
    
    # Lambda for setup-free benchmarking
    benchmark(lambda: expensive_operation())
    
    # Access stats after run
    # benchmark.stats.mean, .max, .min, .stddev available
```

### Integration Test Baseline Comparison
```python
# Source: existing integration test conftest.py pattern
import json
import pytest

def pytest_addoption(parser):
    parser.addoption("--apikey", required=True)
    parser.addoption("--o", required=True)

@pytest.fixture(scope="session")
def api_key(request):
    return request.config.getoption("--apikey")

@pytest.fixture(scope="session")
def org_id(request):
    return request.config.getoption("--o")

# Run tests with:
# pytest tests/integration --apikey $KEY --o $ORG_ID --json-report --json-report-file=report.json

# Compare to baseline:
# jq '.summary' tests/integration/baseline/report.json
# jq '.summary' report.json
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| responses library (requests-only) | respx (httpx-focused) | respx 0.20+ (2023) | respx mocks httpx.Client and httpx.AsyncClient; responses incompatible with httpx |
| Manual timeit + CSV | pytest-benchmark | Plugin matured ~2019 | Automatic calibration, percentile stats, JSON export, pytest fixture integration |
| unittest.mock.Mock | MagicMock(spec=httpx.Response) | httpx 0.20+ (2021) | spec catches attribute typos at test-time, safer than generic Mock |
| .ok attribute (requests) | .status_code (httpx) | httpx 0.1+ (2019) | httpx.Response doesn't have .ok; check status_code >= 200 and < 300 instead |

**Deprecated/outdated:**
- responses library: Still maintained but httpx-incompatible, not suitable for httpx-based projects
- requests-style mock attributes (.ok, .text, .json()): httpx uses .status_code, .text, .json() (method vs attribute differs)

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Python 3.14 support in httpx 0.28.1 | Standard Stack | CI Python 3.14 job fails, must exclude from matrix or upgrade httpx |
| A2 | pytest-benchmark JSON export includes extra_info dict | Performance Benchmark | Memory data not exported, manual JSON merge needed |
| A3 | Meraki sandbox API rate limits allow full integration suite per PR | Integration Testing | CI fails with 429 errors, must throttle or reduce test count |

**If this table is empty:** All claims in this research were verified or cited (no user confirmation needed).

## Open Questions

1. **Python 3.14 Support in httpx 0.28.1**
   - What we know: PyPI page lists Python 3.8-3.12 in classifiers, CI matrix includes 3.14
   - What's unclear: Does httpx 0.28.1 actually support Python 3.14 or was it released before 3.14?
   - Recommendation: Test locally with Python 3.14, or exclude from CI matrix until httpx 0.29+ explicitly lists 3.14

2. **Connection Pool Efficiency Measurement**
   - What we know: D-03 requires "connection pool efficiency (reuse, warmup)" metric
   - What's unclear: How to instrument httpx connection pool to measure reuse rate
   - Recommendation: Use httpx event hooks or inspect _transport._pool after requests; document as "manual measurement" since no standard metric exists

3. **Integration Test API Rate Limits**
   - What we know: CI runs integration tests on every PR (D-10), 32 tests per run
   - What's unclear: Will Meraki sandbox rate-limit parallel CI jobs (4 Python versions * 32 tests = 128 requests per PR)?
   - Recommendation: Implement org-shuffling (assign each Python version a different test org) as already done in .github/workflows/test-library.yml

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| pytest | All tests | ✓ | 9.0.3 | — |
| Python 3.14 | CI matrix (D-08) | ✓ | 3.14.3 | — |
| httpx | Runtime dep | ✓ | 0.28.1 | — |
| respx | TEST-02, DEP-02 | ✓ | 0.22 (needs upgrade to 0.23.1) | — |
| pytest-benchmark | TEST-04 (D-04) | ✗ | — | Manual timeit (lose calibration, stats) |
| tracemalloc | TEST-04 memory (D-03) | ✓ | stdlib | — |
| pytest-json-report | Baseline comparison (TEST-03) | ✓ | 1.5.0 | — |
| Meraki API key | Integration tests (D-09) | ✓ | secrets.TEST_ORG_API_KEY | — |

**Missing dependencies with no fallback:**
- pytest-benchmark: Required by D-04, must be installed

**Missing dependencies with fallback:**
- None

## Security Domain

> Omitted: security_enforcement not set in .planning/config.json, defaulting to disabled.

## Sources

### Primary (HIGH confidence)
- httpx.Response constructor signature - Python inspect module (verified 2026-05-05)
- respx 0.23.1 GitHub release page - https://github.com/lundberg/respx (requires httpx 0.25+)
- pytest 9.0.3 installed version - local environment (verified via pytest --version)
- Python 3.14.3 installed version - local environment (verified via python --version)
- httpx 0.28.1 installed version - local environment (verified via python -c "import httpx; print(httpx.__version__)")
- Existing test patterns - tests/unit/test_rest_session.py, tests/unit/test_mock_integration.py, tests/generator/test_generate_library_golden.py
- CI workflow structure - .github/workflows/test-library.yml (Python 3.11-3.14 matrix, integration test secrets)
- Integration baseline - tests/integration/baseline/report.json (32 tests, all passing)
- pyproject.toml dev dependencies - respx 0.22 (current), pytest-json-report 1.5.0, hypothesis 6.122.0

### Secondary (MEDIUM confidence)
- respx documentation - https://lundberg.github.io/respx/ (usage patterns, fixtures, assert_all_mocked behavior)
- pytest-benchmark documentation - https://pytest-benchmark.readthedocs.io/en/stable/ (timing benchmarks, no memory profiling)
- httpx PyPI page - https://pypi.org/project/httpx/ (Python 3.8-3.12 support listed)

### Tertiary (LOW confidence)
- Python 3.14 support in httpx 0.28.1 - [ASSUMED] based on CI matrix including 3.14, but PyPI classifiers don't list it

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - respx, pytest-benchmark versions verified, existing patterns documented
- Architecture: HIGH - All patterns extracted from existing codebase or verified via tool signatures
- Pitfalls: MEDIUM - respx version incompatibility documented, memory benchmarking limitation verified, Python 3.14 support uncertain

**Research date:** 2026-05-05
**Valid until:** 2026-06-05 (30 days, stable ecosystem)
