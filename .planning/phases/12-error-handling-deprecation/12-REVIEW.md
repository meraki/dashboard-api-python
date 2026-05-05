---
phase: 12-error-handling-deprecation
reviewed: 2026-05-05T12:00:00Z
depth: standard
files_reviewed: 3
files_reviewed_list:
  - meraki/exceptions.py
  - tests/unit/test_exceptions.py
  - HTTPX-MIGRATION.md
findings:
  critical: 0
  warning: 4
  info: 1
  total: 5
status: issues_found
---

# Phase 12: Code Review Report

**Reviewed:** 2026-05-05T12:00:00Z
**Depth:** standard
**Files Reviewed:** 3
**Status:** issues_found

## Summary

Reviewed the exception hierarchy (`meraki/exceptions.py`), its unit tests, and the migration plan doc. The deprecation pattern for `AsyncAPIError` is well-designed (subclass + warning). However, there are several logic bugs in `APIError.__init__` that produce incorrect behavior for edge cases, including falsy JSON bodies and missing whitespace in user-facing messages.

## Warnings

### WR-01: Falsy JSON body incorrectly treated as None

**File:** `meraki/exceptions.py:44`
**Issue:** The condition `self.response.json()` uses truthiness to decide whether to assign the message. If the API returns a valid but falsy JSON body (`{}`, `[]`, `0`, `""`, `false`), `self.message` is set to `None` instead of the actual response body. Additionally, `.json()` is called twice (once for the check, once for assignment), doubling parse cost.
**Fix:**
```python
json_body = self.response.json()
self.message = json_body if json_body is not None else None
```
Or simpler, since `json()` raises `ValueError` on non-JSON, just assign directly:
```python
self.message = self.response.json()
```

### WR-02: Falsy status_code (e.g. 0) incorrectly treated as None

**File:** `meraki/exceptions.py:41`
**Issue:** The condition `self.response.status_code` uses truthiness. A status code of `0` (which some mock/proxy responses produce) would be treated as `None`. Should use explicit `is not None` check.
**Fix:**
```python
self.status = self.response.status_code if self.response is not None else None
```

### WR-03: Missing space before "please wait" message

**File:** `meraki/exceptions.py:48`
**Issue:** String concatenation `self.message += "please wait..."` produces output like `"Not found hereplease wait a minute..."` with no separator. Same bug on line 85 in `AsyncAPIError`.
**Fix:**
```python
self.message += " please wait a minute if the key or org was just newly created."
```
Apply the same fix at line 85.

### WR-04: UnicodeDecodeError not handled in content fallback

**File:** `meraki/exceptions.py:46`
**Issue:** When JSON parsing fails, the code does `self.response.content[:100].decode("UTF-8")`. If the response body contains non-UTF-8 bytes (e.g., binary error pages from proxies), this raises `UnicodeDecodeError` which escapes the `except ValueError` block and crashes the exception constructor.
**Fix:**
```python
self.message = self.response.content[:100].decode("UTF-8", errors="replace").strip()
```

## Info

### IN-01: Test documents bug rather than correct behavior

**File:** `tests/unit/test_exceptions.py:222-223`
**Issue:** `test_none_doc_link` asserts that `"None"` (the string) appears in the exception message when `doc_link=None` is passed. This documents a UX issue where users see the literal word "None" in error messages. Consider handling `None` doc_link in `SessionInputError.__init__`.
**Fix:**
```python
# In SessionInputError.__init__:
parts = [self.message]
if self.doc_link:
    parts.append(self.doc_link)
super().__init__(" ".join(parts))
```

---

_Reviewed: 2026-05-05T12:00:00Z_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
