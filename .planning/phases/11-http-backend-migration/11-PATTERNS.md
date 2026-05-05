# Phase 11: HTTP Backend Migration - Pattern Map

**Mapped:** 2026-05-04
**Files analyzed:** 5
**Analogs found:** 5 / 5

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `meraki/session/sync.py` | transport | request-response | `meraki/session/sync.py` (self, requests-based) | self-upgrade |
| `meraki/session/async_.py` | transport | request-response | `meraki/session/async_.py` (self, aiohttp-based) | self-upgrade |
| `meraki/exceptions.py` | error-handler | - | `meraki/exceptions.py` (self, current attrs) | self-upgrade |
| `meraki/config.py` | config | - | `meraki/config.py` (self, current constant) | self-upgrade |
| `pyproject.toml` | config | - | `pyproject.toml` (self, current deps) | self-upgrade |

## Pattern Assignments

### `meraki/session/sync.py` (transport, request-response)

**Analog:** `meraki/session/sync.py` (current requests implementation)

**Current imports pattern** (lines 1-17):
```python
from __future__ import annotations

import time
import urllib.parse
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict

import requests

from meraki.common import (
    iterator_for_get_pages_bool,
    use_iterator_for_get_pages_setter,
)
from meraki.exceptions import SessionInputError
from meraki.session.base import SessionBase

if TYPE_CHECKING:
    import httpx
```

**Replace with httpx imports:**
```python
from __future__ import annotations

import time
import urllib.parse
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict

import httpx

from meraki.common import (
    iterator_for_get_pages_bool,
    use_iterator_for_get_pages_setter,
)
from meraki.exceptions import SessionInputError
from meraki.session.base import SessionBase
```

**Current session init pattern** (lines 30-36):
```python
def __init__(self, logger, api_key, **kwargs: Any) -> None:
    super().__init__(logger, api_key, **kwargs)

    # Initialize requests session
    self._req_session = requests.session()
    self._req_session.encoding = "utf-8"
    self._req_session.headers = self._build_headers()
```

**Replace with persistent httpx.Client:**
```python
def __init__(self, logger, api_key, **kwargs: Any) -> None:
    super().__init__(logger, api_key, **kwargs)

    # Build client config from session config
    client_kwargs = {}
    if self._certificate_path:
        client_kwargs["verify"] = self._certificate_path
    if self._requests_proxy:
        client_kwargs["proxy"] = self._requests_proxy
    client_kwargs["timeout"] = self._single_request_timeout
    
    # Persistent httpx client
    self._client = httpx.Client(**client_kwargs)
    self._client.headers.update(self._build_headers())
```

**Current _send_request pattern** (lines 46-49):
```python
def _send_request(self, method: str, url: str, **kwargs: Any) -> "httpx.Response":
    """Send HTTP request via requests.Session."""
    response = self._req_session.request(method, url, **kwargs)
    return response  # type: ignore[return-value]
```

**Replace with httpx client request:**
```python
def _send_request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
    """Send HTTP request via httpx.Client."""
    try:
        response = self._client.request(method, url, follow_redirects=False, **kwargs)
        return response
    except httpx.HTTPError as e:
        # Convert transport error to APIError (handled in base class retry loop)
        raise
```

**Current _transport_kwargs pattern** (lines 55-62):
```python
def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Map config to requests-specific kwargs (verify, proxies, timeout)."""
    if self._certificate_path:
        kwargs.setdefault("verify", self._certificate_path)
    if self._requests_proxy:
        kwargs.setdefault("proxies", {"https": self._requests_proxy})
    kwargs.setdefault("timeout", self._single_request_timeout)
    return kwargs
```

**Remove _transport_kwargs (httpx config at client level):**
```python
def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """No-op for httpx (config handled at client initialization)."""
    return kwargs
```

**Pagination pattern** (lines 117-302) - NO CHANGES NEEDED:
- Uses `response.links` (identical in httpx)
- Uses `response.json()` (identical in httpx)
- Uses `response.close()` (identical in httpx)
- Uses `response.content` (identical in httpx)

---

### `meraki/session/async_.py` (transport, request-response)

