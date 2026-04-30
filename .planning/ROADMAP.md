# Roadmap: Meraki Dashboard API Python SDK

## Overview

Build a modular OASv3 generator that replaces the abandoned monolithic attempt, following v2's proven parse-organize-render architecture. Parser layer normalizes OASv3 features ($ref, requestBody, oneOf, nullable) into v2-compatible param dicts for template reuse. Five phases deliver foundation parsers, unified parameter handling, module generation, type stubs, and comprehensive testing with CI drift detection.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: Parser Foundation** - Core v3 parsing with $ref resolution, caching, and requestBody handling
- [ ] **Phase 2: Unified Parameter Parser** - Path-level inheritance, nullable, oneOf, and array serialization
- [ ] **Phase 3: Generation Integration** - Module generation, batch actions, and CLI entry point
- [ ] **Phase 4: Type Stubs** - .pyi generation via Jinja2 for static analysis
- [ ] **Phase 5: Testing & CI** - Golden files, v2 vs v3 drift detection, and integration tests

## Phase Details

### Phase 1: Parser Foundation
**Goal**: Core v3 parsing functions normalize $ref resolution and requestBody handling
**Depends on**: Nothing (first phase)
**Requirements**: PARSE-01, PARSE-02
**Success Criteria** (what must be TRUE):
  1. Generator resolves $ref JSON pointers with cycle detection (no stack overflow on circular schemas)
  2. Generator caches resolved $refs (no O(n^2) performance degradation)
  3. Generator parses requestBody for application/json, multipart/form-data, and application/octet-stream
  4. Parser functions return normalized params dict matching v2 format (enables template reuse)
**Plans**: 2 plans
Plans:
- [x] 01-01-PLAN.md: $ref resolution with caching and cycle detection (TDD)
- [x] 01-02-PLAN.md: requestBody parsing for json, multipart, octet-stream (TDD)

### Phase 2: Unified Parameter Parser
**Goal**: Unified parse_params_v3 function merges path, query, and body parameters with OASv3 features
**Depends on**: Phase 1
**Requirements**: PARSE-03, PARSE-04, PARSE-05, PARSE-06
**Success Criteria** (what must be TRUE):
  1. Generator inherits path-level parameters into operations (operation params override on name match)
  2. Generator adds | None to type annotations for nullable: true parameters
  3. Generator documents oneOf query params as "string or object" (not generic "object")
  4. Golden-file test with synthetic v3 fixture validates parser output format
**Plans**: 2 plans
Plans:
- [x] 02-01-PLAN.md: TDD parse_params_v3 with path inheritance, nullable, oneOf, style/explode
- [x] 02-02-PLAN.md: Golden-file snapshot test for output contract validation

### Phase 3: Generation Integration
**Goal**: v3 generator produces sync, async, and batch modules from OASv3 spec
**Depends on**: Phase 2
**Requirements**: GEN-01, GEN-02, GEN-04, GEN-05
**Success Criteria** (what must be TRUE):
  1. Generator produces meraki/api/, meraki/aio/api/, and meraki/api/batch/ modules matching v2 structure
  2. Generated methods use explicit param construction (not kwargs.update(locals()))
  3. Generator handles x-batchable-actions for batch class generation (298 batch endpoints)
  4. CLI accepts same args as v2 and fetches v3 spec with ?version=3 param
**Plans**: 2 plans

### Phase 4: Type Stubs
**Goal**: Generator produces .pyi type stubs via Jinja2 for static analysis
**Depends on**: Phase 3
**Requirements**: GEN-03
**Success Criteria** (what must be TRUE):
  1. Generator creates .pyi files with full method signatures when --stubs flag passed
  2. Package includes py.typed marker for PEP 561 compliance
  3. Type stubs reflect nullable (str | None) and oneOf (Union[str, dict]) semantics
**Plans**: 2 plans

### Phase 5: Testing & CI
**Goal**: Comprehensive test suite and CI drift detection validate v3 generator correctness
**Depends on**: Phase 4
**Requirements**: TEST-01, TEST-02, TEST-03
**Success Criteria** (what must be TRUE):
  1. Synthetic v3 fixture exercises all v3-specific features ($ref with cycles, requestBody, oneOf, nullable, multipart, path-level params)
  2. Golden-file tests validate v3 generator output for sync, async, and batch modules (semantic correctness, not byte-for-byte v2 match)
  3. CI workflow runs semantic diff of v2 vs v3 generator output on live spec (params, types, structure, not text diff)
**Plans**: 2 plans

## Progress

**Execution Order:**
Phases execute in numeric order: 1 > 2 > 3 > 4 > 5

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Parser Foundation | 0/2 | Planning complete | - |
| 2. Unified Parameter Parser | 0/? | Not started | - |
| 3. Generation Integration | 0/? | Not started | - |
| 4. Type Stubs | 0/? | Not started | - |
| 5. Testing & CI | 0/? | Not started | - |
