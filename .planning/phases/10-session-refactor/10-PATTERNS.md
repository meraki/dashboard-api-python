# Phase 10: Session Refactor - Pattern Map

**Mapped:** 2026-05-04
**Files analyzed:** 7 (4 new, 2 modified, 1 generator)
**Analogs found:** 7 / 7

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `meraki/session/base.py` | base-class | request-response | `meraki/rest_session.py` | role-match |
| `meraki/session/sync.py` | session | request-response | `meraki/rest_session.py` | exact |
| `meraki/session/async_.py` | session | request-response | `meraki/aio/rest_session.py` | exact |
| `meraki/session/__init__.py` | module | export | `meraki/api/__init__.py` | role-match |
| `meraki/__init__.py` | module | export | (existing) | exact |
| `meraki/aio/__init__.py` | module | export | (existing) | exact |
| `generator/generate_library.py` | generator | code-gen | (existing) | exact |

## Pattern Assignments

### `meraki/session/base.py` (base-class, request-response)

**Analog:** `meraki/rest_session.py`

**Imports pattern** (lines 1-39):
```python
import random
import urllib.parse
from datetime import datetime, timezone
import json
import time

from meraki._version import __version__
from meraki.common import (
    check_python_version,
    iterator_for_get_pages_bool,
    reject_v0_base_url,
    use_iterator_for_get_pages_setter,
    validate_base_url,
    validate_user_agent,
)
from meraki.config import (
    ACTION_BATCH_RETRY_WAIT_TIME,
    BE_GEO_ID,
    CERTIFICATE_PATH,
    DEFAULT_BASE_URL,
    MAXIMUM_RETRIES,
    MERAKI_PYTHON_SDK_CALLER,
    NETWORK_DELETE_RETRY_WAIT_TIME,
    NGINX_429_RETRY_WAIT_TIME,
    REQUESTS_PROXY,
    RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME,
    SIMULATE_API_CALLS,
    SINGLE_REQUEST_TIMEOUT,
    USE_ITERATOR_FOR_GET_PAGES,
    WAIT_ON_RATE_LIMIT,
)
from meraki.exceptions import APIError, APIResponseError, SessionInputError
from meraki.response_handler import handle_3xx
```

**Constructor pattern** (lines 127-198):
```python
class RestSession(object):
    def __init__(
        self,
        logger,
        api_key,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=SINGLE_REQUEST_TIMEOUT,
        certificate_path=CERTIFICATE_PATH,
        requests_proxy=REQUESTS_PROXY,
        wait_on_rate_limit=WAIT_ON_RATE_LIMIT,
        nginx_429_retry_wait_time=NGINX_429_RETRY_WAIT_TIME,
        action_batch_retry_wait_time=ACTION_BATCH_RETRY_WAIT_TIME,
        network_delete_retry_wait_time=NETWORK_DELETE_RETRY_WAIT_TIME,
        retry_4xx_error=RETRY_4XX_ERROR,
        retry_4xx_error_wait_time=RETRY_4XX_ERROR_WAIT_TIME,
        maximum_retries=MAXIMUM_RETRIES,
        simulate=SIMULATE_API_CALLS,
        be_geo_id=BE_GEO_ID,
        caller=MERAKI_PYTHON_SDK_CALLER,
        use_iterator_for_get_pages=USE_ITERATOR_FOR_GET_PAGES,
        validate_kwargs=False,
    ):
        super(RestSession, self).__init__()

        # Initialize attributes and properties
        self._version = __version__
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._requests_proxy = requests_proxy
        self._wait_on_rate_limit = wait_on_rate_limit
        self._nginx_429_retry_wait_time = nginx_429_retry_wait_time
        self._action_batch_retry_wait_time = action_batch_retry_wait_time
        self._network_delete_retry_wait_time = network_delete_retry_wait_time
        self._retry_4xx_error = retry_4xx_error
        self._retry_4xx_error_wait_time = retry_4xx_error_wait_time
        self._maximum_retries = maximum_retries
        self._simulate = simulate
        self._be_geo_id = be_geo_id
        self._caller = caller
        self.use_iterator_for_get_pages = use_iterator_for_get_pages
        self._validate_kwargs = validate_kwargs

        # Check the Python version
        check_python_version()

        # Check base URL
        reject_v0_base_url(self)

        # Log API calls
        self._logger = logger
        self._parameters = {"version": self._version}
        self._parameters.update(locals())
        self._parameters.pop("self")
        self._parameters.pop("logger")
        self._parameters.pop("__class__")
        self._parameters["api_key"] = "*" * 36 + self._api_key[-4:]
        if self._logger:
            self._logger.info(f"Meraki dashboard API session initialized with these parameters: {self._parameters}")
```