**Analog:** `meraki/session/async_.py` (current aiohttp implementation)

**Current imports pattern** (lines 1-18):
```python
from __future__ import annotations

import asyncio
import json
import random
import ssl
import urllib.parse
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict, Optional

import aiohttp

from meraki.common import validate_base_url, validate_user_agent
from meraki.config import AIO_MAXIMUM_CONCURRENT_REQUESTS
from meraki.exceptions import APIError, AsyncAPIError
from meraki.session.base import SessionBase

if TYPE_CHECKING:
    import httpx
```

**Replace with httpx imports (remove ssl, aiohttp):**
```python
from __future__ import annotations

import asyncio
import json
import random
import urllib.parse
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any, Dict, Optional

import httpx

from meraki.common import validate_base_url, validate_user_agent
from meraki.config import AIO_MAXIMUM_CONCURRENT_REQUESTS
from meraki.exceptions import APIError, AsyncAPIError
from meraki.session.base import SessionBase
```

**Current init pattern** (lines 32-63):
```python
def __init__(
    self,
    logger,
    api_key,
    maximum_concurrent_requests: int = AIO_MAXIMUM_CONCURRENT_REQUESTS,
    **kwargs: Any,
) -> None:
    super().__init__(logger, api_key, **kwargs)
    self._concurrent_requests_semaphore = asyncio.Semaphore(maximum_concurrent_requests)

    # Build headers dict (aiohttp uses dict, not session.headers)
    self._headers = self._build_headers()
    # Async user-agent prefix
    self._headers["User-Agent"] = f"python-meraki/aio-{self._version} " + validate_user_agent(
        self._be_geo_id, self._caller
    )

    # SSL context for certificate_path
    if self._certificate_path:
        self._sslcontext: Optional[ssl.SSLContext] = ssl.create_default_context()
        self._sslcontext.load_verify_locations(self._certificate_path)
    else:
        self._sslcontext = None

    # Initialize aiohttp session
    self._req_session = aiohttp.ClientSession(
        headers=self._headers,
        timeout=aiohttp.ClientTimeout(total=self._single_request_timeout),
    )

    # Trigger the property setter to bind the correct get_pages implementation
    self.use_iterator_for_get_pages = self._use_iterator_for_get_pages
```

**Replace with httpx.AsyncClient + Limits (remove semaphore):**
```python
def __init__(
    self,
    logger,
    api_key,
    maximum_concurrent_requests: int = AIO_MAXIMUM_CONCURRENT_REQUESTS,
    **kwargs: Any,
) -> None:
    super().__init__(logger, api_key, **kwargs)

    # Build headers dict
    headers = self._build_headers()
    # Async user-agent prefix
    headers["User-Agent"] = f"python-meraki/aio-{self._version} " + validate_user_agent(
        self._be_geo_id, self._caller
    )

    # Build client config
    client_kwargs = {
        "timeout": self._single_request_timeout,
        "limits": httpx.Limits(max_connections=maximum_concurrent_requests),
        "headers": headers,
    }
    if self._certificate_path:
        client_kwargs["verify"] = self._certificate_path
    if self._requests_proxy:
        client_kwargs["proxy"] = self._requests_proxy
    
    # Persistent async client
    self._client = httpx.AsyncClient(**client_kwargs)

    # Trigger the property setter to bind the correct get_pages implementation
    self.use_iterator_for_get_pages = self._use_iterator_for_get_pages
```

**Current _send_request pattern** (lines 81-85):
```python
async def _send_request(self, method: str, url: str, **kwargs: Any) -> "httpx.Response":
    """Send HTTP request via aiohttp with semaphore gating (D-08)."""
    async with self._concurrent_requests_semaphore:
        response = await self._req_session.request(method, url, **kwargs)
        return response  # type: ignore[return-value]
```

**Replace with httpx.AsyncClient request (no semaphore):**
```python
async def _send_request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
    """Send HTTP request via httpx.AsyncClient (pool limits enforce concurrency)."""
    try:
        response = await self._client.request(method, url, follow_redirects=False, **kwargs)
        return response
    except httpx.HTTPError as e:
        # Convert transport error to APIError (handled in base class retry loop)
        raise
```

