class SplashSettings(object):
    def __init__(self, session):
        super(SplashSettings, self).__init__()
        self._session = session
    
    def getNetworkSsidSplashSettings(self, networkId: str, number: str):
        """
        **Display the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api/#!get-network-ssid-splash-settings
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['Splash settings'],
            'operation': 'getNetworkSsidSplashSettings',
        }
        resource = f'/networks/{networkId}/ssids/{number}/splashSettings'

        return self._session.get(metadata, resource)

    def updateNetworkSsidSplashSettings(self, networkId: str, number: str, **kwargs):
        """
        **Modify the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api/#!update-network-ssid-splash-settings
        
        - networkId (string)
        - number (string)
        - splashUrl (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
        - useSplashUrl (boolean): [optional] Boolean indicating whether the user will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Splash settings'],
            'operation': 'updateNetworkSsidSplashSettings',
        }
        resource = f'/networks/{networkId}/ssids/{number}/splashSettings'

        body_params = ['splashUrl', 'useSplashUrl']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

