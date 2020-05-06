class AsyncOpenAPISpec:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationOpenapiSpec(self, organizationId: str):
        """
        **Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-organization-openapi-spec
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['OpenAPI Spec'],
            'operation': 'getOrganizationOpenapiSpec',
        }
        resource = f'/organizations/{organizationId}/openapiSpec'

        return await self._session.get(metadata, resource)

