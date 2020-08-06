class MX1ManyNATRules(object):
    def __init__(self, session):
        super(MX1ManyNATRules, self).__init__()
        self._session = session
    
    def getNetworkOneToManyNatRules(self, networkId: str):
        """
        **Return the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-one-to-many-nat-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX 1:Many NAT rules'],
            'operation': 'getNetworkOneToManyNatRules',
        }
        resource = f'/networks/{networkId}/oneToManyNatRules'

        return self._session.get(metadata, resource)

    def updateNetworkOneToManyNatRules(self, networkId: str, rules: list):
        """
        **Set the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-one-to-many-nat-rules
        
        - networkId (string)
        - rules (array): An array of 1:Many nat rules
        """

        kwargs = locals()

        metadata = {
            'tags': ['MX 1:Many NAT rules'],
            'operation': 'updateNetworkOneToManyNatRules',
        }
        resource = f'/networks/{networkId}/oneToManyNatRules'

        body_params = ['rules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

