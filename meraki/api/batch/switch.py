import urllib


class ActionBatchSwitch(object):
    def __init__(self):
        super(ActionBatchSwitch, self).__init__()

    def cycleDeviceSwitchPorts(self, serial: str, ports: list, **kwargs):
        """
        **Cycle a set of switch ports on non-Catalyst MS devices. For Catalyst support, use /devices/{serial}/liveTools/ports/cycle, which supports all switch product families.**
        https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

        - serial (string): Serial
        - ports (array): List of switch ports
        """

        kwargs = locals()

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/ports/cycle"

        body_params = [
            "ports",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "cycle",
            "body": payload,
        }
        return action

    def updateDeviceSwitchPortsMirror(self, serial: str, source: dict, destination: dict, **kwargs):
        """
        **Update a port mirror**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-ports-mirror

        - serial (string): The switch identifier
        - source (object): Source ports mirror configuration
        - destination (object): Destination port mirror configuration
        - tags (array): Port mirror tags
        - role (string): Switch role can be source or destination
        - comment (string): My pretty comment
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/ports/mirror"

        body_params = [
            "serial",
            "source",
            "destination",
            "tags",
            "role",
            "comment",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "mirrors/update",
            "body": payload,
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
        - type (string): The type of the switch port ('access', 'trunk', 'stack', 'routed', 'svl' or 'dad').
        - vlan (integer): The VLAN of the switch port. For a trunk port, this is the native VLAN. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
        - activeVlans (string): The VLANs that are active on the switch port. Only applicable to trunk ports.
        - isolationEnabled (boolean): The isolation status of the switch port.
        - rstpEnabled (boolean): The rapid spanning tree protocol status.
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
        - stpPortFastTrunk (boolean): The state of STP PortFast Trunk on the switch port.
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
        - highSpeed (object): High speed port enablement settings for C9500-32QC
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["access", "dad", "routed", "stack", "svl", "trunk"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
        if "stpGuard" in kwargs:
            options = ["bpdu guard", "disabled", "loop guard", "root guard"]
            assert kwargs["stpGuard"] in options, (
                f'''"stpGuard" cannot be "{kwargs["stpGuard"]}", & must be set to one of: {options}'''
            )
        if "udld" in kwargs:
            options = ["Alert only", "Enforce"]
            assert kwargs["udld"] in options, f'''"udld" cannot be "{kwargs["udld"]}", & must be set to one of: {options}'''
        if "accessPolicyType" in kwargs:
            options = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        serial = urllib.parse.quote(serial, safe="")
        portId = urllib.parse.quote(portId, safe="")
        resource = f"/devices/{serial}/switch/ports/{portId}"

        body_params = [
            "name",
            "tags",
            "enabled",
            "poeEnabled",
            "type",
            "vlan",
            "voiceVlan",
            "allowedVlans",
            "activeVlans",
            "isolationEnabled",
            "rstpEnabled",
            "stpGuard",
            "stpPortFastTrunk",
            "linkNegotiation",
            "portScheduleId",
            "udld",
            "accessPolicyType",
            "accessPolicyNumber",
            "macAllowList",
            "macWhitelistLimit",
            "stickyMacAllowList",
            "stickyMacAllowListLimit",
            "stormControlEnabled",
            "adaptivePolicyGroupId",
            "peerSgtCapable",
            "flexibleStackingEnabled",
            "daiTrusted",
            "profile",
            "dot3az",
            "highSpeed",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createDeviceSwitchRoutingInterface(self, serial: str, name: str, **kwargs):
        """
        **Create a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface

        - serial (string): Serial
        - name (string): A friendly name or description for the interface or VLAN (max length 128 characters).
        - mode (string): L3 Interface mode, can be one of 'vlan', 'routed', 'loopback'. Default is 'vlan'. CS 17.18 or higher is required for 'routed' mode.
        - subnet (string): The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - switchPortId (string): Switch Port ID when in Routed mode (CS 17.18 or higher required)
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - mtu (integer): The interface MTU. Applies to native switch layer 3 interfaces, including VLAN and routed modes.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
        - isSwitchDefaultGateway (boolean): When true, the switch uses the IPv4 uplink gateway as its IPv4 default gateway. This can only be set if the interface is designated as the IPv4 uplink and the switch is running IOS XE version >= 17.18.3.
        - uplinkV4 (boolean): When true, this interface is used as static IPv4 uplink.
        - candidateUplinkV4 (boolean): When true, this interface is a UAC candidate for IPv4 Uplink.
        - uplinkV6 (boolean): When true, this interface is used as static IPv6 uplink.
        - staticV4Dns1 (string): Primary IPv4 DNS server address
        - staticV4Dns2 (string): Secondary IPv4 DNS server address
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        - loopback (object): The loopback settings of the interface.
        """

        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert kwargs["mode"] in options, f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces"

        body_params = [
            "name",
            "mode",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "mtu",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "isSwitchDefaultGateway",
            "uplinkV4",
            "candidateUplinkV4",
            "uplinkV6",
            "staticV4Dns1",
            "staticV4Dns2",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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
        - switchPortId (string): Switch Port ID when in Routed mode (CS 17.18 or higher required)
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - mtu (integer): The interface MTU. Applies to native switch layer 3 interfaces, including VLAN and routed modes.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
        - isSwitchDefaultGateway (boolean): When true, the switch uses the IPv4 uplink gateway as its IPv4 default gateway. This can only be set if the interface is designated as the IPv4 uplink and the switch is running IOS XE version >= 17.18.3.
        - uplinkV4 (boolean): When true, this interface is used as static IPv4 uplink.
        - candidateUplinkV4 (boolean): When true, this interface is a UAC candidate for IPv4 Uplink.
        - uplinkV6 (boolean): When true, this interface is used as static IPv6 uplink.
        - staticV4Dns1 (string): Primary IPv4 DNS server address
        - staticV4Dns2 (string): Secondary IPv4 DNS server address
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        - loopback (object): The loopback settings of the interface.
        """

        kwargs.update(locals())

        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        serial = urllib.parse.quote(serial, safe="")
        interfaceId = urllib.parse.quote(interfaceId, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interfaceId}"

        body_params = [
            "name",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "mtu",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "isSwitchDefaultGateway",
            "uplinkV4",
            "candidateUplinkV4",
            "uplinkV6",
            "staticV4Dns1",
            "staticV4Dns2",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str):
        """
        **Delete a layer 3 interface from the switch**
        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        serial = urllib.parse.quote(serial, safe="")
        interfaceId = urllib.parse.quote(interfaceId, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interfaceId}"

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

        if "dhcpMode" in kwargs:
            options = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]
            assert kwargs["dhcpMode"] in options, (
                f'''"dhcpMode" cannot be "{kwargs["dhcpMode"]}", & must be set to one of: {options}'''
            )
        if "dhcpLeaseTime" in kwargs:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert kwargs["dhcpLeaseTime"] in options, (
                f'''"dhcpLeaseTime" cannot be "{kwargs["dhcpLeaseTime"]}", & must be set to one of: {options}'''
            )
        if "dnsNameserversOption" in kwargs:
            options = ["custom", "googlePublicDns", "openDns"]
            assert kwargs["dnsNameserversOption"] in options, (
                f'''"dnsNameserversOption" cannot be "{kwargs["dnsNameserversOption"]}", & must be set to one of: {options}'''
            )

        serial = urllib.parse.quote(serial, safe="")
        interfaceId = urllib.parse.quote(interfaceId, safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp"

        body_params = [
            "dhcpMode",
            "dhcpRelayServerIps",
            "dhcpLeaseTime",
            "dnsNameserversOption",
            "dnsCustomNameservers",
            "bootOptionsEnabled",
            "bootNextServer",
            "bootFileName",
            "dhcpOptions",
            "reservedIpRanges",
            "fixedIpAssignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        staticRouteId = urllib.parse.quote(staticRouteId, safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "managementNextHop",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str):
        """
        **Delete a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        """

        serial = urllib.parse.quote(serial, safe="")
        staticRouteId = urllib.parse.quote(staticRouteId, safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}"

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

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/switch/warmSpare"

        body_params = [
            "enabled",
            "spareSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createNetworkSwitchAccessPolicy(
        self, networkId: str, name: str, radiusServers: list, radiusAccountingEnabled: bool, **kwargs
    ):
        """
        **Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy

        - networkId (string): Network ID
        - name (string): Name of the access policy(max length 255)
        - radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
        - radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
        - radius (object): Object for RADIUS Settings
        - guestPortBouncing (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
        - radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
        - radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
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
        - guestGroupPolicyId (string): Group policy Number for guest group policy
        - guestSgtId (integer): Security Group Tag ID for guest group policy
        """

        kwargs.update(locals())

        if "hostMode" in kwargs:
            options = ["Multi-Auth", "Multi-Domain", "Multi-Host", "Single-Host"]
            assert kwargs["hostMode"] in options, (
                f'''"hostMode" cannot be "{kwargs["hostMode"]}", & must be set to one of: {options}'''
            )
        if "accessPolicyType" in kwargs:
            options = ["802.1x", "Hybrid authentication", "MAC authentication bypass"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/accessPolicies"

        body_params = [
            "name",
            "radiusServers",
            "radius",
            "guestPortBouncing",
            "radiusTestingEnabled",
            "radiusCoaSupportEnabled",
            "radiusAccountingEnabled",
            "radiusAccountingServers",
            "radiusGroupAttribute",
            "hostMode",
            "accessPolicyType",
            "increaseAccessSpeed",
            "guestVlanId",
            "dot1x",
            "voiceVlanClients",
            "urlRedirectWalledGardenEnabled",
            "urlRedirectWalledGardenRanges",
            "guestGroupPolicyId",
            "guestSgtId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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
        - guestGroupPolicyId (string): Group policy Number for guest group policy
        - guestSgtId (integer): Security Group Tag ID for guest group policy
        """

        kwargs.update(locals())

        if "hostMode" in kwargs:
            options = ["Multi-Auth", "Multi-Domain", "Multi-Host", "Single-Host"]
            assert kwargs["hostMode"] in options, (
                f'''"hostMode" cannot be "{kwargs["hostMode"]}", & must be set to one of: {options}'''
            )
        if "accessPolicyType" in kwargs:
            options = ["802.1x", "Hybrid authentication", "MAC authentication bypass"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        accessPolicyNumber = urllib.parse.quote(accessPolicyNumber, safe="")
        resource = f"/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}"

        body_params = [
            "name",
            "radiusServers",
            "radius",
            "guestPortBouncing",
            "radiusTestingEnabled",
            "radiusCoaSupportEnabled",
            "radiusAccountingEnabled",
            "radiusAccountingServers",
            "radiusGroupAttribute",
            "hostMode",
            "accessPolicyType",
            "increaseAccessSpeed",
            "guestVlanId",
            "dot1x",
            "voiceVlanClients",
            "urlRedirectWalledGardenEnabled",
            "urlRedirectWalledGardenRanges",
            "guestGroupPolicyId",
            "guestSgtId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str):
        """
        **Delete an access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        """

        networkId = urllib.parse.quote(networkId, safe="")
        accessPolicyNumber = urllib.parse.quote(accessPolicyNumber, safe="")
        resource = f"/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}"

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

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/alternateManagementInterface"

        body_params = [
            "enabled",
            "vlanId",
            "protocols",
            "switches",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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

        if "defaultPolicy" in kwargs:
            options = ["allow", "block"]
            assert kwargs["defaultPolicy"] in options, (
                f'''"defaultPolicy" cannot be "{kwargs["defaultPolicy"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy"

        body_params = [
            "alerts",
            "defaultPolicy",
            "allowedServers",
            "blockedServers",
            "arpInspection",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(
        self, networkId: str, mac: str, vlan: int, ipv4: dict, **kwargs
    ):
        """
        **Add a server to be trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        - networkId (string): Network ID
        - mac (string): The mac address of the trusted server being added
        - vlan (integer): The VLAN of the trusted server being added. It must be between 1 and 4094
        - ipv4 (object): The IPv4 attributes of the trusted server being added
        """

        kwargs = locals()

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers"

        body_params = [
            "mac",
            "vlan",
            "ipv4",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        trustedServerId = urllib.parse.quote(trustedServerId, safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}"

        body_params = [
            "mac",
            "vlan",
            "ipv4",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(self, networkId: str, trustedServerId: str):
        """
        **Remove a server from being trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        - networkId (string): Network ID
        - trustedServerId (string): Trusted server ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        trustedServerId = urllib.parse.quote(trustedServerId, safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateNetworkSwitchDscpToCosMappings(self, networkId: str, mappings: list, **kwargs):
        """
        **Update the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

        - networkId (string): Network ID
        - mappings (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.
        """

        kwargs = locals()

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/dscpToCosMappings"

        body_params = [
            "mappings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createNetworkSwitchLinkAggregation(self, networkId: str, **kwargs):
        """
        **Create a link aggregation group**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation

        - networkId (string): Network ID
        - switchPorts (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - esiMhPairId (string): ESI-MH pair ID. Required when creating a downstream aggregation across ESI-MH pair member switches.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations"

        body_params = [
            "switchPorts",
            "switchProfilePorts",
            "esiMhPairId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        linkAggregationId = urllib.parse.quote(linkAggregationId, safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations/{linkAggregationId}"

        body_params = [
            "switchPorts",
            "switchProfilePorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str):
        """
        **Split a link aggregation group into separate ports**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

        - networkId (string): Network ID
        - linkAggregationId (string): Link aggregation ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        linkAggregationId = urllib.parse.quote(linkAggregationId, safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations/{linkAggregationId}"

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

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/mtu"

        body_params = [
            "defaultMtuSize",
            "overrides",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        portScheduleId = urllib.parse.quote(portScheduleId, safe="")
        resource = f"/networks/{networkId}/switch/portSchedules/{portScheduleId}"

        body_params = [
            "name",
            "portSchedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createNetworkSwitchPortsProfile(self, networkId: str, **kwargs):
        """
        **Create a port profile in a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-ports-profile

        - networkId (string): Network ID
        - name (string): The name of the profile.
        - description (string): Text describing the profile.
        - tags (array): Space-seperated list of tags
        - defaultRadiusProfileName (string): When present, the default RADIUS attribute value for RADIUS-based port profile application
        - authentication (object): Authentication settings for RADIUS-based port profile application.
        - port (object): Configuration settings for port profile
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/ports/profiles"

        body_params = [
            "name",
            "description",
            "tags",
            "defaultRadiusProfileName",
            "authentication",
            "port",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "profiles/create",
            "body": payload,
        }
        return action

    def updateNetworkSwitchPortsProfile(self, networkId: str, id: str, **kwargs):
        """
        **Update a port profile in a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-ports-profile

        - networkId (string): Network ID
        - id (string): ID
        - name (string): The name of the profile.
        - description (string): Text describing the profile.
        - tags (array): Space-seperated list of tags
        - defaultRadiusProfileName (string): When present, the default RADIUS attribute value for RADIUS-based port profile application
        - authentication (object): Authentication settings for RADIUS-based port profile application.
        - port (object): Configuration settings for port profile
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/networks/{networkId}/switch/ports/profiles/{id}"

        body_params = [
            "name",
            "description",
            "tags",
            "defaultRadiusProfileName",
            "authentication",
            "port",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "profiles/update",
            "body": payload,
        }
        return action

    def deleteNetworkSwitchPortsProfile(self, networkId: str, id: str):
        """
        **Delete a port profile from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-ports-profile

        - networkId (string): Network ID
        - id (string): ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/networks/{networkId}/switch/ports/profiles/{id}"

        action = {
            "resource": resource,
            "operation": "profiles/destroy",
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

        if "protocol" in kwargs:
            options = ["ANY", "TCP", "UDP"]
            assert kwargs["protocol"] in options, (
                f'''"protocol" cannot be "{kwargs["protocol"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/qosRules"

        body_params = [
            "vlan",
            "protocol",
            "srcPort",
            "srcPortRange",
            "dstPort",
            "dstPortRange",
            "dscp",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateNetworkSwitchQosRulesOrder(self, networkId: str, ruleIds: list, **kwargs):
        """
        **Update the order in which the rules should be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

        - networkId (string): Network ID
        - ruleIds (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.
        """

        kwargs = locals()

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/qosRules/order"

        body_params = [
            "ruleIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update_order",
            "body": payload,
        }
        return action

    def deleteNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Delete a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        qosRuleId = urllib.parse.quote(qosRuleId, safe="")
        resource = f"/networks/{networkId}/switch/qosRules/{qosRuleId}"

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

        if "protocol" in kwargs:
            options = ["ANY", "TCP", "UDP"]
            assert kwargs["protocol"] in options, (
                f'''"protocol" cannot be "{kwargs["protocol"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        qosRuleId = urllib.parse.quote(qosRuleId, safe="")
        resource = f"/networks/{networkId}/switch/qosRules/{qosRuleId}"

        body_params = [
            "vlan",
            "protocol",
            "srcPort",
            "srcPortRange",
            "dstPort",
            "dstPortRange",
            "dscp",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast"

        body_params = [
            "defaultSettings",
            "overrides",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "ms/multicast/actions/update",
            "body": payload,
        }
        return action

    def createNetworkSwitchRoutingMulticastRendezvousPoint(
        self, networkId: str, interfaceIp: str, multicastGroup: str, **kwargs
    ):
        """
        **Create a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - interfaceIp (string): The IP address of the interface where the RP needs to be created.
        - multicastGroup (string): 'Any', or the IP address of a multicast group
        - vrf (object): The VRF with PIM enabled L3 interface
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints"

        body_params = [
            "interfaceIp",
            "multicastGroup",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def deleteNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str):
        """
        **Delete a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        """

        networkId = urllib.parse.quote(networkId, safe="")
        rendezvousPointId = urllib.parse.quote(rendezvousPointId, safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateNetworkSwitchRoutingMulticastRendezvousPoint(
        self, networkId: str, rendezvousPointId: str, interfaceIp: str, multicastGroup: str, **kwargs
    ):
        """
        **Update a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        - interfaceIp (string): The IP address of the interface where the RP needs to be created.
        - multicastGroup (string): 'Any', or the IP address of a multicast group
        - vrf (object): The VRF with PIM enabled L3 interface
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        rendezvousPointId = urllib.parse.quote(rendezvousPointId, safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}"

        body_params = [
            "interfaceIp",
            "multicastGroup",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateNetworkSwitchRoutingOspf(self, networkId: str, **kwargs):
        """
        **Update layer 3 OSPF routing configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-ospf

        - networkId (string): Network ID
        - vrf (string): The VRF to return the OSPF routing configuration for. When not provided, the default VRF is used. Requires IOS XE 17.18 or higher
        - enabled (boolean): Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default.
        - helloTimerInSeconds (integer): Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds.
        - deadTimerInSeconds (integer): Time interval to determine when the peer will be declared inactive/dead. Value must be between 1 and 65535
        - areas (array): OSPF areas
        - v3 (object): OSPF v3 configuration
        - md5AuthenticationEnabled (boolean): Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default.
        - md5AuthenticationKey (object): MD5 authentication credentials. This param is only relevant if md5AuthenticationEnabled is true
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/routing/ospf"

        body_params = [
            "enabled",
            "helloTimerInSeconds",
            "deadTimerInSeconds",
            "areas",
            "v3",
            "md5AuthenticationEnabled",
            "md5AuthenticationKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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
        - portChannelFallback (boolean): Port channel fallback
        - uplinkSelection (object): Settings related to uplink selection on IOS-XE switches.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/settings"

        body_params = [
            "vlan",
            "useCombinedPower",
            "powerExceptions",
            "uplinkClientSampling",
            "macBlocklist",
            "portChannelFallback",
            "uplinkSelection",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "settings/actions/update",
            "body": payload,
        }
        return action

    def updateNetworkSwitchSpanningTree(self, networkId: str, **kwargs):
        """
        **Updates Spanning Tree configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-spanning-tree

        - networkId (string): Network ID
        - enabled (boolean): Network-level spanning Tree enable
        - mode (string): Catalyst Spanning Tree Protocol mode (mst, rpvst+)
        - priorities (array): Spanning tree priority for switches/stacks or switch templates. An empty array will clear the priority settings.
        """

        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["mst", "rpvst+"]
            assert kwargs["mode"] in options, f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/spanningTree"

        body_params = [
            "enabled",
            "mode",
            "priorities",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateNetworkSwitchStack(self, networkId: str, switchStackId: str, **kwargs):
        """
        **Update a switch stack. At least one of 'name' or 'members' must be provided. If 'members' is provided, it replaces the entire stack membership.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - name (string): The name of the switch stack
        - members (array): The complete list of switches that should be in the stack. Minimum 2 and maximum 8 members. Omitting this field leaves stack membership unchanged.
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}"

        body_params = [
            "name",
            "members",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "stacks/actions/update",
            "body": payload,
        }
        return action

    def updateNetworkSwitchStackPortsMirror(
        self, networkId: str, switchStackId: str, source: dict, destination: dict, **kwargs
    ):
        """
        **Update switch port mirrors for switch stacks**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-ports-mirror

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - source (object): Source port details
        - destination (object): Destination port Details
        - tags (array): Port mirror tags
        - role (string): Switch role can be source or destination
        - comment (string): My pretty comment
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/ports/mirror"

        body_params = [
            "source",
            "destination",
            "tags",
            "role",
            "comment",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, name: str, **kwargs):
        """
        **Create a layer 3 interface for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - name (string): A friendly name or description for the interface or VLAN (max length 128 characters).
        - mode (string): L3 Interface mode, can be one of 'vlan', 'routed', 'loopback'. Default is 'vlan'. CS 17.18 or higher is required for 'routed' mode.
        - subnet (string): The network that this L3 interface is on, in CIDR notation (ex. 10.1.1.0/24).
        - switchPortId (string): Switch Port ID when in Routed mode (CS 17.18 or higher required)
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - mtu (integer): The interface MTU. Applies to native switch layer 3 interfaces, including VLAN and routed modes.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
        - isSwitchDefaultGateway (boolean): When true, the switch uses the IPv4 uplink gateway as its IPv4 default gateway. This can only be set if the interface is designated as the IPv4 uplink and the switch is running IOS XE version >= 17.18.3.
        - uplinkV4 (boolean): When true, this interface is used as static IPv4 uplink.
        - candidateUplinkV4 (boolean): When true, this interface is a UAC candidate for IPv4 Uplink.
        - uplinkV6 (boolean): When true, this interface is used as static IPv6 uplink.
        - staticV4Dns1 (string): Primary IPv4 DNS server address
        - staticV4Dns2 (string): Secondary IPv4 DNS server address
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        - loopback (object): The loopback settings of the interface.
        """

        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert kwargs["mode"] in options, f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces"

        body_params = [
            "name",
            "mode",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "mtu",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "isSwitchDefaultGateway",
            "uplinkV4",
            "candidateUplinkV4",
            "uplinkV6",
            "staticV4Dns1",
            "staticV4Dns2",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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
        - switchPortId (string): Switch Port ID when in Routed mode (CS 17.18 or higher required)
        - interfaceIp (string): The IP address that will be used for Layer 3 routing on this VLAN or subnet. This cannot be the same         as the device management IP.
        - mtu (integer): The interface MTU. Applies to native switch layer 3 interfaces, including VLAN and routed modes.
        - multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are:         'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
        - vlanId (integer): The VLAN this L3 interface is on. VLAN must be between 1 and 4094.
        - defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route.         This IP address must exist in a subnet with a L3 interface. Required if this is the first IPv4 interface.
        - isSwitchDefaultGateway (boolean): When true, the switch uses the IPv4 uplink gateway as its IPv4 default gateway. This can only be set if the interface is designated as the IPv4 uplink and the switch is running IOS XE version >= 17.18.3.
        - uplinkV4 (boolean): When true, this interface is used as static IPv4 uplink.
        - candidateUplinkV4 (boolean): When true, this interface is a UAC candidate for IPv4 Uplink.
        - uplinkV6 (boolean): When true, this interface is used as static IPv6 uplink.
        - staticV4Dns1 (string): Primary IPv4 DNS server address
        - staticV4Dns2 (string): Secondary IPv4 DNS server address
        - ospfSettings (object): The OSPF routing settings of the interface.
        - ipv6 (object): The IPv6 settings of the interface.
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        - loopback (object): The loopback settings of the interface.
        """

        kwargs.update(locals())

        if "multicastRouting" in kwargs:
            options = ["IGMP snooping querier", "disabled", "enabled"]
            assert kwargs["multicastRouting"] in options, (
                f'''"multicastRouting" cannot be "{kwargs["multicastRouting"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        interfaceId = urllib.parse.quote(interfaceId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}"

        body_params = [
            "name",
            "subnet",
            "switchPortId",
            "interfaceIp",
            "mtu",
            "multicastRouting",
            "vlanId",
            "defaultGateway",
            "isSwitchDefaultGateway",
            "uplinkV4",
            "candidateUplinkV4",
            "uplinkV6",
            "staticV4Dns1",
            "staticV4Dns2",
            "ospfSettings",
            "ipv6",
            "vrf",
            "loopback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        interfaceId = urllib.parse.quote(interfaceId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}"

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

        if "dhcpMode" in kwargs:
            options = ["dhcpDisabled", "dhcpRelay", "dhcpServer"]
            assert kwargs["dhcpMode"] in options, (
                f'''"dhcpMode" cannot be "{kwargs["dhcpMode"]}", & must be set to one of: {options}'''
            )
        if "dhcpLeaseTime" in kwargs:
            options = ["1 day", "1 hour", "1 week", "12 hours", "30 minutes", "4 hours"]
            assert kwargs["dhcpLeaseTime"] in options, (
                f'''"dhcpLeaseTime" cannot be "{kwargs["dhcpLeaseTime"]}", & must be set to one of: {options}'''
            )
        if "dnsNameserversOption" in kwargs:
            options = ["custom", "googlePublicDns", "openDns"]
            assert kwargs["dnsNameserversOption"] in options, (
                f'''"dnsNameserversOption" cannot be "{kwargs["dnsNameserversOption"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        interfaceId = urllib.parse.quote(interfaceId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp"

        body_params = [
            "dhcpMode",
            "dhcpRelayServerIps",
            "dhcpLeaseTime",
            "dnsNameserversOption",
            "dnsCustomNameservers",
            "bootOptionsEnabled",
            "bootNextServer",
            "bootFileName",
            "dhcpOptions",
            "reservedIpRanges",
            "fixedIpAssignments",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createNetworkSwitchStackRoutingStaticRoute(
        self, networkId: str, switchStackId: str, subnet: str, nextHopIp: str, **kwargs
    ):
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
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
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
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        staticRouteId = urllib.parse.quote(staticRouteId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}"

        body_params = [
            "name",
            "subnet",
            "nextHopIp",
            "managementNextHop",
            "advertiseViaOspfEnabled",
            "preferOverOspfRoutesEnabled",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        switchStackId = urllib.parse.quote(switchStackId, safe="")
        staticRouteId = urllib.parse.quote(staticRouteId, safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}"

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

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/stormControl"

        body_params = [
            "broadcastThreshold",
            "multicastThreshold",
            "unknownUnicastThreshold",
            "treatTheseTrafficTypesAsOneThreshold",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
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

        networkId = urllib.parse.quote(networkId, safe="")
        resource = f"/networks/{networkId}/switch/stp"

        body_params = [
            "rstpEnabled",
            "stpBridgePriority",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateOrganizationConfigTemplateSwitchProfilePortsMirror(
        self, organizationId: str, configTemplateId: str, profileId: str, source: dict, destination: dict, **kwargs
    ):
        """
        **Update a port mirror**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-ports-mirror

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - profileId (string): Profile ID
        - source (object): Source ports mirror configuration
        - destination (object): Destination port mirror configuration
        - tags (array): Port mirror tags
        - role (string): Switch role can be source or destination
        - comment (string): My pretty comment
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        configTemplateId = urllib.parse.quote(configTemplateId, safe="")
        profileId = urllib.parse.quote(profileId, safe="")
        resource = (
            f"/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/mirror"
        )

        body_params = [
            "source",
            "destination",
            "tags",
            "role",
            "comment",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "mirrors/update",
            "body": payload,
        }
        return action

    def updateOrganizationConfigTemplateSwitchProfilePort(
        self, organizationId: str, configTemplateId: str, profileId: str, portId: str, **kwargs
    ):
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
        - type (string): The type of the switch template port ('access', 'trunk', 'stack', 'routed', 'svl' or 'dad').
        - vlan (integer): The VLAN of the switch template port. For a trunk port, this is the native VLAN. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch template port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch template port. Only applicable to trunk ports.
        - activeVlans (string): The VLANs that are active on the switch template port. Only applicable to trunk ports.
        - isolationEnabled (boolean): The isolation status of the switch template port.
        - rstpEnabled (boolean): The rapid spanning tree protocol status.
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard').
        - stpPortFastTrunk (boolean): The state of STP PortFast Trunk on the switch template port.
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
        - highSpeed (object): High speed port enablement settings for C9500-32QC
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["access", "dad", "routed", "stack", "svl", "trunk"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
        if "stpGuard" in kwargs:
            options = ["bpdu guard", "disabled", "loop guard", "root guard"]
            assert kwargs["stpGuard"] in options, (
                f'''"stpGuard" cannot be "{kwargs["stpGuard"]}", & must be set to one of: {options}'''
            )
        if "udld" in kwargs:
            options = ["Alert only", "Enforce"]
            assert kwargs["udld"] in options, f'''"udld" cannot be "{kwargs["udld"]}", & must be set to one of: {options}'''
        if "accessPolicyType" in kwargs:
            options = ["Custom access policy", "MAC allow list", "Open", "Sticky MAC allow list"]
            assert kwargs["accessPolicyType"] in options, (
                f'''"accessPolicyType" cannot be "{kwargs["accessPolicyType"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        configTemplateId = urllib.parse.quote(configTemplateId, safe="")
        profileId = urllib.parse.quote(profileId, safe="")
        portId = urllib.parse.quote(portId, safe="")
        resource = (
            f"/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}"
        )

        body_params = [
            "name",
            "tags",
            "enabled",
            "poeEnabled",
            "type",
            "vlan",
            "voiceVlan",
            "allowedVlans",
            "activeVlans",
            "isolationEnabled",
            "rstpEnabled",
            "stpGuard",
            "stpPortFastTrunk",
            "linkNegotiation",
            "portScheduleId",
            "udld",
            "accessPolicyType",
            "accessPolicyNumber",
            "macAllowList",
            "macWhitelistLimit",
            "stickyMacAllowList",
            "stickyMacAllowListLimit",
            "stormControlEnabled",
            "flexibleStackingEnabled",
            "daiTrusted",
            "profile",
            "dot3az",
            "highSpeed",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def cloneOrganizationSwitchProfilesToTemplateNetwork(self, organizationId: str, **kwargs):
        """
        **Clone existing switch templates into a destination template network.**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-profiles-to-template-network

        - organizationId (string): Organization ID
        - profileIds (array): Switch profile IDs to clone
        - templateNodeGroupId (string): Destination template network ID
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/cloneProfilesToTemplateNetwork"

        body_params = [
            "profileIds",
            "templateNodeGroupId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "cloneProfilesToTemplateNetwork",
            "body": payload,
        }
        return action

    def cloneOrganizationSwitchDevices(self, organizationId: str, sourceSerial: str, targetSerials: list, **kwargs):
        """
        **Clone port-level and some switch-level configuration settings from a source switch to one or more target switches. Cloned settings include: Aggregation Groups, Power Settings, Multicast Settings, MTU Configuration, STP Bridge priority, Port Mirroring**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

        - organizationId (string): Organization ID
        - sourceSerial (string): Serial number of the source switch (must be on a network not bound to a template)
        - targetSerials (array): Array of serial numbers of one or more target switches (must be on a network not bound to a template)
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/devices/clone"

        body_params = [
            "sourceSerial",
            "targetSerials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "settings/actions/clone",
            "body": payload,
        }
        return action

    def createOrganizationSwitchPortsProfile(self, organizationId: str, **kwargs):
        """
        **Create a port profile in an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-ports-profile

        - organizationId (string): Organization ID
        - name (string): The name of the profile.
        - description (string): Text describing the profile.
        - isOrganizationWide (boolean): The scope of the profile whether it is organization level or network level
        - networks (object): The networks which are included/excluded in the profile
        - networkId (string): The network identifier
        - tags (array): Space-seperated list of tags
        - defaultRadiusProfileName (string): When present, the default RADIUS attribute value for RADIUS-based port profile application
        - authentication (object): Authentication settings for RADIUS-based port profile application.
        - port (object): Configuration settings for port profile
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles"

        body_params = [
            "name",
            "description",
            "isOrganizationWide",
            "networks",
            "networkId",
            "tags",
            "defaultRadiusProfileName",
            "authentication",
            "port",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "profiles/create",
            "body": payload,
        }
        return action

    def batchOrganizationSwitchPortsProfilesAssignmentsAssign(self, organizationId: str, items: list, **kwargs):
        """
        **Batch assign or unassign port profiles to switch ports**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-switch-ports-profiles-assignments-assign

        - organizationId (string): Organization ID
        - items (array): Array of assignment operations (max 100)
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/assignments/batchAssign"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "batch_assign",
            "body": payload,
        }
        return action

    def createOrganizationSwitchPortsProfilesAutomation(self, organizationId: str, **kwargs):
        """
        **Create a port profile automation for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-ports-profiles-automation

        - organizationId (string): Organization ID
        - name (string): Name of the port profile automation.
        - description (string): Text describing the port profile automation.
        - fallbackProfile (object): Configuration settings for port profile
        - rules (array): Configuration settings for port profile automation rules
        - assignedSwitchPorts (array): assigned switch ports
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations"

        body_params = [
            "name",
            "description",
            "fallbackProfile",
            "rules",
            "assignedSwitchPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "automations/actions/update",
            "body": payload,
        }
        return action

    def updateOrganizationSwitchPortsProfilesAutomation(self, organizationId: str, id: str, **kwargs):
        """
        **Update a port profile automation in an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-switch-ports-profiles-automation

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of the port profile automation.
        - description (string): Text describing the port profile automation.
        - fallbackProfile (object): Configuration settings for port profile
        - rules (array): Configuration settings for port profile automation rules
        - assignedSwitchPorts (array): assigned switch ports
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations/{id}"

        body_params = [
            "name",
            "description",
            "fallbackProfile",
            "rules",
            "assignedSwitchPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "automations/actions/update",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchPortsProfilesAutomation(self, organizationId: str, id: str):
        """
        **Delete an automation port profile from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profiles-automation

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations/{id}"

        action = {
            "resource": resource,
            "operation": "automations/actions/destroy",
        }
        return action

    def createOrganizationSwitchPortsProfilesNetworksAssignment(
        self, organizationId: str, type: str, profile: dict, network: dict, **kwargs
    ):
        """
        **Create Network and Smart Ports Profile association for a specific profile**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-ports-profiles-networks-assignment

        - organizationId (string): Organization ID
        - type (string): Type of association
        - profile (object): Smart Port Profile object
        - network (object): Network object
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments"

        body_params = [
            "type",
            "profile",
            "network",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "profiles/create",
            "body": payload,
        }
        return action

    def batchOrganizationSwitchPortsProfilesNetworksAssignmentsCreate(self, organizationId: str, items: list, **kwargs):
        """
        **Batch Create Network and Smart Ports Profile associations for a specific profile**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-switch-ports-profiles-networks-assignments-create

        - organizationId (string): Organization ID
        - items (array): Array of network and profile associations
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments/batchCreate"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "batch_create",
            "body": payload,
        }
        return action

    def bulkOrganizationSwitchPortsProfilesNetworksAssignmentsDelete(self, organizationId: str, items: list, **kwargs):
        """
        **Bulk delete Network and Smart Port Profile associations**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-switch-ports-profiles-networks-assignments-delete

        - organizationId (string): Organization ID
        - items (array): Array of assignments to delete
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments/bulkDelete"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "bulk_destroy",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchPortsProfilesNetworksAssignment(self, organizationId: str, assignmentId: str):
        """
        **Delete Network and Smart Port profile association for a specific profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profiles-networks-assignment

        - organizationId (string): Organization ID
        - assignmentId (string): Assignment ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        assignmentId = urllib.parse.quote(assignmentId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments/{assignmentId}"

        action = {
            "resource": resource,
            "operation": "profiles/destroy",
        }
        return action

    def createOrganizationSwitchPortsProfilesRadiusAssignment(self, organizationId: str, network: dict, **kwargs):
        """
        **Create a port profile RADIUS assignment**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-ports-profiles-radius-assignment

        - organizationId (string): Organization ID
        - network (object): The network where the RADIUS name is assigned
        - portProfile (object): The assigned port profile
        - radius (object): The RADIUS options for this assignment
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments"

        body_params = [
            "network",
            "portProfile",
            "radius",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationSwitchPortsProfilesRadiusAssignment(self, organizationId: str, id: str, **kwargs):
        """
        **Update a port profile RADIUS assignment**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-switch-ports-profiles-radius-assignment

        - organizationId (string): Organization ID
        - id (string): ID
        - network (object): The network where the RADIUS name is assigned
        - portProfile (object): The assigned port profile
        - radius (object): The RADIUS options for this assignment
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments/{id}"

        body_params = [
            "network",
            "portProfile",
            "radius",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchPortsProfilesRadiusAssignment(self, organizationId: str, id: str):
        """
        **Deletes a port profile RADIUS assignment**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profiles-radius-assignment

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationSwitchPortsProfile(self, organizationId: str, id: str, **kwargs):
        """
        **Update a port profile in an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-switch-ports-profile

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): The name of the profile.
        - description (string): Text describing the profile.
        - isOrganizationWide (boolean): The scope of the profile whether it is organization level or network level
        - networks (object): The networks which are included/excluded in the profile
        - networkId (string): The network identifier
        - tags (array): Space-seperated list of tags
        - defaultRadiusProfileName (string): When present, the default RADIUS attribute value for RADIUS-based port profile application
        - authentication (object): Authentication settings for RADIUS-based port profile application.
        - port (object): Configuration settings for port profile
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/{id}"

        body_params = [
            "name",
            "description",
            "isOrganizationWide",
            "networks",
            "networkId",
            "tags",
            "defaultRadiusProfileName",
            "authentication",
            "port",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "profiles/update",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchPortsProfile(self, organizationId: str, id: str):
        """
        **Delete a port profile from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profile

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/{id}"

        action = {
            "resource": resource,
            "operation": "profiles/destroy",
        }
        return action

    def createOrganizationSwitchRoutingBgpAutonomousSystem(self, organizationId: str, number: int, **kwargs):
        """
        **Create an autonomous system. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-autonomous-system

        - organizationId (string): Organization ID
        - number (integer): The autonomous system number (CLI: 'router bgp <number>')
        - description (string): A description for the autonomous system
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems"

        body_params = [
            "number",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "systems/create",
            "body": payload,
        }
        return action

    def updateOrganizationSwitchRoutingBgpAutonomousSystem(self, organizationId: str, autonomousSystemId: str, **kwargs):
        """
        **Update an autonomous system. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-switch-routing-bgp-autonomous-system

        - organizationId (string): Organization ID
        - autonomousSystemId (string): Autonomous system ID
        - number (integer): The autonomous system number (CLI: 'router bgp <number>')
        - description (string): A description for the autonomous system
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        autonomousSystemId = urllib.parse.quote(autonomousSystemId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems/{autonomousSystemId}"

        body_params = [
            "number",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "systems/update",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchRoutingBgpAutonomousSystem(self, organizationId: str, autonomousSystemId: str):
        """
        **Delete an autonomous system from an organization. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-autonomous-system

        - organizationId (string): Organization ID
        - autonomousSystemId (string): Autonomous system ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        autonomousSystemId = urllib.parse.quote(autonomousSystemId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems/{autonomousSystemId}"

        action = {
            "resource": resource,
            "operation": "systems/destroy",
        }
        return action

    def createOrganizationSwitchRoutingBgpFiltersFilterListsDeploy(
        self, organizationId: str, filterList: dict, network: dict, rules: list, **kwargs
    ):
        """
        **Create or update a filter list, in addition to its associated rules. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-filters-filter-lists-deploy

        - organizationId (string): Organization ID
        - filterList (object): Information regarding the filter list
        - network (object): Information regarding the network the filter list belongs to
        - rules (array): Information regarding the filter list rules
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists/deploy"

        body_params = [
            "filterList",
            "network",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "deploy",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchRoutingBgpFiltersFilterList(self, organizationId: str, listId: str):
        """
        **Delete a filter list. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-filters-filter-list

        - organizationId (string): Organization ID
        - listId (string): List ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        listId = urllib.parse.quote(listId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists/{listId}"

        action = {
            "resource": resource,
            "operation": "lists/destroy",
        }
        return action

    def createOrganizationSwitchRoutingBgpFiltersPrefixListsDeploy(
        self, organizationId: str, network: dict, prefixList: dict, rules: list, **kwargs
    ):
        """
        **Create or update a prefix list, in addition to its associated rules. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-filters-prefix-lists-deploy

        - organizationId (string): Organization ID
        - network (object): Information regarding the network the prefix list belongs to
        - prefixList (object): Information regarding the prefix list
        - rules (array): Information regarding the prefix list rules
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists/deploy"

        body_params = [
            "network",
            "prefixList",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "deploy",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchRoutingBgpFiltersPrefixList(self, organizationId: str, listId: str):
        """
        **Delete a prefix list. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-filters-prefix-list

        - organizationId (string): Organization ID
        - listId (string): List ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        listId = urllib.parse.quote(listId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists/{listId}"

        action = {
            "resource": resource,
            "operation": "lists/destroy",
        }
        return action

    def createOrganizationSwitchRoutingBgpPeersGroupsDeploy(
        self,
        organizationId: str,
        addressFamily: dict,
        network: dict,
        peerGroup: dict,
        peerGroupAddressFamilyBindingProfile: dict,
        peerGroupProfile: dict,
        policies: list,
        router: dict,
        **kwargs,
    ):
        """
        **Create or update a peer group, in addition to an associated peer group profile, peer group address family binding, peer group address family binding profile and routing policies associated with the peer group. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-peers-groups-deploy

        - organizationId (string): Organization ID
        - addressFamily (object): Information regarding the address family the peer group address family binding belongs to
        - network (object): Information regarding the network the peer group profile belongs to
        - peerGroup (object): Information regarding the peer group
        - peerGroupAddressFamilyBindingProfile (object): Information regarding the peer group address family binding profile
        - peerGroupProfile (object): Information regarding the peer group profile
        - policies (array): Information regarding the routing policies
        - router (object): Information regarding the router this peer group belongs to
        - peerGroupAddressFamilyBinding (object): Information regarding the peer group address family binding. Only required when updating.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/groups/deploy"

        body_params = [
            "addressFamily",
            "network",
            "peerGroup",
            "peerGroupAddressFamilyBinding",
            "peerGroupAddressFamilyBindingProfile",
            "peerGroupProfile",
            "policies",
            "router",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "deploy",
            "body": payload,
        }
        return action

    def createOrganizationSwitchRoutingBgpPeersNeighborsDeploy(
        self,
        organizationId: str,
        addressFamily: dict,
        neighbor: dict,
        neighborAddressFamilyBinding: dict,
        peerGroup: dict,
        policies: list,
        router: dict,
        **kwargs,
    ):
        """
        **Create or update a neighor, in addition to an associated neighbor address family binding and routing policies associated with the neighbor. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-peers-neighbors-deploy

        - organizationId (string): Organization ID
        - addressFamily (object): Information regarding the address family this binding is bound to
        - neighbor (object): Information regarding the BPG neighbor
        - neighborAddressFamilyBinding (object): Information regarding the neighbor address family binding
        - peerGroup (object): Information regarding the peer group this neighbor belongs to
        - policies (array): Information regarding the routing policies related to the neighbor
        - router (object): Information regarding the router this neighbor peers with
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/neighbors/deploy"

        body_params = [
            "addressFamily",
            "neighbor",
            "neighborAddressFamilyBinding",
            "peerGroup",
            "policies",
            "router",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "deploy",
            "body": payload,
        }
        return action

    def createOrganizationSwitchRoutingBgpRoutersDeploy(
        self,
        organizationId: str,
        addressFamily: dict,
        addressFamilyPrefixes: list,
        addressFamilyProfile: dict,
        autonomousSystem: dict,
        router: dict,
        switch: dict,
        **kwargs,
    ):
        """
        **Create a BGP router, in addition to an associated address family, address family prefixes, and address family profile. This is helpful for the initial deployment of a BGP router.. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-routers-deploy

        - organizationId (string): Organization ID
        - addressFamily (object): Information regarding the address family
        - addressFamilyPrefixes (array): The list of network prefixes to which the address family applies
        - addressFamilyProfile (object): Information regarding the profile applied to the address family
        - autonomousSystem (object): Information regarding the router's autonomous system
        - router (object): Information regarding the BPG router
        - switch (object): The router's switch node. When the router is part of a switch stack, this is the switch stack's active node
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/deploy"

        body_params = [
            "addressFamily",
            "addressFamilyPrefixes",
            "addressFamilyProfile",
            "autonomousSystem",
            "router",
            "switch",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "deploy",
            "body": payload,
        }
        return action

    def createOrganizationSwitchRoutingBgpRoutersPeersDeploy(
        self, organizationId: str, addressFamily: dict, peerGroups: list, router: dict, **kwargs
    ):
        """
        **Create and update listen ranges, update peers' enabled flag, and delete peer groups for a BGP router. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-routers-peers-deploy

        - organizationId (string): Organization ID
        - addressFamily (object): Information regarding the address family
        - peerGroups (array): Information regarding the peer group peers for a router's peer group
        - router (object): Information regarding the BPG router
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/peers/deploy"

        body_params = [
            "addressFamily",
            "peerGroups",
            "router",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "peers_deploy",
            "body": payload,
        }
        return action

    def deleteOrganizationSwitchRoutingBgpRouter(self, organizationId: str, routerId: str):
        """
        **Delete a router from an organization. Border Gateway Protocol requires IOS XE 17.18 or higher**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-router

        - organizationId (string): Organization ID
        - routerId (string): Router ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        routerId = urllib.parse.quote(routerId, safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/{routerId}"

        action = {
            "resource": resource,
            "operation": "ms/actions/bgp/routers/destroy",
        }
        return action
