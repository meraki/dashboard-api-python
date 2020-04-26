class AsyncSwitchProfiles:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationConfigTemplateSwitchProfiles(self, organizationId: str, configTemplateId: str):
        """
        **List the switch profiles for your switch template configuration**
        https://api.meraki.com/api_docs#list-the-switch-profiles-for-your-switch-template-configuration
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['Switch profiles'],
            'operation': 'getOrganizationConfigTemplateSwitchProfiles',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switchProfiles'

        return await self._session.get(metadata, resource)

