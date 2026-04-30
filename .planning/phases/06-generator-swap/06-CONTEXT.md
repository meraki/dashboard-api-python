# Phase 6: Generator Swap - Context

**Gathered:** 2026-04-30
**Status:** Ready for planning
**Mode:** Auto-generated (infrastructure phase)

<domain>
## Phase Boundary

Rename v2 generator to generate_library_oasv2.py with deprecation warning, promote v3 generator to generate_library.py as the new default entry point.

</domain>

<decisions>
## Implementation Decisions

### Claude's Discretion
All implementation choices are at Claude's discretion. Key constraints:

- `generate_library.py` must become v3 generator (copy/move generate_library_v3.py content)
- `generate_library_oasv2.py` must be the old v2 generator (rename generate_library.py)
- Deprecation warning on v2: `warnings.warn("generate_library_oasv2.py is deprecated, use generate_library.py", DeprecationWarning)`
- Both generators must still work after the swap
- Tests must still pass

</decisions>

<code_context>
## Existing Code Insights

### Files to swap
- `generator/generate_library.py` (current v2, 800+ lines) -> `generator/generate_library_oasv2.py`
- `generator/generate_library_v3.py` (current v3, 630 lines) -> `generator/generate_library.py`

### Integration Points
- Tests reference `generate_library_v3.py` in imports
- CI workflows may reference `generate_library.py`
- `generate_library.py` is called from project scripts

</code_context>

<specifics>
## Specific Ideas

No specific requirements beyond the swap.

</specifics>

<deferred>
## Deferred Ideas

None.

</deferred>
