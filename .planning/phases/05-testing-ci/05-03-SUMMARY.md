---
phase: 05-testing-ci
plan: 03
subsystem: ci-drift-detection
tags: [ci, semantic-diff, drift-detection, testing]
dependency_graph:
  requires: [05-02]
  provides: [semantic-diff-v2-v3, drift-detection-workflow]
  affects: [ci-pipeline, generator-validation]
tech_stack:
  added: [GitHub-Actions-workflow, semantic-diff-script]
  patterns: [method-signature-extraction, regex-based-parsing, offline-generation]
key_files:
  created:
    - scripts/semantic_diff_v2_v3.py
    - .github/workflows/v3-drift-detection.yml
    - tests/generator/test_semantic_diff.py
  modified: []
decisions:
  - decision: Exit 0 for PARAM_DIFF and TYPE_DIFF, only fail on MISSING_IN_V3
    rationale: v3 generator intentionally changes param handling (GEN-02), so param/type differences are expected and informational
    alternatives: [fail-on-any-drift, allowlist-known-diffs]
  - decision: Mock requests.get in both generators during diff
    rationale: Enables offline comparison without network calls or GitHub authentication
    alternatives: [use-cached-files, skip-non-generated-files]
  - decision: Weekly scheduled run on Mondays at 6am UTC
    rationale: Catches spec evolution drift regularly without blocking every commit
    alternatives: [daily-runs, on-demand-only]
metrics:
  duration_seconds: 1
  tasks_completed: 2
  tests_added: 11
  files_created: 3
  completed_at: 2026-04-30
---

# Phase 05 Plan 03: V3 Drift Detection Summary

Semantic diff CI workflow for v2/v3 generator output comparison.

## One-Liner

CI workflow and semantic diff script that compares v2 vs v3 generator output method signatures, detecting when v3 drops methods v2 has while treating param/type differences as informational.

## Tasks Completed

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | Create semantic diff script | 68959a7 | scripts/semantic_diff_v2_v3.py |
| 2 | Create CI workflow and unit tests | 6f4540a | .github/workflows/v3-drift-detection.yml, tests/generator/test_semantic_diff.py |

## What Was Built

**Semantic diff script (scripts/semantic_diff_v2_v3.py):**
- Runs both v2 and v3 generators against the same spec in isolated temp directories
- Extracts method names, parameter lists, and type annotations via regex from generated modules
- Compares semantically (not textually): ignores whitespace, formatting, kwargs style differences
- Reports four drift categories:
  - MISSING_IN_V3: Method exists in v2 but not v3 (critical)
  - MISSING_IN_V2: Method exists in v3 but not v2 (informational, new endpoints)
  - PARAM_DIFF: Same method, different param names
  - TYPE_DIFF: Same param name, different type annotation
- CLI flags: `--live` (fetch live spec), `--json` (machine-readable output), `--fail-on-missing` (strict mode)
- Exit code 0 for expected differences, 1 with `--fail-on-missing` when MISSING_IN_V3 detected

**CI workflow (.github/workflows/v3-drift-detection.yml):**
- Triggers on push/PR to main/release when generator/ or semantic_diff_v2_v3.py changes
- Weekly scheduled run (Mondays 6am UTC) to catch spec evolution drift
- Uses uv to install dependencies, runs semantic diff against live spec
- Fails (exit 1) only if MISSING_IN_V3 detected (critical drift)
- Uploads drift-report.json artifact (30-day retention) for review
- Reports param/type differences as informational (expected v3 divergence from v2)

**Unit tests (tests/generator/test_semantic_diff.py):**
- TestExtractMethods: Validates method signature parsing (simple/multiple params, defaults, __init__ exclusion)
- TestCompareModules: Validates drift detection (identical, missing in v3/v2, param diff, type diff, kwargs ignored)
- 11 tests, all passing

## Deviations from Plan

None. Plan executed exactly as written.

## Verification Results

- [x] All 11 unit tests pass
- [x] extract_methods correctly parses method signatures with type annotations
- [x] compare_modules detects missing methods, param differences, type differences
- [x] Workflow YAML is valid (uses standard GitHub Actions syntax)
- [x] Script runs offline when given local spec file (mocks requests.get)
- [x] --fail-on-missing flag correctly exits 1 when MISSING_IN_V3 detected

## Next Steps

- Run workflow against live spec to establish baseline drift metrics
- Monitor weekly runs for spec evolution (new endpoints, deprecations)
- If v3 drops methods unexpectedly, investigate spec changes or v3 parser bugs
- Consider adding allowlist for known intentional method removals

## Self-Check: PASSED

Created files verified:
- FOUND: scripts/semantic_diff_v2_v3.py
- FOUND: .github/workflows/v3-drift-detection.yml
- FOUND: tests/generator/test_semantic_diff.py

Commits verified:
- FOUND: 68959a7
- FOUND: 6f4540a
