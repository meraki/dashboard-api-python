# Technology Stack: OASv3 Code Generator

**Domain:** Python code generation from OpenAPI 3.0.1 specs
**Researched:** 2026-04-29
**Overall confidence:** HIGH

## Executive Summary

The OASv3 generator requires minimal new dependencies. The live Meraki spec (tested 2026-04-29) uses requestBody, nullable, and oneOf but has ZERO $refs and no components/schemas, so complex dereferencing libraries are unnecessary. Hand-rolled JSON pointer traversal (already present in abandoned generator) suffices for future-proofing. Type stub generation should use Jinja2 templates (consistency with existing generator) rather than external tools.

## Core Technologies

All existing runtime dependencies remain unchanged. Generator adds one dependency.

| Technology | Version | Purpose | Why |
|------------|---------|---------|-----|
| Python | >=3.11 | Runtime requirement | Already specified in pyproject.toml |
| Jinja2 | ==3.1.6 | Template rendering | Already used for code generation, pinned in `dependency-groups.generator` |
| requests | >=2.33.1,<3 | Fetching OpenAPI spec | Already used in v2 generator |
| ruff | >=0.15.12 | Code formatting | Already used for post-generation formatting |

**No new core dependencies required.**

## Supporting Libraries

### For $ref Resolution: NONE

**Decision:** Hand-roll JSON pointer traversal (port from abandoned `generate_library_oasv3.py`).

**Rationale:**
- Live Meraki v3 spec has **0 $refs** (verified 2026-04-29)
- Simple `#/components/schemas/X` pointer walking: 15 lines of code
- No external URLs, no file loading, no complex edge cases
- Cycle detection: visited set, 5 lines
- Libraries like `jsonref` (1.1.0), `jsonpointer` (3.1.1), `prance` (25.4.8.0) are overkill

**If future specs have $refs:**
- `jsonpointer` (3.1.1, MIT): RFC 6901 compliant, production-stable, Python 3.10+
- Fallback: current hand-rolled resolver handles simple cases fine

### For OpenAPI Parsing: NONE

**Decision:** Direct dict traversal of parsed JSON.

**Rationale:**
- `openapi-spec-validator` (0.8.5): Validates specs, doesn't help parsing
- `openapi-core`: Request/response validation, not generation
- `prance` (25.4.8.0): Parser + validator, but adds dependency for features we don't need (external file refs, validation backends)
- Meraki spec is pre-validated (published by API team), direct access simpler

### For Type Stub Generation: Jinja2 Templates

**Decision:** Use existing Jinja2 template approach, not `mypy stubgen`.

**Rationale:**
- `mypy stubgen` (1.20.2): CLI-only, generates drafts with `Any` types, requires manual refinement
- Jinja2 templates give precise control over generated stubs with OAS types → Python types mapping
- Consistency with existing generator architecture
- Pattern already proven in `function_template.jinja2`

**Template approach:**
```python
# api_stub_template.jinja2 generates:
def getOrganization(self, organizationId: str) -> dict: ...
def updateOrganization(self, organizationId: str, **kwargs: Any) -> dict: ...
```

**PEP 561 compliance:**
- Add `py.typed` marker file to package root (already present per grep results)
- `.pyi` files alongside `.py` modules (e.g., `meraki/api/organizations.pyi`)

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| $ref resolution | Hand-rolled | `jsonref` 1.1.0 | Live spec has 0 $refs. Hand-rolled is 20 lines including cycle detection. Library is 3 files + proxy overhead for unused features. |
| $ref resolution | Hand-rolled | `prance` 25.4.8.0 | Parser includes validation backends, external file handling, URI resolution. Adds 5 dependencies for features not used. Documentation says cycle detection "not mentioned." |
| OpenAPI parsing | Direct dict access | `openapi-spec-validator` 0.8.5 | Validates specs, doesn't simplify parsing. Adds dependency for unused validation (Meraki spec is pre-validated). |
| OpenAPI parsing | Direct dict access | `openapi-core` | Request/response validation library, not a spec parser. Wrong tool for code generation. |
| Type stubs | Jinja2 templates | `mypy stubgen` 1.20.2 | CLI-only, generates `Any` everywhere, requires manual fixes. No programmatic API. Template approach gives full type precision from OAS types. |
| Type stubs | Jinja2 templates | `stubgen` package | PyPI page failed to load (2026-04-29). Mypy's stubgen is CLI-only per official docs. |