**Current _transport_kwargs pattern** (lines 91-98):
```python
def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Map config to aiohttp-specific kwargs (ssl, proxy, timeout)."""
    if self._sslcontext:
        kwargs.setdefault("ssl", self._sslcontext)
    if self._requests_proxy:
        kwargs.setdefault("proxy", self._requests_proxy)
    kwargs.setdefault("timeout", self._single_request_timeout)
    return kwargs
```

**Remove _transport_kwargs (httpx config at client level):**
```python
def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """No-op for httpx (config handled at client initialization)."""
    return kwargs
```

**Current async request pattern** (lines 104-189):
- Line 137: `response.release()` -> change to `response.close()` (httpx method)
- Line 157: `response.status` -> change to `response.status_code` (httpx attr)
- Line 158: `response.reason` -> change to `response.reason_phrase` (httpx attr)

**Current async status handlers** (lines 195-329):
- Line 204: `response.reason` -> `response.reason_phrase`
- Line 205: `response.status` -> `response.status_code`
- Line 218: `await response.json(content_type=None)` -> `await response.json()` (httpx doesn't have content_type param)
- Line 244: `response.reason` -> `response.reason_phrase`
- Line 245: `response.status` -> `response.status_code`
- Line 272: `response.reason` -> `response.reason_phrase`
- Line 273: `response.status` -> `response.status_code`
- Line 277: `await response.json(content_type=None)` -> `await response.json()`
- Line 399: `response.release()` -> `response.close()`

**Current close pattern** (lines 519-520):
```python
async def close(self):
    await self._req_session.close()
```

**Replace with httpx aclose:**
```python
async def close(self):
    await self._client.aclose()
```

**Convenience methods** (lines 334-517):
- Line 339: `await response.json(content_type=None)` -> `await response.json()`
- Line 346: `await response.json(content_type=None)` -> `await response.json()`
- Line 438: `await response.json(content_type=None)` -> `await response.json()`
- Line 475: `await response.json(content_type=None)` -> `await response.json()`
- Line 477: `await response.json(content_type=None)` -> `await response.json()`
- Line 483: `await response.json(content_type=None)` -> `await response.json()`
- Line 504: `await response.json(content_type=None)` -> `await response.json()`
- Line 510: `await response.json(content_type=None)` -> `await response.json()`

---

### `meraki/exceptions.py` (error-handler)

**Analog:** `meraki/exceptions.py` (current exception classes)

**Current APIError pattern** (lines 36-52):
```python
class APIError(Exception):
    def __init__(self, metadata, response):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = self.response.status_code if self.response is not None and self.response.status_code else None
        self.reason = self.response.reason if self.response is not None and self.response.reason else None
        try:
            self.message = self.response.json() if self.response is not None and self.response.json() else None
        except ValueError:
            self.message = self.response.content[:100].decode("UTF-8").strip()
            if isinstance(self.message, str) and self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."
        super(APIError, self).__init__(f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}")

    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
```

**Update to use httpx response attributes:**
```python
class APIError(Exception):
    def __init__(self, metadata, response):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = self.response.status_code if self.response is not None and self.response.status_code else None
        # httpx uses .reason_phrase (not .reason)
        self.reason = self.response.reason_phrase if self.response is not None and hasattr(self.response, "reason_phrase") else None
        try:
            self.message = self.response.json() if self.response is not None and self.response.json() else None
        except ValueError:
            self.message = self.response.content[:100].decode("UTF-8").strip()
            if isinstance(self.message, str) and self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."
        super(APIError, self).__init__(f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}")

    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
```

**Current AsyncAPIError pattern** (lines 56-72):
```python
class AsyncAPIError(Exception):
    def __init__(self, metadata, response, message):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = response.status if response is not None and response.status else None
        self.reason = response.reason if response is not None and response.reason else None
        self.message = message
        if isinstance(self.message, str):
            self.message = self.message.strip()
            if self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."

        super().__init__(f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}")

    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
```

**Update to use httpx response attributes:**
```python
class AsyncAPIError(Exception):
    def __init__(self, metadata, response, message):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        # httpx uses .status_code (not .status) and .reason_phrase (not .reason)
        self.status = response.status_code if response is not None and hasattr(response, "status_code") else None
        self.reason = response.reason_phrase if response is not None and hasattr(response, "reason_phrase") else None
        self.message = message
        if isinstance(self.message, str):
            self.message = self.message.strip()
            if self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."

        super().__init__(f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}")

    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
```

---

### `meraki/config.py` (config)

**Analog:** `meraki/config.py` (current constant)

**Current AIO_MAXIMUM_CONCURRENT_REQUESTS constant** (lines 71-72):
```python
# Number of concurrent API requests for asynchronous class
AIO_MAXIMUM_CONCURRENT_REQUESTS = 8
```

**Update docstring to reflect httpx pool limits:**
```python
# Number of concurrent API requests for asynchronous class
# Maps to httpx.Limits(max_connections=N) in AsyncRestSession
AIO_MAXIMUM_CONCURRENT_REQUESTS = 8
```

---

### `pyproject.toml` (config)

**Analog:** `pyproject.toml` (current dependencies)

**Current dependencies** (lines 16-19):
```toml
dependencies = [
    "requests>=2.33.1,<3",
    "aiohttp>=3.13.5,<4",
]
```

**Replace with httpx:**
```toml
dependencies = [
    "httpx>=0.28,<1",
]
```

---

## Shared Patterns

### Exception Handling (Transport Errors)

**Source:** RESEARCH.md Pattern 2
**Apply to:** `meraki/session/sync.py`, `meraki/session/async_.py`

```python
import httpx
from meraki.exceptions import APIError, APIResponseError

# In _send_request methods, catch httpx.HTTPError as single typed exception
try:
    response = self._client.request(method, url, follow_redirects=False, **kwargs)
    return response
except httpx.HTTPError as e:
    # Base class retry loop will catch this and convert to APIError
    raise
```

### Response Attribute Migration (Breaking Change)

**Source:** httpx docs + CONTEXT.md D-04
**Apply to:** All files reading response attributes

| Old (requests/aiohttp) | New (httpx) | Files Affected |
|------------------------|-------------|----------------|
| `response.reason` | `response.reason_phrase` | `meraki/exceptions.py`, `meraki/session/async_.py` |
| `response.status` (aiohttp) | `response.status_code` | `meraki/session/async_.py` |
| `allow_redirects=False` | `follow_redirects=False` | `meraki/session/base.py` (line 187) |
| `await response.json(content_type=None)` | `await response.json()` | `meraki/session/async_.py` (8 occurrences) |
| `response.release()` (aiohttp) | `response.close()` | `meraki/session/async_.py` (2 occurrences) |
| `await session.close()` (aiohttp) | `await session.aclose()` | `meraki/session/async_.py` (line 520) |

### Connection Pooling (Persistent Client)

**Source:** RESEARCH.md Pattern 1
**Apply to:** `meraki/session/sync.py`, `meraki/session/async_.py`

**Sync pattern:**
```python
# In __init__
self._client = httpx.Client(
    timeout=self._single_request_timeout,
    verify=self._certificate_path or True,
    proxy=self._requests_proxy or None,
)
self._client.headers.update(self._build_headers())

# In _send_request
response = self._client.request(method, url, follow_redirects=False, **kwargs)
```

**Async pattern:**
```python
# In __init__
self._client = httpx.AsyncClient(
    timeout=self._single_request_timeout,
    limits=httpx.Limits(max_connections=maximum_concurrent_requests),
    verify=self._certificate_path or True,
    proxy=self._requests_proxy or None,
    headers=headers,
)

# In _send_request
response = await self._client.request(method, url, follow_redirects=False, **kwargs)

# In close()
await self._client.aclose()
```

### Redirect Handling

**Source:** `meraki/response_handler.py` + `meraki/session/base.py`
**Status:** NO CHANGES NEEDED

- `response.headers["Location"]` works identically in httpx (case-insensitive dict-like headers)
- Base class calls `_handle_redirect()` for 3xx responses (unchanged)
- httpx defaults to `follow_redirects=False` (same behavior as `allow_redirects=False` in requests)

### Pagination

**Source:** `meraki/session/sync.py` lines 117-302, `meraki/session/async_.py` lines 341-497
**Status:** NO CHANGES NEEDED

- `response.links` works identically in httpx (dict of link rels)
- `response.json()` works identically (async version loses `content_type=None` param)
- `response.content` works identically (bytes)
- `response.close()` / `response.release()` need rename for async only

---

## No Analog Found

None. All files are self-upgrades (replacing transport layer in existing files).

---

## Code Cleanup (Phase 9 Transition Complete)

**Source:** CONTEXT.md D-07

- **DELETE:** `meraki/rest_session.py` lines 41-107 (old `encode_params` function, if file still exists)
- **VERIFY:** Codebase only uses `meraki.encoding.encode_meraki_params` (Phase 9 stdlib encoder)

Search for old function:
```bash
grep -r "def encode_params" meraki/
```

Expected: No matches (Phase 9 already removed). If matches found, delete the function.

---

## Test Mock Updates

**Source:** `tests/unit/test_session_base.py`, `tests/unit/test_rest_session.py`

**Current mock pattern** (test_session_base.py lines 63-83):
```python
def _mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=b'{"ok":true}',
):
    """Create a mock httpx-like response."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.reason_phrase = reason_phrase
    resp.headers = headers or {}
    resp.content = content
    if json_data is not None:
        resp.json.return_value = json_data
    else:
        try:
            resp.json.return_value = json.loads(content) if content.strip() else None
        except (json.JSONDecodeError, ValueError):
            resp.json.side_effect = ValueError("No JSON")
    return resp
```

**Status:** Already httpx-compatible (uses `reason_phrase`, `status_code`). Keep as-is.

**Current sync mock pattern** (test_rest_session.py lines 39-56):
```python
def _mock_response(
    status_code=200,
    json_data=None,
    reason="OK",
    headers=None,
    content=b'{"ok":true}',
    links=None,
):
    resp = MagicMock(spec=requests.Response)
    resp.status_code = status_code
    resp.reason = reason
    resp.reason_phrase = reason
    resp.headers = headers or {}
    resp.content = content
    resp.links = links or {}
    resp.json.return_value = json_data if json_data is not None else {"ok": True}
    resp.close = MagicMock()
    return resp
```

**Update to httpx.Response spec:**
```python
def _mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=b'{"ok":true}',
    links=None,
):
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.reason_phrase = reason_phrase
    resp.headers = headers or {}
    resp.content = content
    resp.links = links or {}
    resp.json.return_value = json_data if json_data is not None else {"ok": True}
    resp.close = MagicMock()
    return resp
```

---

## Metadata

**Analog search scope:** `meraki/session/`, `meraki/exceptions.py`, `meraki/config.py`, `pyproject.toml`, `tests/unit/`
**Files scanned:** 5 source files, 3 test files
**Pattern extraction date:** 2026-05-04

**Key insights:**

1. **Persistent client pattern:** Both sync and async sessions use persistent httpx clients initialized in `__init__` (not per-request). Timeout, proxy, verify all configured at client level (not per-request kwargs).

2. **Concurrency control:** AsyncRestSession removes `asyncio.Semaphore`, uses `httpx.Limits(max_connections=N)` instead. Config constant `AIO_MAXIMUM_CONCURRENT_REQUESTS` preserved for backward compat.

3. **Response attributes:** Breaking changes documented in HTTPX-MIGRATION.md (per D-04):
   - `.reason` -> `.reason_phrase`
   - `.status` (aiohttp) -> `.status_code`
   - `allow_redirects` -> `follow_redirects`
   - `content_type=None` in `.json()` removed

4. **Exception handling:** Catch `httpx.HTTPError` as single typed exception (covers ConnectTimeout, ReadTimeout, etc.). Base class retry loop converts to APIError.

5. **No changes needed:** Pagination, redirect handling, response body parsing all work identically with httpx.

6. **Test mocks:** `test_session_base.py` already httpx-compatible. `test_rest_session.py` needs spec update from `requests.Response` to `httpx.Response`.
