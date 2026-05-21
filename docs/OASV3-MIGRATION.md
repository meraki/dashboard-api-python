# OASv3 Generator: Plan

## Context

The Meraki Dashboard API offers both OASv2 (`/openapiSpec`) and OASv3 (`/openapiSpec?version=3`) specs. The v3 spec is OpenAPI 3.0.1 and has features not expressible in v2. The current production generator (`generate_library.py`) only handles v2. An abandoned attempt (`generate_library_oasv3.py`) exists but is monolithic, missing key features, and never finished. Goal: build a proper v3 generator following the v2 generator's modular architecture.

## OASv3 Features Not in v2

| Feature | v2 | v3 | Code-gen impact |
|---------|----|----|-----------------|
| `requestBody` separate from `parameters` | Body params in `parameters` with `"in": "body"` | Dedicated `requestBody.content["application/json"].schema` | Need separate parsing path, merge into same dict format |
| `$ref` references | Inline schemas only | `$ref` to `#/components/schemas/...` | Must resolve at parse time |
| `oneOf` query params | N/A | e.g. `startDate` can be string OR object with `lt/gt/lte/gte/neq` | New param type to handle |
| `nullable: true` | N/A | Properties can be nullable | Informational for docstrings |
| `parameter.schema` structure | `parameter.type` directly OR `parameter.schema.properties` for body | Always `parameter.schema.type` for path/query | Different extraction path |
| `components/schemas` | `definitions` (but Meraki v2 doesn't use it) | Reusable schemas referenced via `$ref` | Need resolver |
| `servers` array | `host` + `basePath` + `schemes` | `servers[].url` with variables | Informational only |

## Approach

Replace `generator/generate_library_oasv3.py` with a proper modular implementation following the v2 generator's structure. Reuse `common.py`, all jinja2 templates, and produce identical output format. Port useful parsing logic from the abandoned oasv3 file.

## Deprecation Plan

Once the v3 generator is fully vetted:

1. **Parity gate**: CI drift detection (step 6 in Verification) must show zero semantic differences on the live spec for 2+ consecutive API releases
2. **Rename**: `generate_library.py` becomes `generate_library_oasv2.py` (deprecated, retained for rollback)
3. **Promote**: `generate_library_oasv3.py` becomes `generate_library.py` (new default)
4. **Update CI/automation**: all workflows, Makefile targets, and docs point to the new default
5. **Deprecation notice**: `generate_library_oasv2.py` gets a warning on import and a docstring noting it is unmaintained
6. **Removal**: delete `generate_library_oasv2.py` after one minor version cycle with no rollbacks

## File Changes

| Action | File |
|--------|------|
| CREATE | `generator/generate_library_oasv3.py` (replace existing abandoned file) |
| CREATE | `tests/generator/fixtures/synthetic_spec_oasv3.json` |
| CREATE | `tests/generator/test_generate_library_oasv3_golden.py` |
| CREATE | `tests/generator/golden_oasv3/meraki/api/networks.py` |
| CREATE | `tests/generator/golden_oasv3/meraki/aio/api/networks.py` |
| CREATE | `tests/generator/golden_oasv3/meraki/api/batch/networks.py` |

## Implementation

### 1. Core v3 Parsing Functions

Port from abandoned oasv3 + enhance:

```python
def resolve_ref(spec: dict, ref: str, _visiting: set | None = None) -> dict | None
    # Follow #/components/schemas/... JSON pointer
    # Circular ref protection: track visited refs, return None on cycle
    # Cache resolved refs on spec["_ref_cache"] to avoid repeated traversal

def get_schema_from_item(item: dict, spec: dict) -> dict | None
    # Extract schema, resolve $ref if present

def parse_request_body(operation: str, request_body: dict, spec: dict) -> dict
    # Parse requestBody.content by content type:
    #   - application/json: parse schema.properties
    #   - multipart/form-data: parse schema.properties, mark file fields (format: binary)
    #   - application/octet-stream: single binary body param
    # Warn and skip unsupported content types
    # Return dict with "in": "body" markers (same format v2 produces)

def resolve_oneof_type(schema: dict) -> tuple[str, str]
    # Returns (type, extra_description) for oneOf schemas
    # Prefers string over object; appends object property names to description
```

### 2. Unified `parse_params` (v3 signature)

```python
def parse_params(
    operation: str,
    parameters: list | None,
    request_body: dict | None,
    spec: dict,
    param_filters=None
) -> dict
```

Internally:

1. Collect path-level parameters, then merge operation-level parameters (operation wins on name+in collision)
2. Parse path/query params from merged `parameters` list (using `param.schema.type`)
3. For array params, respect `style`/`explode` (default: `style: form`, `explode: true` per OAS3 spec)
4. Parse body params from `requestBody` via `parse_request_body()`
5. Merge into single dict
6. Add pagination params if `perPage` present
7. Filter via `return_params()` (ported unchanged from v2)

### 3. HTTP-Method Parsers

Same signatures as v2 but with `request_body` and `spec` threaded through:

```python
def parse_get_params(operation, parameters, request_body, spec)
def parse_post_and_put_params(method, operation, parameters, request_body, spec)
def parse_delete_params(operation, parameters, request_body, spec)
```

### 4. Module Generation

Reuse v2 structure exactly:

- `generate_library()` - top-level orchestrator
- `generate_modules()` - iterate scopes, create files
- `generate_standard_and_async_functions()` - render function templates
- `generate_action_batch_functions()` - render batch templates
- `render_class_template()` - render class headers
- Use `common.organize_spec()` for scope organization
- Use `jinja_env.filters["to_double_quote_list"]` for tag rendering
- Use `ruff` for formatting at end

### 5. `x-batchable-actions` Handling

Present in v3 spec (298 entries). Same structure as v2: `{ group, summary, resource, operation }`. Matching logic unchanged (match `endpoint["description"]` against `action["summary"]`).

```python
batchable_actions = spec["x-batchable-actions"]
```

Look up operation type from spec (not hardcoded), matching v2's behavior.

### 6. `oneOf` Query Parameter Strategy

These are optional query params, so they land in `**kwargs` (not the typed signature). For docstrings:

- Report type as `"string or object"` (accurate, not lossy)
- Document the object sub-properties (e.g., `lt`, `gt`, `lte`, `gte`, `neq`)
- If one were ever required, use no type annotation (bare param name) rather than lying with `str`
- The `rest_session.py` `encode_params` already handles dict values passed as query params

### 7. CLI and Spec Fetching

Same args as v2: `-h`, `-o`, `-k`, `-v`, `-a`, `-g`

```python
requests.get("https://api.meraki.com/api/v1/openapiSpec", params={"version": 3})
```

### 8. Test Fixture (`synthetic_spec_oasv3.json`)

v3 equivalent of the existing `synthetic_spec.json`:

- Same endpoints (getNetworkClients, updateNetworkSettings, deleteNetwork) converted to OASv3 structure (requestBody, parameter.schema, etc.)
- Add one `oneOf` query param to exercise object-type query param handling
- Add one `$ref` usage in requestBody to exercise reference resolution
- Add a circular `$ref` to exercise cycle detection (should resolve to None gracefully)
- Add a `nullable: true` property to exercise nullable annotation
- Add one endpoint with `multipart/form-data` requestBody containing a `format: binary` field
- Add path-level parameters on one path to exercise inheritance/override logic
- Same `x-batchable-actions`

Golden files will NOT match v2 golden output. They will reflect v3-specific output differences (richer docstrings from `oneOf` descriptions, nullable annotations, etc.). The golden files validate that the v3 generator produces correct output for v3 features, not that it matches v2 byte-for-byte.

## Key Design Decisions

1. **Resolve `$ref` at parse time with cycle protection** - downstream code gets normalized dicts, no template changes needed. Visited-set guard prevents infinite loops on circular refs; cache avoids redundant traversal.
2. **`oneOf` reported accurately** - type shown as `"string or object"` in docstrings; if ever required, no type annotation rather than a lie
3. **`nullable` affects type hints** - nullable params get `| None` in the function signature (e.g., `name: str | None`); also noted in docstring. Only v3.0 `nullable: true` style supported (not v3.1 `type: [string, null]`).
4. **New file, not edit of abandoned one** - cleaner modular structure, easier to maintain
5. **Thread `spec` param through all functions** - needed for `$ref` resolution anywhere in the tree
6. **Content-type awareness** - `parse_request_body` handles `application/json`, `multipart/form-data`, and `application/octet-stream`. Unsupported types emit a warning and are skipped (not silently dropped).
7. **Path-level parameter inheritance** - operation params override path-level params on name+in match, per OAS3 spec
8. **Array serialization** - respect `style`/`explode` attributes; default to `form`+`explode:true` per OAS3 spec
9. **Preserve vendor extensions** - carry all `x-` fields through (not just `x-batchable-actions`); downstream templates can access them

## Code Generation Quality Improvements

### Replace `kwargs.update(locals())`

The current v2 generator emits `kwargs.update(locals())` in every method, which is implicit and leaks internal variables. The v3 generator should emit explicit parameter construction:

```python
# Current (v2) - implicit, fragile
def getOrganizationNetworks(self, organizationId, total_pages=1, direction="next", **kwargs):
    kwargs.update(locals())
    # ...

# Target (v3) - explicit, type-safe
def getOrganizationNetworks(self, organizationId, total_pages=1, direction="next", **kwargs):
    params = {k: v for k, v in kwargs.items() if k in query_params}
    body = {k: v for k, v in kwargs.items() if k in body_params}
    # ...
```

Update the Jinja2 templates (`api_function_template.jinja2`, `batch_function_template.jinja2`) to emit the explicit form. This eliminates the `locals()` antipattern and makes generated code compatible with static analysis tools.

### Generate Type Stubs

Produce `.pyi` stub files alongside each generated scope module:

- `meraki/api/organizations.pyi` with full signatures (param names, types from OAS3 schema, return types)
- Enables downstream type checking without runtime cost
- OAS3 schema types map directly: `string` -> `str`, `integer` -> `int`, `boolean` -> `bool`, `array` -> `list`, `object` -> `dict`
- `oneOf` params get `Union[str, dict]`
- `nullable: true` params get `| None`
- Return types: `dict` for single-object, `list[dict]` for arrays, `Generator` for paginated iterators

Add a `--stubs` flag to the generator CLI. Template: `api_stub_template.jinja2`.

---

## Verification

1. Run `python generator/generate_library_oasv3.py` against live v3 spec
2. Diff output against v2-generated library (should be structurally identical, minor description differences from nullable/oneOf annotations)
3. Run golden-file tests: `pytest tests/generator/test_generate_library_oasv3_golden.py`
4. Run existing test suite to confirm no regressions
5. Spot-check generated functions for correct param handling (especially endpoints with requestBody, arrays, enums)
6. **CI drift detection**: automated diff of v2 vs v3 generator output on the live spec (catches divergence between generators over time)
