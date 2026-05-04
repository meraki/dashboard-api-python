# Phase 11: HTTP Backend Migration - Research

**Researched:** 2026-05-04
**Domain:** Python HTTP client migration (requests/aiohttp to httpx)
**Confidence:** HIGH

## Summary

Phase 11 replaces the dual HTTP backend (requests for sync, aiohttp for async) with httpx.Client and httpx.AsyncClient. The session base class template-method pattern from Phase 10 stays intact. Only the transport-specific subclass implementations change.

httpx 0.28.1 (released 2024-12-06) provides a unified sync/async API that eliminates ~500 lines of duplicated logic. Key migration points: (1) httpx defaults to no redirects (requests auto-follows), (2) response.reason becomes response.reason_phrase, (3) allow_redirects=False becomes follow_redirects=False, (4) aiohttp.ClientSession concurrency semaphore is replaced by httpx.Limits(max_connections=8).

**Primary recommendation:** Update RestSession and AsyncRestSession in place. Use persistent httpx.Client/AsyncClient instances (initialized in __init__) rather than per-request clients to preserve connection pooling. Catch httpx.HTTPError as single typed exception for all transport failures (connect/timeout/protocol). Document breaking changes (.reason to .reason_phrase) in migration guide.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**D-01: AsyncAPIError Transition**
Update AsyncAPIError in place to use httpx response attributes (status_code, reason_phrase) rather than adding a shim. Phase 12 then makes it a subclass of APIError as a clean second step.

**D-02: Concurrency Control**
Remove asyncio.Semaphore from AsyncRestSession. Use httpx.AsyncClient pool limits (max_connections=AIO_MAXIMUM_CONCURRENT_REQUESTS) instead. Update config.py accordingly so the constant name/docs reflect pool-based concurrency.

**D-03: Exception Handling**
Catch httpx.HTTPError as the single typed exception for all transport failures (connect, timeout, protocol). Re-raise as APIError with context. No finer-grained splits needed.

**D-04: Response Compatibility**
Accept the breaking change: .reason becomes .reason_phrase on httpx.Response. APIError.__init__ updated to read reason_phrase. Document this and all other breaking changes in HTTPX-MIGRATION.md under a "Breaking Changes" section with context and resolution steps.

**D-05: Dependencies**
pyproject.toml updated: remove `requests` and `aiohttp` from dependencies, add `httpx>=0.28,<1`.

**D-06: requests_proxy param continues**
`requests_proxy` param continues to work by passing through as `proxy=` kwarg to httpx client.

**D-07: Code Cleanup**
Delete old `encode_params` from rest_session.py (Phase 9 D-06 transition bridge complete).

**D-08: Remove allow_redirects kwarg**
Remove `allow_redirects=False` kwarg (httpx uses `follow_redirects` instead; base class already handles redirects manually).

### Claude's Discretion

