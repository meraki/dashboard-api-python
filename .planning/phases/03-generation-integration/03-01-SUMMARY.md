---
phase: 03-generation-integration
plan: 01
subsystem: generator
tags: [generator, v3, parse_params_v3, explicit-params, batch-actions]
dependency_graph:
  requires: [parser_v3.py, common.py, generate_library.py]
  provides: [generate_library_v3.py, v3 generator entry point]
  affects: [SDK build pipeline, CI generator tests]
tech_stack:
  added: []
  patterns: [Jinja2 template rendering, filtered path dict for organize_spec, empty kwarg_line for explicit param construction]
key_files:
  created:
    - generator/generate_library_v3.py
    - tests/generator/test_generate_library_v3.py
    - tests/generator/fixtures/synthetic_v3_spec_gen.json
  modified: []
decisions:
  - title: "Pre-filter paths before organize_spec"
    rationale: "v3 spec paths contain 'parameters' key alongside HTTP methods. organize_spec expects only HTTP method keys. Pre-filtering cleanly isolates the difference."
    alternatives: "Post-filter section dict after organize_spec, or modify organize_spec to skip non-method keys."
    outcome: "Pre-filter chosen for minimal change surface and cleaner separation of v2/v3 logic."
  - title: "Match batchable actions by description OR summary"
    rationale: "v3 spec inconsistently uses 'description' vs 'summary' for endpoint text. Matching both ensures all batch methods are generated."
    alternatives: "Normalize spec before processing, or rely on single field match."
    outcome: "Dual-field match chosen for robustness without spec mutation."
metrics:
  duration_seconds: 127
  tasks_completed: 2
  files_created: 3
  files_modified: 0
  commits: 2
  tests_added: 6
  tests_passing: 6
  completed_date: "2026-04-30"
---

# Phase 3 Plan 1: Core v3 Generator Summary

v3 generator produces sync/async/batch modules from OASv3 spec using parse_params_v3 and explicit parameter construction (no kwargs.update(locals())).

## Objective Achievement

**Target:** Create the core v3 generator module that produces sync, async, and batch modules from an OASv3 spec using parse_params_v3 and explicit parameter construction.

**Outcome:** Fully achieved. generate_library_v3.py generates all three module types for each scope, integrates Phase 1+2 parser, eliminates locals() antipattern, and passes all 6 tests validating GEN-01, GEN-02, and GEN-04 requirements.

## Tasks Completed

### Task 1: Create test fixture and test scaffolding

**Commit:** 2635dc3

Created synthetic_v3_spec_gen.json with 3 x-batchable-actions (create/update/destroy) matching endpoint descriptions. Implemented test_generate_library_v3.py with 6 tests verifying:
- Sync module generation
- Async module generation
- Batch module generation
- No kwargs.update(locals()) in generated code
- Batch method count matches x-batchable-actions count
- Explicit param construction with query_params/body_params lists

**Files:**
- tests/generator/fixtures/synthetic_v3_spec_gen.json (169 lines, 5 endpoints, 3 batchable actions)
- tests/generator/test_generate_library_v3.py (115 lines, 6 test methods)

### Task 2: Implement generate_library_v3.py core generator

**Commit:** 83ef36f

Implemented v3 generator following v2 architecture with critical GEN-02 fix. Key features:
- Imports parse_params_v3 and clear_cache from parser_v3
- Calls clear_cache() at entry to prevent stale cache between runs
- Pre-filters paths dict to remove 'parameters' key before passing to organize_spec
- Sets kwarg_line="" in both generate_standard_and_async_functions and generate_action_batch_functions
- Matches batchable actions by description OR summary (handles v3 inconsistency)
- Reuses v2 Jinja2 templates (function_template.jinja2, async_function_template.jinja2, batch_function_template.jinja2)
- Runs ruff format on generated output

**Files:**
- generator/generate_library_v3.py (607 lines)

All 6 tests pass. No kwargs.update(locals()) anywhere in generator logic.

## Deviations from Plan

None. Plan executed exactly as written.

## Technical Notes

**Path filtering:** organize_spec expects paths dict with only HTTP method keys (get, post, put, delete). v3 spec paths include "parameters" key at path level. Pre-filtering cleanly removes this before organize_spec call, preserving original spec["paths"] for path_item lookups in generate functions.

**Batchable action matching:** v3 spec inconsistently uses endpoint.description vs endpoint.summary for text content. generate_action_batch_functions checks both fields against batchable_action_summaries list to ensure all batch methods are generated.

**kwarg_line elimination:** Templates check `{% if kwarg_line|length > 0 %}` before rendering locals() logic. Setting kwarg_line="" causes template to skip that block entirely. Generated code builds params/payload dicts explicitly from query_params/body_params/array_params lists passed as template vars.

## Known Stubs

None. All generated methods are fully functional (pending live spec testing in Phase 4).

## Verification Results

```bash
cd C:/Users/jkuchta/Work/_Repos/meraki/dashboard-api-python/.claude/worktrees/agent-a8bc71353a5f3a3c1
python -m pytest tests/generator/test_generate_library_v3.py -v
```

**Result:** 6 passed in 2.43s

```bash
grep -r "kwargs.update(locals())" generator/generate_library_v3.py | wc -l
```

**Result:** 0

```bash
grep -c 'kwarg_line = ""' generator/generate_library_v3.py
```

**Result:** 2 (once in generate_standard_and_async_functions, once in generate_action_batch_functions)

## Self-Check: PASSED

**Created files exist:**
- FOUND: generator/generate_library_v3.py
- FOUND: tests/generator/test_generate_library_v3.py
- FOUND: tests/generator/fixtures/synthetic_v3_spec_gen.json

**Commits exist:**
- FOUND: 2635dc3 (test fixture and scaffolding)
- FOUND: 83ef36f (v3 generator implementation)

**Test results verified:**
- All 6 tests collected and passed
- No kwargs.update(locals()) in generator code
- Batch action count assertion passes (3 expected, 3 generated)

## Requirements Trace

- **GEN-01:** Generator produces meraki/api/{scope}.py, meraki/aio/api/{scope}.py, meraki/api/batch/{scope}.py (verified by test_produces_sync_module, test_produces_async_module, test_produces_batch_module)
- **GEN-02:** No kwargs.update(locals()), explicit param dict construction (verified by test_no_kwargs_update_locals, test_explicit_param_construction, grep results)
- **GEN-04:** All x-batchable-actions produce batch methods (verified by test_batch_action_count)

## Next Steps

Phase 3 Plan 2 will integrate the v3 generator into CI, add golden-file diff tests, and validate output against live v3 spec.
