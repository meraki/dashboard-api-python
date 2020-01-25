class MXPortForwardingRules(object):
    def __init__(self, session):
        super(MXPortForwardingRules, self).__init__()
        self._session = session
    
    def getNetworkPortForwardingRules(self, networkId: str):
        """
        **Return the port forwarding rules for an MX network**
        https://api.meraki.com/api_docs#return-the-port-forwarding-rules-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX port forwarding rules'],
            'operation': 'getNetworkPortForwardingRules',
        }
        resource = f'/networks/{networkId}/portForwardingRules'

        return self._session.get(metadata, resource)

    def updateNetworkPortForwardingRules(self, networkId: str, **kwargs):
        """
        **Update the port forwarding rules for an MX network**
        https://api.meraki.com/api_docs#update-the-port-forwarding-rules-for-an-mx-network
        
        - networkId (string)
        - rules (array): An array of port forwarding params
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX port forwarding rules'],
            'operation': 'updateNetworkPortForwardingRules',
        }
        resource = f'/networks/{networkId}/portForwardingRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

