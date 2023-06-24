import getopt
import os
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

=== USAGE ===
python[3] generate_library.py [-o <org_id>] [-k <api_key>] [-v <version_number>] [-g <is_called_from_github_action>]
API key can, and is recommended to, be set as an environment variable named MERAKI_DASHBOARD_API_KEY. 
"""

REVERSE_PAGINATION = ['getNetworkEvents', 'getOrganizationConfigurationChanges']


# Helper function to return pagination parameters depending on endpoint
def generate_pagination_parameters(operation):
    ret = {
        'total_pages': {
            'type': 'integer or string',
            'description': 'use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages',
        },
        'direction': {
            'type': 'string',
            'description': 'direction to paginate, either "next" or "prev" (default) page'
            if operation in REVERSE_PAGINATION
            else 'direction to paginate, either "next" (default) or "prev" page',
        }
    }
    if operation == 'getNetworkEvents':
        ret['event_log_end_time'] = {'type': 'string',
                                     'description': 'ISO8601 Zulu/UTC time, to use in conjunction with startingAfter, '
                                                    'to retrieve events within a time window'}
    return ret


# Returns full link to endpoint's documentation on Developer Hub
def docs_url(operation):
    base_url = 'https://developer.cisco.com/meraki/api-v1/#!'
    ret = ''
    for letter in operation:
        if letter.islower():
            ret += letter
        else:
            ret += f'-{letter.lower()}'
    return base_url + ret


# Helper function to return the right params; used in parse_params
def return_params(operation, params, param_filters):
    # Return parameters based on matching input filters
    if not param_filters:
        return params
    else:
        ret = {}
        if 'required' in param_filters:
            ret.update({k: v for k, v in params.items() if 'required' in v and v['required']})
        if 'pagination' in param_filters:
            ret.update(generate_pagination_parameters(operation) if 'perPage' in params else {})
        if 'optional' in param_filters:
            ret.update({k: v for k, v in params.items() if 'required' in v and not v['required']})
        if 'path' in param_filters:
            ret.update({k: v for k, v in params.items() if 'in' in v and v['in'] == 'path'})
        if 'query' in param_filters:
            ret.update({k: v for k, v in params.items() if 'in' in v and v['in'] == 'query'})
        if 'body' in param_filters:
            ret.update({k: v for k, v in params.items() if 'in' in v and v['in'] == 'body'})
        if 'array' in param_filters:
            ret.update({k: v for k, v in params.items() if 'in' in v and v['type'] == 'array'})
        if 'enum' in param_filters:
            ret.update({k: v for k, v in params.items() if 'enum' in v})
        return ret


# Helper function to return parameters within OAS spec, optionally based on list of input filters
def parse_params(operation, parameters, param_filters=None):
    if param_filters is None:
        param_filters = []
    if parameters is None:
        return {}

    # Create dict with information on endpoint's parameters
    params = {}
    for p in parameters:
        name = p['name']

        # consult the schema if there is one
        if 'schema' in p:
            # the parameter will have a top-level object 'schema' and within that, 'properties' in OASv2
            # in OASv3, the parameter will only have this for query and path parameters, and requestBody params
            # will be in a separate key
            keys = p['schema']['properties']

            # parse the properties and assign types and descriptions
            for k in keys:
                # if required, set required true
                if 'required' in p['schema'] and k in p['schema']['required']:
                    params[k] = {'required': True}
                else:
                    params[k] = {'required': False}

                # identify whether the parameter is in the path or query, or for OASv2, in the body
                params[k]['in'] = p['in']

                # assign the right data type to the parameter per the schema
                params[k]['type'] = keys[k]['type']

                # assign the description to the parameter per the schema
                params[k]['description'] = keys[k]['description']

                # capture schema enum if available
                if 'enum' in keys[k]:
                    params[k]['enum'] = keys[k]['enum']

                # capture schema example if available
                if 'example' in p['schema'] and k in p['schema']['example']:
                    params[k]['example'] = p['schema']['example'][k]

        # if there is no schema, then consult the required attribute
        elif 'required' in p and p['required']:
            params[name] = {'required': True}

            # identify whether the parameter is in the path or query, or for OASv2, in the body
            params[name]['in'] = p['in']

            # assign the right data type to the parameter
            params[name]['type'] = p['type']

            # assign the description to the parameter if it's available
            if 'description' in p:
                params[name]['description'] = p['description']

            # fall back to required if there is no description
            else:
                params[name]['description'] = '(required)'

            # capture the enum if available
            if 'enum' in p:
                params[name]['enum'] = p['enum']

        # if there is no schema and no required attribute, then the parameter is not required
        else:
            params[name] = {'required': False}
            params[name]['in'] = p['in']
            params[name]['type'] = p['type']
            params[name]['description'] = p['description']
            if 'enum' in p:
                params[name]['enum'] = p['enum']

    # Add custom library parameters to handle pagination
    if 'perPage' in params:
        params.update(generate_pagination_parameters(operation))

    # Return parameters based on matching input filters
    return return_params(operation, params, param_filters)


def generate_library(spec, version_number, is_github_action):
    # Supported scopes list will include organizations, networks, devices, and all product types.
    supported_scopes = ['organizations', 'networks', 'devices', 'appliance', 'camera', 'cellularGateway', 'insight',
                        'sm', 'switch', 'wireless', 'sensor', 'administered', 'licensing', 'secureConnect']
    # legacy scopes = ['organizations', 'networks', 'devices', 'appliance', 'camera', 'cellularGateway', 'insight',
    #                  'sm', 'switch', 'wireless']
    tags = spec['tags']
    paths = spec['paths']
    # Scopes used when generating the library will depend on the provided version of the API spec.
    scopes = {tag['name']: {} for tag in tags if tag['name'] in supported_scopes}

    batchable_action_summaries = [action['summary'] for action in spec['x-batchable-actions']]

    # Set template_dir if a GitHub action is invoking it
    if is_github_action:
        template_dir = 'generator/'
    else:
        template_dir = ''

    # Check paths and create sub-directories if needed
    subdirs = ['meraki', 'meraki/api', 'meraki/api/batch', 'meraki/aio', 'meraki/aio/api', 'meraki/api/batch']
    for dir in subdirs:
        if not os.path.isdir(dir):
            os.mkdir(dir)

    # Files that are not generated
    non_generated = ['__init__.py', 'config.py', 'exceptions.py', 'rest_session.py', 'api/__init__.py',
                     'aio/__init__.py', 'aio/rest_session.py', 'aio/api/__init__.py', 'api/batch/__init__.py']
    base_url = 'https://raw.githubusercontent.com/meraki/dashboard-api-python/master/meraki/'
    for file in non_generated:
        response = requests.get(f'{base_url}{file}')
        with open(f'meraki/{file}', 'w+', encoding='utf-8', newline=None) as fp:
            contents = response.text
            if file == '__init__.py':
                start = contents.find('__version__ = ')
                end = contents.find('\n', start)
                contents = f'{contents[:start]}__version__ = \'{version_number}\'{contents[end:]}'
            fp.write(contents)

    # Organize data from OpenAPI specification
    operations = list()  # list of operation IDs
    for path, methods in paths.items():
        # method is the HTTP action, e.g. get, put, etc.
        for method in methods:

            # endpoint is the method for that specific path
            endpoint = paths[path][method]

            # the endpoint has tags
            tags = endpoint['tags']

            # the endpoint has an operationId
            operation = endpoint['operationId']

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
    print(f'Total of {len(operations)} endpoints found from OpenAPI spec...')

    # Generate API libraries
    # We will use newline=None to ensure that line breaks are handled correctly, especially when generating
    # on Windows and using git autocrlf true
    jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

    # Iterate through the scopes creating standard, asyncio and batch modules for each
    for scope in scopes:
        print(f'...generating {scope}')
        section = scopes[scope]

        # Generate the standard module
        with open(f'meraki/api/{scope}.py', 'w', encoding='utf-8', newline=None) as output:
            with open(f'{template_dir}class_template.jinja2', encoding='utf-8', newline=None) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                output.write(
                    template.render(
                        class_name=scope[0].upper() + scope[1:],
                    )
                )

            # Generate Asyncio API libraries
            async_output = open(f'meraki/aio/api/{scope}.py', 'w', encoding='utf-8', newline=None)
            with open(f'{template_dir}async_class_template.jinja2', encoding='utf-8', newline=None) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                async_output.write(
                    template.render(
                        class_name=scope[0].upper() + scope[1:],
                    )
                )

            # Generate Action Batch API libraries
            batch_output = open(f'meraki/api/batch/{scope}.py', 'w', encoding='utf-8', newline=None)
            with open(f'{template_dir}batch_class_template.jinja2', encoding='utf-8', newline=None) as fp:
                class_template = fp.read()
                template = jinja_env.from_string(class_template)
                batch_output.write(
                    template.render(
                        class_name=scope[0].upper() + scope[1:],
                    )
                )

            # Generate API & Asyncio API functions
            for path, methods in section.items():
                for method, endpoint in methods.items():
                    # Get metadata
                    tags = endpoint['tags']
                    operation = endpoint['operationId']
                    description = endpoint['summary']

                    # will need updating for OASv3
                    parameters = endpoint['parameters'] if 'parameters' in endpoint else None

                    # Function definition
                    definition = ''
                    if parameters:
                        for p, values in parse_params(operation, parameters, 'required').items():
                            if values['type'] == 'array':
                                definition += f', {p}: list'
                            elif values['type'] == 'number':
                                definition += f', {p}: float'
                            elif values['type'] == 'integer':
                                definition += f', {p}: int'
                            elif values['type'] == 'boolean':
                                definition += f', {p}: bool'
                            elif values['type'] == 'object':
                                definition += f', {p}: dict'
                            elif values['type'] == 'string':
                                definition += f', {p}: str'

                        if 'perPage' in parse_params(operation, parameters):
                            if operation in REVERSE_PAGINATION:
                                definition += ", total_pages=1, direction='prev'"
                            else:
                                definition += ", total_pages=1, direction='next'"
                            if operation == 'getNetworkEvents':
                                definition += ', event_log_end_time=None'

                        if parse_params(operation, parameters, ['optional']):
                            definition += f', **kwargs'

                    # Docstring
                    param_descriptions = []
                    all_params = parse_params(operation, parameters, ['required', 'pagination', 'optional'])
                    if all_params:
                        for p, values in all_params.items():
                            param_descriptions.append(f'{p} ({values["type"]}): {values["description"]}')

                    # Combine keyword args with locals
                    kwarg_line = ''
                    if parse_params(operation, parameters, ['optional']):
                        kwarg_line = 'kwargs.update(locals())'
                    elif parse_params(operation, parameters, ['query', 'array', 'body']):
                        kwarg_line = 'kwargs = locals()'

                    # Assert valid values for enum
                    enum_params = parse_params(operation, parameters, ['enum'])
                    assert_blocks = []
                    if enum_params:
                        for p, values in enum_params.items():
                            assert_blocks.append((p, values['enum']))

                    # Function body for GET endpoints
                    query_params = array_params = body_params = path_params = {}
                    if method == 'get':
                        query_params = parse_params(operation, parameters, 'query')
                        array_params = parse_params(operation, parameters, 'array')
                        path_params = parse_params(operation, parameters, 'path')
                        pagination_params = parse_params(operation, parameters, 'pagination')
                        if query_params or array_params:
                            if pagination_params:
                                if operation == 'getNetworkEvents':
                                    call_line = 'return self._session.get_pages(metadata, resource, params, ' \
                                                'total_pages, direction, event_log_end_time)'
                                else:
                                    call_line = 'return self._session.get_pages(metadata, resource, params, ' \
                                                'total_pages, direction)'
                            else:
                                call_line = 'return self._session.get(metadata, resource, params)'
                        else:
                            call_line = 'return self._session.get(metadata, resource)'

                    # Function body for POST/PUT endpoints
                    elif method == 'post' or method == 'put':
                        body_params = parse_params(operation, parameters, 'body')
                        path_params = parse_params(operation, parameters, 'path')
                        if body_params:
                            call_line = f'return self._session.{method}(metadata, resource, payload)'
                        else:
                            call_line = f'return self._session.{method}(metadata, resource)'

                    # Function body for DELETE endpoints
                    elif method == 'delete':
                        path_params = parse_params(operation, parameters, 'path')
                        call_line = 'return self._session.delete(metadata, resource)'

                    # Add function to files
                    with open(f'{template_dir}function_template.jinja2', encoding='utf-8', newline=None) as fp:
                        function_template = fp.read()
                        template = jinja_env.from_string(function_template)
                        output.write(
                            '\n\n' +
                            template.render(
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
                                call_line=call_line
                            )
                        )
                        async_output.write(
                            '\n\n' +
                            template.render(
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
                                call_line=call_line
                            )
                        )

            # Generate API action batch functions
            for path, methods in section.items():
                for method, endpoint in methods.items():
                    if endpoint['description'] in batchable_action_summaries:
                        # Get metadata
                        tags = endpoint['tags']
                        operation = endpoint['operationId']
                        description = endpoint['summary']

                        # May need update for OASv3
                        parameters = endpoint['parameters'] if 'parameters' in endpoint else None

                        # Function definition
                        definition = ''
                        if parameters:
                            for p, values in parse_params(operation, parameters, 'required').items():
                                if values['type'] == 'array':
                                    definition += f', {p}: list'
                                elif values['type'] == 'number':
                                    definition += f', {p}: float'
                                elif values['type'] == 'integer':
                                    definition += f', {p}: int'
                                elif values['type'] == 'boolean':
                                    definition += f', {p}: bool'
                                elif values['type'] == 'object':
                                    definition += f', {p}: dict'
                                elif values['type'] == 'string':
                                    definition += f', {p}: str'

                            if 'perPage' in parse_params(operation, parameters):
                                if operation in REVERSE_PAGINATION:
                                    definition += ", total_pages=1, direction='prev'"
                                else:
                                    definition += ", total_pages=1, direction='next'"
                                if operation == 'getNetworkEvents':
                                    definition += ', event_log_end_time=None'

                            if parse_params(operation, parameters, ['optional']):
                                definition += f', **kwargs'

                        # Docstring
                        param_descriptions = []
                        all_params = parse_params(operation, parameters, ['required', 'pagination', 'optional'])
                        if all_params:
                            for p, values in all_params.items():
                                param_descriptions.append(f'{p} ({values["type"]}): {values["description"]}')

                        # Combine keyword args with locals
                        kwarg_line = ''
                        if parse_params(operation, parameters, ['optional']):
                            kwarg_line = 'kwargs.update(locals())'

                        # will need update for OASv3
                        elif parse_params(operation, parameters, ['query', 'array', 'body']):
                            kwarg_line = 'kwargs = locals()'

                        # Assert valid values for enum
                        enum_params = parse_params(operation, parameters, ['enum'])
                        assert_blocks = list()
                        if enum_params:
                            for p, values in enum_params.items():
                                assert_blocks.append((p, values['enum']))

                        # Function body for GET endpoints
                        query_params = array_params = body_params = {}

                        # Function body for POST/PUT endpoints
                        if method == 'post' or method == 'put':

                            # will need update for OASv3
                            body_params = parse_params(operation, parameters, 'body')
                            if method == 'post':
                                batch_operation = 'create'
                            else:
                                batch_operation = 'update'

                        # Function body for DELETE endpoints
                        elif method == 'delete':
                            batch_operation = 'destroy'

                        # Function return statement
                        call_line = 'return action'

                        # Add function to files
                        with open(f'{template_dir}batch_function_template.jinja2', encoding='utf-8', newline=None) \
                                as fp:
                            function_template = fp.read()
                            template = jinja_env.from_string(function_template)
                            batch_output.write(
                                '\n\n' +
                                template.render(
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
                                    batch_operation=batch_operation
                                )
                            )


# Prints READ_ME help message for user to read
def print_help():
    lines = READ_ME.split('\n')
    for line in lines:
        print(f'# {line}')


# Parse command line arguments
def main(inputs):
    api_key = os.environ.get('MERAKI_DASHBOARD_API_KEY')
    org_id = None
    version_number = 'custom'
    is_github_action = False

    try:
        opts, args = getopt.getopt(inputs, 'ho:k:v:g:')
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit(2)
        elif opt == '-o':
            org_id = arg
        elif opt == '-k' and api_key is None:
            api_key = arg
        elif opt == '-v':
            version_number = arg
        elif opt == '-g':
            if arg.lower() == 'true':
                is_github_action = True

    # Retrieve latest OpenAPI specification
    if org_id:
        if not api_key:
            print_help()
            sys.exit(2)
        else:
            response = requests.get(f'https://api.meraki.com/api/v1/organizations/{org_id}/openapiSpec',
                                    headers={f'Bearer: {api_key}'})
            if response.ok:
                spec = response.json()
            else:
                print_help()
                sys.exit(f'API key provided does not have access to org {org_id}')
    else:
        spec = requests.get('https://api.meraki.com/api/v1/openapiSpec').json()

    generate_library(spec, version_number, is_github_action)


if __name__ == '__main__':
    main(sys.argv[1:])