**Retry loop structure** (lines 207-319):
```python
def request(self, metadata, method, url, **kwargs):
    # Metadata on endpoint
    tag = metadata["tags"][0]
    operation = metadata["operation"]

    # Update request kwargs with session defaults
    self.prepare_request(kwargs)

    # Ensure proper base URL
    abs_url = validate_base_url(self, url)

    # Set the maximum number of retries
    retries = self._maximum_retries

    # Option to simulate non-safe API calls without actually sending them
    if self._logger:
        self._logger.debug(metadata)
    if self._simulate and method != "GET":
        if self._logger:
            self._logger.info(f"{tag}, {operation} - SIMULATED")
        return None
    else:
        response = None
        while retries > 0:
            # Make the HTTP request to the API endpoint
            try:
                if response:
                    response.close()
                if self._logger:
                    self._logger.info(f"{method} {abs_url}")
                response = self._req_session.request(method, abs_url, allow_redirects=False, **kwargs)
                reason = response.reason if response.reason else ""
                status = response.status_code
            except requests.exceptions.RequestException as e:
                if self._logger:
                    self._logger.warning(f"{tag}, {operation} - {e}, retrying in 1 second")
                time.sleep(1)
                retries -= 1
                if retries == 0:
                    if e.response and e.response.status_code:
                        raise APIError(
                            metadata,
                            APIResponseError(e.__class__.__name__, e.response.status_code, str(e)),
                        )
                    else:
                        raise APIError(
                            metadata,
                            APIResponseError(e.__class__.__name__, 503, str(e)),
                        )
                else:
                    continue

            match status:
                # Handle 3xx redirects automatically
                case status if 300 <= status < 400:
                    abs_url = handle_3xx(self, response)
                # Handle 2xx success
                case status if 200 <= status < 300:
                    # [success handler logic]
                # Handle rate limiting
                case 429:
                    # [429 handler logic]
                # Handle 5xx errors
                case status if 500 <= status:
                    # [5xx handler logic]
                # Handle other 4xx errors
                case status if status != 429 and 400 <= status < 500:
                    retries = self.handle_4xx_errors(metadata, operation, reason, response, retries, status, tag)

    return response
```

**Success handler pattern** (lines 264-285):
```python
case status if 200 <= status < 300:
    if "page" in metadata:
        counter = metadata["page"]
        if self._logger:
            self._logger.info(f"{tag}, {operation}; page {counter} - {status} {reason}")
    else:
        if self._logger:
            self._logger.info(f"{tag}, {operation} - {status} {reason}")
    # For non-empty response to GET, ensure valid JSON
    try:
        if method == "GET" and response.content.strip():
            response.json()
        return response
    except json.decoder.JSONDecodeError as e:
        if self._logger:
            self._logger.warning(f"{tag}, {operation} - {e}, retrying in 1 second")
        time.sleep(1)
        retries -= 1
        if retries == 0:
            raise APIError(metadata, response)
        else:
            continue
```

**Rate limit handler pattern** (lines 287-306):
```python
case 429:
    # Retry if 429 retries are enabled and there are retries left
    if self._wait_on_rate_limit and retries > 0:
        if "Retry-After" in response.headers:
            wait = int(response.headers["Retry-After"])
        else:
            attempt = self._maximum_retries - retries
            wait = min(
                (2**attempt) * (1 + random.random()),
                self._nginx_429_retry_wait_time,
            )
        if self._logger:
            self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
        time.sleep(wait)
        retries -= 1
        if retries == 0:
            raise APIError(metadata, response)
    # We're either out of retries or the client told us not to retry
    else:
        raise APIError(metadata, response)
```

**Server error handler pattern** (lines 308-314):
```python
case status if 500 <= status:
    if self._logger:
        self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in 1 second")
    time.sleep(1)
    retries -= 1
    if retries == 0:
        raise APIError(metadata, response)
```

