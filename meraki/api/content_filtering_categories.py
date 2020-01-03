class ContentFilteringCategories(object):
    def __init__(self, session):
        super(ContentFilteringCategories, self).__init__()
        self._session = session
    
    def getNetworkContentFilteringCategories(self, networkId: str):
        """
        **List all available content filtering categories for an MX network**
        https://api.meraki.com/api_docs#list-all-available-content-filtering-categories-for-an-mx-network
        - networkId (string)
        """

        metadata = {
            'tags': ['Content filtering categories'],
            'operation': 'getNetworkContentFilteringCategories',
        }
        resource = f'/networks/{networkId}/contentFiltering/categories'

        return self._session.get(metadata, resource)

