class VLANs(object):
    def __init__(self, session):
        super(VLANs, self).__init__()
        self._session = session
    
    def getNetworkVlans(self, networkId: str):
        """
        **List the VLANs for an MX network**
        https://api.meraki.com/api_docs#list-the-vlans-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['VLANs'],
            'operation': 'getNetworkVlans',
        }
        resource = f'/networks/{networkId}/vlans'

        return self._session.get(metadata, resource)

    def createNetworkVlan(self, networkId: str, id: str, name: str, subnet: str, applianceIp: str):
        """
        **Add a VLAN**
        https://api.meraki.com/api_docs#add-a-vlan
        
        - networkId (string)
        - id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
        - name (string): The name of the new VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        """

        kwargs = locals()

        metadata = {
            'tags': ['VLANs'],
            'operation': 'createNetworkVlan',
        }
        resource = f'/networks/{networkId}/vlans'

        body_params = ['id', 'name', 'subnet', 'applianceIp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkVlan(self, networkId: str, vlanId: str):
        """
        **Return a VLAN**
        https://api.meraki.com/api_docs#return-a-vlan
        
        - networkId (string)
        - vlanId (string)
        """

        metadata = {
            'tags': ['VLANs'],
            'operation': 'getNetworkVlan',
        }
        resource = f'/networks/{networkId}/vlans/{vlanId}'

        return self._session.get(metadata, resource)

    def updateNetworkVlan(self, networkId: str, vlanId: str, **kwargs):
        """
        **Update a VLAN**
        https://api.meraki.com/api_docs#update-a-vlan
        
        - networkId (string)
        - vlanId (string)
        - name (string): The name of the VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        - vpnNatSubnet (string): The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN
        - dhcpHandling (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
        - dhcpRelayServerIps (array): The IPs of the DHCP servers that DHCP requests should be relayed to
        - dhcpLeaseTime (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
        - dhcpBootOptionsEnabled (boolean): Use DHCP boot options specified in other properties
        - dhcpBootNextServer (string): DHCP boot option to direct boot clients to the server to load the boot file from
        - dhcpBootFilename (string): DHCP boot option for boot filename
        - fixedIpAssignments (object): The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
        - reservedIpRanges (array): The DHCP reserved IP ranges on the VLAN
        - dnsNameservers (string): The DNS nameservers used for DHCP responses, either "upstream_dns", "google_dns", "opendns", or a newline seperated string of IP addresses or domain names
        - dhcpOptions (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
        """

        kwargs.update(locals())

        if 'dhcpHandling' in kwargs:
            options = ['Run a DHCP server', 'Relay DHCP to another server', 'Do not respond to DHCP requests']
            assert kwargs['dhcpHandling'] in options, f'''"dhcpHandling" cannot be "{kwargs['dhcpHandling']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['30 minutes', '1 hour', '4 hours', '12 hours', '1 day', '1 week']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['VLANs'],
            'operation': 'updateNetworkVlan',
        }
        resource = f'/networks/{networkId}/vlans/{vlanId}'

        body_params = ['name', 'subnet', 'applianceIp', 'vpnNatSubnet', 'dhcpHandling', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dhcpBootOptionsEnabled', 'dhcpBootNextServer', 'dhcpBootFilename', 'fixedIpAssignments', 'reservedIpRanges', 'dnsNameservers', 'dhcpOptions']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkVlan(self, networkId: str, vlanId: str):
        """
        **Delete a VLAN from a network**
        https://api.meraki.com/api_docs#delete-a-vlan-from-a-network
        
        - networkId (string)
        - vlanId (string)
        """

        metadata = {
            'tags': ['VLANs'],
            'operation': 'deleteNetworkVlan',
        }
        resource = f'/networks/{networkId}/vlans/{vlanId}'

        return self._session.delete(metadata, resource)

    def getNetworkVlansEnabledState(self, networkId: str):
        """
        **Returns the enabled status of VLANs for the network**
        https://api.meraki.com/api_docs#returns-the-enabled-status-of-vlans-for-the-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['VLANs'],
            'operation': 'getNetworkVlansEnabledState',
        }
        resource = f'/networks/{networkId}/vlansEnabledState'

        return self._session.get(metadata, resource)

    def updateNetworkVlansEnabledState(self, networkId: str, enabled: bool):
        """
        **Enable/Disable VLANs for the given network**
        https://api.meraki.com/api_docs#enable/disable-vlans-for-the-given-network
        
        - networkId (string)
        - enabled (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network
        """

        kwargs = locals()

        metadata = {
            'tags': ['VLANs'],
            'operation': 'updateNetworkVlansEnabledState',
        }
        resource = f'/networks/{networkId}/vlansEnabledState'

        body_params = ['enabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

