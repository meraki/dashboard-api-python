# Phase 1: Parser Foundation - Pattern Map

**Mapped:** 2026-04-30
**Files analyzed:** 1 new file, 3 existing analogs
**Analogs found:** 3 / 3

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `generator/parser_v3.py` | utility | transform | `generator/generate_library_oasv3.py` | role-match |

## Pattern Assignments

### `generator/parser_v3.py` (utility, transform)

**Analog:** `generator/generate_library_oasv3.py` (abandoned v3 attempt) + `generator/generate_library.py` (v2 production)

**Imports pattern** (generate_library.py lines 1-12):
```python
import getopt
import json
import os
import platform
import re
import subprocess
import sys

import jinja2
import requests

import common as common
```

**Module-level cache pattern** (NEW for parser_v3.py):
```python
# Module-level dict cache for $ref resolution
_ref_cache = {}

def clear_cache():
    """Clear ref cache between generator runs."""
    global _ref_cache
    _ref_cache = {}
```

**$ref resolution pattern** (generate_library_oasv3.py lines 25-41):
```python
# Helper function to resolve $ref references in OASv3
def resolve_ref(spec, ref):
    """
    Resolve a $ref reference in OASv3 spec.
    Example: #/components/schemas/Network -> spec['components']['schemas']['Network']
    """
    if not ref.startswith("#/"):
        return None

    parts = ref[2:].split("/")  # Remove '#/' and split
    result = spec
    for part in parts:
        if isinstance(result, dict) and part in result:
            result = result[part]
        else:
            return None
    return result
```

**Enhancement needed:** Add caching, cycle detection, raise on unresolvable per CONTEXT.md D-01, D-02, D-03

**requestBody parsing pattern** (generate_library_oasv3.py lines 140-193):
```python
# Helper function to parse requestBody from OASv3
def parse_request_body(operation, request_body, spec):
    """
    Parse requestBody from OASv3 specification.
    In OASv3, requestBody has a 'content' object with media types (e.g., 'application/json').
    """
    if not request_body:
        return {}

    params = {}

    # OASv3 requestBody has a 'content' object
    if "content" in request_body:
        # Usually we want application/json
        content = request_body["content"]
        json_content = content.get("application/json", {})

        if json_content:
            schema = get_schema_from_item(json_content, spec)
            if schema and "properties" in schema:
                # Get required fields from schema
                required_fields = schema.get("required", [])

                # Parse each property
                for prop_name, prop_schema in schema["properties"].items():
                    # Resolve $ref if present
                    if "$ref" in prop_schema:
                        resolved = resolve_ref(spec, prop_schema["$ref"])
                        if resolved:
                            prop_schema = resolved

                    params[prop_name] = {
                        "required": prop_name in required_fields,
                        "in": "body",
                        "type": prop_schema.get("type", "object"),
                        "description": prop_schema.get("description", ""),
                    }

                    # Handle enum
                    if "enum" in prop_schema:
                        params[prop_name]["enum"] = prop_schema["enum"]

                    # Handle array type
                    if prop_schema.get("type") == "array":
                        params[prop_name]["type"] = "array"
                        if "items" in prop_schema:
                            items = prop_schema["items"]
                            if "$ref" in items:
                                resolved = resolve_ref(spec, items["$ref"])
                                if resolved:
                                    params[prop_name]["items"] = resolved

    return params
```

**Enhancement needed:** Add `nullable` field per CONTEXT.md D-10, add `content_type` tracking per D-06

**Param dict contract** (generate_library.py lines 109-133):
```python
def unpack_param_without_schema(all_params: dict, this_param: dict, name: str, is_required: bool):
    # Set required attribute
    all_params[name] = {"required": is_required}

    # Assign relevant attributes
    for attribute in ("in", "type"):
        all_params[name][attribute] = this_param[attribute]

    # Capture the enum if available
    if "enum" in this_param:
        all_params[name]["enum"] = this_param["enum"]

    # Assign the description to the parameter if it's available
    if "description" in this_param:
        all_params[name]["description"] = this_param["description"]

    # Fall back to required if there is no description
    elif is_required:
        all_params[name]["description"] = "(required)"

    # Fall back to whatever the description is otherwise
    else:
        all_params[name]["description"] = this_param["description"]

    return all_params
```

**v2 param dict format (MUST MAINTAIN):**
- Keys: `required` (bool), `in` (str: "path"/"query"/"body"), `type` (str), `description` (str)
- Optional keys: `enum` (list), `items` (dict for arrays)
- NEW in v3: `nullable` (bool, defaults to False)

**Standalone function pattern** (generate_library.py lines 32-51):
```python
# Helper function to return pagination parameters depending on endpoint
def generate_pagination_parameters(operation: str):
    ret = {
        "total_pages": {
            "type": "integer or string",
            "description": 'use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages',
        },
        "direction": {
            "type": "string",
            "description": 'direction to paginate, either "next" or "prev" (default) page'
            if operation in REVERSE_PAGINATION
            else 'direction to paginate, either "next" (default) or "prev" page',
        },
    }
    if operation == "getNetworkEvents":
        ret["event_log_end_time"] = {
            "type": "string",
            "description": "ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, "
            "to retrieve events within a time window",
        }
    return ret
```

