# Phase 9: Foundation - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-05-01
**Phase:** 09-foundation
**Areas discussed:** Module location, Function signature, Property-based tests, Transition bridge

---

## Module Location

| Option | Description | Selected |
|--------|-------------|----------|
| meraki/encoding.py | New focused module. Clean dependency graph for Phase 10 base class. | ✓ |
| meraki/utils.py | General utility module. Risk: becomes a junk drawer. | |
| Keep in rest_session.py | Minimal file changes. Stays coupled to requests. | |

**User's choice:** meraki/encoding.py
**Notes:** None

---

## Function Signature

| Option | Description | Selected |
|--------|-------------|----------|
| Clean now + adapter | encode_meraki_params(data) with lambda adapter for monkey-patch | ✓ |
| Legacy shape until Phase 11 | Keep (_, data) signature until requests removed | |

**User's choice:** Clean signature now with transition adapter
**Notes:** User asked for ramification explanation. Clarified this is internal-only (not public API), and the integration baseline makes behavioral drift detectable.

---

## Property-Based Tests

| Option | Description | Selected |
|--------|-------------|----------|
| Roundtrip fidelity | Encoded output parsed back reconstructs original keys/values | ✓ |
| Array-of-objects contract | Dict values in lists produce param[]key=value format | |
| Passthrough invariants | str/bytes/file-like returned unchanged | |
| Edge case fuzzing | Unicode, empty dicts, None values, nested structures | |

**User's choice:** Roundtrip fidelity (mandatory). Others at Claude's discretion.
**Notes:** None

---

## Transition Bridge

| Option | Description | Selected |
|--------|-------------|----------|
| Import + adapter | Single source of truth, lambda bridges monkey-patch | |
| Duplicate until Phase 11 | Old function stays, new function in encoding.py, two copies | ✓ |
| You decide | Claude picks during planning | |

**User's choice:** Duplicate until Phase 11
**Notes:** User asked for ramification explanation. Chose conservative approach despite integration tests making the adapter safe. Prefers zero-change to existing code.

---

## Claude's Discretion

- Hypothesis strategies and input generators
- Whether to add parametrize-based unit tests alongside property tests
- Internal helper functions within encoding.py

## Deferred Ideas

None.
