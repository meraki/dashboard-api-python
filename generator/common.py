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
                    case 'spaces':
                        scope = 'spaces'
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
