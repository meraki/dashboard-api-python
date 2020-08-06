class MGUplinkSettings(object):
    def __init__(self, session):
        super(MGUplinkSettings, self).__init__()
        self._session = session
    
    def getNetworkCellularGatewaySettingsUplink(self, networkId: str):
        """
        **Returns the uplink settings for your MG network.**
        https://developer.cisco.com/meraki/api/#!get-network-cellular-gateway-settings-uplink
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MG uplink settings'],
            'operation': 'getNetworkCellularGatewaySettingsUplink',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/uplink'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsUplink(self, networkId: str, **kwargs):
        """
        **Updates the uplink settings for your MG network.**
        https://developer.cisco.com/meraki/api/#!update-network-cellular-gateway-settings-uplink
        
        - networkId (string)
        - bandwidthLimits (object): The bandwidth settings for the 'cellular' uplink
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG uplink settings'],
            'operation': 'updateNetworkCellularGatewaySettingsUplink',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/uplink'

        body_params = ['bandwidthLimits']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

