class TrafficShaping(object):
    def __init__(self, session):
        super(TrafficShaping, self).__init__()
        self._session = session
    
    def updateNetworkSsidTrafficShaping(self, networkId: str, number: str, **kwargs):
        """
        **Update the traffic shaping settings for an SSID on an MR network**
        https://developer.cisco.com/meraki/api/#!update-network-ssid-traffic-shaping
        
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
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSsidTrafficShaping(self, networkId: str, number: str):
        """
        **Display the traffic shaping settings for a SSID on an MR network**
        https://developer.cisco.com/meraki/api/#!get-network-ssid-traffic-shaping
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkSsidTrafficShaping',
        }
        resource = f'/networks/{networkId}/ssids/{number}/trafficShaping'

        return self._session.get(metadata, resource)

    def updateNetworkTrafficShaping(self, networkId: str, **kwargs):
        """
        **Update the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-traffic-shaping
        
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
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkTrafficShaping(self, networkId: str):
        """
        **Display the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-traffic-shaping
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkTrafficShaping',
        }
        resource = f'/networks/{networkId}/trafficShaping'

        return self._session.get(metadata, resource)

    def getNetworkTrafficShapingApplicationCategories(self, networkId: str):
        """
        **Returns the application categories for traffic shaping rules.**
        https://developer.cisco.com/meraki/api/#!get-network-traffic-shaping-application-categories
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkTrafficShapingApplicationCategories',
        }
        resource = f'/networks/{networkId}/trafficShaping/applicationCategories'

        return self._session.get(metadata, resource)

    def getNetworkTrafficShapingDscpTaggingOptions(self, networkId: str):
        """
        **Returns the available DSCP tagging options for your traffic shaping rules.**
        https://developer.cisco.com/meraki/api/#!get-network-traffic-shaping-dscp-tagging-options
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Traffic shaping'],
            'operation': 'getNetworkTrafficShapingDscpTaggingOptions',
        }
        resource = f'/networks/{networkId}/trafficShaping/dscpTaggingOptions'

        return self._session.get(metadata, resource)

