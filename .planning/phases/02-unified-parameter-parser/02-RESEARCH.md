# Phase 2: Unified Parameter Parser - Research

**Researched:** 2026-04-30
**Domain:** OpenAPI v3 parameter parsing and merging
**Confidence:** HIGH

## Summary

Phase 2 implements `parse_params_v3()` to merge path, query, and body parameters from OASv3 operations into a normalized dict matching v2 generator output format. Core responsibilities: inherit path-level parameters (with operation-level override on name+in match), handle `nullable: true` flag from Phase 1, document `oneOf` query params, and respect array param serialization defaults.

OASv3 spec analysis confirms: (1) Meraki spec has NO path-level parameters in production, making inheritance a defensive feature tested synthetically; (2) `oneOf` query params exist for date filters (string OR object with comparative operators); (3) `nullable` appears in requestBody schemas (already handled by Phase 1 `parse_request_body`), rarely in query/path parameters; (4) array params lack explicit `style`/`explode` attributes, defaulting to `form`/`true` per OASv3 spec.

**Primary recommendation:** Build `parse_params_v3(operation, path_item, spec)` that merges operation.parameters + path_item.parameters (op overrides on name match), calls Phase 1's `parse_request_body()` for body params, detects `perPage` for pagination injection, and documents `oneOf` as "string or object". Golden-file test validates output structure.

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| PARSE-03 | Generator handles `nullable: true` with `| None` type annotations and docstring notes | `nullable` field already in param dict from Phase 1 `parse_request_body`; parser adds field for query/path params if present (rare in Meraki spec) |
| PARSE-04 | Generator inherits path-level parameters, operation overrides on name+in match | OASv3 spec: path-level params inherited, operation overrides by (name, in) composite key; Meraki spec has zero path-level params but feature needed for spec compliance |
| PARSE-05 | Generator resolves `oneOf` schemas as "string or object" with sub-property documentation | Meraki spec uses `oneOf: [{type: object, properties: {lt, gt, ...}}, {type: string}]` for date filters; document as "string or object" with property details |
| PARSE-06 | Generator respects array param `style`/`explode` attributes (default: form + explode:true) | Meraki spec arrays lack explicit `style`/`explode`; OASv3 defaults: query params use `style: form, explode: true` (separate param per value) |
</phase_requirements>

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- parse_params_v3(operation, path_item, spec) signature; path_item provides access to path-level parameters
- Detect `perPage` in merged params and call existing `generate_pagination_parameters` (matches v2 behavior)
- Return tuple `(params_dict, metadata_dict)` where metadata contains content_type from requestBody
- Reuse v2's `return_params` filter logic for param_filters support (import from common.py or inline equivalent)
- `nullable` boolean already present in param dict entries from Phase 1 parse_request_body (D-10)
- `oneOf` query params documented as "string or object" in type field (per success criteria)
- Path-level parameters inherited into operation; operation params override on matching `name`

### Claude's Discretion
- Internal helper naming and decomposition within parser_v3.py
- Exact golden file format (JSON vs inline assertion)

### Deferred Ideas (OUT OF SCOPE)
None. Discussion stayed within phase scope.
</user_constraints>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Parameter merging (path/query/body) | Parser (parse_params_v3) | — | Single function owns merge logic for all param sources |
| Path-level inheritance | Parser (parse_params_v3) | — | OASv3 spec feature; parser enforces override-by-name-and-in rule |
| `nullable` field propagation | Parser (parse_request_body + parse_params_v3) | — | Phase 1 handles body params; Phase 2 adds field for query/path params |
| `oneOf` documentation | Parser (parse_params_v3) | Template renderer | Parser sets `type: "string or object"`; templates render docstrings |
| Pagination param injection | Parser (parse_params_v3) | — | Detects `perPage`, calls `generate_pagination_parameters` from common.py |
| `style`/`explode` defaults | Parser (parse_params_v3) | — | OASv3 defaults (form/true); parser documents in param dict for template use |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Python stdlib | 3.10+ | Dict merging, basic parsing | Project baseline per generate_library.py requirements |

