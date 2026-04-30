# Testing Patterns

**Analysis Date:** 2026-04-29

## Test Framework

**Runner:**
- pytest 8.3.5 through 9.x
- Config: `pyproject.toml` under `[tool.pytest.ini_options]`
- Test paths: `tests/unit` (unit tests only; excludes `tests/generator`)

**Assertion Library:**
- pytest's built-in assertions and `assert` statements
- No separate assertion library; standard pytest patterns

**Run Commands:**
```bash
pytest                           # Run all unit tests
pytest -v                        # Verbose output
pytest tests/unit/               # Run unit tests only
pytest -k "test_name"            # Run specific test
pytest --cov=meraki              # Run with coverage
pytest --cov=meraki --cov-report=html  # Generate HTML coverage report
pytest -m integration            # Run integration tests (if marked)
```

**Coverage:**
- Tool: pytest-cov
- Requirement: 90% minimum (configured in `pyproject.toml` as `fail_under = 90`)
- Excluded from coverage: `meraki/api/*` and `meraki/aio/api/*` (generated files) and `meraki/aio/__init__.py`
- Report shows missing lines: `show_missing = true`

## Test File Organization

**Location:**
- Co-located pattern: test files in `tests/` directory mirror source structure
- Unit tests: `tests/unit/`
- Integration tests: `tests/integration/`
- Generator tests: `tests/generator/` (not run with default pytest)

**Naming:**
- Files: `test_*.py` prefix pattern (pytest discovery)
- Example: `test_common.py`, `test_rest_session.py`, `test_exceptions.py`, `test_aio_rest_session.py`

**Structure:**
```
tests/
├── unit/
│   ├── test_common.py
│   ├── test_dashboard_api_init.py
│   ├── test_exceptions.py
│   ├── test_mock_integration.py
│   ├── test_response_handler.py
│   ├── test_rest_session.py
│   └── test_aio_rest_session.py
├── integration/
│   ├── conftest.py (pytest_addoption for --apikey and --o flags)
│   ├── test_async_dashboard_api.py
│   └── test_dashboard_api_python_library.py
└── generator/
    ├── conftest.py
    └── test_pure_functions.py
```

## Test Structure

**Suite Organization:**
- Test classes group related functionality: `class TestCheckPythonVersion:`, `class TestValidateUserAgent:`, `class TestAPIKeyError:` (file `tests/unit/test_common.py:16-30`)
- One test method per assertion focus: `def test_valid_version(self):`, `def test_too_old_raises(self):`, `def test_python2_raises(self):`
- Async tests use `async def test_*` pattern with pytest-asyncio
- Async session fixture patches dependencies and creates mock client: (file `tests/unit/test_aio_rest_session.py:57-84`)

**Patterns:**
- Setup: `@pytest.fixture` decorator for reusable test fixtures
- Example fixture for sync RestSession: (file `tests/unit/test_rest_session.py:10-32`)
  ```python
  @pytest.fixture
  def session():
      with patch("meraki.rest_session.check_python_version"):
          s = RestSession(
              logger=None,
              api_key="fake_api_key_1234567890123456789012345678901234567890",
              # ... all required parameters
          )
      return s
  ```
- Teardown: No explicit teardown; fixtures auto-clean when test ends
- Assertion pattern: `assert` statements with descriptive conditions: `assert "TestApp TestVendor" in result`

## Mocking

**Framework:** `unittest.mock` from Python standard library

**Patterns:**
```python
from unittest.mock import MagicMock, patch, AsyncMock

# Patch function/class
@patch("meraki.rest_session.check_python_version")
def test_something(self, mock_check):
    s = RestSession(...)

# Patch with context manager
with patch("meraki.rest_session.check_python_version"):
    from meraki.aio.rest_session import AsyncRestSession
    s = AsyncRestSession(...)

# Create mock response
resp = MagicMock(spec=requests.Response)
resp.status_code = 200
resp.reason = "OK"
resp.headers = {}
resp.content = b'{"ok":true}'
resp.links = {}
resp.json.return_value = {"ok": True}
resp.close = MagicMock()
```
(file `tests/unit/test_rest_session.py:39-55`)

**Async Mocking:**
- AsyncMock for async methods: `AsyncMock()` returns awaitable
- Wrapper class `_AwaitableValue` (file `tests/unit/test_aio_rest_session.py:10-50`) makes values both synchronously usable and awaitable for error handling compatibility
- Patch `aiohttp.ClientSession`: (file `tests/unit/test_aio_rest_session.py:59-63`)

