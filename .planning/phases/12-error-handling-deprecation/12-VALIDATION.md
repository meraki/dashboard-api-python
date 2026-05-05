---
phase: 12
slug: error-handling-deprecation
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-05-05
---

# Phase 12 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 7.x |
| **Config file** | `pytest.ini` |
| **Quick run command** | `python -m pytest tests/unit/test_exceptions.py -x -q` |
| **Full suite command** | `python -m pytest tests/ -x -q` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python -m pytest tests/unit/test_exceptions.py -x -q`
- **After every plan wave:** Run `python -m pytest tests/ -x -q`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 12-01-01 | 01 | 1 | ERR-02 | — | N/A | unit | `python -m pytest tests/unit/test_exceptions.py::test_async_api_error_is_subclass -x` | ❌ W0 | ⬜ pending |
| 12-01-02 | 01 | 1 | ERR-02 | — | N/A | unit | `python -m pytest tests/unit/test_exceptions.py::test_async_api_error_deprecation_warning -x` | ❌ W0 | ⬜ pending |
| 12-01-03 | 01 | 1 | ERR-02 | — | N/A | unit | `python -m pytest tests/unit/test_exceptions.py::test_async_api_error_old_3arg_signature -x` | ❌ W0 | ⬜ pending |
| 12-01-04 | 01 | 1 | ERR-02 | — | N/A | unit | `python -m pytest tests/unit/test_exceptions.py::test_async_api_error_caught_by_api_error -x` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/unit/test_exceptions.py` — add stubs for ERR-02 deprecation tests (subclass, warning, 3-arg compat, catch-by-parent)

*Existing test infrastructure covers framework needs. Only new test cases required.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Documentation recommends catching APIError | ERR-02 | Prose content in HTTPX-MIGRATION.md | Read HTTPX-MIGRATION.md "Deprecated: AsyncAPIError" section; verify it says to catch APIError |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
