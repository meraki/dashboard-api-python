# Phase 12: Error Handling Deprecation - Research

**Researched:** 2026-05-05
**Domain:** Python exception class inheritance and deprecation warnings
**Confidence:** HIGH

## Summary

Phase 12 unifies exception handling by making AsyncAPIError a deprecated subclass of APIError with backwards-compatible `__init__`. The critical technical challenge is signature compatibility: APIError takes 2 args `(metadata, response)`, AsyncAPIError takes 3 args `(metadata, response, message)`. The subclass must accept both signatures to maintain backwards compatibility.

Python's warnings module (stdlib since 2.6) provides DeprecationWarning with stacklevel control. Pytest 9.0 has native `pytest.warns()` support for testing deprecation warnings. The phase is code-only (no external dependencies, no data migration, no runtime state changes).

**Primary recommendation:** Make AsyncAPIError inherit from APIError with dual-signature `__init__` that detects 3-arg vs 2-arg calls. Emit warning on every instantiation. Update HTTPX-MIGRATION.md. Add pytest.warns test.

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Exception class hierarchy | API / Backend | — | Exception classes defined in meraki/exceptions.py, raised by session layer |
| Deprecation warning emission | API / Backend | — | warnings.warn fires at instantiation time in exception __init__ |
| Migration documentation | Static docs | — | HTTPX-MIGRATION.md consumed by library users during upgrade |
| Deprecation testing | Test framework | — | pytest.warns validates warning emission |

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions

**D-01: Signature Compatibility**
AsyncAPIError.__init__ accepts both signatures: `(metadata, response, message=None)`. If `message` is passed, use it directly; if not, fall through to APIError's `response.json()` extraction logic. Old 3-arg callers continue working without changes.

**D-02: Deprecation Mechanism**
`warnings.warn('AsyncAPIError is deprecated, catch APIError instead', DeprecationWarning, stacklevel=2)` fires on every instantiation of AsyncAPIError. No import-time or catch-time warnings.

**D-03: Async Session Raise Sites**
async_.py continues raising AsyncAPIError (now a subclass of APIError). Existing user catch blocks (`except AsyncAPIError`) keep working. Since it's a subclass, `except APIError` also catches it. Migration is optional, not forced.

**D-04: Migration Documentation**
HTTPX-MIGRATION.md gets a "Deprecated: AsyncAPIError" section with before/after code examples. AsyncAPIError class docstring points users to catch APIError instead.

### Claude's Discretion

- Whether to use `__init_subclass__` or simple inheritance
- Exact wording of deprecation warning message
- Whether to suppress repeated warnings via `warnings.simplefilter`

### Deferred Ideas (OUT OF SCOPE)

None. Discussion stayed within phase scope.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| ERR-02 | AsyncAPIError deprecated as subclass of APIError with compat __init__ | Signature compatibility via optional 3rd param + isinstance check; Python warnings module for deprecation; pytest.warns for validation |
</phase_requirements>

## Standard Stack

### Core

| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| warnings | stdlib (3.11+) | Emit DeprecationWarning | Built-in since Python 2.6, no install needed, stacklevel controls caller attribution |
| pytest.warns | 9.0.3 (in dev deps) | Test warning emission | Native pytest feature for asserting warnings, already in project deps |

No external dependencies required. `warnings` is stdlib and always available in Python >=3.11 (project minimum per pyproject.toml).

**Installation:** None required (stdlib only).

**Version verification:**
```bash
# warnings module is stdlib - always available
python -c "import warnings; print('available')"
# available

# pytest already in project
pytest --version
# pytest 9.0.3
```

### Supporting

None. This is a pure Python stdlib task.

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| DeprecationWarning | UserWarning | DeprecationWarning is semantically correct for API deprecations; Python tooling filters it by default (must run with -W to see), which is desired behavior |
| warnings.warn | logging.warning | warnings integrates with pytest.warns and user filter control; logging would require users to configure loggers |
| Simple inheritance | __init_subclass__ hook | __init_subclass__ is for customizing subclass creation, not instance creation; simple inheritance with custom __init__ is correct pattern |

