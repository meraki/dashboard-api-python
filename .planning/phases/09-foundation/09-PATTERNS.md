# Phase 9: Foundation - Pattern Map

**Mapped:** 2026-05-01
**Files analyzed:** 2
**Analogs found:** 2 / 2

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `meraki/encoding.py` | utility | transform | `meraki/common.py` | role-match |
| `tests/unit/test_encoding.py` | test | N/A | `tests/unit/test_rest_session.py` | exact |

## Pattern Assignments

### `meraki/encoding.py` (utility, transform)

**Analog:** `meraki/common.py`

**Imports pattern** (lines 1-6):
```python
import platform
import re
import sys
import urllib.parse

from meraki.exceptions import PythonVersionError, SessionInputError
```

**Core pattern** (stdlib-only utility function):
```python
# Source: meraki/common.py lines 77-90
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

**Function structure** (no class, pure function):
```python
# Source: meraki/common.py lines 9-23
def check_python_version():
    # Check minimum Python version
    
    if not (int(platform.python_version_tuple()[0]) == 3 and int(platform.python_version_tuple()[1]) >= 10):
        message = (
            f"This library requires Python 3.10 at minimum..."
        )
        
        raise PythonVersionError(message)
```

**Docstring style** (multi-line, behavior-focused):
```python
# Source: meraki/rest_session.py lines 42-57
def encode_params(_, data):
    """Encode parameters in a piece of data.

    Will successfully encode parameters when passed as a dict or a list of
    2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
    if parameters are supplied as a dict.

    MERAKI OVERRIDE:
    By default, when parameters are supplied as a dict, only the object keys
    are encoded.

    Ex. {"param": [{"key_1":"value_1"}, {"key_2":"value_2"}]} => ?param[]=key_1&param[]=key_2

    Now when parameters are supplied as a dict, dict keys will be appended to
    parameter names. This adds support for the "array of objects" query parameter type.

    Ex. {"param": [{"key_1":"value_1"}, {"key_2":"value_2"}]} => ?param[]key_1=value_1&param[]key_2=value_2
    """
```

**Error handling pattern** (raise built-in exceptions, not custom):
```python
# Note: common.py raises custom exceptions (PythonVersionError, SessionInputError)
# But encoding.py should raise built-in exceptions (TypeError, ValueError) for invalid inputs
# since it's a low-level utility with no domain-specific error context
```

**Type checking pattern** (isinstance + hasattr):
```python
# Source: meraki/rest_session.py lines 59-63
if isinstance(data, (str, bytes)):
    return data
elif hasattr(data, "read"):
    return data
elif hasattr(data, "__iter__"):
    # process iterable
```

---

### `tests/unit/test_encoding.py` (test, N/A)

**Analog:** `tests/unit/test_rest_session.py`

**Imports pattern** (lines 1-8):
```python
# Source: tests/unit/test_rest_session.py lines 1-8 (inferred from structure)
# Standard pattern:
import pytest
from meraki.encoding import encode_meraki_params
from urllib.parse import parse_qs
from hypothesis import given, strategies as st
```

**Test class structure** (lines 61-92):
```python
class TestEncodeParams:
    def test_string_passthrough(self):
        assert encode_params(None, "already_encoded") == "already_encoded"

    def test_bytes_passthrough(self):
        assert encode_params(None, b"raw") == b"raw"

    def test_file_like_passthrough(self):
        class FakeFile:
            def read(self):
                pass

        f = FakeFile()
        assert encode_params(None, f) is f

    def test_simple_dict(self):
        result = encode_params(None, {"key": "value"})
        assert "key=value" in result

    def test_list_values(self):
        result = encode_params(None, {"tag": ["a", "b"]})
        assert "tag=a" in result
        assert "tag=b" in result

    def test_dict_values_appended_keys(self):
        result = encode_params(None, {"param[]": [{"key1": "val1"}, {"key2": "val2"}]})
        assert "param%5B%5Dkey1=val1" in result
        assert "param%5B%5Dkey2=val2" in result

    def test_none_passthrough(self):
        assert encode_params(None, 42) == 42
