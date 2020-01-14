class AsyncMX11NATRules(object):
    def __init__(self, session):
        super().__init__()
        self._session = session

    async def getNetworkOneToOneNatRules(self, networkId: str):
        """
        **Return the 1:1 NAT mapping rules for an MX network**
        https://api.meraki.com/api_docs#return-the-11-nat-mapping-rules-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            "tags": ["MX 1:1 NAT rules"],
            "operation": "getNetworkOneToOneNatRules",
        }
        resource = f"/networks/{networkId}/oneToOneNatRules"

        return await self._session.get(metadata, resource)

    async def updateNetworkOneToOneNatRules(self, networkId: str, **kwargs):
        """
        **Set the 1:1 NAT mapping rules for an MX network**
        https://api.meraki.com/api_docs#set-the-11-nat-mapping-rules-for-an-mx-network
        
        - networkId (string)
        - rules (array): An array of 1:1 nat rules
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["MX 1:1 NAT rules"],
            "operation": "updateNetworkOneToOneNatRules",
        }
        resource = f"/networks/{networkId}/oneToOneNatRules"

        body_params = ["rules"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)
