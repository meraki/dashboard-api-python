class AsyncMXVPNFirewall:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationVpnFirewallRules(self, organizationId: str):
        """
        **Return the firewall rules for an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api/#!get-organization-vpn-firewall-rules
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['MX VPN firewall'],
            'operation': 'getOrganizationVpnFirewallRules',
        }
        resource = f'/organizations/{organizationId}/vpnFirewallRules'

        return await self._session.get(metadata, resource)

    async def updateOrganizationVpnFirewallRules(self, organizationId: str, **kwargs):
        """
        **Update the firewall rules of an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api/#!update-organization-vpn-firewall-rules
        
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
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

