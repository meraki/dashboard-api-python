# Phase 12: Error Handling Deprecation - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-05-05
**Phase:** 12-error-handling-deprecation
**Areas discussed:** Signature compat, Deprecation mechanism, Async session raise sites, Migration docs

---

## Signature Compat

| Option | Description | Selected |
|--------|-------------|----------|
| Accept both signatures | AsyncAPIError.__init__(metadata, response, message=None). If message passed, use it directly; if not, fall through to APIError's response.json() extraction. | ✓ |
| Override message after super().__init__ | Call APIError.__init__(metadata, response), then overwrite self.message if a 3rd arg was passed. | |
| You decide | Claude picks the cleanest approach during planning | |

**User's choice:** Accept both signatures (Recommended)
**Notes:** None

---

## Deprecation Mechanism

| Option | Description | Selected |
|--------|-------------|----------|
| On instantiation | warnings.warn fires every time AsyncAPIError() is created | ✓ |
| On import | Warning fires when AsyncAPIError is imported | |
| On catch | Warning fires only when user code catches AsyncAPIError (metaclass) | |

**User's choice:** On instantiation (Recommended)
**Notes:** None

---

## Async Session Raise Sites

| Option | Description | Selected |
|--------|-------------|----------|
| Keep raising AsyncAPIError | Existing user catch blocks keep working. Since it's a subclass, except APIError also catches it. | ✓ |
| Switch to APIError immediately | async_.py raises APIError directly. Forces users to update catch blocks. | |
| Configurable | Flag to let users opt-in to new behavior early | |

**User's choice:** Keep raising AsyncAPIError (Recommended)
**Notes:** None

---

## Migration Docs

| Option | Description | Selected |
|--------|-------------|----------|
| HTTPX-MIGRATION.md + docstring | Migration doc gets a section with before/after code. Class docstring points to APIError. | ✓ |
| HTTPX-MIGRATION.md only | All guidance in the migration doc, minimal code changes | |
| All three | Migration doc + docstring + changelog | |

**User's choice:** HTTPX-MIGRATION.md + docstring (Recommended)
**Notes:** None

---

## Claude's Discretion

- Whether to use `__init_subclass__` or simple inheritance
- Exact wording of deprecation warning message
- Whether to suppress repeated warnings

## Deferred Ideas

None.
