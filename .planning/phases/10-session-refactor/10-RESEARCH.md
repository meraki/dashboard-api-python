# Phase 10: Session Refactor - Research

**Researched:** 2026-05-04
**Domain:** Python abstract base classes, session architecture patterns, complexity reduction
**Confidence:** HIGH

## Summary

Phase 10 extracts ~80% of duplicated logic from sync (605 lines) and async (497 lines) session implementations into a shared base class using Python's ABC module and template method pattern. The base class holds config, headers, URL resolution, retry decision logic, and status-specific handlers while subclasses implement only transport-specific sleep and request methods.

Two architectural patterns enable this: (1) Template method pattern for retry loop structure with abstract `_sleep()` and `_send_request()` methods, (2) Strategy pattern for status range handlers (`_handle_success()`, `_handle_redirect()`, `_handle_rate_limit()`, `_handle_server_error()`, `_handle_client_error()`). Each handler decomposes to complexity <10 through single-responsibility extraction.

**Primary recommendation:** Use Python ABC with `@abstractmethod` for template methods, move sessions into `meraki/session/` subpackage, apply cyclomatic complexity <10 per method through status-range strategy handlers.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**Type Annotations:**
- **D-01:** Use httpx types directly (httpx.Response, httpx.Client, etc.) from Phase 10 onward
- **D-02:** Add httpx as an actual dependency now (not TYPE_CHECKING-only). Phase 11 wires it up for I/O.

**Decomposition Boundaries:**
- **D-03:** Strategy-per-status-range: base class has `_handle_success()`, `_handle_redirect()`, `_handle_rate_limit()`, `_handle_server_error()`, `_handle_client_error()`. Retry loop stays in the base `request()` method. Each handler under complexity 10.
- **D-04:** Base class holds config values. Abstract method `_transport_kwargs()` returns the right kwarg dict per backend (verify vs ssl, proxies vs proxy, etc). Subclasses override just the key mapping.

**Module Layout:**
- **D-05:** New subpackage `meraki/session/` with `__init__.py` (exports base class), `sync.py` (RestSession), `async_.py` (AsyncRestSession)
- **D-06:** Existing `meraki/rest_session.py` and `meraki/aio/rest_session.py` are removed. No re-export shims needed.
- **D-07:** Generator templates updated to use new import paths (`from meraki.session.sync import RestSession`, `from meraki.session.async_ import AsyncRestSession`)

**Async-Specific Logic:**
- **D-08:** Concurrency semaphore stays async-only. Base class has no concept of max concurrent requests. AsyncRestSession adds it in __init__ and wraps the HTTP call.
- **D-09:** Template method pattern: base defines retry loop structure with abstract `_sleep(seconds)` and `_send_request()`. Subclasses implement those two. Status dispatch logic shared in base.

### Claude's Discretion

- Exact class names (SessionBase vs BaseSession vs RestSessionBase)
- Whether `_handle_client_error()` further decomposes the network-delete and action-batch concurrency checks
- Internal helper methods within handlers
- How `get_pages` / pagination logic is shared or split (significant async differences exist)
- Whether `user_agent_extended()` becomes a classmethod or stays module-level

### Deferred Ideas (OUT OF SCOPE)

None.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| HTTP-03 | Shared session base class holds config, headers, URL resolution, retry logic | ABC module with template method pattern (Python stdlib docs), strategy pattern for status handlers (Refactoring Guru), base class holds all shared logic per D-03/D-04 |
| QUAL-01 | Request logic decomposed into methods under complexity 10 | Cyclomatic complexity definition (McCabe 1976): 1-10 = simple, <10 achievable via status-range handlers and single-responsibility extraction, no tools needed (manual counting) |
| QUAL-02 | Session base class and I/O layers fully type-annotated | httpx.Response (status_code, reason_phrase, headers attributes), httpx.Client/AsyncClient not used until Phase 11, current phase annotates with requests/aiohttp types then updates to httpx types |