**Pattern:** Module-level functions (not class-based), spec/params passed as args. Per CONTEXT.md D-08.

**Reusable utility from common.py** (lines 1-36):
```python
def organize_spec(paths, scopes):
    operations = list()  # list of operation IDs
    for path, methods in paths.items():
        # method is the HTTP action, e.g., get, put, etc.
        for method in methods:
            # endpoint is the method for that specific path
            endpoint = paths[path][method]

            # the endpoint has tags
            tags = endpoint["tags"]

            # the endpoint has an operationId
            operation = endpoint["operationId"]

            # add the operation ID to the list
            operations.append(operation)

            # The endpoint has a scope defined by the first tag
            # There are a handful of operations that are currently mistagged
            # This helps ensure they are scoped to the correct module
            if len(tags) > 2:
                match tags[2]:
                    case "spaces":
                        scope = "spaces"
                    case _:
                        scope = tags[0]
            else:
                scope = tags[0]

            # Needs documentation
            if path not in scopes[scope]:
                scopes[scope][path] = {method: endpoint}
            # Needs documentation
            else:
                scopes[scope][path][method] = endpoint
    return operations, scopes
```

**Reuse:** Import from `common` module, don't duplicate. Per CONTEXT.md code_context.

**Test pattern** (tests/generator/test_pure_functions.py lines 1-4):
```python
import pytest

import generate_library as gen


class TestDocsUrl:
    def test_simple(self):
        assert gen.docs_url("getOrganizations") == (
            "https://developer.cisco.com/meraki/api-v1/#!get-organizations"
        )
```

**Pattern:** pytest classes grouping related tests, descriptive test names, import module under test directly

---

## Shared Patterns

### JSON Pointer Escaping (RFC 6901)
**Source:** RESEARCH.md code examples
**Apply to:** `resolve_ref()` function in parser_v3.py
```python
# Manual escaping for JSON pointer tokens per RFC 6901
def unescape_pointer_token(token: str) -> str:
    """Unescape JSON pointer token per RFC 6901."""
    return token.replace("~1", "/").replace("~0", "~")

# Example: #/paths/~1devices~1{serial}/get
# After split: ["paths", "~1devices~1{serial}", "get"]
# After unescape: ["paths", "/devices/{serial}", "get"]
```

### Error Handling
**Source:** generate_library_oasv3.py lines 26-41 (return None on error)
**Enhancement:** Per CONTEXT.md D-03, raise exception on unresolvable refs instead of returning None
```python
# OLD pattern (abandoned v3):
if isinstance(result, dict) and part in result:
    result = result[part]
else:
    return None  # Silent failure

# NEW pattern (parser_v3.py should use):
if isinstance(result, dict) and part in result:
    result = result[part]
else:
    raise KeyError(f"Unresolvable $ref: {ref}")  # Hard fail per D-03
```

### Module Structure
**Source:** generator/ directory structure
**Apply to:** parser_v3.py file placement
```
generator/
├── generate_library.py          # v2 generator (production)
├── generate_library_oasv3.py    # Abandoned v3 (reference only)
├── parser_v3.py                 # NEW: Phase 1 core parsing
├── common.py                    # Shared utilities (reuse)
└── templates/                   # Jinja2 templates (unchanged Phase 1)
```

**Pattern:** Sibling modules at generator/ root level, no subdirectories per CONTEXT.md D-07.

### Type Annotations
**Source:** generate_library.py lines 32, 84, 109
**Apply to:** All parser_v3.py functions
```python
def generate_pagination_parameters(operation: str):
def return_params(operation: str, params: dict, param_filters):
def unpack_param_without_schema(all_params: dict, this_param: dict, name: str, is_required: bool):
```

**Pattern:** Type hints for function parameters, return types on complex functions. Match stdlib typing usage in existing code.

---

## No Analog Found

None. All patterns have existing analogs in codebase.

---

## Implementation Notes

### Key Differences from Abandoned v3
1. **Caching:** parser_v3.py adds module-level `_ref_cache` dict (abandoned v3 has no caching)
2. **Cycle detection:** parser_v3.py uses visited set passed through recursion (abandoned v3 has no cycle protection)
3. **Error handling:** parser_v3.py raises on unresolvable refs (abandoned v3 returns None silently)
4. **nullable field:** parser_v3.py adds `nullable` to param dicts (abandoned v3 doesn't track it)
5. **content_type metadata:** parser_v3.py tracks operation-level content-type (abandoned v3 doesn't expose it)

### Integration Points
- parser_v3.py will be imported by future generate_library_v3.py (Phase 3)
- Output dicts MUST match return_params() expectations (generate_library.py lines 84-106)
- Output dicts MUST work with existing Jinja2 templates (same keys v2 references)
- common.py utilities (organize_spec, etc.) should be imported, not duplicated

---

## Metadata

**Analog search scope:** generator/, tests/generator/
**Files scanned:** 4 (common.py, generate_library.py, generate_library_oasv3.py, test_pure_functions.py)
**Pattern extraction date:** 2026-04-30
