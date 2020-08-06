class AsyncMXCellularFirewall:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkCellularFirewallRules(self, networkId: str):
        """
        **Return the cellular firewall rules for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-cellular-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX cellular firewall'],
            'operation': 'getNetworkCellularFirewallRules',
        }
        resource = f'/networks/{networkId}/cellularFirewallRules'

        return await self._session.get(metadata, resource)

    async def updateNetworkCellularFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the cellular firewall rules of an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-cellular-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX cellular firewall'],
            'operation': 'updateNetworkCellularFirewallRules',
        }
        resource = f'/networks/{networkId}/cellularFirewallRules'

        body_params = ['rules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

