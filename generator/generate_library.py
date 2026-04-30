import getopt
import json
import os
import re
import subprocess
import sys

import jinja2
import requests

import common as common
from parser_v3 import parse_params_v3, clear_cache
from generate_library_oasv2 import (
    REVERSE_PAGINATION,
    docs_url,
    check_python_version,
    return_params,
)
from generate_stubs import generate_stub_modules

READ_ME = """
=== PREREQUISITES ===
Include the jinja2 files in same directory as this script, and install Python requests
pip[3] install requests

=== DESCRIPTION ===
This script generates the Meraki Python library from the OpenAPI v3 specification.

=== USAGE ===
python[3] generate_library_v3.py [-o <org_id>] [-k <api_key>] [-v <version_number>] [-a <api_version_number>] [-g <is_called_from_github_action>] [-s]

-s generates .pyi type stub files for static analysis

API key can, and is recommended to, be set as an environment variable named MERAKI_DASHBOARD_API_KEY."""


def generate_library(
    spec: dict, version_number: str, api_version_number: str, is_github_action: bool, generate_stubs: bool = False
):
    # Clear parser cache at entry
    clear_cache()

    # Supported scopes list will include organizations, networks, devices, and all product types.
    supported_scopes = [
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
        "administered",
        "licensing",
        "secureConnect",
        "wirelessController",
        "campusGateway",
        "spaces",
        "nac",
    ]

    tags = spec["tags"]
    paths = spec["paths"]
    scopes = {tag["name"]: {} for tag in tags if tag["name"] in supported_scopes}

    batchable_actions = spec["x-batchable-actions"]

    # Set template_dir if a GitHub action is invoking it
    if is_github_action:
        template_dir = "generator/"
    else:
        template_dir = ""

    # Check paths and create directories if needed
    directories = [
        "meraki",
        "meraki/api",
        "meraki/api/batch",
        "meraki/aio",
        "meraki/aio/api",
    ]
    for directory in directories:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    # Files that are not generated
    non_generated = [
        "__init__.py",
        "_version.py",
        "config.py",
        "common.py",
        "exceptions.py",
        "response_handler.py",
        "rest_session.py",
        "api/__init__.py",
        "aio/__init__.py",
        "aio/rest_session.py",
        "aio/api/__init__.py",
        "api/batch/__init__.py",
    ]
    base_url = "https://raw.githubusercontent.com/meraki/dashboard-api-python/master/meraki/"
    for file in non_generated:
        response = requests.get(f"{base_url}{file}")
        with open(f"meraki/{file}", "w+", encoding="utf-8", newline=None) as fp:
            contents = response.text
            if file == "_version.py":
                # replace library version
                start = contents.find("__version__ = ")
                end = contents.find("\n", start)
                contents = f"{contents[:start]}__version__ = '{version_number}'{contents[end:]}"
            elif file == "__init__.py":
                start = contents.find("__api_version__ = ")
                end = contents.find("\n", start)
                contents = f"{contents[:start]}__api_version__ = '{api_version_number}'{contents[end:]}"
            fp.write(contents)

    # Filter paths to remove "parameters" key before passing to organize_spec
    # organize_spec expects only HTTP method keys (get, post, put, delete)
    filtered_paths = {}
    for path, path_item in paths.items():
        filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

    # Organize data from OpenAPI specification
    operations, scopes = common.organize_spec(filtered_paths, scopes)

    # Inform the user how many operations were found
    print(f"Total of {len(operations)} endpoints found from OpenAPI spec...")

    # Generate API libraries
    jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    jinja_env.filters["to_double_quote_list"] = lambda lst: json.dumps(lst)

    # Iterate through the scopes creating standard, asyncio and batch modules for each
    generate_modules(spec, batchable_actions, jinja_env, scopes, template_dir)

    # Generate type stubs if requested
    if generate_stubs:
        print("Generating .pyi type stubs...")
        generate_stub_modules(spec, scopes, jinja_env, template_dir)
        # Write py.typed marker for PEP 561
        open("meraki/py.typed", "w").close()
        print("Type stubs and py.typed marker created.")

    # Format generated code with ruff
    print("Formatting generated code with ruff...")
    subprocess.run(["ruff", "check", "--fix", "--quiet", "meraki/"], check=False)
    subprocess.run(["ruff", "format", "--quiet", "meraki/"], check=False)


