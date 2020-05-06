class AsyncSwitchProfiles:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationConfigTemplateSwitchProfiles(self, organizationId: str, configTemplateId: str):
        """
        **List the switch profiles for your switch template configuration**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-organization-config-template-switch-profiles
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['Switch profiles'],
            'operation': 'getOrganizationConfigTemplateSwitchProfiles',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switchProfiles'

        return await self._session.get(metadata, resource)

