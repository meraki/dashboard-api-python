# Phase 5: Testing & CI - Context

**Gathered:** 2026-04-30
**Status:** Ready for planning
**Mode:** Auto-generated (infrastructure phase, discuss skipped)

<domain>
## Phase Boundary

Comprehensive test suite exercising all v3-specific features plus CI workflow for semantic drift detection between v2 and v3 generator output on live spec.

</domain>

<decisions>
## Implementation Decisions

### Claude's Discretion
All implementation choices are at Claude's discretion. Key constraints from success criteria:

- Synthetic fixture must exercise ALL v3 features: $ref with cycles, requestBody, oneOf, nullable, multipart, path-level params
- Golden-file tests validate v3 generator output for sync, async, batch modules (semantic correctness)
- CI workflow runs semantic diff (params, types, structure) not byte-for-byte text diff
- Tests should validate that v3 output is semantically equivalent to v2 where applicable
- CI drift detection catches regressions when live spec changes

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `tests/generator/fixtures/synthetic_v3_spec.json`: Existing Phase 1 fixture (basic $ref, requestBody)
- `tests/generator/fixtures/synthetic_v3_spec_gen.json`: Existing Phase 3 fixture (generation testing)
- `tests/generator/fixtures/parse_params_v3_golden.json`: Golden file from Phase 2
- `tests/generator/test_parser_v3.py`: 34 tests from Phases 1-2
- `tests/generator/test_generate_library_v3.py`: 15+ tests from Phases 3-4
- `tests/generator/test_generate_stubs.py`: 8 tests from Phase 4

### Established Patterns
- pytest with fixtures loading JSON from fixtures directory
- Golden-file comparison for output format locking
- Existing CI via GitHub Actions (check .github/workflows/)

### Integration Points
- CI workflow at .github/workflows/ (new file)
- Tests run via pytest from project root
- Live spec at https://api.meraki.com/api/v1/openapiSpec?version=3

</code_context>

<specifics>
## Specific Ideas

No specific requirements. Standard approaches are fine.

</specifics>

<deferred>
## Deferred Ideas

None.

</deferred>
