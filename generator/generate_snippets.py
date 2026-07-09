import os
import sys

import httpx
from jinja2 import Template
import common as common
from parser_v3 import parse_params_v3, clear_cache

CALL_TEMPLATE = Template(
    """import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

API_KEY = 'your-key-here'

dashboard = meraki.DashboardAPI(API_KEY)
{{ parameter_assignments }}
response = dashboard.{{ section }}.{{ operation }}({{ parameters }})

print(response)
"""
)

REVERSE_PAGINATION = ["getNetworkEvents", "getOrganizationConfigurationChanges"]


# Helper function to convert camel case parameter name to snake case
def snakify(param):
    ret = ""
    for s in param:
        if s.islower():
            ret += s
        elif s == "_":
            ret += "_"
        else:
            ret += "_" + s.lower()
    return ret


# Helper function to return parameters within the OASv3 spec, optionally based on
# a list of input filters. Delegates parsing/$ref-resolution/requestBody handling to
# parser_v3.parse_params_v3 (the same parser used by the library/stub generators) so
# snippets stay consistent with generated code. parse_params_v3 applies the filters via
# common.return_params and injects pagination params when perPage is present.
def parse_params(endpoint, path_item, spec, param_filters=None):
    if param_filters is None:
        param_filters = []
    params, _metadata = parse_params_v3(endpoint, path_item, spec, param_filters)
    return params


# Generate text for parameter assignments
def process_assignments(parameters):
    text = "\n"

    for k, v in parameters.items():
        param_name = snakify(k)
        if param_name == "id":
            param_name = "id_"

        if v == "list":
            text += f"{param_name} = []\n"
        elif v == "float":
            text += f"{param_name} = 0.0\n"
        elif v == "int":
            text += f"{param_name} = 0\n"
        elif v == "bool":
            text += f"{param_name} = False\n"
        elif v == "dict":
            text += f"{param_name} = {{}}\n"
        elif v == "str":
            text += f"{param_name} = ''\n"
        else:
            if isinstance(v, str):
                value = f"'{v}'"
            else:
                value = v
            text += f"{param_name} = {value}\n"

    return text


def main():
    # Get the latest OpenAPI v3 specification (version=3 selects OASv3 over the legacy v2 shape)
    spec = httpx.get("https://api.meraki.com/api/v1/openapiSpec", params={"version": 3}).json()

    # Reset parser_v3's $ref cache at entry, matching the library generator
    clear_cache()

    # Supported scopes list will include organizations, networks, devices, and all product types.
    supported_scopes = [
        "administered",
        "organizations",
        "networks",
        "devices",
        "appliance",
        "camera",
        "cellularGateway",
        "insight",
        "sm",
        "switch",
        "wireless",
        "sensor",
        "licensing",
        "secureConnect",
        "wirelessController",
        "campusGateway",
        "spaces",
        "nac",
    ]
    # legacy scopes = ['organizations', 'networks', 'devices',
    #           'appliance', 'camera', 'cellularGateway', 'insight', 'sm', 'switch', 'wireless']
    tags = spec["tags"]
    paths = spec["paths"]
    # Scopes used when generating the library will depend on the provided version of the API spec.
    scopes = {tag["name"]: {} for tag in tags if tag["name"] in supported_scopes}

    # Filter paths to remove the path-level "parameters" key before organize_spec, which
    # expects only HTTP method keys. The original path_item (incl. path-level params) is
    # passed to parse_params_v3 separately via spec["paths"][path].
    filtered_paths = {}
    for path, path_item in paths.items():
        filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

    # Organize data from OpenAPI specification
    operations, scopes = common.organize_spec(filtered_paths, scopes)

    # Generate API libraries
    for scope in scopes:
        print(f"...generating {scope}")
        section = scopes[scope]

        for path, methods in section.items():
            for method, endpoint in methods.items():
                # Get metadata
                tags = endpoint["tags"]
                operation = endpoint["operationId"]

                # Full path_item (incl. path-level parameters) for parse_params_v3
                path_item = spec["paths"][path]

                # An endpoint contributes params if it declares parameters or a requestBody
                has_params = "parameters" in endpoint or "requestBody" in endpoint

                required = {}
                optional = {}

                if has_params:
                    if "perPage" in parse_params(endpoint, path_item, spec):
                        pagination = True
                    else:
                        pagination = False

                    for p, values in parse_params(endpoint, path_item, spec, ["required"]).items():
                        if "example" in values:
                            required[p] = values["example"]
                        elif p == "organizationId":
                            required[p] = "549236"
                        elif p == "networkId":
                            # DevNet Sandbox ALWAYS ON network @ https://n149.meraki.com/o/-t35Mb/manage/organization/overview
                            required[p] = "L_646829496481105433"
                        elif p == "serial":
                            required[p] = "Q2QN-9J8L-SLPD"
                        elif values["type"] == "array":
                            required[p] = "list"
                        elif values["type"] == "number":
                            required[p] = "float"
                        elif values["type"] == "integer":
                            required[p] = "int"
                        elif values["type"] == "boolean":
                            required[p] = "bool"
                        elif values["type"] == "object":
                            required[p] = "dict"
                        elif values["type"] == "string":
                            required[p] = "str"
                        else:
                            sys.exit(f"Unhandled param type for {p}: {values}")

                    if pagination:
                        if operation not in REVERSE_PAGINATION:
                            optional["total_pages"] = "all"
                        else:
                            optional["total_pages"] = 3

                    for p, values in parse_params(endpoint, path_item, spec, ["optional"]).items():
                        if "example" in values:
                            optional[p] = values["example"]

                if operation == "createNetworkGroupPolicy":
                    print(required)
                    print(optional)

                if "code_snippets" not in os.listdir():
                    os.mkdir("code_snippets")

                with open(f"code_snippets/{operation}.py", "w", encoding="utf-8") as fp:
                    if required.items():
                        parameters_text = "\n    "
                        for k, v in required.items():
                            param_name = snakify(k)
                            if param_name == "id":
                                param_name = "id_"
                            parameters_text += f"{param_name}, "
                        for k, v in optional.items():
                            if k == "total_pages" and v == "all":
                                parameters_text += "total_pages='all'"
                            elif k == "total_pages" and v == 1:
                                parameters_text += "total_pages=1"
                            elif isinstance(v, str):
                                parameters_text += f"\n    {k}='{v}', "
                            else:
                                parameters_text += f"\n    {k}={v}, "
                        if parameters_text[-2:] == ", ":
                            parameters_text = parameters_text[:-2]
                        parameters_text += "\n"
                    else:
                        parameters_text = ""

                    fp.write(
                        CALL_TEMPLATE.render(
                            parameter_assignments=process_assignments(required),
                            section=scope,
                            operation=operation,
                            parameters=parameters_text,
                        )
                    )


if __name__ == "__main__":
    main()
