# Domain Pitfalls: OASv3 Code Generator

**Domain:** OpenAPI 3.0 code generation for existing v2 system
**Researched:** 2026-04-29
**Context:** Adding OASv3 generator alongside working v2 generator for Meraki Dashboard API Python SDK

## Critical Pitfalls

Mistakes that cause rewrites or major issues.

### Pitfall 1: Infinite Loop in $ref Resolution Without Cycle Detection
**What goes wrong:** Circular `$ref` chains (Schema A → Schema B → Schema A) cause infinite recursion and stack overflow. The abandoned oasv3 file has NO cycle detection in `resolve_ref()` (lines 26-41).

**Why it happens:** OpenAPI 3.0 spec allows circular references for recursive data structures. Simple traversal hits the same refs repeatedly without tracking visited nodes.

**Consequences:** Generator crashes on valid specs with recursive schemas. Silent hang if max recursion isn't reached but loops for seconds. Production failure on spec updates that introduce circular refs.

**Prevention:**
```python
def resolve_ref(spec: dict, ref: str, _visiting: set | None = None) -> dict | None:
    if _visiting is None:
        _visiting = set()
    
    if ref in _visiting:
        return None  # Circular ref detected
    
    _visiting.add(ref)
    # ... rest of resolution logic
```

**Detection:** Spec with `#/components/schemas/Foo` containing `properties: { child: { $ref: "#/components/schemas/Foo" } }` triggers the issue. Test fixture MUST include circular ref case.

### Pitfall 2: Missing $ref Cache Causes O(n²) Performance
**What goes wrong:** Resolving the same `$ref` thousands of times when spec has shared schemas referenced by 298+ endpoints. Each resolution traverses the full JSON pointer path.

**Why it happens:** No memoization. Abandoned oasv3 file calls `resolve_ref()` inline everywhere (lines 54, 167, 188, 235) with no caching.

**Consequences:** 30+ second generation time for live spec (vs <5s for v2). CI timeouts. Developer friction during iteration.

**Prevention:** Add cache on first spec access:
```python
if "_ref_cache" not in spec:
    spec["_ref_cache"] = {}

if ref in spec["_ref_cache"]:
    return spec["_ref_cache"][ref]

# resolve and cache before returning
```

**Detection:** `time python generate_library_oasv3.py` taking >10s on live spec when v2 takes <5s.

### Pitfall 3: Path-Level Parameter Inheritance Not Implemented
**What goes wrong:** OASv3 allows parameters at path level that apply to all operations. Abandoned file ignores `paths[path]["parameters"]` and only checks `paths[path][method]["parameters"]` (line 209, 441). Missing required path params like `organizationId`.

**Why it happens:** v2 doesn't have path-level params. Direct port of v2 logic misses this OASv3 feature.

**Consequences:** Generated functions missing required parameters. Runtime errors when calling SDK methods. Silent param drops if parameter appears at path level but not operation level.

**Prevention:**
```python
# Collect path-level params first
path_level_params = paths[path].get("parameters", [])
operation_params = endpoint.get("parameters", [])

# Merge with operation params overriding on (name, in) collision
merged = merge_params(path_level_params, operation_params)
```

**Detection:** Golden file test with path-level param that doesn't appear in operation-level params. Diff v3 vs v2 output on live spec shows missing params.

### Pitfall 4: requestBody Content-Type Priority Inverted
**What goes wrong:** Abandoned file checks `application/json` first (line 155) and ignores other content types. Multipart/form-data endpoints (file uploads) get parsed as JSON and lose binary field markers.

**Why it happens:** Defaulting to JSON without checking all content types. Spec can have multiple `requestBody.content` keys for different consumers.

**Consequences:** File upload endpoints broken (missing `Content-Type: multipart/form-data`). Binary fields treated as string params. Runtime errors when SDK tries to JSON-encode binary data.