**What to Mock:**
- External dependencies: `requests.Response`, `aiohttp.ClientSession`, platform functions
- Functions that check system state: `platform.python_version_tuple()`
- Network calls: HTTP session methods
- Do NOT mock the code being tested (the actual session class)

**What NOT to Mock:**
- The actual session classes being tested
- Utility functions like `encode_params()`, `validate_base_url()`
- Exception classes (let them construct naturally)
- Local utility functions used by the code under test

## Fixtures and Factories

**Test Data:**
- Helper method pattern: `def _metadata(operation="getOrganizations", tags=None):` (file `tests/unit/test_rest_session.py:35-36`)
- Mock response factory: `def _mock_response(status_code=200, ...)` with parameter defaults (file `tests/unit/test_rest_session.py:39-55`)
- pytest fixture for session: creates session with mocked dependencies (file `tests/unit/test_rest_session.py:10-32`)
- Fixture scope: default (function scope); creates fresh instance per test

**Location:**
- Fixtures defined at module level or in fixture file
- Helper methods defined as class methods with `_` prefix: `def _make_response(self, ...)`
- Shared fixtures can be moved to `conftest.py` (see `tests/integration/conftest.py`)

**Example fixture:**
```python
@pytest.fixture
def session():
    with patch("meraki.rest_session.check_python_version"):
        s = RestSession(
            logger=None,
            api_key="fake_api_key_1234567890123456789012345678901234567890",
            base_url="https://api.meraki.com/api/v1",
            single_request_timeout=60,
            # ... all parameters
        )
    return s
```

## Test Types

**Unit Tests:**
- Scope: Test individual functions and methods in isolation
- Location: `tests/unit/`
- Examples: `test_common.py` tests validation functions, `test_exceptions.py` tests exception classes
- Pattern: Mock external dependencies, test internal logic
- Coverage requirement: 90% minimum

**Integration Tests:**
- Scope: Test multiple components working together; typically requires real API key
- Location: `tests/integration/`
- Execution: Optional; requires `--apikey` parameter
- Example: `test_dashboard_api_python_library.py` makes real API calls
- CLI pattern: `pytest tests/integration/ --apikey=YOUR_KEY`

**E2E Tests:**
- Not used; integration tests serve as end-to-end validation

**Generator Tests:**
- Location: `tests/generator/`
- Purpose: Test code generation templates and functions
- Pattern: Pure function tests with fixtures
- Example: `test_pure_functions.py` tests documentation URL generation, pagination generation (file `tests/generator/test_pure_functions.py:1-42`)

## Async Testing

**Pattern:**
```python
@pytest.mark.asyncio
async def test_async_method(self):
    # test code
    await some_async_call()
```

**Async Session Creation:**
```python
@pytest.fixture
async def async_session():
    with (
        patch("meraki.aio.rest_session.check_python_version"),
        patch("aiohttp.ClientSession") as mock_client,
    ):
        mock_client.return_value = MagicMock()
        from meraki.aio.rest_session import AsyncRestSession
        s = AsyncRestSession(...)
    return s
```
(file `tests/unit/test_aio_rest_session.py:57-84`)

**pytest-asyncio Configuration:**
- `asyncio_mode = "auto"` in `pyproject.toml` (line 56)
- Automatically runs async tests without needing explicit markers in simple cases

## Error Testing

**Pattern:**
```python
def test_invalid_caller_raises(self):
    with pytest.raises(SessionInputError):
        validate_user_agent("", "invalid format!!!")

def test_too_old_raises(self, mock_ver):
    with pytest.raises(PythonVersionError):
        check_python_version()
```
(file `tests/unit/test_common.py:42-44`, `tests/unit/test_common.py:22-24`)

**Exception Assertion:**
- Use `pytest.raises(ExceptionType)` context manager
- Verify exception message/attributes: `err.message`, `err.status`, `err.reason`
- Test both exception raising and exception attribute values (file `tests/unit/test_exceptions.py:64-72`)

## Coverage Gaps and Strategy

**Excluded from Coverage:**
- Generated API endpoint files: `meraki/api/*` and `meraki/aio/api/*` (auto-generated; coverage would be fragile)
- Async init files: `meraki/aio/__init__.py`

**Testing Strategy:**
- Unit test the non-generated code: session management, error handling, utilities
- Integration tests for actual API calls to validate end-to-end flow
- Generator tests validate template functions work correctly

---

*Testing analysis: 2026-04-29*
