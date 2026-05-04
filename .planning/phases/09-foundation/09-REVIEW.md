---
phase: 09-foundation
reviewed: 2026-05-04T12:00:00Z
depth: standard
files_reviewed: 2
files_reviewed_list:
  - meraki/encoding.py
  - tests/unit/test_encoding.py
findings:
  critical: 1
  warning: 1
  info: 1
  total: 3
status: issues_found
---

# Phase 9: Code Review Report

**Reviewed:** 2026-05-04T12:00:00Z
**Depth:** standard
**Files Reviewed:** 2
**Status:** issues_found

## Summary

The encoding module is clean, focused, and well-tested. One crash bug exists when `None` appears in a list value (falls into dict-handling branch). One inconsistency in non-string key handling for array-of-objects. Test coverage is solid with property-based tests.

## Critical Issues

### CR-01: AttributeError crash when list contains None

**File:** `meraki/encoding.py:57`
**Issue:** When a list value contains `None`, the condition on line 49 (`v is not None and not isinstance(v, dict)`) evaluates to `False`, sending `None` into the `else` branch. Line 57 then calls `v.items()` on `None`, raising `AttributeError`.
**Fix:**
```python
for v in vs:
    if v is None:
        continue
    elif isinstance(v, dict):
        # Array-of-objects: concatenate dict keys to param name
        for k_inner, v_inner in v.items():
            result.append((
                (k + k_inner).encode("utf-8") if isinstance(k, str) else k_inner,
                v_inner.encode("utf-8") if isinstance(v_inner, str) else v_inner,
            ))
    else:
        # Simple key-value pair
        result.append((
            k.encode("utf-8") if isinstance(k, str) else k,
            v.encode("utf-8") if isinstance(v, str) else v,
        ))
```

## Warnings

### WR-01: Non-string key drops outer key in array-of-objects branch

**File:** `meraki/encoding.py:59`
**Issue:** When `k` is not a `str` (e.g., `bytes`), the ternary uses `k_inner` alone as the composite key, discarding the outer key `k`. The `str` branch correctly concatenates `k + k_inner`. This means bytes keys lose their prefix in array-of-objects encoding.
**Fix:**
```python
(k + k_inner.encode("utf-8") if isinstance(k, bytes) else (k + k_inner).encode("utf-8")) if isinstance(k, (str, bytes)) else k_inner,
```
Or more readably, handle concatenation for bytes keys:
```python
if isinstance(k, str):
    composite = (k + k_inner).encode("utf-8")
elif isinstance(k, bytes):
    composite = k + (k_inner.encode("utf-8") if isinstance(k_inner, str) else k_inner)
else:
    composite = k_inner
```

## Info

### IN-01: No test coverage for None-in-list edge case

**File:** `tests/unit/test_encoding.py`
**Issue:** No test exercises the `None` value path (e.g., `{"key": [None, "val"]}`). This is the path that triggers CR-01.
**Fix:** Add a test:
```python
def test_none_in_list_skipped(self):
    result = encode_meraki_params({"key": [None, "val"]})
    assert "key=val" in result
```

---

_Reviewed: 2026-05-04T12:00:00Z_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
