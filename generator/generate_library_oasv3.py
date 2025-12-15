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
ID as inputs, a specific dashboard org's OpenAPI spec. This version is compatible with OpenAPI Specification v3.

=== USAGE ===
python[3] generate_library_oasv3.py [-o <org_id>] [-k <api_key>] [-v <version_number>] [-g <is_called_from_github_action>]
API key can, and is recommended to, be set as an environment variable named MERAKI_DASHBOARD_API_KEY. 
"""

REVERSE_PAGINATION = ['getNetworkEvents', 'getOrganizationConfigurationChanges']


# Helper function to resolve $ref references in OASv3
def resolve_ref(spec, ref):
    """
    Resolve a $ref reference in OASv3 spec.
    Example: #/components/schemas/Network -> spec['components']['schemas']['Network']
    """
    if not ref.startswith('#/'):
        return None
    
    parts = ref[2:].split('/')  # Remove '#/' and split
    result = spec
    for part in parts:
        if isinstance(result, dict) and part in result:
            result = result[part]
        else:
            return None
    return result


# Helper function to get schema from OASv3 parameter or requestBody
def get_schema_from_item(item, spec):
    """
    Extract schema from an OASv3 parameter or requestBody content item.
    Handles both inline schemas and $ref references.
    """
    if 'schema' in item:
        schema = item['schema']
        # If it's a $ref, resolve it
        if '$ref' in schema:
            resolved = resolve_ref(spec, schema['$ref'])
            if resolved:
                return resolved
        return schema
    return None


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


# Helper function to parse requestBody from OASv3
def parse_request_body(operation, request_body, spec):
    """
    Parse requestBody from OASv3 specification.
    In OASv3, requestBody has a 'content' object with media types (e.g., 'application/json').
    """
    if not request_body:
        return {}
    
    params = {}
    
    # OASv3 requestBody has a 'content' object
    if 'content' in request_body:
        # Usually we want application/json
        content = request_body['content']
        json_content = content.get('application/json', {})
        
        if json_content:
            schema = get_schema_from_item(json_content, spec)
            if schema and 'properties' in schema:
                # Get required fields from schema
                required_fields = schema.get('required', [])
                
                # Parse each property
                for prop_name, prop_schema in schema['properties'].items():
                    # Resolve $ref if present
                    if '$ref' in prop_schema:
                        resolved = resolve_ref(spec, prop_schema['$ref'])
                        if resolved:
                            prop_schema = resolved
                    
                    params[prop_name] = {
                        'required': prop_name in required_fields,
                        'in': 'body',
                        'type': prop_schema.get('type', 'object'),
                        'description': prop_schema.get('description', ''),
                    }
                    
                    # Handle enum
                    if 'enum' in prop_schema:
                        params[prop_name]['enum'] = prop_schema['enum']
                    
                    # Handle array type
                    if prop_schema.get('type') == 'array':
                        params[prop_name]['type'] = 'array'
                        if 'items' in prop_schema:
                            items = prop_schema['items']
                            if '$ref' in items:
                                resolved = resolve_ref(spec, items['$ref'])
                                if resolved:
                                    params[prop_name]['items'] = resolved
    
    return params


# Helper function to return parameters within OASv3 spec, optionally based on list of input filters
def parse_params(operation, parameters, request_body, spec, param_filters=None):
    """
    Parse parameters from OASv3 specification.
    In OASv3, body parameters are in requestBody, not in parameters with in='body'.
    """
    if param_filters is None:
        param_filters = []
    
    # Create dict with information on endpoint's parameters
    params = {}
    
    # Parse path and query parameters (these are still in 'parameters')
    if parameters:
        for p in parameters:
            name = p['name']
            param_in = p.get('in', 'query')  # 'path', 'query', 'header', 'cookie'
            
            # Get schema (OASv3 uses 'schema' directly, not nested in 'schema.properties')
            schema = get_schema_from_item(p, spec)
            
            if schema:
                # OASv3: schema is directly on the parameter, not nested
                param_type = schema.get('type', 'string')
                
                params[name] = {
                    'required': p.get('required', False),
                    'in': param_in,
                    'type': param_type,
                    'description': schema.get('description', p.get('description', '')),
                }
                
                # Handle enum
                if 'enum' in schema:
                    params[name]['enum'] = schema['enum']
                
                # Handle array type
                if param_type == 'array' and 'items' in schema:
                    items = schema['items']
                    if '$ref' in items:
                        resolved = resolve_ref(spec, items['$ref'])
                        if resolved:
                            params[name]['items'] = resolved
            else:
                # Fallback: use parameter directly if no schema
                params[name] = {
                    'required': p.get('required', False),
                    'in': param_in,
                    'type': p.get('type', 'string'),
                    'description': p.get('description', ''),
                }
                if 'enum' in p:
                    params[name]['enum'] = p['enum']
    
    # Parse requestBody (OASv3 specific)
    if request_body:
        body_params = parse_request_body(operation, request_body, spec)
        params.update(body_params)
    
    # Add custom library parameters to handle pagination
    if 'perPage' in params:
        params.update(generate_pagination_parameters(operation))
    
    # Return parameters based on matching input filters
    return return_params(operation, params, param_filters)


def generate_library(spec, version_number, is_github_action):
    # Supported scopes list will include organizations, networks, devices, and all product types.
    supported_scopes = ['organizations', 'networks', 'devices', 'appliance', 'camera', 'cellularGateway', 'insight',
                        'sm', 'switch', 'wireless', 'sensor', 'administered', 'licensing', 'secureConnect', 'campusGateway', 
                        'nac', 'spaces', 'wirelessController']
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

                    # OASv3: parameters are for path/query/header/cookie, requestBody is separate
                    parameters = endpoint.get('parameters', None)
                    request_body = endpoint.get('requestBody', None)

                    # Function definition
                    definition = ''
                    parsed_params = parse_params(operation, parameters, request_body, spec, 'required')
                    if parsed_params:
                        for p, values in parsed_params.items():
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

                        all_parsed_params = parse_params(operation, parameters, request_body, spec)
                        if 'perPage' in all_parsed_params:
                            if operation in REVERSE_PAGINATION:
                                definition += ", total_pages=1, direction='prev'"
                            else:
                                definition += ", total_pages=1, direction='next'"
                            if operation == 'getNetworkEvents':
                                definition += ', event_log_end_time=None'

                        optional_params = parse_params(operation, parameters, request_body, spec, ['optional'])
                        if optional_params:
                            definition += f', **kwargs'

                    # Docstring
                    param_descriptions = []
                    all_params = parse_params(operation, parameters, request_body, spec, ['required', 'pagination', 'optional'])
                    if all_params:
                        for p, values in all_params.items():
                            param_descriptions.append(f'{p} ({values["type"]}): {values["description"]}')

                    # Combine keyword args with locals
                    kwarg_line = ''
                    optional_params = parse_params(operation, parameters, request_body, spec, ['optional'])
                    if optional_params:
                        kwarg_line = 'kwargs.update(locals())'
                    else:
                        query_body_array = parse_params(operation, parameters, request_body, spec, ['query', 'array', 'body'])
                        if query_body_array:
                            kwarg_line = 'kwargs = locals()'

                    # Assert valid values for enum
                    enum_params = parse_params(operation, parameters, request_body, spec, ['enum'])
                    assert_blocks = []
                    if enum_params:
                        for p, values in enum_params.items():
                            assert_blocks.append((p, values['enum']))

                    # Function body for GET endpoints
                    query_params = array_params = body_params = path_params = {}
                    if method == 'get':
                        query_params = parse_params(operation, parameters, request_body, spec, 'query')
                        array_params = parse_params(operation, parameters, request_body, spec, 'array')
                        path_params = parse_params(operation, parameters, request_body, spec, 'path')
                        pagination_params = parse_params(operation, parameters, request_body, spec, 'pagination')
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
                        body_params = parse_params(operation, parameters, request_body, spec, 'body')
                        path_params = parse_params(operation, parameters, request_body, spec, 'path')
                        if body_params:
                            call_line = f'return self._session.{method}(metadata, resource, payload)'
                        else:
                            call_line = f'return self._session.{method}(metadata, resource)'

                    # Function body for DELETE endpoints
                    elif method == 'delete':
                        path_params = parse_params(operation, parameters, request_body, spec, 'path')
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

                        # OASv3: parameters are for path/query/header/cookie, requestBody is separate
                        parameters = endpoint.get('parameters', None)
                        request_body = endpoint.get('requestBody', None)

                        # Function definition
                        definition = ''
                        parsed_params = parse_params(operation, parameters, request_body, spec, 'required')
                        if parsed_params:
                            for p, values in parsed_params.items():
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

                            all_parsed_params = parse_params(operation, parameters, request_body, spec)
                            if 'perPage' in all_parsed_params:
                                if operation in REVERSE_PAGINATION:
                                    definition += ", total_pages=1, direction='prev'"
                                else:
                                    definition += ", total_pages=1, direction='next'"
                                if operation == 'getNetworkEvents':
                                    definition += ', event_log_end_time=None'

                            optional_params = parse_params(operation, parameters, request_body, spec, ['optional'])
                            if optional_params:
                                definition += f', **kwargs'

                        # Docstring
                        param_descriptions = []
                        all_params = parse_params(operation, parameters, request_body, spec, ['required', 'pagination', 'optional'])
                        if all_params:
                            for p, values in all_params.items():
                                param_descriptions.append(f'{p} ({values["type"]}): {values["description"]}')

                        # Combine keyword args with locals
                        kwarg_line = ''
                        optional_params = parse_params(operation, parameters, request_body, spec, ['optional'])
                        if optional_params:
                            kwarg_line = 'kwargs.update(locals())'
                        else:
                            query_body_array = parse_params(operation, parameters, request_body, spec, ['query', 'array', 'body'])
                            if query_body_array:
                                kwarg_line = 'kwargs = locals()'

                        # Assert valid values for enum
                        enum_params = parse_params(operation, parameters, request_body, spec, ['enum'])
                        assert_blocks = list()
                        if enum_params:
                            for p, values in enum_params.items():
                                assert_blocks.append((p, values['enum']))

                        # Function body for GET endpoints
                        query_params = array_params = body_params = {}

                        # Function body for POST/PUT endpoints
                        if method == 'post' or method == 'put':
                            body_params = parse_params(operation, parameters, request_body, spec, 'body')
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
            # Request OASv3 spec by adding version=3 parameter
            response = requests.get(f'https://api.meraki.com/api/v1/organizations/{org_id}/openapiSpec',
                                    headers={'Authorization': f'Bearer {api_key}'},
                                    params={'version': 3})
            if response.ok:
                spec = response.json()
            else:
                print_help()
                sys.exit(f'API key provided does not have access to org {org_id}')
    else:
        # Request OASv3 spec by adding version=3 parameter
        response = requests.get('https://api.meraki.com/api/v1/openapiSpec', params={'version': 3})
        if response.ok:
            spec = response.json()
        else:
            print_help()
            sys.exit('Failed to retrieve OpenAPI v3 specification. Please try again.')

    generate_library(spec, version_number, is_github_action)


if __name__ == '__main__':
    main(sys.argv[1:])

