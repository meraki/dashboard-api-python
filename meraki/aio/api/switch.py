import urllib


class AsyncSwitch:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getDeviceSwitchPorts(self, serial: str, **kwargs):
        """
        **List the switch ports for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports

        - serial (string): Serial
        - hideDefaultPorts (boolean): Optional flag that, when true, will hide modular switchports that may not be connected to the device at the moment
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports"],
            "operation": "getDeviceSwitchPorts",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports"

        query_params = [
            "hideDefaultPorts",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceSwitchPorts: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def cycleDeviceSwitchPorts(self, serial: str, ports: list, **kwargs):
        """
        **Cycle a set of switch ports on non-Catalyst MS devices**
        https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports

        - serial (string): Serial
        - ports (array): List of switch ports
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "liveTools", "ports"],
            "operation": "cycleDeviceSwitchPorts",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports/cycle"

        body_params = [
            "ports",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"cycleDeviceSwitchPorts: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "mirror"],
            "operation": "updateDeviceSwitchPortsMirror",
        }
        serial = urllib.parse.quote(str(serial), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceSwitchPortsMirror: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

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
            "tags": ["switch", "monitor", "ports", "statuses"],
            "operation": "getDeviceSwitchPortsStatuses",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports/statuses"

        query_params = [
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceSwitchPortsStatuses: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getDeviceSwitchPortsStatusesPackets(self, serial: str, **kwargs):
        """
        **Return the packet counters for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The value is used only to determine the elapsed duration between t0 and the time of the request; the API snaps that duration to the nearest preset window (5 minutes, 15 minutes, 1 hour, or 1 day).
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify t0. The value must be in seconds and be less than or equal to 86400 seconds (1 day). The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "statuses", "packets"],
            "operation": "getDeviceSwitchPortsStatusesPackets",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/ports/statuses/packets"

        query_params = [
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceSwitchPortsStatusesPackets: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getDeviceSwitchPort(self, serial: str, portId: str):
        """
        **Return a switch port**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port

        - serial (string): Serial
        - portId (string): Port ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports"],
            "operation": "getDeviceSwitchPort",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        portId = urllib.parse.quote(str(portId), safe="")
        resource = f"/devices/{serial}/switch/ports/{portId}"

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

        metadata = {
            "tags": ["switch", "configure", "ports"],
            "operation": "updateDeviceSwitchPort",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        portId = urllib.parse.quote(str(portId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceSwitchPort: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getDeviceSwitchRoutingInterfaces(self, serial: str, **kwargs):
        """
        **List layer 3 interfaces for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interfaces

        - serial (string): Serial
        - mode (string): Optional parameter to filter L3 interfaces by mode.
        - protocol (string): Optional parameter to filter L3 interfaces by protocol.
        """

        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert kwargs["mode"] in options, f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
        if "protocol" in kwargs:
            options = ["ipv4", "ipv6"]
            assert kwargs["protocol"] in options, (
                f'''"protocol" cannot be "{kwargs["protocol"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "getDeviceSwitchRoutingInterfaces",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces"

        query_params = [
            "mode",
            "protocol",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceSwitchRoutingInterfaces: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

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

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "createDeviceSwitchRoutingInterface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceSwitchRoutingInterface: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str):
        """
        **Return a layer 3 interface for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "getDeviceSwitchRoutingInterface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interfaceId}"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "updateDeviceSwitchRoutingInterface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceSwitchRoutingInterface: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteDeviceSwitchRoutingInterface(self, serial: str, interfaceId: str):
        """
        **Delete a layer 3 interface from the switch**
        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-interface

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces"],
            "operation": "deleteDeviceSwitchRoutingInterface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interfaceId}"

        return self._session.delete(metadata, resource)

    def getDeviceSwitchRoutingInterfaceDhcp(self, serial: str, interfaceId: str):
        """
        **Return a layer 3 interface DHCP configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-interface-dhcp

        - serial (string): Serial
        - interfaceId (string): Interface ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces", "dhcp"],
            "operation": "getDeviceSwitchRoutingInterfaceDhcp",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
        resource = f"/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp"

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

        metadata = {
            "tags": ["switch", "configure", "routing", "interfaces", "dhcp"],
            "operation": "updateDeviceSwitchRoutingInterfaceDhcp",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateDeviceSwitchRoutingInterfaceDhcp: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getDeviceSwitchRoutingStaticRoutes(self, serial: str):
        """
        **List layer 3 static routes for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-routes

        - serial (string): Serial
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "getDeviceSwitchRoutingStaticRoutes",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes"

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
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "createDeviceSwitchRoutingStaticRoute",
        }
        serial = urllib.parse.quote(str(serial), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceSwitchRoutingStaticRoute: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str):
        """
        **Return a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "getDeviceSwitchRoutingStaticRoute",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}"

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
        - managementNextHop (string): Optional fallback IP address for management traffic
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "updateDeviceSwitchRoutingStaticRoute",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceSwitchRoutingStaticRoute: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteDeviceSwitchRoutingStaticRoute(self, serial: str, staticRouteId: str):
        """
        **Delete a layer 3 static route for a switch**
        https://developer.cisco.com/meraki/api-v1/#!delete-device-switch-routing-static-route

        - serial (string): Serial
        - staticRouteId (string): Static route ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "staticRoutes"],
            "operation": "deleteDeviceSwitchRoutingStaticRoute",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe="")
        resource = f"/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}"

        return self._session.delete(metadata, resource)

    def getDeviceSwitchWarmSpare(self, serial: str):
        """
        **Return warm spare configuration for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-warm-spare

        - serial (string): Serial
        """

        metadata = {
            "tags": ["switch", "configure", "warmSpare"],
            "operation": "getDeviceSwitchWarmSpare",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/warmSpare"

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
            "tags": ["switch", "configure", "warmSpare"],
            "operation": "updateDeviceSwitchWarmSpare",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/switch/warmSpare"

        body_params = [
            "enabled",
            "spareSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceSwitchWarmSpare: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchAccessControlLists(self, networkId: str):
        """
        **Return the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "accessControlLists"],
            "operation": "getNetworkSwitchAccessControlLists",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/accessControlLists"

        return self._session.get(metadata, resource)

    def updateNetworkSwitchAccessControlLists(self, networkId: str, rules: list, **kwargs):
        """
        **Update the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-control-lists

        - networkId (string): Network ID
        - rules (array): An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "accessControlLists"],
            "operation": "updateNetworkSwitchAccessControlLists",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/accessControlLists"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchAccessControlLists: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchAccessPolicies(self, networkId: str):
        """
        **List the access policies for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "getNetworkSwitchAccessPolicies",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/accessPolicies"

        return self._session.get(metadata, resource)

    def createNetworkSwitchAccessPolicy(
        self, networkId: str, name: str, radiusServers: list, radiusAccountingEnabled: bool, **kwargs
    ):
        """
        **Create an access policy for a switch network**
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

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "createNetworkSwitchAccessPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSwitchAccessPolicy: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str):
        """
        **Return a specific access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        """

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "getNetworkSwitchAccessPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        accessPolicyNumber = urllib.parse.quote(str(accessPolicyNumber), safe="")
        resource = f"/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}"

        return self._session.get(metadata, resource)

    def updateNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str, **kwargs):
        """
        **Update an access policy for a switch network**
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

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "updateNetworkSwitchAccessPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        accessPolicyNumber = urllib.parse.quote(str(accessPolicyNumber), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchAccessPolicy: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str):
        """
        **Delete an access policy for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy

        - networkId (string): Network ID
        - accessPolicyNumber (string): Access policy number
        """

        metadata = {
            "tags": ["switch", "configure", "accessPolicies"],
            "operation": "deleteNetworkSwitchAccessPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        accessPolicyNumber = urllib.parse.quote(str(accessPolicyNumber), safe="")
        resource = f"/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}"

        return self._session.delete(metadata, resource)

    def getNetworkSwitchAlternateManagementInterface(self, networkId: str):
        """
        **Return the switch alternate management interface for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-alternate-management-interface

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "alternateManagementInterface"],
            "operation": "getNetworkSwitchAlternateManagementInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/alternateManagementInterface"

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
            "tags": ["switch", "configure", "alternateManagementInterface"],
            "operation": "updateNetworkSwitchAlternateManagementInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/alternateManagementInterface"

        body_params = [
            "enabled",
            "vlanId",
            "protocols",
            "switches",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchAlternateManagementInterface: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchDhcpV4ServersSeen(self, networkId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["switch", "configure", "dhcp", "v4", "servers", "seen"],
            "operation": "getNetworkSwitchDhcpV4ServersSeen",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dhcp/v4/servers/seen"

        query_params = [
            "t0",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkSwitchDhcpV4ServersSeen: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkSwitchDhcpServerPolicy(self, networkId: str):
        """
        **Return the DHCP server settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy"],
            "operation": "getNetworkSwitchDhcpServerPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy"

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

        if "defaultPolicy" in kwargs:
            options = ["allow", "block"]
            assert kwargs["defaultPolicy"] in options, (
                f'''"defaultPolicy" cannot be "{kwargs["defaultPolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy"],
            "operation": "updateNetworkSwitchDhcpServerPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy"

        body_params = [
            "alerts",
            "defaultPolicy",
            "allowedServers",
            "blockedServers",
            "arpInspection",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchDhcpServerPolicy: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers(
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkSwitchDhcpServerPolicyArpInspectionTrustedServers: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers"

        body_params = [
            "mac",
            "vlan",
            "ipv4",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        trustedServerId = urllib.parse.quote(str(trustedServerId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}"

        body_params = [
            "mac",
            "vlan",
            "ipv4",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer(self, networkId: str, trustedServerId: str):
        """
        **Remove a server from being trusted by Dynamic ARP Inspection on this network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-dhcp-server-policy-arp-inspection-trusted-server

        - networkId (string): Network ID
        - trustedServerId (string): Trusted server ID
        """

        metadata = {
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "trustedServers"],
            "operation": "deleteNetworkSwitchDhcpServerPolicyArpInspectionTrustedServer",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        trustedServerId = urllib.parse.quote(str(trustedServerId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers/{trustedServerId}"

        return self._session.delete(metadata, resource)

    def getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice(
        self, networkId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["switch", "configure", "dhcpServerPolicy", "arpInspection", "warnings", "byDevice"],
            "operation": "getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkSwitchDhcpServerPolicyArpInspectionWarningsByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkSwitchDscpToCosMappings(self, networkId: str):
        """
        **Return the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "dscpToCosMappings"],
            "operation": "getNetworkSwitchDscpToCosMappings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dscpToCosMappings"

        return self._session.get(metadata, resource)

    def updateNetworkSwitchDscpToCosMappings(self, networkId: str, mappings: list, **kwargs):
        """
        **Update the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings

        - networkId (string): Network ID
        - mappings (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "dscpToCosMappings"],
            "operation": "updateNetworkSwitchDscpToCosMappings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/dscpToCosMappings"

        body_params = [
            "mappings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchDscpToCosMappings: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchLinkAggregations(self, networkId: str, **kwargs):
        """
        **List link aggregation groups**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations

        - networkId (string): Network ID
        - serials (array): Optional parameter to filter by device serial numbers. Matches multiple exact serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "getNetworkSwitchLinkAggregations",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations"

        query_params = [
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkSwitchLinkAggregations: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

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
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "createNetworkSwitchLinkAggregation",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations"

        body_params = [
            "switchPorts",
            "switchProfilePorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSwitchLinkAggregation: ignoring unrecognized kwargs: {invalid}")

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
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "updateNetworkSwitchLinkAggregation",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        linkAggregationId = urllib.parse.quote(str(linkAggregationId), safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations/{linkAggregationId}"

        body_params = [
            "switchPorts",
            "switchProfilePorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchLinkAggregation: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str):
        """
        **Split a link aggregation group into separate ports**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation

        - networkId (string): Network ID
        - linkAggregationId (string): Link aggregation ID
        """

        metadata = {
            "tags": ["switch", "configure", "linkAggregations"],
            "operation": "deleteNetworkSwitchLinkAggregation",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        linkAggregationId = urllib.parse.quote(str(linkAggregationId), safe="")
        resource = f"/networks/{networkId}/switch/linkAggregations/{linkAggregationId}"

        return self._session.delete(metadata, resource)

    def getNetworkSwitchMtu(self, networkId: str):
        """
        **Return the MTU configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "mtu"],
            "operation": "getNetworkSwitchMtu",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/mtu"

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
            "tags": ["switch", "configure", "mtu"],
            "operation": "updateNetworkSwitchMtu",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/mtu"

        body_params = [
            "defaultMtuSize",
            "overrides",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchMtu: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchPortSchedules(self, networkId: str):
        """
        **List switch port schedules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "getNetworkSwitchPortSchedules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/portSchedules"

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
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "createNetworkSwitchPortSchedule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/portSchedules"

        body_params = [
            "name",
            "portSchedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSwitchPortSchedule: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def deleteNetworkSwitchPortSchedule(self, networkId: str, portScheduleId: str):
        """
        **Delete a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule

        - networkId (string): Network ID
        - portScheduleId (string): Port schedule ID
        """

        metadata = {
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "deleteNetworkSwitchPortSchedule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        portScheduleId = urllib.parse.quote(str(portScheduleId), safe="")
        resource = f"/networks/{networkId}/switch/portSchedules/{portScheduleId}"

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
            "tags": ["switch", "configure", "portSchedules"],
            "operation": "updateNetworkSwitchPortSchedule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        portScheduleId = urllib.parse.quote(str(portScheduleId), safe="")
        resource = f"/networks/{networkId}/switch/portSchedules/{portScheduleId}"

        body_params = [
            "name",
            "portSchedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchPortSchedule: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchPortsProfiles(self, networkId: str):
        """
        **List the port profiles in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-ports-profiles

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "getNetworkSwitchPortsProfiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/ports/profiles"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "createNetworkSwitchPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSwitchPortsProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "updateNetworkSwitchPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        id = urllib.parse.quote(str(id), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchPortsProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSwitchPortsProfile(self, networkId: str, id: str):
        """
        **Delete a port profile from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-ports-profile

        - networkId (string): Network ID
        - id (string): ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "deleteNetworkSwitchPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/networks/{networkId}/switch/ports/profiles/{id}"

        return self._session.delete(metadata, resource)

    def getNetworkSwitchQosRules(self, networkId: str):
        """
        **List quality of service rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "getNetworkSwitchQosRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/qosRules"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "createNetworkSwitchQosRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSwitchQosRule: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchQosRulesOrder(self, networkId: str):
        """
        **Return the quality of service rule IDs by order in which they will be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "qosRules", "order"],
            "operation": "getNetworkSwitchQosRulesOrder",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/qosRules/order"

        return self._session.get(metadata, resource)

    def updateNetworkSwitchQosRulesOrder(self, networkId: str, ruleIds: list, **kwargs):
        """
        **Update the order in which the rules should be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order

        - networkId (string): Network ID
        - ruleIds (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "qosRules", "order"],
            "operation": "updateNetworkSwitchQosRulesOrder",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/qosRules/order"

        body_params = [
            "ruleIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchQosRulesOrder: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Return a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        """

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "getNetworkSwitchQosRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        qosRuleId = urllib.parse.quote(str(qosRuleId), safe="")
        resource = f"/networks/{networkId}/switch/qosRules/{qosRuleId}"

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Delete a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule

        - networkId (string): Network ID
        - qosRuleId (string): Qos rule ID
        """

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "deleteNetworkSwitchQosRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        qosRuleId = urllib.parse.quote(str(qosRuleId), safe="")
        resource = f"/networks/{networkId}/switch/qosRules/{qosRuleId}"

        return self._session.delete(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "qosRules"],
            "operation": "updateNetworkSwitchQosRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        qosRuleId = urllib.parse.quote(str(qosRuleId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchQosRule: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchRaGuardPolicy(self, networkId: str):
        """
        **Return RA Guard settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-ra-guard-policy

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "raGuardPolicy"],
            "operation": "getNetworkSwitchRaGuardPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/raGuardPolicy"

        return self._session.get(metadata, resource)

    def updateNetworkSwitchRaGuardPolicy(self, networkId: str, **kwargs):
        """
        **Update RA Guard settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-ra-guard-policy

        - networkId (string): Network ID
        - defaultPolicy (string): New Router Advertisers are 'allowed' or 'blocked'. Default value is 'allowed'.
        - allowedServers (array): List the MAC addresses of Router Advertisers to permit on the network when defaultPolicy is set to blocked.
        - blockedServers (array): List the MAC addresses of Router Advertisers to block on the network when defaultPolicy is set to allowed.
        """

        kwargs.update(locals())

        if "defaultPolicy" in kwargs:
            options = ["allowed", "blocked"]
            assert kwargs["defaultPolicy"] in options, (
                f'''"defaultPolicy" cannot be "{kwargs["defaultPolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "raGuardPolicy"],
            "operation": "updateNetworkSwitchRaGuardPolicy",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/raGuardPolicy"

        body_params = [
            "defaultPolicy",
            "allowedServers",
            "blockedServers",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchRaGuardPolicy: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchRoutingMulticast(self, networkId: str):
        """
        **Return multicast settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast"],
            "operation": "getNetworkSwitchRoutingMulticast",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast"

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
            "tags": ["switch", "configure", "routing", "multicast"],
            "operation": "updateNetworkSwitchRoutingMulticast",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast"

        body_params = [
            "defaultSettings",
            "overrides",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchRoutingMulticast: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchRoutingMulticastRendezvousPoints(self, networkId: str):
        """
        **List multicast rendezvous points**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-points

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "getNetworkSwitchRoutingMulticastRendezvousPoints",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "createNetworkSwitchRoutingMulticastRendezvousPoint",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints"

        body_params = [
            "interfaceIp",
            "multicastGroup",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkSwitchRoutingMulticastRendezvousPoint: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str):
        """
        **Return a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "getNetworkSwitchRoutingMulticastRendezvousPoint",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rendezvousPointId = urllib.parse.quote(str(rendezvousPointId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}"

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str):
        """
        **Delete a multicast rendezvous point**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-routing-multicast-rendezvous-point

        - networkId (string): Network ID
        - rendezvousPointId (string): Rendezvous point ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "deleteNetworkSwitchRoutingMulticastRendezvousPoint",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rendezvousPointId = urllib.parse.quote(str(rendezvousPointId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}"

        return self._session.delete(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "routing", "multicast", "rendezvousPoints"],
            "operation": "updateNetworkSwitchRoutingMulticastRendezvousPoint",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rendezvousPointId = urllib.parse.quote(str(rendezvousPointId), safe="")
        resource = f"/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}"

        body_params = [
            "interfaceIp",
            "multicastGroup",
            "vrf",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchRoutingMulticastRendezvousPoint: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchRoutingOspf(self, networkId: str, **kwargs):
        """
        **Return layer 3 OSPF routing configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-ospf

        - networkId (string): Network ID
        - vrf (string): The VRF to return the OSPF routing configuration for. When not provided, the default VRF is used. Included on networks with IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "ospf"],
            "operation": "getNetworkSwitchRoutingOspf",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/routing/ospf"

        query_params = [
            "vrf",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkSwitchRoutingOspf: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

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

        metadata = {
            "tags": ["switch", "configure", "routing", "ospf"],
            "operation": "updateNetworkSwitchRoutingOspf",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchRoutingOspf: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettings(self, networkId: str):
        """
        **Returns the switch network settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "settings"],
            "operation": "getNetworkSwitchSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/settings"

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
        - portChannelFallback (boolean): Port channel fallback
        - uplinkSelection (object): Settings related to uplink selection on IOS-XE switches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "settings"],
            "operation": "updateNetworkSwitchSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchSettings: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

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

        metadata = {
            "tags": ["switch", "configure", "spanningTree"],
            "operation": "updateNetworkSwitchSpanningTree",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/spanningTree"

        body_params = [
            "enabled",
            "mode",
            "priorities",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchSpanningTree: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchStacks(self, networkId: str):
        """
        **List the switch stacks in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stacks

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "getNetworkSwitchStacks",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/stacks"

        return self._session.get(metadata, resource)

    def createNetworkSwitchStack(self, networkId: str, name: str, serials: list, **kwargs):
        """
        **Create a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack

        - networkId (string): Network ID
        - name (string): The name of the new stack
        - serials (array): An array of switch serials to be added into the new stack
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "createNetworkSwitchStack",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/stacks"

        body_params = [
            "name",
            "serials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSwitchStack: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateNetworkSwitchStack(self, networkId: str, switchStackId: str, **kwargs):
        """
        **Update a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - name (string): The name of the stack
        - members (array): The list of switches that should be in the stack
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "updateNetworkSwitchStack",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}"

        body_params = [
            "name",
            "members",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchStack: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Show a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "getNetworkSwitchStack",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}"

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Delete a stack**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "deleteNetworkSwitchStack",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}"

        return self._session.delete(metadata, resource)

    def addNetworkSwitchStack(self, networkId: str, switchStackId: str, serial: str, **kwargs):
        """
        **Add a switch to a stack**
        https://developer.cisco.com/meraki/api-v1/#!add-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - serial (string): The serial of the switch to be added
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "addNetworkSwitchStack",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/add"

        body_params = [
            "serial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"addNetworkSwitchStack: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["switch", "configure", "stacks", "ports", "mirror"],
            "operation": "updateNetworkSwitchStackPortsMirror",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/ports/mirror"

        body_params = [
            "source",
            "destination",
            "tags",
            "role",
            "comment",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchStackPortsMirror: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def removeNetworkSwitchStack(self, networkId: str, switchStackId: str, serial: str, **kwargs):
        """
        **Remove a switch from a stack**
        https://developer.cisco.com/meraki/api-v1/#!remove-network-switch-stack

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - serial (string): The serial of the switch to be removed
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "stacks"],
            "operation": "removeNetworkSwitchStack",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/remove"

        body_params = [
            "serial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"removeNetworkSwitchStack: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchStackRoutingInterfaces(self, networkId: str, switchStackId: str, **kwargs):
        """
        **List layer 3 interfaces for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-interfaces

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        - mode (string): Optional parameter to filter L3 interfaces by mode.
        - protocol (string): Optional parameter to filter L3 interfaces by protocol.
        """

        kwargs.update(locals())

        if "mode" in kwargs:
            options = ["loopback", "oob_management", "routed", "vlan"]
            assert kwargs["mode"] in options, f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''
        if "protocol" in kwargs:
            options = ["ipv4", "ipv6"]
            assert kwargs["protocol"] in options, (
                f'''"protocol" cannot be "{kwargs["protocol"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "getNetworkSwitchStackRoutingInterfaces",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces"

        query_params = [
            "mode",
            "protocol",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkSwitchStackRoutingInterfaces: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

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

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "createNetworkSwitchStackRoutingInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkSwitchStackRoutingInterface: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "getNetworkSwitchStackRoutingInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "updateNetworkSwitchStackRoutingInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchStackRoutingInterface: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["switch", "configure", "stacks", "routing", "interfaces"],
            "operation": "deleteNetworkSwitchStackRoutingInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}"

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
            "tags": ["switch", "configure", "stacks", "routing", "interfaces", "dhcp"],
            "operation": "getNetworkSwitchStackRoutingInterfaceDhcp",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp"

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

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "interfaces", "dhcp"],
            "operation": "updateNetworkSwitchStackRoutingInterfaceDhcp",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        interfaceId = urllib.parse.quote(str(interfaceId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchStackRoutingInterfaceDhcp: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchStackRoutingStaticRoutes(self, networkId: str, switchStackId: str):
        """
        **List layer 3 static routes for a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stack-routing-static-routes

        - networkId (string): Network ID
        - switchStackId (string): Switch stack ID
        """

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "getNetworkSwitchStackRoutingStaticRoutes",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "createNetworkSwitchStackRoutingStaticRoute",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkSwitchStackRoutingStaticRoute: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "getNetworkSwitchStackRoutingStaticRoute",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}"

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
        - managementNextHop (string): Optional fallback IP address for management traffic
        - advertiseViaOspfEnabled (boolean): Option to advertise static route via OSPF
        - preferOverOspfRoutesEnabled (boolean): Option to prefer static route over OSPF routes
        - vrf (object): The VRF settings of the interface. Requires IOS XE 17.18 or higher
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "updateNetworkSwitchStackRoutingStaticRoute",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkSwitchStackRoutingStaticRoute: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["switch", "configure", "stacks", "routing", "staticRoutes"],
            "operation": "deleteNetworkSwitchStackRoutingStaticRoute",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        switchStackId = urllib.parse.quote(str(switchStackId), safe="")
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe="")
        resource = f"/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}"

        return self._session.delete(metadata, resource)

    def getNetworkSwitchStormControl(self, networkId: str):
        """
        **Return the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "stormControl"],
            "operation": "getNetworkSwitchStormControl",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/stormControl"

        return self._session.get(metadata, resource)

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
            "tags": ["switch", "configure", "stormControl"],
            "operation": "updateNetworkSwitchStormControl",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/stormControl"

        body_params = [
            "broadcastThreshold",
            "multicastThreshold",
            "unknownUnicastThreshold",
            "treatTheseTrafficTypesAsOneThreshold",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchStormControl: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchStp(self, networkId: str):
        """
        **Returns STP settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["switch", "configure", "stp"],
            "operation": "getNetworkSwitchStp",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/stp"

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
            "tags": ["switch", "configure", "stp"],
            "operation": "updateNetworkSwitchStp",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/switch/stp"

        body_params = [
            "rstpEnabled",
            "stpBridgePriority",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSwitchStp: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationConfigTemplatesSwitchProfilesPortsMirrorsBySwitchProfile(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **list the port mirror configurations in an organization by switch profile**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates-switch-profiles-ports-mirrors-by-switch-profile

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - configTemplateIds (array): Optional parameter to filter the result set by the included set of config template IDs
        - ids (array): A list of switch profile ids. The returned profiles will be filtered to only include these ids.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports", "mirrors", "bySwitchProfile"],
            "operation": "getOrganizationConfigTemplatesSwitchProfilesPortsMirrorsBySwitchProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates/switch/profiles/ports/mirrors/bySwitchProfile"

        query_params = [
            "configTemplateIds",
            "ids",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "configTemplateIds",
            "ids",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationConfigTemplatesSwitchProfilesPortsMirrorsBySwitchProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationConfigTemplateSwitchProfiles(self, organizationId: str, configTemplateId: str):
        """
        **List the switch templates for your switch template configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        """

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles"],
            "operation": "getOrganizationConfigTemplateSwitchProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles"

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
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "getOrganizationConfigTemplateSwitchProfilePorts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports", "mirror"],
            "operation": "updateOrganizationConfigTemplateSwitchProfilePortsMirror",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationConfigTemplateSwitchProfilePortsMirror: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationConfigTemplateSwitchProfilePort(
        self, organizationId: str, configTemplateId: str, profileId: str, portId: str
    ):
        """
        **Return a switch template port**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - profileId (string): Profile ID
        - portId (string): Port ID
        """

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "getOrganizationConfigTemplateSwitchProfilePort",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        portId = urllib.parse.quote(str(portId), safe="")
        resource = (
            f"/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}"
        )

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "configTemplates", "profiles", "ports"],
            "operation": "updateOrganizationConfigTemplateSwitchProfilePort",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        portId = urllib.parse.quote(str(portId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationConfigTemplateSwitchProfilePort: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationSummarySwitchPowerHistory(self, organizationId: str, **kwargs):
        """
        **Returns the total PoE power draw for all switch ports in the organization over the requested timespan (by default the last 24 hours)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-switch-power-history

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "summary", "power", "history"],
            "operation": "getOrganizationSummarySwitchPowerHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/switch/power/history"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummarySwitchPowerHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchAlertsPoeByDevice(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Gets all poe related alerts over a given network and returns information by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-alerts-poe-by-device

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "alerts", "poe", "byDevice"],
            "operation": "getOrganizationSwitchAlertsPoeByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/alerts/poe/byDevice"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchAlertsPoeByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def aurora2OrganizationSwitchSwitchTemplates(self, organizationId: str):
        """
        **List switch templates running IOS XE Catalyst firmware.**
        https://developer.cisco.com/meraki/api-v1/#!aurora-2-organization-switch-switch-templates

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["switch", "configure"],
            "operation": "aurora2OrganizationSwitchSwitchTemplates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/aurora2SwitchTemplates"

        return self._session.get(metadata, resource)

    def getOrganizationSwitchClientsConnectionsAuthenticationByClient(self, organizationId: str, **kwargs):
        """
        **Summarizes authentication outcomes per switch client across an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-clients-connections-authentication-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "clients", "connections", "authentication", "byClient"],
            "operation": "getOrganizationSwitchClientsConnectionsAuthenticationByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/clients/connections/authentication/byClient"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchClientsConnectionsAuthenticationByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchClientsConnectionsDhcpByClient(self, organizationId: str, **kwargs):
        """
        **Get IP assignment for all clients in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-clients-connections-dhcp-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "clients", "connections", "dhcp", "byClient"],
            "operation": "getOrganizationSwitchClientsConnectionsDhcpByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/clients/connections/dhcp/byClient"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchClientsConnectionsDhcpByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchClientsConnectionsSwitchPortStatusByClient(self, organizationId: str, **kwargs):
        """
        **Switch port status by client.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-clients-connections-switch-port-status-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "clients", "connections", "switchPortStatus", "byClient"],
            "operation": "getOrganizationSwitchClientsConnectionsSwitchPortStatusByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/clients/connections/switchPortStatus/byClient"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchClientsConnectionsSwitchPortStatusByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def cloneOrganizationSwitchProfilesToTemplateNetwork(self, organizationId: str, **kwargs):
        """
        **Clone existing switch templates into a destination template network.**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-profiles-to-template-network

        - organizationId (string): Organization ID
        - profileIds (array): Switch profile IDs to clone
        - templateNodeGroupId (string): Destination template network ID
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure"],
            "operation": "cloneOrganizationSwitchProfilesToTemplateNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/cloneProfilesToTemplateNetwork"

        body_params = [
            "profileIds",
            "templateNodeGroupId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"cloneOrganizationSwitchProfilesToTemplateNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchConnectivityLanLinkErrorsByDeviceByPort(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Lan link errors by device and port.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-connectivity-lan-link-errors-by-device-by-port

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "connectivity", "lanLink", "errors", "byDevice", "byPort"],
            "operation": "getOrganizationSwitchConnectivityLanLinkErrorsByDeviceByPort",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/connectivity/lanLink/errors/byDevice/byPort"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchConnectivityLanLinkErrorsByDeviceByPort: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchConnectivityLanStpErrorsByDeviceByPort(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Lan STP errors by device and port.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-connectivity-lan-stp-errors-by-device-by-port

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "connectivity", "lanStp", "errors", "byDevice", "byPort"],
            "operation": "getOrganizationSwitchConnectivityLanStpErrorsByDeviceByPort",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/connectivity/lanStp/errors/byDevice/byPort"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchConnectivityLanStpErrorsByDeviceByPort: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchConnectivityVrrpFailuresByDevice(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Gets all vrrp related alerts over a given network and returns information by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-connectivity-vrrp-failures-by-device

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "connectivity", "vrrp", "failures", "byDevice"],
            "operation": "getOrganizationSwitchConnectivityVrrpFailuresByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/connectivity/vrrp/failures/byDevice"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchConnectivityVrrpFailuresByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def cloneOrganizationSwitchDevices(self, organizationId: str, sourceSerial: str, targetSerials: list, **kwargs):
        """
        **Clone port-level and some switch-level configuration settings from a source switch to one or more target switches**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices

        - organizationId (string): Organization ID
        - sourceSerial (string): Serial number of the source switch (must be on a network not bound to a template)
        - targetSerials (array): Array of serial numbers of one or more target switches (must be on a network not bound to a template)
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "devices"],
            "operation": "cloneOrganizationSwitchDevices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/devices/clone"

        body_params = [
            "sourceSerial",
            "targetSerials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"cloneOrganizationSwitchDevices: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchDevicesSystemQueuesHistoryBySwitchByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Return a historical record of packet transmission and loss, broken down by protocol, for insight into switch device health.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-devices-system-queues-history-by-switch-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 1200, 14400, 86400. The default is 1200. Interval is calculated if time params are provided.
        - networkIds (array): Optional parameter to filter connectivity history by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter connectivity history by switch.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "devices", "system", "queues", "history", "bySwitch", "byInterval"],
            "operation": "getOrganizationSwitchDevicesSystemQueuesHistoryBySwitchByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/devices/system/queues/history/bySwitch/byInterval"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchDevicesSystemQueuesHistoryBySwitchByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsBySwitch(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the switchports in an organization by switch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - extendedParams (boolean): Optional flag to return all of the switchport data vs smaller dataset
        - hideDefaultPorts (boolean): Optional flag that, when true, will hide modular switchports that may not be connected to the device at the moment
        - type (array): Optional parameter to filter switchports by type ('access', 'trunk', 'stack', 'routed', 'svl' or 'dad'). All types are selected if not supplied.
        - configurationUpdatedAfter (string): Optional parameter to filter items to switches where the configuration has been updated after the given timestamp.
        - mac (string): Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match.
        - macs (array): Optional parameter to filter items to switches that have one of the provided MAC addresses.
        - name (string): Optional parameter to filter items to switches with names that contain the search term or are an exact match.
        - networkIds (array): Optional parameter to filter items to switches in one of the provided networks.
        - portProfileIds (array): Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles.
        - serial (string): Optional parameter to filter items to switches with serial number that contains the search term or are an exact match.
        - serials (array): Optional parameter to filter items to switches that have one of the provided serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "bySwitch"],
            "operation": "getOrganizationSwitchPortsBySwitch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/bySwitch"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "extendedParams",
            "hideDefaultPorts",
            "type",
            "configurationUpdatedAfter",
            "mac",
            "macs",
            "name",
            "networkIds",
            "portProfileIds",
            "serial",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "type",
            "macs",
            "networkIds",
            "portProfileIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSwitchPortsBySwitch: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsClientsOverviewByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the number of clients for all switchports with at least one online client in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-clients-overview-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Optional parameter to filter items to switches where the configuration has been updated after the given timestamp.
        - mac (string): Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match.
        - macs (array): Optional parameter to filter items to switches that have one of the provided MAC addresses.
        - name (string): Optional parameter to filter items to switches with names that contain the search term or are an exact match.
        - networkIds (array): Optional parameter to filter items to switches in one of the provided networks.
        - portProfileIds (array): Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles.
        - serial (string): Optional parameter to filter items to switches with serial number that contains the search term or are an exact match.
        - serials (array): Optional parameter to filter items to switches that have one of the provided serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "clients", "overview", "byDevice"],
            "operation": "getOrganizationSwitchPortsClientsOverviewByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/clients/overview/byDevice"

        query_params = [
            "t0",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "configurationUpdatedAfter",
            "mac",
            "macs",
            "name",
            "networkIds",
            "portProfileIds",
            "serial",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "macs",
            "networkIds",
            "portProfileIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsClientsOverviewByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsMirrorsBySwitch(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **list the port mirror configurations in an organization by switch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-mirrors-by-switch

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "mirrors", "bySwitch"],
            "operation": "getOrganizationSwitchPortsMirrorsBySwitch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/mirrors/bySwitch"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsMirrorsBySwitch: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsOverview(self, organizationId: str, **kwargs):
        """
        **Returns the counts of all active ports for the requested timespan, grouped by speed**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-overview

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 12 hours and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "overview"],
            "operation": "getOrganizationSwitchPortsOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSwitchPortsOverview: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchPortsProfiles(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the port profiles in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Return the port profiles for the specified network(s)
        - formattedStaticAssignments (boolean): Returns the list of static switchports that are assigned to the switchport profile
        - searchQuery (string): Optional parameter to filter the result set by the search query
        - radiusProfileEnabled (boolean): Optional parameter. If true, only return port profiles with a radius profile enabled
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "getOrganizationSwitchPortsProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles"

        query_params = [
            "networkIds",
            "formattedStaticAssignments",
            "searchQuery",
            "radiusProfileEnabled",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSwitchPortsProfiles: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "createOrganizationSwitchPortsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSwitchPortsProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def batchOrganizationSwitchPortsProfilesAssignmentsAssign(self, organizationId: str, items: list, **kwargs):
        """
        **Batch assign or unassign port profiles to switch ports**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-switch-ports-profiles-assignments-assign

        - organizationId (string): Organization ID
        - items (array): Array of assignment operations (max 100)
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "assignments"],
            "operation": "batchOrganizationSwitchPortsProfilesAssignmentsAssign",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/assignments/batchAssign"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"batchOrganizationSwitchPortsProfilesAssignmentsAssign: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchPortsProfilesAssignmentsByPort(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the port profile assignments in an organization, grouped by port**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-assignments-by-port

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - profileIds (array): Filter by specific profile IDs
        - serials (array): Filter by switch serials
        - networkIds (array): Filter by network IDs
        - templateIds (array): Filter by template (node_profile) IDs
        - types (array): Filter by port type: switch, template
        - assignmentTypes (array): Filter by assignment type: direct, template, exception
        - isActive (boolean): Filter by assignment status. true: only ports with active assignments, showing only active assignments per port. false: only ports with inactive assignments, showing only inactive assignments per port. Omit: all ports with all assignment layers.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "assignments", "byPort"],
            "operation": "getOrganizationSwitchPortsProfilesAssignmentsByPort",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/assignments/byPort"

        query_params = [
            "profileIds",
            "serials",
            "networkIds",
            "templateIds",
            "types",
            "assignmentTypes",
            "isActive",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "profileIds",
            "serials",
            "networkIds",
            "templateIds",
            "types",
            "assignmentTypes",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsProfilesAssignmentsByPort: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsProfilesAssignmentsBySwitch(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the port profile assignments in an organization, grouped by switch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-assignments-by-switch

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - profileIds (array): Filter by specific profile IDs
        - serials (array): Filter by switch serials
        - networkIds (array): Filter by network IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "assignments", "bySwitch"],
            "operation": "getOrganizationSwitchPortsProfilesAssignmentsBySwitch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/assignments/bySwitch"

        query_params = [
            "profileIds",
            "serials",
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "profileIds",
            "serials",
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsProfilesAssignmentsBySwitch: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsProfilesAutomations(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **list the automation port profiles in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-automations

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - ids (array): Optional parameter to filter the result set by the included set of automation IDs
        - networkIds (array): Optional parameter to filter the result set by the associated networks.
        - isOrganizationWide (string): Optional parameter to filter the result set by automations org-wide flag.
        - searchQuery (string): Optional parameter to filter the result set by the search query
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "automations"],
            "operation": "getOrganizationSwitchPortsProfilesAutomations",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations"

        query_params = [
            "ids",
            "networkIds",
            "isOrganizationWide",
            "searchQuery",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "ids",
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsProfilesAutomations: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "automations"],
            "operation": "createOrganizationSwitchPortsProfilesAutomation",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations"

        body_params = [
            "name",
            "description",
            "fallbackProfile",
            "rules",
            "assignedSwitchPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchPortsProfilesAutomation: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "automations"],
            "operation": "updateOrganizationSwitchPortsProfilesAutomation",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations/{id}"

        body_params = [
            "name",
            "description",
            "fallbackProfile",
            "rules",
            "assignedSwitchPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSwitchPortsProfilesAutomation: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSwitchPortsProfilesAutomation(self, organizationId: str, id: str):
        """
        **Delete an automation port profile from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profiles-automation

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "automations"],
            "operation": "deleteOrganizationSwitchPortsProfilesAutomation",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/automations/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchPortsProfilesNetworksAssignments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Fetch all Network - Smart Port Profile associations for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-networks-assignments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): Number of records per page
        - page (integer): Page number
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "networks", "assignments"],
            "operation": "getOrganizationSwitchPortsProfilesNetworksAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments"

        query_params = [
            "perPage",
            "page",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsProfilesNetworksAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "networks", "assignments"],
            "operation": "createOrganizationSwitchPortsProfilesNetworksAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments"

        body_params = [
            "type",
            "profile",
            "network",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchPortsProfilesNetworksAssignment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def batchOrganizationSwitchPortsProfilesNetworksAssignmentsCreate(self, organizationId: str, items: list, **kwargs):
        """
        **Batch Create Network and Smart Ports Profile associations for a specific profile**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-switch-ports-profiles-networks-assignments-create

        - organizationId (string): Organization ID
        - items (array): Array of network and profile associations
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "networks", "assignments"],
            "operation": "batchOrganizationSwitchPortsProfilesNetworksAssignmentsCreate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments/batchCreate"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"batchOrganizationSwitchPortsProfilesNetworksAssignmentsCreate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationSwitchPortsProfilesNetworksAssignmentsDelete(self, organizationId: str, items: list, **kwargs):
        """
        **Bulk delete Network and Smart Port Profile associations**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-switch-ports-profiles-networks-assignments-delete

        - organizationId (string): Organization ID
        - items (array): Array of assignments to delete
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "networks", "assignments"],
            "operation": "bulkOrganizationSwitchPortsProfilesNetworksAssignmentsDelete",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments/bulkDelete"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationSwitchPortsProfilesNetworksAssignmentsDelete: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationSwitchPortsProfilesNetworksAssignment(self, organizationId: str, assignmentId: str):
        """
        **Delete Network and Smart Port profile association for a specific profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profiles-networks-assignment

        - organizationId (string): Organization ID
        - assignmentId (string): Assignment ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "networks", "assignments"],
            "operation": "deleteOrganizationSwitchPortsProfilesNetworksAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        assignmentId = urllib.parse.quote(str(assignmentId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/networks/assignments/{assignmentId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchPortsProfilesOverviewByProfile(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the port profiles in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-overview-by-profile

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Return the port profiles for the specified network(s)
        - formattedStaticAssignments (boolean): Returns the list of static switchports that are assgined to the switchport profile
        - searchQuery (string): Optional parameter to filter the result set by the search query
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "overview", "byProfile"],
            "operation": "getOrganizationSwitchPortsProfilesOverviewByProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/overview/byProfile"

        query_params = [
            "networkIds",
            "formattedStaticAssignments",
            "searchQuery",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsProfilesOverviewByProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsProfilesRadiusAssignments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the port profile RADIUS assignments**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-radius-assignments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): If present, the networks to limit the assignments to
        - portProfileIds (array): If present, the port profiles to limit the assignments to
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "radius", "assignments"],
            "operation": "getOrganizationSwitchPortsProfilesRadiusAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments"

        query_params = [
            "networkIds",
            "portProfileIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "portProfileIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsProfilesRadiusAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "radius", "assignments"],
            "operation": "createOrganizationSwitchPortsProfilesRadiusAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments"

        body_params = [
            "network",
            "portProfile",
            "radius",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchPortsProfilesRadiusAssignment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchPortsProfilesRadiusAssignment(self, organizationId: str, id: str):
        """
        **Return a port profile RADIUS assignment**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profiles-radius-assignment

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "radius", "assignments"],
            "operation": "getOrganizationSwitchPortsProfilesRadiusAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments/{id}"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "radius", "assignments"],
            "operation": "updateOrganizationSwitchPortsProfilesRadiusAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments/{id}"

        body_params = [
            "network",
            "portProfile",
            "radius",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSwitchPortsProfilesRadiusAssignment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSwitchPortsProfilesRadiusAssignment(self, organizationId: str, id: str):
        """
        **Deletes a port profile RADIUS assignment**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profiles-radius-assignment

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles", "radius", "assignments"],
            "operation": "deleteOrganizationSwitchPortsProfilesRadiusAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/radius/assignments/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchPortsProfile(self, organizationId: str, id: str):
        """
        **Get detailed information about a port profile**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-profile

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "getOrganizationSwitchPortsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/{id}"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "updateOrganizationSwitchPortsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationSwitchPortsProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSwitchPortsProfile(self, organizationId: str, id: str):
        """
        **Delete a port profile from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-ports-profile

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["switch", "configure", "ports", "profiles"],
            "operation": "deleteOrganizationSwitchPortsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/profiles/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchPortsStatusesBySwitch(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the switchports in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-statuses-by-switch

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Optional parameter to filter items to switches where the configuration has been updated after the given timestamp.
        - mac (string): Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match.
        - macs (array): Optional parameter to filter items to switches that have one of the provided MAC addresses.
        - name (string): Optional parameter to filter items to switches with names that contain the search term or are an exact match.
        - networkIds (array): Optional parameter to filter items to switches in one of the provided networks.
        - portProfileIds (array): Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles.
        - serial (string): Optional parameter to filter items to switches with serial number that contains the search term or are an exact match.
        - serials (array): Optional parameter to filter items to switches that have one of the provided serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "statuses", "bySwitch"],
            "operation": "getOrganizationSwitchPortsStatusesBySwitch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/statuses/bySwitch"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "configurationUpdatedAfter",
            "mac",
            "macs",
            "name",
            "networkIds",
            "portProfileIds",
            "serial",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "macs",
            "networkIds",
            "portProfileIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsStatusesBySwitch: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsStatusesPacketsByDeviceByPort(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Switch port packets by device and port.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-statuses-packets-by-device-by-port

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 1200, 14400, 86400. The default is 14400. Interval is calculated if time params are provided.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "statuses", "packets", "byDevice", "byPort"],
            "operation": "getOrganizationSwitchPortsStatusesPacketsByDeviceByPort",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/statuses/packets/byDevice/byPort"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsStatusesPacketsByDeviceByPort: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSwitchPortsTopologyDiscoveryByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List most recently seen LLDP/CDP discovery and topology information per switch port in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-topology-discovery-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Optional parameter to filter items to switches where the configuration has been updated after the given timestamp.
        - mac (string): Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match.
        - macs (array): Optional parameter to filter items to switches that have one of the provided MAC addresses.
        - name (string): Optional parameter to filter items to switches with names that contain the search term or are an exact match.
        - networkIds (array): Optional parameter to filter items to switches in one of the provided networks.
        - portProfileIds (array): Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles.
        - serial (string): Optional parameter to filter items to switches with serial number that contains the search term or are an exact match.
        - serials (array): Optional parameter to filter items to switches that have one of the provided serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "topology", "discovery", "byDevice"],
            "operation": "getOrganizationSwitchPortsTopologyDiscoveryByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/topology/discovery/byDevice"

        query_params = [
            "t0",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "configurationUpdatedAfter",
            "mac",
            "macs",
            "name",
            "networkIds",
            "portProfileIds",
            "serial",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "macs",
            "networkIds",
            "portProfileIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsTopologyDiscoveryByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsTransceiversReadingsHistoryBySwitch(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Return time-series digital optical monitoring (DOM) readings for ports on each DOM-enabled switch in an organization, in addition to thresholds for each relevant Small Form Factor Pluggable (SFP) module.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-transceivers-readings-history-by-switch

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 1 day. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 1200, 14400, 86400. The default is 1200. Interval is calculated if time params are provided.
        - networkIds (array): Networks for which information should be gathered.
        - serials (array): Optional parameter to filter usage by switch.
        - portIds (array): Optional parameter to filter usage by port ID.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "transceivers", "readings", "history", "bySwitch"],
            "operation": "getOrganizationSwitchPortsTransceiversReadingsHistoryBySwitch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/transceivers/readings/history/bySwitch"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
            "networkIds",
            "serials",
            "portIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "portIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsTransceiversReadingsHistoryBySwitch: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchPortsUsageHistoryByDeviceByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the historical usage and traffic data of switchports in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-usage-history-by-device-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 1200, 14400, 86400. The default is 1200. Interval is calculated if time params are provided.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Optional parameter to filter items to switches where the configuration has been updated after the given timestamp.
        - mac (string): Optional parameter to filter items to switches with MAC addresses that contain the search term or are an exact match.
        - macs (array): Optional parameter to filter items to switches that have one of the provided MAC addresses.
        - name (string): Optional parameter to filter items to switches with names that contain the search term or are an exact match.
        - networkIds (array): Optional parameter to filter items to switches in one of the provided networks.
        - portProfileIds (array): Optional parameter to filter items to switches that contain switchports belonging to one of the specified port profiles.
        - serial (string): Optional parameter to filter items to switches with serial number that contains the search term or are an exact match.
        - serials (array): Optional parameter to filter items to switches that have one of the provided serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "ports", "usage", "history", "byDevice", "byInterval"],
            "operation": "getOrganizationSwitchPortsUsageHistoryByDeviceByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/ports/usage/history/byDevice/byInterval"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "interval",
            "perPage",
            "startingAfter",
            "endingBefore",
            "configurationUpdatedAfter",
            "mac",
            "macs",
            "name",
            "networkIds",
            "portProfileIds",
            "serial",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "macs",
            "networkIds",
            "portProfileIds",
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchPortsUsageHistoryByDeviceByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpAutonomousSystems(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the autonomous systems configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-autonomous-systems

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - numbers (array): Optional parameter to filter autonomous systems by number. This filter uses multiple exact matches.
        - autonomousSystemIds (array): Optional parameter to filter autonomous systems by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "autonomousSystems"],
            "operation": "getOrganizationSwitchRoutingBgpAutonomousSystems",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "numbers",
            "autonomousSystemIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "numbers",
            "autonomousSystemIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpAutonomousSystems: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSwitchRoutingBgpAutonomousSystem(self, organizationId: str, number: int, **kwargs):
        """
        **Create an autonomous system**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-autonomous-system

        - organizationId (string): Organization ID
        - number (integer): The autonomous system number (CLI: 'router bgp <number>')
        - description (string): A description for the autonomous system
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "autonomousSystems"],
            "operation": "createOrganizationSwitchRoutingBgpAutonomousSystem",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems"

        body_params = [
            "number",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpAutonomousSystem: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchRoutingBgpAutonomousSystemsOverviewByAutonomousSystem(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the overview of the autonomous systems configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-autonomous-systems-overview-by-autonomous-system

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - numbers (array): Optional parameter to filter autonomous systems by number. This filter uses multiple exact matches.
        - autonomousSystemIds (array): Optional parameter to filter autonomous systems by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "autonomousSystems", "overview", "byAutonomousSystem"],
            "operation": "getOrganizationSwitchRoutingBgpAutonomousSystemsOverviewByAutonomousSystem",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems/overview/byAutonomousSystem"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "numbers",
            "autonomousSystemIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "numbers",
            "autonomousSystemIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpAutonomousSystemsOverviewByAutonomousSystem: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateOrganizationSwitchRoutingBgpAutonomousSystem(self, organizationId: str, autonomousSystemId: str, **kwargs):
        """
        **Update an autonomous system**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-switch-routing-bgp-autonomous-system

        - organizationId (string): Organization ID
        - autonomousSystemId (string): Autonomous system ID
        - number (integer): The autonomous system number (CLI: 'router bgp <number>')
        - description (string): A description for the autonomous system
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "autonomousSystems"],
            "operation": "updateOrganizationSwitchRoutingBgpAutonomousSystem",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        autonomousSystemId = urllib.parse.quote(str(autonomousSystemId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems/{autonomousSystemId}"

        body_params = [
            "number",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSwitchRoutingBgpAutonomousSystem: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSwitchRoutingBgpAutonomousSystem(self, organizationId: str, autonomousSystemId: str):
        """
        **Delete an autonomous system from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-autonomous-system

        - organizationId (string): Organization ID
        - autonomousSystemId (string): Autonomous system ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "autonomousSystems"],
            "operation": "deleteOrganizationSwitchRoutingBgpAutonomousSystem",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        autonomousSystemId = urllib.parse.quote(str(autonomousSystemId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/autonomousSystems/{autonomousSystemId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchRoutingBgpFiltersFilterLists(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the filter lists configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-filters-filter-lists

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter 'filter lists' by network ID. This filter uses multiple exact matches.
        - listIds (array): Optional parameter to filter 'filter lists' by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "filterLists"],
            "operation": "getOrganizationSwitchRoutingBgpFiltersFilterLists",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "listIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "listIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpFiltersFilterLists: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSwitchRoutingBgpFiltersFilterListsDeploy(
        self, organizationId: str, filterList: dict, network: dict, rules: list, **kwargs
    ):
        """
        **Create or update a filter list, in addition to its associated rules**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-filters-filter-lists-deploy

        - organizationId (string): Organization ID
        - filterList (object): Information regarding the filter list
        - network (object): Information regarding the network the filter list belongs to
        - rules (array): Information regarding the filter list rules
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "filterLists", "deploy"],
            "operation": "createOrganizationSwitchRoutingBgpFiltersFilterListsDeploy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists/deploy"

        body_params = [
            "filterList",
            "network",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpFiltersFilterListsDeploy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchRoutingBgpFiltersFilterListsOverviewByFilterList(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the overview of the filter lists configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-filters-filter-lists-overview-by-filter-list

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter 'filter list' overviews by network ID. This filter uses multiple exact matches.
        - listIds (array): Optional parameter to filter 'filter list' overviews by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "routing", "bgp", "filters", "filterLists", "overview", "byFilterList"],
            "operation": "getOrganizationSwitchRoutingBgpFiltersFilterListsOverviewByFilterList",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists/overview/byFilterList"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "listIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "listIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpFiltersFilterListsOverviewByFilterList: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpFiltersFilterListsRules(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the filter list rules configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-filters-filter-lists-rules

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter 'filter list' rules by network ID. This filter uses multiple exact matches.
        - ruleIds (array): Optional parameter to filter 'filter list' rules by ID. This filter uses multiple exact matches.
        - filterListIds (array): Optional parameter to filter 'filter lists' by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "filterLists", "rules"],
            "operation": "getOrganizationSwitchRoutingBgpFiltersFilterListsRules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists/rules"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "ruleIds",
            "filterListIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ruleIds",
            "filterListIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpFiltersFilterListsRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationSwitchRoutingBgpFiltersFilterList(self, organizationId: str, listId: str):
        """
        **Delete a filter list**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-filters-filter-list

        - organizationId (string): Organization ID
        - listId (string): List ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "filterLists"],
            "operation": "deleteOrganizationSwitchRoutingBgpFiltersFilterList",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        listId = urllib.parse.quote(str(listId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/filterLists/{listId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchRoutingBgpFiltersPrefixLists(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the prefix lists configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-filters-prefix-lists

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter prefix lists by network ID. This filter uses multiple exact matches.
        - listIds (array): Optional parameter to filter prefix lists by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "prefixLists"],
            "operation": "getOrganizationSwitchRoutingBgpFiltersPrefixLists",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "listIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "listIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpFiltersPrefixLists: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSwitchRoutingBgpFiltersPrefixListsDeploy(
        self, organizationId: str, network: dict, prefixList: dict, rules: list, **kwargs
    ):
        """
        **Create or update a prefix list, in addition to its associated rules**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-filters-prefix-lists-deploy

        - organizationId (string): Organization ID
        - network (object): Information regarding the network the prefix list belongs to
        - prefixList (object): Information regarding the prefix list
        - rules (array): Information regarding the prefix list rules
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "prefixLists", "deploy"],
            "operation": "createOrganizationSwitchRoutingBgpFiltersPrefixListsDeploy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists/deploy"

        body_params = [
            "network",
            "prefixList",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpFiltersPrefixListsDeploy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchRoutingBgpFiltersPrefixListsOverviewByPrefixList(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the overview of the prefix lists configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-filters-prefix-lists-overview-by-prefix-list

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter prefix list overviews by network ID. This filter uses multiple exact matches.
        - listIds (array): Optional parameter to filter prefix list overviews by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "routing", "bgp", "filters", "prefixLists", "overview", "byPrefixList"],
            "operation": "getOrganizationSwitchRoutingBgpFiltersPrefixListsOverviewByPrefixList",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists/overview/byPrefixList"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "listIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "listIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpFiltersPrefixListsOverviewByPrefixList: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpFiltersPrefixListsRules(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the prefix list rules configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-filters-prefix-lists-rules

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter prefix list rules by network ID. This filter uses multiple exact matches.
        - prefixListIds (array): Optional parameter to filter prefix list rules by prefix list ID. This filter uses multiple exact matches.
        - ruleIds (array): Optional parameter to filter prefix list rules by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "prefixLists", "rules"],
            "operation": "getOrganizationSwitchRoutingBgpFiltersPrefixListsRules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists/rules"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "prefixListIds",
            "ruleIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "prefixListIds",
            "ruleIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpFiltersPrefixListsRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationSwitchRoutingBgpFiltersPrefixList(self, organizationId: str, listId: str):
        """
        **Delete a prefix list**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-filters-prefix-list

        - organizationId (string): Organization ID
        - listId (string): List ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "filters", "prefixLists"],
            "operation": "deleteOrganizationSwitchRoutingBgpFiltersPrefixList",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        listId = urllib.parse.quote(str(listId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/filters/prefixLists/{listId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchRoutingBgpPeersGroups(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the BGP peer groups configured in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter peer groups by network ID. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter peer groups by router ID. This filter uses multiple exact matches.
        - profileIds (array): Optional parameter to filter peer groups by profile ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter peer groups by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "groups"],
            "operation": "getOrganizationSwitchRoutingBgpPeersGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/groups"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "routerIds",
            "profileIds",
            "peerGroupIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "routerIds",
            "profileIds",
            "peerGroupIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersGroups: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpPeersGroupsAddressFamiliesDeployments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List all BGP deployment information for multiple peer groups or address families configured in the given organization, including profile information, peer group address family information, neighbors, and listen ranges**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-groups-address-families-deployments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter peer group address family deployments by network ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter peer group address family deployments by peer group
        - addressFamilyIds (array): Optional parameter to filter peer group address family deployments by address family
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "groups", "addressFamilies", "deployments"],
            "operation": "getOrganizationSwitchRoutingBgpPeersGroupsAddressFamiliesDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/groups/addressFamilies/deployments"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "peerGroupIds",
            "addressFamilyIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "peerGroupIds",
            "addressFamilyIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersGroupsAddressFamiliesDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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
        **Create or update a peer group, in addition to an associated peer group profile, peer group address family binding, peer group address family binding profile and routing policies associated with the peer group**
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

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "groups", "deploy"],
            "operation": "createOrganizationSwitchRoutingBgpPeersGroupsDeploy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpPeersGroupsDeploy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchRoutingBgpPeersGroupsDeployments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List all BGP deployment information for peer groups configured in the given organization, including peer group address family information, as well as routing policies**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-groups-deployments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter peer group deployments by network ID. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter peer group deployments by router ID. This filter uses multiple exact matches.
        - profileIds (array): Optional parameter to filter peer group deployments by profile ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter peer group deployments by peer group ID. This filter uses multiple exact matches.
        - afi (string): Optional parameter to filter deployments on each peer group by address family identifier (AFI).
        - safi (string): Optional parameter to filter deployments on each peer group by subsequent address family identifier (SAFI).
        """

        kwargs.update(locals())

        if "afi" in kwargs:
            options = ["ipv4"]
            assert kwargs["afi"] in options, f'''"afi" cannot be "{kwargs["afi"]}", & must be set to one of: {options}'''
        if "safi" in kwargs:
            options = ["unicast"]
            assert kwargs["safi"] in options, f'''"safi" cannot be "{kwargs["safi"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "groups", "deployments"],
            "operation": "getOrganizationSwitchRoutingBgpPeersGroupsDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/groups/deployments"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "routerIds",
            "profileIds",
            "peerGroupIds",
            "afi",
            "safi",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "routerIds",
            "profileIds",
            "peerGroupIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersGroupsDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpPeersGroupsOverviewByPeerGroup(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the overview of the BGP peer groups configured in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-groups-overview-by-peer-group

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter peer group overviews by network ID. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter peer group overviews by router ID. This filter uses multiple exact matches.
        - profileIds (array): Optional parameter to filter peer group overviews by profile ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter peer group overviews by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "routing", "bgp", "peers", "groups", "overview", "byPeerGroup"],
            "operation": "getOrganizationSwitchRoutingBgpPeersGroupsOverviewByPeerGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/groups/overview/byPeerGroup"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "routerIds",
            "profileIds",
            "peerGroupIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "routerIds",
            "profileIds",
            "peerGroupIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersGroupsOverviewByPeerGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpPeersListenRanges(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the listen ranges configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-listen-ranges

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter listen ranges by network ID. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter listen ranges by router ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter listen ranges by peer group ID. This filter uses multiple exact matches.
        - listenRangeIds (array): Optional parameter to filter listen ranges by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "listenRanges"],
            "operation": "getOrganizationSwitchRoutingBgpPeersListenRanges",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/listenRanges"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "routerIds",
            "peerGroupIds",
            "listenRangeIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "routerIds",
            "peerGroupIds",
            "listenRangeIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersListenRanges: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpPeersNeighbors(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the neighbors configured for BGP in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-neighbors

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter neighbors by network ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter neighbors by peer group ID. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter neighbors by router ID. This filter uses multiple exact matches.
        - neighborIds (array): Optional parameter to filter neighbors by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "neighbors"],
            "operation": "getOrganizationSwitchRoutingBgpPeersNeighbors",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/neighbors"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "peerGroupIds",
            "routerIds",
            "neighborIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "peerGroupIds",
            "routerIds",
            "neighborIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersNeighbors: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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
        **Create or update a neighor, in addition to an associated neighbor address family binding and routing policies associated with the neighbor**
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

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "neighbors", "deploy"],
            "operation": "createOrganizationSwitchRoutingBgpPeersNeighborsDeploy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpPeersNeighborsDeploy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchRoutingBgpPeersNeighborsDeployments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List all BGP deployment information for neighbors configured in the given organization, including address family information, as well as routing policies**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-peers-neighbors-deployments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter neighbor deployments by network ID. This filter uses multiple exact matches.
        - peerGroupIds (array): Optional parameter to filter neighbor deployments by peer group ID. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter neighbor deployments by router ID. This filter uses multiple exact matches.
        - neighborIds (array): Optional parameter to filter neighbor deployments by neighbor ID. This filter uses multiple exact matches.
        - afi (string): Optional parameter to filter deployments on each neighbor by address family identifier (AFI).
        - safi (string): Optional parameter to filter deployments on each neighbor by subsequent address family identifier (SAFI).
        """

        kwargs.update(locals())

        if "afi" in kwargs:
            options = ["ipv4"]
            assert kwargs["afi"] in options, f'''"afi" cannot be "{kwargs["afi"]}", & must be set to one of: {options}'''
        if "safi" in kwargs:
            options = ["unicast"]
            assert kwargs["safi"] in options, f'''"safi" cannot be "{kwargs["safi"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "peers", "neighbors", "deployments"],
            "operation": "getOrganizationSwitchRoutingBgpPeersNeighborsDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/peers/neighbors/deployments"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "peerGroupIds",
            "routerIds",
            "neighborIds",
            "afi",
            "safi",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "peerGroupIds",
            "routerIds",
            "neighborIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpPeersNeighborsDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpRouters(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the routers configured in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-routers

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter routers by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter routers by serial. This filter uses multiple exact matches.
        - switchNames (array): Optional parameter to filter routers by switch name. The filter uses multiple exact matches.
        - asNumbers (array): Optional parameter to filter routers by autonomous system number. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter routers by ID. This filter uses multiple exact matches.
        - switchStackIds (array): Optional parameter to filter routers by switch stack id. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "routers"],
            "operation": "getOrganizationSwitchRoutingBgpRouters",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "switchNames",
            "asNumbers",
            "routerIds",
            "switchStackIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "switchNames",
            "asNumbers",
            "routerIds",
            "switchStackIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpRouters: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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
        **Create a BGP router, in addition to an associated address family, address family prefixes, and address family profile**
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

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "routers", "deploy"],
            "operation": "createOrganizationSwitchRoutingBgpRoutersDeploy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
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

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpRoutersDeploy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSwitchRoutingBgpRoutersDeployments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List all BGP deployment information for routers configured in a given organization, including all address families**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-routers-deployments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter router deployments by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter router deployments by serial. This filter uses multiple exact matches.
        - switchNames (array): Optional parameter to filter router deployments by switch name. The filter uses multiple exact matches.
        - asNumbers (array): Optional parameter to filter router deployments by autonomous system number. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter router deployments by router ID. This filter uses multiple exact matches.
        - switchStackIds (array): Optional parameter to filter router deployments by switch stack id. This filter uses multiple exact matches.
        - afi (string): Optional parameter to filter deployments on each router by address family identifier (AFI).
        - safi (string): Optional parameter to filter deployments on each router by subsequent address family identifier (SAFI).
        """

        kwargs.update(locals())

        if "afi" in kwargs:
            options = ["ipv4"]
            assert kwargs["afi"] in options, f'''"afi" cannot be "{kwargs["afi"]}", & must be set to one of: {options}'''
        if "safi" in kwargs:
            options = ["unicast"]
            assert kwargs["safi"] in options, f'''"safi" cannot be "{kwargs["safi"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "routers", "deployments"],
            "operation": "getOrganizationSwitchRoutingBgpRoutersDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/deployments"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "switchNames",
            "asNumbers",
            "routerIds",
            "switchStackIds",
            "afi",
            "safi",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "switchNames",
            "asNumbers",
            "routerIds",
            "switchStackIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpRoutersDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchRoutingBgpRoutersOverviewByRouter(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the overview of the routers configured in the given organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-bgp-routers-overview-by-router

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter router overviews by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter router overviews by serial. This filter uses multiple exact matches.
        - switchNames (array): Optional parameter to filter router overviews by switch name. This filter uses multiple exact matches.
        - asNumbers (array): Optional parameter to filter router overviews by autonomous system number. This filter uses multiple exact matches.
        - routerIds (array): Optional parameter to filter router overviews by ID. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "routing", "bgp", "routers", "overview", "byRouter"],
            "operation": "getOrganizationSwitchRoutingBgpRoutersOverviewByRouter",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/overview/byRouter"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "switchNames",
            "asNumbers",
            "routerIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "switchNames",
            "asNumbers",
            "routerIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingBgpRoutersOverviewByRouter: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSwitchRoutingBgpRoutersPeersDeploy(
        self, organizationId: str, addressFamily: dict, peerGroups: list, router: dict, **kwargs
    ):
        """
        **Create and update listen ranges, update peers' enabled flag, and delete peer groups for a BGP router**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-switch-routing-bgp-routers-peers-deploy

        - organizationId (string): Organization ID
        - addressFamily (object): Information regarding the address family
        - peerGroups (array): Information regarding the peer group peers for a router's peer group
        - router (object): Information regarding the BPG router
        """

        kwargs = locals()

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "routers", "peers", "deploy"],
            "operation": "createOrganizationSwitchRoutingBgpRoutersPeersDeploy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/peers/deploy"

        body_params = [
            "addressFamily",
            "peerGroups",
            "router",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSwitchRoutingBgpRoutersPeersDeploy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationSwitchRoutingBgpRouter(self, organizationId: str, routerId: str):
        """
        **Delete a router from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-switch-routing-bgp-router

        - organizationId (string): Organization ID
        - routerId (string): Router ID
        """

        metadata = {
            "tags": ["switch", "configure", "routing", "bgp", "routers"],
            "operation": "deleteOrganizationSwitchRoutingBgpRouter",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        routerId = urllib.parse.quote(str(routerId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/bgp/routers/{routerId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSwitchRoutingStaticRoutes(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List layer 3 static routes for switches within an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-routing-static-routes

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "monitor", "routing", "staticRoutes"],
            "operation": "getOrganizationSwitchRoutingStaticRoutes",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/routing/staticRoutes"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchRoutingStaticRoutes: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchSpanningTree(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns Spanning Tree configuration settings**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-spanning-tree

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter by network ID.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "spanningTree"],
            "operation": "getOrganizationSwitchSpanningTree",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/spanningTree"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSwitchSpanningTree: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSwitchStacksPortsMirrorsByStack(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the port mirror configurations in an organization by switch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-stacks-ports-mirrors-by-stack

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - ids (array): Return the port mirror configuration for the specified stack(s)
        - networkIds (array): Return the port mirror configurations for the specified network(s)
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["switch", "configure", "stacks", "ports", "mirrors", "byStack"],
            "operation": "getOrganizationSwitchStacksPortsMirrorsByStack",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/switch/stacks/ports/mirrors/byStack"

        query_params = [
            "ids",
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "ids",
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSwitchStacksPortsMirrorsByStack: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
