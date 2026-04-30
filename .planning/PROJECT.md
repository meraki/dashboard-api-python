# Meraki Dashboard API Python SDK

## What This Is

A Python SDK wrapping the Meraki Dashboard API, auto-generated from the OpenAPI spec. Provides both synchronous and async interfaces with pagination, retry logic, rate limiting, and batch action support.

## Core Value

Developers can interact with every Meraki Dashboard API endpoint through a well-typed, well-documented Python client that stays current with the live API spec.

## Current Milestone: v3.1.0 OASv3 Generator

**Goal:** Build a modular OASv3 generator that replaces the abandoned monolithic attempt, following the v2 generator's architecture.

**Target features:**
- Core v3 parsing (resolve `$ref`, `requestBody`, `oneOf`, `nullable`)
- Unified `parse_params` with path-level inheritance and content-type awareness
- HTTP method parsers threaded with `request_body` and `spec`
- Module generation reusing v2's Jinja2 templates and `common.py`
- Action batch handling from `x-batchable-actions`
- Code quality improvements (replace `locals()` antipattern, generate type stubs)
- Golden-file test suite with synthetic v3 fixture
- CI drift detection (v2 vs v3 output diff on live spec)

## Requirements

### Validated

- Generator produces full SDK from OASv2 spec (production, working)
- Sync and async interfaces with identical API surface
- Pagination, retry, rate limiting, batch actions
- kwarg validation with optional logging

### Active

- [ ] OASv3 generator with modular architecture
- [ ] `$ref` resolution with cycle protection
- [ ] `requestBody` parsing (JSON, multipart, octet-stream)
- [ ] `oneOf` query param handling
- [ ] `nullable` type annotations
- [ ] Path-level parameter inheritance
- [ ] Replace `locals()` antipattern with explicit param construction
- [ ] Type stub generation (`.pyi` files)
- [ ] Golden-file test suite for v3 generator
- [ ] CI drift detection between v2 and v3 output

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
| Replace abandoned oasv3 file entirely | Cleaner modular structure vs patching monolith | -- Pending |
| Resolve `$ref` at parse time with caching | Downstream code gets normalized dicts, no template changes | -- Pending |
| `oneOf` reported as "string or object" | Accurate type representation without lying | -- Pending |
| Thread `spec` through all functions | Needed for `$ref` resolution anywhere in tree | -- Pending |
| Explicit param construction over `locals()` | Type-safe, static-analysis friendly | -- Pending |

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
*Last updated: 2026-04-29 after milestone v3.1.0 initialization*
