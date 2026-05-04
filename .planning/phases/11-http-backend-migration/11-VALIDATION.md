---
phase: 11
slug: http-backend-migration
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-05-04
---

# Phase 11 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 9.0.3 |
| **Config file** | pyproject.toml [tool.pytest.ini_options] |
| **Quick run command** | `python -m pytest tests/ -x -q --timeout=30` |
| **Full suite command** | `python -m pytest tests/ --timeout=60` |
| **Estimated runtime** | ~15 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python -m pytest tests/ -x -q --timeout=30`
- **After every plan wave:** Run `python -m pytest tests/ --timeout=60`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 15 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 11-01-01 | 01 | 1 | HTTP-01 | — | N/A | unit | `python -m pytest tests/test_rest_session.py -x -q` | ✅ | ⬜ pending |
| 11-01-02 | 01 | 1 | HTTP-02 | — | N/A | unit | `python -m pytest tests/test_async_rest_session.py -x -q` | ✅ | ⬜ pending |
| 11-02-01 | 02 | 1 | ERR-01 | — | N/A | unit | `python -m pytest tests/test_exceptions.py -x -q` | ✅ | ⬜ pending |
| 11-02-02 | 02 | 1 | ERR-03 | — | N/A | unit | `python -m pytest tests/test_rest_session.py -k "exception" -x -q` | ✅ | ⬜ pending |
| 11-03-01 | 03 | 2 | DEP-01 | — | N/A | integration | `python -c "import meraki; print(meraki.__version__)"` | ✅ | ⬜ pending |
| 11-03-02 | 03 | 2 | DEP-03 | — | N/A | unit | `python -m pytest tests/test_rest_session.py -k "proxy" -x -q` | ✅ | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

*Existing infrastructure covers all phase requirements.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| proxy passthrough works with real proxy | DEP-03 | Requires actual proxy server | Set requests_proxy param, verify httpx receives proxy= kwarg |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 15s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
