# Phase 12: Error Handling Deprecation - Context

**Gathered:** 2026-05-05
**Status:** Ready for planning

<domain>
## Phase Boundary

Unify exception handling: AsyncAPIError becomes a deprecated subclass of APIError with backwards-compatible signature. Users can catch `APIError` for both sync and async errors. No forced migration; existing `except AsyncAPIError` still works.

</domain>

<decisions>
## Implementation Decisions

### Signature Compatibility
- **D-01:** AsyncAPIError.__init__ accepts both signatures: `(metadata, response, message=None)`. If `message` is passed, use it directly; if not, fall through to APIError's `response.json()` extraction logic. Old 3-arg callers continue working without changes.

### Deprecation Mechanism
- **D-02:** `warnings.warn('AsyncAPIError is deprecated, catch APIError instead', DeprecationWarning, stacklevel=2)` fires on every instantiation of AsyncAPIError. No import-time or catch-time warnings.

### Async Session Raise Sites
- **D-03:** async_.py continues raising AsyncAPIError (now a subclass of APIError). Existing user catch blocks (`except AsyncAPIError`) keep working. Since it's a subclass, `except APIError` also catches it. Migration is optional, not forced.

### Migration Documentation
- **D-04:** HTTPX-MIGRATION.md gets a "Deprecated: AsyncAPIError" section with before/after code examples. AsyncAPIError class docstring points users to catch APIError instead.

### Claude's Discretion
- Whether to use `__init_subclass__` or simple inheritance
- Exact wording of deprecation warning message
- Whether to suppress repeated warnings via `warnings.simplefilter`

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Exception Classes
- `meraki/exceptions.py` - APIError (2-arg: metadata, response) and AsyncAPIError (3-arg: metadata, response, message)
- `meraki/__init__.py` lines 51, 61 - Public exports of both exception classes

### Async Session (raise sites)
- `meraki/session/async_.py` lines 157, 166, 173, 236, 288, 299, 310, 316 - All 8 AsyncAPIError raise sites

### Sync Session (reference for APIError usage)
- `meraki/session/base.py` lines 182-374 - APIError raise sites and httpx.HTTPError catch

### Tests
- `tests/unit/test_exceptions.py` - Existing tests for both APIError and AsyncAPIError

### Migration Doc
- `HTTPX-MIGRATION.md` - Breaking changes documentation (add deprecation section)

### Requirements
- `.planning/REQUIREMENTS.md` - ERR-02 (AsyncAPIError deprecated as subclass with compat __init__)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `APIError.__init__` already handles response.json() extraction with ValueError fallback
- Both classes share identical `__repr__` patterns and 404 "please wait" logic

### Established Patterns
- APIError: `(metadata, response)` - extracts message from response.json()
- AsyncAPIError: `(metadata, response, message)` - message passed explicitly by caller
- Sync base.py raises APIError directly; async_.py raises AsyncAPIError

### Integration Points
- `meraki/__init__.py` exports both in `__all__`
- `meraki/session/async_.py` imports both but only raises AsyncAPIError
- `tests/unit/test_exceptions.py` has full coverage of both classes
- User code catches `AsyncAPIError` in `except` blocks (public API contract)

</code_context>

<specifics>
## Specific Ideas

No specific requirements beyond standard approaches.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within phase scope.

</deferred>

---

*Phase: 12-error-handling-deprecation*
*Context gathered: 2026-05-05*
