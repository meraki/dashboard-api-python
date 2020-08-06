class MRL3Firewall(object):
    def __init__(self, session):
        super(MRL3Firewall, self).__init__()
        self._session = session
    
    def getNetworkSsidL3FirewallRules(self, networkId: str, number: str):
        """
        **Return the L3 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api/#!get-network-ssid-l-3-firewall-rules
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['MR L3 firewall'],
            'operation': 'getNetworkSsidL3FirewallRules',
        }
        resource = f'/networks/{networkId}/ssids/{number}/l3FirewallRules'

        return self._session.get(metadata, resource)

    def updateNetworkSsidL3FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L3 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/meraki/api/#!update-network-ssid-l-3-firewall-rules
        
        - networkId (string)
        - number (string)
        - rules (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule)
        - allowLanAccess (boolean): Allow wireless client access to local LAN (boolean value - true allows access and false denies access) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MR L3 firewall'],
            'operation': 'updateNetworkSsidL3FirewallRules',
        }
        resource = f'/networks/{networkId}/ssids/{number}/l3FirewallRules'

        body_params = ['rules', 'allowLanAccess']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