def generate_modules(spec, batchable_actions, jinja_env, scopes, template_dir):
    for scope in scopes:
        print(f"...generating {scope}")
        section = scopes[scope]

        # Generate the standard module
        with open(f"meraki/api/{scope}.py", "w", encoding="utf-8", newline=None) as output:
            # Open module file for Asyncio API libraries
            async_output = open(f"meraki/aio/api/{scope}.py", "w", encoding="utf-8", newline=None)
            # Open module file for Action Batch API libraries
            batch_output = open(f"meraki/api/batch/{scope}.py", "w", encoding="utf-8", newline=None)

            modules = [
                {"template_name": "class_template.jinja2", "module_output": output},
                {
                    "template_name": "async_class_template.jinja2",
                    "module_output": async_output,
                },
                {
                    "template_name": "batch_class_template.jinja2",
                    "module_output": batch_output,
                },
            ]

            # Generate modules
            for module in modules:
                render_class_template(
                    jinja_env,
                    template_dir,
                    module["template_name"],
                    module["module_output"],
                    scope,
                )

            # Generate API & Asyncio API functions
            generate_standard_and_async_functions(jinja_env, template_dir, section, output, async_output, spec)

            # Generate API action batch functions
            generate_action_batch_functions(
                jinja_env,
                template_dir,
                section,
                batch_output,
                batchable_actions,
                spec,
            )


def render_class_template(
    jinja_env: jinja2.Environment,
    template_dir: str,
    template_name: str,
    output: open,
    scope: str,
):
    with open(f"{template_dir}{template_name}", encoding="utf-8", newline=None) as fp:
        class_template = fp.read()
        template = jinja_env.from_string(class_template)
        output.write(
            template.render(
                class_name=scope[0].upper() + scope[1:],
            )
        )


def generate_standard_and_async_functions(
    jinja_env: jinja2.Environment,
    template_dir: str,
    section: dict,
    output: open,
    async_output: open,
    spec: dict,
):
    for path, methods in section.items():
        for method, endpoint in methods.items():
            # Get metadata
            tags = endpoint["tags"]
            operation = endpoint["operationId"]
            description = endpoint.get("summary", endpoint.get("description", ""))

            # Get path_item from spec for parse_params_v3
            path_item = spec["paths"][path]

            # Parse params using v3 parser
            all_params, metadata = parse_params_v3(endpoint, path_item, spec)

            # Function definition
            definition = ""
            defined_params = set()

            # Add required params to definition
            for p, values in return_params(operation, all_params, ["required"]).items():
                defined_params.add(p)
                if values["type"] == "array":
                    definition += f", {p}: list"
                elif values["type"] == "number":
                    definition += f", {p}: float"
                elif values["type"] == "integer":
                    definition += f", {p}: int"
                elif values["type"] == "boolean":
                    definition += f", {p}: bool"
                elif values["type"] == "object":
                    definition += f", {p}: dict"
                elif values["type"] == "string":
                    definition += f", {p}: str"

            # Path params must be in the signature for URL construction
            for p, values in return_params(operation, all_params, ["path"]).items():
                if p not in defined_params:
                    defined_params.add(p)
                    if values["type"] == "array":
                        definition += f", {p}: list"
                    elif values["type"] == "number":
                        definition += f", {p}: float"
                    elif values["type"] == "integer":
                        definition += f", {p}: int"
                    elif values["type"] == "boolean":
                        definition += f", {p}: bool"
                    elif values["type"] == "object":
                        definition += f", {p}: dict"
                    elif values["type"] == "string":
                        definition += f", {p}: str"

            # Catch params referenced in the URL but not declared as path params
            for p in re.findall(r"\{(\w+)\}", path):
                if p not in defined_params:
                    defined_params.add(p)
                    definition += f", {p}: str"

            # Add pagination params if perPage exists
            if "perPage" in all_params:
                if operation in REVERSE_PAGINATION:
                    definition += ", total_pages=1, direction='prev'"
                else:
                    definition += ", total_pages=1, direction='next'"
                if operation == "getNetworkEvents":
                    definition += ", event_log_end_time=None"

            # Function body for GET endpoints
            query_params = array_params = body_params = path_params = {}
            if method == "get":
                query_params = return_params(operation, all_params, ["query"])
                array_params = return_params(operation, all_params, ["array"])
                path_params = return_params(operation, all_params, ["path"])

            # Function body for POST/PUT endpoints
            elif method == "post" or method == "put":
                body_params = return_params(operation, all_params, ["body"])
                path_params = return_params(operation, all_params, ["path"])

            # Function body for DELETE endpoints
            elif method == "delete":
                query_params = return_params(operation, all_params, ["query"])
                path_params = return_params(operation, all_params, ["path"])

            # Add **kwargs if optional params OR body/query/array params exist (templates use kwargs.items())
            if return_params(operation, all_params, ["optional"]) or body_params or query_params or array_params:
                definition += ", **kwargs"

            # Docstring
            param_descriptions = list()
            all_params_for_doc = return_params(operation, all_params, ["required", "pagination", "optional"])
            if all_params_for_doc:
                for p, values in all_params_for_doc.items():
                    param_descriptions.append(f"{p} ({values['type']}): {values['description']}")

            kwarg_line = ""
            if return_params(operation, all_params, ["optional"]):
                kwarg_line = "kwargs.update(locals())"
            elif return_params(operation, all_params, ["query", "array", "body"]):
                kwarg_line = "kwargs = locals()"

            # Assert valid values for enum
            enum_params = return_params(operation, all_params, ["enum"])
            assert_blocks = list()
            if enum_params:
                for p, values in enum_params.items():
                    assert_blocks.append((p, values["enum"]))

            # Generate call_line based on method
            if method == "get":
                pagination_params = return_params(operation, all_params, ["pagination"])
                if query_params or array_params:
                    if pagination_params:
                        if operation == "getNetworkEvents":
                            call_line = "return self._session.get_pages(metadata, resource, params, total_pages, direction, event_log_end_time)"
                        else:
                            call_line = "return self._session.get_pages(metadata, resource, params, total_pages, direction)"
                    else:
                        call_line = "return self._session.get(metadata, resource, params)"
                else:
                    call_line = "return self._session.get(metadata, resource)"

            elif method == "post" or method == "put":
                if body_params:
                    call_line = f"return self._session.{method}(metadata, resource, payload)"
                else:
                    call_line = f"return self._session.{method}(metadata, resource)"

            elif method == "delete":
                if query_params:
                    call_line = "return self._session.delete(metadata, resource, params)"
                else:
                    call_line = "return self._session.delete(metadata, resource)"

            # Ensure all URL-referenced params get quote lines in the template
            for p in re.findall(r"\{(\w+)\}", path):
                if p not in path_params:
                    path_params[p] = {"type": "string", "in": "path"}

            # Add function to files
            with open(
                f"{template_dir}function_template.jinja2",
                encoding="utf-8",
                newline=None,
            ) as fp:
                function_template = fp.read()
                template = jinja_env.from_string(function_template)
                rendered = template.render(
                    operation=operation,
                    function_definition=definition,
                    description=description,
                    doc_url=docs_url(operation),
                    descriptions=param_descriptions,
                    kwarg_line=kwarg_line,
                    all_params=list(all_params_for_doc.keys()) if all_params_for_doc else [],
                    assert_blocks=assert_blocks,
                    tags=tags,
                    resource=path,
                    query_params=query_params,
                    array_params=array_params,
                    body_params=body_params,
                    path_params=path_params,
                    call_line=call_line,
                )
                output.write("\n\n" + rendered)
                async_output.write("\n\n" + rendered)