### Supporting
N/A - pure Python parsing logic, no external dependencies.

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Manual dict merge | pydantic for param validation | Over-engineering; dict-based params match existing SDK contract |

**Installation:**
No new dependencies - Phase 2 builds on Phase 1 functions in parser_v3.py.

## Architecture Patterns

### System Architecture Diagram

```
┌────────────────────────────────────────────────────────────────┐
│                         parse_params_v3                         │
│                   (operation, path_item, spec)                  │
└────────────────────────────────────────────────────────────────┘
                                  │
                ┌─────────────────┼─────────────────┐
                │                 │                 │
                ▼                 ▼                 ▼
     ┌──────────────────┐  ┌─────────────┐  ┌──────────────────┐
     │ Parse query/path │  │ Inherit     │  │ parse_request_   │
     │ params from      │  │ path-level  │  │ body() [Phase 1] │
     │ operation.params │  │ params      │  │                  │
     └──────────────────┘  └─────────────┘  └──────────────────┘
                │                 │                 │
                │                 │                 │
                └─────────────────┼─────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Merge params                │
                    │ (op overrides path on name) │
                    └─────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Apply transforms:           │
                    │ - Resolve $ref              │
                    │ - Add nullable field        │
                    │ - Document oneOf            │
                    │ - Set style/explode         │
                    └─────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Detect perPage →            │
                    │ inject pagination params    │
                    └─────────────────────────────┘
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Return (params_dict,        │
                    │         metadata_dict)      │
                    └─────────────────────────────┘
```

### Recommended Project Structure
```
generator/
├── parser_v3.py         # Phase 1 + Phase 2 functions (resolve_ref, parse_request_body, parse_params_v3)
├── common.py            # Shared utilities (return_params, generate_pagination_parameters)
└── generate_library_oasv3.py  # Abandoned v3 generator (reference only)

tests/generator/
├── test_parser_v3.py    # Phase 1 + Phase 2 tests
└── fixtures/
    └── synthetic_v3_spec.json  # Extended with path-level params, oneOf examples
```

### Pattern 1: Path-Level Parameter Inheritance
**What:** Merge path_item.parameters into operation params; operation params with matching (name, in) override path-level entries.
**When to use:** Every parse_params_v3 call, even if path_item.parameters is empty (defensive coding).
**Example:**
```python
# Source: OASv3 spec + CONTEXT.md decisions
def parse_params_v3(operation: dict, path_item: dict, spec: dict) -> tuple[dict, dict]:
    """
    Parse and merge parameters from path-level and operation-level.
    
    Args:
        operation: Operation dict (e.g., paths["/foo"]["post"])
        path_item: PathItem dict (e.g., paths["/foo"]) for path-level params
        spec: Full OpenAPI spec for $ref resolution
        
    Returns:
        Tuple of (params_dict, metadata_dict)
    """
    merged_params = {}
    
    # Step 1: Inherit path-level parameters
    path_level_params = path_item.get("parameters", [])
    for p in path_level_params:
        # Resolve $ref if present
        if "$ref" in p:
            p = resolve_ref(spec, p["$ref"])
        # Use (name, in) as composite key
        key = (p["name"], p.get("in", "query"))
        merged_params[key] = p
    
    # Step 2: Add/override with operation-level parameters
    op_params = operation.get("parameters", [])
    for p in op_params:
        if "$ref" in p:
            p = resolve_ref(spec, p["$ref"])
        key = (p["name"], p.get("in", "query"))
        merged_params[key] = p  # Overrides path-level if key exists
    
    # Step 3: Parse into v2-compatible dict format
    params = {}
    for (name, location), p in merged_params.items():
        # ... extract type, description, nullable, etc.
        pass
    
    # Step 4: Merge requestBody params (from Phase 1)
    body_params, content_type = parse_request_body(operation, spec)
    params.update(body_params)
    
    # Step 5: Detect perPage and inject pagination
    if "perPage" in params:
        params.update(generate_pagination_parameters(operation["operationId"]))
    
    metadata = {"content_type": content_type}
    return params, metadata
```

