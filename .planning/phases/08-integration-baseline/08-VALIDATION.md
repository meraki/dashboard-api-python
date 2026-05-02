---
phase: 8
slug: integration-baseline
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-05-01
---

# Phase 8 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | pytest 9.0.3 |
| **Config file** | pyproject.toml `[tool.pytest.ini_options]` |
| **Quick run command** | `pytest tests/integration/ --apikey=KEY --o=ORG -x` |
| **Full suite command** | `pytest tests/integration/ --apikey=KEY --o=ORG --json-report --json-report-file=tests/integration/baseline/report.json --json-report-indent=2 --json-report-omit=collectors,log,streams` |
| **Estimated runtime** | ~10 minutes (iterator tests create 100 objects each) |

---

## Sampling Rate

- **After every task commit:** Verify report.json structure if generated
- **After every plan wave:** N/A (single execution phase)
- **Before `/gsd-verify-work`:** report.json exists with `tests` array and `duration` fields
- **Max feedback latency:** N/A (manual sandbox run)

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 8-01-01 | 01 | 1 | TEST-01 | — | N/A | config | `uv add --group dev pytest-json-report && python -c "import pytest_jsonreport"` | ❌ W0 | ⬜ pending |
| 8-01-02 | 01 | 1 | TEST-01 | — | N/A | unit | `python -c "import json; json.load(open('tests/integration/baseline/report.json'))"` | ❌ W0 | ⬜ pending |
| 8-01-03 | 01 | 1 | TEST-01 | — | N/A | manual-only | User runs full suite against Meraki sandbox | N/A | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `pytest-json-report` package added to dev dependencies
- [ ] `tests/integration/baseline/` directory created
- [ ] `conftest.py` FILE_ORDER fixed to match actual filenames

*These are prerequisites before the baseline run can execute.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Full integration test suite passes against Meraki sandbox | TEST-01 | Requires live API credentials and network access | Run full suite command with valid `--apikey` and `--o` values |
| Endpoints list matches actual test coverage | TEST-01 | Requires human review of report vs endpoint table | Compare report.json nodeids against documented endpoint table |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < N/A (manual execution)
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
