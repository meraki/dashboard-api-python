# Phase 7: Legacy Cleanup - Context

**Gathered:** 2026-04-30
**Status:** Ready for planning
**Mode:** Auto-generated (infrastructure phase)

<domain>
## Phase Boundary

Remove abandoned generate_library_oasv3.py, update all imports and CI workflows referencing old filenames.

</domain>

<decisions>
## Implementation Decisions

### Claude's Discretion
All implementation choices are at Claude's discretion. Key constraints:

- Delete `generator/generate_library_oasv3.py` (dead code, abandoned monolithic v3 attempt)
- Update any CI workflows referencing old generator filenames
- Update any documentation referencing old filenames
- Ensure all internal imports use correct current filenames

</decisions>

<code_context>
## Existing Code Insights

### Files to remove
- `generator/generate_library_oasv3.py` (abandoned v3 attempt, not used by anything)

### References to update
- Check .github/workflows/ for references to generate_library_v3.py or generate_library_oasv3.py
- Check scripts/semantic_diff_v2_v3.py for old references
- Check any README or docs referencing old filenames

</code_context>

<specifics>
## Specific Ideas

None.

</specifics>

<deferred>
## Deferred Ideas

None.

</deferred>