## Architecture Patterns

### System Architecture Diagram

```
User code
    |
    | raises/catches exceptions
    v
meraki/exceptions.py
    |
    +-- APIError(Exception)              [2-arg: metadata, response]
    |       |
    |       +-- AsyncAPIError(APIError)   [3-arg compat: metadata, response, message=None]
    |              |
    |              +-- __init__ detects 2-arg vs 3-arg
    |              +-- warnings.warn() fires on instantiation
    |              +-- calls super().__init__() or sets attributes directly
    |
    v
meraki/session/async_.py (8 raise sites)
    |
    | raise AsyncAPIError(metadata, response, message)
    v
User catch blocks
    |
    +-- except AsyncAPIError:  (still works - exact match)
    +-- except APIError:       (now also works - inheritance)
```

### Component Responsibilities

| File | Responsibility | Lines Affected |
|------|----------------|----------------|
| meraki/exceptions.py | AsyncAPIError class definition | ~20 lines (lines 56-73 + new logic) |
| meraki/session/async_.py | Raise sites (no changes needed) | 0 (raises AsyncAPIError unchanged) |
| tests/unit/test_exceptions.py | Add deprecation warning test | +10 lines |
| HTTPX-MIGRATION.md | Deprecation section | +30 lines |

### Recommended Project Structure

No new files. Modifications to existing:

```
meraki/
├── exceptions.py           # AsyncAPIError becomes subclass
└── session/
    └── async_.py           # No changes (still raises AsyncAPIError)
tests/
└── unit/
    └── test_exceptions.py  # Add pytest.warns test
HTTPX-MIGRATION.md          # Add deprecation section
```

### Pattern 1: Dual-Signature Init

**What:** Accept both 2-arg `(metadata, response)` and 3-arg `(metadata, response, message)` signatures in AsyncAPIError.__init__.

**When to use:** When deprecating an exception class that has a different signature from its replacement parent class.

**Example:**
```python
class AsyncAPIError(APIError):
    """Deprecated: Use APIError for both sync and async exceptions."""
    
    def __init__(self, metadata, response, message=None):
        import warnings
        warnings.warn(
            'AsyncAPIError is deprecated. Catch APIError instead, which now handles both sync and async errors.',
            DeprecationWarning,
            stacklevel=2
        )
        
        # If 3-arg form (old callers): use message directly
        if message is not None:
            self.response = response
            self.tag = metadata["tags"][0]
            self.operation = metadata["operation"]
            self.status = response.status_code if response else None
            self.reason = response.reason_phrase if response and hasattr(response, "reason_phrase") else None
            self.message = message.strip() if isinstance(message, str) else message
            if isinstance(self.message, str) and self.status == 404 and self.reason == "Not Found":
                self.message += "please wait a minute if the key or org was just newly created."
            Exception.__init__(self, f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}")
        # If 2-arg form (new callers): fall through to parent
        else:
            super().__init__(metadata, response)
```

**Rationale:** `message=None` default param makes 3rd arg optional. If `message` is passed, replicate old AsyncAPIError logic. If not passed, delegate to APIError.__init__ which extracts message from response.json().

### Pattern 2: Deprecation Warning with Stacklevel

**What:** Use `stacklevel=2` to attribute warning to the caller of AsyncAPIError(), not the __init__ itself.

**When to use:** Any deprecation warning in library code where you want the warning to point to user code, not library internals.

**Example:**
```python
import warnings
warnings.warn(
    'AsyncAPIError is deprecated. Catch APIError instead.',
    DeprecationWarning,
    stacklevel=2  # Points to the line that called AsyncAPIError()
)
```

**Rationale:** `stacklevel=1` (default) would show warning at the warnings.warn() line. `stacklevel=2` shows warning at the `raise AsyncAPIError(...)` line, which is more useful for users.

### Pattern 3: Testing Deprecation Warnings

**What:** Use pytest.warns() context manager to assert that code emits expected warning.

