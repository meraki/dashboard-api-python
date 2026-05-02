# Roadmap: Meraki Dashboard API Python SDK

## Milestones

- ✅ **v1.0 OASv3 Generator** (Phases 1-5, shipped 2026-04-30)
- ✅ **v1.1 Deprecation Cycle** (Phases 6-7, completed)
- 🚧 **v4.0 HTTPX Migration** (Phases 8-13, active)

## Phases

<details>
<summary>✅ v1.0 OASv3 Generator (Phases 1-5) — SHIPPED 2026-04-30</summary>

- [x] Phase 1: Parser Foundation (2/2 plans) — completed 2026-04-30
- [x] Phase 2: Unified Parameter Parser (2/2 plans) — completed 2026-04-30
- [x] Phase 3: Generation Integration (2/2 plans) — completed 2026-04-30
- [x] Phase 4: Type Stubs (2/2 plans) — completed 2026-04-30
- [x] Phase 5: Testing & CI (3/3 plans) — completed 2026-04-30

</details>

<details>
<summary>✅ v1.1 Deprecation Cycle (Phases 6-7) — COMPLETED</summary>

- [x] **Phase 6: Generator Swap** - Rename v2 generator with deprecation warning, promote v3 to default
- [x] **Phase 7: Legacy Cleanup** - Remove abandoned v3 attempt, update all references

</details>

### v4.0 HTTPX Migration (Phases 8-13)

- [ ] **Phase 8: Integration Baseline** - Capture passing integration tests before any HTTP changes
- [ ] **Phase 9: Foundation** - Library-agnostic param encoding and property-based tests
- [ ] **Phase 10: Session Refactor** - Shared base class with decomposed, type-annotated logic
- [ ] **Phase 11: HTTP Backend Migration** - Replace requests/aiohttp with httpx.Client/AsyncClient
- [ ] **Phase 12: Error Handling Deprecation** - Unify exception classes with backwards compatibility
- [ ] **Phase 13: Test Infrastructure** - Update test mocks and validate regression gate

## Phase Details

### Phase 8: Integration Baseline
**Goal**: Record passing integration test state before any HTTP changes
**Depends on**: Nothing (first phase of milestone)
**Requirements**: TEST-01
**Success Criteria** (what must be TRUE):
  1. All integration tests run against Meraki sandbox
  2. Current pass/fail state documented (regression gate reference)
  3. Endpoints exercised by tests are listed
**Plans**: 1 plan
Plans:
- [ ] 08-01-PLAN.md — Install pytest-json-report, fix conftest, capture baseline report

### Phase 9: Foundation
**Goal**: Pure functions for param encoding replace monkey-patched requests internals
**Depends on**: Phase 8
**Requirements**: HTTP-04, QUAL-03
**Success Criteria** (what must be TRUE):
  1. `encode_meraki_params()` function produces query strings matching current behavior
  2. Array-of-objects encoding roundtrips correctly in property-based tests
  3. Function uses only stdlib (urllib.parse), no requests dependency
**Plans**: TBD

### Phase 10: Session Refactor
**Goal**: Shared session base class extracts duplicated logic from sync/async implementations
**Depends on**: Phase 9
**Requirements**: HTTP-03, QUAL-01, QUAL-02
**Success Criteria** (what must be TRUE):
  1. Base class holds config, headers, URL resolution, retry decision logic
  2. Request methods decomposed to complexity <10 each
  3. Session layer fully type-annotated with httpx types
  4. Both sync and async sessions inherit from base
**Plans**: TBD

### Phase 11: HTTP Backend Migration
**Goal**: SDK uses httpx.Client and httpx.AsyncClient for all HTTP requests
**Depends on**: Phase 10
**Requirements**: HTTP-01, HTTP-02, ERR-01, ERR-03, DEP-01, DEP-03
**Success Criteria** (what must be TRUE):
  1. Sync session uses httpx.Client (not requests.Session)
  2. Async session uses httpx.AsyncClient (not aiohttp.ClientSession)
  3. APIError uses httpx.Response attributes (status_code, reason_phrase)
  4. Typed exception handling catches httpx.HTTPError (not bare except)
  5. Dependencies updated: httpx>=0.28,<1 replaces requests and aiohttp
  6. requests_proxy param still works (passes through as proxy=)
**Plans**: TBD

### Phase 12: Error Handling Deprecation
**Goal**: Unified exception handling with backwards-compatible AsyncAPIError
**Depends on**: Phase 11
**Requirements**: ERR-02
**Success Criteria** (what must be TRUE):
  1. AsyncAPIError exists as subclass of APIError
  2. Deprecation warning fires when AsyncAPIError instantiated
  3. Old 3-arg signature still works (message param)
  4. Documentation recommends catching APIError for both sync and async
**Plans**: TBD

### Phase 13: Test Infrastructure
**Goal**: All tests mock httpx responses and validate identical behavior
**Depends on**: Phase 12
**Requirements**: DEP-02, TEST-02, TEST-03, TEST-04
**Success Criteria** (what must be TRUE):
  1. respx library replaces responses in dev dependencies
  2. Unit tests mock httpx.Response (not requests/aiohttp responses)
  3. Integration tests pass with same pass/fail state as Phase 8 baseline
  4. Performance benchmark compares requests/aiohttp vs httpx (documented)
**Plans**: TBD

## Progress

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Parser Foundation | v1.0 | 2/2 | Complete | 2026-04-30 |
| 2. Unified Parameter Parser | v1.0 | 2/2 | Complete | 2026-04-30 |
| 3. Generation Integration | v1.0 | 2/2 | Complete | 2026-04-30 |
| 4. Type Stubs | v1.0 | 2/2 | Complete | 2026-04-30 |
| 5. Testing & CI | v1.0 | 3/3 | Complete | 2026-04-30 |
| 6. Generator Swap | v1.1 | 1/1 | Complete | 2026-04-30 |
| 7. Legacy Cleanup | v1.1 | 0/0 | Complete | 2026-04-30 |
| 8. Integration Baseline | v4.0 | 0/1 | Planning | - |
| 9. Foundation | v4.0 | 0/0 | Not started | - |
| 10. Session Refactor | v4.0 | 0/0 | Not started | - |
| 11. HTTP Backend Migration | v4.0 | 0/0 | Not started | - |
| 12. Error Handling Deprecation | v4.0 | 0/0 | Not started | - |
| 13. Test Infrastructure | v4.0 | 0/0 | Not started | - |

---
*Roadmap updated: 2026-05-01 (Phase 8 planned: 1 plan)*
