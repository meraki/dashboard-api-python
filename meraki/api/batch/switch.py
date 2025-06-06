import urllib


class ActionBatchSwitch(object):
    def __init__(self):
        super(ActionBatchSwitch, self).__init__()
        


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
        resource = f'/devices/{serial}/switch/ports/cycle'

        body_params = ['ports', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "cycle",
            "body": payload
        }
        return action
        





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
        - type (string): The type of the switch port ('trunk', 'access', 'stack' or 'routed').
        - vlan (integer): The VLAN of the switch port. For a trunk port, this is the native VLAN. A null value will clear the value set for trunk ports.
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
        - macWhitelistLimit (integer): The maximum number of MAC addresses for regular MAC allow list. Only applicable when 'accessPolicyType' is 'MAC allow list'.
          Note: Config only supported on verions greater than ms18 only for classic switches.
        - stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stormControlEnabled (boolean): The storm control status of the switch port.
        - adaptivePolicyGroupId (string): The adaptive policy group ID that will be used to tag traffic through this switch port. This ID must pre-exist during the configuration, else needs to be created using adaptivePolicy/groups API. Cannot be applied to a port on a switch bound to profile.
        - peerSgtCapable (boolean): If true, Peer SGT is enabled for traffic through this switch port. Applicable to trunk port only, not access port. Cannot be applied to a port on a switch bound to profile.
        - flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
        - daiTrusted (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
        - profile (object): Profile attributes
        - dot3az (object): dot3az settings for the port
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['access', 'routed', 'stack', 'trunk']
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
        resource = f'/devices/{serial}/switch/ports/{portId}'

        body_params = ['name', 'tags', 'enabled', 'poeEnabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macAllowList', 'macWhitelistLimit', 'stickyMacAllowList', 'stickyMacAllowListLimit', 'stormControlEnabled', 'adaptivePolicyGroupId', 'peerSgtCapable', 'flexibleStackingEnabled', 'daiTrusted', 'profile', 'dot3az', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createDeviceSwitchRoutingInterface(self, serial: str, name: str, **kwargs):
        """
        **Create a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

        - serial (string): Serial
        - name (string): A friendly name or description for the interface or VLAN (max length 128 characters).
        - subnet (string): The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
        - ospfSettings (object): The OSPF routing settings of the interface.
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
        resource = f'/devices/{serial}/switch/routing/interfaces'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str, **kwargs):
        """
        **Update a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        - name (string): A friendly name or description for the interface or VLAN (max length 128 characters).
        - subnet (string): The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
        - ospfSettings (object): The OSPF routing settings of the interface.
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
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





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
        resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp'

        body_params = ['dhcpMode', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dnsNameserversOption', 'dnsCustomNameservers', 'bootOptionsEnabled', 'bootNextServer', 'bootFileName', 'dhcpOptions', 'reservedIpRanges', 'fixedIpAssignments', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/devices/{serial}/switch/routing/staticRoutes'

        body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str, **kwargs):
        """
        **Update a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        - name (string): Name or description for layer 3 static route
        - subnet (string): The subnet which is routed via this static route and should be specified in CIDR notation (ex. 1.2.3.0/24)
        - nextHopIp (string): IP address of the next hop device to which the device sends its traffic for the subnet
        - managementNextHop (string): Optional fallback IP address for management traffic
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
            'operation': 'updateDeviceSwitchRoutingStaticRoute'
        }
        resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'nextHopIp', 'managementNextHop', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateDeviceSwitchWarmSpare(self, serial: str, enabled: bool, **kwargs):
        """
        **Update warm spare configuration for a switch. The spare will use the same L3 configuration as the primary. Note that this will irreversibly destroy any existing L3 configuration on the spare.**
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
        resource = f'/devices/{serial}/switch/warmSpare'

        body_params = ['enabled', 'spareSerial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkSwitchAccessPolicy(self, networkId: str, name: str, radiusServers: list, radiusTestingEnabled: bool, radiusCoaSupportEnabled: bool, radiusAccountingEnabled: bool, hostMode: str, urlRedirectWalledGardenEnabled: bool, **kwargs):
        """
        **Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

        - networkId (string): Network ID
        - name (string): Name of the access policy(max length 255)
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
        resource = f'/networks/{networkId}/switch/accessPolicies'

        body_params = ['name', 'radiusServers', 'radius', 'guestPortBouncing', 'radiusTestingEnabled', 'radiusCoaSupportEnabled', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusGroupAttribute', 'hostMode', 'accessPolicyType', 'increaseAccessSpeed', 'guestVlanId', 'dot1x', 'voiceVlanClients', 'urlRedirectWalledGardenEnabled', 'urlRedirectWalledGardenRanges', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str, **kwargs):
        """
        **Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        - name (string): Name of the access policy(max length 255)
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
        resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

        body_params = ['name', 'radiusServers', 'radius', 'guestPortBouncing', 'radiusTestingEnabled', 'radiusCoaSupportEnabled', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusGroupAttribute', 'hostMode', 'accessPolicyType', 'increaseAccessSpeed', 'guestVlanId', 'dot1x', 'voiceVlanClients', 'urlRedirectWalledGardenEnabled', 'urlRedirectWalledGardenRanges', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/alternateManagementInterface'

        body_params = ['enabled', 'vlanId', 'protocols', 'switches', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkSwitchDhcpServerPolicy(self, networkId: str, **kwargs):
        """
        **Update the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively**
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
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy'

        body_params = ['alerts', 'defaultPolicy', 'allowedServers', 'blockedServers', 'arpInspection', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers'

        body_params = ['mac', 'vlan', 'ipv4', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}'

        body_params = ['mac', 'vlan', 'ipv4', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/dscpToCosMappings'

        body_params = ['mappings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/linkAggregations'

        body_params = ['switchPorts', 'switchProfilePorts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        body_params = ['switchPorts', 'switchProfilePorts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/mtu'

        body_params = ['defaultMtuSize', 'overrides', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/portSchedules/{portScheduleId}'

        body_params = ['name', 'portSchedule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkSwitchQosRule(self, networkId: str, vlan: int, **kwargs):
        """
        **Add a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule

        - networkId (string): Network ID
        - vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
        - protocol (string): The protocol of the incoming packet. Default value is "ANY"
        - srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP.
        - dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP.
        - dscp (integer): DSCP tag for the incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0
        """

        kwargs.update(locals())

        if 'protocol' in kwargs:
            options = ['ANY', 'TCP', 'UDP']
            assert kwargs['protocol'] in options, f'''"protocol" cannot be "{kwargs['protocol']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'createNetworkSwitchQosRule'
        }
        resource = f'/networks/{networkId}/switch/qosRules'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/qosRules/order'

        body_params = ['ruleIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update_order",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkSwitchQosRule(self, networkId: str, qosRuleId: str, **kwargs):
        """
        **Update a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        - vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
        - protocol (string): The protocol of the incoming packet. Default value is "ANY"
        - srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP.
        - dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP.
        - dscp (integer): DSCP tag that should be assigned to incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0
        """

        kwargs.update(locals())

        if 'protocol' in kwargs:
            options = ['ANY', 'TCP', 'UDP']
            assert kwargs['protocol'] in options, f'''"protocol" cannot be "{kwargs['protocol']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'updateNetworkSwitchQosRule'
        }
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/routing/multicast'

        body_params = ['defaultSettings', 'overrides', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints'

        body_params = ['interfaceIp', 'multicastGroup', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str, interfaceIp: str, multicastGroup: str):
        """
        **Update a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        - interfaceIp (string): The IP address of the interface where the RP needs to be created.
        - multicastGroup (string): 'Any', or the IP address of a multicast group
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
            'operation': 'updateNetworkSwitchRoutingMulticastRendezvousPoint'
        }
        resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}'

        body_params = ['interfaceIp', 'multicastGroup', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/routing/ospf'

        body_params = ['enabled', 'helloTimerInSeconds', 'deadTimerInSeconds', 'areas', 'v3', 'md5AuthenticationEnabled', 'md5AuthenticationKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/settings'

        body_params = ['vlan', 'useCombinedPower', 'powerExceptions', 'uplinkClientSampling', 'macBlocklist', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "settings/actions/update",
            "body": payload
        }
        return action
        





    def createNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, name: str, **kwargs):
        """
        **Create a layer 3 interface for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - name (string): A friendly name or description for the interface or VLAN (max length 128 characters).
        - subnet (string): The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
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
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, interfaceId: str, **kwargs):
        """
        **Update a layer 3 interface for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - interfaceId (string): Interface ID
        - name (string): A friendly name or description for the interface or VLAN (max length 128 characters).
        - subnet (string): The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
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
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

        body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', 'ipv6', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp'

        body_params = ['dhcpMode', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dnsNameserversOption', 'dnsCustomNameservers', 'bootOptionsEnabled', 'bootNextServer', 'bootFileName', 'dhcpOptions', 'reservedIpRanges', 'fixedIpAssignments', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes'

        body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





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
        - managementNextHop (string): Optional fallback IP address for management traffic
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
            'operation': 'updateNetworkSwitchStackRoutingStaticRoute'
        }
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'nextHopIp', 'managementNextHop', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkSwitchStormControl(self, networkId: str, **kwargs):
        """
        **Update the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control

        - networkId (string): Network ID
        - broadcastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
        - multicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
        - unknownUnicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.
        - treatTheseTrafficTypesAsOneThreshold (array): Grouped traffic types
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stormControl'],
            'operation': 'updateNetworkSwitchStormControl'
        }
        resource = f'/networks/{networkId}/switch/stormControl'

        body_params = ['broadcastThreshold', 'multicastThreshold', 'unknownUnicastThreshold', 'treatTheseTrafficTypesAsOneThreshold', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/switch/stp'

        body_params = ['rstpEnabled', 'stpBridgePriority', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        - type (string): The type of the switch template port ('trunk', 'access', 'stack' or 'routed').
        - vlan (integer): The VLAN of the switch template port. For a trunk port, this is the native VLAN. A null value will clear the value set for trunk ports.
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
        - macWhitelistLimit (integer): The maximum number of MAC addresses for regular MAC allow list. Only applicable when 'accessPolicyType' is 'MAC allow list'.
          Note: Config only supported on verions greater than ms18 only for classic switches.
        - stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'.
        - stormControlEnabled (boolean): The storm control status of the switch template port.
        - flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
        - daiTrusted (boolean): If true, ARP packets for this port will be considered trusted, and Dynamic ARP Inspection will allow the traffic.
        - profile (object): Profile attributes
        - dot3az (object): dot3az settings for the port
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['access', 'routed', 'stack', 'trunk']
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
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}'

        body_params = ['name', 'tags', 'enabled', 'poeEnabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macAllowList', 'macWhitelistLimit', 'stickyMacAllowList', 'stickyMacAllowListLimit', 'stormControlEnabled', 'flexibleStackingEnabled', 'daiTrusted', 'profile', 'dot3az', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def cloneOrganizationSwitchDevices(self, organizationId: str, sourceSerial: str, targetSerials: list):
        """
        **Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring**
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
        resource = f'/organizations/{organizationId}/switch/devices/clone'

        body_params = ['sourceSerial', 'targetSerials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "clone",
            "body": payload
        }
        return action
        



