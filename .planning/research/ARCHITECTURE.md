# Architecture Patterns: OASv3 Code Generator Integration

**Domain:** Code generator for OpenAPI v3 SDK
**Researched:** 2026-04-29

## Recommended Architecture

The v3 generator should follow v2's modular parse-organize-render pipeline but with a separate spec parsing layer that normalizes OASv3 features into the existing template data model.

```
┌─────────────────────────────────────────────────────────────────────┐
│ Main Entry Point (generate_library_oasv3.py)                        │
│ - CLI parsing (reuse v2 pattern)                                    │
│ - Spec fetching (?version=3 query param)                            │
│ - Call generate_library()                                           │
└────────────────────────┬────────────────────────────────────────────┘
                         │
            ┌────────────▼──────────────┐
            │ generate_library()         │
            │ - Scope initialization     │
            │ - Directory creation       │
            │ - Non-generated files      │
            │ - organize_spec() call     │
            └────────────┬───────────────┘
                         │
            ┌────────────▼──────────────────────────┐
            │ OASv3 Parser Layer (NEW)              │
            │ - resolve_ref() with cache & cycles   │
            │ - parse_params_v3() unified function  │
            │   - Path/query from parameters[]      │
            │   - Body from requestBody             │
            │   - Path-level param inheritance      │
            │ - get_schema_from_item() with $ref    │
            │ - parse_request_body() multi-content  │
            └────────────┬───────────────────────────┘
                         │
            ┌────────────▼──────────────────────┐
            │ common.organize_spec() (REUSE)    │
            │ - Path iteration                  │
            │ - Scope assignment via tags       │
            │ - Operations list                 │
            └────────────┬────────────────────────┘
                         │
            ┌────────────▼──────────────────────────────┐
            │ generate_modules() (REUSE with changes)   │
            │ - Template rendering loop                 │
            │ - Call parse_params_v3 instead of v2      │
            │ - Pass spec for $ref resolution           │
            └────────────┬─────────────────────────────┘
                         │
            ┌────────────▼──────────────────────────────┐
            │ Jinja2 Templates (REUSE)                  │
            │ - function_template.jinja2                │
            │ - class_template.jinja2                   │
            │ - batch_function_template.jinja2          │
            │ - async_class_template.jinja2             │
            │ - async_function_template.jinja2          │
            │ - batch_class_template.jinja2             │
            └────────────┬─────────────────────────────┘
                         │
                ┌────────▼────────┐
                │ Output: meraki/ │
                │ - api/          │
                │ - aio/api/      │
                │ - api/batch/    │
                └─────────────────┘
```

### Component Boundaries

| Component | Responsibility | Communicates With |
|-----------|---------------|-------------------|
| **generate_library_oasv3.py** | CLI entry, spec fetch, pipeline orchestration | Parser layer, common.organize_spec, generate_modules |
| **OASv3 Parser Layer** | Normalize v3 spec into v2-compatible param dicts | Raw spec dict, returns normalized params |
| **common.organize_spec()** | Path/scope organization (version-agnostic) | Receives spec paths, returns scopes dict |
| **generate_modules()** | Module generation loop, template rendering | Parser layer for params, Jinja2 for rendering |
| **parse_get/post/delete_params()** | HTTP method-specific logic | Parser layer, returns call_line + param dicts |
| **Jinja2 Templates** | Code generation from normalized data | Template vars, outputs Python code |

## Data Flow

**OASv3 Spec to Generated Code:**