**Prevention:**
```python
content = request_body.get("content", {})

# Priority order: json → multipart → octet-stream → warn on unsupported
if "application/json" in content:
    # parse JSON schema
elif "multipart/form-data" in content:
    # parse form data, mark format:binary fields
elif "application/octet-stream" in content:
    # single binary body param
else:
    # Warn about unsupported content type, don't silently drop
```

**Detection:** Endpoint with `multipart/form-data` in fixture generates code expecting JSON. Manual test of file upload fails.

### Pitfall 5: Template Data Format Mismatch (Breaking Change)
**What goes wrong:** v3 parser returns `dict[str, dict]` for params but v2 templates expect different keys or structure. Template renders wrong code (empty param lists, missing type annotations).

**Why it happens:** v3 has `parameter.schema.type` nested one level deeper than v2's `parameter.type` OR `parameter.schema.properties`. Changing parse logic without checking template expectations.

**Consequences:** Generated functions missing params entirely. Type annotations wrong (all params become `str`). Pagination/kwargs handling broken. Appears to work but output is subtly wrong.

**Prevention:** 
- Golden file tests that CHECK output structure, not just "does it run"
- Parse v3 into SAME dict format v2 produces: `{ "paramName": { "type": "...", "required": bool, "in": "...", "description": "..." } }`
- Test against existing function_template.jinja2 WITHOUT template changes

**Detection:** Golden file content differs from expected in param types or counts. Ruff errors in generated code. CI diff check shows structural differences.

## Moderate Pitfalls

### Pitfall 6: oneOf Reported as Generic "object" Type
**What goes wrong:** oneOf query params (string OR object with lt/gt/lte/gte) get type annotation `object`, losing string option. Docstring says "object" when user can pass a string.

**Why it happens:** Abandoned file doesn't check for `oneOf` (missing from `get_schema_from_item`). Falls back to `type: object` from schema.

**Consequences:** Misleading documentation. Static analysis tools reject valid string inputs. User confusion when passing string and it works despite docs saying "object".

**Prevention:**
```python
if "oneOf" in schema:
    # Check constituent types
    types = [s.get("type") for s in schema["oneOf"]]
    if "string" in types and "object" in types:
        return ("string or object", f"string or object with properties: {list_object_props(schema)}")
```

**Detection:** Endpoint with oneOf query param generates docstring without "string or" prefix.

### Pitfall 7: No Validation for Missing $ref Targets
**What goes wrong:** Spec references `#/components/schemas/NonExistent` that doesn't exist. `resolve_ref` returns `None` silently (line 40). Param gets skipped or defaults to wrong type.

**Why it happens:** Defensive programming (return None on error) without logging or validation step.

**Consequences:** Missing parameters in generated code. Silent data loss. Hard to debug ("why is this param not showing up?").

**Prevention:**
```python
if result is None:
    # Log warning with context
    print(f"WARNING: Failed to resolve $ref '{ref}' in operation '{operation}'")
    # Option: treat as opaque 'object' type rather than skip
```

**Detection:** Spec with broken `$ref` generates code without warnings. Add fixture with invalid ref, verify warning appears.

## Minor Pitfalls

### Pitfall 8: Array Serialization Style Ignored
**What goes wrong:** OASv3 has `style` (form/spaceDelimited/pipeDelimited) and `explode` (true/false) for array params. Abandoned file ignores these (no check for `style` in param parsing).

**Why it happens:** v2 doesn't have these attributes. Defaulting to single strategy without checking spec.

**Consequences:** Array query params serialized wrong format. API rejects requests with "invalid format" errors. Works in some cases (default form+explode matches API expectation) but breaks on non-default.

**Prevention:**
```python
# OAS3 defaults: style=form, explode=true for query params
style = param.get("style", "form")
explode = param.get("explode", True)

# Document in param description how arrays are sent
if param_type == "array":
    params[name]["serialization"] = {"style": style, "explode": explode}
```

**Detection:** Endpoint with array param + explicit style generates code that doesn't respect style.

### Pitfall 9: nullable Not Reflected in Type Annotations
**What goes wrong:** Param has `nullable: true` but generated function signature is `param: str` instead of `param: str | None`.

