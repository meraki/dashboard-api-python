# Roadmap: Meraki Dashboard API Python SDK

## Milestones

- ✅ **v1.0 OASv3 Generator** — Phases 1-5 (shipped 2026-04-30)
- 🚧 **v1.1 Deprecation Cycle** — Phases 6-7 (active)

## Phases

<details>
<summary>✅ v1.0 OASv3 Generator (Phases 1-5) — SHIPPED 2026-04-30</summary>

- [x] Phase 1: Parser Foundation (2/2 plans) — completed 2026-04-30
- [x] Phase 2: Unified Parameter Parser (2/2 plans) — completed 2026-04-30
- [x] Phase 3: Generation Integration (2/2 plans) — completed 2026-04-30
- [x] Phase 4: Type Stubs (2/2 plans) — completed 2026-04-30
- [x] Phase 5: Testing & CI (3/3 plans) — completed 2026-04-30

</details>

### v1.1 Deprecation Cycle (Phases 6-7)

- [ ] **Phase 6: Generator Swap** - Rename v2 generator with deprecation warning, promote v3 to default
- [ ] **Phase 7: Legacy Cleanup** - Remove abandoned v3 attempt, update all references

## Phase Details

### Phase 6: Generator Swap
**Goal**: v3 generator becomes default entry point, v2 generator deprecated but retained
**Depends on**: Nothing (first phase of milestone)
**Requirements**: DEP-01, DEP-02
**Success Criteria** (what must be TRUE):
  1. `generate_library.py` imports and runs v3 generator code
  2. `generate_library_oasv2.py` imports and runs v2 generator code with deprecation warning
  3. Running `python generator/generate_library.py` produces SDK using v3 parser
  4. Running `python generator/generate_library_oasv2.py` logs deprecation warning but works
**Plans**: 1 plan

Plans:
- [x] 06-01-PLAN.md — Swap generator files, add deprecation warning, update test imports

### Phase 7: Legacy Cleanup
**Goal**: Abandoned v3 attempt removed, all imports and CI workflows updated
**Depends on**: Phase 6
**Requirements**: DEP-03, DEP-04
**Success Criteria** (what must be TRUE):
  1. `generate_library_oasv3.py` file no longer exists in repository
  2. CI workflows reference `generate_library.py` (not old filenames)
  3. Documentation references `generate_library.py` and `generate_library_oasv2.py` (deprecated)
  4. All internal imports use correct generator filenames
**Plans**: TBD

## Progress

| Phase | Milestone | Plans Complete | Status | Completed |
|-------|-----------|----------------|--------|-----------|
| 1. Parser Foundation | v1.0 | 2/2 | Complete | 2026-04-30 |
| 2. Unified Parameter Parser | v1.0 | 2/2 | Complete | 2026-04-30 |
| 3. Generation Integration | v1.0 | 2/2 | Complete | 2026-04-30 |
| 4. Type Stubs | v1.0 | 2/2 | Complete | 2026-04-30 |
| 5. Testing & CI | v1.0 | 3/3 | Complete | 2026-04-30 |
| 6. Generator Swap | v1.1 | 0/1 | Not started | - |
| 7. Legacy Cleanup | v1.1 | 0/0 | Not started | - |

---
*Roadmap updated: 2026-04-30 (Phase 6 plan created)*