**Client error handler pattern** (lines 328-370):
```python
def handle_4xx_errors(self, metadata, operation, reason, response, retries, status, tag):
    try:
        message = response.json()
        message_is_dict = True
    except ValueError:
        message = response.content[:100]
        message_is_dict = False

    # Check specifically for concurrency errors
    network_delete_concurrency_error_text = "concurrent"
    action_batch_concurrency_error_text = "executing batches"

    # First, we check for network deletion concurrency errors
    if operation == "deleteNetwork" and response.status_code == 400:
        # message['errors'][0] is the first error, and it contains helpful text
        # here we use it to confirm that the 400 error is related to concurrent requests
        if network_delete_concurrency_error_text in message["errors"][0]:
            wait = random.randint(30, self._network_delete_retry_wait_time)
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
            time.sleep(wait)
            retries -= 1
        else:
            raise APIError(metadata, response)
    # Second, we check for action batch concurrency errors
    elif action_batch_concurrency_error_text in str(message).lower():
        wait = self._action_batch_retry_wait_time
        if self._logger:
            self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
        time.sleep(wait)
        retries -= 1
    # 4xx retry enabled
    elif self._retry_4xx_error and retries > 0:
        wait = random.randint(1, self._retry_4xx_error_wait_time)
        if self._logger:
            self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
        time.sleep(wait)
        retries -= 1
    else:
        if self._logger:
            self._logger.error(f"{tag}, {operation} - {status} {reason}, {message}")
        raise APIError(metadata, response)
    return retries
```

**Transport kwargs pattern** (lines 321-326):
```python
def prepare_request(self, kwargs):
    if self._certificate_path:
        kwargs.setdefault("verify", self._certificate_path)
    if self._requests_proxy:
        kwargs.setdefault("proxies", {"https": self._requests_proxy})
    kwargs.setdefault("timeout", self._single_request_timeout)
```

---

### `meraki/session/sync.py` (session, request-response)

**Analog:** `meraki/rest_session.py`

**Imports pattern** (lines 1-8):
```python
import requests

from meraki._version import __version__
from meraki.common import validate_user_agent
from meraki.config import DEFAULT_BASE_URL, SINGLE_REQUEST_TIMEOUT
```

**Session initialization** (lines 171-186):
```python
# Initialize a new `requests` session
self._req_session = requests.session()
self._req_session.encoding = "utf-8"

# Update the headers for the session
self._req_session.headers = {
    "Authorization": "Bearer " + self._api_key,
    "Content-Type": "application/json",
    "User-Agent": f"python-meraki/{self._version} " + validate_user_agent(self._be_geo_id, self._caller),
}
```

**Transport send pattern** (line 237):
```python
response = self._req_session.request(method, abs_url, allow_redirects=False, **kwargs)
```

**Sleep pattern** (line 243):
```python
time.sleep(1)
```

**Status code extraction** (line 239):
```python
status = response.status_code
```

---

### `meraki/session/async_.py` (session, request-response)

**Analog:** `meraki/aio/rest_session.py`

**Imports pattern** (lines 1-9):
```python
import asyncio
import json
import random
import ssl
import urllib.parse
from datetime import datetime

import aiohttp
```

**Session initialization** (lines 90-104):
```python
# Update the headers for the session
self._headers = {
    "Authorization": "Bearer " + self._api_key,
    "Content-Type": "application/json",
    "User-Agent": f"python-meraki/aio-{self._version} " + validate_user_agent(self._be_geo_id, self._caller),
}
if self._certificate_path:
    self._sslcontext = ssl.create_default_context()
    self._sslcontext.load_verify_locations(certificate_path)

# Initialize a new `aiohttp` session
self._req_session = aiohttp.ClientSession(
    headers=self._headers,
    timeout=aiohttp.ClientTimeout(total=single_request_timeout),
)
```

**Concurrency semaphore pattern** (lines 78-79):
```python
self._concurrent_requests_semaphore = asyncio.Semaphore(maximum_concurrent_requests)
```

**Transport send pattern with semaphore** (lines 179-185):
```python
# Acquire semaphore only for the HTTP call, not retry waits
async with self._concurrent_requests_semaphore:
    try:
        if self._logger:
            self._logger.info(f"{method} {abs_url}")
        response = await self._req_session.request(method, abs_url, **kwargs)
```

