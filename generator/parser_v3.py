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
