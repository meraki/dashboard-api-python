class AsyncWirelessSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkWirelessSettings(self, networkId: str):
        """
        **Return the wireless settings for a network**
        https://developer.cisco.com/docs/meraki-api-v0/#!get-network-wireless-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Wireless settings'],
            'operation': 'getNetworkWirelessSettings',
        }
        resource = f'/networks/{networkId}/wireless/settings'

        return await self._session.get(metadata, resource)

    async def updateNetworkWirelessSettings(self, networkId: str, **kwargs):
        """
        **Update the wireless settings for a network**
        https://developer.cisco.com/docs/meraki-api-v0/#!update-network-wireless-settings
        
        - networkId (string)
        - meshingEnabled (boolean): Toggle for enabling or disabling meshing in a network
        - ipv6BridgeEnabled (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
        - locationAnalyticsEnabled (boolean): Toggle for enabling or disabling location analytics for your network
        - ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless settings'],
            'operation': 'updateNetworkWirelessSettings',
        }
        resource = f'/networks/{networkId}/wireless/settings'

        body_params = ['meshingEnabled', 'ipv6BridgeEnabled', 'locationAnalyticsEnabled', 'ledLightsOn']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

