"""
OpenAPI v3 parser for Meraki Dashboard API SDK.

Provides $ref resolution (with caching and cycle detection) and requestBody
parsing that normalizes v3 structures into v2-compatible param dicts.

Module-level functions (not class-based) per project convention.
Spec passed as argument to all functions.
"""

# Module-level cache for resolved $ref pointers (D-01)
_ref_cache: dict[str, dict] = {}


def clear_cache() -> None:
    """Clear ref cache between generator runs. Call at generator entry point."""
    _ref_cache.clear()


def resolve_ref(spec: dict, ref: str, _visited: set | None = None) -> dict:
    """
    Resolve a JSON pointer ($ref) within an OpenAPI spec.

    Uses module-level cache (D-01) and visited-set cycle detection (D-02).
    Raises on unresolvable refs (D-03).

    Args:
        spec: Full OpenAPI spec dict.
        ref: JSON pointer string (must start with "#/").
        _visited: Internal; tracks pointers in current resolution chain.

    Returns:
        Resolved schema dict. Empty dict {} if circular reference detected.

    Raises:
        ValueError: If ref is not an internal reference (doesn't start with "#/").
        KeyError: If pointer path cannot be resolved in spec.
    """
    # Reject external refs
    if not ref.startswith("#/"):
        raise ValueError(f"Only internal refs supported: {ref}")

    # Check cache first (D-01)
    if ref in _ref_cache:
        return _ref_cache[ref]

    # Cycle detection (D-02)
    if _visited is None:
        _visited = set()

    if ref in _visited:
        return {}  # Sentinel for circular reference

    _visited.add(ref)

    # Parse JSON pointer (RFC 6901)
    parts = ref[2:].split("/")
    result = spec
    for part in parts:
        # Unescape JSON pointer tokens per RFC 6901
        part = part.replace("~1", "/").replace("~0", "~")
        if isinstance(result, dict) and part in result:
            result = result[part]
        else:
            raise KeyError(f"Unresolvable $ref: {ref}")

    # If resolved value itself contains $ref, resolve recursively
    if isinstance(result, dict) and "$ref" in result:
        result = resolve_ref(spec, result["$ref"], _visited)

    # Cache resolved value (D-01)
    _ref_cache[ref] = result
    return result


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
    if "requestBody" not in operation:
        return {}, None

    request_body = operation["requestBody"]
    content = request_body.get("content", {})

    # Priority order: json > multipart > octet-stream (D-04)
    if "application/json" in content:
        content_type = "application/json"
        schema = content["application/json"].get("schema", {})
    elif "multipart/form-data" in content:
        content_type = "multipart/form-data"
        schema = content["multipart/form-data"].get("schema", {})
    elif "application/octet-stream" in content:
        # Octet-stream: single 'file' param (D-05)
        return {
            "file": {
                "required": True,
                "in": "body",
                "type": "file",
                "description": "Binary file content",
                "nullable": False,
            }
        }, "application/octet-stream"
    else:
        return {}, None

    if not schema:
        return {}, content_type

    # Resolve $ref if schema itself is a reference
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])

    # Extract properties and required list
    properties = schema.get("properties", {})
    required_list = schema.get("required", [])

    params = {}
    for prop_name, prop_schema in properties.items():
        # Resolve nested $ref in property
        if "$ref" in prop_schema:
            prop_schema = resolve_ref(spec, prop_schema["$ref"])

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

        params[prop_name] = entry

    return params, content_type
