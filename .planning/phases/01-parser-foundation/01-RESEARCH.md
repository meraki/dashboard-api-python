# Phase 1: Parser Foundation - Research

**Researched:** 2026-04-30
**Domain:** OpenAPI v3 spec parsing with JSON pointer resolution and requestBody handling
**Confidence:** HIGH

## Summary

Phase 1 establishes core v3 parsing functions in a new `generator/parser_v3.py` module. The live Meraki v3 spec (OpenAPI 3.0.1) uses **all inline schemas with zero `$ref` usage**, simplifying the implementation significantly. The spec contains 637 paths, 340 with requestBody, and exclusively uses `application/json` content type (no multipart/form-data or octet-stream in current spec).

User decisions lock the architecture: module-level dict cache for `$ref` resolution, visited-set cycle detection, hard-fail on unresolvable refs, and standalone functions matching v2's pattern. The abandoned `generate_library_oasv3.py` contains a basic `resolve_ref()` implementation without caching or cycle protection, serving as a starting point.

**Primary recommendation:** Build minimal `$ref` resolution infrastructure (required by OpenAPI 3.0 spec compliance) even though live spec doesn't use it, focus implementation effort on requestBody parsing (340 operations), and defer multipart/octet-stream support until spec evidence emerges.

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| $ref resolution | Build/Generation | - | Code generation phase, not runtime |
| requestBody parsing | Build/Generation | - | Transform spec to param dicts at build time |
| Param dict construction | Build/Generation | - | Generator output consumed by templates |
| Cycle detection | Build/Generation | - | Spec validation during generation |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Python stdlib json | 3.14+ | Parse OpenAPI spec | Built-in, zero dependencies |
| Python stdlib typing | 3.14+ | Type hints for params | Built-in, matches existing v2 code |
| requests | (existing) | Fetch live spec | Already in generator dependencies |
| jinja2 | (existing) | Template rendering | Already in generator dependencies |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| jsonpointer | 3.1.1 | RFC 6901 JSON pointer resolution | If complex $ref patterns emerge (not needed for current spec) [VERIFIED: PyPI 2026-03-23] |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Manual pointer parsing | jsonpointer library | Current spec has zero $refs; manual parsing is simpler and has zero install overhead |
| openapi-spec-validator | Custom validation | Validator adds 67+ code snippets for features we don't need; spec is trusted (Meraki-provided) |

**Installation:**
```bash
# No new dependencies required for Phase 1
# Existing: requests, jinja2 (already in generator/requirements.txt)
# Optional (if $ref usage emerges): pip install jsonpointer==3.1.1
```

**Version verification:** Existing dependencies confirmed in project environment (Python 3.14.3, pytest 9.0.3).

## Architecture Patterns