**Why it happens:** Abandoned file checks `nullable` in parsing (not shown in excerpt) but doesn't thread through to type annotation logic.

**Consequences:** Type checkers reject valid `None` inputs. Misleading type hints. Runtime passes None but static analysis fails.

**Prevention:**
```python
# In function definition builder
if values["type"] == "string":
    if values.get("nullable", False):
        definition += f", {p}: str | None"
    else:
        definition += f", {p}: str"
```

**Detection:** Param with `nullable: true` generates signature without `| None`.

### Pitfall 10: Vendor Extension Loss
**What goes wrong:** `x-batchable-actions` survives (line 292) but other `x-*` fields at parameter or operation level get dropped during parsing.

**Why it happens:** Explicit extraction only for known vendor extensions. Generic `x-*` fields not forwarded.

**Consequences:** Custom tooling that relies on vendor extensions breaks. Metadata loss that downstream consumers need.

**Prevention:**
```python
# Copy all x- prefixed keys
for key, value in schema.items():
    if key.startswith("x-"):
        params[name][key] = value
```

**Detection:** Spec with custom `x-meraki-preview` flag on param doesn't appear in generated code.

## Phase-Specific Warnings

| Phase Topic | Likely Pitfall | Mitigation |
|-------------|---------------|------------|
| Phase 1: Core v3 Parsing | Circular $ref causing crash | Implement cycle detection in `resolve_ref` with visited-set guard |
| Phase 1: Core v3 Parsing | Missing $ref cache causing slow generation | Add `spec["_ref_cache"]` dict, check before traversal |
| Phase 2: Unified parse_params | Path-level params ignored | Merge path-level and operation-level params before parsing |
| Phase 2: Unified parse_params | requestBody content-type priority wrong | Parse all content types, document priority order |
| Phase 3: HTTP Method Parsers | Template data format doesn't match v2 | Golden file tests BEFORE changing templates |
| Phase 4: Module Generation | locals() antipattern survives in v3 | Update templates to explicit param construction DURING v3 work |
| Phase 5: Batch Actions | Operation type lookup fails for v3 structure | Test batch endpoint in golden fixture, verify operation field |
| Phase 6: oneOf Handling | Generic "object" type loses oneOf semantics | `resolve_oneof_type` helper with accurate type strings |
| Phase 7: Testing | Golden files too rigid (byte-for-byte match) | v3 golden files allow enhanced docstrings, not v2 parity |
| Phase 8: CI Drift Detection | False positives from docstring enhancements | Semantic diff (params, types, structure) not text diff |

## Integration Gotchas

### Gotcha 1: Shared common.py Not Threadsafe for spec Param
**What:** v2's `common.organize_spec()` doesn't expect `spec` arg. Threading spec through all functions breaks imports if v2 and v3 generators run concurrently in tests.

**Impact:** Test pollution. Race conditions if CI runs both generators in parallel.

**Fix:** Either accept breaking import change (update v2 if needed) OR namespace v3 helpers differently (`common_v3.py`).

### Gotcha 2: Template Filter Registration Skipped
**What:** v2 registers `jinja_env.filters["to_double_quote_list"]` (line 299 in v2). If oasv3 file forgets this, template rendering fails with "unknown filter" error.

**Impact:** Generation crashes late (after parsing succeeds). Confusing error far from root cause.

**Fix:** Copy ALL jinja_env setup from v2, not just template loading. Add test that uses filter.

### Gotcha 3: ruff Invocation Assumes cwd
**What:** v2 runs `subprocess.run(["ruff", "check", "--fix", "meraki/"])` assuming cwd is project root (line 306). If v3 generator changes cwd or runs from generator/ dir, ruff formats wrong files or fails.

**Impact:** Generated code not formatted. CI fails on style check. Looks like generator is broken when it's just cwd issue.

**Fix:** Use absolute paths for ruff invocation. Test in tmp_path directory like golden tests do.

