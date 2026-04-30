# Requirements: Meraki Dashboard API Python SDK

**Defined:** 2026-04-30
**Core Value:** Developers can interact with every Meraki Dashboard API endpoint through a well-typed, well-documented Python client that stays current with the live API spec.

## v1.1 Requirements

Requirements for Deprecation Cycle milestone. Promotes v3 generator to default, removes legacy code.

### Deprecation

- [ ] **DEP-01**: Rename v2 generator to `generate_library_oasv2.py` with deprecation warning on import
- [ ] **DEP-02**: Promote v3 generator to `generate_library.py` (new default entry point)
- [ ] **DEP-03**: Remove abandoned `generate_library_oasv3.py` (dead code cleanup)
- [ ] **DEP-04**: Update all imports, CI workflows, and documentation referencing old filenames

## Future Requirements

None planned beyond this milestone.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Changing runtime SDK behavior | rest_session, pagination, etc. are stable |
| OpenAPI 3.1 support | Only 3.0.1 style supported |
| Rewriting Jinja2 templates | Reuse existing, extend as needed |
| Removing v2 generator immediately | One version cycle buffer required |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| DEP-01 | Phase 6 | Pending |
| DEP-02 | Phase 6 | Pending |
| DEP-03 | Phase 7 | Pending |
| DEP-04 | Phase 7 | Pending |

**Coverage:**
- v1.1 requirements: 4 total
- Mapped to phases: 4
- Unmapped: 0

---
*Requirements updated: 2026-04-30 (traceability mapped to phases 6-7)*
