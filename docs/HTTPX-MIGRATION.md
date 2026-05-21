# HTTPX Migration Plan

## Why Migrate?

### The core problem: two libraries, one SDK

This library maintains two HTTP backends (`requests` for sync, `aiohttp` for async) with ~80% duplicated logic across `rest_session.py` (670 lines) and `aio/rest_session.py` (547 lines). This duplication is the root cause of multiple concerns documented in `.planning/codebase/CONCERNS.md`:

**Tech debt it directly eliminates:**

- Sync/async code duplication (bugs must be fixed twice, inconsistencies accumulate)
- High cyclomatic complexity in `AsyncRestSession._request` (42), which exists partly because async required a full reimplementation
- Two pinned dependencies at risk of breaking changes (`requests<3`, `aiohttp<4`)

**Bugs it fixes by replacement:**

- Bare `except Exception` in async handler (replaces with typed `httpx.HTTPError`)
- Inconsistent error handling between sync (catches `requests.exceptions.RequestException`) and async (catches everything)
- Blocking `time.sleep()` call in async 4xx handler (`aio/rest_session.py:268`), which blocks the event loop during network-delete retry waits

**Quality gaps it creates the opportunity to close:**

- No type annotations in core modules (rewrite is the natural time to add them)
- Missing error path test coverage (new code gets new tests)
- Test mocking uses `responses` library (requests-only); migration to `respx` modernizes the test infra

### Why httpx specifically?

- Provides `httpx.Client` (sync) and `httpx.AsyncClient` (async) with an identical API surface
- After `await client.request()`, response body is already buffered; `.json()` is synchronous even on the async client (simplifies pagination logic)
- Same `verify=`, `timeout=` semantics as requests (minimal learning curve for contributors)
- `proxy=` as a simple string (matches current config model)
- `response.links` property parses Link headers identically to requests (same `{'next': {'url': '...'}}` dict format)
- Actively maintained, type-annotated from the start, HTTP/2 capable
- Industry momentum: FastAPI, Starlette, and most modern Python HTTP tooling default to or recommend httpx

### What it does NOT solve

These concerns remain and require separate work:

- Adaptive retry strategy (app logic, not library choice)
- Pagination memory buffering (iterator pattern already exists)
- API key exposure risk (logging concern, unrelated to transport)
- OASv3 generator migration
- Request cancellation/OpenTelemetry integration (httpx has better primitives, but wiring them up is separate scope)

---

## Phase 0: Integration Test Baseline

Before touching HTTP code, capture a passing integration test run against the Meraki sandbox. This becomes the regression gate for all subsequent phases.

- Run existing integration tests, record pass/fail state
- Document which endpoints are exercised
- This baseline validates that Phases 2-3 produce identical external behavior

---

## Phase 1: Shared Utilities (additive, no breaking changes)

**Create `meraki/http_utils.py`** with one library-agnostic function:

### `encode_meraki_params(data) -> str | None`

Replaces the monkey-patched `requests.models.RequestEncodingMixin._encode_params` (rest_session.py:41-107). Reimplements the custom array-of-objects encoding as a pure function using only `urllib.parse.urlencode`.

Strategy: pre-encode params into a query string and append to the URL before passing to httpx (httpx has no monkey-patch hook for param encoding).

Current behavior:
- Input: `{"param[]": [{"key_1": "value_1"}]}`
- Output: `param%5B%5Dkey_1=value_1`

The existing impl uses `requests.utils.to_key_val_list` (just `.items()` on dicts) and `requests.compat.basestring` (just `str` in Python 3). Both are trivially replaceable.

Note: `response.links` does NOT need a replacement utility. httpx provides `.links` with the same dict format as requests.

---

## Phase 2: Session Base Class

**Create `meraki/_session_base.py`** extracting shared logic from both session files:

- All configuration storage (api_key, base_url, timeouts, retries, proxy, cert)
- Header construction
- URL resolution and validation
- Retry decision logic (`_should_retry_4xx`, `_get_retry_wait`)
- Param encoding dispatch (`_apply_params` calls `encode_meraki_params`)

The two concrete session classes become thin I/O layers over this base.

**Design decision for sync/async split:** The base class holds all decision logic (should we retry? how long to wait? what error to raise?) but does NOT hold the retry loop itself, because the loop calls `time.sleep()` (sync) vs `await asyncio.sleep()` (async). Each concrete class implements `_execute_with_retry` using the base's decision methods. This keeps the base simple and avoids abstract-method overhead.

---

## Phase 3: Rewrite Sync Session

**Rewrite `meraki/rest_session.py`** to use `httpx.Client`:

| requests | httpx |
|----------|-------|
| `requests.session()` | `httpx.Client(headers=..., verify=..., proxy=..., timeout=..., follow_redirects=False)` |
| `session.request(method, url, allow_redirects=False, **kwargs)` | `self._client.request(method, url, **kwargs)` |
| `requests.exceptions.RequestException` | `httpx.HTTPError` |
| `response.reason` | `response.reason_phrase` |
| `response.links` | `response.links` (same API) |
| `verify=path` | `verify=path` (same) |
| `proxies={"https": url}` | `proxy=url` |
| `timeout=60` | `timeout=60` (same) |

