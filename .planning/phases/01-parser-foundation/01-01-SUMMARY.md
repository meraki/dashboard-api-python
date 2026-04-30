---
phase: 01-parser-foundation
plan: 01
subsystem: parser
tags: [tdd, v3-parser, ref-resolution]
dependencies:
  requires: []
  provides: [resolve_ref, clear_cache, _ref_cache]
  affects: []
tech_stack:
  added: [parser_v3.py]
  patterns: [module-level caching, visited-set cycle detection, RFC 6901 escaping]
key_files:
  created:
    - generator/parser_v3.py
    - tests/generator/test_parser_v3.py
    - tests/generator/fixtures/synthetic_v3_spec.json
  modified: []
decisions:
  - "Module-level cache (_ref_cache) over class-based: matches v2 generator pattern"
  - "Empty dict {} as circular ref sentinel: distinguishes from None, fails gracefully"
  - "External ref rejection: security + simplicity (no filesystem traversal)"
metrics:
  duration: 9
  tasks_completed: 2
  tasks_total: 2
  completed_date: "2026-04-30"
---

# Phase 01 Plan 01: $ref Resolution Foundation

**One-liner:** Module-level cached $ref resolution with visited-set cycle detection and RFC 6901 escaping.

## Objective

Implement `resolve_ref` and `clear_cache` in `generator/parser_v3.py` following TDD. Foundation for all v3 parsing; downstream `parse_request_body` (Plan 02) depends on this for schema resolution.

## Execution Summary

Both tasks completed following RED-GREEN TDD cycle.

**Task 1 (RED):** Created synthetic v3 fixture with $ref, requestBody, multipart, octet-stream examples. Created test scaffold with 10 tests covering basic resolution, caching, cycle detection, escaping, and error cases. Tests failed with ModuleNotFoundError as expected.

**Task 2 (GREEN):** Implemented `parser_v3.py` with module-level `_ref_cache`, `clear_cache()`, and `resolve_ref()`. All 10 tests passed. No regressions in existing generator tests (41 tests total).

## Deviations from Plan

None. Plan executed exactly as written.

## Verification Results

**Primary verification (plan success criteria):**
```bash
cd C:/Users/jkuchta/Work/_Repos/meraki/dashboard-api-python
python -m pytest tests/generator/test_parser_v3.py -v
```
Result: ✓ All 10 tests passed in 0.02s

**Regression check:**
```bash
python -m pytest tests/generator/ -v
```
Result: ✓ All 41 tests passed in 1.14s (31 existing + 10 new)

## Key Implementation Details

### resolve_ref Behavior

- **Caching (D-01):** First call resolves and caches. Second call returns cached object (identity check passes).
- **Cycle detection (D-02):** Visited set tracks pointers in resolution chain. Circular refs return `{}` sentinel.
- **Error handling (D-03):** External refs raise `ValueError`. Unresolvable pointers raise `KeyError`.
- **RFC 6901 escaping:** `~0` → `~`, `~1` → `/` per spec.
- **Recursive resolution:** If resolved value contains nested `$ref`, recursively resolves.

### Module Structure

```python
_ref_cache: dict[str, dict] = {}  # Module-level state

def clear_cache() -> None:
    """Call at generator entry point."""

def resolve_ref(spec: dict, ref: str, _visited: set | None = None) -> dict:
    """Resolve JSON pointer with caching and cycle detection."""
```

Matches v2 generator pattern: module-level functions, spec passed as arg.

## Threat Surface Scan

No new security-relevant surface beyond plan's threat model. All four threats (T-01-01 through T-01-04) mitigated as specified.

## Known Stubs

None. Implementation complete per requirements.

## Self-Check

**Created files exist:**
- ✓ `generator/parser_v3.py` (73 lines)
- ✓ `tests/generator/test_parser_v3.py` (76 lines)
- ✓ `tests/generator/fixtures/synthetic_v3_spec.json` (116 lines)

**Commits exist:**
- ✓ e20f9a3: test(01-01): add failing test for resolve_ref and clear_cache
- ✓ f6a1a89: feat(01-01): implement resolve_ref and clear_cache

**Self-Check: PASSED**

## Next Steps

This plan provides the foundation for Plan 02 (parse_request_body). The `resolve_ref` function will be called during requestBody parsing to resolve schema `$ref` pointers into concrete param dicts.
