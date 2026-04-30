"""
Type stub (.pyi) generation for Meraki Dashboard API SDK.

Produces .pyi files with typed method signatures from parsed OASv3 params.
"""

import os
import re
import jinja2
from parser_v3 import parse_params_v3
from generate_library import return_params, REVERSE_PAGINATION


def _python_type_annotation(param_dict: dict) -> str:
    """
    Convert param dict to Python type annotation string.

    Args:
        param_dict: Param entry with keys: type, nullable, required

    Returns:
        Type annotation string (e.g., "str", "str | None", "str | dict | None")
    """
    param_type = param_dict.get("type", "object")

    # Map OAS type to Python type
    type_map = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "list",
        "object": "dict",
    }

    # Handle oneOf case (type = "string or object")
    if " or " in param_type:
        parts = param_type.split(" or ")
        python_types = sorted([type_map.get(p.strip(), "Any") for p in parts])
        base_type = " | ".join(python_types)
    else:
        base_type = type_map.get(param_type, "Any")

    # Apply nullable annotation
    if param_dict.get("nullable", False):
        return f"{base_type} | None"

    # Apply optional annotation (not required)
    if not param_dict.get("required", False):
        return f"{base_type} | None"

    return base_type


def generate_stub_modules(spec: dict, scopes: dict, jinja_env: jinja2.Environment, template_dir: str):
    """
    Generate .pyi stub modules for each scope.

    Args:
        spec: Full OpenAPI spec dict
        scopes: Dict of scope name -> {path: {method: endpoint}}
        jinja_env: Jinja2 environment
        template_dir: Directory containing templates (empty string if cwd)
    """
    for scope in scopes:
        section = scopes[scope]

        stub_path = f"meraki/api/{scope}.pyi"
        with open(stub_path, "w", encoding="utf-8", newline=None) as stub_output:
            # Render class header
            with open(f"{template_dir}stub_template.jinja2", encoding="utf-8", newline=None) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                stub_output.write(
                    template.render(
                        class_name=scope[0].upper() + scope[1:],
                    )
                )

            # Generate method signatures
            for path, methods in section.items():
                for method, endpoint in methods.items():
                    operation = endpoint["operationId"]

                    # Get path_item from spec
                    path_item = spec["paths"][path]

                    # Parse params using v3 parser
                    all_params, metadata = parse_params_v3(endpoint, path_item, spec)

                    # Build method signature
                    signature_parts = ["self"]
                    defined_params = set()

                    # Add required params
                    for p, values in return_params(operation, all_params, ["required"]).items():
                        defined_params.add(p)
                        annotation = _python_type_annotation(values)
                        signature_parts.append(f"{p}: {annotation}")

                    # Add path params (if not already in required)
                    for p, values in return_params(operation, all_params, ["path"]).items():
                        if p not in defined_params:
                            defined_params.add(p)
                            annotation = _python_type_annotation(values)
                            signature_parts.append(f"{p}: {annotation}")

                    # Catch params referenced in URL but not declared
                    for p in re.findall(r"\{(\w+)\}", path):
                        if p not in defined_params:
                            defined_params.add(p)
                            signature_parts.append(f"{p}: str")

                    # Add pagination params if perPage exists
                    if "perPage" in all_params:
                        if operation in REVERSE_PAGINATION:
                            signature_parts.append("total_pages: int = 1")
                            signature_parts.append("direction: str = 'prev'")
                        else:
                            signature_parts.append("total_pages: int = 1")
                            signature_parts.append("direction: str = 'next'")
                        if operation == "getNetworkEvents":
                            signature_parts.append("event_log_end_time: Any | None = None")

                    # Add optional params explicitly (stubs need full signatures, not **kwargs)
                    optional_params = return_params(operation, all_params, ["optional"])
                    for p, values in optional_params.items():
                        if p not in defined_params:
                            annotation = _python_type_annotation(values)
                            # Optional params always get = None default
                            signature_parts.append(f"{p}: {annotation} = None")

                    signature = ", ".join(signature_parts)

                    # Write method stub
                    stub_output.write(f"\n    def {operation}({signature}) -> Any: ...\n")
