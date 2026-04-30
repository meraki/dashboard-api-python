class ActionBatchNetworks(object):
    def __init__(self):
        super(ActionBatchNetworks, self).__init__()

    def updateNetworkSettings(self, networkId: str, **kwargs):
        """
        **Update the settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): Network ID
        - localStatusPageEnabled (boolean): Enables / disables the local device status pages.
        - securePort (object): A hash of SecureConnect options.
        """

        kwargs.update(locals())

        resource = f"/networks/{networkId}/settings"

        body_params = [
            "localStatusPageEnabled",
            "securePort",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetwork(self, networkId: str):
        """
        **Delete a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): Network ID
        """

        resource = f"/networks/{networkId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