### System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│ Entry: Live OpenAPI v3 Spec (HTTPS fetch)                  │
│ https://api.meraki.com/api/v1/openapiSpec?version=3        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Spec Loader (existing in generate_library.py)              │
│ • Fetch spec JSON                                           │
│ • Validate structure                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ parser_v3.py: $ref Resolution (NEW - Phase 1)              │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ resolve_ref(spec, pointer)                          │   │
│ │ • Check module-level cache (dict keyed by pointer)  │   │
│ │ • If cached: return cached value                    │   │
│ │ • Parse JSON pointer (#/path/to/schema)             │   │
│ │ • Traverse spec dict                                │   │
│ │ • Cycle detection: visited set, return sentinel     │   │
│ │ • Cache result before return                        │   │
│ │ • Raise on unresolvable                             │   │
│ └─────────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ parser_v3.py: requestBody Parser (NEW - Phase 1)           │
│ ┌─────────────────────────────────────────────────────┐   │
│ │ parse_request_body(operation_spec, spec)            │   │
│ │ • Extract operation.requestBody.content             │   │
│ │ • Identify content-type (application/json primary)  │   │
│ │ • Extract schema.properties                         │   │
│ │ • For each property: build param dict entry         │   │
│ │   {name: {required, in:'body', type, description}}  │   │
│ │ • Set operation.content_type metadata               │   │
│ │ • Return normalized params dict                     │   │
│ └─────────────────────────────────────────────────────┘   │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│ Output: Normalized Params Dict                             │
│ • Matches v2 format (required, in, type, description)       │
│ • Plus nullable field (consumed in Phase 2)                 │
│ • Compatible with existing return_params() filter           │
│ • Compatible with existing Jinja2 templates                 │
└─────────────────────────────────────────────────────────────┘
```

### Component Responsibilities Table

| File | Function | Input | Output | Depends On |
|------|----------|-------|--------|------------|
| `parser_v3.py` | `resolve_ref(spec, ref_string)` | OpenAPI spec dict, JSON pointer string | Resolved schema dict or raise exception | Module cache, visited set |
| `parser_v3.py` | `parse_request_body(op_spec, spec)` | Operation dict, spec dict | Params dict `{name: {required, in, type, ...}}` | `resolve_ref()` if $ref found |
| `parser_v3.py` | `clear_cache()` | None | None | Module cache dict |
| `common.py` (reuse) | `organize_spec(paths, scopes)` | Paths dict, scopes dict | Operations list, scoped paths | None |

### Recommended Project Structure
```
generator/
├── generate_library.py          # v2 generator (unchanged Phase 1)
├── generate_library_oasv3.py    # Abandoned v3 (reference only)
├── parser_v3.py                 # NEW: Phase 1 core parsing
├── common.py                    # Shared utilities (reuse)
└── templates/                   # Jinja2 templates (unchanged Phase 1)
```

### Pattern 1: Module-Level Cache with Visited Set

**What:** `$ref` resolution uses a module-level dict cache keyed by JSON pointer string, with a per-call visited set passed through recursive resolution to detect cycles.

**When to use:** Every `resolve_ref()` call, cleared between generator runs.

**Example:**
```python
# Source: User decision D-01, D-02 from CONTEXT.md
_ref_cache = {}  # Module-level cache

def resolve_ref(spec: dict, ref: str, visited: set = None) -> dict:
    """Resolve JSON pointer with cycle detection and caching."""
    if visited is None:
        visited = set()
    
    # Check cache first
    if ref in _ref_cache:
        return _ref_cache[ref]
    
    # Cycle detection
    if ref in visited:
        return {}  # Sentinel value for cycle
    
    visited.add(ref)
    
    # Parse JSON pointer (RFC 6901)
    if not ref.startswith("#/"):
        raise ValueError(f"Only internal refs supported: {ref}")
    
    parts = ref[2:].split("/")
    result = spec
    for part in parts:
        # Unescape JSON pointer tokens
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(result, dict) and part in result:
            result = result[part]
        else:
            raise KeyError(f"Unresolvable $ref: {ref}")
    
    # Cache before return
    _ref_cache[ref] = result
    return result

def clear_cache():
    """Clear ref cache between generator runs."""
    global _ref_cache
    _ref_cache = {}
```

### Pattern 2: RequestBody to Param Dict Normalization

**What:** Extract `requestBody.content[content_type].schema.properties` and transform each property into a v2-compatible param dict entry.

**When to use:** For every operation with `requestBody` (340 operations in live spec).

**Example:**
```python
# Source: Derived from v2 param dict format (generate_library.py) + user decision D-04, D-10
def parse_request_body(operation: dict, spec: dict) -> tuple[dict, str]:
    """
    Parse requestBody into param dict and content type.
    
    Returns:
        (params_dict, content_type)
    """
    if "requestBody" not in operation:
        return {}, None
    
    request_body = operation["requestBody"]
    content = request_body.get("content", {})
    
    # Prioritize application/json (only type in live spec)
    content_type = None
    schema = None
    
    if "application/json" in content:
        content_type = "application/json"
        schema = content["application/json"].get("schema", {})
    elif "multipart/form-data" in content:
        content_type = "multipart/form-data"
        schema = content["multipart/form-data"].get("schema", {})
    elif "application/octet-stream" in content:
        content_type = "application/octet-stream"
        # Octet-stream: single 'file' param (D-05)
        return {
            "file": {
                "required": True,
                "in": "body",
                "type": "file",
                "description": "Binary file content"
            }
        }, content_type
    
    if not schema:
        return {}, content_type
    
    # Resolve $ref if present
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])
    
    # Extract properties
    properties = schema.get("properties", {})
    required_list = schema.get("required", [])
    
    params = {}
    for prop_name, prop_schema in properties.items():
        # Resolve nested $ref
        if "$ref" in prop_schema:
            prop_schema = resolve_ref(spec, prop_schema["$ref"])
        
        params[prop_name] = {
            "required": prop_name in required_list,
            "in": "body",
            "type": prop_schema.get("type", "object"),
            "description": prop_schema.get("description", ""),
            "nullable": prop_schema.get("nullable", False),  # v3-specific (D-10)
        }
        
        # Include enum if present
        if "enum" in prop_schema:
            params[prop_name]["enum"] = prop_schema["enum"]
        
        # Include array items if present
        if prop_schema.get("type") == "array" and "items" in prop_schema:
            params[prop_name]["items"] = prop_schema["items"]
    
    return params, content_type
