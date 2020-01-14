class MXVPNFirewall(object):
    def __init__(self, session):
        super(MXVPNFirewall, self).__init__()
        self._session = session
    
    def getOrganizationVpnFirewallRules(self, organizationId: str):
        """
        **Return the firewall rules for an organization's site-to-site VPN**
        https://api.meraki.com/api_docs#return-the-firewall-rules-for-an-organizations-site-to-site-vpn
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['MX VPN firewall'],
            'operation': 'getOrganizationVpnFirewallRules',
        }
        resource = f'/organizations/{organizationId}/vpnFirewallRules'

        return self._session.get(metadata, resource)

    def updateOrganizationVpnFirewallRules(self, organizationId: str, **kwargs):
        """
        **Update the firewall rules of an organization's site-to-site VPN**
        https://api.meraki.com/api_docs#update-the-firewall-rules-of-an-organizations-site-to-site-vpn
        
        - organizationId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX VPN firewall'],
            'operation': 'updateOrganizationVpnFirewallRules',
        }
        resource = f'/organizations/{organizationId}/vpnFirewallRules'

        body_params = ['rules', 'syslogDefaultRule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