**When to use:** Testing any code that uses warnings.warn().

**Example:**
```python
import pytest
from meraki.exceptions import AsyncAPIError

def test_async_api_error_emits_deprecation_warning():
    metadata = {"tags": ["devices"], "operation": "getDevices"}
    response = MagicMock()
    response.status_code = 400
    response.reason_phrase = "Bad Request"
    
    with pytest.warns(DeprecationWarning, match="AsyncAPIError is deprecated"):
        err = AsyncAPIError(metadata, response, "error message")
    
    assert err.tag == "devices"
    assert err.status == 400
```

**Rationale:** pytest.warns validates both that warning fires AND captures it (prevents test output pollution). `match=` regex validates warning message content.

### Anti-Patterns to Avoid

- **Emitting warning at import time:** Wrong scope. Users importing exceptions.py for type hints would trigger warnings. Emit at instantiation (__init__) only.
- **Emitting warning in try/except block:** Catch blocks don't instantiate exceptions, they reference already-instantiated objects. Warning fires at raise site, not catch site.
- **Using logging.warning instead of warnings.warn:** Logging doesn't integrate with Python's warning filters or pytest.warns(). Use warnings module for API deprecations.
- **Calling super().__init__ when message provided:** APIError.__init__ expects 2 args and extracts message from response. If old 3-arg form used, must bypass parent __init__ and call Exception.__init__ directly.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Deprecation warnings | Custom "please migrate" messages in exceptions | warnings.warn() with DeprecationWarning | Python tooling (pytest, -W flag, PYTHONWARNINGS env) filters DeprecationWarning by category; custom messages bypass this ecosystem |
| Warning suppression | Try/except to silence warnings | warnings.filterwarnings() or -W flag | Warnings have stdlib control mechanisms; catching warnings as exceptions breaks compatibility |
| Stacklevel calculation | Hardcoded line numbers in warning messages | stacklevel parameter | warnings module uses stack introspection to attribute warnings to correct caller; manual line numbers break on refactor |

**Key insight:** Python's warnings system is designed for library deprecations. It has user-controllable filters, IDE integration, and pytest support. Custom deprecation messages (e.g., "This class is deprecated, see docs") lose all these benefits and make warnings harder to suppress or test.

## Common Pitfalls

### Pitfall 1: Wrong Stacklevel Attribution

**What goes wrong:** Warning shows file/line of warnings.warn() call instead of user's raise site.

**Why it happens:** Default stacklevel=1 attributes to immediate caller. Library code needs stacklevel=2+ to reach user code.

**How to avoid:** Always use `stacklevel=2` for warnings in library __init__ methods. Test with pytest.warns to verify warning message shows expected caller location.

**Warning signs:**
```python
# BAD - warning attributes to exceptions.py
warnings.warn("deprecated", DeprecationWarning)

# GOOD - warning attributes to async_.py raise line
warnings.warn("deprecated", DeprecationWarning, stacklevel=2)
```

### Pitfall 2: Super Init Signature Mismatch

**What goes wrong:** `TypeError: APIError.__init__() takes 3 positional arguments but 4 were given` when calling `super().__init__(metadata, response, message)`.

**Why it happens:** APIError.__init__ signature is `(self, metadata, response)` (2 params after self). Passing 3 params fails.

**How to avoid:** Only call `super().__init__(metadata, response)` when message is NOT provided (2-arg form). For 3-arg form, bypass parent init and call `Exception.__init__()` directly with formatted string.

**Warning signs:** Test failures with "takes X arguments but Y were given" when instantiating AsyncAPIError with 3 args.

### Pitfall 3: Missing __repr__ Override

**What goes wrong:** repr() output changes between parent and child class, breaking user code that relies on exception string format.

**Why it happens:** Parent class may have custom __repr__. If child bypasses parent __init__, parent's attribute setup doesn't run, and parent's __repr__ may fail.

**How to avoid:** AsyncAPIError already has identical __repr__ to APIError (both return `f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"`). Keep this override even as subclass.

