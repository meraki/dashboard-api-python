class NetFlowSettings(object):
    def __init__(self, session):
        super(NetFlowSettings, self).__init__()
        self._session = session
    
    def getNetworkNetflowSettings(self, networkId: str):
        """
        **Return the NetFlow traffic reporting settings for a network**
        https://api.meraki.com/api_docs#return-the-netflow-traffic-reporting-settings-for-a-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['NetFlow settings'],
            'operation': 'getNetworkNetflowSettings',
        }
        resource = f'/networks/{networkId}/netflowSettings'

        return self._session.get(metadata, resource)

    def updateNetworkNetflowSettings(self, networkId: str, **kwargs):
        """
        **Update the NetFlow traffic reporting settings for a network**
        https://api.meraki.com/api_docs#update-the-netflow-traffic-reporting-settings-for-a-network
        
        - networkId (string)
        - reportingEnabled (boolean): Boolean indicating whether NetFlow traffic reporting is enabled (true) or disabled (false).
        - collectorIp (string): The IPv4 address of the NetFlow collector.
        - collectorPort (integer): The port that the NetFlow collector will be listening on.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['NetFlow settings'],
            'operation': 'updateNetworkNetflowSettings',
        }
        resource = f'/networks/{networkId}/netflowSettings'

        body_params = ['reportingEnabled', 'collectorIp', 'collectorPort']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

