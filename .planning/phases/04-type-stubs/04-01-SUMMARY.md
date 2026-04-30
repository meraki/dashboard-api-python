---
phase: 04-type-stubs
plan: 01
subsystem: generator
tags: [type-stubs, tdd, code-quality]
requires: [parser_v3.parse_params_v3, generate_library.return_params]
provides: [generate_stubs.generate_stub_modules, stub_template.jinja2]
affects: []
tech_stack:
  added: []
  patterns: [type-annotation-mapping, explicit-optional-params]
key_files:
  created:
    - generator/generate_stubs.py
    - generator/stub_template.jinja2
    - tests/generator/test_generate_stubs.py
  modified:
    - tests/generator/fixtures/synthetic_v3_spec_gen.json
decisions:
  - title: "Sort oneOf union types alphabetically"
    rationale: "Consistent ordering (dict | str instead of str | dict) for predictable output"
    alternatives: ["Preserve spec order", "Arbitrary order"]
    outcome: "Alphabetical sort applied"
  - title: "Explicit optional params in stub signatures"
    rationale: "Stubs need full type info for static analysis, not **kwargs"
    alternatives: ["Use **kwargs like runtime code"]
    outcome: "All optional params explicit with = None default"
  - title: "Nullable vs optional handling"
    rationale: "nullable=True means type | None annotation even if required=True"
    alternatives: ["Treat nullable and optional identically"]
    outcome: "Separate handling: nullable adds | None, optional adds = None default"
metrics:
  duration: 216
  tasks_completed: 1
  commits: 2
  files_created: 3
  files_modified: 1
  tests_added: 8
  completed_date: 2026-04-30
---

# Phase 04 Plan 01: Stub Generation Summary

Type stub (.pyi) generation with typed method signatures from OASv3 params for static analysis tooling.

## Objective

Create the .pyi stub generation module and Jinja2 template that produces type-annotated method signatures from parsed OASv3 params, supporting nullable and oneOf semantics for mypy/pyright/IDE autocomplete.

## Completed Tasks

### Task 1: TDD stub generation with type annotation semantics (TDD)

**RED:** Added 8 failing tests covering .pyi generation, nullable params, oneOf params, required/optional distinction, and ellipsis bodies.

**GREEN:** Implemented generate_stubs.py with generate_stub_modules function and stub_template.jinja2. Type annotation mapping handles:
- OAS types to Python types (string -> str, integer -> int, etc.)
- OneOf as union types (object or string -> dict | str, sorted alphabetically)
- Nullable as | None annotation even on required params
- Optional params as explicit signature params with = None default (not **kwargs)
- Ellipsis bodies (: ...) for stub methods

**REFACTOR:** Type mapping logic already extracted to _python_type_annotation helper. No further refactoring needed.

**Commits:**
- cbe5e99: test(04-01): add failing test for stub generation
- 9361e79: feat(04-01): implement stub generation

## Deviations from Plan

None. Plan executed exactly as written.

## Key Decisions

**1. Alphabetical sorting of oneOf union types**

Parser returns "object or string" from spec. Initially rendered as "dict | str" vs test expecting "str | dict". Chose alphabetical sort for consistent, predictable output.

**2. Explicit optional params in signatures**

Stubs (.pyi files) serve static analysis tools, which need full type information. Unlike runtime code (which uses **kwargs for optional params), stubs list every optional param explicitly with type annotation and = None default.

**3. Nullable vs optional semantics**

- `nullable: true, required: true` -> `param: str | None` (no default)
- `nullable: false, required: false` -> `param: str | None = None` (optional default)
- Both add | None to annotation, but only optional gets = None default

This distinction matters for provisionNetworkClients(deviceName) where deviceName is required but accepts null.

## Technical Implementation

**Type annotation mapping:**
```python
def _python_type_annotation(param_dict: dict) -> str:
    # OAS type -> Python type (string -> str, integer -> int, etc.)
    # Handle oneOf: "object or string" -> "dict | str"
    # Apply nullable: append | None if nullable=True
    # Apply optional: append | None if required=False
```

**Stub generation pattern:**
```python
for scope in scopes:
    # Render class header from stub_template.jinja2
    # For each operation:
    #   - Parse params via parse_params_v3
    #   - Build signature: required params, path params, pagination, optional params
    #   - Write: def operation(signature) -> Any: ...
```

**Example output (networks.pyi):**
```python
from typing import Any

class Networks:
    def __init__(self, session: Any) -> None: ...
    def getNetwork(self, networkId: str, name: str | None = None) -> Any: ...
    def getNetworkClients(self, networkId: str, count: int, filter: dict | str | None = None) -> Any: ...
    def provisionNetworkClients(self, networkId: str, deviceName: str | None, mac: str) -> Any: ...
```

## Verification

All tests pass:
```bash
cd generator && python -m pytest ../tests/generator/test_generate_stubs.py -v
# 8 passed in 0.13s
```

Acceptance criteria verified:
- generate_stubs.py contains "def generate_stub_modules" ✓
- generate_stubs.py imports from parser_v3 ✓
- stub_template.jinja2 contains "class {{ class_name }}" ✓
- Tests assert "str | None" ✓
- Tests assert "dict | str" (oneOf union) ✓
- Generated .pyi files contain "..." (ellipsis bodies) ✓
- All tests pass ✓

## Success Criteria

- [x] generate_stubs.py produces .pyi files with correct typed signatures
- [x] Nullable params annotated as type | None
- [x] OneOf params annotated as dict | str (union types)
- [x] Optional params have = None default
- [x] Required params have no default (just type annotation)
- [x] No function bodies in .pyi (just ellipsis)
- [x] All TDD tests pass

## Known Stubs

None. This plan generates type stubs, not runtime code.

## Requirements Fulfilled

GEN-03: Type stub generation (`.pyi` files) with full signatures reflecting nullable and oneOf semantics.

## Self-Check: PASSED

**Created files exist:**
```bash
[ -f "generator/generate_stubs.py" ] && echo "FOUND: generator/generate_stubs.py" || echo "MISSING"
# FOUND: generator/generate_stubs.py

[ -f "generator/stub_template.jinja2" ] && echo "FOUND: generator/stub_template.jinja2" || echo "MISSING"
# FOUND: generator/stub_template.jinja2

[ -f "tests/generator/test_generate_stubs.py" ] && echo "FOUND: tests/generator/test_generate_stubs.py" || echo "MISSING"
# FOUND: tests/generator/test_generate_stubs.py
```

**Commits exist:**
```bash
git log --oneline --all | grep -q "cbe5e99" && echo "FOUND: cbe5e99" || echo "MISSING"
# FOUND: cbe5e99

git log --oneline --all | grep -q "9361e79" && echo "FOUND: 9361e79" || echo "MISSING"
# FOUND: 9361e79
```
