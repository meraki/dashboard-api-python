# Requirements: Meraki Dashboard API Python SDK

**Defined:** 2026-04-29
**Core Value:** Developers can interact with every Meraki Dashboard API endpoint through a well-typed, well-documented Python client that stays current with the live API spec.

## v3.1.0 Requirements

Requirements for OASv3 generator milestone. Each maps to roadmap phases.

### Parsing

- [ ] **PARSE-01**: Generator resolves `$ref` JSON pointers with cycle protection and caching
- [ ] **PARSE-02**: Generator parses `requestBody` for application/json, multipart/form-data, and application/octet-stream
- [ ] **PARSE-03**: Generator handles `nullable: true` with `| None` type annotations and docstring notes
- [ ] **PARSE-04**: Generator inherits path-level parameters, operation overrides on name+in match
- [ ] **PARSE-05**: Generator resolves `oneOf` schemas as "string or object" with sub-property documentation
- [ ] **PARSE-06**: Generator respects array param `style`/`explode` attributes (default: form + explode:true)

### Code Generation

- [ ] **GEN-01**: Generator produces sync/async/batch modules matching v2 output structure
- [ ] **GEN-02**: Generated methods use explicit param construction instead of `kwargs.update(locals())`
- [ ] **GEN-03**: Generator produces `.pyi` type stubs with full signatures via `--stubs` flag
- [ ] **GEN-04**: Generator handles `x-batchable-actions` for batch class generation
- [ ] **GEN-05**: CLI accepts same args as v2 (`-h`, `-o`, `-k`, `-v`, `-a`, `-g`) and fetches v3 spec

### Testing & CI

- [ ] **TEST-01**: Synthetic v3 fixture exercises all v3-specific features ($ref, requestBody, oneOf, nullable, multipart, path-level params)
- [ ] **TEST-02**: Golden-file tests validate v3 generator output for sync, async, and batch modules
- [ ] **TEST-03**: CI workflow runs semantic diff of v2 vs v3 generator output on live spec

## Future Requirements

### Deprecation Cycle

- **DEP-01**: Rename v2 generator to `generate_library_oasv2.py` with deprecation warning
- **DEP-02**: Promote v3 generator to `generate_library.py` (new default)
- **DEP-03**: Remove v2 generator after one minor version cycle with no rollbacks

## Out of Scope

| Feature | Reason |
|---------|--------|
| Modifying the v2 generator | Kept for rollback until parity gate passes |
| Changing runtime SDK behavior | rest_session, pagination, etc. are stable |
| OpenAPI 3.1 support | Only 3.0.1 `nullable: true` style, not 3.1 `type: [string, null]` |
| Rewriting Jinja2 templates from scratch | Reuse existing, extend as needed |
| Pydantic model generation | Over-engineering; dict-based params match existing SDK contract |
| Client-side request validation | Adds overhead, API validates server-side |
| OAuth helper generation | Not part of Meraki auth model |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| PARSE-01 | Phase 1 | Pending |
| PARSE-02 | Phase 1 | Pending |
| PARSE-03 | Phase 2 | Pending |
| PARSE-04 | Phase 2 | Pending |
| PARSE-05 | Phase 2 | Pending |
| PARSE-06 | Phase 2 | Pending |
| GEN-01 | Phase 3 | Pending |
| GEN-02 | Phase 3 | Pending |
| GEN-03 | Phase 4 | Pending |
| GEN-04 | Phase 3 | Pending |
| GEN-05 | Phase 3 | Pending |
| TEST-01 | Phase 5 | Pending |
| TEST-02 | Phase 5 | Pending |
| TEST-03 | Phase 5 | Pending |

**Coverage:**
- v3.1.0 requirements: 14 total
- Mapped to phases: 14
- Unmapped: 0

---
*Requirements defined: 2026-04-29*
*Last updated: 2026-04-29 after roadmap creation*
