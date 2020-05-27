class OpenAPISpec(object):
    def __init__(self, session):
        super(OpenAPISpec, self).__init__()
        self._session = session
    
    def getOrganizationOpenapiSpec(self, organizationId: str):
        """
        **Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**
        https://developer.cisco.com/meraki/api/#!get-organization-openapi-spec
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['OpenAPI Spec'],
            'operation': 'getOrganizationOpenapiSpec',
        }
        resource = f'/organizations/{organizationId}/openapiSpec'

        return self._session.get(metadata, resource)

