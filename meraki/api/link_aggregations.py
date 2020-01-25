class LinkAggregations(object):
    def __init__(self, session):
        super(LinkAggregations, self).__init__()
        self._session = session
    
    def getNetworkSwitchLinkAggregations(self, networkId: str):
        """
        **List link aggregation groups**
        https://api.meraki.com/api_docs#list-link-aggregation-groups
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Link aggregations'],
            'operation': 'getNetworkSwitchLinkAggregations',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations'

        return self._session.get(metadata, resource)

    def createNetworkSwitchLinkAggregation(self, networkId: str, **kwargs):
        """
        **Create a link aggregation group**
        https://api.meraki.com/api_docs#create-a-link-aggregation-group
        
        - networkId (string)
        - switchPorts (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Link aggregations'],
            'operation': 'createNetworkSwitchLinkAggregation',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations'

        body_params = ['switchPorts', 'switchProfilePorts']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def updateNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str, **kwargs):
        """
        **Update a link aggregation group**
        https://api.meraki.com/api_docs#update-a-link-aggregation-group
        
        - networkId (string)
        - linkAggregationId (string)
        - switchPorts (array): Array of switch or stack ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Link aggregations'],
            'operation': 'updateNetworkSwitchLinkAggregation',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        body_params = ['switchPorts', 'switchProfilePorts']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str):
        """
        **Split a link aggregation group into separate ports**
        https://api.meraki.com/api_docs#split-a-link-aggregation-group-into-separate-ports
        
        - networkId (string)
        - linkAggregationId (string)
        """

        metadata = {
            'tags': ['Link aggregations'],
            'operation': 'deleteNetworkSwitchLinkAggregation',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        return self._session.delete(metadata, resource)

