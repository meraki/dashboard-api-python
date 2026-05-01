# Requirements: Meraki Dashboard API Python SDK

**Defined:** 2026-05-01
**Core Value:** Developers can interact with every Meraki Dashboard API endpoint through a well-typed, well-documented Python client that stays current with the live API spec.

## v4.0 Requirements

Requirements for HTTPX Migration milestone. Replaces dual HTTP backends with unified httpx.

### Infrastructure

- [ ] **HTTP-01**: SDK uses httpx.Client for all sync HTTP requests
- [ ] **HTTP-02**: SDK uses httpx.AsyncClient for all async HTTP requests
- [ ] **HTTP-03**: Shared session base class holds config, headers, URL resolution, retry logic
- [ ] **HTTP-04**: Param encoding uses pure urllib.parse function (no monkey-patch)

### Error Handling

- [ ] **ERR-01**: APIError uses httpx.Response attributes (status_code, reason_phrase)
- [ ] **ERR-02**: AsyncAPIError deprecated as subclass of APIError with compat __init__
- [ ] **ERR-03**: Typed exception handling replaces bare except (httpx.HTTPError)

### Dependencies

- [ ] **DEP-01**: httpx>=0.28,<1 replaces requests and aiohttp in dependencies
- [ ] **DEP-02**: respx replaces responses library in dev dependencies
- [ ] **DEP-03**: requests_proxy param still works (passes through as proxy=)

### Code Quality

- [ ] **QUAL-01**: Request logic decomposed into methods under complexity 10
- [ ] **QUAL-02**: Session base class and I/O layers fully type-annotated
- [ ] **QUAL-03**: Property-based tests validate param encoding roundtrip

### Testing

- [ ] **TEST-01**: Integration test baseline captured before any HTTP changes
- [ ] **TEST-02**: Unit tests mock httpx.Response (not requests/aiohttp)
- [ ] **TEST-03**: Integration tests pass after migration (regression gate)
- [ ] **TEST-04**: Before/after performance benchmark comparing requests/aiohttp vs httpx

## Future Requirements

None planned beyond this milestone.

## Out of Scope

| Feature | Reason |
| ------- | ------ |
| Adaptive retry strategy | App logic, not library choice |
| Pagination memory buffering | Iterator pattern already exists |
| API key exposure risk | Logging concern, unrelated to transport |
| Request cancellation / OpenTelemetry | httpx has primitives but wiring is separate scope |
| Generator scripts' requests usage | Dev-only, optional future work |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| HTTP-01 | TBD | Pending |
| HTTP-02 | TBD | Pending |
| HTTP-03 | TBD | Pending |
| HTTP-04 | TBD | Pending |
| ERR-01 | TBD | Pending |
| ERR-02 | TBD | Pending |
| ERR-03 | TBD | Pending |
| DEP-01 | TBD | Pending |
| DEP-02 | TBD | Pending |
| DEP-03 | TBD | Pending |
| QUAL-01 | TBD | Pending |
| QUAL-02 | TBD | Pending |
| QUAL-03 | TBD | Pending |
| TEST-01 | TBD | Pending |
| TEST-02 | TBD | Pending |
| TEST-03 | TBD | Pending |
| TEST-04 | TBD | Pending |

**Coverage:**
- v4.0 requirements: 17 total
- Mapped to phases: 0 (pending roadmap)
- Unmapped: 17

---
*Requirements defined: 2026-05-01*