Key: params are pre-encoded into the URL via `_apply_params()`, so httpx never sees `params=`.

**Important:** Remove the monkey-patch (`requests.models.RequestEncodingMixin._encode_params = encode_params` at line 107) in this same phase. If requests remains importable (e.g., generator scripts), the monkey-patch must not fire at SDK import time.

---

## Phase 4: Rewrite Async Session

**Rewrite `meraki/aio/rest_session.py`** to use `httpx.AsyncClient`:

| aiohttp | httpx |
|---------|-------|
| `aiohttp.ClientSession(headers=..., timeout=aiohttp.ClientTimeout(...))` | `httpx.AsyncClient(headers=..., verify=..., proxy=..., timeout=..., follow_redirects=False)` |
| `response.status` | `response.status_code` |
| `await response.json(content_type=None)` | `response.json()` (sync after await on request) |
| `ssl=ssl_context` | `verify=path` (httpx handles SSLContext internally) |
| `proxy=url` (singular) | `proxy=url` (same) |
| `response.release()` | (delete, body already buffered) |
| `async with await self.request(...) as response:` | `response = await self.request(...)` |
| `response.links` | `response.links` (same API) |

**Structural changes beyond the table:**

- All 6 `async with await self.request(...) as response:` patterns (get, post, put, delete, _get_pages_legacy x2) become simple assignment. This is a pervasive rewrite, not a find-replace.
- `response.release()` calls in the async iterator are deleted (httpx buffers fully on await).
- `content_type=None` in `response.json()` calls (~10 occurrences) is dropped silently; httpx doesn't validate MIME type by default.

The `asyncio.Semaphore` for concurrency control and `asyncio.create_task` for page pre-fetching remain unchanged.

---

## Phase 5: Update Exceptions

**Modify `meraki/exceptions.py`:**

Current state:
- `APIError.__init__(metadata, response)` uses `response.status_code`, `response.reason`
- `AsyncAPIError.__init__(metadata, response, message)` uses `response.status`, `response.reason`, separate `message` param

These have **different signatures and different attribute sources**. Unifying requires:

1. Change `APIError`:
   - `response.reason` -> `response.reason_phrase`
   - `response.content` -> `response.content` (same in httpx)

2. Change `AsyncAPIError`:
   - `response.status` -> `response.status_code`
   - `response.reason` -> `response.reason_phrase`

3. Deprecation path for `AsyncAPIError`:
   - Keep the class but make it a subclass of `APIError` with a compatibility `__init__` that accepts the old 3-arg signature
   - Add a deprecation warning when instantiated directly
   - Document in CHANGELOG that users should catch `APIError` for both sync and async in future versions

---

## Deprecated: AsyncAPIError

**Status:** Deprecated as of v4.0. Use `APIError` for both sync and async exceptions.

### What Changed

In previous versions, the SDK used two separate exception classes:
- `APIError` for synchronous errors
- `AsyncAPIError` for asynchronous errors

Starting in v4.0, both sync and async sessions raise exceptions that inherit from `APIError`. The `AsyncAPIError` class remains available for backwards compatibility but is deprecated.

### Migration

**Before (v3.x):**
```python
from meraki.aio import AsyncDashboardAPI
from meraki.exceptions import AsyncAPIError

async with AsyncDashboardAPI(api_key=API_KEY) as aiomeraki:
    try:
        response = await aiomeraki.organizations.getOrganizations()
    except AsyncAPIError as e:
        print(f"Error: {e.status} {e.reason}")
```

**After (v4.0+):**
```python
from meraki.aio import AsyncDashboardAPI
from meraki.exceptions import APIError  # Changed

async with AsyncDashboardAPI(api_key=API_KEY) as aiomeraki:
    try:
        response = await aiomeraki.organizations.getOrganizations()
    except APIError as e:  # Changed
        print(f"Error: {e.status} {e.reason}")
```

### Backwards Compatibility

Existing code using `except AsyncAPIError:` will continue to work because `AsyncAPIError` is now a subclass of `APIError`. However, you will see a `DeprecationWarning` when the exception is raised.

To suppress the warning during migration:
```python
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning, module='meraki')
```

### Recommended Action

Update exception handlers to catch `APIError` instead of `AsyncAPIError`. This future-proofs your code and eliminates deprecation warnings.

---

## Phase 6: Update Dependencies

**Modify `pyproject.toml`:**

```toml
dependencies = [
    "httpx>=0.28,<1",
]

[dependency-groups]
dev = [
    "respx>=0.22,<1",        # replaces 'responses'
    # ... rest unchanged
]
```

Remove: `requests`, `aiohttp`, `responses`

