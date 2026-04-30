# Coding Conventions

**Analysis Date:** 2026-04-29

## Naming Patterns

**Files:**
- Snake_case for module files: `rest_session.py`, `response_handler.py`
- Exception classes in `exceptions.py`
- Generated API endpoint files use CamelCase where tied to service names: `devices.py`, `networks.py`, `cellularGateway.py`, `wirelessController.py`
- Batch operation files: `meraki/api/batch/` directory with matching service names

**Functions:**
- camelCase for all function names: `check_python_version()`, `validate_user_agent()`, `getDevice()`, `updateDevice()`
- Special methods use Python conventions: `__init__()`, `__repr__()`, `__str__()`
- Private functions: no underscore prefix in generated code; prefix with `_` for internal helpers

**Variables:**
- camelCase for parameters: `be_geo_id`, `single_request_timeout`, `certificate_path`
- snake_case for local variables: `user_agent`, `allowed_format_in_regex`
- Dicts and collections use descriptive names: `metadata`, `payload`, `body_params`, `kwargs`
- Metadata dicts follow pattern: `metadata = {"tags": [...], "operation": "..."}`

**Types:**
- Type hints used in function signatures: `def getDevice(self, serial: str):` (file `meraki/api/devices.py:9`)
- Type hints for parameters but not always return types
- Exception classes are all UPPERCASE suffixed with `Error`: `APIKeyError`, `APIResponseError`, `APIError`, `AsyncAPIError`, `PythonVersionError`, `SessionInputError` (file `meraki/exceptions.py`)

**Classes:**
- CamelCase: `DashboardAPI`, `RestSession`, `AsyncRestSession`, `Devices`, `Organizations` (file `meraki/__init__.py:58`)
- Class names match API endpoint groups or functionality areas
- Parent class inherits from `object`: `class DashboardAPI(object):` (file `meraki/__init__.py:58`)

## Code Style

**Formatting:**
- Line length: 127 characters (configured in `pyproject.toml`)
- Tool: ruff (formatter and linter)
- Configuration: `tool.ruff` section in `pyproject.toml`

**Linting:**
- Tool: ruff with flake8 compatibility
- Config file: `pyproject.toml` under `[tool.ruff]`
- Pre-commit hooks run: `ruff-format` and `ruff --fix` (file `.pre-commit-config.yaml`)
- Exclusions from formatting: generated API code in `meraki/(aio/api|api/batch|api)/`, notebooks, code generation snippets

**Formatting examples from codebase:**
```python
# Long parameter lists continue on new lines
def __init__(
    self,
    api_key=None,
    base_url=DEFAULT_BASE_URL,
    single_request_timeout=SINGLE_REQUEST_TIMEOUT,
    certificate_path=CERTIFICATE_PATH,
    # ... continues
):
```
(file `meraki/__init__.py:87-112`)

## Import Organization

**Order:**
1. Standard library imports: `import logging`, `import os`, `import platform`, `import re`, `import sys`, `import urllib.parse`
2. Third-party imports: `import requests`, `import aiohttp`
3. Local application imports: `from meraki.api.administered import Administered`

**Path Aliases:**
- No aliases used; direct relative imports within the package
- Imports from `meraki.config` for constants (file `meraki/__init__.py:25-49`)

**Import patterns:**
```python
import logging
import os

from meraki.api.administered import Administered
from meraki.config import (
    API_KEY_ENVIRONMENT_VARIABLE,
    DEFAULT_BASE_URL,
    # ... multiline from imports
)
```
(file `meraki/__init__.py:1-49`)

## Error Handling

**Patterns:**
- Raise custom exceptions defined in `meraki/exceptions.py`: `APIError`, `AsyncAPIError`, `APIKeyError`, `APIResponseError`, `PythonVersionError`, `SessionInputError`
- Check conditions and raise before proceeding: `if not api_key: raise APIKeyError()` (file `meraki/__init__.py:115-116`)
- Exception __init__ stores attributes for later access: `self.status`, `self.reason`, `self.message` (file `meraki/exceptions.py:37-48`)
- Exception __str__ and __repr__ methods format error output: `def exc_message(self):` returns formatted string (file `meraki/exceptions.py:22-26`)
- Try/except for JSON decode failures: wrap `response.json()` and fallback to `response.content` (file `meraki/exceptions.py:43-46`)
- 404 status codes append contextual help: "please wait a minute if the key or org was just newly created." (file `meraki/exceptions.py:47-48`)

