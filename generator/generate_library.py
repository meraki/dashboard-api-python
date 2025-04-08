import getopt
import os
import platform
import sys

import jinja2
import requests

READ_ME = """
=== PREREQUISITES ===
Include the jinja2 files in same directory as this script, and install Python requests
pip[3] install requests 

=== DESCRIPTION ===
This script generates the Meraki Python library using either the public OpenAPI specification, or, with an API key & org
ID as inputs, a specific dashboard org's OpenAPI spec.

=== USAGE === python[3] generate_library.py [-o <org_id>] [-k <api_key>] [-v <version_number>] [-av 
<api_version_number>] [-g <is_called_from_github_action>] 

API key can, and is recommended to, be set as an environment variable named MERAKI_DASHBOARD_API_KEY."""

REVERSE_PAGINATION = ["getNetworkEvents", "getOrganizationConfigurationChanges"]


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


def check_python_version():
    # Check minimum Python version
    version_warning_string = (
        f"This library generator requires Python 3.10 at minimum. "
        f"Your interpreter version is: {platform.python_version()}. "
        f"Please consult the readme at your convenience: "
        f"https://github.com/meraki/dashboard-api-python/blob/main/generator/readme.md "
        f"Additional details: "
        f"python_version_tuple()[0] = {platform.python_version_tuple()[0]}; "
        f"python_version_tuple()[1] = {platform.python_version_tuple()[1]} "
    )

    if not (
        int(platform.python_version_tuple()[0]) == 3
        and int(platform.python_version_tuple()[1]) >= 10
    ):
        sys.exit(version_warning_string)


# Returns full link to endpoint's documentation on Developer Hub
# Note: updates to the documentation site may impact these URLs.
def docs_url(operation: str):
    base_url = "https://developer.cisco.com/meraki/api-v1/#!"
    ret = ""
    for letter in operation:
        if letter.islower():
            ret += letter
        else:
            ret += f"-{letter.lower()}"
    return base_url + ret


# Helper function to return the right params; used in parse_params
def return_params(operation: str, params: dict, param_filters):
    # Return parameters based on matching input filters
    if not param_filters:
        return params
    else:
        ret = {}
        if "required" in param_filters:
            ret.update(
                {k: v for k, v in params.items() if "required" in v and v["required"]}
            )
        if "pagination" in param_filters:
            ret.update(
                generate_pagination_parameters(operation) if "perPage" in params else {}
            )
        if "optional" in param_filters:
            ret.update(
                {
                    k: v
                    for k, v in params.items()
                    if "required" in v and not v["required"]
                }
            )
        if "path" in param_filters:
            ret.update(
                {k: v for k, v in params.items() if "in" in v and v["in"] == "path"}
            )
        if "query" in param_filters:
            ret.update(
                {k: v for k, v in params.items() if "in" in v and v["in"] == "query"}
            )
        if "body" in param_filters:
            ret.update(
                {k: v for k, v in params.items() if "in" in v and v["in"] == "body"}
            )
        if "array" in param_filters:
            ret.update(
                {k: v for k, v in params.items() if "in" in v and v["type"] == "array"}
            )
        if "enum" in param_filters:
            ret.update({k: v for k, v in params.items() if "enum" in v})
        return ret


def unpack_param_without_schema(
    all_params: dict, this_param: dict, name: str, is_required: bool
):
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


def unpack_param_with_schema(all_params: dict, this_param: dict):
    # the parameter will have a top-level object 'schema' and within that, 'properties' in OASv2
    # in OASv3, the parameter will only have this for query and path parameters, and requestBody params
    # will be in a separate key
    keys = this_param["schema"]["properties"]

    # parse the properties and assign types and descriptions
    for k in keys:
        # if required, set required true
        if "required" in this_param["schema"] and k in this_param["schema"]["required"]:
            all_params[k] = {"required": True}
        else:
            all_params[k] = {"required": False}

        # identify whether the parameter is in the path or query, or for OASv2, in the body
        all_params[k]["in"] = this_param["in"]

        # assign the right data type/description to the parameter per the schema
        for attribute in ("type", "description"):
            all_params[k][attribute] = keys[k][attribute]

        # capture schema enum if available
        if "enum" in keys[k]:
            all_params[k]["enum"] = keys[k]["enum"]

        # capture schema example if available
        if "example" in this_param["schema"] and k in this_param["schema"]["example"]:
            all_params[k]["example"] = this_param["schema"]["example"][k]

    return all_params


