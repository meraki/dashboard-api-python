import urllib


class Switch(object):
    def __init__(self, session):
        super(Switch, self).__init__()
        self._session = session
        


    def getDeviceSwitchPorts(self, serial: str):
        """
        **List the switch ports for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports

        - serial (string): Serial
        """

        metadata = {
            'tags': ['switch', 'configure', 'ports'],
            'operation': 'getDeviceSwitchPorts'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/ports'

        return self._session.get(metadata, resource)
        


    def cycleDeviceSwitchPorts(self, serial: str, ports: list):
        """
        **Cycle a set of switch ports**
        https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

        - serial (string): Serial
        - ports (array): List of switch ports
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'liveTools', 'ports'],
            'operation': 'cycleDeviceSwitchPorts'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/ports/cycle'

        body_params = ['ports', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getDeviceSwitchPortsStatuses(self, serial: str, **kwargs):
        """
        **Return the status for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'monitor', 'ports', 'statuses'],
            'operation': 'getDeviceSwitchPortsStatuses'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/ports/statuses'

        query_params = ['t0', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceSwitchPortsStatusesPackets(self, serial: str, **kwargs):
        """
        **Return the packet counters for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'monitor', 'ports', 'statuses', 'packets'],
            'operation': 'getDeviceSwitchPortsStatusesPackets'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/ports/statuses/packets'

        query_params = ['t0', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceSwitchPort(self, serial: str, portId: str):
        """
        **Return a switch port**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port

        - serial (string): Serial
        - portId (string): Port ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'ports'],
            'operation': 'getDeviceSwitchPort'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        portId = urllib.parse.quote(str(portId), safe='')
        resource = f'/devices/{serial}/switch/ports/{portId}'

        return self._session.get(metadata, resource)
        


    def updateDeviceSwitchPort(self, serial: str, portId: str, **kwargs):
        """
        **Update a switch port**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port

        - serial (string): Serial
        - portId (string): Port ID
        - name (string): The name of the switch port.
        - tags (array): The list of tags of the switch port.
        - enabled (boolean): The status of the switch port.
        - poeEnabled (boolean): The PoE status of the switch port.
        - type (string): The type of the switch port ('trunk' or 'access').
        - vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
        - isolationEnabled (boolean): The isolation status of the switch port.
        - rstpEnabled (boolean): The rapid spanning tree protocol status.
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
        - linkNegotiation (string): The link speed for the switch port.
        - portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
        - udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
        - accessPolicyType (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.
        - accessPolicyNumber (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
        - macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'.
        - stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stormControlEnabled (boolean): The storm control status of the switch port.
        - adaptivePolicyGroupId (string): The adaptive policy group ID that will be used to tag traffic through this switch port. This ID must pre-exist during the configuration, else needs to be created using adaptivePolicy/groups API. Cannot be applied to a port on a switch bound to profile.
        - peerSgtCapable (boolean): If true, Peer SGT is enabled for traffic through this switch port. Applicable to trunk port only, not access port. Cannot be applied to a port on a switch bound to profile.
        - flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
        - daiTrusted (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
        - profile (object): Profile attributes
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['access', 'trunk']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''
        if 'stpGuard' in kwargs:
            options = ['bpdu guard', 'disabled', 'loop guard', 'root guard']
            assert kwargs['stpGuard'] in options, f'''"stpGuard" cannot be "{kwargs['stpGuard']}", & must be set to one of: {options}'''
        if 'udld' in kwargs:
            options = ['Alert only', 'Enforce']
            assert kwargs['udld'] in options, f'''"udld" cannot be "{kwargs['udld']}", & must be set to one of: {options}'''
        if 'accessPolicyType' in kwargs:
            options = ['Custom access policy', 'MAC allow list', 'Open', 'Sticky MAC allow list']
            assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'ports'],
            'operation': 'updateDeviceSwitchPort'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        portId = urllib.parse.quote(str(portId), safe='')
        resource = f'/devices/{serial}/switch/ports/{portId}'

        body_params = ['name', 'tags', 'enabled', 'poeEnabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macAllowList', 'stickyMacAllowList', 'stickyMacAllowListLimit', 'stormControlEnabled', 'adaptivePolicyGroupId', 'peerSgtCapable', 'flexibleStackingEnabled', 'daiTrusted', 'profile', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceSwitchRoutingInterfaces(self, serial: str):
        """
        **List layer 3 interfaces for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces

        - serial (string): Serial
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces'],
            'operation': 'getDeviceSwitchRoutingInterfaces'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces'

        return self._session.get(metadata, resource)
        


    def createDeviceSwitchRoutingInterface(self, serial: str, **kwargs):
        """
        **Create a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

        - serial (string): Serial
        - name (string): A friendly name or description for the interface or VLAN.
        - subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch's management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ospfV3 (object): The OSPFv3 routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        """

        kwargs.update(locals())

        if 'multicastRouting' in kwargs:
            options = ['IGMP snooping querier', 'disabled', 'enabled']
            assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces'],
            'operation': 'createDeviceSwitchRoutingInterface'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ospfV3', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str):
        """
        **Return a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces'],
            'operation': 'getDeviceSwitchRoutingInterface'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

        return self._session.get(metadata, resource)
        


    def updateDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str, **kwargs):
        """
        **Update a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        - name (string): A friendly name or description for the interface or VLAN.
        - subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same         as the switch's management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a routed interface. Required if this is the first IPv4 interface.
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ospfV3 (object): The OSPFv3 routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        """

        kwargs.update(locals())

        if 'multicastRouting' in kwargs:
            options = ['IGMP snooping querier', 'disabled', 'enabled']
            assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces'],
            'operation': 'updateDeviceSwitchRoutingInterface'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ospfV3', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str):
        """
        **Delete a layer 3 interface from the switch**
        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces'],
            'operation': 'deleteDeviceSwitchRoutingInterface'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

        return self._session.delete(metadata, resource)
        


    def getDeviceSwitchRoutingInterfaceDhcp(self, serial: str, interfaceId: str):
        """
        **Return a layer 3 interface DHCP configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface-dhcp

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces', 'dhcp'],
            'operation': 'getDeviceSwitchRoutingInterfaceDhcp'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp'

        return self._session.get(metadata, resource)
        


    def updateDeviceSwitchRoutingInterfaceDhcp(self, serial: str, interfaceId: str, **kwargs):
        """
        **Update a layer 3 interface DHCP configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp

        - serial (string): Serial
        - interfaceId (string): Interface ID
        - dhcpMode (string): The DHCP mode options for the switch interface
       ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
        - dhcpRelayServerIps (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch interface
        - dhcpLeaseTime (string): The DHCP lease time config for the dhcp server running on switch interface
        ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
        - dnsNameserversOption (string): The DHCP name server option for the dhcp server running on the switch interface
        ('googlePublicDns', 'openDns' or 'custom')
        - dnsCustomNameservers (array): The DHCP name server IPs when DHCP name server option is
        'custom'
        - bootOptionsEnabled (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch
        interface
        - bootNextServer (string): The PXE boot server IP for the DHCP server running on the switch interface
        - bootFileName (string): The PXE boot server filename for the DHCP server running on the switch interface
        - dhcpOptions (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch interface
        - reservedIpRanges (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch interface
        - fixedIpAssignments (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch interface
        """

        kwargs.update(locals())

        if 'dhcpMode' in kwargs:
            options = ['dhcpDisabled', 'dhcpRelay', 'dhcpServer']
            assert kwargs['dhcpMode'] in options, f'''"dhcpMode" cannot be "{kwargs['dhcpMode']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['1 day', '1 hour', '1 week', '12 hours', '30 minutes', '4 hours']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''
        if 'dnsNameserversOption' in kwargs:
            options = ['custom', 'googlePublicDns', 'openDns']
            assert kwargs['dnsNameserversOption'] in options, f'''"dnsNameserversOption" cannot be "{kwargs['dnsNameserversOption']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'interfaces', 'dhcp'],
            'operation': 'updateDeviceSwitchRoutingInterfaceDhcp'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp'

        body_params = ['dhcpMode', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dnsNameserversOption', 'dnsCustomNameservers', 'bootOptionsEnabled', 'bootNextServer', 'bootFileName', 'dhcpOptions', 'reservedIpRanges', 'fixedIpAssignments', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceSwitchRoutingStaticRoutes(self, serial: str):
        """
        **List layer 3 static routes for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-routes

        - serial (string): Serial
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
            'operation': 'getDeviceSwitchRoutingStaticRoutes'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/routing/staticRoutes'

        return self._session.get(metadata, resource)
        


    def createDeviceSwitchRoutingStaticRoute(self, serial: str, subnet: str, nextHopIp: str, **kwargs):
        """
        **Create a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-static-route

        - serial (string): Serial
        - subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
        - nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
        - name (string): Name or description for layer 3 static route
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
            'operation': 'createDeviceSwitchRoutingStaticRoute'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/routing/staticRoutes'

        body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str):
        """
        **Return a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
            'operation': 'getDeviceSwitchRoutingStaticRoute'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

        return self._session.get(metadata, resource)
        


    def updateDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str, **kwargs):
        """
        **Update a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        - name (string): Name or description for layer 3 static route
        - subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
        - nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
            'operation': 'updateDeviceSwitchRoutingStaticRoute'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str):
        """
        **Delete a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
            'operation': 'deleteDeviceSwitchRoutingStaticRoute'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

        return self._session.delete(metadata, resource)
        


    def getDeviceSwitchWarmSpare(self, serial: str):
        """
        **Return warm spare configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-warm-spare

        - serial (string): Serial
        """

        metadata = {
            'tags': ['switch', 'configure', 'warmSpare'],
            'operation': 'getDeviceSwitchWarmSpare'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/warmSpare'

        return self._session.get(metadata, resource)
        


    def updateDeviceSwitchWarmSpare(self, serial: str, enabled: bool, **kwargs):
        """
        **Update warm spare configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare

        - serial (string): Serial
        - enabled (boolean): Enable or disable warm spare for a switch
        - spareSerial (string): Serial number of the warm spare switch
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'warmSpare'],
            'operation': 'updateDeviceSwitchWarmSpare'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/switch/warmSpare'

        body_params = ['enabled', 'spareSerial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchAccessControlLists(self, networkId: str):
        """
        **Return the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'accessControlLists'],
            'operation': 'getNetworkSwitchAccessControlLists'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/accessControlLists'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchAccessControlLists(self, networkId: str, rules: list):
        """
        **Update the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-control-lists

        - networkId (string): Network ID
        - rules (array): An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'accessControlLists'],
            'operation': 'updateNetworkSwitchAccessControlLists'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/accessControlLists'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchAccessPolicies(self, networkId: str):
        """
        **List the access policies for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'accessPolicies'],
            'operation': 'getNetworkSwitchAccessPolicies'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/accessPolicies'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchAccessPolicy(self, networkId: str, name: str, radiusServers: list, radiusTestingEnabled: bool, radiusCoaSupportEnabled: bool, radiusAccountingEnabled: bool, hostMode: str, urlRedirectWalledGardenEnabled: bool, **kwargs):
        """
        **Create an access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

        - networkId (string): Network ID
        - name (string): Name of the access policy
        - radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
        - radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
        - radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
        - radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
        - hostMode (string): Choose the Host Mode for the access policy.
        - urlRedirectWalledGardenEnabled (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
        - radius (object): Object for RADIUS Settings
        - guestPortBouncing (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
        - radiusAccountingServers (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
        - radiusGroupAttribute (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
        - accessPolicyType (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
        - increaseAccessSpeed (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
        - guestVlanId (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
        - dot1x (object): 802.1x Settings
        - voiceVlanClients (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
        - urlRedirectWalledGardenRanges (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
        """

        kwargs.update(locals())

        if 'hostMode' in kwargs:
            options = ['Multi-Auth', 'Multi-Domain', 'Multi-Host', 'Single-Host']
            assert kwargs['hostMode'] in options, f'''"hostMode" cannot be "{kwargs['hostMode']}", & must be set to one of: {options}'''
        if 'accessPolicyType' in kwargs:
            options = ['802.1x', 'Hybrid authentication', 'MAC authentication bypass']
            assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'accessPolicies'],
            'operation': 'createNetworkSwitchAccessPolicy'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/accessPolicies'

        body_params = ['name', 'radiusServers', 'radius', 'guestPortBouncing', 'radiusTestingEnabled', 'radiusCoaSupportEnabled', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusGroupAttribute', 'hostMode', 'accessPolicyType', 'increaseAccessSpeed', 'guestVlanId', 'dot1x', 'voiceVlanClients', 'urlRedirectWalledGardenEnabled', 'urlRedirectWalledGardenRanges', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str):
        """
        **Return a specific access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        """

        metadata = {
            'tags': ['switch', 'configure', 'accessPolicies'],
            'operation': 'getNetworkSwitchAccessPolicy'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        accessPolicyNumber = urllib.parse.quote(str(accessPolicyNumber), safe='')
        resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str, **kwargs):
        """
        **Update an access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        - name (string): Name of the access policy
        - radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
        - radius (object): Object for RADIUS Settings
        - guestPortBouncing (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
        - radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
        - radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
        - radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
        - radiusAccountingServers (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
        - radiusGroupAttribute (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
        - hostMode (string): Choose the Host Mode for the access policy.
        - accessPolicyType (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
        - increaseAccessSpeed (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
        - guestVlanId (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
        - dot1x (object): 802.1x Settings
        - voiceVlanClients (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
        - urlRedirectWalledGardenEnabled (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
        - urlRedirectWalledGardenRanges (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
        """

        kwargs.update(locals())

        if 'hostMode' in kwargs:
            options = ['Multi-Auth', 'Multi-Domain', 'Multi-Host', 'Single-Host']
            assert kwargs['hostMode'] in options, f'''"hostMode" cannot be "{kwargs['hostMode']}", & must be set to one of: {options}'''
        if 'accessPolicyType' in kwargs:
            options = ['802.1x', 'Hybrid authentication', 'MAC authentication bypass']
            assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'accessPolicies'],
            'operation': 'updateNetworkSwitchAccessPolicy'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        accessPolicyNumber = urllib.parse.quote(str(accessPolicyNumber), safe='')
        resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

        body_params = ['name', 'radiusServers', 'radius', 'guestPortBouncing', 'radiusTestingEnabled', 'radiusCoaSupportEnabled', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusGroupAttribute', 'hostMode', 'accessPolicyType', 'increaseAccessSpeed', 'guestVlanId', 'dot1x', 'voiceVlanClients', 'urlRedirectWalledGardenEnabled', 'urlRedirectWalledGardenRanges', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str):
        """
        **Delete an access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        """

        metadata = {
            'tags': ['switch', 'configure', 'accessPolicies'],
            'operation': 'deleteNetworkSwitchAccessPolicy'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        accessPolicyNumber = urllib.parse.quote(str(accessPolicyNumber), safe='')
        resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSwitchAlternateManagementInterface(self, networkId: str):
        """
        **Return the switch alternate management interface for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-alternate-management-interface

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'alternateManagementInterface'],
            'operation': 'getNetworkSwitchAlternateManagementInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/alternateManagementInterface'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchAlternateManagementInterface(self, networkId: str, **kwargs):
        """
        **Update the switch alternate management interface for the network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-alternate-management-interface

        - networkId (string): Network ID
        - enabled (boolean): Boolean value to enable or disable AMI configuration. If enabled, VLAN and protocols must be set
        - vlanId (integer): Alternate management VLAN, must be between 1 and 4094
        - protocols (array): Can be one or more of the following values: 'radius', 'snmp' or 'syslog'
        - switches (array): Array of switch serial number and IP assignment. If parameter is present, it cannot have empty body. Note: switches parameter is not applicable for template networks, in other words, do not put 'switches' in the body when updating template networks. Also, an empty 'switches' array will remove all previous assignments
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'alternateManagementInterface'],
            'operation': 'updateNetworkSwitchAlternateManagementInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/alternateManagementInterface'

        body_params = ['enabled', 'vlanId', 'protocols', 'switches', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchDhcpV4ServersSeen(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-v-4-servers-seen

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'dhcp', 'v4', 'servers', 'seen'],
            'operation': 'getNetworkSwitchDhcpV4ServersSeen'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dhcp/v4/servers/seen'

        query_params = ['t0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkSwitchDhcpServerPolicy(self, networkId: str):
        """
        **Return the DHCP server settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy'],
            'operation': 'getNetworkSwitchDhcpServerPolicy'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchDhcpServerPolicy(self, networkId: str, **kwargs):
        """
        **Update the DHCP server settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy

        - networkId (string): Network ID
        - alerts (object): Alert settings for DHCP servers
        - defaultPolicy (string): 'allow' or 'block' new DHCP servers. Default value is 'allow'.
        - allowedServers (array): List the MAC addresses of DHCP servers to permit on the network when defaultPolicy is set to block. An empty array will clear the entries.
        - blockedServers (array): List the MAC addresses of DHCP servers to block on the network when defaultPolicy is set to allow. An empty array will clear the entries.
        - arpInspection (object): Dynamic ARP Inspection settings
        """

        kwargs.update(locals())

        if 'defaultPolicy' in kwargs:
            options = ['allow', 'block']
            assert kwargs['defaultPolicy'] in options, f'''"defaultPolicy" cannot be "{kwargs['defaultPolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy'],
            'operation': 'updateNetworkSwitchDhcpServerPolicy'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy'

        body_params = ['alerts', 'defaultPolicy', 'allowedServers', 'blockedServers', 'arpInspection', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the list of servers trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-trusted-servers

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy', 'arpInspection', 'trustedServers'],
            'operation': 'getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(self, networkId: str, mac: str, vlan: int, ipv4: dict):
        """
        **Add a server to be trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        - networkId (string): Network ID
        - mac (string): The mac address of the trusted server being added
        - vlan (integer): The VLAN of the trusted server being added. It must be between 1 and 4094
        - ipv4 (object): The IPv4 attributes of the trusted server being added
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy', 'arpInspection', 'trustedServers'],
            'operation': 'createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers'

        body_params = ['mac', 'vlan', 'ipv4', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(self, networkId: str, trustedServerId: str, **kwargs):
        """
        **Update a server that is trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        - networkId (string): Network ID
        - trustedServerId (string): Trusted server ID
        - mac (string): The updated mac address of the trusted server
        - vlan (integer): The updated VLAN of the trusted server. It must be between 1 and 4094
        - ipv4 (object): The updated IPv4 attributes of the trusted server
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy', 'arpInspection', 'trustedServers'],
            'operation': 'updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        trustedServerId = urllib.parse.quote(str(trustedServerId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}'

        body_params = ['mac', 'vlan', 'ipv4', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(self, networkId: str, trustedServerId: str):
        """
        **Remove a server from being trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        - networkId (string): Network ID
        - trustedServerId (string): Trusted server ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy', 'arpInspection', 'trustedServers'],
            'operation': 'deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        trustedServerId = urllib.parse.quote(str(trustedServerId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the devices that have a Dynamic ARP Inspection warning and their warnings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy-arp-inspection-warnings-by-device

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy', 'arpInspection', 'warnings', 'byDevice'],
            'operation': 'getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkSwitchDscpToCosMappings(self, networkId: str):
        """
        **Return the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'dscpToCosMappings'],
            'operation': 'getNetworkSwitchDscpToCosMappings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dscpToCosMappings'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchDscpToCosMappings(self, networkId: str, mappings: list):
        """
        **Update the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

        - networkId (string): Network ID
        - mappings (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'dscpToCosMappings'],
            'operation': 'updateNetworkSwitchDscpToCosMappings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/dscpToCosMappings'

        body_params = ['mappings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchLinkAggregations(self, networkId: str):
        """
        **List link aggregation groups**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'getNetworkSwitchLinkAggregations'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/linkAggregations'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchLinkAggregation(self, networkId: str, **kwargs):
        """
        **Create a link aggregation group**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

        - networkId (string): Network ID
        - switchPorts (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'createNetworkSwitchLinkAggregation'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/linkAggregations'

        body_params = ['switchPorts', 'switchProfilePorts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str, **kwargs):
        """
        **Update a link aggregation group**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation

        - networkId (string): Network ID
        - linkAggregationId (string): Link aggregation ID
        - switchPorts (array): Array of switch or stack ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'updateNetworkSwitchLinkAggregation'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        linkAggregationId = urllib.parse.quote(str(linkAggregationId), safe='')
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        body_params = ['switchPorts', 'switchProfilePorts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str):
        """
        **Split a link aggregation group into separate ports**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

        - networkId (string): Network ID
        - linkAggregationId (string): Link aggregation ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'deleteNetworkSwitchLinkAggregation'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        linkAggregationId = urllib.parse.quote(str(linkAggregationId), safe='')
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSwitchMtu(self, networkId: str):
        """
        **Return the MTU configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'mtu'],
            'operation': 'getNetworkSwitchMtu'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/mtu'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchMtu(self, networkId: str, **kwargs):
        """
        **Update the MTU configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu

        - networkId (string): Network ID
        - defaultMtuSize (integer): MTU size for the entire network. Default value is 9578.
        - overrides (array): Override MTU size for individual switches or switch templates. An empty array will clear overrides.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'mtu'],
            'operation': 'updateNetworkSwitchMtu'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/mtu'

        body_params = ['defaultMtuSize', 'overrides', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchPortSchedules(self, networkId: str):
        """
        **List switch port schedules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'getNetworkSwitchPortSchedules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/portSchedules'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchPortSchedule(self, networkId: str, name: str, **kwargs):
        """
        **Add a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-port-schedule

        - networkId (string): Network ID
        - name (string): The name for your port schedule. Required
        - portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
    When it's empty, default schedule with all days of a week are configured.
    Any unspecified day in the schedule is added as a default schedule configuration of the day.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'createNetworkSwitchPortSchedule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/portSchedules'

        body_params = ['name', 'portSchedule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def deleteNetworkSwitchPortSchedule(self, networkId: str, portScheduleId: str):
        """
        **Delete a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule

        - networkId (string): Network ID
        - portScheduleId (string): Port schedule ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'deleteNetworkSwitchPortSchedule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        portScheduleId = urllib.parse.quote(str(portScheduleId), safe='')
        resource = f'/networks/{networkId}/switch/portSchedules/{portScheduleId}'

        return self._session.delete(metadata, resource)
        


    def updateNetworkSwitchPortSchedule(self, networkId: str, portScheduleId: str, **kwargs):
        """
        **Update a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule

        - networkId (string): Network ID
        - portScheduleId (string): Port schedule ID
        - name (string): The name for your port schedule.
        - portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
    When it's empty, default schedule with all days of a week are configured.
    Any unspecified day in the schedule is added as a default schedule configuration of the day.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'updateNetworkSwitchPortSchedule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        portScheduleId = urllib.parse.quote(str(portScheduleId), safe='')
        resource = f'/networks/{networkId}/switch/portSchedules/{portScheduleId}'

        body_params = ['name', 'portSchedule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchQosRules(self, networkId: str):
        """
        **List quality of service rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'getNetworkSwitchQosRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchQosRule(self, networkId: str, vlan: int, **kwargs):
        """
        **Add a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

        - networkId (string): Network ID
        - vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
        - protocol (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY"
        - srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dscp (integer): DSCP tag. Set this to -1 to trust incoming DSCP. Default value is 0
        """

        kwargs.update(locals())

        if 'protocol' in kwargs:
            options = ['ANY', 'TCP', 'UDP']
            assert kwargs['protocol'] in options, f'''"protocol" cannot be "{kwargs['protocol']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'createNetworkSwitchQosRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchQosRulesOrder(self, networkId: str):
        """
        **Return the quality of service rule IDs by order in which they will be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules', 'order'],
            'operation': 'getNetworkSwitchQosRulesOrder'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules/order'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchQosRulesOrder(self, networkId: str, ruleIds: list):
        """
        **Update the order in which the rules should be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

        - networkId (string): Network ID
        - ruleIds (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'qosRules', 'order'],
            'operation': 'updateNetworkSwitchQosRulesOrder'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules/order'

        body_params = ['ruleIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Return a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'getNetworkSwitchQosRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        qosRuleId = urllib.parse.quote(str(qosRuleId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        return self._session.get(metadata, resource)
        


    def deleteNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Delete a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'deleteNetworkSwitchQosRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        qosRuleId = urllib.parse.quote(str(qosRuleId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        return self._session.delete(metadata, resource)
        


    def updateNetworkSwitchQosRule(self, networkId: str, qosRuleId: str, **kwargs):
        """
        **Update a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        - vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
        - protocol (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY".
        - srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dscp (integer): DSCP tag that should be assigned to incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0.
        """

        kwargs.update(locals())

        if 'protocol' in kwargs:
            options = ['ANY', 'TCP', 'UDP']
            assert kwargs['protocol'] in options, f'''"protocol" cannot be "{kwargs['protocol']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'updateNetworkSwitchQosRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        qosRuleId = urllib.parse.quote(str(qosRuleId), safe='')
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchRoutingMulticast(self, networkId: str):
        """
        **Return multicast settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast'],
            'operation': 'getNetworkSwitchRoutingMulticast'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchRoutingMulticast(self, networkId: str, **kwargs):
        """
        **Update multicast settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast

        - networkId (string): Network ID
        - defaultSettings (object): Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
        - overrides (array): Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast'],
            'operation': 'updateNetworkSwitchRoutingMulticast'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast'

        body_params = ['defaultSettings', 'overrides', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchRoutingMulticastRendezvousPoints(self, networkId: str):
        """
        **List multicast rendezvous points**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-points

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
            'operation': 'getNetworkSwitchRoutingMulticastRendezvousPoints'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, interfaceIp: str, multicastGroup: str):
        """
        **Create a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - interfaceIp (string): The IP address of the interface where the RP needs to be created.
        - multicastGroup (string): 'Any', or the IP address of a multicast group
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
            'operation': 'createNetworkSwitchRoutingMulticastRendezvousPoint'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints'

        body_params = ['interfaceIp', 'multicastGroup', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str):
        """
        **Return a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
            'operation': 'getNetworkSwitchRoutingMulticastRendezvousPoint'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rendezvousPointId = urllib.parse.quote(str(rendezvousPointId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}'

        return self._session.get(metadata, resource)
        


    def deleteNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str):
        """
        **Delete a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
            'operation': 'deleteNetworkSwitchRoutingMulticastRendezvousPoint'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rendezvousPointId = urllib.parse.quote(str(rendezvousPointId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}'

        return self._session.delete(metadata, resource)
        


    def updateNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str, interfaceIp: str, multicastGroup: str):
        """
        **Update a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        - interfaceIp (string): The IP address of the interface to use
        - multicastGroup (string): 'Any', or the IP address of a multicast group
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
            'operation': 'updateNetworkSwitchRoutingMulticastRendezvousPoint'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rendezvousPointId = urllib.parse.quote(str(rendezvousPointId), safe='')
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}'

        body_params = ['interfaceIp', 'multicastGroup', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchRoutingOspf(self, networkId: str):
        """
        **Return layer 3 OSPF routing configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-ospf

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'ospf'],
            'operation': 'getNetworkSwitchRoutingOspf'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/routing/ospf'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchRoutingOspf(self, networkId: str, **kwargs):
        """
        **Update layer 3 OSPF routing configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

        - networkId (string): Network ID
        - enabled (boolean): Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default.
        - helloTimerInSeconds (integer): Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds.
        - deadTimerInSeconds (integer): Time interval to determine when the peer will be declared inactive/dead. Value must be between 1 and 65535
        - areas (array): OSPF areas
        - v3 (object): OSPF v3 configuration
        - md5AuthenticationEnabled (boolean): Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default.
        - md5AuthenticationKey (object): MD5 authentication credentials. This param is only relevant if md5AuthenticationEnabled is true
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'ospf'],
            'operation': 'updateNetworkSwitchRoutingOspf'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/routing/ospf'

        body_params = ['enabled', 'helloTimerInSeconds', 'deadTimerInSeconds', 'areas', 'v3', 'md5AuthenticationEnabled', 'md5AuthenticationKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchSettings(self, networkId: str):
        """
        **Returns the switch network settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'settings'],
            'operation': 'getNetworkSwitchSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchSettings(self, networkId: str, **kwargs):
        """
        **Update switch network settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings

        - networkId (string): Network ID
        - vlan (integer): Management VLAN
        - useCombinedPower (boolean): The use Combined Power as the default behavior of secondary power supplies on supported devices.
        - powerExceptions (array): Exceptions on a per switch basis to "useCombinedPower"
        - uplinkClientSampling (object): Uplink client sampling
        - macBlocklist (object): MAC blocklist
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'settings'],
            'operation': 'updateNetworkSwitchSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/settings'

        body_params = ['vlan', 'useCombinedPower', 'powerExceptions', 'uplinkClientSampling', 'macBlocklist', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchStacks(self, networkId: str):
        """
        **List the switch stacks in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stacks

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks'],
            'operation': 'getNetworkSwitchStacks'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/stacks'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchStack(self, networkId: str, name: str, serials: list):
        """
        **Create a stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack

        - networkId (string): Network ID
        - name (string): The name of the new stack
        - serials (array): An array of switch serials to be added into the new stack
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'stacks'],
            'operation': 'createNetworkSwitchStack'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/stacks'

        body_params = ['name', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Show a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks'],
            'operation': 'getNetworkSwitchStack'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}'

        return self._session.get(metadata, resource)
        


    def deleteNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Delete a stack**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks'],
            'operation': 'deleteNetworkSwitchStack'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}'

        return self._session.delete(metadata, resource)
        


    def addNetworkSwitchStack(self, networkId: str, switchStackId: str, serial: str):
        """
        **Add a switch to a stack**
        https://developer.cisco.com/meraki/api-v1/#!add-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - serial (string): The serial of the switch to be added
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'stacks'],
            'operation': 'addNetworkSwitchStack'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/add'

        body_params = ['serial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def removeNetworkSwitchStack(self, networkId: str, switchStackId: str, serial: str):
        """
        **Remove a switch from a stack**
        https://developer.cisco.com/meraki/api-v1/#!remove-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - serial (string): The serial of the switch to be removed
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'stacks'],
            'operation': 'removeNetworkSwitchStack'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/remove'

        body_params = ['serial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchStackRoutingInterfaces(self, networkId: str, switchStackId: str):
        """
        **List layer 3 interfaces for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interfaces

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
            'operation': 'getNetworkSwitchStackRoutingInterfaces'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, name: str, vlanId: int, **kwargs):
        """
        **Create a layer 3 interface for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - name (string): A friendly name or description for the interface or VLAN.
        - vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
        - subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        """

        kwargs.update(locals())

        if 'multicastRouting' in kwargs:
            options = ['IGMP snooping querier', 'disabled', 'enabled']
            assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
            'operation': 'createNetworkSwitchStackRoutingInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, interfaceId: str):
        """
        **Return a layer 3 interface from a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - interfaceId (string): Interface ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
            'operation': 'getNetworkSwitchStackRoutingInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, interfaceId: str, **kwargs):
        """
        **Update a layer 3 interface for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - interfaceId (string): Interface ID
        - name (string): A friendly name or description for the interface or VLAN.
        - subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
        - vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        """

        kwargs.update(locals())

        if 'multicastRouting' in kwargs:
            options = ['IGMP snooping querier', 'disabled', 'enabled']
            assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
            'operation': 'updateNetworkSwitchStackRoutingInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, interfaceId: str):
        """
        **Delete a layer 3 interface from a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - interfaceId (string): Interface ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
            'operation': 'deleteNetworkSwitchStackRoutingInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSwitchStackRoutingInterfaceDhcp(self, networkId: str, switchStackId: str, interfaceId: str):
        """
        **Return a layer 3 interface DHCP configuration for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interface-dhcp

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - interfaceId (string): Interface ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces', 'dhcp'],
            'operation': 'getNetworkSwitchStackRoutingInterfaceDhcp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchStackRoutingInterfaceDhcp(self, networkId: str, switchStackId: str, interfaceId: str, **kwargs):
        """
        **Update a layer 3 interface DHCP configuration for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - interfaceId (string): Interface ID
        - dhcpMode (string): The DHCP mode options for the switch stack interface
        ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
        - dhcpRelayServerIps (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface
        - dhcpLeaseTime (string): The DHCP lease time config for the dhcp server running on switch stack interface
        ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
        - dnsNameserversOption (string): The DHCP name server option for the dhcp server running on the switch stack interface
        ('googlePublicDns', 'openDns' or 'custom')
        - dnsCustomNameservers (array): The DHCP name server IPs when DHCP name server option is '
        custom'
        - bootOptionsEnabled (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch
        stack interface
        - bootNextServer (string): The PXE boot server IP for the DHCP server running on the switch stack interface
        - bootFileName (string): The PXE boot server file name for the DHCP server running on the switch stack interface
        - dhcpOptions (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the
        switch stack interface
        - reservedIpRanges (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface
        - fixedIpAssignments (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface
        """

        kwargs.update(locals())

        if 'dhcpMode' in kwargs:
            options = ['dhcpDisabled', 'dhcpRelay', 'dhcpServer']
            assert kwargs['dhcpMode'] in options, f'''"dhcpMode" cannot be "{kwargs['dhcpMode']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['1 day', '1 hour', '1 week', '12 hours', '30 minutes', '4 hours']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''
        if 'dnsNameserversOption' in kwargs:
            options = ['custom', 'googlePublicDns', 'openDns']
            assert kwargs['dnsNameserversOption'] in options, f'''"dnsNameserversOption" cannot be "{kwargs['dnsNameserversOption']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces', 'dhcp'],
            'operation': 'updateNetworkSwitchStackRoutingInterfaceDhcp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        interfaceId = urllib.parse.quote(str(interfaceId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp'

        body_params = ['dhcpMode', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dnsNameserversOption', 'dnsCustomNameservers', 'bootOptionsEnabled', 'bootNextServer', 'bootFileName', 'dhcpOptions', 'reservedIpRanges', 'fixedIpAssignments', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchStackRoutingStaticRoutes(self, networkId: str, switchStackId: str):
        """
        **List layer 3 static routes for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-routes

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
            'operation': 'getNetworkSwitchStackRoutingStaticRoutes'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes'

        return self._session.get(metadata, resource)
        


    def createNetworkSwitchStackRoutingStaticRoute(self, networkId: str, switchStackId: str, subnet: str, nextHopIp: str, **kwargs):
        """
        **Create a layer 3 static route for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-static-route

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
        - nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
        - name (string): Name or description for layer 3 static route
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
            'operation': 'createNetworkSwitchStackRoutingStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes'

        body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSwitchStackRoutingStaticRoute(self, networkId: str, switchStackId: str, staticRouteId: str):
        """
        **Return a layer 3 static route for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-route

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - staticRouteId (string): Static route ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
            'operation': 'getNetworkSwitchStackRoutingStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchStackRoutingStaticRoute(self, networkId: str, switchStackId: str, staticRouteId: str, **kwargs):
        """
        **Update a layer 3 static route for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-static-route

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - staticRouteId (string): Static route ID
        - name (string): Name or description for layer 3 static route
        - subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
        - nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
            'operation': 'updateNetworkSwitchStackRoutingStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSwitchStackRoutingStaticRoute(self, networkId: str, switchStackId: str, staticRouteId: str):
        """
        **Delete a layer 3 static route for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-static-route

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - staticRouteId (string): Static route ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
            'operation': 'deleteNetworkSwitchStackRoutingStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        switchStackId = urllib.parse.quote(str(switchStackId), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSwitchStormControl(self, networkId: str):
        """
        **Return the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stormControl'],
            'operation': 'getNetworkSwitchStormControl'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/stormControl'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchStormControl(self, networkId: str, **kwargs):
        """
        **Update the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

        - networkId (string): Network ID
        - broadcastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
        - multicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
        - unknownUnicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stormControl'],
            'operation': 'updateNetworkSwitchStormControl'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/stormControl'

        body_params = ['broadcastThreshold', 'multicastThreshold', 'unknownUnicastThreshold', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSwitchStp(self, networkId: str):
        """
        **Returns STP settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'stp'],
            'operation': 'getNetworkSwitchStp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/stp'

        return self._session.get(metadata, resource)
        


    def updateNetworkSwitchStp(self, networkId: str, **kwargs):
        """
        **Updates STP settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp

        - networkId (string): Network ID
        - rstpEnabled (boolean): The spanning tree protocol status in network
        - stpBridgePriority (array): STP bridge priority for switches/stacks or switch templates. An empty array will clear the STP bridge priority settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stp'],
            'operation': 'updateNetworkSwitchStp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/switch/stp'

        body_params = ['rstpEnabled', 'stpBridgePriority', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationConfigTemplateSwitchProfiles(self, organizationId: str, configTemplateId: str):
        """
        **List the switch templates for your switch template configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles'],
            'operation': 'getOrganizationConfigTemplateSwitchProfiles'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles'

        return self._session.get(metadata, resource)
        


    def getOrganizationConfigTemplateSwitchProfilePorts(self, organizationId: str, configTemplateId: str, profileId: str):
        """
        **Return all the ports of a switch template**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-ports

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - profileId (string): Profile ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
            'operation': 'getOrganizationConfigTemplateSwitchProfilePorts'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        profileId = urllib.parse.quote(str(profileId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports'

        return self._session.get(metadata, resource)
        


    def getOrganizationConfigTemplateSwitchProfilePort(self, organizationId: str, configTemplateId: str, profileId: str, portId: str):
        """
        **Return a switch template port**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - profileId (string): Profile ID
        - portId (string): Port ID
        """

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
            'operation': 'getOrganizationConfigTemplateSwitchProfilePort'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        profileId = urllib.parse.quote(str(profileId), safe='')
        portId = urllib.parse.quote(str(portId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}'

        return self._session.get(metadata, resource)
        


    def updateOrganizationConfigTemplateSwitchProfilePort(self, organizationId: str, configTemplateId: str, profileId: str, portId: str, **kwargs):
        """
        **Update a switch template port**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - profileId (string): Profile ID
        - portId (string): Port ID
        - name (string): The name of the switch template port.
        - tags (array): The list of tags of the switch template port.
        - enabled (boolean): The status of the switch template port.
        - poeEnabled (boolean): The PoE status of the switch template port.
        - type (string): The type of the switch template port ('trunk' or 'access').
        - vlan (integer): The VLAN of the switch template port. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch template port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch template port. Only applicable to trunk ports.
        - isolationEnabled (boolean): The isolation status of the switch template port.
        - rstpEnabled (boolean): The rapid spanning tree protocol status.
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
        - linkNegotiation (string): The link speed for the switch template port.
        - portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
        - udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
        - accessPolicyType (string): The type of the access policy of the switch template port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'.
        - accessPolicyNumber (integer): The number of a custom access policy to configure on the switch template port. Only applicable when 'accessPolicyType' is 'Custom access policy'.
        - macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'.
        - stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stormControlEnabled (boolean): The storm control status of the switch template port.
        - flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
        - daiTrusted (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
        - profile (object): Profile attributes
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['access', 'trunk']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''
        if 'stpGuard' in kwargs:
            options = ['bpdu guard', 'disabled', 'loop guard', 'root guard']
            assert kwargs['stpGuard'] in options, f'''"stpGuard" cannot be "{kwargs['stpGuard']}", & must be set to one of: {options}'''
        if 'udld' in kwargs:
            options = ['Alert only', 'Enforce']
            assert kwargs['udld'] in options, f'''"udld" cannot be "{kwargs['udld']}", & must be set to one of: {options}'''
        if 'accessPolicyType' in kwargs:
            options = ['Custom access policy', 'MAC allow list', 'Open', 'Sticky MAC allow list']
            assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
            'operation': 'updateOrganizationConfigTemplateSwitchProfilePort'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        profileId = urllib.parse.quote(str(profileId), safe='')
        portId = urllib.parse.quote(str(portId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}'

        body_params = ['name', 'tags', 'enabled', 'poeEnabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macAllowList', 'stickyMacAllowList', 'stickyMacAllowListLimit', 'stormControlEnabled', 'flexibleStackingEnabled', 'daiTrusted', 'profile', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationSummarySwitchPowerHistory(self, organizationId: str, **kwargs):
        """
        **Returns the total PoE power draw for all switch ports in the organization over the requested timespan (by default the last 24 hours)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-switch-power-history

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'monitor', 'summary', 'power', 'history'],
            'operation': 'getOrganizationSummarySwitchPowerHistory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/switch/power/history'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def cloneOrganizationSwitchDevices(self, organizationId: str, sourceSerial: str, targetSerials: list):
        """
        **Clone port-level and some switch-level configuration settings from a source switch to one or more target switches**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

        - organizationId (string): Organization ID
        - sourceSerial (string): Serial number of the source switch (must be on a network not bound to a template)
        - targetSerials (array): Array of serial numbers of one or more target switches (must be on a network not bound to a template)
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'devices'],
            'operation': 'cloneOrganizationSwitchDevices'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/switch/devices/clone'

        body_params = ['sourceSerial', 'targetSerials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationSwitchPortsBySwitch(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the switchports in an organization by switch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter switchports by network.
        - portProfileIds (array): Optional parameter to filter switchports belonging to the specified port profiles.
        - name (string): Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
        - mac (string): Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
        - macs (array): Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
        - serial (string): Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
        - serials (array): Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
        - configurationUpdatedAfter (string): Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'ports', 'bySwitch'],
            'operation': 'getOrganizationSwitchPortsBySwitch'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/switch/ports/bySwitch'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'portProfileIds', 'name', 'mac', 'macs', 'serial', 'serials', 'configurationUpdatedAfter', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'portProfileIds', 'macs', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
