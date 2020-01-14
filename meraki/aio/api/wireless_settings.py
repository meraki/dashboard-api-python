class WirelessSettings(object):
    def __init__(self, session):
        super(WirelessSettings, self).__init__()
        self._session = session
    
    def getNetworkWirelessSettings(self, networkId: str):
        """
        **Return the wireless settings for a network**
        https://api.meraki.com/api_docs#return-the-wireless-settings-for-a-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Wireless settings'],
            'operation': 'getNetworkWirelessSettings',
        }
        resource = f'/networks/{networkId}/wireless/settings'

        return self._session.get(metadata, resource)

    def updateNetworkWirelessSettings(self, networkId: str, **kwargs):
        """
        **Update the wireless settings for a network**
        https://api.meraki.com/api_docs#update-the-wireless-settings-for-a-network
        
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

        return self._session.put(metadata, resource, payload)

