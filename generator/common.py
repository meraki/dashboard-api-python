import platform
import sys


REVERSE_PAGINATION = ["getNetworkEvents", "getOrganizationConfigurationChanges"]


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
    version_warning_string = (
        f"This library generator requires Python 3.10 at minimum. "
        f"Your interpreter version is: {platform.python_version()}. "
        f"Please consult the readme at your convenience: "
        f"https://github.com/meraki/dashboard-api-python/blob/main/generator/readme.md "
        f"Additional details: "
        f"python_version_tuple()[0] = {platform.python_version_tuple()[0]}; "
        f"python_version_tuple()[1] = {platform.python_version_tuple()[1]} "
    )

    if not (int(platform.python_version_tuple()[0]) == 3 and int(platform.python_version_tuple()[1]) >= 10):
        sys.exit(version_warning_string)


def docs_url(operation: str):
    base_url = "https://developer.cisco.com/meraki/api-v1/#!"
    ret = ""
    for letter in operation:
        if letter.islower():
            ret += letter
        else:
            ret += f"-{letter.lower()}"
    return base_url + ret


def return_params(operation: str, params: dict, param_filters):
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


def unpack_param_without_schema(all_params: dict, this_param: dict, name: str, is_required: bool):
    all_params[name] = {"required": is_required}

    for attribute in ("in", "type"):
        all_params[name][attribute] = this_param[attribute]

    if "enum" in this_param:
        all_params[name]["enum"] = this_param["enum"]

    if "description" in this_param:
        all_params[name]["description"] = this_param["description"]
    elif is_required:
        all_params[name]["description"] = "(required)"
    else:
        all_params[name]["description"] = this_param.get("description", "")

    return all_params


def unpack_param_with_schema(all_params: dict, this_param: dict):
    keys = this_param["schema"]["properties"]

    for k in keys:
        if "required" in this_param["schema"] and k in this_param["schema"]["required"]:
            all_params[k] = {"required": True}
        else:
            all_params[k] = {"required": False}

        all_params[k]["in"] = this_param["in"]

        for attribute in ("type", "description"):
            all_params[k][attribute] = keys[k][attribute]

        if "enum" in keys[k]:
            all_params[k]["enum"] = keys[k]["enum"]

        if "example" in this_param["schema"] and k in this_param["schema"]["example"]:
            all_params[k]["example"] = this_param["schema"]["example"][k]

    return all_params


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
