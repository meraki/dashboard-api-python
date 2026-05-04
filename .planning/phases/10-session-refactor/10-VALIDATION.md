---
phase: 10
slug: session-refactor
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-05-04
---

# Phase 10 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 7.x |
| **Config file** | `pytest.ini` |
| **Quick run command** | `python -m pytest tests/ -x -q --tb=short` |
| **Full suite command** | `python -m pytest tests/ --tb=short` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python -m pytest tests/ -x -q --tb=short`
- **After every plan wave:** Run `python -m pytest tests/ --tb=short`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 10-01-01 | 01 | 1 | HTTP-03 | — | N/A | unit | `python -m pytest tests/test_session_base.py -x -q` | ❌ W0 | ⬜ pending |
| 10-01-02 | 01 | 1 | QUAL-01 | — | N/A | unit | `python -m pytest tests/test_session_base.py -x -q` | ❌ W0 | ⬜ pending |
| 10-02-01 | 02 | 1 | QUAL-02 | — | N/A | unit | `python -m pytest tests/test_session_sync.py -x -q` | ❌ W0 | ⬜ pending |
| 10-02-02 | 02 | 1 | HTTP-03 | — | N/A | integration | `python -m pytest tests/test_session_sync.py tests/test_session_async.py -x -q` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/test_session_base.py` — stubs for HTTP-03, QUAL-01
- [ ] `tests/test_session_sync.py` — stubs for sync session inheritance
- [ ] `tests/test_session_async.py` — stubs for async session inheritance
- [ ] `tests/conftest.py` — shared fixtures (mock config, headers)

*Existing pytest infrastructure exists but session-specific test files need creation.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Generator templates produce valid imports | HTTP-03 | Requires running generator and checking output | Run `python generator/generate_library.py` and verify import paths |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
