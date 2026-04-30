import urllib


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

        networkId = urllib.parse.quote(networkId, safe="")
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

    def updateNetworkProfile(self, networkId: str, profileId: str, **kwargs):
        """
        **Update a network profile**
        https://developer.cisco.com/meraki/api-v1/#!update-network-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        - name (string): Name of the profile.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        profileId = urllib.parse.quote(profileId, safe="")
        resource = f"/networks/{networkId}/profiles/{profileId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateNetworkPolicy(self, networkId: str, policyId: str, **kwargs):
        """
        **Update a network policy**
        https://developer.cisco.com/meraki/api-v1/#!update-network-policy

        - networkId (string): Network ID
        - policyId (string): ID of the policy.
        - description (string): Description of the policy.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        policyId = urllib.parse.quote(policyId, safe="")
        resource = f"/networks/{networkId}/policies/{policyId}"

        body_params = [
            "policyId",
            "description",
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

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
