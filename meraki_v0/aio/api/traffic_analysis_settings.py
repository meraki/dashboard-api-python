class AsyncTrafficAnalysisSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkTrafficAnalysisSettings(self, networkId: str):
        """
        **Return the traffic analysis settings for a network**
        https://developer.cisco.com/meraki/api/#!get-network-traffic-analysis-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic analysis settings'],
            'operation': 'getNetworkTrafficAnalysisSettings',
        }
        resource = f'/networks/{networkId}/trafficAnalysisSettings'

        return await self._session.get(metadata, resource)

    async def updateNetworkTrafficAnalysisSettings(self, networkId: str, **kwargs):
        """
        **Update the traffic analysis settings for a network**
        https://developer.cisco.com/meraki/api/#!update-network-traffic-analysis-settings
        
        - networkId (string)
        - mode (string):     The traffic analysis mode for the network. Can be one of 'disabled' (do not collect traffic types),
    'basic' (collect generic traffic categories), or 'detailed' (collect destination hostnames).

        - customPieChartItems (array): The list of items that make up the custom pie chart for traffic reporting.
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['disabled', 'basic', 'detailed']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Traffic analysis settings'],
            'operation': 'updateNetworkTrafficAnalysisSettings',
        }
        resource = f'/networks/{networkId}/trafficAnalysisSettings'

        body_params = ['mode', 'customPieChartItems']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