**Sleep pattern** (line 189):
```python
await asyncio.sleep(1)
```

**Status code extraction** (line 185):
```python
status = response.status
```

**Transport kwargs pattern** (lines 139-143):
```python
# Update request kwargs with session defaults
if self._certificate_path:
    kwargs.setdefault("ssl", self._sslcontext)
if self._requests_proxy:
    kwargs.setdefault("proxy", self._requests_proxy)
kwargs.setdefault("timeout", self._single_request_timeout)
```

**URL validation pattern** (lines 145-157):
```python
# Ensure proper base URL
allowed_domains = ["meraki.com", "meraki.cn"]

# aiohttp manipulates URLs as instances of the yarl.URL class
if not isinstance(url, str):
    url = str(url)

parsed_url = urllib.parse.urlparse(url)

if any(domain in parsed_url.netloc for domain in allowed_domains):
    abs_url = url
else:
    abs_url = self._base_url + url
```

---

### `meraki/session/__init__.py` (module, export)

**Analog:** `meraki/api/__init__.py`

**Export pattern** (lines 1-22 from api/__init__.py):
```python
from meraki.api.administered import Administered
from meraki.api.appliance import Appliance

# Batch class imports
from meraki.api.batch import Batch
from meraki.api.camera import Camera
# ... more imports
```

**Apply to new file:**
```python
"""Session implementations for Meraki Dashboard API.

Exports:
    SessionBase: Abstract base class with shared logic
    RestSession: Sync session (meraki.session.sync)
    AsyncRestSession: Async session (meraki.session.async_)
"""

from meraki.session.base import SessionBase
from meraki.session.sync import RestSession
from meraki.session.async_ import AsyncRestSession

__all__ = ["SessionBase", "RestSession", "AsyncRestSession"]
```

---

### `meraki/__init__.py` (module, export)

**Analog:** (existing file)

**Current import** (line 50):
```python
from meraki.rest_session import RestSession
```

**Update to:**
```python
from meraki.session.sync import RestSession
```

---

### `meraki/aio/__init__.py` (module, export)

**Analog:** (existing file)

**Current import** (line 20):
```python
from meraki.aio.rest_session import AsyncRestSession
```

**Update to:**
```python
from meraki.session.async_ import AsyncRestSession
```

---

### `generator/generate_library.py` (generator, code-gen)

**Analog:** (existing file)

**Non-generated files list** (lines 90-100):
```python
# Files that are not generated
non_generated = [
    "__init__.py",
    "_version.py",
    "config.py",
    "common.py",
    "exceptions.py",
    "response_handler.py",
    "rest_session.py",          # REMOVE
    "api/__init__.py",
    "aio/__init__.py",
    "aio/rest_session.py",      # REMOVE
```

**Update to:**
```python
# Files that are not generated
non_generated = [
    "__init__.py",
    "_version.py",
    "config.py",
    "common.py",
    "exceptions.py",
    "response_handler.py",
    "encoding.py",
    "session/__init__.py",      # ADD
    "session/base.py",          # ADD
    "session/sync.py",          # ADD
    "session/async_.py",        # ADD
    "api/__init__.py",
    "aio/__init__.py",
```

---

## Shared Patterns

### User Agent Generation
**Source:** `meraki/common.py` (lines 26-51)
**Apply to:** SessionBase constructor
```python
def validate_user_agent(be_geo_id, caller):
    # Generate extended portion of the User Agent
    # Validate that it follows the expected format
    user_agent = dict()

    allowed_format_in_regex = r"^[A-Za-z0-9]+(?:/[0-9A-Za-z]+(?:\.[0-9A-Za-z]+)*(-[a-z]+)?)? [A-Za-z-0-9]+$"

    if caller and re.match(allowed_format_in_regex, caller):
        user_agent["caller"] = caller
    elif be_geo_id and re.match(allowed_format_in_regex, be_geo_id):
        user_agent["caller"] = be_geo_id
    else:
        if caller:
            message = "Please follow the user agent format prescribed in our User Agents guide, available here:"
            doc_link = "https://developer.cisco.com/meraki/api-v1/user-agents-overview/"
            raise SessionInputError("MERAKI_PTYHON_SDK_CALLER", caller, message, doc_link)
        elif be_geo_id:
            message = "Use of be_geo_id is deprecated. Please use the argument MERAKI_PTYHON_SDK_CALLER instead."
            doc_link = "https://developer.cisco.com/meraki/api-v1/user-agents-overview/"
            raise SessionInputError("BE_GEO_ID", caller, message, doc_link)
        else:
            user_agent["caller"] = "unidentified"

    caller_string = f"Caller/({user_agent['caller']})"

    return caller_string
```

