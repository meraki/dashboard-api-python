class ContentFilteringRules(object):
    def __init__(self, session):
        super(ContentFilteringRules, self).__init__()
        self._session = session
    
    def getNetworkContentFiltering(self, networkId: str):
        """
        **Return the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-content-filtering
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Content filtering rules'],
            'operation': 'getNetworkContentFiltering',
        }
        resource = f'/networks/{networkId}/contentFiltering'

        return self._session.get(metadata, resource)

    def updateNetworkContentFiltering(self, networkId: str, **kwargs):
        """
        **Update the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-content-filtering
        
        - networkId (string)
        - allowedUrlPatterns (array): A list of URL patterns that are allowed
        - blockedUrlPatterns (array): A list of URL patterns that are blocked
        - blockedUrlCategories (array): A list of URL categories to block
        - urlCategoryListSize (string): URL category list size which is either 'topSites' or 'fullList'
        """

        kwargs.update(locals())

        if 'urlCategoryListSize' in kwargs:
            options = ['topSites', 'fullList']
            assert kwargs['urlCategoryListSize'] in options, f'''"urlCategoryListSize" cannot be "{kwargs['urlCategoryListSize']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Content filtering rules'],
            'operation': 'updateNetworkContentFiltering',
        }
        resource = f'/networks/{networkId}/contentFiltering'

        body_params = ['allowedUrlPatterns', 'blockedUrlPatterns', 'blockedUrlCategories', 'urlCategoryListSize']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