def unpack_params(operation: str, parameters: dict, param_filters):
    # Create dict with information on endpoint's parameters
    unpacked_params = dict()

    # Iterate through the endpoint's parameters
    for p in parameters:
        # Name the parameter
        name = p["name"]

        # Consult the schema if there is one
        if "schema" in p:
            unpacked_params.update(unpack_param_with_schema(unpacked_params, p))

        # If there is no schema, then consult the required attribute if it exists
        elif "required" in p and p["required"]:
            unpacked_params.update(
                unpack_param_without_schema(unpacked_params, p, name, True)
            )

        # Otherwise the parameter is not required
        else:
            unpacked_params.update(
                unpack_param_without_schema(unpacked_params, p, name, False)
            )

    # Add custom library parameters to handle pagination
    if "perPage" in unpacked_params:
        unpacked_params.update(generate_pagination_parameters(operation))

    # Return parameters based on matching input filters
    return return_params(operation, unpacked_params, param_filters)


# Helper function to return parameters within OAS spec, optionally based on list of input filters
def parse_params(operation: str, parameters: dict, param_filters=None):
    if param_filters is None:
        param_filters = list()
    if parameters is None:
        return {}

    return unpack_params(operation, parameters, param_filters)


def generate_library(spec: dict, version_number: str, api_version_number: str, is_github_action: bool):
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
        "campusGateway"
    ]
    # legacy scopes = ['organizations', 'networks', 'devices', 'appliance', 'camera', 'cellularGateway', 'insight',
    #                  'sm', 'switch', 'wireless']
    tags = spec["tags"]
    paths = spec["paths"]
    # Scopes used when generating the library will depend on the provided version of the API spec.
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
        "meraki/api/batch",
    ]
    for directory in directories:
        if not os.path.isdir(directory):
            os.mkdir(directory)

    # Files that are not generated
    non_generated = [
        "__init__.py",
        "config.py",
        "common.py",
        "exceptions.py",
        "rest_session.py",
        "api/__init__.py",
        "aio/__init__.py",
        "aio/rest_session.py",
        "aio/api/__init__.py",
        "api/batch/__init__.py",
    ]
    base_url = (
        "https://raw.githubusercontent.com/meraki/dashboard-api-python/master/meraki/"
    )
    for file in non_generated:
        response = requests.get(f"{base_url}{file}")
        with open(f"meraki/{file}", "w+", encoding="utf-8", newline=None) as fp:
            contents = response.text
            if file == "__init__.py":
                # replace library version
                start = contents.find("__version__ = ")
                end = contents.find("\n", start)
                contents = f"{contents[:start]}__version__ = '{version_number}'{contents[end:]}"
                # replace API version
                start = contents.find("__api_version__ = ")
                end = contents.find("\n", start)
                contents = f"{contents[:start]}__api_version__ = '{api_version_number}'{contents[end:]}"
            fp.write(contents)

    # Organize data from OpenAPI specification
    operations = list()  # list of operation IDs
    for path, methods in paths.items():
        # method is the HTTP action, e.g. get, put, etc.
        for method in methods:
            # endpoint is the method for that specific path
            endpoint = paths[path][method]

            # the endpoint has tags
            tags = endpoint["tags"]

            # the endpoint has an operationId
            operation = endpoint["operationId"]

            # add the operation ID to the list
            operations.append(operation)

            # the endpoint has a scope defined by the first tag
            scope = tags[0]

            # Needs documentation
            if path not in scopes[scope]:
                scopes[scope][path] = {method: endpoint}
            # Needs documentation
            else:
                scopes[scope][path][method] = endpoint

    # Inform the user of the number of operations found
    print(f"Total of {len(operations)} endpoints found from OpenAPI spec...")

    # Generate API libraries
    # We will use newline=None to ensure that line breaks are handled correctly, especially when generating
    # on Windows and using `git autocrlf true`
    jinja_env = jinja2.Environment(
        trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True
    )

    # Iterate through the scopes creating standard, asyncio and batch modules for each
    generate_modules(batchable_actions, jinja_env, scopes, template_dir)


def generate_modules(batchable_actions, jinja_env, scopes, template_dir):
    for scope in scopes:
        print(f"...generating {scope}")
        section = scopes[scope]

        # Generate the standard module
        with open(
            f"meraki/api/{scope}.py", "w", encoding="utf-8", newline=None
        ) as output:
            # Open module file for Asyncio API libraries
            async_output = open(
                f"meraki/aio/api/{scope}.py", "w", encoding="utf-8", newline=None
            )
            # Open module file for Action Batch API libraries
            batch_output = open(
                f"meraki/api/batch/{scope}.py", "w", encoding="utf-8", newline=None
            )

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
            generate_standard_and_async_functions(
                jinja_env, template_dir, section, output, async_output
            )

            # Generate API action batch functions
            generate_action_batch_functions(
                jinja_env,
                template_dir,
                section,
                batch_output,
                batchable_actions,
            )


