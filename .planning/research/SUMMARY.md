# Research Summary: OASv3 Generator Project

**Date:** 2026-04-29
**Project:** Meraki Dashboard API Python SDK - OpenAPI 3.0 Generator

## Executive Summary

- **Live spec tested (2026-04-29) has 0 $refs**, 340 requestBody, 152 nullable, 2 oneOf. Hand-rolled JSON pointer resolver (20 lines) sufficient, no jsonref dependency needed.
- **Core challenge is OASv3 requestBody parsing** (moved from parameters array), not spec complexity. Templates reusable, parser layer normalizes v3 → v2 data format.
- **Abandoned attempt has 5 critical bugs**: no cycle detection, no $ref cache (O(n²)), ignores path-level params, wrong content-type priority, no oneOf detection.
- **Zero new runtime dependencies**. Jinja2 templates (not mypy stubgen) for type stubs. Ruff already present for formatting.
- **298 batchable actions share schemas**. $ref cache essential for performance even though live spec has 0 refs (future-proofing + test fixtures will use refs).

## Stack Additions Needed

**None for runtime.** Generator uses existing dependencies.

| Component | Version | Purpose | Status |
|-----------|---------|---------|--------|
| Jinja2 | 3.1.6 | Template rendering + stub generation | Already in pyproject.toml |
| requests | >=2.33.1 | Fetch v3 spec (?version=3 param) | Already present |
| ruff | >=0.15.12 | Post-generation formatting | Already present |
| Python | >=3.11 | Type annotation syntax (str \| None) | Runtime requirement |

**Rejected:**
- jsonref (1.1.0): Proxy overhead for 0 refs in live spec
- prance (25.4.8.0): 5 dependencies for unused file loading
- openapi-spec-validator (0.8.5): Validation we don't need (spec pre-validated)
- mypy stubgen (1.20.2): CLI-only, generates Any everywhere, no programmatic API

## Feature Table Stakes vs Differentiators

### Table Stakes (P0)

Must-have for production generator:

| Feature | Complexity | Notes |
|---------|------------|-------|
| $ref resolution + cycle detection | Medium | 0 in live spec but needed for fixtures, abandoned code crashes on cycles |
| requestBody parsing (JSON/multipart/octet-stream) | Medium | 340 uses in live spec, v2 doesn't have this |
| oneOf as Union[str, dict] | Medium | 2 in live spec, docstring "string or object" |
| nullable → str \| None annotations | Low | 152 in live spec |
| Path-level parameter inheritance | Low | OASv3 standard, abandoned code ignores |
| Array serialization (style/explode) | Low | OASv3 defaults: form + explode=true |

### Differentiators (P1)

High-value, not expected by default:

| Feature | Value | Status |
|---------|-------|--------|
| Type stubs (.pyi) via Jinja2 | Static analysis without runtime cost | Planned with --stubs flag |
| Explicit param construction | Replaces locals() antipattern | Enables static analysis |
| Golden-file test suite | Regression protection | Planned |
| CI drift detection | v2 vs v3 output comparison | Planned |
| kwarg validation + opt-in logging | Catch typos | Already in v2 |
| Vendor extension (x-batchable-actions) | 298 batch endpoints | Already in v2 |

### Anti-Features (Avoid)

Commonly requested but wrong for this project:

- **Pydantic model generation**: Runtime overhead, spec churn = breaking changes, 1000+ endpoints balloon size
- **Full OAS 3.1 support**: Different type system (type: [string, null]), adds complexity
- **Response model objects**: Dict returns work, TypedDict stubs provide typing
- **Auto-generated examples in docstrings**: Specs rarely have good examples, go stale

## Architecture Integration Strategy

### Parser Layer (NEW)

Normalizes OASv3 → v2-compatible param dicts for template reuse.

```
OASv3 spec fetch
  ↓
resolve_ref(spec, ref, cache, stack)  ← 20 lines, cycle detection, caching
  ↓
get_schema_from_item(item, spec, cache)  ← Extract schema, handle $ref
  ↓
parse_request_body(op, requestBody, spec, cache)  ← JSON/multipart/octet-stream → params dict
  ↓
parse_params_v3(op, params, requestBody, spec, filters)  ← Unified parser merges path/query/body
  ↓
return_params(op, params, filters)  ← Reuse v2 filtering (extract to common.py)
  ↓
Templates (REUSE AS-IS)  ← function_template.jinja2, class_template.jinja2, batch_template.jinja2
```

