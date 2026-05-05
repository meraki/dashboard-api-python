---
phase: 13-test-infrastructure
plan: 03
subsystem: ci
tags: [ci, benchmarks, integration-gate, baseline]
dependency_graph:
  requires: [13-01]
  provides: [ci-benchmark-job, baseline-validation]
  affects: [.github/workflows/test-library.yml]
tech_stack:
  added: [actions/upload-artifact@v4]
  patterns: [benchmark-artifact-upload, baseline-regression-gate]
key_files:
  modified:
    - .github/workflows/test-library.yml
decisions:
  - Baseline validation uses --co (collect-only) to count tests without running them
  - Benchmark job depends on unit-test (not integration-test) to run in parallel
metrics:
  duration: 84s
  completed: "2026-05-05T22:43:30Z"
  tasks_completed: 1
  tasks_total: 1
---

# Phase 13 Plan 03: CI Benchmark Job and Baseline Validation Summary

CI workflow enhanced with benchmark job (Python 3.11-3.14 matrix, JSON artifact upload) and integration test baseline regression gate validating 32-test minimum.

## Changes Made

### Task 1: Add benchmark job and baseline comparison to CI (22960d3)

- Added `tests/benchmarks/**` to both push and pull_request path triggers
- Added "Validate against baseline" step after integration tests (collects tests, asserts >= 32)
- Added `benchmark:` job with Python 3.11-3.14 matrix, pytest-benchmark JSON output, and artifact upload via actions/upload-artifact@v4
- Verified existing PR gating (D-10) and Python matrix (D-08) already satisfied

## Deviations from Plan

None - plan executed exactly as written.

## Verification Results

- `grep "benchmark:" .github/workflows/test-library.yml` - PASS
- `grep "baseline" .github/workflows/test-library.yml` - PASS
- `grep "pull_request" .github/workflows/test-library.yml` - PASS
- YAML validation via `yaml.safe_load()` - PASS

## Commits

| Task | Commit | Message |
|------|--------|---------|
| 1 | 22960d3 | feat(13-03): add benchmark job and baseline validation to CI |