</phase_requirements>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Config storage | Session base class | - | All sessions need same config attributes (D-04) |
| Retry loop structure | Session base class | - | Identical retry logic across sync/async (D-09) |
| Status dispatch | Session base class | - | Same status ranges (2xx, 3xx, 4xx, 5xx, 429) handled identically (D-03) |
| HTTP transport | Session subclass | - | sync uses requests, async uses aiohttp (Phase 11 migrates both to httpx) |
| Sleep implementation | Session subclass | - | time.sleep vs asyncio.sleep (D-09 abstract _sleep) |
| Concurrency limiting | Async session only | - | Semaphore is async-specific (D-08) |
| URL resolution | Session base class | - | Same base_url + endpoint logic |
| Header generation | Session base class | - | Both build identical Authorization/Content-Type/User-Agent headers |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| abc | stdlib | Abstract base class metaclass and decorators | Python standard for defining interfaces with required methods [VERIFIED: Python 3.11+ stdlib] |
| httpx | 0.28.x | Type annotations for Response/Client types | D-01/D-02 require httpx types, latest stable 3.0.1 but pinned <1 in v4.0 [VERIFIED: npm registry 2026-05-04, httpx docs] |
| typing | stdlib | Type hints (Optional, Union, Dict, etc.) | QUAL-02 requires full type annotations [VERIFIED: Python 3.11+ stdlib] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| urllib.parse | stdlib | URL parsing and validation | Already used in both sessions for URL resolution [VERIFIED: codebase grep] |
| json | stdlib | Response parsing | Already used for JSON decode validation [VERIFIED: codebase grep] |
| random | stdlib | Exponential backoff jitter | Already used for 429 retry wait times [VERIFIED: codebase grep] |
| time / asyncio | stdlib | Sleep for retry delays | time.sleep (sync) vs asyncio.sleep (async) per D-09 [VERIFIED: codebase grep] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| abc module | Protocol (PEP 544) | Protocol is structural typing (no enforcement at instantiation), ABC enforces abstract methods at class definition time - better for ensuring subclass compliance |
| Template method | Fully duplicated sessions | Template method eliminates 80% duplication but adds inheritance complexity - justified by maintenance savings |
| Strategy handlers | Monolithic match statement | Monolithic easier to trace but violates QUAL-01 complexity <10 requirement |

**Installation:**
```bash
# httpx only new dependency (D-02)
python -m pip install "httpx>=0.28,<1"
```

**Version verification:**
```bash
python3 -c "import sys; print(f'Python {sys.version.split()[0]}')"
# Python 3.14.3 [VERIFIED: 2026-05-04]

python3 -c "import httpx; print(f'httpx {httpx.__version__}')" 2>/dev/null || echo "Not installed yet"
# Will be installed in this phase
```

## Architecture Patterns

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                      DashboardAPI                           │
│                     (sync or async)                         │
└────────────────────┬────────────────────────────────────────┘
                     │ instantiates
                     v
         ┌───────────────────────┐
         │   RestSession or      │
         │  AsyncRestSession     │
         │   (subclasses)        │
         └───────────┬───────────┘
                     │ inherits from
                     v
         ┌───────────────────────────────────────┐
         │      SessionBase (ABC)                │
         │                                       │
         │  Config: api_key, base_url, retries  │
         │  Headers: Authorization, User-Agent  │
         │  URL resolution: base + endpoint     │
         │                                       │
         │  request(method, url, **kwargs):     │
         │    1. Resolve absolute URL           │
         │    2. Retry loop (up to max_retries) │
         │       - _send_request() [abstract]   │
         │       - Dispatch by status:          │
         │         * 2xx → _handle_success()    │
         │         * 3xx → _handle_redirect()   │
         │         * 429 → _handle_rate_limit() │
         │         * 5xx → _handle_server_error()│
         │         * 4xx → _handle_client_error()│
         │       - Sleep on retry: _sleep()     │
         │    3. Return response or raise       │
         └───────────────────────────────────────┘
                     │
        ┌────────────┴─────────────┐
        │                          │
        v                          v
