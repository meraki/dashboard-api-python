# Architecture

**Analysis Date:** 2026-04-29

## Pattern Overview

**Overall:** Multi-layer façade pattern wrapping the Meraki Dashboard API with configurable HTTP session management. The SDK provides both synchronous (requests-based) and asynchronous (aiohttp-based) interfaces, each exposing identical API scopes through separate entry points.

**Key Characteristics:**
- Code generated from OpenAPI specification v1 (auto-generated from Meraki OpenAPI spec)
- Dual API access patterns (synchronous DashboardAPI and async AsyncDashboardAPI)
- Centralized HTTP session handling with retry logic, pagination, and rate limiting
- Scoped API endpoints organized by resource type (organizations, networks, devices, etc.)
- Batch action support through separate Batch helper classes
- Configurable logging, timeouts, retries, and kwarg validation

## Layers

**Entry Point Layer:**
- Purpose: Public API initialization and scope access
- Location: `meraki/__init__.py` (sync), `meraki/aio/__init__.py` (async)
- Contains: DashboardAPI and AsyncDashboardAPI classes with scope properties
- Depends on: RestSession/AsyncRestSession, all API scope classes
- Used by: End users instantiating the client

**Scope/Resource Layer:**
- Purpose: Group operations by Meraki resource type (Organizations, Networks, Devices, etc.)
- Location: `meraki/api/{scope}.py` (sync), `meraki/aio/api/{scope}.py` (async)
- Contains: Classes like Organizations, Networks, Devices, Appliance, Camera, etc. (17 total scopes)
- Depends on: RestSession.get/post/put/delete methods
- Used by: Users calling operations like `dashboard.organizations.getOrganizations()`

**Batch Helper Layer:**
- Purpose: Specialized classes for batch operations (Action Batches)
- Location: `meraki/api/batch/{scope}.py`
- Contains: ActionBatchOrganizations, ActionBatchNetworks, etc.
- Depends on: Batch class aggregation
- Used by: Users batching multiple API calls for concurrent execution

**HTTP Session Layer:**
- Purpose: Handle all HTTP communication, retry logic, rate limiting, pagination
- Location: `meraki/rest_session.py` (sync), `meraki/aio/rest_session.py` (async)
- Contains: RestSession and AsyncRestSession classes
- Depends on: requests (sync), aiohttp (async), response_handler, common utilities
- Used by: All scope classes making actual API calls

**Configuration Layer:**
- Purpose: Define default constants and environment variable names
- Location: `meraki/config.py`
- Contains: API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, timeouts, retry policies, logging options
- Depends on: Nothing (config only)
- Used by: DashboardAPI, AsyncDashboardAPI, RestSession, AsyncRestSession initialization

**Utility Layer:**
- Purpose: Shared helpers for validation, logging, parameter encoding
- Location: `meraki/common.py`, `meraki/response_handler.py`
- Contains: Python version check, base URL validation, iterator logic, user agent formatting
- Depends on: Nothing (utilities only)
- Used by: RestSession, common initialization

**Error Handling Layer:**
- Purpose: Exception types for API and validation errors
- Location: `meraki/exceptions.py`
- Contains: APIKeyError, APIError, AsyncAPIError, PythonVersionError, SessionInputError
- Depends on: Nothing (exceptions only)
- Used by: RestSession, AsyncRestSession, DashboardAPI initialization

## Data Flow

**Synchronous Request Flow:**

1. User calls `dashboard.organizations.getOrganizations()`
2. Organizations instance method builds metadata dict with operation name and tags
3. Method constructs resource path and extracts valid kwargs into params/payload dicts
4. Organizations calls `self._session.get(metadata, resource, params)`
5. RestSession.get() calls request() with metadata, resource, params
6. request() performs retry loop with rate limit/4xx error handling
7. requests library makes actual HTTP call with Bearer token auth header
8. Response is logged and returned to Organizations method
9. Organizations method returns data to caller

**Asynchronous Request Flow:**

1. User calls `await aiomeraki.organizations.getOrganizations()`
2. Same scope method structure, but AsyncOrganizations calls `await self._session.get()`
3. AsyncRestSession.get() calls request() coroutine with same parameters
4. request() performs retry loop with rate limit/4xx error handling using aiohttp
5. aiohttp client makes actual HTTP call
6. Response awaited and returned through scope method
7. Caller receives awaitable result

**Pagination Flow:**

1. User calls listOperation with total_pages parameter
2. get_pages() is called (iterator or legacy mode)
3. Iterator mode: returns generator yielding individual items across pages
4. Legacy mode: yields complete page lists based on total_pages/perPage
5. Handles startingAfter/endingBefore tokens in Link headers for pagination

**State Management:**

- Session state: Stored in RestSession/AsyncRestSession instance (headers, config, retry policy)
- Per-request state: Metadata dict carries operation metadata for logging/error handling
- User agent state: Dynamically constructed with caller identifier and SDK version
- Pagination state: Tracked via response Link headers, not stored between calls

