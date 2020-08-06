class MGDHCPSettings(object):
    def __init__(self, session):
        super(MGDHCPSettings, self).__init__()
        self._session = session
    
    def getNetworkCellularGatewaySettingsDhcp(self, networkId: str):
        """
        **List common DHCP settings of MGs**
        https://developer.cisco.com/meraki/api/#!get-network-cellular-gateway-settings-dhcp
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MG DHCP settings'],
            'operation': 'getNetworkCellularGatewaySettingsDhcp',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/dhcp'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsDhcp(self, networkId: str, **kwargs):
        """
        **Update common DHCP settings of MGs**
        https://developer.cisco.com/meraki/api/#!update-network-cellular-gateway-settings-dhcp
        
        - networkId (string)
        - dhcpLeaseTime (string): DHCP Lease time for all MG of the network. It can be '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
        - dnsNameservers (string): DNS name servers mode for all MG of the network. It can take 4 different values: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
        - dnsCustomNameservers (array): list of fixed IP representing the the DNS Name servers when the mode is 'custom'
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG DHCP settings'],
            'operation': 'updateNetworkCellularGatewaySettingsDhcp',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/dhcp'

        body_params = ['dhcpLeaseTime', 'dnsNameservers', 'dnsCustomNameservers']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

