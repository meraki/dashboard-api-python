import urllib


class ActionBatchNetworks(object):
    def __init__(self):
        super(ActionBatchNetworks, self).__init__()

    def deleteNetwork(self, networkId: str):
        """
        **Delete a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): Network ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createNetwork(self, name: str, type: str, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network

        - name (string): Network name
        - type (string): Network type
        """

        resource = "/networks"

        body_params = [
            "name",
            "type",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateNetworkSettings(self, networkId: str, **kwargs):
        """
        **Update a network's settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): Network ID
        - localStatusPageEnabled (boolean): Enable local status page
        """

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/settings"

        body_params = [
            "localStatusPageEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action
