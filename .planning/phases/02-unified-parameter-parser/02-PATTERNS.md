# Phase 2: Unified Parameter Parser - Pattern Map

**Mapped:** 2026-04-30
**Files analyzed:** 2 new files
**Analogs found:** 2 / 2

## File Classification

| New/Modified File | Role | Data Flow | Closest Analog | Match Quality |
|-------------------|------|-----------|----------------|---------------|
| `generator/parser_v3.py` (extend) | parser | transform | `generator/parser_v3.py` (Phase 1) | exact |
| `tests/generator/test_parser_v3.py` (extend) | test | validation | `tests/generator/test_parser_v3.py` (Phase 1) | exact |
| `tests/generator/fixtures/synthetic_v3_spec.json` (extend) | fixture | test-data | `tests/generator/fixtures/synthetic_v3_spec.json` (Phase 1) | exact |

## Pattern Assignments

### `generator/parser_v3.py` (parser, transform)

**Analog:** `generator/parser_v3.py` (Phase 1) + `generator/generate_library.py` (v2 generator)

**Module structure** (lines 1-13):
```python
"""
OpenAPI v3 parser for Meraki Dashboard API SDK.

Provides $ref resolution (with caching and cycle detection) and requestBody
parsing that normalizes v3 structures into v2-compatible param dicts.

Module-level functions (not class-based) per project convention.
Spec passed as argument to all functions.
"""

# Module-level cache for resolved $ref pointers (D-01)
_ref_cache: dict[str, dict] = {}
```

**Function signature pattern** (lines 76-90):
```python
def parse_request_body(operation: dict, spec: dict) -> tuple[dict, str | None]:
    """
    Parse requestBody into normalized param dict and content type.

    Handles application/json, multipart/form-data, and application/octet-stream.
    Output matches v2 param dict format with added nullable field (D-04, D-05, D-06, D-10).

    Args:
        operation: Single operation dict from OpenAPI spec (e.g., paths["/foo"]["post"]).
        spec: Full OpenAPI spec dict (for $ref resolution).

    Returns:
        Tuple of (params_dict, content_type).
        params_dict: {param_name: {required, in, type, description, nullable, ...}}
        content_type: String like "application/json" or None if no requestBody.
    """
```

**Resolve $ref pattern** (lines 20-73):
```python
# Use resolve_ref for any $ref in parameters:
if "$ref" in p:
    p = resolve_ref(spec, p["$ref"])
```

**Param dict format** (lines 136-152):
```python
entry = {
    "required": prop_name in required_list,
    "in": "body",
    "type": prop_schema.get("type", "object"),
    "description": prop_schema.get("description", ""),
    "nullable": prop_schema.get("nullable", False),  # D-10
}

# Include enum if present
if "enum" in prop_schema:
    entry["enum"] = prop_schema["enum"]

# Include array items if present
if prop_schema.get("type") == "array" and "items" in prop_schema:
    entry["items"] = prop_schema["items"]
```

**v2 generator pattern references** (from `generator/generate_library.py`):

**Pagination detection** (lines 32-51):
```python
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

**Param filtering** (lines 84-106):
```python
def return_params(operation: str, params: dict, param_filters):
    # Return parameters based on matching input filters
    if not param_filters:
        return params
    else:
        ret = {}
        if "required" in param_filters:
            ret.update({k: v for k, v in params.items() if "required" in v and v["required"]})
        if "pagination" in param_filters:
            ret.update(generate_pagination_parameters(operation) if "perPage" in params else {})
        if "optional" in param_filters:
            ret.update({k: v for k, v in params.items() if "required" in v and not v["required"]})
        if "path" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "path"})
        if "query" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "query"})
        if "body" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["in"] == "body"})
        if "array" in param_filters:
            ret.update({k: v for k, v in params.items() if "in" in v and v["type"] == "array"})
        if "enum" in param_filters:
            ret.update({k: v for k, v in params.items() if "enum" in v})
        return ret
```

---

### `tests/generator/test_parser_v3.py` (test, validation)

**Analog:** `tests/generator/test_parser_v3.py` (Phase 1)

**Test module structure** (lines 1-22):
```python
import json
import pytest
from pathlib import Path

from parser_v3 import resolve_ref, clear_cache, _ref_cache, parse_request_body

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def v3_spec():
    with open(FIXTURES / "synthetic_v3_spec.json") as f:
        return json.load(f)


@pytest.fixture(autouse=True)
def reset_cache():
    """Clear cache before each test to prevent cross-test pollution."""
    clear_cache()
    yield
    clear_cache()