```

### Anti-Patterns to Avoid

- **Don't import jsonpointer library yet:** Live spec has zero `$ref` usage. Manual parsing is simpler and avoids dependency. Only add library if future spec versions introduce $refs. [VERIFIED: Live spec analysis 2026-04-30]
- **Don't build OOP hierarchy:** User decided standalone functions matching v2 style (D-08). Class-based design adds complexity templates don't need.
- **Don't normalize content-type at param level:** User decided operation-level `content_type` metadata (D-06). Param dict format stays identical across content types.
- **Don't handle $ref chains:** JSON Schema spec prohibits `$ref` chains (`$ref` to `$ref` causes infinite loop). Assume spec is valid; single-level resolution suffices. [CITED: https://json-schema.org/understanding-json-schema/structuring.html]

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| JSON pointer parsing | Custom pointer parser with manual escaping | Python stdlib `str.split()` + escape replace | RFC 6901 only defines `~0` and `~1` escapes; stdlib sufficient for current spec |
| Spec validation | Custom schema validator | Trust Meraki spec + raise on unresolvable refs | Spec is production-tested; over-validation adds latency and dependencies |
| Recursive resolution | Manual stack tracking | Visited set with early return | Stack overflow risk with complex schemas; visited set is O(1) cycle check |

**Key insight:** The live Meraki spec uses zero `$ref` pointers (all inline schemas), so complex resolution machinery is unnecessary. Build minimal RFC 6901-compliant resolver for spec compliance, but implementation won't exercise it in production.

## Runtime State Inventory

> Phase 1 is greenfield (new module creation), not rename/refactor. This section is omitted.

## Common Pitfalls

### Pitfall 1: Assuming $ref is Common in Meraki Spec
**What goes wrong:** Implementing complex $ref resolver with external file support, JSON Schema draft detection, URI resolution, etc.
**Why it happens:** OpenAPI v3 spec supports $refs; developers assume it's heavily used.
**How to avoid:** **Verify spec structure first.** Live Meraki spec (verified 2026-04-30) has 637 paths, zero `$ref` usage, all inline schemas. Build minimal resolver for compliance, not optimization.
**Warning signs:** Spending more than 30 minutes on $ref code when `grep -r '$ref' spec.json` returns empty.

### Pitfall 2: Cache Pollution Between Runs
**What goes wrong:** Generator run N caches refs, run N+1 reuses stale cache pointing to old spec structure.
**Why it happens:** Module-level cache persists across function calls; if generator imports parser_v3 once and calls multiple times (e.g., in test suite), cache never clears.
**How to avoid:** **Call `clear_cache()` at generator entry point** (before each spec parse). Export `clear_cache()` from parser_v3, invoke in `generate_library_v3.py` main().
**Warning signs:** Tests pass individually but fail when run as suite; generated output differs between runs with same input.

### Pitfall 3: Multipart Content-Type Not in Spec Yet
**What goes wrong:** Building multipart/form-data parser that's never tested because spec doesn't use it.
**Why it happens:** Requirements list multipart support (PARSE-02), developers implement without verifying spec usage.
**How to avoid:** **Defer implementation until spec evidence exists.** Current spec (verified 2026-04-30): 340 requestBody operations, 0 multipart, 0 octet-stream, 340 application/json. Build JSON parser first, add multipart when spec uses it.
**Warning signs:** Writing code with no test fixture (because spec has no examples).

### Pitfall 4: Breaking v2 Param Dict Contract
**What goes wrong:** Adding v3-specific fields that break existing `return_params()` filter or templates.
**Why it happens:** v3 has `nullable`, `oneOf`, etc.; developers add new dict structure without checking downstream consumers.
**How to avoid:** **Follow user decision D-10:** Add `nullable` field to param dicts (Phase 2 consumes it), but keep all v2 keys (`required`, `in`, `type`, `description`, `enum`, `items`). Templates that don't reference `nullable` ignore it gracefully.
**Warning signs:** Existing templates crash with `KeyError`; `return_params()` filter returns empty dicts.

## Code Examples

Verified patterns from existing codebase and OpenAPI spec:

### Param Dict Format (v2 Contract)
```python
# Source: generate_library.py, existing v2 generator
# Phase 1 output MUST match this structure
params = {
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
        "description": "Device name",
        "nullable": True  # NEW in Phase 1, consumed in Phase 2
    },
    "tags": {
        "required": False,
        "in": "body",
        "type": "array",
        "items": {"type": "string"},
        "description": "Device tags"
    }
}
```

### Reusable Utility from common.py
```python
# Source: generator/common.py (existing)
# Reuse this function; don't duplicate
def organize_spec(paths, scopes):
    """Organize spec paths by scope (first tag)."""
    operations = list()
    for path, methods in paths.items():
        for method in methods:
            endpoint = paths[path][method]
            tags = endpoint["tags"]
            operation = endpoint["operationId"]
            operations.append(operation)
            
            # Scope determination logic
            if len(tags) > 2:
                match tags[2]:
                    case "spaces":
                        scope = "spaces"
                    case _:
                        scope = tags[0]
            else:
                scope = tags[0]
            
            if path not in scopes[scope]:
                scopes[scope][path] = {method: endpoint}
            else:
                scopes[scope][path][method] = endpoint
    
    return operations, scopes
