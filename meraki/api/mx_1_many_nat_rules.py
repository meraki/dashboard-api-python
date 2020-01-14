class MX1ManyNATRules(object):
    def __init__(self, session):
        super(MX1ManyNATRules, self).__init__()
        self._session = session

    def getNetworkOneToManyNatRules(self, networkId: str):
        """
        **Return the 1:Many NAT mapping rules for an MX network**
        https://api.meraki.com/api_docs#return-the-1many-nat-mapping-rules-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            "tags": ["MX 1:Many NAT rules"],
            "operation": "getNetworkOneToManyNatRules",
        }
        resource = f"/networks/{networkId}/oneToManyNatRules"

        return self._session.get(metadata, resource)

    def updateNetworkOneToManyNatRules(self, networkId: str, **kwargs):
        """
        **Set the 1:Many NAT mapping rules for an MX network**
        https://api.meraki.com/api_docs#set-the-1many-nat-mapping-rules-for-an-mx-network
        
        - networkId (string)
        - rules (array): An array of 1:Many nat rules
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["MX 1:Many NAT rules"],
            "operation": "updateNetworkOneToManyNatRules",
        }
        resource = f"/networks/{networkId}/oneToManyNatRules"

        body_params = ["rules"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)