def generate_standard_and_async_functions(
    jinja_env: jinja2.Environment,
    template_dir: str,
    section: dict,
    output: open,
    async_output: open,
):
    for path, methods in section.items():
        for method, endpoint in methods.items():
            # Get metadata
            tags = endpoint["tags"]
            operation = endpoint["operationId"]
            description = endpoint["summary"]

            # will need updating for OASv3
            parameters = endpoint["parameters"] if "parameters" in endpoint else None

            # Function definition
            definition = ""
            if parameters:
                for p, values in parse_params(
                    operation, parameters, "required"
                ).items():
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

                if "perPage" in parse_params(operation, parameters):
                    if operation in REVERSE_PAGINATION:
                        definition += ", total_pages=1, direction='prev'"
                    else:
                        definition += ", total_pages=1, direction='next'"
                    if operation == "getNetworkEvents":
                        definition += ", event_log_end_time=None"

                if parse_params(operation, parameters, ["optional"]):
                    definition += ", **kwargs"

            # Docstring
            param_descriptions = list()
            all_params = parse_params(
                operation, parameters, ["required", "pagination", "optional"]
            )
            if all_params:
                for p, values in all_params.items():
                    param_descriptions.append(
                        f'{p} ({values["type"]}): {values["description"]}'
                    )

            # Combine keyword args with locals
            kwarg_line = ""
            if parse_params(operation, parameters, ["optional"]):
                kwarg_line = "kwargs.update(locals())"
            elif parse_params(operation, parameters, ["query", "array", "body"]):
                kwarg_line = "kwargs = locals()"

            # Assert valid values for enum
            enum_params = parse_params(operation, parameters, ["enum"])
            assert_blocks = list()
            if enum_params:
                for p, values in enum_params.items():
                    assert_blocks.append((p, values["enum"]))

            # Function body for GET endpoints
            query_params = array_params = body_params = path_params = {}
            if method == "get":
                array_params, call_line, path_params, query_params = parse_get_params(
                    operation, parameters
                )

            # Function body for POST/PUT endpoints
            elif method == "post" or method == "put":
                body_params, call_line, path_params = parse_post_and_put_params(
                    method, operation, parameters
                )

            # Function body for DELETE endpoints
            elif method == "delete":
                call_line, path_params, query_params = parse_delete_params(operation, parameters)

            # Add function to files
            with open(
                f"{template_dir}function_template.jinja2",
                encoding="utf-8",
                newline=None,
            ) as fp:
                function_template = fp.read()
                template = jinja_env.from_string(function_template)
                output.write(
                    "\n\n"
                    + template.render(
                        operation=operation,
                        function_definition=definition,
                        description=description,
                        doc_url=docs_url(operation),
                        descriptions=param_descriptions,
                        kwarg_line=kwarg_line,
                        all_params=list(all_params.keys()),
                        assert_blocks=assert_blocks,
                        tags=tags,
                        resource=path,
                        query_params=query_params,
                        array_params=array_params,
                        body_params=body_params,
                        path_params=path_params,
                        call_line=call_line,
                    )
                )
                async_output.write(
                    "\n\n"
                    + template.render(
                        operation=operation,
                        function_definition=definition,
                        description=description,
                        doc_url=docs_url(operation),
                        descriptions=param_descriptions,
                        kwarg_line=kwarg_line,
                        all_params=list(all_params.keys()),
                        assert_blocks=assert_blocks,
                        tags=tags,
                        resource=path,
                        query_params=query_params,
                        array_params=array_params,
                        body_params=body_params,
                        path_params=path_params,
                        call_line=call_line,
                    )
                )


def parse_get_params(operation: str, parameters: dict):
    query_params = parse_params(operation, parameters, "query")
    array_params = parse_params(operation, parameters, "array")
    path_params = parse_params(operation, parameters, "path")
    pagination_params = parse_params(operation, parameters, "pagination")
    if query_params or array_params:
        if pagination_params:
            if operation == "getNetworkEvents":
                call_line = (
                    "return self._session.get_pages(metadata, resource, params, "
                    "total_pages, direction, event_log_end_time)"
                )
            else:
                call_line = (
                    "return self._session.get_pages(metadata, resource, params, "
                    "total_pages, direction)"
                )
        else:
            call_line = "return self._session.get(metadata, resource, params)"
    else:
        call_line = "return self._session.get(metadata, resource)"
    return array_params, call_line, path_params, query_params


def parse_post_and_put_params(method: str, operation: str, parameters: dict):
    body_params = parse_params(operation, parameters, "body")
    path_params = parse_params(operation, parameters, "path")
    if body_params:
        call_line = f"return self._session.{method}(metadata, resource, payload)"
    else:
        call_line = f"return self._session.{method}(metadata, resource)"
    return body_params, call_line, path_params