## Key Abstractions

**Session Abstraction (RestSession/AsyncRestSession):**
- Purpose: Shields scope classes from HTTP implementation details
- Examples: `meraki/rest_session.py`, `meraki/aio/rest_session.py`
- Pattern: Both implement identical interface (get, post, put, delete, get_pages) with different transport
- Allows scope code to be generated once, shared between sync/async via templates

**Scope Operation Pattern:**
- Purpose: Standardized method structure for all API operations
- Examples: `meraki/api/organizations.py`, `meraki/api/networks.py`
- Pattern: kwargs.update(locals()), metadata dict, resource path building, param extraction, session call
- Allows generated code to consistently handle pagination, kwarg validation, URL encoding

**Parameter Encoding Abstraction:**
- Purpose: Support complex query parameter types (array of objects)
- Examples: `meraki/rest_session.py` encode_params() monkey patch
- Pattern: Custom requests library override for handling {"param": [{"key_1":"value_1"}]} => ?param[]key_1=value_1
- Necessary for Meraki API's complex query parameter requirements

**Batch Helper Pattern:**
- Purpose: Provide staging for Action Batch requests without session dependency
- Examples: `meraki/api/batch/organizations.py`
- Pattern: Stateless helper objects building batch payloads, not executing requests
- Separate from session because batches are composed then submitted separately

**Metadata Dictionary:**
- Purpose: Carry operation context through request lifecycle for logging/error reporting
- Structure: {"tags": ["scope_name", "read/configure"], "operation": "operationName"}
- Usage: Extracted from exception handlers and logged with requests for audit trail

## Entry Points

**DashboardAPI (Sync):**
- Location: `meraki/__init__.py`
- Triggers: `api_instance = meraki.DashboardAPI(api_key="...", ...)`
- Responsibilities: Initialize RestSession with config, instantiate all scope properties, manage logger setup
- Configuration: 17 parameters controlling auth, retries, logging, simulation, pagination mode

**AsyncDashboardAPI (Async):**
- Location: `meraki/aio/__init__.py`
- Triggers: `async with meraki.aio.AsyncDashboardAPI() as api_instance:`
- Responsibilities: Same as sync but with AsyncRestSession, manages async context manager for session cleanup
- Configuration: Identical 17 parameters plus AIO_MAXIMUM_CONCURRENT_REQUESTS

**Module import:**
- Location: `meraki/__init__.py`
- Triggers: `import meraki`
- Responsibilities: Exports DashboardAPI, config constants, version string
- No initialization required

## Error Handling

**Strategy:** Exceptions caught at session layer, re-raised with context as APIError/AsyncAPIError. User handles try/except at caller level.

**Patterns:**

- **Rate Limiting (429):** Caught in RestSession.request() retry loop, waits NGINX_429_RETRY_WAIT_TIME before retry
- **4XX Errors:** Caught in handle_4xx_errors(), optionally retried if RETRY_4XX_ERROR is true
- **5XX Errors:** Caught in request() retry loop, retried up to MAXIMUM_RETRIES times
- **API Key Missing:** Caught in DashboardAPI.__init__() before session creation, raises APIKeyError
- **Python Version:** Caught in RestSession.__init__(), raises PythonVersionError
- **Invalid Configuration:** Caught in common validation functions, raises SessionInputError with doc link
- **Response Parsing:** Caught in AsyncAPIError/APIError constructors, falls back to raw content if JSON parse fails

## Cross-Cutting Concerns

**Logging:** 
- Implementation: Standard logging module with file/console handlers configured in DashboardAPI.__init__()
- Per-call: RestSession logs request params before each call, logs response status after
- Redaction: API key masked to last 4 chars in log output
- Control: suppress_logging=True disables all logging; inherit_logging_config=True uses external logger

**Validation:**
- User agent format: validate_user_agent() regex check on MERAKI_PYTHON_SDK_CALLER format
- Base URL: reject_v0_base_url() prevents v0 API access, validate_base_url() whitelists domains
- Python version: check_python_version() enforces Python 3.10+
- Kwargs: Optional validate_kwargs mode logs warnings when unrecognized kwargs passed to operations

**Authentication:**
- Method: Bearer token in Authorization header, token from API_KEY_ENVIRONMENT_VARIABLE or parameter
- Per-call: RestSession sets header once at init, reused for all requests
- Security: Requires explicit API key provision or environment variable, fails fast if missing

**Retry Policy:**
- Rate limits: Waits NGINX_429_RETRY_WAIT_TIME (default 60s) before retry
- Action batch conflicts: Waits ACTION_BATCH_RETRY_WAIT_TIME (default 60s) before retry
- Network deletion conflicts: Waits NETWORK_DELETE_RETRY_WAIT_TIME (default 240s) before retry
- Other 4XX: Optionally retried if RETRY_4XX_ERROR enabled, waits RETRY_4XX_ERROR_WAIT_TIME
- 5XX: Retried up to MAXIMUM_RETRIES times with exponential backoff (implementation in RestSession.request())
