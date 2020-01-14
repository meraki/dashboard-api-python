class AsyncMXL7ApplicationCategories(object):
    def __init__(self, session):
        super(MXL7ApplicationCategories, self).__init__()
        self._session = session

    async def getNetworkL7FirewallRulesApplicationCategories(self, networkId: str):
        """
        **Return the L7 firewall application categories and their associated applications for an MX network**
        https://api.meraki.com/api_docs#return-the-l7-firewall-application-categories-and-their-associated-applications-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            "tags": ["MX L7 application categories"],
            "operation": "getNetworkL7FirewallRulesApplicationCategories",
        }
        resource = f"/networks/{networkId}/l7FirewallRules/applicationCategories"

        return await self._session.get(metadata, resource)
