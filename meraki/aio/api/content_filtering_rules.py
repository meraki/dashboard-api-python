class AsyncContentFilteringRules:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkContentFiltering(self, networkId: str):
        """
        **Return the content filtering settings for an MX network**
        https://api.meraki.com/api_docs#return-the-content-filtering-settings-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Content filtering rules'],
            'operation': 'getNetworkContentFiltering',
        }
        resource = f'/networks/{networkId}/contentFiltering'

        return await self._session.get(metadata, resource)

    async def updateNetworkContentFiltering(self, networkId: str, **kwargs):
        """
        **Update the content filtering settings for an MX network**
        https://api.meraki.com/api_docs#update-the-content-filtering-settings-for-an-mx-network
        
        - networkId (string)
        - allowedUrlPatterns (array): A whitelist of URL patterns to allow
        - blockedUrlPatterns (array): A blacklist of URL patterns to block
        - blockedUrlCategories (array): A list of URL categories to block
        - urlCategoryListSize (string): URL category list size which is either 'topSites' or 'fullList'
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Content filtering rules'],
            'operation': 'updateNetworkContentFiltering',
        }
        resource = f'/networks/{networkId}/contentFiltering'

        body_params = ['allowedUrlPatterns', 'blockedUrlPatterns', 'blockedUrlCategories', 'urlCategoryListSize']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

