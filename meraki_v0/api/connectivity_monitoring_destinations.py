class ConnectivityMonitoringDestinations(object):
    def __init__(self, session):
        super(ConnectivityMonitoringDestinations, self).__init__()
        self._session = session
    
    def getNetworkConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-connectivity-monitoring-destinations
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Connectivity monitoring destinations'],
            'operation': 'getNetworkConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)

    def updateNetworkConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-connectivity-monitoring-destinations
        
        - networkId (string)
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Connectivity monitoring destinations'],
            'operation': 'updateNetworkConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/connectivityMonitoringDestinations'

        body_params = ['destinations']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

