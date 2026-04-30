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

**Quality gaps it creates the opportunity to close:**

- No type annotations in core modules (rewrite is the natural time to add them)
- Missing error path test coverage (new code gets new tests)
- Test mocking uses `responses` library (requests-only); migration to `respx` modernizes the test infra

### Why httpx specifically?

- Provides `httpx.Client` (sync) and `httpx.AsyncClient` (async) with an identical API surface
- After `await client.request()`, response body is already buffered; `.json()` is synchronous even on the async client (simplifies pagination logic)
- Same `verify=`, `timeout=` semantics as requests (minimal learning curve for contributors)
- `proxy=` as a simple string (matches current config model)
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

## Phase 0: Shared Utilities (additive, no breaking changes)

**Create `meraki/http_utils.py`** with two library-agnostic functions:

### `encode_meraki_params(data) -> str | None`

Replaces the monkey-patched `requests.models.RequestEncodingMixin._encode_params` (rest_session.py:41-107). Reimplements the custom array-of-objects encoding as a pure function using only `urllib.parse.urlencode`.

Strategy: pre-encode params into a query string and append to the URL before passing to httpx (httpx has no monkey-patch hook for param encoding).

Current behavior:
- Input: `{"param[]": [{"key_1": "value_1"}]}`
- Output: `param%5B%5Dkey_1=value_1`

The existing impl uses `requests.utils.to_key_val_list` (just `.items()` on dicts) and `requests.compat.basestring` (just `str` in Python 3). Both are trivially replaceable.

### `parse_link_header(header_value: str | None) -> dict`

Replaces `response.links` (used in 5 pagination locations). httpx has no `.links` property.

Returns `{"next": {"url": "..."}, "prev": {"url": "..."}}` matching the requests format. Parses RFC 8288 `<URL>; rel="name"` comma-separated values.

---

## Phase 1: Session Base Class

**Create `meraki/_session_base.py`** extracting shared logic from both session files:

- All configuration storage (api_key, base_url, timeouts, retries, proxy, cert)
- Header construction
- URL resolution and validation
- Retry decision logic (`_should_retry_4xx`, `_get_retry_wait`)
- Param encoding dispatch (`_apply_params` calls `encode_meraki_params`)
- Link header parsing dispatch

The two concrete session classes become thin I/O layers over this base.

---

## Phase 2: Rewrite Sync Session

**Rewrite `meraki/rest_session.py`** to use `httpx.Client`:

| requests | httpx |
|----------|-------|
| `requests.session()` | `httpx.Client(headers=..., verify=..., proxy=..., timeout=..., follow_redirects=False)` |
| `session.request(method, url, allow_redirects=False, **kwargs)` | `self._client.request(method, url, **kwargs)` |
| `requests.exceptions.RequestException` | `httpx.HTTPError` |
| `response.reason` | `response.reason_phrase` |
| `response.links` | `parse_link_header(response.headers.get("link"))` |
| `verify=path` | `verify=path` (same) |
| `proxies={"https": url}` | `proxy=url` |
| `timeout=60` | `timeout=60` (same) |

Key: params are pre-encoded into the URL via `_apply_params()`, so httpx never sees `params=`.

---

## Phase 3: Rewrite Async Session

**Rewrite `meraki/aio/rest_session.py`** to use `httpx.AsyncClient`:

| aiohttp | httpx |
|---------|-------|
| `aiohttp.ClientSession(headers=..., timeout=aiohttp.ClientTimeout(...))` | `httpx.AsyncClient(headers=..., verify=..., proxy=..., timeout=..., follow_redirects=False)` |
| `response.status` | `response.status_code` |
| `await response.json(content_type=None)` | `response.json()` (sync after await on request) |
| `ssl=ssl_context` | `verify=path` (httpx handles SSLContext internally) |
| `proxy=url` (singular) | `proxy=url` (same) |
| `response.release()` | (not needed, body already buffered) |
| `async with await self.request(...) as response:` | `response = await self.request(...)` |

The `asyncio.Semaphore` for concurrency control and `asyncio.create_task` for page pre-fetching remain unchanged.

---

## Phase 4: Update Exceptions

