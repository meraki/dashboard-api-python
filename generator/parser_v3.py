"""
OpenAPI v3 parser for Meraki Dashboard API SDK.

Provides $ref resolution (with caching and cycle detection) and requestBody
parsing that normalizes v3 structures into v2-compatible param dicts.

Module-level functions (not class-based) per project convention.
Spec passed as argument to all functions.
"""

from common import generate_pagination_parameters, return_params

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


def _document_oneof(schema: dict) -> tuple[str, str]:
    """Document oneOf schema as type string with property details."""
    if "oneOf" not in schema:
        return schema.get("type", "object"), ""

    oneof_types = [s.get("type") for s in schema["oneOf"] if "type" in s]

    # Extract object properties
    object_props = []
    for s in schema["oneOf"]:
        if s.get("type") == "object" and "properties" in s:
            object_props = sorted(s["properties"].keys())
            break

    type_str = " or ".join(sorted(set(oneof_types)))

    desc_add = ""
    if object_props:
        desc_add = f" (object supports: {', '.join(object_props)})"

    return type_str, desc_add


def _extract_param_entry(p: dict, spec: dict) -> dict:
    """Convert OASv3 parameter to v2-compatible param dict entry."""
    schema = p.get("schema", {})
    if "$ref" in schema:
        schema = resolve_ref(spec, schema["$ref"])

    # Handle oneOf schemas
    if "oneOf" in schema:
        type_str, desc_add = _document_oneof(schema)
    elif schema.get("type") == "array":
        type_str = "array"
    else:
        type_str = schema.get("type", "string")

    description = p.get("description", schema.get("description", ""))
    if "oneOf" in schema:
        _, desc_add = _document_oneof(schema)
        if desc_add:
            description = description + desc_add if description else desc_add

    entry = {
        "required": p.get("required", False),
        "in": p.get("in", "query"),
        "type": type_str,
        "description": description,
        "nullable": schema.get("nullable", False),
    }

    # Include enum if present
    if "enum" in schema:
        entry["enum"] = schema["enum"]

    # Array params: include items and style/explode defaults
    if schema.get("type") == "array":
        if "items" in schema:
            entry["items"] = schema["items"]
        # OASv3 defaults for query arrays: style=form, explode=true
        if p.get("in", "query") == "query":
            entry["style"] = schema.get("style", "form")
            entry["explode"] = schema.get("explode", True)

    return entry


def parse_params_v3(operation: dict, path_item: dict, spec: dict, param_filters=None) -> tuple[dict, dict]:
    """
    Parse and merge parameters from path-level and operation-level sources.

    Merges path_item.parameters + operation.parameters (op overrides on name+in match),
    then merges requestBody params via parse_request_body. Detects perPage for pagination injection.
    Applies param_filters via return_params if provided (per CONTEXT.md: reuse v2 filter logic).

    Args:
        operation: Operation dict (e.g., paths["/foo"]["get"]).
        path_item: PathItem dict (e.g., paths["/foo"]) for path-level params.
        spec: Full OpenAPI spec dict (for $ref resolution).
        param_filters: Optional list of filter strings (e.g., ["required", "query"]).
            Passed to return_params() from generate_library.py. None = return all.

    Returns:
        Tuple of (params_dict, metadata_dict).
        params_dict: {param_name: {required, in, type, description, nullable, ...}}
        metadata_dict: {"content_type": str | None}
    """
    if param_filters is None:
        param_filters = []

    merged_params = {}

    # Step 1: Inherit path-level parameters
    for p in path_item.get("parameters", []):
        if "$ref" in p:
            p = resolve_ref(spec, p["$ref"])
        key = (p["name"], p.get("in", "query"))
        merged_params[key] = p

    # Step 2: Add/override with operation-level parameters
    for p in operation.get("parameters", []):
        if "$ref" in p:
            p = resolve_ref(spec, p["$ref"])
        key = (p["name"], p.get("in", "query"))
        merged_params[key] = p  # Overrides path-level on name+in match

    # Step 3: Convert to v2-compatible param dict format
    params = {}
    for (name, location), p in merged_params.items():
        params[name] = _extract_param_entry(p, spec)

    # Step 4: Merge requestBody params
    body_params, content_type = parse_request_body(operation, spec)
    params.update(body_params)

    # Step 5: Detect perPage and inject pagination params
    operation_id = operation.get("operationId", "")
    if "perPage" in params:
        params.update(generate_pagination_parameters(operation_id))

    # Step 6: Apply param_filters via return_params (per CONTEXT.md decision)
    params = return_params(operation_id, params, param_filters)

    metadata = {"content_type": content_type}
    return params, metadata
