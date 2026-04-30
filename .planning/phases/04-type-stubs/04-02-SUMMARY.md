---
phase: 04-type-stubs
plan: 02
subsystem: generator
tags: [cli, type-stubs, pep561]
dependency_graph:
  requires: [04-01]
  provides: [stub-generation-cli-integration]
  affects: [generator/generate_library_v3.py]
tech_stack:
  added: []
  patterns: [cli-flag-extension, pep561-marker]
key_files:
  created: []
  modified:
    - generator/generate_library_v3.py
    - tests/generator/test_generate_library_v3.py
decisions:
  - "Use -s flag (no argument) for stub generation trigger"
  - "py.typed marker created as empty file per PEP 561 standard"
  - "Stub generation runs after module generation, before ruff formatting"
metrics:
  duration_seconds: 142
  tasks_completed: 2
  files_modified: 2
  tests_added: 6
  completed: 2026-04-30
---

# Phase 04 Plan 02: CLI Stub Generation Integration

**One-liner:** Wire --stubs CLI flag into v3 generator to produce PEP 561 compliant .pyi files and py.typed marker.

## Overview

Integrated stub generation from Plan 01 into generate_library_v3.py CLI by adding -s flag, wiring generate_stub_modules call, and creating py.typed marker for PEP 561 compliance.

## Tasks Completed

| Task | Description | Commit | Key Changes |
|------|-------------|--------|-------------|
| 1 | Wire --stubs flag to stub generation | 16bc7e0 | Added -s CLI flag, generate_stubs param, py.typed marker creation |
| 2 | Integration tests for --stubs flag | 98ec416 | 6 new tests verifying .pyi creation, py.typed marker, backward compat |

## Implementation Details

### Task 1: CLI Flag and Stub Generation Wiring

Added to `generate_library_v3.py`:
- Import: `from generate_stubs import generate_stub_modules`
- CLI flag: `-s` in getopt pattern `"ho:k:v:a:g:s"`
- Parameter: `generate_stubs: bool = False` in `generate_library()` signature
- Logic block after `generate_modules()`:
  ```python
  if generate_stubs:
      print("Generating .pyi type stubs...")
      generate_stub_modules(spec, scopes, jinja_env, template_dir)
      with open("meraki/py.typed", "w") as f:
          pass  # Empty marker file
      print("Type stubs and py.typed marker created.")
  ```
- Updated help text to document `-s` flag

**Verification:** Import successful, flag parsing works.

### Task 2: Integration Tests

Added `TestV3Stubs` class with 6 tests:
1. `test_stubs_flag_produces_pyi`: Verifies .pyi files created when -s flag active
2. `test_stubs_flag_creates_py_typed`: Verifies py.typed marker created
3. `test_no_stubs_without_flag`: Backward compat check (no stubs without flag)
4. `test_pyi_contains_typed_signatures`: Verifies method signatures in .pyi
5. `test_pyi_nullable_annotation`: Verifies | None annotations present
6. `test_cli_accepts_s_flag`: Verifies CLI flag parsing via getopt

Added helper: `_run_v3_generation_with_stubs()` (mirrors existing pattern, passes `generate_stubs=True`)

**Verification:** All 16 tests pass (10 existing + 6 new).

## Deviations from Plan

None. Plan executed exactly as written.

## Technical Decisions

### py.typed Marker Placement
Created as empty file at `meraki/py.typed` per PEP 561. Empty file signals "this package has inline type hints + stub files."

### Generation Order
Stubs generated after standard modules (sync/async/batch) but before ruff formatting. Ensures all .py modules exist before generating corresponding .pyi files.

### Backward Compatibility
Default behavior unchanged. Stub generation opt-in via explicit -s flag. Existing workflows unaffected.

## Testing Coverage

- CLI flag parsing (getopt compatibility)
- .pyi file creation with --stubs
- py.typed marker creation with --stubs
- No stubs without --stubs (regression protection)
- Type annotation content verification
- Nullable param annotation verification

All existing tests remain passing.

## Integration Points

### From Plan 01
- `generate_stub_modules(spec, scopes, jinja_env, template_dir)` function
- Stub generation logic (signature building, type annotations)
- `stub_template.jinja2` template for class headers

### To Future Consumers
- CLI: `python generate_library_v3.py -s` produces stubs
- Output: `.pyi` files in `meraki/api/` alongside `.py` modules
- Marker: `meraki/py.typed` signals type completeness to type checkers

## Known Limitations

None. GEN-03 requirement complete.

## Security Considerations

No new security surface. Stub generation is read-only operation producing type annotation files from same spec used for runtime code generation.

## Artifacts

### Modified Files
- `generator/generate_library_v3.py`: +19 lines (import, flag, logic, help text)
- `tests/generator/test_generate_library_v3.py`: +56 lines (6 tests + helper)

### Generated at Runtime (when -s flag used)
- `meraki/api/*.pyi` (one per scope)
- `meraki/py.typed` (empty marker)

## Next Steps

GEN-03 complete. Type stub infrastructure ready for:
- IDE autocompletion improvements
- Static analysis (mypy, pyright) compatibility
- Documentation generation from typed signatures

## Self-Check: PASSED

### Created Files
All test files verified present during test execution.

### Modified Files Exist
```
FOUND: generator/generate_library_v3.py
FOUND: tests/generator/test_generate_library_v3.py
```

### Commits Exist
```
FOUND: 16bc7e0
FOUND: 98ec416
```

### Tests Pass
16/16 tests passing (verified above).
