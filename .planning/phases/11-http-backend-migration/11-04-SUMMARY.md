---
phase: 11-http-backend-migration
plan: 04
status: complete
started: 2026-05-05
completed: 2026-05-05
---

## Summary

Narrowed exception catches in both sync and async session retry loops from `except Exception` to `except httpx.HTTPError`, satisfying ERR-03.

## What Was Built

Typed exception handling in retry loops. Only transport-level failures (connection errors, timeouts, protocol errors) now trigger retries. Programming errors propagate immediately instead of being silently retried.

## Key Changes

- `meraki/session/base.py`: Changed `except Exception as e:` to `except httpx.HTTPError as e:` in request() retry loop. Promoted `import httpx` from TYPE_CHECKING to runtime import.
- `meraki/session/async_.py`: Changed `except Exception as e:` to `except httpx.HTTPError as e:` in async request() retry loop. Fixed FakeResponse `json` lambda signature (`lambda self: {}` instead of `lambda: {}`).
- `tests/unit/test_aio_rest_session.py`: Updated 3 tests to use `httpx.ConnectError` instead of bare `Exception` for simulating transport failures.

## Self-Check: PASSED

- `except httpx.HTTPError as e:` appears exactly 1 time in each session file
- `except Exception as e:` appears 0 times in either session file
- All 123 unit tests pass (53 sync + 70 async)

## key-files

### modified
- meraki/session/base.py
- meraki/session/async_.py
- tests/unit/test_aio_rest_session.py
