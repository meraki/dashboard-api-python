---
phase: 01-parser-foundation
reviewed: 2026-04-30T00:00:00Z
depth: standard
files_reviewed: 3
files_reviewed_list:
  - generator/parser_v3.py
  - tests/generator/test_parser_v3.py
  - tests/generator/fixtures/synthetic_v3_spec.json
findings:
  critical: 0
  warning: 1
  info: 1
  total: 2
status: issues_found
---

# Phase 01: Code Review Report

**Reviewed:** 2026-04-30T00:00:00Z
**Depth:** standard
**Files Reviewed:** 3
**Status:** issues_found

## Summary

Reviewed parser foundation implementation (resolve_ref, parse_request_body) with test coverage and synthetic fixture. Code quality is high. One warning (missing nested $ref resolution in array items) and one info item (direct cache import in tests couples to internals).

## Warnings

### WR-01: Array items with $ref not resolved

**File:** `generator/parser_v3.py:149-150`
**Issue:** When copying `items` from prop_schema to output, code doesn't check if items contains a `$ref` that needs resolution. If an array property has `"items": {"$ref": "#/components/schemas/SomeModel"}`, the unresolved reference gets passed downstream.

**Fix:**
```python
# Include array items if present
if prop_schema.get("type") == "array" and "items" in prop_schema:
    items = prop_schema["items"]
    if isinstance(items, dict) and "$ref" in items:
        items = resolve_ref(spec, items["$ref"])
    entry["items"] = items
```

## Info

### IN-01: Test imports internal cache directly

**File:** `tests/generator/test_parser_v3.py:5`
**Issue:** Test imports `_ref_cache` (module-level private cache) to verify caching behavior. This couples tests to internal implementation. If cache moves to different structure (e.g., LRU cache object), test breaks.

**Fix:** Consider exposing cache inspection via public function (e.g., `get_cache_keys()`) or accepting the coupling as reasonable for unit tests that verify caching behavior.

---

_Reviewed: 2026-04-30T00:00:00Z_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