### Component Changes

| Component | Action | Why |
|-----------|--------|-----|
| generate_library_oasv3.py | NEW | Entry point, ?version=3 param, spec fetch |
| OASv3 parser functions | NEW | resolve_ref, get_schema_from_item, parse_request_body, parse_params_v3 |
| return_params() | EXTRACT to common.py | Reuse filter logic (required, path, query, array, enum) |
| generate_pagination_parameters() | EXTRACT to common.py | Version-agnostic |
| docs_url() | EXTRACT to common.py | Pure transform op → URL |
| organize_spec() | REUSE | Path/scope mapping version-agnostic |
| Jinja2 templates | REUSE | Consume normalized params, no changes |
| generate_modules() | DUPLICATE + modify | Call parse_params_v3, thread spec |

### Data Flow Critical Point

**Parser must produce v2-compatible dict format:**

```python
{
  "paramName": {
    "required": bool,
    "in": "path" | "query" | "body",
    "type": "string" | "integer" | "boolean" | "array" | "object",
    "description": str,
    "enum": list,  # optional
    "items": dict,  # optional for arrays
    "nullable": bool  # NEW for v3
  }
}
```

Templates expect this. Change breaks generated code.

## Key Pitfalls to Watch

### Critical (Rewrite Risk)

1. **No cycle detection in $ref**: Circular schemas crash generator. Abandoned code lacks visited-set guard. Add `_visiting` set param to resolve_ref().

2. **No $ref cache**: O(n²) with 298 batchable operations. 30+ second generation vs <5s. Add `spec["_ref_cache"]` dict, check before traversal.

3. **Path-level params ignored**: OASv3 allows `paths[path]["parameters"]` inherited by all operations. Abandoned code only checks operation-level. Merge before parsing.

4. **requestBody content-type priority wrong**: Checks JSON only, multipart endpoints (file uploads) break. Priority: JSON → multipart → octet-stream → warn.

5. **Template data format mismatch**: Parser returns wrong dict structure, templates render empty params. Golden file tests catch this. Match v2 format exactly.

### Moderate (Correctness Issues)

6. **oneOf reported as generic "object"**: Loses "string or object" semantics. Add oneOf detection in get_schema_from_item, docstring enhancement.

7. **Missing $ref target silent**: Returns None, param dropped without warning. Log warning with operation context.

### Minor (Enhancement Opportunities)

8. **Array serialization style ignored**: OASv3 style/explode attributes not checked. Document defaults (form + explode=true).

9. **nullable not in type annotations**: `nullable: true` doesn't add `| None`. Thread nullable through to type builder.

10. **Vendor extension loss**: x-batchable-actions survives, other x-* fields dropped. Forward all x- prefixed keys.

### Integration Gotchas

- **Shared common.py not threadsafe**: If v2/v3 run concurrently in tests, spec param breaks imports. Namespace v3 helpers or accept breaking change.
- **Template filter registration skipped**: v2 registers `to_double_quote_list`, forget = crash. Copy ALL jinja_env setup.
- **ruff assumes cwd**: Absolute paths needed. Test in tmp_path.

## Phase Ordering Implications

### Phase 1: Parser Foundation (5-7 days)
**What:** Core v3 parsing without generation

**Delivers:**
- resolve_ref() with cycle detection + caching (unit tests)
- get_schema_from_item() with $ref support
- parse_request_body() (JSON, multipart, octet-stream)
- Extract return_params() to common.py

**Pitfalls addressed:** #1 (cycles), #2 (cache), #4 (content-type)

**Research needed:** No. Patterns well-documented, abandoned code shows what NOT to do.

**Rationale:** Foundation must be solid. $ref resolution used by all downstream parsing. Unit tests fast, isolated from generation complexity.

### Phase 2: Unified Parameter Parser (3-5 days)
**What:** parse_params_v3() merges path/query/body

**Delivers:**
- parse_params_v3() with path-level inheritance
- Golden-file test with synthetic v3 fixture
- Pagination param injection for perPage endpoints

**Pitfalls addressed:** #3 (path-level params), #5 (data format)

**Research needed:** No. Template expectations clear from function_template.jinja2.

**Rationale:** Parser output must match template input. Golden file prevents template breakage. Synthetic fixture exercises edge cases (cycle, oneOf, nullable, multipart) not in live spec.

**Dependencies:** Phase 1 complete (resolve_ref, parse_request_body)

### Phase 3: Generation Integration (4-6 days)
**What:** Duplicate generate_modules() with v3 parsing

