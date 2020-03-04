class AsyncMGUplinkSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkCellularGatewaySettingsUplink(self, networkId: str):
        """
        **Returns the uplink settings for your MG network.**
        https://api.meraki.com/api_docs#returns-the-uplink-settings-for-your-mg-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MG uplink settings'],
            'operation': 'getNetworkCellularGatewaySettingsUplink',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/uplink'

        return await self._session.get(metadata, resource)

    async def updateNetworkCellularGatewaySettingsUplink(self, networkId: str, **kwargs):
        """
        **Updates the uplink settings for your MG network.**
        https://api.meraki.com/api_docs#updates-the-uplink-settings-for-your-mg-network
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

