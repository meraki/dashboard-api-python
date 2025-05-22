import urllib


class ActionBatchSpaces(object):
    def __init__(self):
        super(ActionBatchSpaces, self).__init__()
        


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
        resource = f'/organizations/{organizationId}/spaces/integration/remove'

        action = {
            "resource": resource,
            "operation": "integration",
        }
        return action
        



