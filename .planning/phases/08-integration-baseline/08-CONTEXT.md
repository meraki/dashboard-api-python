# Phase 8: Integration Baseline - Context

**Gathered:** 2026-05-01
**Status:** Ready for planning

<domain>
## Phase Boundary

Record passing integration test state before any HTTP changes. This establishes the regression gate that Phase 13 will validate against after the httpx migration.

</domain>

<decisions>
## Implementation Decisions

### Baseline Format
- **D-01:** Use pytest-json-report to produce machine-readable pass/fail per test
- **D-02:** Include timing data (test durations) for Phase 13 performance comparison
- **D-03:** Store report in `tests/integration/baseline/` (survives .planning/ cleanup, easy Phase 13 reference)

### Test Scope
- **D-04:** Run only `tests/integration/` (5 files: CRUD lifecycle sync/async, org-wide workflows, iterators sync/async)
- **D-05:** Update `conftest.py` FILE_ORDER to match actual filenames on disk (currently references non-existent pagination files)

### Failure Policy
- **D-06:** Document current pass/fail state as-is (known failures tagged, not fixed)
- **D-07:** Regression gate for Phase 13 = "same or better" (no new failures allowed, new passes OK)

### Claude's Discretion
- Exact pytest-json-report flags and output filename
- Whether to add a README in the baseline directory explaining the artifact
- How to tag known failures in the report (markers vs separate list)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Test Infrastructure
- `tests/integration/conftest.py` - Fixture definitions, FILE_ORDER, pytest_addoption for --apikey/--o
- `tests/integration/test_client_crud_lifecycle_sync.py` - Sync CRUD test patterns
- `tests/integration/test_client_crud_lifecycle_async.py` - Async CRUD test patterns
- `tests/integration/test_org_wide_workflows.py` - Org-wide workflow tests
- `tests/integration/test_iterator_sync.py` - Sync pagination iterator tests
- `tests/integration/test_iterator_async.py` - Async pagination iterator tests

### Project Context
- `.planning/codebase/TESTING.md` - Testing patterns and conventions
- `.planning/REQUIREMENTS.md` - TEST-01 requirement definition

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `tests/integration/conftest.py`: shared fixtures (api_key, org_id), file ordering logic
- All 5 integration test files already exist and are structured with pytest conventions

### Established Patterns
- Integration tests use `--apikey` and `--o` CLI options for credentials
- Session-scoped fixtures for dashboard client and network setup
- FILE_ORDER in conftest controls execution sequence

### Integration Points
- `pyproject.toml` pytest config (may need pytest-json-report added to dev deps)
- `tests/integration/baseline/` directory (new, will hold report artifact)

</code_context>

<specifics>
## Specific Ideas

No specific requirements. Open to standard approaches for report generation and storage.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within phase scope.

</deferred>

---

*Phase: 08-integration-baseline*
*Context gathered: 2026-05-01*