**Warning signs:** repr(exception) shows `<AsyncAPIError object at 0x...>` instead of formatted string with tag/operation/status.

### Pitfall 4: DeprecationWarning Invisible in Tests

**What goes wrong:** Warning fires but doesn't appear in test output or pytest.warns() doesn't catch it.

**Why it happens:** Python filters DeprecationWarning by default. Must run pytest with `-W default::DeprecationWarning` or use pytest.warns() context manager.

**How to avoid:** Use pytest.warns() in test code. For manual testing, run `python -W default::DeprecationWarning script.py`.

**Warning signs:**
```bash
# This WON'T show deprecation warnings
python -c "from meraki.exceptions import AsyncAPIError; ..."

# This WILL show deprecation warnings
python -W default::DeprecationWarning -c "from meraki.exceptions import AsyncAPIError; ..."
```

### Pitfall 5: Deprecation Warning Spam in Retry Loops

**What goes wrong:** Single API call with 3 retries emits 3 identical warnings, cluttering logs.

**Why it happens:** Each `raise AsyncAPIError(...)` triggers __init__, which calls warnings.warn(). Retry loop raises multiple times.

**How to avoid:** Per D-02 decision, warning fires on every instantiation (this is intentional - user needs to fix all raise sites). If spam becomes issue, add `warnings.filterwarnings('once', category=DeprecationWarning)` to session base, but this is discretionary.

**Warning signs:** Test output shows 3+ identical "AsyncAPIError is deprecated" warnings for single test case.

## Code Examples

Verified patterns from stdlib and project conventions:

### Dual-Signature Init Implementation

```python
# Source: D-01 decision from 12-CONTEXT.md + Python stdlib pattern
class AsyncAPIError(APIError):
    """Deprecated: Use APIError for both sync and async exceptions.
    
    This exception is deprecated as of version 4.0. Catch APIError instead,
    which now handles both synchronous and asynchronous errors.
    
    Existing code using `except AsyncAPIError:` will continue to work
    because AsyncAPIError is now a subclass of APIError.
    """
    
    def __init__(self, metadata, response, message=None):
        import warnings
        warnings.warn(
            'AsyncAPIError is deprecated. Catch APIError instead, which now handles both sync and async errors.',
            DeprecationWarning,
            stacklevel=2
        )
        
        if message is not None:
            # Old 3-arg form: replicate original AsyncAPIError logic
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
            Exception.__init__(self, f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}")
        else:
            # New 2-arg form: delegate to APIError
            super().__init__(metadata, response)
    
    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
```

### Testing Deprecation Warning

