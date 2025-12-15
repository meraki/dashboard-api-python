import urllib


class Spaces(object):
    def __init__(self, session):
        super(Spaces, self).__init__()
        self._session = session
        


    def getOrganizationSpacesIntegrateStatus(self, organizationId: str):
        """
        **Get the status of the Spaces integration in Meraki**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-integrate-status

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['spaces', 'configure', 'integrate', 'status'],
            'operation': 'getOrganizationSpacesIntegrateStatus'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/spaces/integrate/status'

        return self._session.get(metadata, resource)
        


    def removeOrganizationSpacesIntegration(self, organizationId: str):
        """
        **Remove the Spaces integration from Meraki**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['spaces', 'configure', 'integration'],
            'operation': 'removeOrganizationSpacesIntegration'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/spaces/integration/remove'

        return self._session.post(metadata, resource)
        
