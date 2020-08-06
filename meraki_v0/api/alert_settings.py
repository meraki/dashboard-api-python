class AlertSettings(object):
    def __init__(self, session):
        super(AlertSettings, self).__init__()
        self._session = session
    
    def getNetworkAlertSettings(self, networkId: str):
        """
        **Return the alert configuration for this network**
        https://developer.cisco.com/meraki/api/#!get-network-alert-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Alert settings'],
            'operation': 'getNetworkAlertSettings',
        }
        resource = f'/networks/{networkId}/alertSettings'

        return self._session.get(metadata, resource)

    def updateNetworkAlertSettings(self, networkId: str, **kwargs):
        """
        **Update the alert configuration for this network**
        https://developer.cisco.com/meraki/api/#!update-network-alert-settings
        
        - networkId (string)
        - defaultDestinations (object): The network-wide destinations for all alerts on the network.
        - alerts (array): Alert-specific configuration for each type. Only alerts that pertain to the network can be updated.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Alert settings'],
            'operation': 'updateNetworkAlertSettings',
        }
        resource = f'/networks/{networkId}/alertSettings'

        body_params = ['defaultDestinations', 'alerts']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