**Modify `meraki/exceptions.py`:**

- `APIError.__init__`: change `response.reason` to `response.reason_phrase`
- `AsyncAPIError`: keep as alias of `APIError` for backwards compat (both now use `response.status_code`)
- `APIResponseError`: unchanged (wraps connection errors, not HTTP responses)

---

## Phase 5: Update Dependencies

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

---

## Phase 6: Update Tests

| Test file | Change |
|-----------|--------|
| `tests/unit/test_rest_session.py` | Mock `httpx.Response` instead of `requests.Response`; `.reason` -> `.reason_phrase`; `.links` -> link header in `response.headers` |
| `tests/unit/test_aio_rest_session.py` | Replace aiohttp mocks with httpx mocks; `.status` -> `.status_code`; remove `__aenter__`/`__aexit__` patterns; `.json()` no longer awaitable |
| `tests/unit/test_mock_integration.py` | Replace `responses` library with `respx` |
| Integration tests | No changes (test high-level API, not HTTP layer) |

---

## Phase 7: Backwards Compatibility

| Concern | Resolution |
|---------|------------|
| `requests_proxy` parameter name | Keep it. Pass through as `proxy=` internally. |
| `REQUESTS_PROXY` config constant | Keep it. Just a default value string. |
| `AsyncAPIError` class | Keep as alias of `APIError`. |
| `_req_session` internal attribute | Add deprecation property mapping to `_client`. |

---

## Phase 8: Generator Scripts (optional, low priority)

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

## Phase 2a: Type Annotations

Type-annotate the new unified session base class and both thin I/O layers. This is the natural place to introduce typing since the code is being rewritten anyway, and the shared base class gives ~80% coverage for free.

- All public methods get full signatures (params and return types)
- Use `httpx.Response` directly (no wrapper)
- Add `py.typed` marker (PEP 561) in the same commit

---

## Phase 2b: Decompose Request Logic

The current `AsyncRestSession._request` has complexity 40 (4x industry ceiling). During rewrite, decompose into:

| Method | Responsibility |
|--------|---------------|
| `_execute_with_retry` | Retry loop, attempt counting, backoff timing |
| `_handle_rate_limit` | 429 detection, Retry-After parsing, wait logic |
| `_handle_error_response` | 4xx/5xx classification, exception raising |
| `_log_request` | Request/response debug logging |

Each method stays under complexity 10. The base class holds the logic; sync/async layers only differ in `await`.

---

## Phase 6a: Property-Based Tests

Add `hypothesis` property-based tests for the two new utility functions:

| Function | Properties to verify |
|----------|---------------------|
| `encode_meraki_params` | Roundtrip: parsed output matches input structure; never produces bare `=` without key; handles empty dicts/lists; output is valid URL query string |
| `parse_link_header` | Roundtrip with generated Link headers; handles missing rel; handles multiple rels; empty input returns empty dict |

Add `hypothesis` to dev dependencies in `pyproject.toml`.

---

## Risk Mitigation

- httpx sync responses are fully buffered (like requests). No behavior change.
- httpx async responses: body already read after `await client.request()`. Simplifies async code.
- Connection pooling: `Client`/`AsyncClient` maintain pools like `requests.Session`.
- Timeout: httpx default is 5s, but SDK explicitly sets 60s. No issue.
- Certificate verification: `verify="/path/to/cert.pem"` works identically.
- Proxy: `proxy="http://host:port"` as string. Direct pass-through.

---

## Execution Order

| Step | Risk | Validation |
|------|------|------------|
| Phase 0 (utilities) | None | Unit tests for encode/parse functions |
| Phase 1 (base class) | None | Unit tests for shared logic |
| Phase 2 (sync rewrite) | **High** | Full sync test suite passes |
| Phase 3 (async rewrite) | **High** | Full async test suite passes |
| Phase 4 (exceptions) | Medium | Error formatting matches expected output |
| Phase 5 (dependencies) | Low | `pip install -e .` succeeds |
| Phase 6 (tests) | Medium | All tests green |
| Phase 7 (compat) | Low | Existing user code still works |
| Integration gate | **Critical** | Live API tests pass against Meraki sandbox |
