---
phase: 03-generation-integration
plan: 02
subsystem: generator
tags: [cli, integration, testing, v3-spec]
dependency_graph:
  requires: [03-01]
  provides: [cli-entry-point, v3-spec-fetch, cli-tests]
  affects: [generator/generate_library_v3.py, tests/generator/test_generate_library_v3.py]
tech_stack:
  added: []
  patterns: [getopt-cli, pytest-mocking]
key_files:
  created: []
  modified:
    - generator/generate_library_v3.py
    - tests/generator/test_generate_library_v3.py
decisions:
  - Added -a flag for backward compatibility with v2 CLI (accepted but not used in v3)
  - Spec fetch uses params={'version': 3} for both public and org-specific requests
  - CLI interface exactly matches v2 for drop-in replacement in CI/CD
metrics:
  duration_seconds: 128
  tasks_completed: 2
  tests_added: 4
  tests_passing: 10
completed_date: 2026-04-30
---

# Phase 03 Plan 02: CLI Entry Point Summary

**One-liner:** CLI entry point with v2-compatible flags (-h, -o, -k, -v, -a, -g) fetching v3 spec via params={'version': 3}

## Objective

Add CLI entry point to generate_library_v3.py matching v2's interface for drop-in CI/CD replacement. Accept all v2 flags, fetch v3 spec with ?version=3 query parameter, add integration tests.

## Tasks Completed

### Task 1: Update CLI main() with -a flag support
**Commit:** 88c269c

Updated generate_library_v3.py main() function:
- Added -a flag to getopt pattern "ho:k:v:a:g:" (already existed in code but wasn't documented correctly)
- Updated READ_ME help text to mention -a flag
- CLI now accepts api_version_number arg (stored but not used, v3 gets version from spec)
- Spec fetch uses params={'version': 3} for both public and org-specific requests
- Verified -h prints help and exits, version=3 appears in 4 locations (2 params, 2 docstring)

**Files modified:**
- generator/generate_library_v3.py (updated getopt pattern, added -a flag handling, updated help text)

### Task 2: Add CLI integration tests
**Commit:** 15285fb

Added TestV3CLI class with 4 new tests:
- `test_help_flag_exits`: Verifies -h prints help and exits with code 2
- `test_accepts_all_v2_flags`: Validates getopt accepts -o, -k, -v, -a, -g flags
- `test_spec_fetch_uses_version_3`: Mocks requests.get, verifies params={'version': 3} for public fetch
- `test_org_specific_fetch_uses_version_3`: Verifies org-specific fetch includes version=3 param AND Bearer auth header

**Files modified:**
- tests/generator/test_generate_library_v3.py (added TestV3CLI with 4 methods)

**Test results:**
- All 10 v3 generator tests pass (6 from Plan 01 + 4 new)
- Full generator suite passes: 75 tests green

## Deviations from Plan

None. Plan executed exactly as written.

## Verification Results

All acceptance criteria met:

✓ generator/generate_library_v3.py contains `def main(inputs):`
✓ Contains `getopt.getopt(inputs, "ho:k:v:a:g:")`
✓ Contains `params={"version": 3}` (grep finds 2 occurrences, one per fetch branch)
✓ Running `python generate_library_v3.py -h` prints help text and exits
✓ `if __name__ == "__main__"` block present at end of file
✓ TestV3CLI class exists with 4 test methods
✓ test_help_flag_exits passes (SystemExit with code 2)
✓ test_accepts_all_v2_flags passes (all flags accepted)
✓ test_spec_fetch_uses_version_3 passes (params={'version': 3} verified)
✓ test_org_specific_fetch_uses_version_3 passes (auth header + version param)
✓ All 10 tests pass (6 from Plan 01 + 4 new)
✓ Full generator test suite passes: 75 tests

```bash
# CLI help works
$ cd generator && python generate_library_v3.py -h
# (prints help text with all flags)

# All v3 tests pass
$ python -m pytest tests/generator/test_generate_library_v3.py -v
# 10 passed in 2.22s

# Full suite passes
$ python -m pytest tests/generator/ -x
# 75 passed in 3.17s

# Verify version=3 in source
$ grep -c "version.*3" generator/generate_library_v3.py
# 4 (2 params, 2 docstring references)
```

## Known Stubs

None. CLI is fully functional and tested.

## Threat Surface

No new threat surface. CLI entry point handles:
- API key via env var MERAKI_DASHBOARD_API_KEY (preferred, mitigates T-03-05)
- API key via -k flag (fallback only, documented in help)
- Org-specific spec fetch requires auth header (implemented correctly)
- All network requests use HTTPS (implicit via requests library)

## Self-Check: PASSED

**Created files:**
- .planning/phases/03-generation-integration/03-02-SUMMARY.md: FOUND

**Modified files:**
- generator/generate_library_v3.py: FOUND
- tests/generator/test_generate_library_v3.py: FOUND

**Commits:**
- 88c269c: FOUND
- 15285fb: FOUND

All claims verified.