Note on upper pin: `<1` guards against httpx 1.0 API breaks (they've discussed backwards-incompatible changes for 1.0). Re-evaluate when 1.0 ships.

**This phase MUST be atomic with Phases 3-4.** If `requests` remains installed while the new code is live, the old monkey-patch import path could still fire from stale .pyc caches or editable installs.

---

## Phase 7: Update Tests

| Test file | Change |
|-----------|--------|
| `tests/unit/test_rest_session.py` | Mock `httpx.Response` instead of `requests.Response`; `.reason` -> `.reason_phrase`; `.links` remains same API |
| `tests/unit/test_aio_rest_session.py` | Replace aiohttp mocks with httpx mocks; `.status` -> `.status_code`; remove `__aenter__`/`__aexit__` patterns; `.json()` no longer awaitable |
| `tests/unit/test_mock_integration.py` | Replace `responses` library with `respx` |
| Integration tests | Re-run baseline from Phase 0, confirm identical pass/fail |

---

## Phase 8: Backwards Compatibility

| Concern | Resolution |
|---------|------------|
| `requests_proxy` parameter name | Keep it. Pass through as `proxy=` internally. |
| `REQUESTS_PROXY` config constant | Keep it. Just a default value string. |
| `AsyncAPIError` class | Keep as deprecated subclass of `APIError`. |
| `_req_session` internal attribute | Add deprecation property mapping to `_client`. |

---

## Phase 9: Decompose Request Logic

The current `AsyncRestSession._request` has complexity 40 (4x industry ceiling). During rewrite, decompose into:

| Method | Responsibility |
|--------|---------------|
| `_execute_with_retry` | Retry loop, attempt counting, backoff timing |
| `_handle_rate_limit` | 429 detection, Retry-After parsing, wait logic |
| `_handle_error_response` | 4xx/5xx classification, exception raising |
| `_log_request` | Request/response debug logging |

Each method stays under complexity 10. Decision logic lives in the base class; sync/async layers differ only in sleep/request calls.

---

## Phase 10: Type Annotations

Type-annotate the new unified session base class and both thin I/O layers. This is the natural place to introduce typing since the code is being rewritten anyway, and the shared base class gives ~80% coverage for free.

- All public methods get full signatures (params and return types)
- Use `httpx.Response` directly (no wrapper)
- Add `py.typed` marker (PEP 561) in the same commit

---

## Phase 11: Property-Based Tests

Add `hypothesis` property-based tests for the param encoding utility:

| Function | Properties to verify |
|----------|---------------------|
| `encode_meraki_params` | Roundtrip: parsed output matches input structure; never produces bare `=` without key; handles empty dicts/lists; output is valid URL query string |

Add `hypothesis` to dev dependencies in `pyproject.toml`.

---

## Phase 12: Generator Scripts (optional, low priority)

`generator/generate_library.py` and siblings use `requests.get()` at build-time to fetch OpenAPI specs. Not shipped to users. Can migrate separately or leave as dev-only dependency.

---

## TODO.md Items Made Obsolete

These items from TODO.md are eliminated or simplified by this migration:

- **Stream 1, Step 3** (Eliminate sync/async duplication) - obsolete
- **Stream 1, Step 1** (Async `_request` complexity 42) - rewrite > refactor
- **Stream 1, Step 2** (`_get_pages_legacy` complexity) - rewrite > refactor
- **Stream 3** (Cover 36 missing lines) - those lines get replaced
- **Add integration test for async client** - one client = one test surface

---

## Risk Mitigation

- httpx sync responses are fully buffered (like requests). No behavior change.
- httpx async responses: body already read after `await client.request()`. Simplifies async code.
- Connection pooling: `Client`/`AsyncClient` maintain pools like `requests.Session`.
- Timeout: httpx default is 5s, but SDK explicitly sets 60s. No issue.
- Certificate verification: `verify="/path/to/cert.pem"` works identically.
- Proxy: `proxy="http://host:port"` as string. Direct pass-through.
- Monkey-patch removal: must happen atomically with requests removal to avoid import-time side effects on other packages.

---

## Execution Order

| Step | Risk | Validation |
|------|------|------------|
| Phase 0 (integration baseline) | None | Record current pass/fail state |
| Phase 1 (utilities) | None | Unit tests for encode function |
| Phase 2 (base class) | None | Unit tests for shared logic |
| Phase 3 (sync rewrite) | **High** | Full sync test suite passes |
| Phase 4 (async rewrite) | **High** | Full async test suite passes |
| Phase 5 (exceptions) | Medium | Error formatting matches expected output |
| Phase 6 (dependencies) | Medium | `pip install -e .` succeeds; atomic with 3-4 |
| Phase 7 (tests) | Medium | All tests green |
| Phase 8 (compat) | Low | Existing user code still works |
| Phase 9 (decompose) | Low | Complexity scores under 10 per method |
| Phase 10 (types) | Low | mypy passes |
| Phase 11 (property tests) | Low | hypothesis finds no violations |
| Phase 12 (generator) | None | Optional, dev-only |
| Integration gate | **Critical** | Live API tests pass against Meraki sandbox |
