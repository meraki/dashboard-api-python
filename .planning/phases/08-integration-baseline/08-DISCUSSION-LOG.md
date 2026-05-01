# Phase 8: Integration Baseline - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md. This log preserves the alternatives considered.

**Date:** 2026-05-01
**Phase:** 08-integration-baseline
**Areas discussed:** Baseline format, Test scope, Failure policy

---

## Baseline Format

| Option | Description | Selected |
|--------|-------------|----------|
| pytest JSON report | Machine-readable pass/fail per test. Easy to diff in Phase 13. | ✓ |
| Markdown summary | Human-readable table with test name, status, endpoint hit. | |
| Both | JSON + markdown summary for quick reference. | |

**User's choice:** pytest JSON report
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| .planning/phases/08/ | Alongside phase artifacts. | |
| tests/integration/baseline/ | Next to tests. Survives cleanup, easy Phase 13 reference. | ✓ |
| Both | Primary in tests/, copy in phase dir. | |

**User's choice:** tests/integration/baseline/
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Yes | Include durations for Phase 13 performance comparison. | ✓ |
| No, just pass/fail | Simpler. Performance benchmark is Phase 13's job. | |

**User's choice:** Yes (include timing data)
**Notes:** None

---

## Test Scope

| Option | Description | Selected |
|--------|-------------|----------|
| tests/integration/ only | 5 files hitting real API endpoints. | ✓ |
| All tests (unit + integration) | More comprehensive but unit tests unaffected by HTTP swap. | |
| Integration + generator | Generator tests are pure-function, not HTTP-related. | |

**User's choice:** tests/integration/ only
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| No, baseline what exists | Run only files that exist. Conftest ordering is aspirational. | |
| Yes, stub them out | Create missing pagination test files. | |

**User's choice:** (Other) Update conftest.py FILE_ORDER to match actual filenames on disk
**Notes:** All integration tests already exist in the folder; conftest references are just out of date.

---

## Failure Policy

| Option | Description | Selected |
|--------|-------------|----------|
| Document as-is | Baseline records current state. Known failures tagged. Gate = same or better. | ✓ |
| Fix first, then baseline | Get all tests green before capturing. May delay phase. | |
| Exclude known failures | Only baseline passing tests. Simpler gate but loses info. | |

**User's choice:** Document as-is
**Notes:** None

| Option | Description | Selected |
|--------|-------------|----------|
| Same or better | Phase 13 must pass everything baseline passed. New passes OK. | ✓ |
| Identical | Exact same pass/fail/skip set. Strictest. | |
| All pass | Everything green. Higher bar, may require fixing pre-existing issues. | |

**User's choice:** Same or better
**Notes:** None

---

## Claude's Discretion

- Exact pytest-json-report flags and output filename
- Whether to add a README in baseline directory
- How to tag known failures in the report

## Deferred Ideas

None.
