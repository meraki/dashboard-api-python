class MGConnectivityMonitoringDestinations(object):
    def __init__(self, session):
        super(MGConnectivityMonitoringDestinations, self).__init__()
        self._session = session
    
    def getNetworkCellularGatewaySettingsConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MG network**
        https://developer.cisco.com/meraki/api/#!get-network-cellular-gateway-settings-connectivity-monitoring-destinations
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MG connectivity monitoring destinations'],
            'operation': 'getNetworkCellularGatewaySettingsConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MG network**
        https://developer.cisco.com/meraki/api/#!update-network-cellular-gateway-settings-connectivity-monitoring-destinations
        
        - networkId (string)
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG connectivity monitoring destinations'],
            'operation': 'updateNetworkCellularGatewaySettingsConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/connectivityMonitoringDestinations'

        body_params = ['destinations']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