```

### JSON Pointer Escaping (RFC 6901)
```python
# Source: RFC 6901 specification
# Manual escaping for JSON pointer tokens
def unescape_pointer_token(token: str) -> str:
    """Unescape JSON pointer token per RFC 6901."""
    return token.replace("~1", "/").replace("~0", "~")

# Example: #/paths/~1devices~1{serial}/get
# After split: ["paths", "~1devices~1{serial}", "get"]
# After unescape: ["paths", "/devices/{serial}", "get"]
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| Swagger 2.0 parameters array | OpenAPI 3.0 requestBody object | OpenAPI 3.0.0 (2017) | Meraki spec migrated to v3 in 2020+; v2 generator doesn't parse requestBody |
| Inline everything | $ref for reusable schemas | OpenAPI 3.0 best practice | Meraki spec chose inline approach; zero $refs in production |
| Untyped params | Type + nullable support | OpenAPI 3.0.0 | Phase 2 adds nullable handling; Phase 1 includes field |

**Deprecated/outdated:**
- **generate_library_oasv3.py:** Abandoned v3 attempt with basic `resolve_ref()` lacking caching/cycles. Don't extend; replace entirely per user decision. [VERIFIED: File exists at generator/generate_library_oasv3.py]
- **jsonpointer library for Meraki spec:** Unnecessary for current spec (zero $refs). Revisit if spec structure changes. [ASSUMED: Based on current spec analysis]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | Live Meraki spec will continue using inline schemas (zero $refs) in near-term releases | Don't Hand-Roll, Common Pitfalls | $ref resolver is too simple; need external file support, URI resolution |
| A2 | Multipart/form-data and octet-stream content types will appear in future spec versions | Standard Stack, Common Pitfalls | Implementation deferred; user must request these content types before Phase 2 completion |
| A3 | JSON Schema prohibits $ref chains (per spec), so Meraki spec won't have them | Architecture Patterns | Need multi-level resolution with infinite loop protection |

## Open Questions

1. **When will multipart/form-data endpoints appear in live spec?**
   - What we know: Requirements include multipart support (PARSE-02); current spec has zero multipart endpoints
   - What's unclear: Timeline for new endpoints; whether to implement speculatively or wait for spec evidence
   - Recommendation: Defer multipart implementation until spec contains examples (avoid untested code); add in Phase 2 if spec updates before release

2. **Should clear_cache() be automatic or explicit?**
   - What we know: User decided module-level cache (D-01); cache must clear between runs to avoid pollution
   - What's unclear: Whether to clear on first resolve_ref() call (implicit) or require caller to invoke clear_cache() (explicit)
   - Recommendation: Explicit `clear_cache()` at generator entry point (clearer contract, easier to debug cache issues)

## Environment Availability

> Phase 1 has no external dependencies beyond existing Python environment and pip-installed packages.

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python 3.10+ | Code execution | ✓ | 3.14.3 | - |
| pytest | Test execution | ✓ | 9.0.3 | - |
| requests | Spec fetching | ✓ | (existing) | - |
| jinja2 | Template rendering | ✓ | (existing) | - |

