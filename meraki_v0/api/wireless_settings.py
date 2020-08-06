class WirelessSettings(object):
    def __init__(self, session):
        super(WirelessSettings, self).__init__()
        self._session = session
    
    def getNetworkWirelessSettings(self, networkId: str):
        """
        **Return the wireless settings for a network**
        https://developer.cisco.com/meraki/api/#!get-network-wireless-settings
        
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
        https://developer.cisco.com/meraki/api/#!update-network-wireless-settings
        
        - networkId (string)
        - meshingEnabled (boolean): Toggle for enabling or disabling meshing in a network
        - ipv6BridgeEnabled (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
        - locationAnalyticsEnabled (boolean): Toggle for enabling or disabling location analytics for your network
        - upgradeStrategy (string): The upgrade strategy to apply to the network. Must be one of 'minimizeUpgradeTime' or 'minimizeClientDowntime'. Requires firmware version MR 26.8 or higher'
        - ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
        """

        kwargs.update(locals())

        if 'upgradeStrategy' in kwargs:
            options = ['minimizeUpgradeTime', 'minimizeClientDowntime']
            assert kwargs['upgradeStrategy'] in options, f'''"upgradeStrategy" cannot be "{kwargs['upgradeStrategy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless settings'],
            'operation': 'updateNetworkWirelessSettings',
        }
        resource = f'/networks/{networkId}/wireless/settings'

        body_params = ['meshingEnabled', 'ipv6BridgeEnabled', 'locationAnalyticsEnabled', 'upgradeStrategy', 'ledLightsOn']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

