class SplashLoginAttempts(object):
    def __init__(self, session):
        super(SplashLoginAttempts, self).__init__()
        self._session = session
    
    def getNetworkSplashLoginAttempts(self, networkId: str, **kwargs):
        """
        **List the splash login attempts for a network**
        https://api.meraki.com/api_docs#list-the-splash-login-attempts-for-a-network
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

