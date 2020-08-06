class AsyncUplinkSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkUplinkSettings(self, networkId: str):
        """
        **Returns the uplink settings for your MX network.**
        https://developer.cisco.com/meraki/api/#!get-network-uplink-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Uplink settings'],
            'operation': 'getNetworkUplinkSettings',
        }
        resource = f'/networks/{networkId}/uplinkSettings'

        return await self._session.get(metadata, resource)

    async def updateNetworkUplinkSettings(self, networkId: str, **kwargs):
        """
        **Updates the uplink settings for your MX network.**
        https://developer.cisco.com/meraki/api/#!update-network-uplink-settings
        
        - networkId (string)
        - bandwidthLimits (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Uplink settings'],
            'operation': 'updateNetworkUplinkSettings',
        }
        resource = f'/networks/{networkId}/uplinkSettings'

        body_params = ['bandwidthLimits']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

