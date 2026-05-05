# Phase 13: Test Infrastructure - Pattern Map

**Mapped:** 2026-05-05
**Files analyzed:** 9 new/modified files
**Analogs found:** 9 / 9

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `tests/benchmarks/conftest.py` | test config | fixture setup | `tests/unit/test_mock_integration.py` | role-match |
| `tests/benchmarks/test_latency_benchmark.py` | test | request-response | `tests/unit/test_mock_integration.py` | role-match |
| `tests/benchmarks/test_throughput_benchmark.py` | test | concurrent load | `tests/unit/test_mock_integration.py` | role-match |
| `tests/benchmarks/test_memory_benchmark.py` | test | request-response | `tests/unit/test_mock_integration.py` | role-match |
| `tests/generator/test_generate_library_golden.py` | test | file I/O | `tests/generator/test_generate_library_golden.py` | exact (migration) |
| `tests/generator/test_generate_library_v3.py` | test | file I/O | `tests/generator/test_generate_library_v3.py` | exact (migration) |
| `generator/generate_library.py` | utility script | request-response | `generator/generate_library.py` | exact (migration) |
| `.github/workflows/test-library.yml` | CI config | workflow | `.github/workflows/test-library.yml` | exact (enhancement) |
| `pyproject.toml` | config | dependency management | `pyproject.toml` | exact (upgrade) |

## Pattern Assignments

### `tests/benchmarks/conftest.py` (test config, fixture setup)

**Analog:** `tests/unit/test_mock_integration.py`

**Imports pattern** (lines 1-11):
```python
import httpx
import pytest
import respx

import meraki

BASE = "https://api.meraki.com/api/v1"
ORG_ID = "123456"
NETWORK_ID = "N_123456"
```

**respx fixture pattern** (lines 20-23):
```python
@pytest.fixture
def mock_api():
    with respx.mock(assert_all_mocked=False) as rsps:
        yield rsps
```

**DashboardAPI fixture pattern** (lines 26-33):
```python
@pytest.fixture
def dashboard(mock_api):
    return meraki.DashboardAPI(
        "fake_key_1234567890123456789012345678901234567890",
        suppress_logging=True,
        caller="MockTest MockVendor",
        maximum_retries=1,
    )
```

---

### `tests/benchmarks/test_latency_benchmark.py` (test, request-response)

**Analog:** `tests/unit/test_mock_integration.py`

**respx route mocking pattern** (lines 41-50):
```python
def test_returns_identity(self, mock_api, dashboard):
    mock_api.get(f"{BASE}/administered/identities/me").mock(
        return_value=httpx.Response(
            200,
            json={
                "name": "Test User",
                "email": "test@example.com",
                "authentication": {"api": {"key": {"created": True}}},
            },
        )
    )
    me = dashboard.administered.getAdministeredIdentitiesMe()
```

**pytest-benchmark fixture usage** (from RESEARCH.md):
```python
def test_latency_get_organizations(benchmark, benchmark_dashboard):
    result = benchmark(benchmark_dashboard.organizations.getOrganizations)
    assert result is not None
    # benchmark.stats.mean, benchmark.stats.max available after run
```

---

### `tests/benchmarks/test_throughput_benchmark.py` (test, concurrent load)

**Analog:** `tests/unit/test_mock_integration.py`

**Base pattern:** Same respx mocking as test_latency_benchmark.py, but with concurrent execution pattern from RESEARCH.md.

---

### `tests/benchmarks/test_memory_benchmark.py` (test, request-response)

**Analog:** `tests/unit/test_mock_integration.py`

**Memory measurement pattern** (from RESEARCH.md):
```python
import tracemalloc

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

---

### `tests/generator/test_generate_library_golden.py` (test, file I/O)

**Analog:** `tests/generator/test_generate_library_golden.py` (MIGRATION NEEDED)

**Current requests-style mock** (lines 50-54):
```python
def _mock_requests_get(url):
    mock_response = MagicMock()
    mock_response.text = f"# placeholder for {url.split('/')[-1]}\n"
    mock_response.ok = True
    return mock_response
```

**Target httpx-style mock** (from RESEARCH.md):
```python
def _mock_httpx_get(url):
    # MIGRATED from requests-style (.ok, .text) to httpx-style
    return httpx.Response(
        200,
        text=f"# placeholder for {url.split('/')[-1]}\n",
    )
```

**Patch location** (line 61):
```python
# OLD: with patch("generate_library_oasv2.requests.get", side_effect=_mock_requests_get):
# NEW: with patch("generate_library_oasv2.httpx.get", side_effect=_mock_httpx_get):
```

---

### `tests/generator/test_generate_library_v3.py` (test, file I/O)

**Analog:** `tests/generator/test_generate_library_v3.py` (MIGRATION NEEDED)

**Current requests-style mock** (lines 34-38):
```python
def _mock_requests_get(url):
    mock_response = MagicMock()
    mock_response.text = f"# placeholder for {url.split('/')[-1]}\n"
    mock_response.ok = True
    return mock_response