### Pattern 2: oneOf Query Parameter Documentation
**What:** When parameter.schema.oneOf exists, document as "string or object" with sub-property descriptions.
**When to use:** Query params with `oneOf` (Meraki uses for date filter operators).
**Example:**
```python
# Source: Meraki spec analysis + CONTEXT.md success criteria
def _document_oneof(schema: dict) -> tuple[str, str]:
    """
    Document oneOf schema as "string or object" with property details.
    
    Args:
        schema: Parameter schema dict with oneOf key
        
    Returns:
        Tuple of (type_string, description_addition)
    """
    if "oneOf" not in schema:
        return schema.get("type", "object"), ""
    
    oneof_types = [s.get("type") for s in schema["oneOf"] if "type" in s]
    
    # Extract object properties if one oneOf branch is object
    object_props = []
    for s in schema["oneOf"]:
        if s.get("type") == "object" and "properties" in s:
            object_props = list(s["properties"].keys())
            break
    
    type_str = " or ".join(sorted(set(oneof_types)))  # "object or string"
    
    if object_props:
        desc_add = f" (object supports: {', '.join(object_props)})"
    else:
        desc_add = ""
    
    return type_str, desc_add
```

### Pattern 3: nullable Field Propagation
**What:** Add `nullable: bool` to every param entry; extract from schema.nullable or default False.
**When to use:** All query/path parameters (body params already handled by Phase 1).
**Example:**
```python
# Source: Phase 1 parse_request_body + CONTEXT.md nullable decision
def _extract_param_entry(p: dict, spec: dict) -> dict:
    """
    Convert OASv3 parameter to v2-compatible param dict entry.
    
    Args:
        p: Parameter dict from operation.parameters or path_item.parameters
        spec: Full spec for $ref resolution
        
    Returns:
        Dict with keys: required, in, type, description, nullable
    """
    schema = p.get("schema", {})
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])
    
    entry = {
        "required": p.get("required", False),
        "in": p.get("in", "query"),
        "type": schema.get("type", "string"),
        "description": p.get("description", schema.get("description", "")),
        "nullable": schema.get("nullable", False),  # OASv3 nullable flag
    }
    
    # Include enum if present
    if "enum" in schema:
        entry["enum"] = schema["enum"]
    
    # Include array items if present
    if schema.get("type") == "array" and "items" in schema:
        entry["items"] = schema["items"]
    
    return entry
```

### Anti-Patterns to Avoid
- **Ignoring path_item.parameters:** Even if Meraki spec has none, OASv3 allows them; parser must be spec-compliant.
- **Forgetting (name, in) composite key:** Two params with same name but different `in` are distinct; don't override incorrectly.
- **Returning content_type outside metadata dict:** v2 parse_params returns only params; v3 needs metadata for Phase 3 integration.

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Param filtering (required/optional/path/query/body) | Custom filter logic | `return_params()` from common.py or generate_library.py | v2 generator already has this; reuse maintains parity |
| Pagination param injection | Inline dict construction | `generate_pagination_parameters()` from generate_library.py | v2 behavior includes special-case logic for getNetworkEvents; reuse ensures compatibility |
| $ref resolution | Parse JSON pointers manually | `resolve_ref()` from Phase 1 | Already implemented with caching and cycle detection |

**Key insight:** v2 generator has battle-tested param filtering and pagination logic. Don't reimplement; import or copy directly.

## Common Pitfalls

### Pitfall 1: Path-Level Parameter Override Logic
**What goes wrong:** Parser overrides path-level params by `name` only, ignoring `in` field; creates bugs when param names collide across locations.
**Why it happens:** OASv3 spec says "unique by name and location" but it's easy to forget the composite key.
**How to avoid:** Use `(name, in)` tuple as dict key during merge; operation params override path params only when BOTH match.
**Warning signs:** Test with param `foo` in path (in=path) and `foo` in query (in=query) at operation level; if path-level `foo` disappears, key is wrong.