```

**Test class structure** (lines 77-159):
```python
class TestParseRequestBody:
    """Tests for parse_request_body per PARSE-02."""

    def test_json_body_extracts_properties(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, content_type = parse_request_body(operation, v3_spec)
        assert "name" in params
        assert "tags" in params
        assert "timeZone" in params
        assert "notes" in params
        assert params["name"]["in"] == "body"
        assert params["name"]["type"] == "string"
        assert params["name"]["description"] == "Network name"

    def test_required_tracking(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, _ = parse_request_body(operation, v3_spec)
        assert params["name"]["required"] is True
        assert params["tags"]["required"] is False
        assert params["notes"]["required"] is False
```

**Test naming convention:**
- Class: `TestFunctionName` (e.g., `TestParseParamsV3`)
- Method: `test_specific_behavior` (e.g., `test_path_level_inheritance`)

---

### `tests/generator/fixtures/synthetic_v3_spec.json` (fixture, test-data)

**Analog:** `tests/generator/fixtures/synthetic_v3_spec.json` (Phase 1)

**Fixture structure** (lines 1-121):
```json
{
  "openapi": "3.0.1",
  "info": {"title": "Synthetic Meraki v3", "version": "1.0.0"},
  "components": {
    "schemas": {
      "Network": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "name": {"type": "string", "description": "Network name"}
        }
      }
    }
  },
  "paths": {
    "/networks/{networkId}": {
      "get": {
        "tags": ["networks", "configure"],
        "operationId": "getNetwork",
        "parameters": [
          {"name": "networkId", "in": "path", "required": true, "schema": {"type": "string"}}
        ],
        "responses": {"200": {"description": "OK"}}
      },
      "put": {
        "tags": ["networks", "configure"],
        "operationId": "updateNetwork",
        "parameters": [
          {"name": "networkId", "in": "path", "required": true, "schema": {"type": "string"}}
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "type": "object",
                "properties": {
                  "name": {"type": "string", "description": "Network name"},
                  "tags": {"type": "array", "items": {"type": "string"}, "description": "Network tags"},
                  "timeZone": {"type": "string", "description": "Timezone", "nullable": true},
                  "notes": {"type": "string", "description": "Notes for the network"}
                },
                "required": ["name"]
              }
            }
          }
        },
        "responses": {"200": {"description": "OK"}}
      }
    }
  }
}
```

**Extension requirements for Phase 2:**
- Add path-level parameters to existing paths
- Add oneOf query parameter examples
- Add operation with query params (in: query)
- Maintain existing structure and schema references

---

## Shared Patterns

### $ref Resolution
**Source:** `generator/parser_v3.py` lines 20-73
**Apply to:** All functions handling OASv3 parameter or schema objects
```python
if "$ref" in param_or_schema:
    param_or_schema = resolve_ref(spec, param_or_schema["$ref"])
```

### Param Dict Format (v2 compatibility)
**Source:** `generator/parser_v3.py` lines 136-152
**Apply to:** All parameter parsing functions
```python
{
    "required": bool,
    "in": "path" | "query" | "body",
    "type": str,
    "description": str,
    "nullable": bool,
    # Optional:
    "enum": list,
    "items": dict,  # for arrays
}
```

### Module-Level Caching
**Source:** `generator/parser_v3.py` lines 11-17
**Apply to:** Parser functions that need cross-call memoization
```python
_cache_name: dict = {}

def clear_cache() -> None:
    """Clear cache between generator runs."""
    _cache_name.clear()
```

### Docstring Format
**Source:** `generator/parser_v3.py` lines 76-90
**Apply to:** All public functions
- Triple-quoted docstring with one-line summary
- Args section with type hints in signature (not docstring)
- Returns section describing tuple/dict structure
- No Raises section needed (type hints cover contracts)

### Test Fixtures
**Source:** `tests/generator/test_parser_v3.py` lines 10-21
**Apply to:** All test modules using JSON fixtures
```python
FIXTURES = Path(__file__).parent / "fixtures"

@pytest.fixture
def v3_spec():
    with open(FIXTURES / "synthetic_v3_spec.json") as f:
        return json.load(f)

@pytest.fixture(autouse=True)
def reset_cache():
    """Clear cache before each test to prevent cross-test pollution."""
    clear_cache()
    yield
    clear_cache()
```

---

## No Analog Found

None. All Phase 2 files extend existing Phase 1 files with same structure/patterns.

---

## Metadata

**Analog search scope:**
- `generator/*.py` (5 files scanned)
- `tests/generator/*.py` (5 files scanned)
- `tests/generator/fixtures/*.json` (2 files scanned)

**Files scanned:** 12

**Pattern extraction date:** 2026-04-30

**Key decisions:**
- Phase 2 extends Phase 1 code in same files (parser_v3.py, test_parser_v3.py)
- New function `parse_params_v3` follows exact pattern as `parse_request_body`
- Reuse v2 generator utilities (`return_params`, `generate_pagination_parameters`) via import
- Test structure mirrors Phase 1 with new `TestParseParamsV3` class
- Fixture extension adds path-level params and oneOf examples to existing synthetic_v3_spec.json