```
1. Fetch OASv3 spec from Meraki API
   https://api.meraki.com/api/v1/openapiSpec?version=3

2. Parse spec structure
   spec = {
     "openapi": "3.0.1",
     "paths": {
       "/networks/{networkId}": {
         "get": {
           "operationId": "getNetwork",
           "parameters": [{"name": "networkId", "in": "path", "schema": {...}}],
           "requestBody": null  # GET has no body
         },
         "put": {
           "operationId": "updateNetwork",
           "parameters": [{"name": "networkId", "in": "path", "schema": {...}}],
           "requestBody": {
             "content": {
               "application/json": {
                 "schema": {
                   "$ref": "#/components/schemas/UpdateNetworkRequest"
                 }
               }
             }
           }
         }
       }
     },
     "components": {
       "schemas": {
         "UpdateNetworkRequest": {
           "type": "object",
           "properties": {
             "name": {"type": "string"},
             "tags": {"type": "array", "items": {"type": "string"}}
           }
         }
       }
     }
   }

3. Initialize scope structure
   scopes = {"networks": {}, "organizations": {}, ...}

4. organize_spec() groups paths by scope
   scopes["networks"]["/networks/{networkId}"] = {
     "get": endpoint_dict,
     "put": endpoint_dict
   }

5. For each endpoint, parse_params_v3() normalizes parameters
   
   Input (OASv3):
   - parameters: [{"name": "networkId", "in": "path", "schema": {"type": "string"}}]
   - requestBody: {"content": {"application/json": {"schema": {...}}}}
   
   Output (normalized for templates):
   {
     "networkId": {
       "required": True,
       "in": "path",
       "type": "string",
       "description": "Network ID"
     },
     "name": {
       "required": False,
       "in": "body",
       "type": "string",
       "description": "Network name"
     },
     "tags": {
       "required": False,
       "in": "body",
       "type": "array",
       "description": "Network tags"
     }
   }

6. return_params() filters by criteria
   parse_params_v3("updateNetwork", params, requestBody, spec, ["required"])
   # Returns only required params for function signature

7. Template renders with normalized data
   function_template.jinja2 receives:
   - operation: "updateNetwork"
   - function_definition: ", networkId: str"
   - path_params: {"networkId": {...}}
   - body_params: {"name": {...}, "tags": {...}}
   - call_line: "return self._session.put(metadata, resource, payload)"

8. Generated code
   def updateNetwork(self, networkId: str, **kwargs):
       kwargs = locals()
       metadata = {"tags": ["networks", "configure"], "operation": "updateNetwork"}
       networkId = urllib.parse.quote(str(networkId), safe="")
       resource = f"/networks/{networkId}"
       body_params = ["name", "tags"]
       payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
       return self._session.put(metadata, resource, payload)
```

**State Management:**

| State | Storage | Lifetime |
|-------|---------|----------|
| OpenAPI spec | `spec` dict in generate_library() | Function scope |
| $ref resolution cache | `_ref_cache` dict in resolve_ref() | Function scope, reset per generate_library() call |
| $ref resolution stack | `_ref_stack` list in resolve_ref() | Call stack (cycle detection) |
| Scopes dict | `scopes` in generate_library() | Function scope |
| Jinja2 environment | `jinja_env` in generate_library() | Function scope |
| Template directory | `template_dir` string | Function scope |

## Integration Points with Existing Code

### NEW Components (v3-specific)

**1. resolve_ref(spec, ref, cache=None, stack=None)**
- **Purpose:** Resolve `$ref` references with cycle detection and caching
- **Location:** generate_library_oasv3.py
- **Dependencies:** None (pure function)
- **Used by:** get_schema_from_item, parse_request_body
- **Signature:**
  ```python
  def resolve_ref(spec: dict, ref: str, cache: dict = None, stack: list = None) -> dict | None:
      """
      Resolve $ref like #/components/schemas/Network to actual schema.
      
      Args:
          spec: Full OpenAPI spec dict
          ref: Reference string starting with #/
          cache: Dict for memoization (mutated in place)
          stack: List for cycle detection (mutated in place)
      
      Returns:
          Resolved schema dict or None if reference invalid/cyclic
      """
  ```

