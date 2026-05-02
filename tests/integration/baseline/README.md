# Integration Test Baseline

Machine-readable pass/fail snapshot of all integration tests captured before the httpx migration (v4.0 Phase 8).

## Purpose

Phase 13 uses `report.json` as the regression gate. The rule (D-07): **same or better**. No new failures allowed after migration; new passes are OK.

## How it was captured

```bash
pytest tests/integration/ \
  --apikey="$MERAKI_DASHBOARD_API_KEY" \
  --o="$MERAKI_ORG_ID" \
  -v \
  --json-report \
  --json-report-file=tests/integration/baseline/report.json \
  --json-report-indent=2 \
  --json-report-omit=collectors,log,streams
```

## Schema

See pytest-json-report docs. Key fields per test: `nodeid`, `outcome`, `call.duration`.

## Regression comparison (Phase 13)

For each test in baseline where `outcome == "passed"`, Phase 13 must also pass.
Tests that failed in baseline are "known failures" and do not block.
