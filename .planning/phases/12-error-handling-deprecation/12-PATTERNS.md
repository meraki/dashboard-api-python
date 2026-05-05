# Phase 12: Error Handling Deprecation - Pattern Map

**Mapped:** 2026-05-05
**Files analyzed:** 3
**Analogs found:** 3 / 3

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `meraki/exceptions.py` (AsyncAPIError) | exception | n/a | `meraki/exceptions.py` (APIError) | exact |
| `tests/unit/test_exceptions.py` | test | n/a | `tests/unit/test_exceptions.py` (TestAPIError) | exact |
| `HTTPX-MIGRATION.md` | documentation | n/a | `HTTPX-MIGRATION.md` (Phase sections) | exact |

## Pattern Assignments

### `meraki/exceptions.py` (exception class, deprecation with inheritance)

**Analog:** `meraki/exceptions.py` (APIError lines 36-52, AsyncAPIError lines 56-72)

**Current inheritance pattern** (lines 36-52):
```python
class APIError(Exception):
    def __init__(self, metadata, response):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = self.response.status_code if self.response is not None and self.response.status_code else None
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

**Deprecation warning pattern (external analog)** `generator/generate_library_oasv2.py` (lines 14-19):
```python
if __name__ == "__main__" or "generate_library_oasv2" in sys.argv[0]:
    warnings.warn(
        "generate_library_oasv2.py is deprecated and will be removed in v1.2. Use generate_library.py instead.",
        DeprecationWarning,
        stacklevel=2,
    )
