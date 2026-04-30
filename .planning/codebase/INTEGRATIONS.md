# External Integrations

**Analysis Date:** 2026-04-29

## APIs & External Services

**Cisco Meraki Dashboard API:**
- REST API for network, device, and organization management
  - Endpoint: `https://api.meraki.com/api/v1` (default) with regional alternatives
  - SDK/Client: requests (sync), aiohttp (async)
  - Auth: Bearer token via `Authorization: Bearer [API_KEY]` header
  - OpenAPI Spec: Available at `https://api.meraki.com/api/v1/openapiSpec`
  - Purpose: Core SDK interfaces all Meraki cloud-managed platform features via 16+ scoped API classes
  - Location: `meraki/api/` and `meraki/aio/api/` contain generated endpoint implementations

**API Scopes/Modules:**
The SDK exposes the following API scope classes, each wrapping a category of Dashboard API endpoints:
- Organizations - Org management (`meraki/api/organizations.py`)
- Networks - Network configuration (`meraki/api/networks.py`)
- Devices - Device management (`meraki/api/devices.py`)
- Wireless - Wireless networks (`meraki/api/wireless.py`)
- Switch - Switch configuration (`meraki/api/switch.py`)
- Appliance - Security appliance (`meraki/api/appliance.py`)
- Camera - Camera settings (`meraki/api/camera.py`)
- Sensor - Environmental sensors (`meraki/api/sensor.py`)
- Licensing - License management (`meraki/api/licensing.py`)
- Insight - Network analytics (`meraki/api/insight.py`)
- SM - System Manager (`meraki/api/sm.py`)
- CellularGateway - Cellular gateway settings (`meraki/api/cellularGateway.py`)
- CampusGateway - Campus gateway settings (`meraki/api/campusGateway.py`)
- WirelessController - Wireless controller (`meraki/api/wirelessController.py`)
- Spaces - Workspace management (`meraki/api/spaces.py`)
- Administered - Administered identities (`meraki/api/administered.py`)

## Data Storage

**Databases:**
- None - This is a client library, not an application with persistent storage
- All data originates from Cisco Meraki Dashboard cloud platform

**File Storage:**
- Local filesystem only - Logging output stored to disk if enabled
  - Default log location: Current working directory
  - Log file format: `meraki_api_[YYYY-MM-DD_HH-MM-SS].log`
  - Configurable via `log_path` and `log_file_prefix` parameters

**Caching:**
- None - Requests library handles HTTP caching per standard HTTP headers
- Application developers can implement caching layers on top of SDK calls

## Authentication & Identity

**Auth Provider:**
- Custom (API Key-based)
- Implementation: HTTP Bearer token via `Authorization` header
- API Key source: Environment variable `MERAKI_DASHBOARD_API_KEY` or constructor parameter
- Key format: Long hexadecimal string issued via Meraki Dashboard UI
- No OAuth, no session management
- Location: `meraki/rest_session.py` (line 6-96 in sync), `meraki/aio/rest_session.py` (async equivalent)

## Monitoring & Observability

**Error Tracking:**
- None - Library provides exception objects for caller to handle
- Custom exception classes: `APIKeyError`, `APIError`, `AsyncAPIError`, `SessionInputError`
- Location: `meraki/exceptions.py`

**Logs:**
- Python logging framework (stdlib)
- Default: Logs to both console and rotating file if enabled
- Can inherit external logger instance via `inherit_logging_config=True`
- Log levels: DEBUG for full request/response, INFO for console output
- Configurable via:
  - `suppress_logging=False` to enable logging
  - `output_log=True` to write to file
  - `print_console=True` for console output
  - `log_path` and `log_file_prefix` for custom locations
- Location: Configured in `meraki/__init__.py` (lines 127-156)

## CI/CD & Deployment

**Hosting:**
- PyPI (Python Package Index) - Distribution point for pip/uv installations
- GitHub (source code and issue tracking)
- GitHub Actions - CI pipeline for test execution

**CI Pipeline:**
- pytest runs on PR and main branch commits via GitHub Actions
- Coverage requirement: 90% minimum (enforced in pyproject.toml)
- Linting: flake8 and ruff applied via pre-commit hooks
- Integration tests available in `tests/integration/` (separate from unit tests)

## Environment Configuration

**Required env vars:**
- `MERAKI_DASHBOARD_API_KEY` - Meraki Dashboard API authentication key (required)

**Optional env vars:**
- `BE_GEO_ID` - Legacy partner identifier for API tracking (deprecated, use MERAKI_PYTHON_SDK_CALLER)
- `MERAKI_PYTHON_SDK_CALLER` - Application identifier for API usage tracking (format: "AppName/Version VendorName")

**Secrets location:**
- Secrets NOT stored in repository (`.env*` in `.gitignore`)
- Users manage API keys outside the codebase
- No embedded credentials or configuration defaults for real environments

## Webhooks & Callbacks

**Incoming:**
- None - SDK does not accept incoming webhooks
- Users can configure webhooks in Meraki Dashboard to receive events (external to SDK)

**Outgoing:**
- API supports callback configuration for device events
- Parameters: `callback` object with either `httpServerId` OR `url` and `sharedSecret`
- Used in endpoints like `updateDeviceLiveToolsPing`, `createDeviceLiveToolsArpTable`, etc.
- Location: Callback parameter support visible in `meraki/api/devices.py` and `meraki/aio/api/devices.py`
- SDK passes callback configuration as JSON to Dashboard API; does not handle callback execution

## Request/Response Patterns

**Rate Limiting:**
- Dashboard API rate limits via HTTP 429 responses
- SDK automatically retries 429 errors with exponential backoff
- Retry wait time: `nginx_429_retry_wait_time` (default 60s)
- Maximum retries: `maximum_retries` (default 2)
- Configurable via `wait_on_rate_limit=True/False`
- `Retry-After` header parsed from 429 responses

**Pagination:**
- Built-in support for paginated results
- Query parameters: `perPage`, `startingAfter`, `endingBefore`
- Methods can return iterators or complete lists via `use_iterator_for_get_pages`
- Link header parsing for next/prev pages

**Error Handling:**
- HTTP status codes >= 400 raise APIError with metadata
- 4XX retries optional via `retry_4xx_error` (default False)
- SSL/TLS certificate validation customizable via `certificate_path`
- Proxy support via `requests_proxy` parameter

**Simulation Mode:**
- `simulate=True` parameter prevents POST/PUT/DELETE from executing
- GET requests still execute normally
- Useful for testing workflows without making actual changes

---

*Integration audit: 2026-04-29*
