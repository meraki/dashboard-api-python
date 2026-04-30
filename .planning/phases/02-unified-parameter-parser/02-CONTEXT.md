# Phase 2: Unified Parameter Parser - Context

**Gathered:** 2026-04-30
**Status:** Ready for planning

<domain>
## Phase Boundary

Unified `parse_params_v3` function that merges path, query, and body parameters from an OASv3 operation into a single normalized param dict. Handles path-level parameter inheritance, `nullable` annotations, and `oneOf` query param documentation.

</domain>

<decisions>
## Implementation Decisions

### Function Interface & Integration
- parse_params_v3(operation, path_item, spec) signature; path_item provides access to path-level parameters
- Detect `perPage` in merged params and call existing `generate_pagination_parameters` (matches v2 behavior)
- Return tuple `(params_dict, metadata_dict)` where metadata contains content_type from requestBody
- Reuse v2's `return_params` filter logic for param_filters support (import from common.py or inline equivalent)

### OASv3 Feature Handling
- `nullable` boolean already present in param dict entries from Phase 1 parse_request_body (D-10)
- `oneOf` query params documented as "string or object" in type field (per success criteria)
- Path-level parameters inherited into operation; operation params override on matching `name`

### Testing Strategy
- Golden-file test with synthetic v3 fixture validates full parser output format
- Extend existing `tests/generator/fixtures/synthetic_v3_spec.json` with path-level params and oneOf examples
- Snapshot comparison for full output validation (JSON golden file)

### Claude's Discretion
- Internal helper naming and decomposition within parser_v3.py
- Exact golden file format (JSON vs inline assertion)

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `generator/parser_v3.py`: resolve_ref, clear_cache, parse_request_body from Phase 1
- `generator/common.py`: return_params, generate_pagination_parameters
- `tests/generator/fixtures/synthetic_v3_spec.json`: existing fixture with $ref, requestBody examples

### Established Patterns
- Module-level functions with spec passed as argument (D-08 from Phase 1)
- Param dicts: {name: {required, in, type, description, nullable, ...}}
- Tests use pytest fixtures loading JSON from fixtures directory

### Integration Points
- parse_params_v3 calls parse_request_body (Phase 1) for body params
- parse_params_v3 calls resolve_ref (Phase 1) for $ref in parameters
- Output consumed by Phase 3 (generation integration) via template rendering

</code_context>

<specifics>
## Specific Ideas

No specific requirements beyond the decisions above. Standard approaches are fine.

</specifics>

<deferred>
## Deferred Ideas

None. Discussion stayed within phase scope.

</deferred>

---

*Phase: 02-unified-parameter-parser*
*Context gathered: 2026-04-30*
