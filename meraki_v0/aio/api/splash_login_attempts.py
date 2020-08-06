class AsyncSplashLoginAttempts:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkSplashLoginAttempts(self, networkId: str, **kwargs):
        """
        **List the splash login attempts for a network**
        https://developer.cisco.com/meraki/api/#!get-network-splash-login-attempts
        
        - networkId (string)
        - ssidNumber (integer): Only return the login attempts for the specified SSID
        - loginIdentifier (string): The username, email, or phone number used during login
        - timespan (integer): The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months
        """

        kwargs.update(locals())

        if 'ssidNumber' in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs['ssidNumber'] in options, f'''"ssidNumber" cannot be "{kwargs['ssidNumber']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Splash login attempts'],
            'operation': 'getNetworkSplashLoginAttempts',
        }
        resource = f'/networks/{networkId}/splashLoginAttempts'

        query_params = ['ssidNumber', 'loginIdentifier', 'timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

