class AsyncContentFilteringCategories:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkContentFilteringCategories(self, networkId: str):
        """
        **List all available content filtering categories for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-content-filtering-categories
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Content filtering categories'],
            'operation': 'getNetworkContentFilteringCategories',
        }
        resource = f'/networks/{networkId}/contentFiltering/categories'

        return await self._session.get(metadata, resource)