### URL Validation
**Source:** `meraki/common.py` (lines 77-90)
**Apply to:** SessionBase request method
```python
def validate_base_url(self, url):
    allowed_domains = [
        "meraki.com",
        "meraki.ca",
        "meraki.cn",
        "meraki.in",
        "gov-meraki.com",
    ]
    parsed_url = urllib.parse.urlparse(url)
    if any(domain in parsed_url.netloc for domain in allowed_domains):
        abs_url = url
    else:
        abs_url = self._base_url + url
    return abs_url
```

### Python Version Check
**Source:** `meraki/common.py` (lines 9-23)
**Apply to:** SessionBase constructor
```python
def check_python_version():
    # Check minimum Python version

    if not (int(platform.python_version_tuple()[0]) == 3 and int(platform.python_version_tuple()[1]) >= 10):
        message = (
            f"This library requires Python 3.10 at minimum. Python versions 3.8 and below are EOL as of October 2024"
            f" or earlier. End of life Python versions no longer receive security updates since reaching end of life"
            f" and of support per the Python maintainers. Your interpreter version is: {platform.python_version()}. "
            f"Please consult the readme at your convenience: https://github.com/meraki/dashboard-api-python "
            f"Additional details: "
            f"python_version_tuple()[0] = {platform.python_version_tuple()[0]}; "
            f"python_version_tuple()[1] = {platform.python_version_tuple()[1]} "
        )

        raise PythonVersionError(message)
```

### Base URL Rejection
**Source:** `meraki/common.py` (lines 54-61)
**Apply to:** SessionBase constructor
```python
def reject_v0_base_url(self):
    if "v0" in self._base_url:
        sys.exit(
            f"This library does not support dashboard API v0 ({self._base_url} was configured as the base"
            f" URL).  API v0 has been end of life since 2020 August 5."
        )
    elif self._base_url[-1] == "/":
        self._base_url = self._base_url[:-1]
```

### Redirect Handler
**Source:** `meraki/response_handler.py` (lines 1-7)
**Apply to:** SessionBase redirect handler
```python
def handle_3xx(self, response):
    abs_url = response.headers["Location"]
    substring = "meraki.com/api/v"
    if substring not in abs_url:
        substring = "meraki.cn/api/v"
    self._base_url = abs_url[: abs_url.find(substring) + len(substring) + 1]
    return abs_url
```

### API Key Masking for Logs
**Source:** `meraki/rest_session.py` (lines 189-197)
**Apply to:** SessionBase constructor
```python
# Log API calls
self._logger = logger
self._parameters = {"version": self._version}
self._parameters.update(locals())
self._parameters.pop("self")
self._parameters.pop("logger")
self._parameters.pop("__class__")
self._parameters["api_key"] = "*" * 36 + self._api_key[-4:]
if self._logger:
    self._logger.info(f"Meraki dashboard API session initialized with these parameters: {self._parameters}")
```

---

## No Analog Found

None. All files have clear patterns from existing codebase.

---

## Metadata

**Analog search scope:**
- `meraki/*.py` (session implementations)
- `meraki/aio/*.py` (async session)
- `meraki/common.py` (shared utilities)
- `meraki/response_handler.py` (redirect handler)
- `generator/generate_library.py` (code generation)

**Files scanned:** 7
**Pattern extraction date:** 2026-05-04

**Key insights:**
1. Both sessions share 80%+ identical logic (constructor, retry loop, status handlers)
2. Transport differences isolated to: session init, request call, sleep method, status attribute name
3. Async-only: concurrency semaphore (lines 78-79, 179-185 in aio/rest_session.py)
4. Generator's non_generated list (lines 90-100) must be updated for new subpackage structure
5. `meraki/encoding.py` already extracted from Phase 9, ready for base class import
6. All shared utilities already in `meraki/common.py`, no extraction needed
