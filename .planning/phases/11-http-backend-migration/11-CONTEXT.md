# Phase 11: HTTP Backend Migration - Context

**Gathered:** 2026-05-04
**Status:** Ready for planning

<domain>
## Phase Boundary

SDK uses httpx.Client and httpx.AsyncClient for all HTTP requests. Removes runtime dependency on requests and aiohttp. The session base class template-method pattern (from Phase 10) stays intact; only the transport-specific subclass implementations change.

</domain>

<decisions>
## Implementation Decisions

### AsyncAPIError Transition
- **D-01:** Update AsyncAPIError in place to use httpx response attributes (status_code, reason_phrase) rather than adding a shim. Phase 12 then makes it a subclass of APIError as a clean second step.

### Concurrency Control
- **D-02:** Remove asyncio.Semaphore from AsyncRestSession. Use httpx.AsyncClient pool limits (max_connections=AIO_MAXIMUM_CONCURRENT_REQUESTS) instead. Update config.py accordingly so the constant name/docs reflect pool-based concurrency.

### Exception Handling
- **D-03:** Catch httpx.HTTPError as the single typed exception for all transport failures (connect, timeout, protocol). Re-raise as APIError with context. No finer-grained splits needed.

### Response Compatibility
- **D-04:** Accept the breaking change: `.reason` becomes `.reason_phrase` on httpx.Response. APIError.__init__ updated to read reason_phrase. Document this and all other breaking changes in HTTPX-MIGRATION.md under a "Breaking Changes" section with context and resolution steps.

### Dependencies
- **D-05:** pyproject.toml updated: remove `requests` and `aiohttp` from dependencies, add `httpx>=0.28,<1`.
- **D-06:** `requests_proxy` param continues to work by passing through as `proxy=` kwarg to httpx client.

### Code Cleanup
- **D-07:** Delete old `encode_params` from rest_session.py (Phase 9 D-06 transition bridge complete).
- **D-08:** Remove `allow_redirects=False` kwarg (httpx uses `follow_redirects` instead; base class already handles redirects manually).

### Claude's Discretion
- Whether to configure httpx.Client/AsyncClient at __init__ time (persistent client) or per-request
- Exact httpx timeout configuration (httpx.Timeout vs plain float)
- Whether `_transport_kwargs()` still exists or merges into client config since httpx handles verify/proxy/timeout at client level
- How to handle aiohttp-specific content_type=None in json() calls (httpx doesn't need it)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Session Implementation (Phase 10 output)
- `meraki/session/base.py` - SessionBase ABC with retry loop, status dispatch, template methods
- `meraki/session/sync.py` - RestSession (requests-based transport)
- `meraki/session/async_.py` - AsyncRestSession (aiohttp-based transport)
- `meraki/session/__init__.py` - Package exports

### Error Handling
- `meraki/exceptions.py` - APIError (uses .status_code, .reason), AsyncAPIError (uses .status, .reason)

### Config
- `meraki/config.py` - AIO_MAXIMUM_CONCURRENT_REQUESTS and all session defaults
- `pyproject.toml` - Current dependencies (requests, aiohttp)

### Encoding (Phase 9)
- `meraki/encoding.py` - Pure param encoder (stdlib only, kept)
- `meraki/rest_session.py` lines 41-107 - Old encode_params to be deleted (if file still exists)

### Migration Doc
- `.planning/HTTPX-MIGRATION.md` - Overall migration plan (if exists)

### Requirements
- `.planning/REQUIREMENTS.md` - HTTP-01, HTTP-02, ERR-01, ERR-03, DEP-01, DEP-03

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `SessionBase` template-method pattern: _send_request, _sleep, _transport_kwargs already abstracted
- `meraki/encoding.py`: Pure stdlib encoder, no changes needed
- `meraki/response_handler.py`: handle_3xx works with any response that has .headers["Location"]
- `meraki/common.py`: validate_base_url, validate_user_agent are transport-agnostic

### Established Patterns
- Sync session: persistent `requests.Session()` in __init__; same pattern maps to `httpx.Client()`
- Async session: `aiohttp.ClientSession()` in __init__; maps to `httpx.AsyncClient()`
- Both use `_transport_kwargs()` to inject verify/proxy/timeout; httpx handles these at client level instead
- Pagination uses `response.links` (same attribute name in httpx)
- Async session uses `response.status` (aiohttp); httpx uses `response.status_code` (same as requests)

### Integration Points
- Generated SDK modules import from `meraki.session.sync` and `meraki.session.async_`
- `meraki/__init__.py` / `meraki/aio/__init__.py` instantiate sessions
- Test mocks currently patch requests/aiohttp (Phase 13 migrates to respx)

</code_context>

<specifics>
## Specific Ideas

- Breaking changes section in HTTPX-MIGRATION.md should include: the change, why it happened, and exact code fix users need (e.g., `error.reason` -> `error.reason_phrase`)
- config.py constant update should preserve backwards compat for the name (AIO_MAXIMUM_CONCURRENT_REQUESTS can stay, or alias)

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within phase scope.

</deferred>

---

*Phase: 11-http-backend-migration*
*Context gathered: 2026-05-04*