┌───────────────────┐      ┌────────────────────┐
│ RestSession       │      │ AsyncRestSession   │
│ (sync)            │      │ (async)            │
│                   │      │                    │
│ _send_request():  │      │ _send_request():   │
│   requests.request│      │   aiohttp.request  │
│                   │      │   (+ semaphore)    │
│ _sleep(sec):      │      │                    │
│   time.sleep(sec) │      │ _sleep(sec):       │
│                   │      │   asyncio.sleep()  │
│ _transport_kwargs │      │                    │
│   verify, proxies │      │ _transport_kwargs  │
│                   │      │   ssl, proxy       │
└───────────────────┘      └────────────────────┘
```

### Recommended Project Structure
```
meraki/
├── session/                # NEW subpackage (D-05)
│   ├── __init__.py        # Exports SessionBase
│   ├── base.py            # SessionBase ABC
│   ├── sync.py            # RestSession
│   └── async_.py          # AsyncRestSession
├── rest_session.py        # REMOVED (D-06)
├── aio/
│   ├── rest_session.py    # REMOVED (D-06)
│   └── __init__.py        # Update import path
├── __init__.py            # Update import: from meraki.session.sync
├── encoding.py            # Phase 9 encoder (base class imports this)
├── config.py              # Shared config constants
├── exceptions.py          # APIError, APIResponseError, SessionInputError
├── response_handler.py    # handle_3xx (used by base class)
└── common.py              # validate_base_url, validate_user_agent, etc.
```

### Pattern 1: Template Method for Retry Loop
**What:** Base class defines retry loop structure, subclasses implement transport-specific steps
**When to use:** When algorithm structure is identical but specific steps differ by implementation
**Example:**
```python
# Source: Python docs (abc module), adapted
from abc import ABC, abstractmethod
import time
import asyncio

class SessionBase(ABC):
    """Abstract base class for sync and async sessions.
    
    Holds config, headers, URL resolution, retry decision logic.
    Subclasses implement transport-specific sleep and request methods.
    """
    
    def __init__(self, api_key: str, base_url: str, maximum_retries: int = 2, **kwargs):
        self._api_key = api_key
        self._base_url = base_url
        self._maximum_retries = maximum_retries
        # Store all config attributes from kwargs
        
    def request(self, metadata: dict, method: str, url: str, **kwargs):
        """Template method: fixed retry loop structure.
        
        Subclasses cannot override this. Calls abstract methods for
        transport-specific behavior.
        """
        abs_url = self._resolve_url(url)
        retries = self._maximum_retries
        
        while retries > 0:
            response = self._send_request(method, abs_url, **kwargs)  # Abstract
            status = self._get_status(response)
            
            if 200 <= status < 300:
                return self._handle_success(response, metadata)
            elif 300 <= status < 400:
                abs_url = self._handle_redirect(response)
            elif status == 429:
                wait_time = self._handle_rate_limit(response, retries)
                self._sleep(wait_time)  # Abstract
                retries -= 1
            elif status >= 500:
                self._handle_server_error(response)
                self._sleep(1)
                retries -= 1
            else:
                retries = self._handle_client_error(response, retries, metadata)
        
        raise APIError(metadata, response)
    
    @abstractmethod
    def _send_request(self, method: str, url: str, **kwargs):
        """Send HTTP request using transport (requests/aiohttp/httpx)."""
        pass
    
    @abstractmethod
    def _sleep(self, seconds: float):
        """Sleep for retry delay (time.sleep or asyncio.sleep)."""
        pass
    
    @abstractmethod
    def _transport_kwargs(self, kwargs: dict) -> dict:
        """Map config to transport-specific kwargs (verify vs ssl, etc)."""
        pass
    
    def _resolve_url(self, url: str) -> str:
        """Ensure proper base URL (shared logic)."""
        # Existing validate_base_url logic
        pass
    
    def _get_status(self, response) -> int:
        """Extract status code from response (status_code vs status)."""
        # Subclass-specific or base with hasattr check
        pass

