class MXPortForwardingRules(object):
    def __init__(self, session):
        super(MXPortForwardingRules, self).__init__()
        self._session = session
    
    def getNetworkPortForwardingRules(self, networkId: str):
        """
        **Return the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-port-forwarding-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX port forwarding rules'],
            'operation': 'getNetworkPortForwardingRules',
        }
        resource = f'/networks/{networkId}/portForwardingRules'

        return self._session.get(metadata, resource)

    def updateNetworkPortForwardingRules(self, networkId: str, rules: list):
        """
        **Update the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-port-forwarding-rules
        
        - networkId (string)
        - rules (array): An array of port forwarding params
        """

        kwargs = locals()

        metadata = {
            'tags': ['MX port forwarding rules'],
            'operation': 'updateNetworkPortForwardingRules',
        }
        resource = f'/networks/{networkId}/portForwardingRules'

        body_params = ['rules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