def parse_delete_params(operation: str, parameters: dict):
    query_params = parse_params(operation, parameters, "query")
    path_params = parse_params(operation, parameters, "path")

    if query_params:
        call_line = "return self._session.delete(metadata, resource, params)"
    else:
        call_line = "return self._session.delete(metadata, resource)"
    return call_line, path_params, query_params


def generate_action_batch_functions(
    jinja_env: jinja2.Environment,
    template_dir: str,
    section: dict,
    batch_output: open,
    batchable_actions: list,
):
    for path, methods in section.items():
        for method, endpoint in methods.items():
            batchable_action_summaries = [
                action["summary"] for action in batchable_actions
            ]
            if endpoint["description"] in batchable_action_summaries:
                # Get metadata
                tags = endpoint["tags"]
                operation = endpoint["operationId"]
                description = endpoint["description"]
                summary = endpoint["summary"]

                this_action = [
                    action
                    for action in batchable_actions
                    if action["summary"] == description or action["summary"] == summary
                ][0]

                batch_operation = this_action["operation"]

                # May need update for OASv3
                parameters = (
                    endpoint["parameters"] if "parameters" in endpoint else None
                )

                # Function body for GET endpoints
                query_params = array_params = body_params = {}

                # Function body for POST/PUT endpoints
                if method == "post" or method == "put":
                    # will need update for OASv3
                    body_params = parse_params(operation, parameters, "body")

                # Function body for DELETE endpoints is empty (HTTP 204)

                # Function definition
                definition = ""
                if parameters:
                    for p, values in parse_params(
                        operation, parameters, "required"
                    ).items():
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

                    if "perPage" in parse_params(operation, parameters):
                        if operation in REVERSE_PAGINATION:
                            definition += ", total_pages=1, direction='prev'"
                        else:
                            definition += ", total_pages=1, direction='next'"
                        if operation == "getNetworkEvents":
                            definition += ", event_log_end_time=None"

                    if parse_params(operation, parameters, ["optional"]):
                        definition += f", **kwargs"

                # Docstring
                param_descriptions = list()
                all_params = parse_params(
                    operation, parameters, ["required", "pagination", "optional"]
                )
                if all_params:
                    for p, values in all_params.items():
                        param_descriptions.append(
                            f'{p} ({values["type"]}): {values["description"]}'
                        )

                # Combine keyword args with locals
                kwarg_line = ""
                if parse_params(operation, parameters, ["optional"]):
                    kwarg_line = "kwargs.update(locals())"

                # will need update for OASv3
                elif parse_params(operation, parameters, ["query", "array", "body"]):
                    kwarg_line = "kwargs = locals()"

                # Assert valid values for enum
                enum_params = parse_params(operation, parameters, ["enum"])
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
                            all_params=list(all_params.keys()),
                            assert_blocks=assert_blocks,
                            tags=tags,
                            resource=path,
                            query_params=query_params,
                            array_params=array_params,
                            body_params=body_params,
                            call_line=call_line,
                            batch_operation=batch_operation,
                        )
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


# Prints READ_ME help message for user to read
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

    try:
        opts, args = getopt.getopt(inputs, "ho:k:v:av:g:")
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
        elif opt == "-av":
            api_version_number = arg
        elif opt == "-g":
            if arg.lower() == "true":
                is_github_action = True

    check_python_version()

    # Retrieve latest OpenAPI specification
    if org_id:
        if not api_key:
            print_help()
            sys.exit(2)
        else:
            response = requests.get(
                f"https://api.meraki.com/api/v1/organizations/{org_id}/openapiSpec",
                headers={"Authorization": f"Bearer {api_key}"},
            )
            if response.ok:
                spec = response.json()
            else:
                print_help()
                sys.exit(f"API key provided does not have access to org {org_id}")
    else:
        response = requests.get("https://api.meraki.com/api/v1/openapiSpec")
        # Validate that the spec pulled successfully before trying to generate the library.
        if response.ok:
            spec = response.json()
            print(f"Successfully pulled Meraki dashboard API OpenAPI spec.")
        else:
            print_help()
            sys.exit(
                f"There was an HTTP error pulling the OpenAPI specification. Please try again in a few minutes. "
                f"If this continues for more than an hour, please contact Meraki support and mention that "
                f'"HTTP GET https://api.meraki.com/api/v1/openapiSpec" is failing.'
            )

    generate_library(spec, version_number, api_version_number, is_github_action)


if __name__ == "__main__":
    main(sys.argv[1:])
