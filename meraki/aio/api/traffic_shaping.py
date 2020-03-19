class AsyncTrafficShaping:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def updateNetworkSsidTrafficShaping(self, networkId: str, number: str, **kwargs):
        """
        **Update the traffic shaping settings for an SSID on an MR network**
        https://api.meraki.com/api_docs#update-the-traffic-shaping-settings-for-an-ssid-on-an-mr-network
        
        - networkId (string)
        - number (string)
        - trafficShapingEnabled (boolean): Whether traffic shaping rules are applied to clients on your SSID.
        - defaultRulesEnabled (boolean):     Whether default traffic shaping rules are enabled (true) or disabled (false).
    There are 4 default rules, which can
    be seen on your network's traffic shaping page. Note that default rules
    count against the rule limit of 8.

        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'updateNetworkSsidTrafficShaping',
        }
        resource = f'/networks/{networkId}/ssids/{number}/trafficShaping'

        body_params = ['trafficShapingEnabled', 'defaultRulesEnabled', 'rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkSsidTrafficShaping(self, networkId: str, number: str):
        """
        **Display the traffic shaping settings for a SSID on an MR network**
        https://api.meraki.com/api_docs#display-the-traffic-shaping-settings-for-a-ssid-on-an-mr-network
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkSsidTrafficShaping',
        }
        resource = f'/networks/{networkId}/ssids/{number}/trafficShaping'

        return await self._session.get(metadata, resource)

    async def updateNetworkTrafficShaping(self, networkId: str, **kwargs):
        """
        **Update the traffic shaping settings for an MX network**
        https://api.meraki.com/api_docs#update-the-traffic-shaping-settings-for-an-mx-network
        
        - networkId (string)
        - defaultRulesEnabled (boolean):     Whether default traffic shaping rules are enabled (true) or disabled (false).
    There are 4 default rules, which can
    be seen on your network's traffic shaping page. Note that default rules
    count against the rule limit of 8.

        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'updateNetworkTrafficShaping',
        }
        resource = f'/networks/{networkId}/trafficShaping'

        body_params = ['defaultRulesEnabled', 'rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkTrafficShaping(self, networkId: str):
        """
        **Display the traffic shaping settings for an MX network**
        https://api.meraki.com/api_docs#display-the-traffic-shaping-settings-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkTrafficShaping',
        }
        resource = f'/networks/{networkId}/trafficShaping'

        return await self._session.get(metadata, resource)

    async def getNetworkTrafficShapingApplicationCategories(self, networkId: str):
        """
        **Returns the application categories for traffic shaping rules.**
        https://api.meraki.com/api_docs#returns-the-application-categories-for-traffic-shaping-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkTrafficShapingApplicationCategories',
        }
        resource = f'/networks/{networkId}/trafficShaping/applicationCategories'

        return await self._session.get(metadata, resource)

    async def getNetworkTrafficShapingDscpTaggingOptions(self, networkId: str):
        """
        **Returns the available DSCP tagging options for your traffic shaping rules.**
        https://api.meraki.com/api_docs#returns-the-available-dscp-tagging-options-for-your-traffic-shaping-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkTrafficShapingDscpTaggingOptions',
        }
        resource = f'/networks/{networkId}/trafficShaping/dscpTaggingOptions'

        return await self._session.get(metadata, resource)

