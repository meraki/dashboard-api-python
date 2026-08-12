import urllib


class ActionBatchSpaces:
    def __init__(self):
        super().__init__()

    def createNetworkSpacesSitesBuilding(self, networkId: str, name: str, **kwargs):
        """
        **Create a new building**
        https://developer.cisco.com/meraki/api-v1/#!create-network-spaces-sites-building

        - networkId (string): Network ID
        - name (string): The name of the building
        - bounds (object): Geographic bounding box for the building, expressed as north-east and south-west corner coordinates.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/spaces/sites/buildings"

        body_params = [
            "name",
            "bounds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateNetworkSpacesSitesBuilding(self, networkId: str, buildingId: str, **kwargs):
        """
        **Update a building**
        https://developer.cisco.com/meraki/api-v1/#!update-network-spaces-sites-building

        - networkId (string): Network ID
        - buildingId (string): Building ID
        - name (string): The name of the building
        - bounds (object): Geographic bounding box for the building, expressed as north-east and south-west corner coordinates.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        buildingId = urllib.parse.quote(buildingId, safe="")
        resource = f"/networks/{networkId}/spaces/sites/buildings/{buildingId}"

        body_params = [
            "name",
            "bounds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetworkSpacesSitesBuilding(self, networkId: str, buildingId: str):
        """
        **Delete a building**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-spaces-sites-building

        - networkId (string): Network ID
        - buildingId (string): Building ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        buildingId = urllib.parse.quote(buildingId, safe="")
        resource = f"/networks/{networkId}/spaces/sites/buildings/{buildingId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def removeOrganizationSpacesIntegration(self, organizationId: str):
        """
        **Remove the Spaces integration from Meraki**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        - organizationId (string): Organization ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/spaces/integration/remove"

        action = {
            "resource": resource,
            "operation": "integration",
        }
        return action