```python
# Source: pytest documentation + pyproject.toml (pytest>=9.0)
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

### User Migration Path (HTTPX-MIGRATION.md section)

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

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Separate sync/async exceptions (APIError vs AsyncAPIError) | Unified exception hierarchy (AsyncAPIError subclass of APIError) | v4.0 (httpx migration) | Users can catch APIError for both sync and async, simplifying exception handling |
| 3-arg AsyncAPIError signature with explicit message | 2-arg APIError signature extracts message from response | v4.0 | AsyncAPIError maintains backwards compat with optional 3rd param, but new code should use 2-arg form |

**Deprecated/outdated:**
- Catching AsyncAPIError specifically: Still works (subclass relationship) but deprecated. Catch APIError instead.
- 3-arg AsyncAPIError signature: Still works (optional param) but discouraged. 2-arg form delegates to APIError logic.

## Assumptions Log

This section lists all claims tagged `[ASSUMED]` in this research.

**Table is empty:** All claims were verified via codebase reading (meraki/exceptions.py, tests/unit/test_exceptions.py, pyproject.toml) or stdlib documentation (warnings module). No unverified assumptions.

## Open Questions

None. All technical details verified against codebase and stdlib documentation.

## Environment Availability

Phase 12 has no external dependencies (stdlib warnings module only). Environment check not needed.

## Validation Architecture

### Test Framework

| Property | Value |
|----------|-------|
| Framework | pytest 9.0.3 |
| Config file | pyproject.toml (tool.pytest.ini_options) |
| Quick run command | `pytest tests/unit/test_exceptions.py::TestAsyncAPIError -x` |
| Full suite command | `pytest tests/unit/test_exceptions.py` |

### Phase Requirements → Test Map

| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| ERR-02 | AsyncAPIError is subclass of APIError | unit | `pytest tests/unit/test_exceptions.py::test_async_api_error_subclass -x` | ❌ Wave 0 |
| ERR-02 | AsyncAPIError emits DeprecationWarning | unit | `pytest tests/unit/test_exceptions.py::test_async_api_error_emits_deprecation_warning -x` | ❌ Wave 0 |
| ERR-02 | 3-arg signature backwards compatible | unit | `pytest tests/unit/test_exceptions.py::test_async_api_error_3arg_signature -x` | ❌ Wave 0 |
| ERR-02 | 2-arg signature delegates to parent | unit | `pytest tests/unit/test_exceptions.py::test_async_api_error_2arg_signature -x` | ❌ Wave 0 |
| ERR-02 | Existing async_.py raise sites still work | unit | `pytest tests/unit/ -k "async" -x` | ✅ (existing tests) |

### Sampling Rate

- **Per task commit:** `pytest tests/unit/test_exceptions.py::TestAsyncAPIError -x` (~1 second)
- **Per wave merge:** `pytest tests/unit/test_exceptions.py` (~3 seconds)
- **Phase gate:** Full unit suite + verify no DeprecationWarning in other tests: `pytest tests/unit/ --tb=short`

### Wave 0 Gaps

- [ ] `tests/unit/test_exceptions.py::test_async_api_error_subclass` — verify isinstance(AsyncAPIError(...), APIError) == True
- [ ] `tests/unit/test_exceptions.py::test_async_api_error_emits_deprecation_warning` — pytest.warns(DeprecationWarning) on instantiation
- [ ] `tests/unit/test_exceptions.py::test_async_api_error_3arg_signature` — old (metadata, response, message) form still works
- [ ] `tests/unit/test_exceptions.py::test_async_api_error_2arg_signature` — new (metadata, response) form delegates to APIError logic

## Security Domain

**security_enforcement:** Not applicable. Phase 12 is internal API refactoring (exception class hierarchy) with no external inputs, cryptography, authentication, or data handling changes. No ASVS categories apply.

## Sources

### Primary (HIGH confidence)

- `meraki/exceptions.py` (lines 36-73) — Existing APIError and AsyncAPIError implementations verified via codebase read
- `meraki/session/async_.py` (lines 157, 166, 173, 236, 288, 299, 310, 316) — 8 AsyncAPIError raise sites verified
- `tests/unit/test_exceptions.py` — Existing exception test patterns (MagicMock usage, pytest patterns)
- `pyproject.toml` — pytest 9.0.3 in dev dependencies, Python >=3.11 requirement
- Python stdlib documentation: warnings module (https://docs.python.org/3/library/warnings.html) — DeprecationWarning and stacklevel behavior
- Pytest documentation: pytest.warns (https://docs.pytest.org/en/stable/how-to/capture-warnings.html) — Testing warnings

### Secondary (MEDIUM confidence)

- `12-CONTEXT.md` — User decisions D-01 through D-04 (signature compat, deprecation mechanism, raise sites, docs)
- `HTTPX-MIGRATION.md` (lines 146-162) — Phase 5 exception update plan, AsyncAPIError deprecation path

### Tertiary (LOW confidence)

None. All findings verified via codebase or stdlib docs.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH — warnings module is stdlib (verified available), pytest.warns tested in environment
- Architecture: HIGH — Dual-signature init pattern verified against existing AsyncAPIError code and Python inheritance semantics
- Pitfalls: HIGH — Common issues derived from Python warnings gotchas (stacklevel, filtered by default) and signature mismatch errors in inheritance

**Research date:** 2026-05-05
**Valid until:** 2026-06-05 (30 days — stable stdlib features, no fast-moving dependencies)
