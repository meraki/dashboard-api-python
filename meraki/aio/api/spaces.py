import urllib


class AsyncSpaces:
    def __init__(self, session):
        super().__init__()
        self._session = session
        


    def removeOrganizationSpacesIntegration(self, organizationId: str):
        """
        **Remove the Spaces integration from Meraki**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['organizations', 'configure', 'spaces', 'integration'],
            'operation': 'removeOrganizationSpacesIntegration'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/spaces/integration/remove'

        return self._session.post(metadata, resource)
        
