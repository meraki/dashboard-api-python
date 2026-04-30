# Phase 1: Parser Foundation - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md. This log preserves the alternatives considered.

**Date:** 2026-04-30
**Phase:** 01-parser-foundation
**Areas discussed:** $ref resolution mechanics, requestBody content types, Module architecture, Output contract

---

## $ref Resolution Mechanics

### Caching Strategy

| Option | Description | Selected |
|--------|-------------|----------|
| Module-level dict | Simple dict keyed by JSON pointer string, populated during parse. Fast, zero deps, cleared between runs. | ✓ |
| LRU cache decorator | functools.lru_cache on resolve_ref(). Automatic eviction, but requires hashable args. | |
| You decide | Claude picks during planning. | |

**User's choice:** Module-level dict
**Notes:** None

### Cycle Detection

| Option | Description | Selected |
|--------|-------------|----------|
| Visited set per resolution | Pass a set of seen pointers through recursive calls. If pointer already in set, return sentinel. | ✓ |
| Max depth limit | Cap recursion at N levels. Simpler but could falsely truncate valid chains. | |
| Both (set + depth cap) | Belt and suspenders approach. | |

**User's choice:** Visited set per resolution
**Notes:** None

### Unresolvable Refs

| Option | Description | Selected |
|--------|-------------|----------|
| Log warning + skip param | Log bad pointer, return empty dict. Generator keeps running. | |
| Raise exception | Hard fail on unresolvable ref. Forces spec correctness. | ✓ |
| Return raw $ref dict | Pass through unresolved ref for templates to handle. | |

**User's choice:** Raise exception
**Notes:** None

---

## requestBody Content Types

### Multipart/form-data Representation

| Option | Description | Selected |
|--------|-------------|----------|
| Same as JSON body params | Properties become standard param dict entries. Content-type distinction at HTTP layer. | ✓ |
| Separate 'in' value | Use in: 'formData' to distinguish from JSON body. | |
| You decide | Claude picks based on template needs. | |

**User's choice:** Same as JSON body params
**Notes:** None

### Octet-stream (Binary Upload)

| Option | Description | Selected |
|--------|-------------|----------|
| Single param with type 'file' | One param entry: {name: 'file', type: 'file', in: 'body', required: true}. | ✓ |
| Flag on operation metadata | Set is_binary_upload: true instead of adding a param. | |
| You decide | Claude picks based on existing template handling. | |

**User's choice:** Single param with type 'file'
**Notes:** None

### Content-Type Tracking

| Option | Description | Selected |
|--------|-------------|----------|
| Yes, store as metadata | Add content_type field to operation-level dict. Templates/session can use it. | ✓ |
| No, infer from param types | If any param has type 'file', it's multipart. Otherwise JSON. | |
| You decide | Claude picks based on RestSession needs. | |

**User's choice:** Yes, store as metadata
**Notes:** None

---

## Module Architecture

### File Organization

| Option | Description | Selected |
|--------|-------------|----------|
| Single parser_v3.py | All parsing functions in one file. Matches v2's single-file pattern. | ✓ |
| Split by concern | Separate files: ref_resolver.py, body_parser.py, param_parser.py. | |
| You decide | Claude picks based on expected complexity. | |

**User's choice:** Single parser_v3.py
**Notes:** None

### Function Style

| Option | Description | Selected |
|--------|-------------|----------|
| Standalone functions | Module-level functions with spec passed as arg. Matches v2 style. | ✓ |
| Parser class | Class holding spec + cache as instance state. | |
| You decide | Claude picks based on spec threading. | |

**User's choice:** Standalone functions
**Notes:** None

### File Location

| Option | Description | Selected |
|--------|-------------|----------|
| generator/parser_v3.py | Sibling to generate_library.py and common.py. | ✓ |
| generator/v3/parser.py | New subdirectory for all v3 code. | |
| You decide | Claude picks based on import ergonomics. | |

**User's choice:** generator/parser_v3.py
**Notes:** None

---

## Output Contract

### New Dict Keys

| Option | Description | Selected |
|--------|-------------|----------|
| Add 'nullable' key only | Add nullable: true/false. Phase 2 uses it for type annotations. No other new keys. | ✓ |
| No new keys yet | Byte-for-byte compatible with v2 param dicts. Phase 2 adds extensions. | |
| Add nullable + content_type + original_ref | More metadata upfront for downstream phases. | |

**User's choice:** Add 'nullable' key only
**Notes:** None

### Compatibility Signaling

| Option | Description | Selected |
|--------|-------------|----------|
| Don't signal, just include | Templates ignore unknown keys. No special signaling needed. | ✓ |
| Version field on output | Add parser_version: 3 for downstream branching. | |
| You decide | Claude picks based on template needs. | |

**User's choice:** Don't signal, just include
**Notes:** None

---

## Claude's Discretion

None. All decisions made explicitly by user.

## Deferred Ideas

None. Discussion stayed within phase scope.
