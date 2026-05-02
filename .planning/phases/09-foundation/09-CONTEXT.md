# Phase 9: Foundation - Context

**Gathered:** 2026-05-01
**Status:** Ready for planning

<domain>
## Phase Boundary

Pure function for param encoding that replaces the monkey-patched `requests` internals. Library-agnostic (stdlib only), with property-based tests proving correctness.

</domain>

<decisions>
## Implementation Decisions

### Module Location
- **D-01:** New module `meraki/encoding.py` houses the encoding function. Clean dependency graph, no requests import.

### Function Signature
- **D-02:** Clean standalone signature: `encode_meraki_params(data)` (no unused `_`/self param)
- **D-03:** Accepts dict, list-of-tuples, str, bytes, file-like. Returns str (urlencode output) or passthrough for non-dict inputs.

### Property-Based Tests
- **D-04:** Hypothesis tests validate roundtrip fidelity: encoded output parsed back with `urllib.parse.parse_qs` reconstructs original keys/values.
- **D-05:** Claude has discretion on additional properties (array-of-objects contract, passthrough invariants, edge cases) but roundtrip is the mandatory property.

### Transition Bridge
- **D-06:** Duplicate approach: old `encode_params` stays untouched in `rest_session.py`. New `encode_meraki_params` lives in `encoding.py`. Phase 11 deletes the old copy when requests is removed.
- **D-07:** No adapter, no import bridging. Two copies coexist until the backend swap.

### Claude's Discretion
- Exact Hypothesis strategies and input generators
- Whether to add parametrize-based unit tests alongside property tests
- Internal helper functions within encoding.py (e.g., for the dict-flattening logic)

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Current Implementation
- `meraki/rest_session.py` lines 41-107 - Current `encode_params` function + monkey-patch line
- `tests/unit/test_rest_session.py` lines 58-91 - Existing unit tests for encode_params

### Requirements
- `.planning/REQUIREMENTS.md` - HTTP-04 (stdlib param encoding), QUAL-03 (property-based tests)

### Integration Baseline
- `tests/integration/baseline/` - Phase 8 regression gate (32 tests, all passing)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `encode_params` in `meraki/rest_session.py`: current implementation to replicate behavior from
- `tests/unit/test_rest_session.py`: existing test cases that define expected behavior (can be copied/adapted)
- `from requests.compat import basestring, urlencode`: these need stdlib replacements (str check, urllib.parse.urlencode)
- `requests.utils.to_key_val_list`: used internally, needs stdlib equivalent

### Established Patterns
- Function handles three cases: passthrough (str/bytes/file), flat list encoding, array-of-objects with key concatenation
- `param[]key=value` format is the Meraki-specific encoding for array-of-objects
- `doseq=True` passed to urlencode for list values

### Integration Points
- Phase 10 session base class will import from `meraki/encoding.py`
- Phase 11 deletes old `encode_params` + monkey-patch from `rest_session.py`
- Existing unit tests serve as behavioral specification

</code_context>

<specifics>
## Specific Ideas

No specific requirements. Open to standard approaches for the implementation.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within phase scope.

</deferred>

---

*Phase: 09-foundation*
*Context gathered: 2026-05-01*
