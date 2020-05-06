class AsyncMXL7ApplicationCategories:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkL7FirewallRulesApplicationCategories(self, networkId: str):
        """
        **Return the L7 firewall application categories and their associated applications for an MX network**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-network-l-7-firewall-rules-application-categories
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX L7 application categories'],
            'operation': 'getNetworkL7FirewallRulesApplicationCategories',
        }
        resource = f'/networks/{networkId}/l7FirewallRules/applicationCategories'

        return await self._session.get(metadata, resource)