### Pitfall 2: oneOf Handling Complexity
**What goes wrong:** Trying to validate which oneOf branch applies at parse time; parser becomes a type checker.
**Why it happens:** oneOf can have complex schemas; tempting to "resolve" which one is correct.
**How to avoid:** Parser documents possibilities, doesn't validate. For Meraki's `startDate` oneOf, document as "string or object" with object properties listed; runtime validation happens at API call time.
**Warning signs:** Parser imports validation libraries or has conditionals checking param values.

### Pitfall 3: style/explode Ignored
**What goes wrong:** Parser ignores `style` and `explode` attributes; array serialization behavior is undocumented.
**Why it happens:** Meraki spec doesn't set these explicitly; defaults are implicit.
**How to avoid:** Document defaults in param dict: `"style": "form", "explode": True` for query arrays. Templates may need this for serialization hints.
**Warning signs:** Generated code serializes arrays incorrectly (comma-separated instead of separate params).

### Pitfall 4: Forgetting Pagination Detection
**What goes wrong:** Parser merges params but forgets to check for `perPage`; pagination params missing from output.
**Why it happens:** Pagination injection is v2-specific behavior not obvious from OASv3 spec.
**How to avoid:** After merging all params (path + op + body), check `"perPage" in params` and call `generate_pagination_parameters()` if present.
**Warning signs:** Golden-file test with `perPage` param doesn't include `total_pages` or `direction` in output.

## Code Examples

Verified patterns from existing codebase:

### v2 parse_params Signature (for reference)
```python
# Source: generator/generate_library.py line 198
def parse_params(operation: str, parameters: dict, param_filters=None):
    """v2 generator signature - single parameters arg, no path_item."""
    if param_filters is None:
        param_filters = list()
    if parameters is None:
        return {}
    return unpack_params(operation, parameters, param_filters)
```

### v2 return_params (reuse in v3)
```python
# Source: generator/generate_library.py line 84
def return_params(operation: str, params: dict, param_filters):
    """Filter params by type (required, optional, path, query, body, etc)."""
    if not param_filters:
        return params
    else:
        ret = {}
        if "required" in param_filters:
            ret.update({k: v for k, v in params.items() if "required" in v and v["required"]})
        if "pagination" in param_filters:
            ret.update(generate_pagination_parameters(operation) if "perPage" in params else {})
        if "optional" in param_filters:
            ret.update({k: v for k, v in params.items() if "required" in v and not v["required"]})
        if "path" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "path"})
        if "query" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "query"})
        if "body" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "body"})
        if "array" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["type"] == "array"})
        if "enum" in param_filters:
            ret.update({k: v for k, v in params.items() if "enum" in v})
        return ret
```

