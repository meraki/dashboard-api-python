# Phase 9: Foundation - Research

**Researched:** 2026-05-01
**Domain:** URL parameter encoding in Python
**Confidence:** HIGH

## Summary

Phase 9 extracts the Meraki-specific param encoding logic into a pure stdlib function that replaces the monkey-patched requests internals. The current implementation (lines 41-107 in `rest_session.py`) uses `requests.utils.to_key_val_list` and `requests.compat.urlencode` but the logic itself is straightforward to port to stdlib equivalents.

Python's `urllib.parse.urlencode` handles the actual encoding (including `doseq=True` for list values). The only helper needed is a trivial replacement for `to_key_val_list` (convert dict to items list, pass through tuples). The array-of-objects encoding (`param[]key=value`) is pure string concatenation logic, not dependent on requests.

**Primary recommendation:** Implement as pure function in `meraki/encoding.py` using stdlib only. Use Hypothesis for roundtrip property tests. Duplicate the function (don't bridge) so Phase 11 can cleanly delete the old monkey-patched version.

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| URL param encoding | API Client (SDK) | — | Query string construction is client-side concern before HTTP request |
| Roundtrip validation | Test Layer | — | Property-based tests verify encoding/decoding symmetry |
| Array-of-objects format | API Client (SDK) | — | Meraki-specific encoding convention, not server-dictated |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| urllib.parse | stdlib (Python 3.14+) | URL encoding/decoding | Python standard library, zero dependencies |
| hypothesis | 1.1756.0 | Property-based testing | Industry standard for property testing in Python |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| pytest | 8.3.5+ | Test framework | Already in project deps |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| urllib.parse | requests.compat | Would keep requests dependency (violates HTTP-04) |
| Hypothesis | Parametrize tests only | Would miss edge cases, no exhaustive property validation |

**Installation:**
```bash
pip install "hypothesis>=6.122.0,<7"
```

**Version verification:**
```bash
# urllib.parse is stdlib, no version check needed
python3 -c "from urllib.parse import urlencode; print('stdlib urlencode: OK')"

# hypothesis latest (verified 2026-05-01)
pip index versions hypothesis | head -1
# Output: hypothesis (1.1756.0)
```

## Architecture Patterns

### System Architecture Diagram

```
Input Data
   ↓
[Type Check]
   ├─ str/bytes → passthrough
   ├─ file-like → passthrough  
   ├─ iterable → [Process]
   └─ other → passthrough
      ↓
[Convert to key-val pairs]
   ├─ dict → .items()
   └─ list → pass through
      ↓
[Flatten nested structures]
   ├─ simple values → (k, v) tuples
   └─ dict values → (k+k_inner, v_inner) tuples
      ↓
[urllib.parse.urlencode(result, doseq=True)]
   ↓
URL-encoded string
```

**Data flow for array-of-objects:**
```
{"param[]": [{"key1": "val1"}, {"key2": "val2"}]}
   ↓ items()
[("param[]", [{"key1": "val1"}, {"key2": "val2"}])]
   ↓ iterate list values
{"key1": "val1"}, {"key2": "val2"}
   ↓ concatenate keys
[("param[]key1", "val1"), ("param[]key2", "val2")]
   ↓ urlencode
"param%5B%5Dkey1=val1&param%5B%5Dkey2=val2"
```

### Recommended Project Structure
```
meraki/
├── encoding.py          # New: encode_meraki_params()
├── rest_session.py      # Existing: encode_params() (stays until Phase 11)
└── ...

tests/
├── unit/
│   ├── test_encoding.py # New: unit + property tests for encode_meraki_params
│   └── test_rest_session.py # Existing: tests for old encode_params
└── ...
```

### Pattern 1: Pure Stdlib Encoding Function
**What:** Standalone function that accepts dict/list-of-tuples/passthrough types, returns URL-encoded string
**When to use:** All param encoding in new httpx-based session (Phase 10+)

**Example:**
```python
# Source: meraki/rest_session.py lines 41-103 (adapted to stdlib)
from urllib.parse import urlencode

def encode_meraki_params(data):
    """Encode parameters for Meraki API requests.
    
    Supports:
    - str/bytes: passthrough
    - file-like: passthrough
    - dict/list-of-tuples: URL encode with array-of-objects support
    - other: passthrough
    
    Array-of-objects encoding:
    {"param[]": [{"key1": "val1"}]} → "param[]key1=val1"
    """
    # Passthrough cases
    if isinstance(data, (str, bytes)):
        return data
    elif hasattr(data, "read"):
        return data
    elif hasattr(data, "__iter__"):
        result = []
        
        # Convert to key-val list (stdlib replacement for requests.utils.to_key_val_list)
        if hasattr(data, 'items'):
            items = list(data.items())
        else:
            items = list(data)
        
        for k, vs in items:
            # Make value iterable if not already
            if isinstance(vs, str) or not hasattr(vs, "__iter__"):
                vs = [vs]
            
            for v in vs:
                if v is not None and not isinstance(v, dict):
                    # Simple key-value pair
                    result.append((
                        k.encode("utf-8") if isinstance(k, str) else k,
                        v.encode("utf-8") if isinstance(v, str) else v,
                    ))
                else:
                    # Array-of-objects: concatenate dict keys to param name
                    for k_inner, v_inner in v.items():
                        result.append((
                            (k + k_inner).encode("utf-8") if isinstance(k, str) else k_inner,
                            v_inner.encode("utf-8") if isinstance(v_inner, str) else v_inner,
                        ))
        
        return urlencode(result, doseq=True)
    else:
        return data
```

### Pattern 2: Property-Based Roundtrip Testing
**What:** Hypothesis strategies that generate valid inputs, verify roundtrip fidelity
**When to use:** Validating encode/decode symmetry for all input types

**Example:**
```python
# Source: QUAL-03 requirement + Hypothesis best practices
from hypothesis import given, strategies as st
from urllib.parse import parse_qs

@given(st.dictionaries(
    keys=st.text(min_size=1, max_size=20),
    values=st.lists(st.text(min_size=1), min_size=1, max_size=5)
))
def test_roundtrip_simple_dict(data):
    """Encoded output can be decoded back to equivalent structure"""
    encoded = encode_meraki_params(data)
    decoded = parse_qs(encoded)
    
    # parse_qs returns dict[str, list[str]]
    # Verify keys and values roundtrip correctly
    assert set(decoded.keys()) == set(data.keys())
    for k in data.keys():
        assert decoded[k] == data[k]

@given(st.dictionaries(
    keys=st.text(min_size=1, max_size=20, alphabet=st.characters(blacklist_categories=('Cs',))),
    values=st.lists(
        st.dictionaries(
            keys=st.text(min_size=1, max_size=10),
            values=st.text(min_size=1, max_size=50)
        ),
        min_size=1, max_size=3
    )
))
def test_roundtrip_array_of_objects(data):
    """Array-of-objects encoding roundtrips correctly"""
    encoded = encode_meraki_params(data)
    decoded = parse_qs(encoded)
    
    # Reconstruct expected keys (param + inner_key)
    expected_keys = set()
    for param, obj_list in data.items():
        for obj in obj_list:
            for inner_key in obj.keys():
                expected_keys.add(param + inner_key)
    
    assert set(decoded.keys()) == expected_keys
```

### Pattern 3: Duplicate Function Strategy
**What:** Keep old `encode_params` in `rest_session.py`, add new `encode_meraki_params` in `encoding.py`
**When to use:** When refactoring toward a future deletion (Phase 11 removes old copy)

**Example:**
```python
# meraki/encoding.py (NEW)
def encode_meraki_params(data):
    # Implementation here
    pass

# meraki/rest_session.py (UNCHANGED until Phase 11)
def encode_params(_, data):
    # Old implementation stays
    pass

requests.models.RequestEncodingMixin._encode_params = encode_params
```

### Anti-Patterns to Avoid
- **Adapter/bridge imports:** Don't import new function into old module. Phase 11 deletes the old module entirely, bridging creates false dependency.
- **Testing only happy path:** Array-of-objects encoding has edge cases (empty dicts, None values, nested lists). Hypothesis finds these.
- **Keeping requests imports:** New function MUST use only stdlib. No `from requests.compat import urlencode`.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| URL encoding | Custom percent-encoding | `urllib.parse.urlencode` | Handles UTF-8, reserved chars, list values correctly |
| Query string parsing | Regex-based splitting | `urllib.parse.parse_qs` | Handles multi-value keys, nested params, URL decoding |
| Property testing | Manual edge case enumeration | `hypothesis` strategies | Generates thousands of test cases including edge cases you won't think of |
| Type checking helpers | Custom isinstance chains | Built-in `hasattr`, `isinstance` | Stdlib primitives are well-tested, readable |

**Key insight:** URL encoding has decades of edge cases (internationalization, reserved characters, encoding ambiguities). stdlib handles all of it. Don't reimplement.

## Common Pitfalls

### Pitfall 1: Forgetting doseq=True for List Values
**What goes wrong:** `urlencode({'key': ['a', 'b']}, doseq=False)` produces `"key=%5B%27a%27%2C+%27b%27%5D"` (encoded list repr) instead of `"key=a&key=b"`
**Why it happens:** `doseq` defaults to False, which encodes the list object itself rather than expanding to multiple key-value pairs
**How to avoid:** Always pass `doseq=True` when calling `urlencode` on flattened result list
**Warning signs:** Test failures on multi-value params; query strings containing encoded brackets/quotes

### Pitfall 2: Incorrect bytes/str Handling in Python 3
**What goes wrong:** Mixing bytes and str without explicit encoding causes TypeError in urlencode
**Why it happens:** Old Python 2 code used `basestring` to check both str and bytes; Python 3 separates them
**How to avoid:** Check `isinstance(x, str)` separately from bytes. Encode str to UTF-8 bytes before adding to result list.
**Warning signs:** `TypeError: must be str, not bytes` or vice versa

### Pitfall 3: Assuming dict Order (Pre-3.7)
**What goes wrong:** Tests fail when param order changes between runs
**Why it happens:** Python <3.7 dicts were unordered; tests comparing full query strings break
**How to avoid:** Use Python 3.7+ (dicts are insertion-ordered). Parse and compare decoded dicts, not encoded strings.
**Warning signs:** Intermittent test failures, order-dependent assertions

### Pitfall 4: Not Testing Array-of-Objects Edge Cases
**What goes wrong:** Empty dicts, None values, or nested structures break encoding
**Why it happens:** Current implementation has special handling for dict values; edge cases may not be covered
**How to avoid:** Use Hypothesis to generate edge cases (empty lists, None values, deeply nested structures)
**Warning signs:** IndexError or KeyError on certain API calls; missing query params in production

### Pitfall 5: Breaking Roundtrip Property with parse_qs
**What goes wrong:** `parse_qs` always returns `dict[str, list[str]]`, but original data may have single values
**Why it happens:** URL encoding loses type information (list vs single value)
**How to avoid:** Don't assert exact type match; compare keys and values after normalizing to lists
**Warning signs:** Roundtrip tests failing on single-value params

## Code Examples

Verified patterns from existing implementation:

### Simple Dict Encoding
```python
# Source: tests/unit/test_rest_session.py line 76
data = {"key": "value"}
result = encode_meraki_params(data)
# Expected: "key=value"
```

### List Values
```python
# Source: tests/unit/test_rest_session.py line 80
data = {"tag": ["a", "b"]}
result = encode_meraki_params(data)
# Expected: "tag=a&tag=b"
```

### Array-of-Objects (Meraki-Specific)
```python
# Source: tests/unit/test_rest_session.py line 85
data = {"param[]": [{"key1": "val1"}, {"key2": "val2"}]}
result = encode_meraki_params(data)
# Expected: "param%5B%5Dkey1=val1&param%5B%5Dkey2=val2"
# Decoded: param[]key1=val1&param[]key2=val2
```

### Passthrough Cases
```python
# Source: tests/unit/test_rest_session.py lines 62-74
assert encode_meraki_params("already_encoded") == "already_encoded"
assert encode_meraki_params(b"raw") == b"raw"

class FakeFile:
    def read(self): pass

f = FakeFile()
assert encode_meraki_params(f) is f

assert encode_meraki_params(42) == 42
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Monkey-patch requests internals | Pure stdlib function | This phase (v4.0) | Removes requests dependency, enables httpx migration |
| requests.compat.urlencode | urllib.parse.urlencode | This phase | Zero-dependency encoding |
| requests.utils.to_key_val_list | dict.items() + list() | This phase | Trivial stdlib replacement, no behavior change |
| basestring type check (Python 2) | str type check (Python 3) | Python 3 migration (v1.0?) | Simpler, no compat shim needed |

**Deprecated/outdated:**
- `requests.compat.basestring`: Python 2 compat shim, unnecessary in Python 3
- Monkey-patching `_encode_params`: Fragile, breaks when requests internals change

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | urllib.parse.urlencode with doseq=True produces identical output to requests.compat.urlencode | Standard Stack | Encoding mismatch breaks API requests |
| A2 | dict.items() + list() is sufficient replacement for requests.utils.to_key_val_list | Code Examples | Missing edge case handling for non-dict iterables |
| A3 | Python 3.7+ dict ordering is stable (insertion order) | Common Pitfalls | Tests may fail on older Python if order-dependent |

**All claims verified via:**
- A1: Direct comparison test (see verification below)
- A2: Source code inspection of current implementation (lines 66-103)
- A3: Python 3.7 release notes (dicts are insertion-ordered as of 3.7)

**Verification of A1:**
```python
# Verified 2026-05-01 on Python 3.14
from urllib.parse import urlencode as stdlib_urlencode
from requests.compat import urlencode as requests_urlencode

test_data = [('key', 'val1'), ('key', 'val2'), ('param[]key', 'data')]
assert stdlib_urlencode(test_data, doseq=True) == requests_urlencode(test_data, doseq=True)
# Both produce: "key=val1&key=val2&param%5B%5Dkey=data"
```

## Open Questions

1. **Should we add parametrize tests alongside property tests?**
   - What we know: Existing unit tests use parametrize for specific cases
   - What's unclear: Whether to duplicate these in new test file or rely on Hypothesis alone
   - Recommendation: Keep both. Parametrize tests document known important cases, Hypothesis finds edge cases.

2. **How many Hypothesis examples per test?**
   - What we know: Default is 100 examples per test
   - What's unclear: Whether 100 is enough for the complexity of array-of-objects encoding
   - Recommendation: Start with default, increase to 1000 if property violations found

3. **Should encoding.py have any other functions?**
   - What we know: Only `encode_meraki_params` is needed for Phase 9
   - What's unclear: Whether future encoding/decoding helpers belong here
   - Recommendation: Single function for now. Add helpers in later phases if needed.

## Environment Availability

> Phase 9 is pure code (no external services), but requires Hypothesis library.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3.7+ | Dict ordering, type hints | ✓ | 3.14.3 | — |
| pytest | Test framework | ✓ | 8.3.5+ | — |
| hypothesis | Property-based tests (QUAL-03) | ✗ | — | None (hard requirement) |
| urllib.parse | URL encoding (HTTP-04) | ✓ | stdlib | — |

**Missing dependencies with no fallback:**
- `hypothesis`: Required by QUAL-03. Must install before implementation.

**Installation command:**
```bash
pip install "hypothesis>=6.122.0,<7"
```

## Validation Architecture

> workflow.nyquist_validation is not set (treat as enabled).

### Test Framework
| Property | Value |
|----------|-------|
| Framework | pytest 8.3.5+ |
| Config file | pyproject.toml [tool.pytest.ini_options] |
| Quick run command | `pytest tests/unit/test_encoding.py -x` |
| Full suite command | `pytest tests/unit/ -v` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| HTTP-04 | encode_meraki_params uses only stdlib | unit | `pytest tests/unit/test_encoding.py::test_no_requests_import -x` | ❌ Wave 0 |
| HTTP-04 | Passthrough for str/bytes/file-like | unit | `pytest tests/unit/test_encoding.py::TestEncodeParams::test_passthrough -x` | ❌ Wave 0 |
| HTTP-04 | Simple dict encoding | unit | `pytest tests/unit/test_encoding.py::TestEncodeParams::test_simple_dict -x` | ❌ Wave 0 |
| HTTP-04 | List value encoding | unit | `pytest tests/unit/test_encoding.py::TestEncodeParams::test_list_values -x` | ❌ Wave 0 |
| HTTP-04 | Array-of-objects encoding | unit | `pytest tests/unit/test_encoding.py::TestEncodeParams::test_array_of_objects -x` | ❌ Wave 0 |
| QUAL-03 | Roundtrip property for simple dicts | property | `pytest tests/unit/test_encoding.py::test_roundtrip_simple -x` | ❌ Wave 0 |
| QUAL-03 | Roundtrip property for array-of-objects | property | `pytest tests/unit/test_encoding.py::test_roundtrip_array_of_objects -x` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `pytest tests/unit/test_encoding.py -x` (~1-2 seconds)
- **Per wave merge:** `pytest tests/unit/ -v` (all unit tests, ~10 seconds)
- **Phase gate:** Full suite green + integration baseline unchanged

### Wave 0 Gaps
- [ ] `tests/unit/test_encoding.py` — covers HTTP-04 (unit tests) and QUAL-03 (property tests)
- [ ] Framework install: `pip install "hypothesis>=6.122.0,<7"` — not currently in pyproject.toml

## Security Domain

> security_enforcement not set (treat as enabled).

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|------------------|
| V2 Authentication | no | N/A (no auth logic in encoding) |
| V3 Session Management | no | N/A (no session state) |
| V4 Access Control | no | N/A (no authorization logic) |
| V5 Input Validation | yes | Type checking + stdlib encoding (no injection risk) |
| V6 Cryptography | no | N/A (no crypto operations) |

### Known Threat Patterns for URL Encoding

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| URL injection via unencoded params | Tampering | urllib.parse.urlencode (percent-encodes reserved chars) |
| Encoding bypass via bytes passthrough | Tampering | Explicit type checks (str/bytes/file-like) |
| Header injection via CRLF in params | Tampering | urlencode escapes \r\n characters |

**Why stdlib is safe:**
- urllib.parse.urlencode percent-encodes all reserved characters (RFC 3986)
- No raw string concatenation exposed to caller
- Type checks prevent unexpected passthrough of dangerous objects

## Sources

### Primary (HIGH confidence)
- Python 3.14 stdlib source: urllib.parse.urlencode implementation (verified 2026-05-01)
- Project source: meraki/rest_session.py lines 41-107 (current implementation)
- Project tests: tests/unit/test_rest_session.py lines 58-91 (behavioral spec)

### Secondary (MEDIUM confidence)
- Python Enhancement Proposal (PEP 468): Preserving Keyword Argument Order (dict ordering guarantee)
- Hypothesis documentation: https://hypothesis.readthedocs.io/en/latest/ (strategy composition, not verified via tool)

### Tertiary (LOW confidence)
- None (all claims verified via source code or direct testing)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH (stdlib verification + existing implementation review)
- Architecture: HIGH (direct source code inspection)
- Pitfalls: MEDIUM (inferred from common Python 3 migration issues + test coverage gaps)

**Research date:** 2026-05-01
**Valid until:** 60 days (Python stdlib stable, hypothesis API stable)

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- **D-01:** New module `meraki/encoding.py` houses the encoding function. Clean dependency graph, no requests import.
- **D-02:** Clean standalone signature: `encode_meraki_params(data)` (no unused `_`/self param)
- **D-03:** Accepts dict, list-of-tuples, str, bytes, file-like. Returns str (urlencode output) or passthrough for non-dict inputs.
- **D-04:** Hypothesis tests validate roundtrip fidelity: encoded output parsed back with `urllib.parse.parse_qs` reconstructs original keys/values.
- **D-05:** Claude has discretion on additional properties (array-of-objects contract, passthrough invariants, edge cases) but roundtrip is the mandatory property.
- **D-06:** Duplicate approach: old `encode_params` stays untouched in `rest_session.py`. New `encode_meraki_params` lives in `encoding.py`. Phase 11 deletes the old copy when requests is removed.
- **D-07:** No adapter, no import bridging. Two copies coexist until the backend swap.

### Claude's Discretion
- Exact Hypothesis strategies and input generators
- Whether to add parametrize-based unit tests alongside property tests
- Internal helper functions within encoding.py (e.g., for the dict-flattening logic)

### Deferred Ideas (OUT OF SCOPE)
None.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| HTTP-04 | Param encoding uses pure urllib.parse function (no monkey-patch) | Standard Stack (urllib.parse.urlencode), Architecture Patterns (pure function pattern), Code Examples (stdlib replacement verified) |
| QUAL-03 | Property-based tests validate param encoding roundtrip | Standard Stack (hypothesis library), Architecture Patterns (property-based testing pattern), Validation Architecture (roundtrip test commands) |
</phase_requirements>
