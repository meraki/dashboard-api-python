---
phase: 05-testing-ci
plan: 02
subsystem: generator-testing
tags: [testing, golden-files, v3-generator, semantic-validation]
dependency_graph:
  requires: [synthetic_v3_spec_gen.json, generate_library_v3.py, parser_v3.py]
  provides: [golden-file-validation, test_golden_v3_output.py]
  affects: [v3-generator-quality-gate, regression-detection]
tech_stack:
  added: []
  patterns: [semantic-comparison, golden-file-testing, pytest-fixtures]
key_files:
  created:
    - tests/generator/test_golden_v3_output.py
    - tests/generator/fixtures/golden_sync_networks.py
    - tests/generator/fixtures/golden_async_networks.py
    - tests/generator/fixtures/golden_batch_networks.py
  modified:
    - generator/generate_library_v3.py
decisions:
  - decision: "Semantic comparison over byte-for-byte matching"
    rationale: "Formatting changes (ruff) shouldn't fail tests; only structural changes matter"
    alternatives: ["diff-based comparison", "AST comparison"]
  - decision: "Extract method signatures with regex"
    rationale: "Lightweight, sufficient for detecting API surface changes"
    alternatives: ["AST parsing", "import and inspect"]
  - decision: "Golden files are Python source, not JSON snapshots"
    rationale: "Developer-readable, can be used as reference examples"
    alternatives: ["serialized AST", "JSON metadata"]
metrics:
  duration_minutes: 3
  completed_date: 2026-04-30
  tasks_completed: 2
  files_created: 4
  files_modified: 1
  tests_added: 10
  auto_fixes: 1
---

# Phase 05 Plan 02: Golden-File Tests Summary

Golden-file validation for v3 generator output using semantic comparison.

## What Was Built

Test suite that validates v3 generator produces correct sync, async, and batch modules by comparing method names, signatures, and class structure against committed golden files. Tests use semantic comparison (not byte-matching) to catch API surface changes without breaking on formatting.

## Tasks Completed

### Task 1: Generate golden files from v3 generator

**Commit:** acb22d5

**Files:**
- tests/generator/fixtures/golden_sync_networks.py
- tests/generator/fixtures/golden_async_networks.py
- tests/generator/fixtures/golden_batch_networks.py
- generator/generate_library_v3.py (fixed)

**What was done:**
Generated golden output files from v3 generator using synthetic_v3_spec_gen.json fixture. Discovered and fixed GEN-02 bug where methods without optional params still used `kwargs.items()` in body/query param construction, causing F821 undefined name errors.

### Task 2: Create golden-file comparison test module

**Commit:** cbe917f

**Files:**
- tests/generator/test_golden_v3_output.py

**What was done:**
Created test module with semantic comparison strategy. Tests extract method signatures, class names, and param lists using regex, then compare against golden files. Validates sync/async/batch modules independently. Supports `--update-golden` flag for regeneration workflow.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] Fixed undefined kwargs in methods with required-only params**
- **Found during:** Task 1, golden file generation
- **Issue:** Methods with only required params (no optional) didn't include `**kwargs` in signature, but templates used `kwargs.items()` for body/query param construction. Ruff reported F821 undefined name errors.
- **Root cause:** Line 294-295 in generate_library_v3.py only added `**kwargs` if optional params existed, but templates unconditionally access kwargs for body/query/array params.
- **Fix:** Modified standard and batch function generation to add `**kwargs` whenever body_params, query_params, or array_params exist (lines 293-315 and 495-510).
- **Files modified:** generator/generate_library_v3.py
- **Commit:** acb22d5

## Verification Results

All acceptance criteria met:

- tests/generator/fixtures/golden_sync_networks.py exists, contains `class Networks`, has method definitions
- tests/generator/fixtures/golden_async_networks.py exists, contains `class Networks`, has method definitions
- tests/generator/fixtures/golden_batch_networks.py exists, contains `class Networks`, has 3 batchable methods + `__init__`
- No golden file contains `kwargs.update(locals())` or `kwargs = locals()`
- tests/generator/test_golden_v3_output.py exists with TestGoldenSync, TestGoldenAsync, TestGoldenBatch classes
- All 10 tests pass (1 skipped without `--update-golden` flag)
- Tests compare method names and signatures semantically
- Golden files match current generator output

## Known Stubs

None. Golden files contain actual generated code from the v3 generator.

## Test Results

```
pytest tests/generator/test_golden_v3_output.py -v
======================== 10 passed, 1 skipped in 5.02s ========================
```

**Test coverage:**
- TestGoldenSync: 4 tests (class name, method names, signatures, no kwargs.update)
- TestGoldenAsync: 3 tests (class name, method names, signatures)
- TestGoldenBatch: 3 tests (class name, method names, method count validation)
- TestGoldenRegeneration: 1 test (skipped without flag)

## Impact

**Quality gates enabled:**
- v3 generator output changes now trigger test failures
- Regression detection for method signature changes
- Validation that GEN-02 fix (no `kwargs.update(locals())`) persists

**Developer workflow:**
1. Make intentional generator changes
2. Run tests (fail)
3. Review diff
4. Run `pytest --update-golden` to commit new baseline
5. Tests pass

## Self-Check: PASSED

### Created files exist
```
FOUND: tests/generator/test_golden_v3_output.py
FOUND: tests/generator/fixtures/golden_sync_networks.py
FOUND: tests/generator/fixtures/golden_async_networks.py
FOUND: tests/generator/fixtures/golden_batch_networks.py
```

### Commits exist
```
FOUND: acb22d5 (Task 1: generator fix + golden files)
FOUND: cbe917f (Task 2: golden-file test module)
```

### Tests pass
```
10 passed, 1 skipped
```