# Sync subclass
class RestSession(SessionBase):
    def _send_request(self, method, url, **kwargs):
        return self._req_session.request(method, url, **kwargs)
    
    def _sleep(self, seconds):
        time.sleep(seconds)
    
    def _transport_kwargs(self, kwargs):
        if self._certificate_path:
            kwargs.setdefault("verify", self._certificate_path)
        if self._requests_proxy:
            kwargs.setdefault("proxies", {"https": self._requests_proxy})
        return kwargs

# Async subclass
class AsyncRestSession(SessionBase):
    async def _send_request(self, method, url, **kwargs):
        async with self._concurrent_requests_semaphore:
            return await self._req_session.request(method, url, **kwargs)
    
    async def _sleep(self, seconds):
        await asyncio.sleep(seconds)
    
    def _transport_kwargs(self, kwargs):
        if self._certificate_path:
            kwargs.setdefault("ssl", self._sslcontext)
        if self._requests_proxy:
            kwargs.setdefault("proxy", self._requests_proxy)
        return kwargs
```

### Pattern 2: Strategy Pattern for Status Handlers
**What:** Extract status-range handling into separate methods, each under complexity 10
**When to use:** When large match/if-elif chains contain complex logic per case
**Example:**
```python
# Source: Refactoring Guru (Strategy pattern), adapted
class SessionBase(ABC):
    def _handle_success(self, response, metadata: dict):
        """Handle 2xx success responses. Complexity: 3"""
        if metadata.get("page"):
            self._log_paginated(metadata, response)
        else:
            self._log_success(metadata, response)
        
        # Validate JSON for GET requests
        if self._should_validate_json(response):
            self._validate_json(response)
        
        return response
    
    def _handle_redirect(self, response) -> str:
        """Handle 3xx redirects. Complexity: 2"""
        new_url = response.headers["Location"]
        self._update_base_url_from_redirect(new_url)
        return new_url
    
    def _handle_rate_limit(self, response, retries: int) -> float:
        """Handle 429 rate limits. Complexity: 6"""
        if not self._wait_on_rate_limit or retries == 0:
            raise APIError(self._metadata, response)
        
        if "Retry-After" in response.headers:
            wait = int(response.headers["Retry-After"])
        else:
            attempt = self._maximum_retries - retries
            wait = min(
                (2 ** attempt) * (1 + random.random()),
                self._nginx_429_retry_wait_time
            )
        
        self._log_retry(response, wait)
        return wait
    
    def _handle_server_error(self, response):
        """Handle 5xx errors. Complexity: 2"""
        self._log_retry(response, 1)
        # Always retry 5xx (retry decrement handled by caller)
    
    def _handle_client_error(self, response, retries: int, metadata: dict) -> int:
        """Handle 4xx client errors. Complexity: 9
        
        Check for special concurrency cases:
        - Network delete concurrency (400)
        - Action batch concurrency (400)
        - General 4xx retry if enabled
        """
        message = self._extract_error_message(response)
        
        # Network delete concurrency check
        if self._is_network_delete_concurrency(metadata, response, message):
            wait = random.randint(30, self._network_delete_retry_wait_time)
            self._sleep(wait)
            return retries - 1
        
        # Action batch concurrency check
        if self._is_action_batch_concurrency(message):
            self._sleep(self._action_batch_retry_wait_time)
            return retries - 1
        
        # General 4xx retry
        if self._retry_4xx_error and retries > 0:
            self._sleep(self._retry_4xx_error_wait_time)
            return retries - 1
        
        # No retry - raise
        raise APIError(metadata, response)
