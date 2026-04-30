---
phase: 1
slug: parser-foundation
status: draft
nyquist_compliant: true
wave_0_complete: false
created: 2026-04-30
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 7.x |
| **Config file** | pytest.ini (or pyproject.toml [tool.pytest.ini_options]) |
| **Quick run command** | `python -m pytest tests/generator/test_parser_v3.py -x -q` |
| **Full suite command** | `python -m pytest tests/generator/ -q` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python -m pytest tests/generator/test_parser_v3.py -x -q`
- **After every plan wave:** Run `python -m pytest tests/generator/ -q`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 1-01-01 | 01 | 1 | PARSE-01 | — | N/A | unit | `python -m pytest tests/generator/test_parser_v3.py::test_resolve_ref_simple -x` | ❌ W0 | ⬜ pending |
| 1-01-02 | 01 | 1 | PARSE-01 | — | Cycle detection prevents stack overflow | unit | `python -m pytest tests/generator/test_parser_v3.py::test_resolve_ref_cycle -x` | ❌ W0 | ⬜ pending |
| 1-01-03 | 01 | 1 | PARSE-01 | — | Cache hit returns same object | unit | `python -m pytest tests/generator/test_parser_v3.py::test_resolve_ref_cache -x` | ❌ W0 | ⬜ pending |
| 1-02-01 | 02 | 1 | PARSE-02 | — | N/A | unit | `python -m pytest tests/generator/test_parser_v3.py::test_parse_request_body_json -x` | ❌ W0 | ⬜ pending |
| 1-02-02 | 02 | 1 | PARSE-02 | — | N/A | unit | `python -m pytest tests/generator/test_parser_v3.py::test_parse_request_body_multipart -x` | ❌ W0 | ⬜ pending |
| 1-02-03 | 02 | 1 | PARSE-02 | — | N/A | unit | `python -m pytest tests/generator/test_parser_v3.py::test_parse_request_body_octet -x` | ❌ W0 | ⬜ pending |
| 1-02-04 | 02 | 1 | PARSE-02 | — | Output matches v2 param dict format | integration | `python -m pytest tests/generator/test_parser_v3.py::test_output_format_v2_compat -x` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/generator/test_parser_v3.py` — test stubs for PARSE-01 and PARSE-02
- [ ] `tests/generator/conftest.py` — shared fixtures (sample v3 spec fragments with $refs, requestBodies)

*Existing pytest infrastructure likely exists; verify before creating new config.*

---

## Manual-Only Verifications

*All phase behaviors have automated verification.*

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
