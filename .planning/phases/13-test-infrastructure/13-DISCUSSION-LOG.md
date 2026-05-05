# Phase 13: Test Infrastructure - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-05
**Phase:** 13-test-infrastructure
**Areas discussed:** Regression gate strategy, Performance benchmark, Generator test mocks, CI test matrix

---

## Regression Gate Strategy

| Option | Description | Selected |
|--------|-------------|----------|
| Run integration tests now | Run suite against Meraki sandbox post-migration, treat current results as baseline | ✓ |
| Skip integration tests | Unit + mock integration tests are sufficient | |
| Capture and compare | Run now, document, compare against future run | |

**User's choice:** Run integration tests now
**Notes:** API key is available, no setup steps needed.

---

## Performance Benchmark

### Metrics

| Option | Description | Selected |
|--------|-------------|----------|
| Request latency | Time per HTTP request (mean, p95, p99) | ✓ |
| Throughput | Requests/second under concurrent load | ✓ |
| Memory usage | RSS/heap difference | ✓ |
| Connection pool | Connection reuse efficiency, warmup time | ✓ |

**User's choice:** All four metrics selected.

### Tooling

| Option | Description | Selected |
|--------|-------------|----------|
| pytest-benchmark | Integrated into test suite, runs with pytest | ✓ |
| Standalone script | Separate benchmark script, more flexibility | |
| Both | pytest-benchmark for latency, standalone for memory | |

**User's choice:** pytest-benchmark

### Baseline

**User's choice:** Use existing baseline at `tests/integration/baseline/report.json`

---

## Generator Test Mocks

| Option | Description | Selected |
|--------|-------------|----------|
| Skip (out of scope) | Leave generator test mocks as-is | |
| Migrate them too | Migrate generator test mocks to httpx style | ✓ |

**User's choice:** Migrate them too

### Follow-up: Generator Scripts

| Option | Description | Selected |
|--------|-------------|----------|
| Just test mocks | Keep generator scripts using requests | |
| Scripts + mocks | Full migration, remove requests from dev deps | ✓ |

**User's choice:** Scripts + mocks (full requests removal)

---

## CI Test Matrix

### Python Versions

**User's choice:** 3.11, 3.12, 3.13, 3.14

### Integration Tests in CI

| Option | Description | Selected |
|--------|-------------|----------|
| CI with secret | Integration tests in CI using stored API key | ✓ |
| Manual only | Developer-triggered only | |
| Nightly schedule | Cron-based, not per-PR | |

**User's choice:** CI with secret

### CI Trigger

| Option | Description | Selected |
|--------|-------------|----------|
| Every PR | Integration tests gate every PR merge | ✓ |
| Main + nightly | PRs run unit/mock only, integration on merge | |
| You decide | Claude picks | |

**User's choice:** Every PR

---

## Claude's Discretion

- pytest-benchmark fixture design and grouping
- Memory measurement approach within pytest-benchmark constraints
- CI workflow file structure (single vs multi-job)
- Whether to use pytest-xdist for parallel test execution

## Deferred Ideas

None.
