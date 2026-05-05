---
phase: 12-error-handling-deprecation
plan: 01
subsystem: exceptions
tags: [deprecation, backwards-compat, error-handling]
dependency_graph:
  requires: []
  provides: [AsyncAPIError-as-APIError-subclass, deprecation-warning-pattern]
  affects: [meraki/session/async_.py, meraki/aio/rest_session.py]
tech_stack:
  added: []
  patterns: [deprecated-subclass-with-dual-signature, warnings.warn-stacklevel-2]
key_files:
  created: []
  modified:
    - meraki/exceptions.py
    - tests/unit/test_exceptions.py
    - HTTPX-MIGRATION.md
decisions:
  - "Exception.__init__ called directly in 3-arg path to avoid triggering APIError's json extraction"
  - "warnings.warn fires on every instantiation (not import-time) per D-02"
metrics:
  duration: 151s
  completed: 2026-05-05T16:31:09Z
  tasks: 2
  files: 3
---

# Phase 12 Plan 01: AsyncAPIError Deprecation Summary

AsyncAPIError made a deprecated subclass of APIError with dual-signature __init__, DeprecationWarning on every instantiation, and migration docs in HTTPX-MIGRATION.md.

## Task Completion

| Task | Name | Type | Commit(s) | Key Files |
|------|------|------|-----------|-----------|
| 1 | TDD - AsyncAPIError subclass | tdd | c9a0eb3 (RED), d52f30b (GREEN) | meraki/exceptions.py, tests/unit/test_exceptions.py |
| 2 | Migration docs | auto | cc4f379 | HTTPX-MIGRATION.md |

## Implementation Details

### AsyncAPIError Refactoring

- Changed `class AsyncAPIError(Exception)` to `class AsyncAPIError(APIError)`
- Added `message=None` parameter for optional 3rd argument
- 3-arg path: replicates original logic, calls `Exception.__init__()` directly (avoids APIError's json extraction)
- 2-arg path: delegates to `super().__init__(metadata, response)` for full APIError behavior
- `warnings.warn()` with `stacklevel=2` fires on every instantiation

### Test Updates

- All 6 existing TestAsyncAPIError tests wrapped with `pytest.warns(DeprecationWarning)`
- 3 new tests: subclass check, warning message match, 2-arg delegation
- 25/25 tests passing

### Documentation

- New "Deprecated: AsyncAPIError" section in HTTPX-MIGRATION.md between Phase 5 and Phase 6
- Before/after migration examples
- Warning suppression pattern for users during transition

## Deviations from Plan

None - plan executed exactly as written.

## TDD Gate Compliance

- RED gate: c9a0eb3 (`test(12-01): add failing tests...`)
- GREEN gate: d52f30b (`feat(12-01): make AsyncAPIError a deprecated subclass...`)
- REFACTOR gate: not needed (implementation is minimal and clean)

## Verification Results

```
pytest tests/unit/test_exceptions.py -x  -> 25 passed
python -c "assert issubclass(AsyncAPIError, APIError)"  -> OK
DeprecationWarning emission  -> OK
grep "## Deprecated: AsyncAPIError" HTTPX-MIGRATION.md  -> found
```