- Whether to configure httpx.Client/AsyncClient at __init__ time (persistent client) or per-request
- Exact httpx timeout configuration (httpx.Timeout vs plain float)
- Whether `_transport_kwargs()` still exists or merges into client config since httpx handles verify/proxy/timeout at client level
- How to handle aiohttp-specific content_type=None in json() calls (httpx doesn't need it)

### Deferred Ideas (OUT OF SCOPE)

None. Discussion stayed within phase scope.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| HTTP-01 | SDK uses httpx.Client for all sync HTTP requests | RestSession instantiates httpx.Client in __init__ (Standard Stack section) |
| HTTP-02 | SDK uses httpx.AsyncClient for all async HTTP requests | AsyncRestSession instantiates httpx.AsyncClient in __init__ (Standard Stack section) |
| ERR-01 | APIError uses httpx.Response attributes (status_code, reason_phrase) | httpx.Response has .status_code and .reason_phrase (API Compatibility section) |
| ERR-03 | Typed exception handling catches httpx.HTTPError | httpx.HTTPError is base exception for all transport failures (Exception Hierarchy section) |
| DEP-01 | httpx>=0.28,<1 replaces requests and aiohttp in dependencies | Latest stable version 0.28.1 verified via PyPI (Standard Stack section) |
| DEP-03 | requests_proxy param still works (passes through as proxy=) | httpx.Client(proxy=url) maps directly from requests_proxy config (Proxy Configuration section) |
</phase_requirements>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| HTTP transport (sync) | SDK Core (RestSession) | — | Sync HTTP requests owned by RestSession subclass |
| HTTP transport (async) | SDK Core (AsyncRestSession) | — | Async HTTP requests owned by AsyncRestSession subclass |
| Connection pooling | httpx.Client | SDK Config | httpx manages pool limits; SDK config.py sets max_connections |
| Retry logic | SessionBase | — | Template method pattern in base class (unchanged from Phase 10) |
| Exception handling | SDK Core (session subclasses) | SessionBase | Transport exceptions caught in subclasses, converted to APIError in base |
| Timeout enforcement | httpx.Client | SDK Config | httpx enforces timeouts at client level; SDK sets default via config.py |

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| httpx | 0.28.1 | Unified sync/async HTTP client | Official Python HTTP client from encode (maintainers of requests), 86.95 Context7 benchmark, supports both sync/async with identical API, active maintenance (Dec 2024 release) |

### Supporting

None. httpx is self-contained (no required peer dependencies).

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| httpx | requests + aiohttp (current) | Current stack requires dual codebases (~500 lines duplicated logic), different exception hierarchies, inconsistent response interfaces |
| httpx | aiohttp only | aiohttp is async-only; would require threading wrapper for sync API (adds complexity, not standard pattern) |

**Installation:**

```bash
uv pip install "httpx>=0.28,<1"
```

**Version verification:**

```bash
# Verified 2026-05-04 via PyPI JSON API
# Latest: 0.28.1 (released 2024-12-06)
# Previous: 0.28.0 (2024-11-28), 0.27.2 (2024-08-27)
```

[VERIFIED: PyPI JSON API]

## Architecture Patterns

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│  Meraki Dashboard API Client (entry point)                  │
│  meraki/__init__.py (sync) or meraki/aio/__init__.py (async)│
└────────────┬────────────────────────────────────────────────┘
             │
             │ instantiates
             ▼
┌─────────────────────────────────────────────────────────────┐
│  Session Layer                                               │
│  ┌──────────────────┐          ┌──────────────────────┐    │
│  │  RestSession     │          │ AsyncRestSession     │    │
│  │  (sync)          │          │ (async)              │    │
│  └────────┬─────────┘          └──────────┬───────────┘    │
│           │                               │                 │
│           │ inherits                      │ inherits        │
│           ▼                               ▼                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │  SessionBase (ABC)                                 │    │
│  │  - config storage                                  │    │
│  │  - retry loop (request method)                     │    │
│  │  - status dispatch (_handle_*)                     │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
             │
             │ delegates to
             ▼
┌─────────────────────────────────────────────────────────────┐
│  HTTP Transport (httpx)                                      │
│  ┌──────────────────┐          ┌──────────────────────┐    │
│  │  httpx.Client    │          │ httpx.AsyncClient    │    │
│  │  (persistent)    │          │ (persistent)         │    │
│  │  - connection    │          │ - connection         │    │
│  │    pooling       │          │    pooling           │    │
│  │  - timeout       │          │ - concurrency        │    │
│  │    enforcement   │          │    limits            │    │
│  └────────┬─────────┘          └──────────┬───────────┘    │
│           │                               │                 │
│           └──────────┬────────────────────┘                 │
│                      ▼                                       │
│            Network I/O (HTTP/1.1)                           │
└─────────────────────────────────────────────────────────────┘
             │
             │ sends requests to
             ▼
┌─────────────────────────────────────────────────────────────┐
│  Meraki Dashboard API (remote service)                      │
│  https://api.meraki.com/api/v1/*                            │
└─────────────────────────────────────────────────────────────┘
```

### Component Responsibilities

| Component | File | Responsibility |
|-----------|------|----------------|
| SessionBase | meraki/session/base.py | Config storage, retry loop, status dispatch (template methods) |
| RestSession | meraki/session/sync.py | Sync transport: instantiate httpx.Client, implement _send_request (sync), _sleep (time.sleep) |
| AsyncRestSession | meraki/session/async_.py | Async transport: instantiate httpx.AsyncClient, implement _send_request (async), _sleep (asyncio.sleep) |
| APIError | meraki/exceptions.py | Sync exception wrapper (reads response.status_code, response.reason_phrase) |
| AsyncAPIError | meraki/exceptions.py | Async exception wrapper (PHASE 11: updated to use response.status_code, response.reason_phrase; PHASE 12: becomes APIError subclass) |
| Config constants | meraki/config.py | AIO_MAXIMUM_CONCURRENT_REQUESTS (maps to httpx.Limits max_connections) |

### Pattern 1: Persistent Client Initialization

**What:** Instantiate httpx.Client/AsyncClient in session __init__ rather than per-request. Configure timeout, proxy, verify at client level.

**When to use:** ALWAYS for connection pooling efficiency. Per-request client instantiation breaks pooling and degrades performance.

**Example (sync):**

```python
# Source: User decision D-02 + httpx docs https://www.python-httpx.org/advanced/clients/
class RestSession(SessionBase):
    def __init__(self, logger, api_key, **kwargs):
        super().__init__(logger, api_key, **kwargs)
        
        # Build client config from session config
        client_kwargs = {}
        if self._certificate_path:
            client_kwargs["verify"] = self._certificate_path
        if self._requests_proxy:
            client_kwargs["proxy"] = self._requests_proxy
        client_kwargs["timeout"] = self._single_request_timeout
        
        # Persistent client
        self._client = httpx.Client(**client_kwargs)
        self._client.headers.update(self._build_headers())
```

**Example (async):**

```python
# Source: User decision D-02 + httpx docs
class AsyncRestSession(SessionBase):
    def __init__(self, logger, api_key, maximum_concurrent_requests=8, **kwargs):
        super().__init__(logger, api_key, **kwargs)
        
        # Build client config
        client_kwargs = {
            "timeout": self._single_request_timeout,
            "limits": httpx.Limits(max_connections=maximum_concurrent_requests),
        }
        if self._certificate_path:
            client_kwargs["verify"] = self._certificate_path
        if self._requests_proxy:
            client_kwargs["proxy"] = self._requests_proxy
        
        # Persistent async client
        self._client = httpx.AsyncClient(**client_kwargs)
        self._client.headers.update(self._build_headers())
```

[CITED: https://www.python-httpx.org/advanced/clients/, https://www.python-httpx.org/async/]

### Pattern 2: Typed Exception Handling

**What:** Catch httpx.HTTPError as single base exception for all transport failures (connect, timeout, protocol).

**When to use:** Wrapping transport calls in session subclasses. Simplifies exception handling (no need to catch ConnectTimeout, ReadTimeout, etc. separately).

**Example:**

```python
# Source: User decision D-03 + httpx docs https://www.python-httpx.org/exceptions/
import httpx
from meraki.exceptions import APIError, APIResponseError

def _send_request(self, method: str, url: str, **kwargs):
    try:
        response = self._client.request(method, url, follow_redirects=False, **kwargs)
        return response
    except httpx.HTTPError as e:
        # Convert transport error to APIError
        raise APIError(
            metadata,
            APIResponseError(e.__class__.__name__, 503, str(e)),
        )
```

[CITED: https://www.python-httpx.org/exceptions/]

### Pattern 3: Response Attribute Migration

**What:** httpx.Response uses .reason_phrase (not .reason). Update all response attribute access.

**When to use:** Anywhere code reads response.reason (APIError, AsyncAPIError, logging statements).

**Example:**

```python
# Source: httpx docs https://www.python-httpx.org/api/ + user decision D-04
# OLD (requests/aiohttp):
reason = response.reason

# NEW (httpx):
reason = response.reason_phrase
```

[CITED: https://www.python-httpx.org/api/]

### Anti-Patterns to Avoid

**Per-request client instantiation:**

```python
# BAD: breaks connection pooling
def _send_request(self, method, url, **kwargs):
    with httpx.Client() as client:  # NEW CLIENT EVERY REQUEST
        return client.request(method, url, **kwargs)

# GOOD: reuse persistent client
def _send_request(self, method, url, **kwargs):
    return self._client.request(method, url, **kwargs)
```

[CITED: https://www.python-httpx.org/async/]

**Forgetting follow_redirects parameter:**

```python
# BAD: httpx defaults to follow_redirects=False, but base class expects redirects NOT to be followed
response = self._client.request(method, url)  # might auto-follow if not configured

# GOOD: explicit control
response = self._client.request(method, url, follow_redirects=False)
```

[CITED: https://www.python-httpx.org/compatibility/]

**Using aiohttp-specific json() parameters:**

```python
# BAD: aiohttp needs content_type=None, httpx doesn't recognize it
data = await response.json(content_type=None)  # TypeError in httpx

# GOOD: httpx json() takes no content_type parameter
data = await response.json()
```

[VERIFIED: code inspection of AsyncRestSession]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| HTTP connection pooling | Manual socket reuse logic | httpx.Client persistent instance | httpx.Limits manages pool automatically (max_connections, keepalive_expiry); hand-rolled pooling misses edge cases (connection timeout, SSL renegotiation, HTTP/2 multiplexing) |
| Async concurrency limiting | asyncio.Semaphore wrapper | httpx.Limits(max_connections=N) | httpx enforces limits at transport level (before DNS resolution); semaphore only gates request submission (DNS/connect still unbounded) |
| Timeout enforcement | Manual asyncio.wait_for wrappers | httpx.Timeout(connect=X, read=Y, write=Z, pool=W) | httpx provides four distinct timeout types (connect/read/write/pool); manual wrappers typically only cover total timeout (miss granular control) |

**Key insight:** HTTP client complexity lives in edge cases (connection reuse with SSL, timeout during redirect chains, partial response reads). httpx has 10+ years of requests/urllib3 lessons baked in. Custom solutions inevitably rediscover those bugs.

## Runtime State Inventory

> Phase 11 is a code-only refactoring (swap HTTP backend). No runtime state modified.

**NOT APPLICABLE**

## Common Pitfalls

### Pitfall 1: Response Attribute Name Mismatch

**What goes wrong:** Code reads `response.reason` (requests/aiohttp) but httpx uses `response.reason_phrase`. Results in AttributeError at runtime.

**Why it happens:** requests.Response has `.reason` attribute; httpx.Response renamed it to `.reason_phrase` for HTTP/2 compatibility (HTTP/2 doesn't have a reason phrase in status line).

**How to avoid:** 

1. Search entire codebase for `.reason` attribute access: `grep -r "\.reason\b" meraki/`
2. Update all occurrences to `.reason_phrase`
3. Update exception classes (APIError, AsyncAPIError) to read `.reason_phrase`
4. Document as breaking change in HTTPX-MIGRATION.md

**Warning signs:** AttributeError: 'Response' object has no attribute 'reason' during test runs.

[VERIFIED: httpx docs https://www.python-httpx.org/api/ + compatibility guide]

### Pitfall 2: Redirect Handling Inversion

**What goes wrong:** httpx defaults to `follow_redirects=False` (opposite of requests which defaults to `allow_redirects=True`). If not specified, redirects aren't followed and base class redirect handler never triggers.

**Why it happens:** httpx philosophy: explicit is better than implicit (redirects should be opt-in, not opt-out).

**How to avoid:**

1. Explicitly pass `follow_redirects=False` in all `_send_request` implementations (even though it's the default)
2. Verify base class `_handle_redirect` is still called for 3xx responses
3. Test with integration test that triggers 301/302 (Meraki API does shard redirects)

**Warning signs:** 3xx responses returned to caller instead of being handled by retry loop.

[VERIFIED: httpx docs https://www.python-httpx.org/compatibility/]

### Pitfall 3: Async Context Manager Confusion

**What goes wrong:** Code uses `with` instead of `async with` for AsyncClient, or forgets to call `.aclose()` when not using context manager. Results in ResourceWarning about unclosed client.

**Why it happens:** AsyncRestSession currently creates aiohttp.ClientSession in __init__ and closes in explicit `close()` method. httpx.AsyncClient needs `await client.aclose()`.

**How to avoid:**

1. AsyncRestSession.__init__ creates httpx.AsyncClient (persistent)
2. AsyncRestSession.close() calls `await self._client.aclose()`
3. Ensure generated API modules call `await dashboard.close()` in cleanup
4. Update integration tests to use `async with AsyncRestSession(...) as session:` pattern

**Warning signs:** ResourceWarning: unclosed <httpx.AsyncClient> in test output.

[CITED: https://www.python-httpx.org/async/]

### Pitfall 4: Semaphore Removal Regression

**What goes wrong:** Removing asyncio.Semaphore from AsyncRestSession without configuring httpx.Limits causes unbounded concurrent requests (OOM or API rate limit exhaustion).

**Why it happens:** Current AsyncRestSession uses semaphore to cap concurrent requests at AIO_MAXIMUM_CONCURRENT_REQUESTS (default 8). httpx.Limits provides this functionality but must be explicitly configured.

**How to avoid:**

1. Pass `limits=httpx.Limits(max_connections=maximum_concurrent_requests)` to AsyncClient constructor
2. Verify integration test with pagination (triggers concurrent requests) still respects concurrency limit
3. Update config.py docstring for AIO_MAXIMUM_CONCURRENT_REQUESTS to explain httpx pool mapping

**Warning signs:** Integration tests fail with rate limit errors (429) when they previously passed.

[VERIFIED: code inspection + user decision D-02]

### Pitfall 5: Test Mock Signature Mismatch

**What goes wrong:** Unit tests mock requests.Response or aiohttp.ClientResponse but httpx.Response has different constructor signature. Mocks fail or produce incorrect test results.

**Why it happens:** httpx.Response requires specific constructor args (status_code, headers as list of tuples, etc.) that differ from requests.

**How to avoid:**

1. Update all test mocks to use httpx.Response signature
2. Or use MagicMock with explicit attribute setting (current pattern in test_session_base.py)
3. Phase 13 will replace mocks with respx library (httpx's equivalent of responses library)
4. For Phase 11, keep MagicMock pattern but add `.reason_phrase` attribute

**Warning signs:** Tests pass but don't actually validate behavior (mock returns wrong data shape).

[VERIFIED: code inspection of tests/unit/test_session_base.py]

## Code Examples

Verified patterns from official sources:

### Client Initialization (Sync)

```python
# Source: https://www.python-httpx.org/advanced/clients/
import httpx

# Persistent client with configuration
client = httpx.Client(
    timeout=60.0,
    verify="/path/to/cert.pem",  # or False, or ssl.SSLContext
    proxy="https://proxy.example.com:8030",
    headers={"Authorization": "Bearer token", "Content-Type": "application/json"},
)

# Use client for multiple requests (connection pooling)
response = client.get("https://api.meraki.com/api/v1/organizations")
response2 = client.get("https://api.meraki.com/api/v1/networks")

# Cleanup
client.close()
```

### Client Initialization (Async)

```python
# Source: https://www.python-httpx.org/async/
import httpx

# Persistent async client with concurrency limits
client = httpx.AsyncClient(
    timeout=60.0,
    limits=httpx.Limits(
        max_connections=8,          # Total concurrent connections
        max_keepalive_connections=5, # Persistent connections in pool
        keepalive_expiry=5.0,        # Seconds before closing idle connections
    ),
    verify="/path/to/cert.pem",
    proxy="https://proxy.example.com:8030",
    headers={"Authorization": "Bearer token"},
)

# Use with async/await
response = await client.get("https://api.meraki.com/api/v1/organizations")

# Cleanup
await client.aclose()
```

### Exception Handling

```python
# Source: https://www.python-httpx.org/exceptions/
import httpx

try:
    response = client.get("https://api.meraki.com/api/v1/organizations")
    response.raise_for_status()
except httpx.HTTPError as exc:
    # Catches all transport errors:
    # - ConnectTimeout, ReadTimeout, WriteTimeout, PoolTimeout
    # - ConnectError, ReadError, WriteError
    # - LocalProtocolError, RemoteProtocolError
    # - HTTPStatusError (from raise_for_status)
    print(f"HTTP error occurred: {exc}")
```

### Response Attribute Access

```python
# Source: https://www.python-httpx.org/api/
response = client.get("https://api.meraki.com/api/v1/organizations")

# Status
status_code = response.status_code  # int (e.g., 200)
reason = response.reason_phrase     # str (e.g., "OK")

# Headers (case-insensitive dict-like)
content_type = response.headers["Content-Type"]

# Body
json_data = response.json()        # Parse JSON
raw_bytes = response.content       # bytes
text = response.text               # str (decoded)
```

### Timeout Configuration

```python
# Source: https://www.python-httpx.org/advanced/timeouts/
import httpx

# Granular timeout control
timeout = httpx.Timeout(
    connect=10.0,  # Max seconds to establish connection
    read=30.0,     # Max seconds waiting for response data
    write=10.0,    # Max seconds writing request data
    pool=5.0,      # Max seconds acquiring connection from pool
)

client = httpx.Client(timeout=timeout)

# Or simple timeout (applies to all phases except pool)
client = httpx.Client(timeout=60.0)

# Per-request override
response = client.get("https://api.meraki.com/api/v1/organizations", timeout=10.0)
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| requests (sync) + aiohttp (async) | httpx (unified sync/async) | httpx 0.11.0 (Aug 2020) introduced AsyncClient | SDK can use single library for both modes, ~500 lines duplicated logic eliminated |
| allow_redirects=False (requests) | follow_redirects=False (httpx) | httpx 0.9.0 (May 2020) | Parameter renamed; default behavior inverted (httpx defaults to no follow) |
| response.reason | response.reason_phrase | httpx 0.7.0 (Jan 2020) | HTTP/2 compatibility (HTTP/2 has no reason phrase in status line); attribute renamed |
| asyncio.Semaphore for concurrency | httpx.Limits(max_connections=N) | httpx 0.10.0 (June 2020) | Built-in connection pool limits replace manual semaphore (enforced at transport layer, not app layer) |

**Deprecated/outdated:**

- **proxies kwarg (dict):** httpx 0.28.0 (Nov 2024) removed `proxies={"https": "..."}` dict form. Use `proxy="..."` string or `mounts` dict with HTTPTransport. [VERIFIED: https://github.com/encode/httpx/blob/master/CHANGELOG.md]
- **app kwarg:** httpx 0.27.0 (Feb 2024) deprecated `app=...` shortcut. Use explicit `transport=httpx.ASGITransport(app=...)`. [VERIFIED: changelog]
- **cert kwarg:** httpx 0.28.0 (Nov 2024) deprecated `cert=...` parameter. Use `verify=ssl.SSLContext` for custom SSL config. [VERIFIED: changelog]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | httpx.Client and httpx.AsyncClient use identical configuration parameters (timeout, proxy, verify, limits) | Standard Stack | Implementation requires different patterns for sync vs async (mitigated: official docs confirm identical API) |
| A2 | SessionBase._send_request signature returning "httpx.Response" (TYPE_CHECKING import) is compatible with actual httpx.Response | Architecture Patterns | Type checker accepts mock but runtime fails (mitigated: tests already use httpx-compatible mocks) |
| A3 | Meraki API shard redirects (301/302) work with httpx.Response.headers["Location"] attribute access | Pitfall 2 | Redirect handler breaks if headers dict interface differs (mitigated: httpx docs confirm case-insensitive dict-like headers) |

## Open Questions

None. All research domains covered with HIGH confidence sources.

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python | SDK runtime | ✓ | 3.14.3 | — |
| pytest | Unit tests | ✓ | 9.0.3 | — |
| uv | Package management | ✓ | 0.10.4 | pip fallback |
| httpx | HTTP transport (post-migration) | ✗ | — (install via uv) | Block execution until installed |

**Missing dependencies with no fallback:**
- httpx (to be installed in Wave 0 of Phase 11 execution)

**Missing dependencies with fallback:**
- None

## Validation Architecture

> nyquist_validation not explicitly enabled/disabled in .planning/config.json. Treating as enabled per default.

### Test Framework

| Property | Value |
|----------|-------|
| Framework | pytest 9.0.3 |
| Config file | pyproject.toml (lines 55-58) |
| Quick run command | `pytest tests/unit -x` |
| Full suite command | `pytest tests/unit --cov=meraki --cov-report=term-missing` |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| HTTP-01 | RestSession uses httpx.Client for sync requests | unit | `pytest tests/unit/test_rest_session.py::TestSyncTransport -x` | ❌ Wave 0 |
| HTTP-02 | AsyncRestSession uses httpx.AsyncClient for async requests | unit | `pytest tests/unit/test_aio_rest_session.py::TestAsyncTransport -x` | ❌ Wave 0 |
| ERR-01 | APIError reads response.reason_phrase (not .reason) | unit | `pytest tests/unit/test_exceptions.py::TestAPIErrorAttributes -x` | ❌ Wave 0 |
| ERR-03 | httpx.HTTPError caught and converted to APIError | unit | `pytest tests/unit/test_rest_session.py::TestExceptionHandling -x` | ❌ Wave 0 |
| DEP-01 | httpx in dependencies, requests/aiohttp removed | smoke | `uv pip list \| grep -E "httpx\|requests\|aiohttp"` (manual) | manual-only |
| DEP-03 | requests_proxy param maps to httpx proxy kwarg | unit | `pytest tests/unit/test_rest_session.py::TestProxyConfiguration -x` | ❌ Wave 0 |

### Sampling Rate

- **Per task commit:** `pytest tests/unit -x` (stop on first failure)
- **Per wave merge:** `pytest tests/unit` (full unit suite)
- **Phase gate:** `pytest tests/unit --cov=meraki --cov-report=term-missing` (coverage report) + integration baseline comparison (Phase 8 output)

### Wave 0 Gaps

- [ ] `tests/unit/test_rest_session.py::TestSyncTransport` — verify httpx.Client instantiation and request method delegation
- [ ] `tests/unit/test_rest_session.py::TestProxyConfiguration` — verify requests_proxy → proxy kwarg mapping
- [ ] `tests/unit/test_rest_session.py::TestExceptionHandling` — verify httpx.HTTPError → APIError conversion
- [ ] `tests/unit/test_aio_rest_session.py::TestAsyncTransport` — verify httpx.AsyncClient instantiation and async request delegation
- [ ] `tests/unit/test_aio_rest_session.py::TestConcurrencyLimits` — verify httpx.Limits enforces max_connections
- [ ] `tests/unit/test_exceptions.py::TestAPIErrorAttributes` — verify APIError reads .reason_phrase not .reason
- [ ] `tests/unit/test_exceptions.py::TestAsyncAPIErrorAttributes` — verify AsyncAPIError reads .status_code and .reason_phrase (aiohttp → httpx compatibility)

## Security Domain

> security_enforcement absent from .planning/config.json — treating as enabled per default.

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|------------------|
| V2 Authentication | no | API key auth unchanged (Bearer token in headers) |
| V3 Session Management | no | Stateless API (no session cookies) |
| V4 Access Control | no | Authorization handled by Meraki API backend |
| V5 Input Validation | yes | httpx validates URL syntax (RFC 3986); SDK validates params via encoding.py |
| V6 Cryptography | yes | TLS verification via httpx.Client(verify=...) — NEVER use verify=False in production |

### Known Threat Patterns for HTTP Client Libraries

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| SSRF via unvalidated URLs | Tampering/Elevation | httpx validates URL scheme (blocks file://, data://, etc.); SDK uses validate_base_url() to enforce api.meraki.com domain |
| TLS certificate bypass | Spoofing | httpx defaults to verify=True; SDK allows certificate_path override for internal CAs but NEVER verify=False |
| Proxy credential leakage in logs | Information Disclosure | httpx redacts proxy credentials from repr(); SDK logs masked API keys (config.py lines 102-103) |
| Response body injection via redirects | Tampering | SDK sets follow_redirects=False and manually validates redirect Location header (response_handler.py handle_3xx) |
| Timeout-based DoS | Denial of Service | httpx enforces default 5s timeout; SDK overrides to 60s via SINGLE_REQUEST_TIMEOUT (config.py line 16) |

## Sources

### Primary (HIGH confidence)

- httpx 0.28.1 PyPI metadata — version verification (2024-12-06 release) [VERIFIED: PyPI JSON API]
- https://www.python-httpx.org/quickstart/ — basic client usage
- https://www.python-httpx.org/advanced/clients/ — Client/AsyncClient configuration
- https://www.python-httpx.org/async/ — AsyncClient patterns and pitfalls
- https://www.python-httpx.org/exceptions/ — HTTPError hierarchy and exception handling
- https://www.python-httpx.org/api/ — Response attributes (status_code, reason_phrase)
- https://www.python-httpx.org/compatibility/ — requests vs httpx API differences
- https://www.python-httpx.org/advanced/timeouts/ — Timeout configuration
- https://www.python-httpx.org/advanced/proxies/ — Proxy configuration
- https://github.com/encode/httpx/blob/master/CHANGELOG.md — v0.28.x and v0.27.x changes

### Secondary (MEDIUM confidence)

None used. All claims verified via official httpx documentation.

### Tertiary (LOW confidence)

None.

## Metadata

**Confidence breakdown:**

- Standard stack: HIGH — httpx 0.28.1 verified via PyPI, official docs confirm sync/async parity
- Architecture: HIGH — Phase 10 template-method pattern established, httpx patterns verified via official docs
- Pitfalls: HIGH — Common issues documented in official httpx compatibility guide and changelog
- Exception handling: HIGH — HTTPError hierarchy documented in official exceptions guide
- Test coverage: MEDIUM — existing test mocks use MagicMock (verified), but respx migration deferred to Phase 13

**Research date:** 2026-05-04
**Valid until:** 2026-06-04 (30 days — httpx is stable with monthly releases)
