# Phase 1: Parser Foundation - Context

**Gathered:** 2026-04-30
**Status:** Ready for planning

<domain>
## Phase Boundary

Core v3 parsing functions that normalize `$ref` resolution and `requestBody` handling into v2-compatible param dicts. Output feeds into Phase 2 (unified param parser) and Phase 3 (generation integration).

</domain>

<decisions>
## Implementation Decisions

### $ref Resolution
- **D-01:** Module-level dict cache keyed by JSON pointer string, populated during parse, cleared between runs
- **D-02:** Cycle detection via visited set passed through recursive calls; if pointer already seen, return sentinel/empty dict
- **D-03:** Unresolvable refs raise an exception (hard fail). Spec correctness is required for generation to proceed

### requestBody Content Types
- **D-04:** Multipart/form-data properties normalize to same dict format as JSON body params (`{name: {required, in: 'body', type, description}}`). Content-type distinction handled at HTTP layer, not param layer
- **D-05:** Octet-stream endpoints produce a single param entry: `{name: 'file', type: 'file', in: 'body', required: true}`
- **D-06:** Operation-level `content_type` metadata field tracks which content-type the requestBody uses (for downstream HTTP header selection)

### Module Architecture
- **D-07:** Single file: `generator/parser_v3.py` (sibling to `generate_library.py` and `common.py`)
- **D-08:** Standalone module-level functions (not class-based). Spec passed as argument. Matches v2 style
- **D-09:** Cache is module-level dict within `parser_v3.py`

### Output Contract
- **D-10:** Param dicts include all v2 keys (required, in, type, description, enum, items) plus `nullable: true/false`
- **D-11:** No version signaling or compatibility flags. Templates that don't reference `nullable` simply ignore it. Phase 2 adds template logic to consume it

### Claude's Discretion
- None; all areas had explicit user decisions

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### Existing Generator Code
- `generator/generate_library.py` - v2 generator (production reference for architecture and param dict format)
- `generator/generate_library_oasv3.py` - Abandoned v3 attempt (reference for what NOT to do; has basic resolve_ref without caching/cycles)
- `generator/common.py` - Shared utilities (must be reused, not duplicated)

### Codebase Analysis
- `.planning/codebase/ARCHITECTURE.md` - Layer diagram and data flow
- `.planning/codebase/CONVENTIONS.md` - Naming, style, import patterns

### Spec
- Live v3 spec: `https://api.meraki.com/api/v1/openapiSpec?version=3` (OpenAPI 3.0.1)

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- `generator/common.py`: Shared utilities already imported by v2 generator
- `generate_pagination_parameters()`: Identical in both v2 and abandoned v3; can be shared
- `return_params()`: Filter logic identical in both; can be shared or imported from common
- `docs_url()`: Identical helper; belongs in common

### Established Patterns
- v2 uses standalone functions with spec/params passed as args (not OOP)
- Param dicts are flat: `{name: {required: bool, in: str, type: str, description: str, ...}}`
- `kwargs.update(locals())` antipattern in generated code (Phase 3 replaces this, not Phase 1)

### Integration Points
- `parser_v3.py` will be imported by future `generate_library_v3.py` (Phase 3)
- Must produce dicts compatible with `return_params()` filter logic
- Must produce dicts compatible with existing Jinja2 templates (same keys they already reference)

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

*Phase: 01-parser-foundation*
*Context gathered: 2026-04-30*
