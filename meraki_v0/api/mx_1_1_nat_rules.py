class MX11NATRules(object):
    def __init__(self, session):
        super(MX11NATRules, self).__init__()
        self._session = session
    
    def getNetworkOneToOneNatRules(self, networkId: str):
        """
        **Return the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-one-to-one-nat-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX 1:1 NAT rules'],
            'operation': 'getNetworkOneToOneNatRules',
        }
        resource = f'/networks/{networkId}/oneToOneNatRules'

        return self._session.get(metadata, resource)

    def updateNetworkOneToOneNatRules(self, networkId: str, rules: list):
        """
        **Set the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-one-to-one-nat-rules
        
        - networkId (string)
        - rules (array): An array of 1:1 nat rules
        """

        kwargs = locals()

        metadata = {
            'tags': ['MX 1:1 NAT rules'],
            'operation': 'updateNetworkOneToOneNatRules',
        }
        resource = f'/networks/{networkId}/oneToOneNatRules'

        body_params = ['rules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

