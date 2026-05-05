# Phase 13: Test Infrastructure - Context

**Gathered:** 2026-05-05
**Status:** Ready for planning

<domain>
## Phase Boundary

All tests mock httpx responses and validate identical behavior post-migration. Integration tests pass against Meraki sandbox. Performance benchmark documents httpx characteristics. Generator scripts and their tests fully migrated from requests to httpx.

</domain>

<decisions>
## Implementation Decisions

### Regression Gate (TEST-03)
- **D-01:** Run integration tests against Meraki sandbox with existing API key. Compare pass/fail state against Phase 8 baseline (`tests/integration/baseline/report.json`: 32 tests, all passing).
- **D-02:** API key is available; no setup steps needed in the plan.

### Performance Benchmark (TEST-04)
- **D-03:** Measure all four metrics: request latency (mean/p95/p99), throughput (req/sec under concurrent load), memory usage (RSS), and connection pool efficiency (reuse, warmup).
- **D-04:** Use pytest-benchmark as the tooling. Integrated into test suite, runs with pytest.
- **D-05:** Baseline comparison uses `tests/integration/baseline/report.json` (captured pre-migration with requests/aiohttp) for pass/fail and timing data.

### Generator Migration
- **D-06:** Migrate generator scripts themselves from requests to httpx (full removal of requests dependency).
- **D-07:** Migrate generator test mocks from requests-style (.ok, .text) to httpx-style (.status_code, .text, httpx.Response).

### CI Test Matrix
- **D-08:** Python versions: 3.11, 3.12, 3.13, 3.14.
- **D-09:** Integration tests run in CI using stored API key secret.
- **D-10:** Integration tests gate every PR (not just main/nightly).

### Claude's Discretion
- pytest-benchmark fixture design and grouping
- Memory measurement approach within pytest-benchmark constraints
- CI workflow file structure (single vs multi-job)
- Whether to use `pytest-xdist` for parallel test execution

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Test Baseline
- `tests/integration/baseline/report.json` - Phase 8 baseline: 32 integration tests, all passing, with timing data

### Current Test Files (already migrated to httpx)
- `tests/unit/test_rest_session.py` - Sync session tests, already uses httpx.Response mocks
- `tests/unit/test_aio_rest_session.py` - Async session tests, already uses httpx.AsyncClient mocks
- `tests/unit/test_mock_integration.py` - Mock integration tests, already uses respx
- `tests/unit/test_exceptions.py` - Exception class tests

### Generator Tests (need migration)
- `tests/generator/test_generate_library_golden.py` - Uses requests-style MagicMock (.ok, .text)
- `tests/generator/test_generate_library_v3.py` - Uses requests-style MagicMock (.ok, .json())

### Generator Scripts (need migration)
- `generator/generate_library.py` - Production generator, uses requests.get
- `generator/common.py` - Shared utilities

### Integration Tests
- `tests/integration/conftest.py` - Test ordering and CLI options (--apikey, --o)
- `tests/integration/test_client_crud_lifecycle_sync.py` - Sync CRUD lifecycle
- `tests/integration/test_client_crud_lifecycle_async.py` - Async CRUD lifecycle
- `tests/integration/test_org_wide_workflows.py` - Org-wide workflows
- `tests/integration/test_iterator_sync.py` - Sync pagination iterator
- `tests/integration/test_iterator_async.py` - Async pagination iterator

### Config
- `pyproject.toml` - pytest config, dependencies, coverage settings

### Requirements
- `.planning/REQUIREMENTS.md` - DEP-02, TEST-02, TEST-03, TEST-04

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `respx` already in dev dependencies and used in `test_mock_integration.py`
- `_mock_response()` factory in `test_rest_session.py` already creates httpx.Response mocks
- `tests/integration/baseline/report.json` has pre-migration timing + pass/fail data

### Established Patterns
- Unit tests: `MagicMock(spec=httpx.Response)` with manual attribute setup
- Mock integration: `respx.mock(assert_all_mocked=False)` context manager with `httpx.Response()` return values
- Async tests: `pytest.mark.asyncio` with `AsyncMock` for client methods
- Fixtures: function-scoped, patch at `meraki.session.base.check_python_version`

### Integration Points
- CI workflow needs API key secret configuration
- `pyproject.toml` [tool.pytest.ini_options] for test paths and markers
- Coverage config excludes generated files (`meraki/api/*`, `meraki/aio/api/*`)

</code_context>

<specifics>
## Specific Ideas

- Baseline report at `tests/integration/baseline/report.json` is the "before" reference for regression gate
- requests dependency should be fully removed (not just from runtime, but from dev deps too after generator migration)
- Python 3.14 in matrix means ensuring httpx/respx support it (may need version bumps)

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within phase scope.

</deferred>

---

*Phase: 13-test-infrastructure*
*Context gathered: 2026-05-05*