**2. get_schema_from_item(item, spec, cache=None)**
- **Purpose:** Extract schema from parameter/requestBody, resolve $ref if present
- **Location:** generate_library_oasv3.py
- **Dependencies:** resolve_ref()
- **Used by:** parse_params_v3, parse_request_body
- **Signature:**
  ```python
  def get_schema_from_item(item: dict, spec: dict, cache: dict = None) -> dict | None:
      """
      Extract schema from OASv3 item (parameter or content item).
      
      Args:
          item: Dict with "schema" key (e.g., parameter or content item)
          spec: Full spec for $ref resolution
          cache: Shared cache for resolve_ref
      
      Returns:
          Schema dict (inline or resolved from $ref) or None
      """
  ```

**3. parse_request_body(operation, request_body, spec, cache=None)**
- **Purpose:** Parse OASv3 requestBody into params dict with "in": "body"
- **Location:** generate_library_oasv3.py
- **Dependencies:** resolve_ref, get_schema_from_item
- **Used by:** parse_params_v3
- **Signature:**
  ```python
  def parse_request_body(operation: str, request_body: dict, spec: dict, cache: dict = None) -> dict:
      """
      Parse OASv3 requestBody into normalized params dict.
      
      Args:
          operation: Operation ID (for logging)
          request_body: OASv3 requestBody object
          spec: Full spec for $ref resolution
          cache: Shared cache
      
      Returns:
          Dict of {param_name: {required, in, type, description, enum?, items?}}
      
      Notes:
          - Handles application/json (primary), multipart/form-data, application/octet-stream
          - Flattens schema properties into top-level params
          - Sets "in": "body" for all params
      """
  ```