def generate_action_batch_functions(
    jinja_env: jinja2.Environment,
    template_dir: str,
    section: dict,
    batch_output: open,
    batchable_actions: list,
    spec: dict,
):
    # Build list of batchable action summaries for matching
    batchable_action_summaries = [action["summary"] for action in batchable_actions]

    for path, methods in section.items():
        for method, endpoint in methods.items():
            # Match by description OR summary (v3 inconsistency)
            endpoint_desc = endpoint.get("description", "")
            endpoint_summary = endpoint.get("summary", "")

            if endpoint_desc in batchable_action_summaries or endpoint_summary in batchable_action_summaries:
                # Get metadata
                tags = endpoint["tags"]
                operation = endpoint["operationId"]
                description = endpoint.get("description", endpoint_summary)
                summary = endpoint.get("summary", endpoint_desc)

                # Find matching action
                this_action = None
                for action in batchable_actions:
                    if action["summary"] == description or action["summary"] == summary:
                        this_action = action
                        break

                if not this_action:
                    continue

                batch_operation = this_action["operation"]

                # Get path_item from spec for parse_params_v3
                path_item = spec["paths"][path]

                # Parse params using v3 parser
                all_params, metadata = parse_params_v3(endpoint, path_item, spec)

                # Initialize param collections
                query_params = array_params = body_params = {}
                path_params = return_params(operation, all_params, ["path"])

                # Ensure all URL-referenced params get quote lines in the template
                for p in re.findall(r"\{(\w+)\}", path):
                    if p not in path_params:
                        path_params[p] = {"type": "string", "in": "path"}

                # Function definition
                definition = ""
                defined_params = set()

                for p, values in return_params(operation, all_params, ["required"]).items():
                    defined_params.add(p)
                    # Match OAS schema types to Python types
                    match values["type"]:
                        case "array":
                            definition += f", {p}: list"
                        case "number":
                            definition += f", {p}: float"
                        case "integer":
                            definition += f", {p}: int"
                        case "boolean":
                            definition += f", {p}: bool"
                        case "object":
                            definition += f", {p}: dict"
                        case "string":
                            definition += f", {p}: str"

                # Path params must be in the signature for URL construction
                for p, values in return_params(operation, all_params, ["path"]).items():
                    if p not in defined_params:
                        defined_params.add(p)
                        match values["type"]:
                            case "array":
                                definition += f", {p}: list"
                            case "number":
                                definition += f", {p}: float"
                            case "integer":
                                definition += f", {p}: int"
                            case "boolean":
                                definition += f", {p}: bool"
                            case "object":
                                definition += f", {p}: dict"
                            case "string":
                                definition += f", {p}: str"

                # Catch params referenced in the URL but not declared as path params
                for p in re.findall(r"\{(\w+)\}", path):
                    if p not in defined_params:
                        defined_params.add(p)
                        definition += f", {p}: str"

                # Add pagination params if perPage exists
                if "perPage" in all_params:
                    if operation in REVERSE_PAGINATION:
                        definition += ", total_pages=1, direction='prev'"
                    else:
                        definition += ", total_pages=1, direction='next'"
                    if operation == "getNetworkEvents":
                        definition += ", event_log_end_time=None"

                # Function body for POST/PUT endpoints
                if method == "post" or method == "put":
                    body_params = return_params(operation, all_params, ["body"])

                # Add **kwargs if optional params OR body params exist (batch template uses kwargs.items())
                if return_params(operation, all_params, ["optional"]) or body_params:
                    definition += ", **kwargs"

                # Docstring
                param_descriptions = list()
                all_params_for_doc = return_params(operation, all_params, ["required", "pagination", "optional"])
                if all_params_for_doc:
                    for p, values in all_params_for_doc.items():
                        param_descriptions.append(f"{p} ({values['type']}): {values['description']}")

                kwarg_line = ""
                if return_params(operation, all_params, ["optional"]):
                    kwarg_line = "kwargs.update(locals())"
                elif return_params(operation, all_params, ["body"]):
                    kwarg_line = "kwargs = locals()"

                # Assert valid values for enum
                enum_params = return_params(operation, all_params, ["enum"])
                assert_blocks = list()
                if enum_params:
                    for p, values in enum_params.items():
                        assert_blocks.append((p, values["enum"]))

                # Function return statement
                call_line = "return action"

                # Add function to files
                with open(
                    f"{template_dir}batch_function_template.jinja2",
                    encoding="utf-8",
                    newline=None,
                ) as fp:
                    function_template = fp.read()
                    template = jinja_env.from_string(function_template)
                    batch_output.write(
                        "\n\n"
                        + template.render(
                            operation=operation,
                            function_definition=definition,
                            description=description,
                            doc_url=docs_url(operation),
                            descriptions=param_descriptions,
                            kwarg_line=kwarg_line,
                            all_params=list(all_params_for_doc.keys()) if all_params_for_doc else [],
                            assert_blocks=assert_blocks,
                            tags=tags,
                            resource=path,
                            query_params=query_params,
                            array_params=array_params,
                            body_params=body_params,
                            path_params=path_params,
                            call_line=call_line,
                            batch_operation=batch_operation,
                        )
                    )


