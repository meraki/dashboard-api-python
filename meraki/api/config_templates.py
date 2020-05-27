class ConfigTemplates(object):
    def __init__(self, session):
        super(ConfigTemplates, self).__init__()
        self._session = session
    
    def getOrganizationConfigTemplates(self, organizationId: str):
        """
        **List the configuration templates for this organization**
        https://developer.cisco.com/meraki/api/#!get-organization-config-templates
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Config templates'],
            'operation': 'getOrganizationConfigTemplates',
        }
        resource = f'/organizations/{organizationId}/configTemplates'

        return self._session.get(metadata, resource)

    def deleteOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Remove a configuration template**
        https://developer.cisco.com/meraki/api/#!delete-organization-config-template
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['Config templates'],
            'operation': 'deleteOrganizationConfigTemplate',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        return self._session.delete(metadata, resource)