**4. parse_params_v3(operation, parameters, request_body, spec, param_filters=None)**
- **Purpose:** Unified parameter parser for OASv3 (replaces v2's parse_params)
- **Location:** generate_library_oasv3.py
- **Dependencies:** return_params (from common or v2), parse_request_body, get_schema_from_item
- **Used by:** generate_standard_and_async_functions, generate_action_batch_functions
- **Signature:**
  ```python
  def parse_params_v3(
      operation: str,
      parameters: list | None,
      request_body: dict | None,
      spec: dict,
      param_filters: list | None = None
  ) -> dict:
      """
      Parse OASv3 parameters and requestBody into normalized dict.
      
      Args:
          operation: Operation ID
          parameters: List of OASv3 parameter objects (path, query, header)
          request_body: OASv3 requestBody object or None
          spec: Full spec for $ref resolution
          param_filters: List of filters for return_params (e.g., ["required", "path"])
      
      Returns:
          Normalized params dict matching v2 format:
          {
              param_name: {
                  "required": bool,
                  "in": "path" | "query" | "body",
                  "type": "string" | "integer" | "boolean" | "array" | "object",
                  "description": str,
                  "enum": list (optional),
                  "items": dict (optional, for arrays)
              }
          }
      
      Notes:
          - Merges parameters[] and requestBody into single dict
          - Handles path-level parameter inheritance (future enhancement)
          - Passes through return_params for filtering
          - Adds pagination params if perPage detected
      """
  ```

### REUSED Components (from v2 or common.py)

**1. organize_spec(paths, scopes)**
- **Location:** common.py
- **Status:** REUSE AS-IS
- **Why:** Path-to-scope mapping is version-agnostic

**2. return_params(operation, params, param_filters)**
- **Location:** generate_library.py (v2) - MOVE TO common.py
- **Status:** REUSE with extraction
- **Why:** Filtering logic (required, path, query, body, array, enum) is identical for v2 and v3
- **Action:** Extract to common.py, import in both generators

**3. generate_pagination_parameters(operation)**
- **Location:** generate_library.py (v2) - MOVE TO common.py
- **Status:** REUSE with extraction
- **Why:** Pagination is a library feature, not spec-version-specific
- **Action:** Extract to common.py

**4. docs_url(operation)**
- **Location:** generate_library.py (v2) - MOVE TO common.py
- **Status:** REUSE with extraction
- **Why:** Pure transformation of operation ID to documentation URL
- **Action:** Extract to common.py

**5. Jinja2 Templates**
- **Location:** generator/*.jinja2
- **Status:** REUSE AS-IS
- **Why:** Templates consume normalized param dicts; v3 parser produces same format as v2

**6. generate_modules(batchable_actions, jinja_env, scopes, template_dir)**
- **Location:** generate_library.py (v2) - DUPLICATE with modifications
- **Status:** DUPLICATE and modify for v3
- **Why:** Core structure identical, but calls parse_params_v3 instead of parse_params
- **Changes:**
  - Replace `endpoint["parameters"]` with `endpoint.get("parameters")` and `endpoint.get("requestBody")`
  - Replace `parse_params(op, params, filters)` with `parse_params_v3(op, params, request_body, spec, filters)`
  - Thread `spec` through all parsing calls

**7. generate_standard_and_async_functions()**
- **Location:** generate_library.py (v2) - DUPLICATE with modifications
- **Status:** DUPLICATE and modify for v3
- **Changes:** Same as generate_modules

**8. generate_action_batch_functions()**
- **Location:** generate_library.py (v2) - DUPLICATE with modifications
- **Status:** DUPLICATE and modify for v3
- **Changes:** Same as generate_modules

### MODIFIED Components

**parse_get_params, parse_post_and_put_params, parse_delete_params**
- **Status:** REUSE AS-IS (they consume normalized params)
- **Why:** HTTP method logic operates on normalized params dict, not raw spec

## Patterns to Follow

### Pattern 1: $ref Resolution with Cycle Detection
**What:** Recursive reference resolution with memoization and stack-based cycle detection
**When:** Parsing any OASv3 schema that may contain $ref
**Example:**
```python
def resolve_ref(spec, ref, cache=None, stack=None):
    if cache is None:
        cache = {}
    if stack is None:
        stack = []
    
    # Already resolved
    if ref in cache:
        return cache[ref]
    
    # Cycle detected
    if ref in stack:
        return None
    
    # Parse #/components/schemas/Network -> ["components", "schemas", "Network"]
    if not ref.startswith("#/"):
        return None
    parts = ref[2:].split("/")
    
    # Walk the spec
    stack.append(ref)
    result = spec
    for part in parts:
        if isinstance(result, dict) and part in result:
            result = result[part]
        else:
            stack.pop()
            return None
    
    # Cache and return
    cache[ref] = result
    stack.pop()
    return result
```

### Pattern 2: Unified Parameter Parsing
**What:** Single function handles path, query, and body parameters
**When:** Parsing any OASv3 operation
**Example:**
```python
def parse_params_v3(operation, parameters, request_body, spec, param_filters=None):
    all_params = {}
    cache = {}  # Shared across parameters and requestBody
    
    # Parse path/query parameters
    if parameters:
        for p in parameters:
            schema = get_schema_from_item(p, spec, cache)
            # Extract type, description, required from schema
            all_params[p["name"]] = normalize_param(p, schema)
    
    # Parse requestBody
    if request_body:
        body_params = parse_request_body(operation, request_body, spec, cache)
        all_params.update(body_params)
    
    # Add pagination if perPage present
    if "perPage" in all_params:
        all_params.update(generate_pagination_parameters(operation))
    
    # Filter and return
    return return_params(operation, all_params, param_filters)
```

### Pattern 3: Content-Type Aware Body Parsing
**What:** Handle multiple requestBody content types (JSON, multipart, octet-stream)
**When:** Parsing OASv3 requestBody
**Example:**
```python
def parse_request_body(operation, request_body, spec, cache):
    if "content" not in request_body:
        return {}
    
    content = request_body["content"]
    
    # Priority: application/json > multipart/form-data > application/octet-stream
    media_type = None
    if "application/json" in content:
        media_type = content["application/json"]
    elif "multipart/form-data" in content:
        media_type = content["multipart/form-data"]
    elif "application/octet-stream" in content:
        # Binary upload, no schema properties to extract
        return {}
    
    if not media_type:
        return {}
    
    schema = get_schema_from_item(media_type, spec, cache)
    if not schema or "properties" not in schema:
        return {}
    
    # Flatten properties into params
    params = {}
    required_fields = schema.get("required", [])
    for prop_name, prop_schema in schema["properties"].items():
        if "$ref" in prop_schema:
            prop_schema = resolve_ref(spec, prop_schema["$ref"], cache)
        params[prop_name] = {
            "required": prop_name in required_fields,
            "in": "body",
            "type": prop_schema.get("type", "object"),
            "description": prop_schema.get("description", "")
        }
        if "enum" in prop_schema:
            params[prop_name]["enum"] = prop_schema["enum"]
    
    return params
```

### Pattern 4: Path-Level Parameter Inheritance
**What:** Path-level parameters apply to all operations on that path
**When:** Parsing OASv3 paths
**Example:**
```python
# In generate_library, when iterating paths:
for path, path_item in paths.items():
    # OASv3: path-level parameters inherited by all operations
    path_level_params = path_item.get("parameters", [])
    
    for method in ["get", "post", "put", "delete", "patch"]:
        if method not in path_item:
            continue
        
        endpoint = path_item[method]
        
        # Merge path-level and operation-level parameters
        operation_params = endpoint.get("parameters", [])
        # Operation params override path params with same name
        param_names = {p["name"] for p in operation_params}
        inherited = [p for p in path_level_params if p["name"] not in param_names]
        all_parameters = operation_params + inherited
        
        # Now parse with merged parameters
        parsed = parse_params_v3(
            endpoint["operationId"],
            all_parameters,
            endpoint.get("requestBody"),
            spec
        )
```

## Anti-Patterns to Avoid

### Anti-Pattern 1: Monolithic Parser Function
**What:** Single function that handles spec fetching, parsing, organizing, and generation
**Why bad:** Impossible to test in isolation, cannot reuse components, hard to debug
**Instead:** Separate concerns into functions with single responsibilities
**Evidence from abandoned attempt:** generate_library_oasv3.py lines 262-765 is a single function doing everything

### Anti-Pattern 2: Inline $ref Resolution
**What:** Resolving references at template time or in every parsing function separately
**Why bad:** No caching, cycle detection fragile, templates become spec-aware
**Instead:** Resolve all $ref at parse time, cache results, pass normalized dicts to templates
**Example of wrong approach:**
```python
# BAD: Template has to understand $ref
{% if body_params[param].get("$ref") %}
  # Special handling in template
{% endif %}

# GOOD: Parser resolves before template
body_params = {
    "name": {"type": "string", "description": "Network name"}  # Already resolved
}
```

### Anti-Pattern 3: Duplicating return_params Logic
**What:** Reimplementing filter logic (required, path, query, etc.) in v3 parser
**Why bad:** Code duplication, divergence over time, missed edge cases
**Instead:** Extract return_params to common.py, reuse in both generators

### Anti-Pattern 4: Not Threading Spec Through Functions
**What:** Passing partial dicts and losing context needed for $ref resolution
**Why bad:** Cannot resolve references, have to refetch or restructure data
**Instead:** Thread full `spec` dict through all parsing functions, use cache for performance
**Example from abandoned attempt:**
```python
# Lines 196-259: parse_params needs spec for $ref but loses context in nested calls
def parse_params(operation, parameters, request_body, spec, param_filters=None):
    # ...
    for p in parameters:
        schema = get_schema_from_item(p, spec)  # Correct, spec threaded
        # ...
    body_params = parse_request_body(operation, request_body, spec)  # Correct
```

### Anti-Pattern 5: Using locals() for Param Construction
**What:** `kwargs.update(locals())` to capture function arguments
**Why bad:** Captures unintended vars (self, operation, metadata), fails static analysis
**Instead:** Explicit param dict construction or structured capture
**Note:** This is v2 tech debt; v3 is opportunity to fix but not blocking for parity

### Anti-Pattern 6: Assuming Single Content Type
**What:** Only parsing application/json from requestBody
**Why bad:** Meraki API uses multipart/form-data for firmware uploads, octet-stream for binaries
**Instead:** Priority-based content type selection (JSON > multipart > octet-stream)

## Scalability Considerations

| Concern | At 100 operations | At 400+ operations (current) | At 1000+ operations |
|---------|-------------------|------------------------------|---------------------|
| $ref cache | Not needed | Essential (298 batchable actions share schemas) | Critical (memory vs re-parse tradeoff) |
| Template rendering | Sequential OK | Sequential OK (fast with Jinja2) | Consider parallel per scope |
| Spec download | Network OK | Network OK | Consider caching in CI |
| Code formatting | ruff fast | ruff fast (current: <5s) | Consider incremental formatting |

**Current scale:** 298 operations across 17 scopes, v3 spec is ~3.2MB JSON

**Performance targets:**
- Full generation (fetch + parse + render + format): <30s
- Parser layer (parse all operations): <5s
- Template rendering: <10s
- Code formatting: <5s

**Bottlenecks to watch:**
1. $ref resolution without caching (O(n²) with nested schemas)
2. Jinja2 template reloading per function (use jinja_env.from_string with reuse)
3. ruff formatting on individual files (batch invocation faster)

## Build Order

**Phase 1: Parser Foundation**
1. resolve_ref() with tests (cycle detection, caching)
2. get_schema_from_item() with tests
3. parse_request_body() with tests (JSON, multipart, octet-stream)
4. Extract return_params to common.py, update v2 imports

**Phase 2: Unified Parser**
5. parse_params_v3() with tests (path, query, body merging)
6. Path-level parameter inheritance
7. Golden-file test with synthetic v3 fixture

**Phase 3: Generation Integration**
8. Duplicate generate_modules and modify for parse_params_v3 calls
9. Duplicate generate_standard_and_async_functions with spec threading
10. Duplicate generate_action_batch_functions with v3 batch operation detection

**Phase 4: CLI and Entry Point**
11. generate_library_oasv3.py main() with ?version=3 param
12. Integration test with live v3 spec
13. CI drift detection (v2 vs v3 output comparison)

**Dependency order:**
- resolve_ref is foundation (no deps)
- get_schema_from_item depends on resolve_ref
- parse_request_body depends on get_schema_from_item and resolve_ref
- parse_params_v3 depends on parse_request_body and return_params
- Generation functions depend on parse_params_v3

**Testing order:**
- Unit tests for pure functions (resolve_ref, get_schema_from_item)
- Unit tests for parse functions with synthetic schemas
- Golden-file tests with synthetic spec (minimal but representative)
- Integration test with live v3 spec (slow, run in CI)

## Sources

**HIGH confidence:**
- Existing v2 generator code analysis (generate_library.py, common.py)
- Abandoned v3 attempt analysis (generate_library_oasv3.py anti-patterns)
- Jinja2 template structure (function_template.jinja2)
- Test suite structure (test_pure_functions.py, test_generate_library_golden.py)
- PROJECT.md requirements and constraints

**MEDIUM confidence:**
- OASv3 spec structure (from OpenAPI 3.0.1 standard, verified in abandoned code)
- Multi-version generator patterns (inferred from v2 structure, industry practice)

**LOW confidence:**
- openapi-generator internal architecture (docs don't cover implementation)
- Optimal caching strategy (scale assumptions based on current 298 operations)

## Gaps and Assumptions

**Assumptions made:**
1. v3 spec structure matches OpenAPI 3.0.1 standard (verified in abandoned code)
2. Meraki v3 spec uses same x-batchable-actions as v2 (PROJECT.md confirms 298 entries)
3. Templates can consume normalized params without modification (confirmed from template analysis)
4. path-level parameter inheritance exists in v3 spec (standard feature, need to verify in live spec)

**Gaps to address in implementation:**
1. oneOf query param handling (mentioned in PROJECT.md, not in abandoned code)
2. nullable type annotations (mentioned in PROJECT.md, need parser support)
3. components/schemas usage patterns (need to analyze live v3 spec)
4. Exact batch operation detection logic for v3 (v2 uses summary match, v3 may differ)
5. Error handling strategy for malformed $ref or missing schemas
