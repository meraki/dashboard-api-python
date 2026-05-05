# Meraki Dashboard API Python SDK

## What This Is

A Python SDK wrapping the Meraki Dashboard API, auto-generated from the OpenAPI spec. Provides both synchronous and async interfaces with pagination, retry logic, rate limiting, and batch action support.

## Core Value

Developers can interact with every Meraki Dashboard API endpoint through a well-typed, well-documented Python client that stays current with the live API spec.

## Current Milestone: v4.0 HTTPX Migration

**Goal:** Replace dual HTTP backends (requests + aiohttp) with unified httpx, eliminating sync/async duplication and fixing known bugs.

**Target features:**
- Unified HTTP backend (httpx.Client + httpx.AsyncClient)
- Shared session base class extracting ~80% of duplicated logic
- Library-agnostic param encoding (remove monkey-patch)
- Decomposed request logic (complexity 42 -> <10 per method)
- Full type annotations on session layer
- Backwards-compatible deprecation of AsyncAPIError
- Property-based tests for param encoding
- Updated test infra (respx replaces responses)

## Previous State (v1.0)

Modular OASv3 generator built and tested. Produces sync, async, and batch modules with explicit param construction, .pyi type stubs, and CI drift detection against live spec. 124 tests passing.

## Requirements

### Validated

- Generator produces full SDK from OASv2 spec (production, working)
- Sync and async interfaces with identical API surface
- Pagination, retry, rate limiting, batch actions
- kwarg validation with optional logging
- ✓ OASv3 generator with modular architecture - v1.0
- ✓ `$ref` resolution with cycle protection - v1.0
- ✓ `requestBody` parsing (JSON, multipart, octet-stream) - v1.0
- ✓ `oneOf` query param handling - v1.0
- ✓ `nullable` type annotations - v1.0
- ✓ Path-level parameter inheritance - v1.0
- ✓ Replace `locals()` antipattern with explicit param construction - v1.0
- ✓ Type stub generation (`.pyi` files) - v1.0
- ✓ Golden-file test suite for v3 generator - v1.0
- ✓ CI drift detection between v2 and v3 output - v1.0

### Active

- [ ] Unified httpx backend replacing requests + aiohttp
- [ ] Shared session base class with decision logic
- [x] Library-agnostic param encoding utility - Validated in Phase 9: Foundation
- [ ] Decomposed request methods (complexity <10 each)
- [ ] Type annotations on session layer
- [x] AsyncAPIError backwards-compatible deprecation - Validated in Phase 12: error-handling-deprecation
- [x] Property-based tests for param encoding - Validated in Phase 9: Foundation
- [ ] Test infra migration (respx replaces responses)

### Out of Scope

- Adaptive retry strategy (app logic, not library choice)
- Pagination memory buffering (iterator pattern already exists)
- API key exposure risk (logging concern, unrelated to transport)
- OASv3 generator migration (separate milestone)
- Request cancellation/OpenTelemetry integration (httpx has primitives but wiring is separate)
- Generator scripts' use of requests (dev-only, optional Phase 12)

## Context

- Live v3 spec at `https://api.meraki.com/api/v1/openapiSpec?version=3` (OpenAPI 3.0.1)
- Existing v2 generator: `generator/generate_library.py` (production)
- Abandoned v3 attempt: `generator/generate_library_oasv3.py` (monolithic, incomplete)
- Shared utilities: `generator/common.py`, Jinja2 templates in `generator/`
- v3 spec has features not in v2: `requestBody`, `$ref`, `oneOf` query params, `nullable`, `components/schemas`
- 298 `x-batchable-actions` entries present in v3 spec

## Constraints

- **Compatibility**: Output must be structurally identical to v2, with enhanced features (like object query params) and docstrings from v3-only features
- **Architecture**: Follow v2's modular structure; reuse `common.py` and templates
- **Testing**: Golden-file tests must validate v3-specific output, not match v2 byte-for-byte
- **Deprecation**: v2 generator retained until parity gate passes for 2+ consecutive API releases

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Replace abandoned oasv3 file entirely | Cleaner modular structure vs patching monolith | ✓ Good |
| Resolve `$ref` at parse time with caching | Downstream code gets normalized dicts, no template changes | ✓ Good |
| `oneOf` reported as "string or object" | Accurate type representation without lying | ✓ Good |
| Thread `spec` through all functions | Needed for `$ref` resolution anywhere in tree | ✓ Good |
| Explicit param construction over `locals()` | Type-safe, static-analysis friendly | ✓ Good |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? -> Move to Out of Scope with reason
2. Requirements validated? -> Move to Validated with phase reference
3. New requirements emerged? -> Add to Active
4. Decisions to log? -> Add to Key Decisions
5. "What This Is" still accurate? -> Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check, still the right priority?
3. Audit Out of Scope, reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-05-05 after Phase 12 (error-handling-deprecation) complete, AsyncAPIError deprecated as APIError subclass*
