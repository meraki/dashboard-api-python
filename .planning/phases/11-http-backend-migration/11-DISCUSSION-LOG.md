# Phase 11: HTTP Backend Migration - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md; this log preserves the alternatives considered.

**Date:** 2026-05-04
**Phase:** 11-http-backend-migration
**Areas discussed:** AsyncAPIError transition, Concurrency control, Exception specificity, Response compatibility

---

## AsyncAPIError Transition

| Option | Description | Selected |
|--------|-------------|----------|
| Update in place | Change AsyncAPIError to use status_code/reason_phrase now. Phase 12 then just makes it a subclass of APIError. Clean two-step. | ✓ |
| Shim attributes | Add .status and .reason as properties on httpx.Response wrapper so AsyncAPIError code doesn't change until Phase 12. | |
| Claude decides | Let Claude pick the cleanest approach based on downstream impact. | |

**User's choice:** Update in place
**Notes:** None

---

## Concurrency Control

| Option | Description | Selected |
|--------|-------------|----------|
| Replace with pool limits | httpx pool handles concurrency natively. Remove semaphore, set max_connections=AIO_MAXIMUM_CONCURRENT_REQUESTS. Simpler, fewer moving parts. | ✓ |
| Keep both layers | Semaphore gates requests before they hit the pool. Defense in depth, but redundant for the common case. | |
| Semaphore only | Keep existing semaphore pattern, let httpx pool be unbounded. Minimal behavior change from current aiohttp approach. | |

**User's choice:** Replace with pool limits
**Notes:** Also update the relevant part of config.py that defines/overrides max connections.

---

## Exception Specificity

| Option | Description | Selected |
|--------|-------------|----------|
| Catch httpx.HTTPError | Single catch for all transport failures (connect, timeout, protocol). Simple, matches current broad-except behavior. Re-raise as APIError with context. | ✓ |
| Split by category | Separate catches for httpx.ConnectError, httpx.TimeoutException, httpx.ProtocolError. More specific error messages per failure type. | |
| Claude decides | Let Claude pick based on what the retry logic actually needs to differentiate. | |

**User's choice:** Catch httpx.HTTPError
**Notes:** None

---

## Response Compatibility

| Option | Description | Selected |
|--------|-------------|----------|
| Accept the break | httpx uses reason_phrase. APIError already reads status_code (same). Update APIError.__init__ to use reason_phrase. Minor breaking change but Phase 12 unifies error classes anyway. | ✓ |
| Add .reason property | Add a .reason property to APIError that reads response.reason_phrase. External code using error.reason still works. | |
| Claude decides | Let Claude evaluate if any downstream code references .reason on the response directly. | |

**User's choice:** Accept the break
**Notes:** Document this and all other breaking changes in HTTPX-MIGRATION.md under a "Breaking Changes" section with context on the change and steps needed to resolve it.

---

## Claude's Discretion

- httpx client initialization strategy (persistent vs per-request)
- Timeout configuration style (httpx.Timeout object vs float)
- Whether _transport_kwargs() survives or merges into client-level config
- Handling aiohttp content_type=None pattern in json() calls

## Deferred Ideas

None.