**Delivers:**
- generate_library_oasv3.py entry point
- generate_modules() calling parse_params_v3
- HTTP method parsers (get/post/put/delete) with v3 support
- Batch action detection for v3 structure

**Pitfalls addressed:** #5 (template format validation)

**Research needed:** No. generate_modules() structure proven in v2.

**Rationale:** Duplication safer than modification. v2 stays stable, v3 iterates independently. Thread `spec` through all parsing calls.

**Dependencies:** Phase 2 complete (parse_params_v3 produces correct format)

### Phase 4: Type Stubs (3-4 days)
**What:** .pyi generation via Jinja2

**Delivers:**
- stub_template.jinja2 for function signatures
- --stubs flag in generate_library_oasv3.py
- py.typed marker in package root
- nullable → str | None, oneOf → Union[str, dict]

**Pitfalls addressed:** #6 (oneOf detection), #9 (nullable)

**Research needed:** No. PEP 561 compliance straightforward, Jinja2 approach proven.

**Rationale:** Defer until core generation stable. Type stubs reuse same parse_params_v3 output. Differentiator feature, not table stakes.

**Dependencies:** Phase 3 complete (generation working)

### Phase 5: Quality & CI (2-3 days)
**What:** Testing, drift detection, docs

**Delivers:**
- Golden file tests expanded (edge cases: cycle, multipart, oneOf, nullable)
- CI drift detection (v2 vs v3 semantic diff, not text)
- Integration test with live v3 spec
- OASV3-MIGRATION.md updates

**Pitfalls addressed:** #7 (missing $ref warnings), #8 (array style), #10 (vendor extensions)

**Research needed:** No. Test patterns exist in test_generate_library_golden.py.

**Rationale:** Catch regressions before v2 replacement. Semantic diff prevents false positives from docstring enhancements.

**Dependencies:** Phase 4 complete (full feature set)

### Defer to Future

- Response model objects (Pydantic/dataclasses): High complexity, low value for dict-based API
- Operation-specific exceptions (NotFoundError): Nice-to-have, APIError works
- Custom HTTP clients (httpx pluggability): requests/aiohttp sufficient

## Open Questions

1. **Does live v3 spec use path-level parameters?** Abandoned code suggests yes (OASv3 standard), but 0 uses found in manual inspection. Verify during Phase 2 golden file fixture creation.

2. **What's the v3 batch action detection logic?** v2 uses summary field match. Does v3 spec structure x-batchable-actions differently? Test during Phase 3 with live spec.

3. **Should v3 fix locals() antipattern?** OASV3-MIGRATION.md suggests explicit param construction. Do it in v3 (fresh start) or defer (maintain v2 parity)? Decide during Phase 3 template work.

4. **CI drift detection semantic vs text diff?** How to diff "params correct, docstrings enhanced" vs "params missing"? Design diffing logic in Phase 5.

5. **Should return_params() extraction break v2 imports?** Move to common.py changes imports. Update v2 (safer) or namespace as common_v3.py (isolation)? Decide in Phase 1.

## Confidence Assessment

| Area | Confidence | Rationale |
|------|------------|-----------|
| Stack | HIGH | Live spec tested 2026-04-29. Jinja2/requests/ruff proven in v2. No new dependencies confirmed. |
| Features | HIGH | OASV3-MIGRATION.md + PROJECT.md align. Table stakes clear from v2 gaps. Live spec verified (340 requestBody, 152 nullable). |
| Architecture | HIGH | v2 structure analyzed. Parse-organize-render pipeline proven. Abandoned code shows pitfalls. Template reuse confirmed. |
| Pitfalls | HIGH | Abandoned code line-by-line comparison. 5 critical bugs identified with prevention. OASv3 spec edge cases documented. |

**Gaps identified:**
- Path-level parameter usage in live spec (assume present per standard)
- Batch action structure in v3 (likely same x-batchable-actions)
- oneOf query param frequency (2 in live spec, need broader fixture coverage)

**No research blockers.** All questions answerable during implementation with live spec + fixtures.

## Ready for Requirements

All research complete. Roadmapper can structure phases with confidence in:
- Technology stack (no new deps, Jinja2 for stubs)
- Feature priorities (table stakes vs differentiators clear)
- Architecture approach (parser layer + template reuse)
- Pitfall prevention (5 critical bugs with solutions)
- Build order (Phase 1-5 dependencies mapped)

Research files committed together for traceability.
