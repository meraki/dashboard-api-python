---
phase: 10
slug: session-refactor
status: verified
threats_open: 0
asvs_level: 1
created: 2026-05-04
---

# Phase 10 — Security

> Per-phase security contract: threat register, accepted risks, and audit trail.

---

## Trust Boundaries

| Boundary | Description | Data Crossing |
|----------|-------------|---------------|
| SDK client -> Meraki API | All HTTP requests cross network boundary | API key, request/response payloads |
| User input -> URL resolution | base_url and endpoint strings from caller | URL strings |
| Response headers -> retry logic | Retry-After header from server influences sleep duration | Integer wait time |
| Caller -> session constructor | Config values (proxy, cert path) from user code | File paths, proxy URLs |

---

## Threat Register

| Threat ID | Category | Component | Disposition | Mitigation | Status |
|-----------|----------|-----------|-------------|------------|--------|
| T-10-01 | Tampering | validate_base_url | mitigate | Domain allowlist in common.py (meraki.com, meraki.ca, meraki.cn, meraki.in, gov-meraki.com); non-matching URLs treated as relative paths appended to base_url | closed |
| T-10-02 | Information Disclosure | API key in logs | mitigate | base.py:103 masks key to `"*" * 36 + key[-4:]` in _parameters dict; full key only in Authorization header (required for auth) | closed |
| T-10-03 | Denial of Service | Retry-After header injection | accept | Server-provided value capped by nginx_429_retry_wait_time config; SDK is client-side so attacker would need MITM position | closed |
| T-10-04 | Tampering | TLS bypass via certificate_path | mitigate | sync.py sets `verify=certificate_path` (custom CA bundle, never False); async_.py uses `ssl.create_default_context()` + `load_verify_locations()` | closed |
| T-10-05 | Spoofing | _send_request proxy passthrough | mitigate | sync.py:60 only applies proxy to HTTPS scheme (`{"https": proxy}`); async uses aiohttp `proxy` kwarg which validates URL scheme | closed |
| T-10-06 | Information Disclosure | aiohttp session headers | mitigate | Headers built via _build_headers; API key only in Authorization header (required); logging uses masked _parameters dict | closed |
| T-10-07 | Elevation of Privilege | SSL context in async session | mitigate | async_.py:51 uses `ssl.create_default_context()` (system CA trust) + `load_verify_locations()` for custom CAs; never sets verify=False or disables hostname checking | closed |

---

## Accepted Risks Log

| Risk ID | Threat Ref | Rationale | Accepted By | Date |
|---------|------------|-----------|-------------|------|
| AR-10-01 | T-10-03 | Retry-After is server-controlled; attacker needs MITM. Capped by config. Client-side SDK has no authority to reject valid server headers. | Phase author | 2026-05-04 |

---

## Security Audit Trail

| Audit Date | Threats Total | Closed | Open | Run By |
|------------|---------------|--------|------|--------|
| 2026-05-04 | 7 | 7 | 0 | gsd-secure-phase |

---

## Sign-Off

- [x] All threats have a disposition (mitigate / accept / transfer)
- [x] Accepted risks documented in Accepted Risks Log
- [x] `threats_open: 0` confirmed
- [x] `status: verified` set in frontmatter

**Approval:** verified 2026-05-04
