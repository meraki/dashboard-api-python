---
phase: 13-test-infrastructure
plan: 01
subsystem: generator, test-infrastructure
tags: [httpx-migration, dependency-upgrade, test-mocks]
dependency_graph:
  requires: []
  provides: [httpx-generator, respx-upgraded, pytest-benchmark]
  affects: [generator/generate_library.py, generator/generate_library_oasv2.py, generator/generate_snippets.py, tests/generator/]
tech_stack:
  added: [pytest-benchmark>=2.0.0]
  patterns: [httpx.Response mock objects, httpx.get patching]
key_files:
  created: []
  modified:
    - pyproject.toml
    - generator/generate_library.py
    - generator/generate_library_oasv2.py
    - generator/generate_snippets.py
    - tests/generator/test_generate_library_golden.py
    - tests/generator/test_generate_library_v3.py
    - tests/generator/test_golden_v3_output.py
decisions:
  - pytest-benchmark pinned >=2.0.0 (no versions exist between 1.5 and 2)
metrics:
  duration_seconds: 514
  completed: "2026-05-05T22:39:01Z"
  tasks_completed: 3
  tasks_total: 3
  files_modified: 7
---

# Phase 13 Plan 01: Generator httpx Migration Summary

Migrated generator scripts and tests from requests to httpx; upgraded respx to 0.23.1; added pytest-benchmark.

## Task Commits

| Task | Name | Commit | Key Files |
|------|------|--------|-----------|
| 1 | Upgrade respx, add pytest-benchmark | e5e1456 | pyproject.toml, uv.lock |
| 2 | Migrate generator scripts to httpx | 1d5c36e | generator/generate_library.py, generate_library_oasv2.py, generate_snippets.py |
| 3 | Migrate generator test mocks | 5f86e1d | tests/generator/test_generate_library_golden.py, test_generate_library_v3.py, test_golden_v3_output.py |

## Verification Results

- `grep -r "import requests" generator/` returns empty
- `grep -r "requests" tests/generator/ --include="*.py"` returns empty
- Golden tests pass (2/2)
- CLI tests pass (4/4)
- Unit tests pass (226/226)

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] pytest-benchmark version constraint**
- **Found during:** Task 1
- **Issue:** Plan specified `>=1.5.0,<2` but no such version exists (jumps from <1.5.0 to >=2.0.0)
- **Fix:** Changed to `>=2.0.0`
- **Files modified:** pyproject.toml
- **Commit:** e5e1456

**2. [Rule 1 - Bug] test_org_specific_fetch env var precedence**
- **Found during:** Task 3
- **Issue:** `MERAKI_DASHBOARD_API_KEY` env var in CI takes precedence over `-k` flag, causing test to assert wrong key
- **Fix:** Added `os.environ.pop("MERAKI_DASHBOARD_API_KEY", None)` inside `patch.dict` context
- **Files modified:** tests/generator/test_generate_library_v3.py
- **Commit:** 5f86e1d

**3. [Rule 2 - Missing] test_golden_v3_output.py not in plan**
- **Found during:** Task 3
- **Issue:** Plan only listed 2 test files but a 3rd (`test_golden_v3_output.py`) also used requests mocks
- **Fix:** Migrated it to httpx.Response mocks alongside the others
- **Files modified:** tests/generator/test_golden_v3_output.py
- **Commit:** 5f86e1d

## Deferred Issues

Pre-existing: `TestV3GeneratorOutput`, `TestV3Stubs`, and `TestGoldenSync/Async/Batch` tests fail with `FileNotFoundError: 'meraki/session/__init__.py'`. The `non_generated` file list in `generate_library.py` includes `session/` subdirectory files, but test fixtures don't create those directories in tmp_path. This predates the httpx migration and is unrelated to this plan.

## Self-Check: PASSED