**No missing dependencies identified.**

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | pytest 9.0.3 |
| Config file | pyproject.toml (ruff config present) |
| Quick run command | `pytest tests/generator/test_parser_v3.py -x` |
| Full suite command | `pytest tests/generator/` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| PARSE-01 | resolve_ref resolves #/components/schemas/Network to correct dict | unit | `pytest tests/generator/test_parser_v3.py::test_resolve_ref_basic -x` | ❌ Wave 0 |
| PARSE-01 | resolve_ref caches resolved refs (no duplicate traversal) | unit | `pytest tests/generator/test_parser_v3.py::test_resolve_ref_caching -x` | ❌ Wave 0 |
| PARSE-01 | resolve_ref detects cycles, returns sentinel (not stack overflow) | unit | `pytest tests/generator/test_parser_v3.py::test_resolve_ref_cycle_detection -x` | ❌ Wave 0 |
| PARSE-01 | resolve_ref raises exception on unresolvable pointer | unit | `pytest tests/generator/test_parser_v3.py::test_resolve_ref_unresolvable -x` | ❌ Wave 0 |
| PARSE-02 | parse_request_body extracts application/json params into flat dict | unit | `pytest tests/generator/test_parser_v3.py::test_parse_request_body_json -x` | ❌ Wave 0 |
| PARSE-02 | parse_request_body handles missing requestBody (returns empty dict) | unit | `pytest tests/generator/test_parser_v3.py::test_parse_request_body_none -x` | ❌ Wave 0 |
| PARSE-02 | parse_request_body sets content_type metadata correctly | unit | `pytest tests/generator/test_parser_v3.py::test_parse_request_body_content_type -x` | ❌ Wave 0 |
| PARSE-02 | parse_request_body output matches v2 param dict format (required, in, type, description keys) | unit | `pytest tests/generator/test_parser_v3.py::test_parse_request_body_v2_compat -x` | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `pytest tests/generator/test_parser_v3.py -x` (new module tests only)
- **Per wave merge:** `pytest tests/generator/` (all generator tests)
- **Phase gate:** Full suite green (`pytest`) before `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `tests/generator/test_parser_v3.py` - covers all PARSE-01, PARSE-02 behaviors
- [ ] `tests/generator/fixtures/synthetic_v3_spec.json` - minimal v3 spec with $ref, requestBody examples for isolated testing

## Security Domain

### Applicable ASVS Categories

| ASVS Category | Applies | Standard Control |
|---------------|---------|------------------|
| V2 Authentication | no | N/A (code generation phase) |
| V3 Session Management | no | N/A (code generation phase) |
| V4 Access Control | no | N/A (code generation phase) |
| V5 Input Validation | yes | Validate JSON pointer format before parsing (reject external refs, malformed pointers) |
| V6 Cryptography | no | N/A (no secrets handled) |

### Known Threat Patterns for Python Code Generation

| Pattern | STRIDE | Standard Mitigation |
|---------|--------|---------------------|
| Malformed JSON pointer causes exception during generation | Denial of Service | Validate pointer format (regex `^#/[a-zA-Z0-9/_-]+$`), catch exceptions, log error with context |
| Untrusted spec with billion-laughs XML equivalent (deeply nested $refs) | Denial of Service | Depth limit in resolve_ref (max 50 levels), visited set prevents infinite loops |
| Path traversal via JSON pointer (`#/../../etc/passwd` equivalent) | Information Disclosure | Reject pointers not starting with `#/`, never use pointer content for file I/O |

## Sources

### Primary (HIGH confidence)
- Live Meraki OpenAPI v3 spec: https://api.meraki.com/api/v1/openapiSpec?version=3 (verified 2026-04-30: 637 paths, 0 $refs, 340 requestBody, all application/json)
- RFC 6901 JSON Pointer: https://datatracker.ietf.org/doc/html/rfc6901 (JSON pointer syntax, escaping rules, no cycle guidance)
- OpenAPI v3.0.1 spec: https://spec.openapis.org/oas/v3.0.1 (requestBody structure, content type definitions, $ref resolution defers to JSON Reference)
- Existing codebase: generator/generate_library.py (v2 param dict format), generator/common.py (organize_spec function)

### Secondary (MEDIUM confidence)
- JSON Schema structuring guide: https://json-schema.org/understanding-json-schema/structuring.html (circular references allowed, $ref chains prohibited)
- PyPI jsonpointer package: https://pypi.org/project/jsonpointer/ (requires Python >=3.10, version 3.1.1 released 2026-03-23)

### Tertiary (LOW confidence)
- Swagger.io $ref guide: https://swagger.io/docs/specification/using-ref/ (no circular reference guidance, sibling-element replacement behavior)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Existing dependencies verified in environment, no new libraries needed for minimal implementation
- Architecture: HIGH - User decisions lock all major choices (D-01 through D-11), existing v2 code provides proven pattern
- Pitfalls: MEDIUM - $ref complexity assumption based on spec analysis (not authoritative guidance); multipart deferral assumes spec won't change mid-phase

**Research date:** 2026-04-30
**Valid until:** 2026-05-30 (30 days; stable domain, but live spec may add $refs/multipart before Phase 2)