## What NOT to Use

### jsonschema (4.26.0)
**Why:** JSON Schema validator, not OpenAPI parser. Does NOT provide OpenAPI-specific $ref resolution. Adds validation overhead for features not needed in code generation.

### openapi-python-client (0.28.3)
**Why:** Full client generator, not a library. Generates entire SDK with opinionated structure. We need selective parsing for our existing architecture, not a competing generator.

### jsonref (1.1.0)
**Why:** Proxy-based lazy evaluation is clever but unnecessary. Live spec has 0 $refs. If future specs have refs, they're simple `#/components/schemas/X` pointers, not recursive or external. Hand-rolled resolver is clearer and avoids proxy overhead.

## Integration with Existing Generator

The v2 generator uses:
- `common.organize_spec()` - organizes paths by scope tags
- Jinja2 templates: `class_template.jinja2`, `function_template.jinja2`, `batch_function_template.jinja2`
- Jinja2 filter: `to_double_quote_list` for JSON arrays
- `ruff` for post-generation formatting

**v3 generator additions:**
- New `resolve_ref()` function (port from abandoned oasv3, already exists)
- New `parse_request_body()` function for OAS3 requestBody
- Thread `spec` dict through all parse functions
- New template: `stub_template.jinja2` for `.pyi` generation

**No changes to:**
- `common.py`
- Existing templates (reuse as-is)
- Runtime SDK (`rest_session.py`, pagination logic, etc.)

## Installation

No changes to runtime dependencies. Generator dependencies already in `pyproject.toml`:

```toml
[dependency-groups]
generator = ["jinja2==3.1.6"]
```

For type stub generation, add `py.typed` marker if not present:

```bash
echo "" > meraki/py.typed
```

## Live Spec Verification (2026-04-29)

Tested against `https://api.meraki.com/api/v1/openapiSpec?version=3`:

| Feature | Count | Impact |
|---------|-------|--------|
| `openapi` | 3.0.1 | Target version confirmed |
| `$ref` | 0 | No dereferencing needed for live spec |
| `components/schemas` | 0 | No reusable schemas |
| `oneOf` | 2 | Need oneOf type handling |
| `nullable` | 152 | Need nullable annotation |
| `requestBody` | 340 | Need requestBody parser |
| `x-batchable-actions` | 298 | Existing batch handling reusable |

**Implication:** The project requirements list `$ref` resolution as a feature, but the live spec doesn't use it. This suggests it's either:
1. Future-proofing for anticipated spec changes
2. Testing requirement (synthetic fixtures may include $refs)
3. Mistaken assumption from OAS3 spec review

**Recommendation:** Implement simple hand-rolled resolver (20 lines) for completeness, but flag in research that it's not exercised by production spec.

## Sources

**HIGH confidence:**
- PyPI (official): openapi-spec-validator 0.8.5, prance 25.4.8.0, jsonschema 4.26.0, jsonref 1.1.0, jsonpointer 3.1.1, mypy 1.20.2, openapi-python-client 0.28.3
- Live Meraki spec verification (2026-04-29): 0 $refs, 340 requestBody, 152 nullable, 2 oneOf
- PEP 561: Type stub distribution standards (py.typed marker, .pyi files)
- Existing codebase: pyproject.toml dependency groups, generate_library.py patterns, abandoned generate_library_oasv3.py resolve_ref()

**MEDIUM confidence:**
- Swagger.io docs: $ref resolution rules, edge cases (escape chars, sibling elements ignored)
- OpenAPI 3.0.3 spec: $ref processing, JSON Reference standard
- mypy docs: stubgen CLI-only, generates draft stubs

**LOW confidence:**
- None (all critical findings verified with authoritative sources)