### Gotcha 4: Non-Generated Files Downloaded Every Run
**What:** Lines 272-287 in v2 download from GitHub every generation (no cache check). v3 copy/paste means slower iteration and network dependency.

**Impact:** Offline generation fails. Slow feedback loop during development.

**Fix:** Check if files exist and are current version before downloading. Or expect files present (don't auto-download).

## "Looks Done But Isn't" Checklist

Generator appears to work but has subtle correctness issues:

- [ ] Circular $ref test in fixture (not just inline schemas)
- [ ] Path-level parameters inherited into operations (not just operation-level)
- [ ] requestBody with multiple content-types handled correctly (not just JSON)
- [ ] oneOf query params documented as "string or object" (not generic "object")
- [ ] nullable params get `| None` type annotation (not bare type)
- [ ] Array params respect style/explode attributes (not default serialization for all)
- [ ] Missing $ref target logs warning (not silent None return)
- [ ] Template receives same dict format as v2 (not nested differently)
- [ ] v3 golden files validate v3-specific output (not byte-for-byte match with v2)
- [ ] CI drift detection checks semantic structure (not just text diff)
- [ ] Batch actions work with v3 operation lookup (not hardcoded from v2 assumptions)
- [ ] Enum assertions survive parsing (not lost in translation)
- [ ] Pagination params injected for perPage endpoints (not dropped)
- [ ] locals() antipattern replaced in templates (not persisted from v2)
- [ ] $ref cache used for performance (not resolving same ref 1000x)

## Technical Debt Patterns

### Debt Pattern 1: Monolithic parse_params (Abandoned Approach)
**What:** Single 200-line function handling path, query, body, requestBody, $ref, oneOf all inline. Abandoned oasv3 file has this (lines 196-260).

**Why it's debt:** Impossible to test individual parsing steps. Changes in one param type affect all others. Hard to debug which clause failed.

**Better approach:** Separate functions: `parse_path_params()`, `parse_query_params()`, `parse_request_body()`, then merge. Each unit-testable.

### Debt Pattern 2: No Intermediate Representation
**What:** Parsing directly into template dict format. Any template change requires parser changes.

**Why it's debt:** Tight coupling. Can't reuse parser for different output formats (like .pyi stubs). Hard to diff "what did parsing extract" vs "what did template render".

**Better approach:** Parse to normalized IR (dataclass or TypedDict), then map IR → template dict separately. Enables stub generation reusing same IR.

### Debt Pattern 3: Error Handling by Omission
**What:** Failed $ref → return None → param dropped silently. Unsupported content-type → skip without warning (implicit in abandoned code).

**Why it's debt:** Silent failures. Debugging "why is param missing" requires reading spec + code. No visibility into what went wrong.

**Better approach:** Explicit warnings. Fail-fast option (`--strict` flag) for CI that errors on missing refs.

## Sources

**Code analysis:**
- `generator/generate_library_oasv3.py` (abandoned attempt, lines 26-833)
- `generator/generate_library.py` (v2 production generator, lines 1-800)
- `generator/function_template.jinja2` (template expectations)
- `tests/generator/test_generate_library_golden.py` (test patterns)
- `OASV3-MIGRATION.md` (known challenges)

**Research:**
- OpenAPI 3.0.3 specification (spec.openapis.org) - $ref resolution warnings, circular reference gaps
- Swagger.io $ref documentation - sibling element confusion, escape character issues
- Codebase git history - abandoned oasv3 file introduced commit a0ea07f, minimal iteration

**Confidence:** HIGH for pitfalls observed in abandoned code, MEDIUM for pitfalls from spec analysis (OAS3 docs incomplete on edge cases), LOW for external tooling pitfalls (Brave API unavailable, OpenAPI Generator issues page shallow)

**Analysis method:** Compared abandoned oasv3 file against working v2 generator line-by-line. Identified missing features (cycle detection, caching, path-level params). Cross-referenced with OAS3 spec for undocumented behaviors. Verified template expectations from jinja2 files.