```

**Target httpx-style mock** (same as test_generate_library_golden.py):
```python
def _mock_httpx_get(url):
    return httpx.Response(
        200,
        text=f"# placeholder for {url.split('/')[-1]}\n",
    )
```

**Patch location** (line 47):
```python
# OLD: with patch("generate_library.requests.get", side_effect=_mock_requests_get):
# NEW: with patch("generate_library.httpx.get", side_effect=_mock_httpx_get):
```

---

### `generator/generate_library.py` (utility script, request-response)

**Analog:** `generator/generate_library.py` (MIGRATION NEEDED)

**Current requests import** (line 9):
```python
import requests
```

**Target httpx import**:
```python
import httpx
```

**Current requests usage** (line 109):
```python
response = requests.get(f"{base_url}{file}")
```

**Target httpx usage**:
```python
response = httpx.get(f"{base_url}{file}")
```

**Response attribute compatibility**: httpx.Response has `.text` attribute (same as requests), no changes needed beyond client call.

---

### `.github/workflows/test-library.yml` (CI config, workflow)

**Analog:** `.github/workflows/test-library.yml` (ENHANCEMENT)

**Current Python matrix** (line 49):
```yaml
matrix:
  python-version: ["3.11", "3.12", "3.13", "3.14"]
```

**Integration test command** (line 118):
```yaml
uv run pytest tests/integration -v --tb=short --apikey ${{ secrets.TEST_ORG_API_KEY }} --o "$ORG_ID"
```

**New benchmark job pattern** (add after integration-test job):
```yaml
benchmark:
  runs-on: ubuntu-latest
  strategy:
    fail-fast: true
    matrix:
      python-version: ["3.11", "3.12", "3.13", "3.14"]
  
  steps:
  - uses: actions/checkout@v6
  
  - name: Install uv
    uses: astral-sh/setup-uv@v5
    with:
      enable-cache: true
  
  - name: Set up Python ${{ matrix.python-version }}
    run: uv python install ${{ matrix.python-version }}
  
  - name: Install dependencies
    run: uv sync --python ${{ matrix.python-version }}
  
  - name: Run benchmarks
    run: uv run pytest tests/benchmarks --benchmark-json=benchmark-${{ matrix.python-version }}.json
  
  - name: Upload benchmark results
    uses: actions/upload-artifact@v4
    with:
      name: benchmark-${{ matrix.python-version }}
      path: benchmark-${{ matrix.python-version }}.json
```

---

### `pyproject.toml` (config, dependency management)

**Analog:** `pyproject.toml` (UPGRADE)

**Current respx version** (line 39):
```toml
"respx>=0.22,<1",
```

**Target respx version**:
```toml
"respx>=0.23.1,<1",
```

**Add pytest-benchmark** (after line 39):
```toml
"pytest-benchmark>=1.5.0,<2",
```

**Remove requests from generator dependencies**: Verify if requests is listed in `generator` group (not visible in current file, but mentioned in CONTEXT.md).

---

## Shared Patterns

### httpx.Response Mocking (Unit Tests)
**Source:** `tests/unit/test_rest_session.py` (lines 43-59)
**Apply to:** All new benchmark tests

```python
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
```

### respx Route Registration
**Source:** `tests/unit/test_mock_integration.py` (lines 41-50)
**Apply to:** All benchmark tests

```python
mock_api.get(f"{BASE}/organizations").mock(
    return_value=httpx.Response(
        200, json=[{"id": "123", "name": "Test Org"}]
    )
)
```

### pytest.mark.asyncio
**Source:** `tests/unit/test_aio_rest_session.py` (lines 14-46)
**Apply to:** All async tests (not needed for Phase 13, but documented for completeness)

```python
@pytest.fixture
def async_session():
    with (
        patch("meraki.session.base.check_python_version"),
        patch("httpx.AsyncClient") as mock_client,
    ):
        mock_instance = MagicMock()
        mock_instance.headers = {}
        mock_instance.request = AsyncMock()
        mock_client.return_value = mock_instance
```

### Integration Test CLI Args
**Source:** `tests/integration/conftest.py` (lines 23-35)
**Apply to:** Integration test baseline comparison

```python
def pytest_addoption(parser):
    parser.addoption("--apikey", action="store", default="")
    parser.addoption("--o", action="store", default="")

@pytest.fixture(scope="session")
def api_key(pytestconfig):
    return pytestconfig.getoption("apikey")

@pytest.fixture(scope="session")
def org_id(pytestconfig):
    return pytestconfig.getoption("o")
```

## No Analog Found

All files have close analogs in the codebase. No files require fallback to RESEARCH.md patterns.

## Metadata

**Analog search scope:** 
- tests/unit/
- tests/integration/
- tests/generator/
- generator/
- .github/workflows/

**Files scanned:** 23
**Pattern extraction date:** 2026-05-05