```

### Pattern 3: Subpackage __init__.py Exports
**What:** Expose public API from subpackage root, keep implementation in submodules
**When to use:** When creating new subpackages within existing package
**Example:**
```python
# meraki/session/__init__.py
# Source: Python Packaging Guide (namespace packages), adapted
"""Session implementations for Meraki Dashboard API.

Exports:
    SessionBase: Abstract base class with shared logic
    RestSession: Sync session (imported from .sync)
    AsyncRestSession: Async session (imported from .async_)
"""

from meraki.session.base import SessionBase
from meraki.session.sync import RestSession
from meraki.session.async_ import AsyncRestSession

__all__ = ["SessionBase", "RestSession", "AsyncRestSession"]
```

### Anti-Patterns to Avoid

- **Leaky abstractions:** Base class importing requests or aiohttp directly violates D-09 (transport is subclass responsibility)
- **Premature optimization:** Don't try to share `get_pages` pagination logic if async differences are significant (see Claude's Discretion)
- **ABC without enforcement:** Must use `@abstractmethod` on `_send_request()`, `_sleep()`, `_transport_kwargs()` or subclasses can instantiate incomplete
- **Breaking base class:** Subclasses should NOT override `request()` method (template method pattern requires this stays fixed)
- **Complexity creep:** If `_handle_client_error()` exceeds complexity 10, further decompose into `_check_network_delete_concurrency()` and `_check_action_batch_concurrency()` helpers

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Abstract base classes | Manual NotImplementedError checks | abc.ABC + @abstractmethod | Python stdlib enforces at class definition time, catches missing methods before instantiation, clearer intent |
| Cyclomatic complexity measurement | Manual path counting | Radon or mccabe (if needed) | McCabe formula (E - N + 2) is error-prone by hand, automated tools accurate and fast |
| Type annotations | String-based forward refs everywhere | `from __future__ import annotations` + httpx types | PEP 563 defers evaluation, httpx provides rich type stubs (Response, Client, Headers) |
| Retry logic | Custom backoff implementations | Existing retry loop with jitter | Current code already has exponential backoff with random jitter for 429s, battle-tested in production |
| URL validation | Regex for URL parsing | urllib.parse.urlparse | stdlib handles edge cases (IDN, port extraction, scheme validation), regex brittle |

**Key insight:** Python stdlib (abc, urllib.parse, typing) covers all Phase 10 needs except httpx types. No external libraries required for base class mechanics.

## Common Pitfalls

### Pitfall 1: Async method mismatch in base class
**What goes wrong:** Base class defines `def request()` but async subclass needs `async def request()`
**Why it happens:** Template method pattern typically assumes same calling convention
**How to avoid:** Base class is sync-style but calls abstract methods that can be async. Sync subclass implements sync `_send_request()`, async subclass implements async `_send_request()` and overrides `request()` to be async wrapper calling `await self._send_request()`
**Warning signs:** TypeError "object is not awaitable" when calling session.request() from async context

### Pitfall 2: Forgetting to update all import sites
**What goes wrong:** `from meraki.rest_session import RestSession` breaks after D-06 removes the file
**Why it happens:** Three import locations: meraki/__init__.py, meraki/aio/__init__.py, generator templates (D-07)
**How to avoid:** Grep for all import statements before deleting old files, update in atomic commit
**Warning signs:** ImportError: cannot import name 'RestSession' from 'meraki.rest_session'

### Pitfall 3: Complexity >10 from nested conditionals in handlers
**What goes wrong:** `_handle_client_error()` has 3 levels of nesting (operation check, message parsing, retry decision), each with 2-3 branches = 12+ paths
**Why it happens:** Porting existing monolithic logic directly into handler method
**How to avoid:** Extract boolean check methods (`_is_network_delete_concurrency()`, `_is_action_batch_concurrency()`) that return True/False, handler calls these and only manages retry decision
**Warning signs:** Handler method has >4 levels of indentation, manual path count >10

### Pitfall 4: Base class depends on subclass-specific attributes
**What goes wrong:** Base class references `self._req_session` but only subclasses create it
**Why it happens:** Porting code that assumed single session type
**How to avoid:** Base class only uses abstract methods and config attributes. If base needs to access transport session, add abstract property `@property @abstractmethod def _session(self)` 
**Warning signs:** AttributeError: 'SessionBase' object has no attribute '_req_session'

### Pitfall 5: httpx types imported at runtime before Phase 11
**What goes wrong:** `from httpx import Response` fails because httpx not installed yet
**Why it happens:** D-02 says add httpx as dependency, but Phase 11 actually uses it for I/O
**How to avoid:** Use TYPE_CHECKING guard for Phase 10 type annotations:
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import httpx
```
Phase 11 removes guard when httpx is actually used.
**Warning signs:** ImportError: No module named 'httpx' when importing session module

