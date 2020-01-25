class MXL3Firewall(object):
    def __init__(self, session):
        super(MXL3Firewall, self).__init__()
        self._session = session
    
    def getNetworkL3FirewallRules(self, networkId: str):
        """
        **Return the L3 firewall rules for an MX network**
        https://api.meraki.com/api_docs#return-the-l3-firewall-rules-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX L3 firewall'],
            'operation': 'getNetworkL3FirewallRules',
        }
        resource = f'/networks/{networkId}/l3FirewallRules'

        return self._session.get(metadata, resource)

    def updateNetworkL3FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the L3 firewall rules of an MX network**
        https://api.meraki.com/api_docs#update-the-l3-firewall-rules-of-an-mx-network
        
        - networkId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX L3 firewall'],
            'operation': 'updateNetworkL3FirewallRules',
        }
        resource = f'/networks/{networkId}/l3FirewallRules'

        body_params = ['rules', 'syslogDefaultRule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

