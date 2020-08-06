class AsyncMXInboundFirewall:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkApplianceFirewallInboundFirewallRules(self, networkId: str):
        """
        **Return the inbound firewall rules for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-appliance-firewall-inbound-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX inbound firewall'],
            'operation': 'getNetworkApplianceFirewallInboundFirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/inboundFirewallRules'

        return await self._session.get(metadata, resource)

    async def updateNetworkApplianceFirewallInboundFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the inbound firewall rules of an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-appliance-firewall-inbound-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX inbound firewall'],
            'operation': 'updateNetworkApplianceFirewallInboundFirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/inboundFirewallRules'

        body_params = ['rules', 'syslogDefaultRule']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

