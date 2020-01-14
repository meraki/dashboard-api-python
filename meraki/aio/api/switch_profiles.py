class SwitchProfiles(object):
    def __init__(self, session):
        super(SwitchProfiles, self).__init__()
        self._session = session
    
    def getOrganizationConfigTemplateSwitchProfiles(self, organizationId: str, configTemplateId: str):
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

        return self._session.get(metadata, resource)