```

**Test naming convention** (test_<behavior>):
```python
# Pattern: test_<input_type>_<expected_behavior>
# Examples from lines 62-91:
# - test_string_passthrough
# - test_bytes_passthrough
# - test_simple_dict
# - test_list_values
# - test_dict_values_appended_keys
```

**Assertion style** (direct asserts, not pytest.raises for happy path):
```python
# Source: lines 62-91
assert encode_params(None, "already_encoded") == "already_encoded"
assert "key=value" in result
assert "tag=a" in result
```

**Mock pattern for file-like objects** (lines 68-74):
```python
def test_file_like_passthrough(self):
    class FakeFile:
        def read(self):
            pass

    f = FakeFile()
    assert encode_params(None, f) is f
```

**Property-based test pattern** (NOT in existing codebase, ADD for this phase):
```python
# Source: RESEARCH.md lines 176-218 (new pattern to introduce)
from hypothesis import given, strategies as st

@given(st.dictionaries(
    keys=st.text(min_size=1, max_size=20),
    values=st.lists(st.text(min_size=1), min_size=1, max_size=5)
))
def test_roundtrip_simple_dict(data):
    """Encoded output can be decoded back to equivalent structure"""
    encoded = encode_meraki_params(data)
    decoded = parse_qs(encoded)
    
    assert set(decoded.keys()) == set(data.keys())
    for k in data.keys():
        assert decoded[k] == data[k]
```

---

## Shared Patterns

### Stdlib-Only Imports
**Source:** `meraki/common.py` lines 1-6
**Apply to:** `meraki/encoding.py`
```python
import platform
import re
import sys
import urllib.parse

from meraki.exceptions import [SomeException]  # Only if needed
```

**Pattern:**
- Stdlib imports first
- Third-party imports second (but encoding.py should have NONE)
- Local imports third (only for exceptions if needed)

### Utility Function Structure
**Source:** `meraki/common.py` (multiple functions)
**Apply to:** `encode_meraki_params` in `meraki/encoding.py`

**Pattern:**
- No classes, pure functions
- Docstring with examples
- Type checks at function entry (isinstance, hasattr)
- Single return type (or passthrough for multiple types)
- Raise built-in exceptions (TypeError, ValueError) not custom

### Test Organization
**Source:** `tests/unit/test_rest_session.py` lines 61-92
**Apply to:** `tests/unit/test_encoding.py`

**Pattern:**
- Test class per function (`TestEncodeParams` → `TestEncodeMerakiParams`)
- One test method per input type/behavior
- Direct asserts (no pytest.raises for success cases)
- Test name format: `test_<input>_<behavior>`
- Inline helper classes for mocks (FakeFile pattern)

### Type Checking Pattern
**Source:** `meraki/rest_session.py` lines 59-63
**Apply to:** `encode_meraki_params` passthrough logic

```python
if isinstance(data, (str, bytes)):
    return data
elif hasattr(data, "read"):
    return data
elif hasattr(data, "__iter__"):
    # process
else:
    return data  # fallback passthrough
```

---

## No Analog Found

No files without analogs. Both files have clear patterns to copy from.

---

## Metadata

**Analog search scope:**
- `meraki/*.py` (7 files scanned)
- `tests/unit/test_*.py` (7 files scanned)

**Files scanned:** 14

**Pattern extraction date:** 2026-05-01

**Key insights:**
- `common.py` is the canonical example of stdlib-only utility functions in this codebase
- `test_rest_session.py` contains the behavioral spec for `encode_params` (lines 61-92)
- No existing property-based tests (Hypothesis) in codebase, this phase introduces them
- Encoding logic from `rest_session.py` lines 41-107 is the implementation blueprint (just swap requests imports for stdlib)