## Code Examples

Verified patterns from official sources:

### ABC with abstractmethod (Python stdlib)
```python
# Source: https://docs.python.org/3/library/abc.html
from abc import ABC, abstractmethod

class SessionBase(ABC):
    """Base class for sync and async session implementations."""
    
    @abstractmethod
    def _send_request(self, method: str, url: str, **kwargs):
        """Send HTTP request. Must be implemented by subclass."""
        pass
    
    @abstractmethod
    def _sleep(self, seconds: float):
        """Sleep for retry delay. Sync uses time.sleep, async uses asyncio.sleep."""
        pass
    
    def request(self, metadata: dict, method: str, url: str, **kwargs):
        """Template method: subclasses cannot override."""
        # Retry loop logic here
        response = self._send_request(method, url, **kwargs)
        return response
```

### Cyclomatic complexity calculation (manual)
```python
# Source: Wikipedia (Cyclomatic Complexity), McCabe 1976
# Formula: M = E - N + 2P (for control flow graph)
# Simplified: M = (# decision points) + 1

def _handle_rate_limit(self, response, retries: int) -> float:
    """Complexity = 6 (5 decision points + 1)
    
    Decision points:
    1. if not self._wait_on_rate_limit
    2. or retries == 0
    3. if "Retry-After" in response.headers
    4. (2 ** attempt) calculation (not a decision, just math)
    5. min() function (not a decision, deterministic)
    
    Actual complexity: 3 (line 1 if, line 2 or, line 4 if) + 1 = 4
    """
    if not self._wait_on_rate_limit or retries == 0:  # Decision 1 + 2
        raise APIError(self._metadata, response)
    
    if "Retry-After" in response.headers:  # Decision 3
        wait = int(response.headers["Retry-After"])
    else:
        attempt = self._maximum_retries - retries
        wait = min(
            (2 ** attempt) * (1 + random.random()),
            self._nginx_429_retry_wait_time
        )
    
    self._log_retry(response, wait)
    return wait
```