# Prints a READ_ME help message for user to read
def print_help():
    lines = READ_ME.split("\n")
    for line in lines:
        print(f"# {line}")


# Parse command line arguments
def main(inputs):
    api_key = os.environ.get("MERAKI_DASHBOARD_API_KEY")
    org_id = None
    version_number = "custom"
    api_version_number = "custom"
    is_github_action = False
    generate_stubs_flag = False

    try:
        opts, args = getopt.getopt(inputs, "ho:k:v:a:g:s")
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print_help()
            sys.exit(2)
        elif opt == "-o":
            org_id = arg
        elif opt == "-k" and api_key is None:
            api_key = arg
        elif opt == "-v":
            version_number = arg
        elif opt == "-a":
            api_version_number = arg
        elif opt == "-g":
            if arg.lower() == "true":
                is_github_action = True
        elif opt == "-s":
            generate_stubs_flag = True

    check_python_version()

    # Retrieve the latest OpenAPI v3 specification
    if org_id:
        if not api_key:
            print_help()
            sys.exit(2)
        else:
            response = requests.get(
                f"https://api.meraki.com/api/v1/organizations/{org_id}/openapiSpec",
                headers={"Authorization": f"Bearer {api_key}"},
                params={"version": 3},
            )
            if response.ok:
                spec = response.json()
            else:
                print_help()
                sys.exit(f"API key provided does not have access to org {org_id}")
    else:
        response = requests.get("https://api.meraki.com/api/v1/openapiSpec", params={"version": 3})
        if response.ok:
            spec = response.json()
            print("Successfully pulled Meraki dashboard API OpenAPI v3 spec.")
        else:
            print_help()
            sys.exit(
                "There was an HTTP error pulling the OpenAPI v3 specification. Please try again in a few minutes. "
                "If this continues for more than an hour, please contact Meraki support."
            )

    generate_library(spec, version_number, api_version_number, is_github_action, generate_stubs=generate_stubs_flag)


if __name__ == "__main__":
    main(sys.argv[1:])