## Logging

**Framework:** Python's built-in `logging` module

**Patterns:**
- Logger instance created in `__init__`: `self._logger = logging.getLogger(__name__)` (file `meraki/__init__.py:129`)
- Logger can be inherited or created fresh based on `inherit_logging_config` flag
- Suppress logging entirely with `suppress_logging=True` (file `meraki/__init__.py:128`)
- Standard formatter: `"%(asctime)s %(name)12s: %(levelname)8s > %(message)s"` (file `meraki/__init__.py:135`)
- Handlers: console handler (StreamHandler) and optional file handler (FileHandler)
- Log level: DEBUG
- Conditional logging based on `print_console` and `output_log` parameters (file `meraki/__init__.py:150-154`)

## Comments

**When to Comment:**
- Docstrings for API methods show endpoint URL and parameters: `"""**Update the attributes of a device** https://developer.cisco.com/meraki/api-v1/..."""` (file `meraki/api/devices.py:28-41`)
- TODO/FIXME comments exist in codebase (check `TODO.md` for list)
- Inline comments explain algorithm details, especially in parameter encoding: `"""Encode parameters in a piece of data..."""` (file `meraki/rest_session.py:41-57`)

**Docstring Format:**
- Triple-quoted strings for docstrings
- API endpoint methods include: operation description, link to documentation, parameter list with types
- Example: `"""**Return a single device** https://developer.cisco.com/meraki/api-v1/#!get-device\n\n- serial (string): Serial"""` (file `meraki/api/devices.py:10-14`)

## Function Design

**Size:** Functions generally stay under 50 lines; generated API methods average 10-30 lines

**Parameters:**
- Use `**kwargs` to capture optional parameters: `def updateDevice(self, serial: str, **kwargs):` (file `meraki/api/devices.py:26`)
- Extract known parameters from kwargs: `payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}` (file `meraki/api/devices.py:63`)
- Validate user input early: check Python version at session init, validate API key before creating session

**Return Values:**
- API methods return result of session call: `return self._session.get(metadata, resource)` (file `meraki/api/devices.py:24`)
- Exceptions raised on errors, no error codes or None returns for failure
- Session methods handle retries, redirects, and error conversion internally

## Module Design

**Exports:**
- Main public interface in `meraki/__init__.py`: imports all top-level API classes and `DashboardAPI`
- Specific imports exposed: `from meraki.exceptions import APIKeyError` (file `meraki/__init__.py:51`)
- Version exposed: `from meraki._version import __version__` (file `meraki/__init__.py:52`)

**Barrel Files:**
- `meraki/__init__.py` re-exports: all API endpoint classes (`Administered`, `Appliance`, `Camera`, etc.)
- API batch operations under `meraki/api/batch/__init__.py` exports `Batch` class
- Async variants under `meraki/aio/__init__.py` and `meraki/aio/api/`

**Session Dependency Injection:**
- All API classes receive session in __init__: `def __init__(self, session): self._session = session` (file `meraki/api/devices.py:5-6`)
- Session methods (`get`, `post`, `put`, `delete`) handle all HTTP communication
- Metadata dict passed with operation name and tags to session for logging and error handling

## Configuration

**Environment Variables:**
- `MERAKI_DASHBOARD_API_KEY`: API key (defined as `API_KEY_ENVIRONMENT_VARIABLE`)
- `BE_GEO_ID`: Partner identifier (deprecated)
- `MERAKI_PYTHON_SDK_CALLER`: API caller tracking identifier
- Default configuration constants in `meraki/config.py`

**Constants Pattern:**
- All config constants defined in `meraki/config.py` with uppercase names: `SINGLE_REQUEST_TIMEOUT`, `MAXIMUM_RETRIES`, `WAIT_ON_RATE_LIMIT`
- Imported into `__init__.py` and passed to RestSession
- Can be overridden at DashboardAPI instantiation time

---

*Convention analysis: 2026-04-29*