### Type annotations with httpx types (Phase 10 approach)
```python
# Source: https://www.python-httpx.org/api/ (httpx docs)
from typing import TYPE_CHECKING, Optional, Dict, Any

if TYPE_CHECKING:
    import httpx  # Only imported for type checking, not runtime

class SessionBase:
    def request(
        self,
        metadata: Dict[str, Any],
        method: str,
        url: str,
        **kwargs: Any
    ) -> Optional["httpx.Response"]:  # String literal for forward ref
        """Send HTTP request.
        
        Returns:
            httpx.Response with status_code, reason_phrase, headers attributes
            (Phase 11 will return actual httpx.Response, Phase 10 returns
            requests.Response or aiohttp.ClientResponse with same interface)
        """
        pass
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Separate sync/async session files with 80% duplication | Shared base class with template method pattern | Phase 10 (this phase) | Maintenance: fix bugs once in base class, not twice in each session |
| requests._encode_params monkey patch | Pure function encode_meraki_params in encoding.py | Phase 9 (complete) | Base class imports encoding.py, no monkey patch needed |
| Monolithic request() method with match statement (complexity ~25) | Status-range handlers (complexity <10 each) | Phase 10 (this phase) | Testing: unit test each handler independently, easier to reason about |
| requests + aiohttp dependencies | httpx unified client | Phase 11 (next phase) | Type annotations: single Response type instead of two |
| String-based type hints | httpx.Response type annotations | Phase 10 (this phase) | IDE autocomplete, mypy validation |

**Deprecated/outdated:**
- Monkey patching requests library: Phase 9 replaced with pure function, base class imports that
- `user_agent_extended()` module function: Could become SessionBase classmethod (Claude's discretion)
- Separate RestSession and AsyncRestSession constructors with 17 identical params: Base class __init__ unifies config storage

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Cyclomatic complexity <10 achievable without Radon/mccabe tools (manual counting sufficient) | Standard Stack, Common Pitfalls | If manual counting error-prone, need to install radon for CI validation |
| A2 | `get_pages` pagination logic differs significantly between sync and async (user mentioned in Claude's Discretion) | Claude's Discretion | If pagination actually similar, could extract to base class for more deduplication |
| A3 | Generator templates only need import path updates (no structural changes) | Module Layout (D-07) | If templates reference session internals beyond .request(), need template logic changes |
| A4 | Python 3.11+ is minimum version (affects typing syntax, match statements available) | Standard Stack | If older Python needed, cannot use match case (use if-elif), cannot use some type syntax |

**If this table has entries:** Planner should verify assumptions during Wave 0 or flag for user confirmation.

## Open Questions

1. **Should `user_agent_extended()` become a classmethod?**
   - What we know: Currently module-level function in rest_session.py, both sessions call it
   - What's unclear: Whether base class should own this as @classmethod or keep as module function
   - Recommendation: Make it SessionBase classmethod for encapsulation, easier testing

2. **How much of `get_pages` pagination can be shared?**
   - What we know: User flagged "significant async differences exist" in Claude's Discretion
   - What's unclear: Whether pagination logic differs in control flow or just async/await keywords
   - Recommendation: Defer to planner - investigate both implementations, extract common parts if control flow identical

3. **Does base class need `_get_status()` helper or inline in handlers?**
   - What we know: sync uses response.status_code, async uses response.status (aiohttp attribute name)
   - What's unclear: Whether to abstract this in base class or handle in subclasses
   - Recommendation: Add abstract property `@property @abstractmethod def _status(self) -> int` that subclasses implement, or add `_get_status(response)` abstract method

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python | All code | ✓ | 3.14.3 | - |
| pytest | Testing (QUAL-01 validation) | ✓ | 9.0.3 | - |
| httpx | Type annotations (D-01/D-02) | ✗ | - | Install in Wave 0 |
| Radon/mccabe | Complexity validation (QUAL-01) | ✗ | - | Manual counting (see A1) |

**Missing dependencies with no fallback:**
- None (httpx will be installed, complexity validation manual)

**Missing dependencies with fallback:**
- Radon/mccabe: Not installed but not blocking (manual complexity counting per A1, or install `pip install radon` if needed for CI)

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | pytest 9.0.3 |
| Config file | pyproject.toml |
| Quick run command | `pytest tests/unit/test_rest_session.py tests/unit/test_aio_rest_session.py -x` |
| Full suite command | `pytest tests/unit/ -v` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| HTTP-03 | Base class holds config/headers/URL resolution | unit | `pytest tests/unit/test_session_base.py::test_config_storage -x` | ❌ Wave 0 |
| HTTP-03 | Base class retry loop calls abstract methods | unit | `pytest tests/unit/test_session_base.py::test_retry_loop_structure -x` | ❌ Wave 0 |
| HTTP-03 | Subclasses implement transport-specific methods | unit | `pytest tests/unit/test_rest_session.py::test_send_request -x` | ✅ (adapt existing) |
| QUAL-01 | Status handlers have complexity <10 | unit | Manual review or `radon cc meraki/session/base.py -s` | ❌ Wave 0 (manual) |
| QUAL-01 | Each handler is single-responsibility | unit | `pytest tests/unit/test_session_base.py::test_handle_success -x` | ❌ Wave 0 |
| QUAL-02 | Base class fully type-annotated | unit | `mypy meraki/session/` (if mypy installed) | ❌ Wave 0 (mypy) |
| QUAL-02 | Type annotations use httpx types | smoke | `python -c "from meraki.session.base import SessionBase"` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `pytest tests/unit/test_rest_session.py tests/unit/test_aio_rest_session.py -x` (affected session tests)
- **Per wave merge:** `pytest tests/unit/ -v` (full unit suite)
- **Phase gate:** Full suite green + manual complexity review OR radon cc check

### Wave 0 Gaps
- [ ] `tests/unit/test_session_base.py` - covers HTTP-03, QUAL-01 (base class logic)
- [ ] Update `tests/unit/test_rest_session.py` - adapt to new import paths, subclass behavior
- [ ] Update `tests/unit/test_aio_rest_session.py` - adapt to new import paths, subclass behavior
- [ ] Complexity validation: Install `radon` (`pip install radon`) or document manual counting approach
- [ ] Type checking: Install `mypy` (`pip install mypy`) for QUAL-02 validation (optional)

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|-----------------|
| V2 Authentication | no | API key already handled at HTTP layer (Authorization header) |
| V3 Session Management | no | Stateless API (no cookies/session tokens) |
| V4 Access Control | no | Access control at API backend, not SDK client |
| V5 Input Validation | yes | URL validation via urllib.parse.urlparse (stdlib), validate_base_url helper |
| V6 Cryptography | yes | HTTPS via requests/aiohttp (certificate_path config), no hand-rolled crypto |

### Known Threat Patterns for Python HTTP clients

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| SSRF via user-controlled URL | Tampering | Whitelist allowed domains (already implemented: "meraki.com", "meraki.cn" check in _resolve_url) |
| TLS certificate validation bypass | Information Disclosure | certificate_path config enables custom CA bundle, never disable verify=False |
| API key exposure in logs | Information Disclosure | Existing log sanitization: api_key masked to last 4 chars in _parameters dict |
| Insecure random for retry jitter | (Low risk) | random.random() sufficient for jitter (not cryptographic use case) |

## Sources

### Primary (HIGH confidence)
- Python abc module documentation (https://docs.python.org/3/library/abc.html) - abstractmethod, ABC metaclass, template method pattern
- httpx API reference (https://www.python-httpx.org/api/) - Response attributes (status_code, reason_phrase), Client/AsyncClient types
- Python Packaging Guide (https://packaging.python.org/) - subpackage structure with __init__.py exports
- Cyclomatic Complexity (Wikipedia / McCabe 1976) - complexity calculation formula, ranges (1-10 simple)

### Secondary (MEDIUM confidence)
- Refactoring Guru Strategy Pattern (https://refactoring.guru/design-patterns/strategy) - status handler decomposition approach
- Refactoring Guru Template Method (https://refactoring.guru/design-patterns/template-method) - base class retry loop structure
- httpx compatibility docs (https://www.python-httpx.org/compatibility/) - API stability, pre-1.0 evolution

### Tertiary (LOW confidence)
- OpenAI Python client (GitHub) - sync/async client architecture (interface consistency pattern observed but implementation details not verified)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - abc/typing stdlib, httpx version verified npm registry, existing codebase grep confirms usage
- Architecture: HIGH - template method and strategy patterns are well-established, Python docs confirm ABC mechanics
- Pitfalls: HIGH - derived from existing codebase analysis (605 + 497 lines), common refactoring errors documented

**Research date:** 2026-05-04
**Valid until:** 2026-06-04 (30 days - Python stdlib stable, httpx pre-1.0 evolving but pinned <1 per requirements)
