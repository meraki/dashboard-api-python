class AsyncConfigTemplates:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationConfigTemplates(self, organizationId: str):
        """
        **List the configuration templates for this organization**
        https://api.meraki.com/api_docs#list-the-configuration-templates-for-this-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Config templates'],
            'operation': 'getOrganizationConfigTemplates',
        }
        resource = f'/organizations/{organizationId}/configTemplates'

        return await self._session.get(metadata, resource)

    async def deleteOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Remove a configuration template**
        https://api.meraki.com/api_docs#remove-a-configuration-template
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['Config templates'],
            'operation': 'deleteOrganizationConfigTemplate',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        return await self._session.delete(metadata, resource)