```

**Pattern to implement:**
- Change `class AsyncAPIError(Exception)` to `class AsyncAPIError(APIError)` (line 56)
- Add `import warnings` at top of `__init__`
- Change signature from `__init__(self, metadata, response, message)` to `__init__(self, metadata, response, message=None)` (make message optional)
- Add deprecation warning as first line in `__init__`: `warnings.warn('AsyncAPIError is deprecated. Catch APIError instead, which now handles both sync and async errors.', DeprecationWarning, stacklevel=2)`
- Implement dual-signature logic:
  - If `message is not None`: keep existing AsyncAPIError attribute setup (lines 58-68) but call `Exception.__init__()` directly
  - If `message is None`: delegate to `super().__init__(metadata, response)` to use APIError's response.json() extraction logic
- Keep existing `__repr__` (line 71-72)

---

### `tests/unit/test_exceptions.py` (unit test, deprecation warning validation)

**Analog:** `tests/unit/test_exceptions.py` (TestAsyncAPIError lines 125-173)

**Existing test pattern** (lines 125-173):
```python
class TestAsyncAPIError:
    def _make_response(self, status_code=400, reason_phrase="Bad Request"):
        resp = MagicMock()
        resp.status_code = status_code
        resp.reason_phrase = reason_phrase
        return resp

    def test_basic_init(self):
        metadata = {"tags": ["devices"], "operation": "getDevices"}
        resp = self._make_response()
        err = AsyncAPIError(metadata, resp, {"errors": ["fail"]})
        assert err.tag == "devices"
        assert err.operation == "getDevices"
        assert err.status == 400
        assert err.reason == "Bad Request"
        assert err.message == {"errors": ["fail"]}

    def test_repr(self):
        metadata = {"tags": ["devices"], "operation": "getDevices"}
        resp = self._make_response()
        err = AsyncAPIError(metadata, resp, "some error")
        r = repr(err)
        assert "devices" in r
        assert "400" in r

    def test_string_message_stripped(self):
        metadata = {"tags": ["orgs"], "operation": "getOrgs"}
        resp = self._make_response()
        err = AsyncAPIError(metadata, resp, "  spaces around  ")
        assert err.message == "spaces around"

    def test_404_appends_wait_message(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        resp = self._make_response(status_code=404, reason_phrase="Not Found")
        err = AsyncAPIError(metadata, resp, "resource missing")
        assert "please wait" in err.message

    def test_non_404_does_not_append_wait_message(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        resp = self._make_response(status_code=500, reason_phrase="Server Error")
        err = AsyncAPIError(metadata, resp, "server broke")
        assert "please wait" not in err.message

    def test_none_response(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        err = AsyncAPIError(metadata, None, "no response")
        assert err.status is None
        assert err.reason is None
```

**Pattern to add:**
- Add new tests wrapped with `pytest.warns(DeprecationWarning)` context manager
- Test 1: Verify deprecation warning fires on instantiation with 3-arg signature
- Test 2: Verify deprecation warning fires on instantiation with 2-arg signature
- Test 3: Verify AsyncAPIError is instance of APIError (inheritance check)
- Test 4: Verify 2-arg form delegates to APIError (extracts message from response.json())
- Wrap ALL existing instantiation calls in TestAsyncAPIError with `pytest.warns(DeprecationWarning)` (6 tests total)

**Concrete test pattern from RESEARCH.md** (lines 369-406):
```python
import pytest
from unittest.mock import MagicMock
from meraki.exceptions import AsyncAPIError

def test_async_api_error_emits_deprecation_warning():
    """Verify AsyncAPIError emits DeprecationWarning on instantiation."""
    metadata = {"tags": ["devices"], "operation": "getDevices"}
    response = MagicMock()
    response.status_code = 400
    response.reason_phrase = "Bad Request"
    
    with pytest.warns(DeprecationWarning, match="AsyncAPIError is deprecated"):
        err = AsyncAPIError(metadata, response, {"errors": ["fail"]})
    
    assert err.tag == "devices"
    assert err.status == 400

def test_async_api_error_3arg_signature_backwards_compatible():
    """Old 3-arg signature still works."""
    metadata = {"tags": ["orgs"], "operation": "getOrgs"}
    response = MagicMock()
    response.status_code = 404
    response.reason_phrase = "Not Found"
    
    with pytest.warns(DeprecationWarning):
        err = AsyncAPIError(metadata, response, "resource missing")
    
    assert err.message == "resource missingplease wait a minute if the key or org was just newly created."

def test_async_api_error_2arg_signature_new_style():
    """New 2-arg signature delegates to APIError."""
    metadata = {"tags": ["networks"], "operation": "getNetworks"}
    response = MagicMock()
    response.status_code = 500
    response.reason_phrase = "Server Error"
    response.json.return_value = {"errors": ["server failed"]}
    
    with pytest.warns(DeprecationWarning):
        err = AsyncAPIError(metadata, response)
    
    assert err.message == {"errors": ["server failed"]}
```

---

### `HTTPX-MIGRATION.md` (documentation, migration guide)

**Analog:** `HTTPX-MIGRATION.md` (Phase structure lines 49-296)

**Existing phase structure pattern** (lines 49-58):
```markdown
## Phase 0: Integration Test Baseline

Before touching HTTP code, capture a passing integration test run against the Meraki sandbox. This becomes the regression gate for all subsequent phases.

- Run existing integration tests, record pass/fail state
- Document which endpoints are exercised
- This baseline validates that Phases 2-3 produce identical external behavior
```

**Existing code example pattern** (lines 99-108):
```markdown
| requests | httpx |
|----------|-------|
| `requests.session()` | `httpx.Client(headers=..., verify=..., proxy=..., timeout=..., follow_redirects=False)` |
| `session.request(method, url, allow_redirects=False, **kwargs)` | `self._client.request(method, url, **kwargs)` |
| `requests.exceptions.RequestException` | `httpx.HTTPError` |
| `response.reason` | `response.reason_phrase` |
| `response.links` | `response.links` (same API) |
| `verify=path` | `verify=path` (same) |
| `proxies={"https": url}` | `proxy=url` |
| `timeout=60` | `timeout=60` (same) |
```

**Pattern to add:**
- Add new section after Phase 5 (lines 141-163) titled "## Deprecated: AsyncAPIError"
- Structure: Status line, "What Changed" subsection, "Migration" subsection with before/after code blocks, "Backwards Compatibility" subsection, "Recommended Action" subsection
- Use existing markdown code fence style with language tags (`python`)
- Include deprecation warning suppression pattern for users during migration
- Reference from RESEARCH.md lines 410-462 for content structure

**Concrete pattern from RESEARCH.md** (lines 410-462):
```markdown
## Deprecated: AsyncAPIError

**Status:** Deprecated as of v4.0. Use `APIError` for both sync and async exceptions.

### What Changed

In previous versions, the SDK used two separate exception classes:
- `APIError` for synchronous errors
- `AsyncAPIError` for asynchronous errors

Starting in v4.0, both sync and async sessions raise exceptions that inherit from `APIError`. The `AsyncAPIError` class remains available for backwards compatibility but is deprecated.

### Migration

**Before (v3.x):**
```python
from meraki.aio import AsyncDashboardAPI
from meraki.exceptions import AsyncAPIError

async with AsyncDashboardAPI(api_key=API_KEY) as aiomeraki:
    try:
        response = await aiomeraki.organizations.getOrganizations()
    except AsyncAPIError as e:
        print(f"Error: {e.status} {e.reason}")
```

**After (v4.0+):**
```python
from meraki.aio import AsyncDashboardAPI
from meraki.exceptions import APIError  # Changed

async with AsyncDashboardAPI(api_key=API_KEY) as aiomeraki:
    try:
        response = await aiomeraki.organizations.getOrganizations()
    except APIError as e:  # Changed
        print(f"Error: {e.status} {e.reason}")
```

### Backwards Compatibility

Existing code using `except AsyncAPIError:` will continue to work because `AsyncAPIError` is now a subclass of `APIError`. However, you will see a `DeprecationWarning` when the exception is raised.

To suppress the warning during migration:
```python
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning, module='meraki')
```

### Recommended Action

Update exception handlers to catch `APIError` instead of `AsyncAPIError`. This future-proofs your code and eliminates deprecation warnings.
```

---

## Shared Patterns

### Exception Inheritance with Dual-Signature Init

**Source:** `meraki/exceptions.py` (APIError lines 36-52, AsyncAPIError lines 56-72)
**Apply to:** AsyncAPIError subclass implementation

**Pattern:**
1. Parent class (APIError) has 2-arg signature `(metadata, response)` with JSON extraction logic
2. Child class (AsyncAPIError) has 3-arg signature `(metadata, response, message)` with explicit message
3. Make message optional: `message=None` in child signature
4. Branch in child `__init__`:
   - If `message is not None`: replicate old 3-arg logic, call `Exception.__init__()` directly
   - If `message is None`: delegate to `super().__init__(metadata, response)` for parent's JSON extraction
5. Keep child's `__repr__` override (both have identical implementations)

### Deprecation Warning with Stacklevel

**Source:** `generator/generate_library_oasv2.py` (lines 14-19)
**Apply to:** AsyncAPIError `__init__`

```python
import warnings
warnings.warn(
    "AsyncAPIError is deprecated. Catch APIError instead, which now handles both sync and async errors.",
    DeprecationWarning,
    stacklevel=2
)
```

**Key points:**
- `stacklevel=2` attributes warning to caller (raise site in async_.py), not the exception class itself
- Fire on every instantiation (in `__init__`), not import time or catch time
- Use DeprecationWarning category (Python tooling filters by default, pytest.warns can capture)

### Pytest Warning Assertion

**Source:** pytest documentation (referenced in RESEARCH.md lines 216-228)
**Apply to:** All new AsyncAPIError tests

```python
import pytest

with pytest.warns(DeprecationWarning, match="AsyncAPIError is deprecated"):
    err = AsyncAPIError(metadata, response, message)
```

**Key points:**
- Wrap instantiation in `pytest.warns()` context manager
- Use `match=` parameter for regex matching on warning message
- All existing test instantiations must be wrapped (backwards compat validation)
- Add new tests for 2-arg form (new behavior)

### MagicMock Response Pattern

**Source:** `tests/unit/test_exceptions.py` (lines 54-62, 126-130)
**Apply to:** All exception tests

```python
from unittest.mock import MagicMock

def _make_response(status_code=400, reason_phrase="Bad Request", json_data=None, content=b""):
    resp = MagicMock()
    resp.status_code = status_code
    resp.reason_phrase = reason_phrase
    resp.json.return_value = json_data or {"errors": ["something"]}
    resp.content = content
    return resp
```

**Key points:**
- Mock response objects with httpx attributes (status_code, reason_phrase, json method)
- TestAPIError uses json_data parameter, TestAsyncAPIError does not (old 3-arg form didn't call json())
- New 2-arg AsyncAPIError tests must include json.return_value to test delegation

---

## No Analog Found

All files have close matches in the codebase. No external patterns required.

---

## Metadata

**Analog search scope:** `meraki/`, `tests/unit/`, `generator/`, root documentation files
**Files scanned:** 47 (exceptions.py + test files + generator scripts + migration doc)
**Pattern extraction date:** 2026-05-05
**Key insight:** Project already has deprecation warning pattern in generator scripts. Exception inheritance exists but no prior deprecated-subclass pattern. Dual-signature compatibility requires branching logic since parent extracts message from response, child accepts it explicitly.