### Phase 1 parse_request_body Output Format
```python
# Source: generator/parser_v3.py line 76
params, content_type = parse_request_body(operation, spec)
# params = {
#     "name": {
#         "required": True,
#         "in": "body",
#         "type": "string",
#         "description": "Network name",
#         "nullable": False,
#     },
#     "timeZone": {
#         "required": False,
#         "in": "body",
#         "type": "string",
#         "description": "Timezone",
#         "nullable": True,
#     }
# }
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| v2: parameters list only at operation level | v3: parameters at path AND operation level | OASv3 spec (2017) | Parser must merge two sources with override logic |
| v2: `in: body` with schema.properties | v3: requestBody with content types | OASv3 spec (2017) | Body params require separate parsing (Phase 1) |
| Type unions via `type: [string, null]` | `nullable: true` boolean | OASv3.0 (deprecated in 3.1) | Phase 2 works with 3.0 style only |
| Implicit array serialization | Explicit `style`/`explode` | OASv3 spec | Parser documents defaults when absent |

**Deprecated/outdated:**
- OASv2 `in: body` parameters: OASv3 uses `requestBody` instead
- OASv3.1 type arrays: Project uses OASv3.0 `nullable` flag, not `type: [string, null]`

## Open Questions

1. **Should parse_params_v3 accept param_filters argument?**
   - What we know: v2 parse_params accepts optional param_filters list
   - What's unclear: CONTEXT.md mentions "reuse return_params filter logic" but doesn't specify if parse_params_v3 signature includes filters
   - Recommendation: Add optional `param_filters=None` arg to match v2 signature; call `return_params()` before returning (maintains v2 API compatibility)

2. **How to document oneOf object properties in param description?**
   - What we know: Success criteria says "string or object" for type field
   - What's unclear: Should object properties be in description field or separate metadata?
   - Recommendation: Document as `type: "string or object"` with appended description like "(object supports: lt, gt, lte, gte, neq)"

3. **Should style/explode be added to param dict even if not in spec?**
   - What we know: OASv3 defaults are `form`/`true` for query arrays
   - What's unclear: Do templates need explicit style/explode fields?
   - Recommendation: Add `"style": "form", "explode": True` to array query params; document as "(array serialized as separate params)" in description

## Environment Availability

No external dependencies beyond Python 3.10+ stdlib. Phase 2 builds on Phase 1 functions in parser_v3.py.

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | pytest 7.4.0 |
| Config file | tests/pytest.ini |
| Quick run command | `pytest tests/generator/test_parser_v3.py -x` |
| Full suite command | `pytest tests/generator/ -v` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PARSE-03 | nullable field in param entries | unit | `pytest tests/generator/test_parser_v3.py::TestParseParamsV3::test_nullable_field -x` | ❌ Wave 0 |
| PARSE-04 | Path-level param inheritance with op override | unit | `pytest tests/generator/test_parser_v3.py::TestParseParamsV3::test_path_level_inheritance -x` | ❌ Wave 0 |
| PARSE-05 | oneOf documented as "string or object" | unit | `pytest tests/generator/test_parser_v3.py::TestParseParamsV3::test_oneof_query_param -x` | ❌ Wave 0 |
| PARSE-06 | style/explode defaults for array params | unit | `pytest tests/generator/test_parser_v3.py::TestParseParamsV3::test_array_param_defaults -x` | ❌ Wave 0 |
| ALL | Golden-file snapshot test | integration | `pytest tests/generator/test_parser_v3.py::TestParseParamsV3::test_golden_file -x` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `pytest tests/generator/test_parser_v3.py::TestParseParamsV3 -x`
- **Per wave merge:** `pytest tests/generator/ -v`
- **Phase gate:** Full suite green before `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `tests/generator/test_parser_v3.py` — add `TestParseParamsV3` class with 5 tests above
- [ ] `tests/generator/fixtures/synthetic_v3_spec.json` — extend with path-level params, oneOf examples
- [ ] `tests/generator/fixtures/parse_params_v3_golden.json` — golden output for snapshot test

## Sources

### Primary (HIGH confidence)
- [VERIFIED: Meraki Dashboard API live spec] OASv3 spec fetched via `https://api.meraki.com/api/v1/openapiSpec?version=3` on 2026-04-30
- [VERIFIED: OpenAPI Specification v3.0.3] Path-level parameter inheritance, style/explode defaults from https://spec.openapis.org/oas/v3.0.3
- [VERIFIED: Codebase grep] v2 generator functions (return_params, generate_pagination_parameters) in generator/generate_library.py

### Secondary (MEDIUM confidence)
- [CITED: OpenAPI Specification v3.0.3] `nullable` property in Schema Object (section 4.7.24 referenced but not fully documented in fetched content)

### Tertiary (LOW confidence)
None - all claims verified against live spec or official docs.

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - pure Python, no external deps
- Architecture: HIGH - pattern matches Phase 1 + v2 generator conventions
- Pitfalls: MEDIUM - inferred from v2 code + OASv3 spec ambiguities

**Research date:** 2026-04-30
**Valid until:** 2026-07-30 (90 days - OASv3 spec is stable)
