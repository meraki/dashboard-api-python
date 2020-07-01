import json
import re
import shutil
import sys

import requests
from jinja2 import Template


CALL_TEMPLATE = Template('''import meraki

# Defining your API key as a variable in source code is not recommended
API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

dashboard = meraki.DashboardAPI(API_KEY)
{{ parameter_assignments }}
response = dashboard.{{ section }}.{{ operation}}({{ parameters }})

print(response)
''')

REVERSE_PAGINATION = ['getNetworkEvents', 'getOrganizationConfigurationChanges']


# Helper function to convert camel case parameter name to snake case
def snakify(param):
    ret = ''
    for s in param:
        if s.islower():
            ret += s
        elif s == '_':
            ret += '_'
        else:
            ret += '_' + s.lower()
    return ret


# Helper function to return pagination parameters depending on endpoint
def generate_pagination_parameters(operation):
    ret = {
        'total_pages': {
            'type': 'integer or string',
            'description': 'total number of pages to retrieve, -1 or "all" for all pages',
        },
        'direction': {
            'type': 'string',
            'description': 'direction to paginate, either "next" or "prev" (default) page' if operation in
                                                                                              REVERSE_PAGINATION else 'direction to paginate, either "next" (default) or "prev" page',
        }
    }
    return ret


# Helper function to return parameters within OAS spec, optionally based on list of input filters
def parse_params(operation, parameters, param_filters=[]):
    if parameters is None:
        return {}

    # Create dict with information on endpoint's parameters
    params = {}
    for p in parameters:
        name = p['name']
        if 'schema' in p:
            keys = p['schema']['properties']
            for k in keys:
                if 'required' in p['schema'] and k in p['schema']['required']:
                    params[k] = {'required': True}
                else:
                    params[k] = {'required': False}
                params[k]['in'] = p['in']
                params[k]['type'] = keys[k]['type']
                params[k]['description'] = keys[k]['description']
                if 'enum' in keys[k]:
                    params[k]['enum'] = keys[k]['enum']
                if 'example' in p['schema'] and k in p['schema']['example']:
                    params[k]['example'] = p['schema']['example'][k]
        elif 'required' in p and p['required']:
            params[name] = {'required': True}
            params[name]['in'] = p['in']
            params[name]['type'] = p['type']
            if 'description' in p:
                params[name]['description'] = p['description']
            else:
                params[name]['description'] = '(required)'
            if 'enum' in p:
                params[name]['enum'] = p['enum']
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


# Generate text for parameter assignments
def process_assignments(parameters):
    text = '\n'

    for k, v in parameters.items():
        param_name = snakify(k)
        if param_name == 'id':
            param_name = 'id_'

        if v == 'list':
            text += f'{param_name} = []\n'
        elif v == 'float':
            text += f'{param_name} = 0.0\n'
        elif v == 'int':
            text += f'{param_name} = 0\n'
        elif v == 'bool':
            text += f'{param_name} = False\n'
        elif v == 'dict':
            text += f'{param_name} = {{}}\n'
        elif v == 'str':
            text += f'{param_name} = \'\'\n'
        else:
            if type(v) == str:
                value = f'\'{v}\''
            else:
                value = v
            text += f'{param_name} = {value}\n'

    return text


def main():
    # Get latest OpenAPI specification
    spec = requests.get('https://api.meraki.com/api/v1/openapiSpec').json()

    # Only care about the first 10 tags, which are the 10 scopes for organizations, networks, devices, & 7 products
    # scopes = ['organizations', 'networks', 'devices',
    #           'appliance', 'camera', 'cellularGateway', 'insight', 'sm', 'switch', 'wireless']
    tags = spec['tags']
    paths = spec['paths']
    scopes = {tag['name']: {} for tag in tags[:10]}

    # Organize data
    operations = []
    for path, methods in paths.items():
        for method in methods:
            endpoint = paths[path][method]
            tags = endpoint['tags']
            operation = endpoint['operationId']
            operations.append(operation)
            scope = tags[0]
            if path not in scopes[scope]:
                scopes[scope][path] = {method: endpoint}
            else:
                scopes[scope][path][method] = endpoint

    # Generate API libraries
    for scope in scopes:
        print(f'...generating {scope}')
        section = scopes[scope]

        for path, methods in section.items():
            for method, endpoint in methods.items():
                # Get metadata
                tags = endpoint['tags']
                operation = endpoint['operationId']
                description = endpoint['summary']
                parameters = endpoint['parameters'] if 'parameters' in endpoint else None
                responses = endpoint['responses']  # not actually used here for library generation

                required = {}
                optional = {}

                if parameters:
                    if 'perPage' in parse_params(operation, parameters):
                        pagination = True
                    else:
                        pagination = False

                    for p, values in parse_params(operation, parameters, 'required').items():
                        if 'example' in values:
                            required[p] = values['example']
                        elif p == 'organizationId':
                            required[p] = '549236'
                        elif p == 'networkId':
                            required[p] = 'L_646829496481105433'    # DevNet Sandbox ALWAYS ON network @ https://n149.meraki.com/o/-t35Mb/manage/organization/overview
                        elif p == 'serial':
                            required[p] = 'Q2QN-9J8L-SLPD'
                        elif values['type'] == 'array':
                            required[p] = 'list'
                        elif values['type'] == 'number':
                            required[p] = 'float'
                        elif values['type'] == 'integer':
                            required[p] = 'int'
                        elif values['type'] == 'boolean':
                            required[p] = 'bool'
                        elif values['type'] == 'object':
                            required[p] = 'dict'
                        elif values['type'] == 'string':
                            required[p] = 'str'
                        else:
                            sys.exit(p, values)

                    if pagination:
                        if operation not in REVERSE_PAGINATION:
                            optional['total_pages'] = 'all'
                        else:
                            optional['total_pages'] = 3

                    for p, values in parse_params(operation, parameters, 'optional').items():
                        if 'example' in values:
                            optional[p] = values['example']

                if operation == 'createNetworkGroupPolicy':
                    print(required)
                    print(optional)

                with open(f'code_snippets/{operation}.py', 'w') as fp:
                    if required.items():
                        parameters_text = '\n    '
                        for k, v in required.items():
                            param_name = snakify(k)
                            if param_name == 'id':
                                param_name = 'id_'
                            parameters_text += f'{param_name}, '
                        for k, v in optional.items():
                            if k == 'total_pages' and v == 'all':
                                parameters_text += f'total_pages=\'all\''
                            elif k == 'total_pages' and v == 1:
                                parameters_text += f'total_pages=1'
                            elif type(v) == str:
                                parameters_text += f'\n    {k}=\'{v}\', '
                            else:
                                parameters_text += f'\n    {k}={v}, '
                        if parameters_text[-2:] == ', ':
                            parameters_text = parameters_text[:-2]
                        parameters_text += '\n'
                    else:
                        parameters_text = ''


                    fp.write(
                        CALL_TEMPLATE.render(
                            parameter_assignments=process_assignments(required),
                            section=scope,
                            operation=operation,
                            parameters=parameters_text,
                        )
                    )


if __name__ == '__main__':
    main()
