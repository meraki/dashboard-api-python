# Meraki Dashboard API Python SDK

## What This Is

A Python SDK wrapping the Meraki Dashboard API, auto-generated from the OpenAPI spec. Provides both synchronous and async interfaces with pagination, retry logic, rate limiting, and batch action support.

## Core Value

Developers can interact with every Meraki Dashboard API endpoint through a well-typed, well-documented Python client that stays current with the live API spec.

## Current State

**Shipped:** v1.0 OASv3 Generator (2026-04-30)

Modular OASv3 generator built and tested. Produces sync, async, and batch modules with explicit param construction, .pyi type stubs, and CI drift detection against live spec.

**New files:**
- `generator/parser_v3.py` (283 LOC) - $ref resolution, requestBody parsing, unified parse_params_v3
- `generator/generate_library_v3.py` (630 LOC) - Module generation + CLI
- `generator/generate_stubs.py` (136 LOC) - .pyi stub generation
- `scripts/semantic_diff_v2_v3.py` (262 LOC) - v2/v3 drift detection
- 124 tests passing

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

(Next milestone TBD)

### Out of Scope

- Modifying the v2 generator (kept for rollback)
- Changing the runtime SDK behavior (rest_session, pagination, etc.)
- Supporting OpenAPI 3.1 (`type: [string, null]` syntax)
- Rewriting Jinja2 templates from scratch (reuse existing, extend as needed)

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
*Last updated: 2026-04-30 after v1.0 milestone*
