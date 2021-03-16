class ActionBatchSwitch(object):
	def __init__(self):
		super(ActionBatchSwitch, self).__init__()

	def cycleDeviceSwitchPorts(self, serial: str, ports: list):
		"""
		**Cycle a set of switch ports**
		https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports
		
		- serial (string): (required)
		- ports (array): List of switch ports. Example: [1, 2-5, 1_MA-MOD-8X10G_1, 1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8]
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
			"operation": "create",
			"body": payload
		}
		return action






	def updateDeviceSwitchPort(self, serial: str, portId: str, **kwargs):
		"""
		**Update a switch port**
		https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port
		
		- serial (string): (required)
		- portId (string): (required)
		- name (string): The name of the switch port
		- tags (array): The list of tags of the switch port
		- enabled (boolean): The status of the switch port
		- type (string): The type of the switch port ('trunk' or 'access')
		- vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
		- voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
		- allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
		- poeEnabled (boolean): The PoE status of the switch port
		- isolationEnabled (boolean): The isolation status of the switch port
		- rstpEnabled (boolean): The rapid spanning tree protocol status
		- stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
		- linkNegotiation (string): The link speed for the switch port
		- portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
		- udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
		- accessPolicyType (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'
		- accessPolicyNumber (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'
		- macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'
		- stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
		- stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
		- stormControlEnabled (boolean): The storm control status of the switch port
		- flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
		"""

		kwargs.update(locals())

		if 'type' in kwargs:
			options = ['trunk', 'access']
			assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''
		if 'stpGuard' in kwargs:
			options = ['disabled', 'root guard', 'bpdu guard', 'loop guard']
			assert kwargs['stpGuard'] in options, f'''"stpGuard" cannot be "{kwargs['stpGuard']}", & must be set to one of: {options}'''
		if 'udld' in kwargs:
			options = ['Alert only', 'Enforce']
			assert kwargs['udld'] in options, f'''"udld" cannot be "{kwargs['udld']}", & must be set to one of: {options}'''
		if 'accessPolicyType' in kwargs:
			options = ['Open', 'Custom access policy', 'MAC allow list', 'Sticky MAC allow list']
			assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'ports'],
			'operation': 'updateDeviceSwitchPort'
		}
		resource = f'/devices/{serial}/switch/ports/{portId}'

		body_params = ['name', 'tags', 'enabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'poeEnabled', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macAllowList', 'stickyMacAllowList', 'stickyMacAllowListLimit', 'stormControlEnabled', 'flexibleStackingEnabled', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def createDeviceSwitchRoutingInterface(self, serial: str, name: str, interfaceIp: str, vlanId: int, **kwargs):
		"""
		**Create a layer 3 interface for a switch**
		https://developer.cisco.com/meraki/api-v1/#!create-device-switch-routing-interface
		
		- serial (string): (required)
		- name (string): A friendly name or description for the interface or VLAN.
		- interfaceIp (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
		- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
		- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
		- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
		- defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
		- ospfSettings (object): The OSPF routing settings of the interface.
		"""

		kwargs.update(locals())

		if 'multicastRouting' in kwargs:
			options = ['disabled', 'enabled', 'IGMP snooping querier']
			assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'routing', 'interfaces'],
			'operation': 'createDeviceSwitchRoutingInterface'
		}
		resource = f'/devices/{serial}/switch/routing/interfaces'

		body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', ]
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
		
		- serial (string): (required)
		- interfaceId (string): (required)
		- name (string): A friendly name or description for the interface or VLAN.
		- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
		- interfaceIp (string): The IP address this switch will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
		- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
		- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
		- ospfSettings (object): The OSPF routing settings of the interface.
		"""

		kwargs.update(locals())

		if 'multicastRouting' in kwargs:
			options = ['disabled', 'enabled', 'IGMP snooping querier']
			assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'routing', 'interfaces'],
			'operation': 'updateDeviceSwitchRoutingInterface'
		}
		resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

		body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'ospfSettings', ]
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
		
		- serial (string): (required)
		- interfaceId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'routing', 'interfaces'],
			'operation': 'deleteDeviceSwitchRoutingInterface'
		}
		resource = f'/devices/{serial}/switch/routing/interfaces/{interfaceId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateDeviceSwitchRoutingInterfaceDhcp(self, serial: str, interfaceId: str, **kwargs):
		"""
		**Update a layer 3 interface DHCP configuration for a switch**
		https://developer.cisco.com/meraki/api-v1/#!update-device-switch-routing-interface-dhcp
		
		- serial (string): (required)
		- interfaceId (string): (required)
		- dhcpMode (string): The DHCP mode options for the switch interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
		- dhcpRelayServerIps (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch interface
		- dhcpLeaseTime (string): The DHCP lease time config for the dhcp server running on switch interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
		- dnsNameserversOption (string): The DHCP name server option for the dhcp server running on the switch interface ('googlePublicDns', 'openDns' or 'custom')
		- dnsCustomNameservers (array): The DHCP name server IPs when DHCP name server option is 'custom'
		- bootOptionsEnabled (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch interface
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
			options = ['30 minutes', '1 hour', '4 hours', '12 hours', '1 day', '1 week']
			assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''
		if 'dnsNameserversOption' in kwargs:
			options = ['googlePublicDns', 'openDns', 'custom']
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
		
		- serial (string): (required)
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
		
		- serial (string): (required)
		- staticRouteId (string): (required)
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
		resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

		body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
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
		
		- serial (string): (required)
		- staticRouteId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'routing', 'staticRoutes'],
			'operation': 'deleteDeviceSwitchRoutingStaticRoute'
		}
		resource = f'/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateDeviceSwitchWarmSpare(self, serial: str, enabled: bool, **kwargs):
		"""
		**Update warm spare configuration for a switch**
		https://developer.cisco.com/meraki/api-v1/#!update-device-switch-warm-spare
		
		- serial (string): (required)
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
		**Create an access policy for a switch network**
		https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy
		
		- networkId (string): (required)
		- name (string): Name of the access policy
		- radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
		- radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
		- radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
		- radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
		- hostMode (string): Choose the Host Mode for the access policy.
		- urlRedirectWalledGardenEnabled (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
		- radiusAccountingServers (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
		- radiusGroupAttribute (string): Acceptable values are `""` for None, or `"11"` for Group Policies ACL
		- accessPolicyType (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
		- increaseAccessSpeed (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
		- guestVlanId (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
		- voiceVlanClients (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
		- urlRedirectWalledGardenRanges (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
		"""

		kwargs.update(locals())

		if 'hostMode' in kwargs:
			options = ['Single-Host', 'Multi-Domain', 'Multi-Host', 'Multi-Auth']
			assert kwargs['hostMode'] in options, f'''"hostMode" cannot be "{kwargs['hostMode']}", & must be set to one of: {options}'''
		if 'accessPolicyType' in kwargs:
			options = ['802.1x', 'MAC authentication bypass', 'Hybrid authentication']
			assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'accessPolicies'],
			'operation': 'createNetworkSwitchAccessPolicy'
		}
		resource = f'/networks/{networkId}/switch/accessPolicies'

		body_params = ['name', 'radiusServers', 'radiusTestingEnabled', 'radiusCoaSupportEnabled', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusGroupAttribute', 'hostMode', 'accessPolicyType', 'increaseAccessSpeed', 'guestVlanId', 'voiceVlanClients', 'urlRedirectWalledGardenEnabled', 'urlRedirectWalledGardenRanges', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "create",
			"body": payload
		}
		return action






	def updateNetworkSwitchAccessPolicy(self, networkId: str, accessPolicyNumber: str, **kwargs):
		"""
		**Update an access policy for a switch network**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy
		
		- networkId (string): (required)
		- accessPolicyNumber (string): (required)
		- name (string): Name of the access policy
		- radiusServers (array): List of RADIUS servers to require connecting devices to authenticate against before granting network access
		- radiusTestingEnabled (boolean): If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers
		- radiusCoaSupportEnabled (boolean): Change of authentication for RADIUS re-authentication and disconnection
		- radiusAccountingEnabled (boolean): Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients
		- radiusAccountingServers (array): List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access
		- radiusGroupAttribute (string): Can be either `""`, which means `None` on Dashboard, or `"11"`, which means `Filter-Id` on Dashboard and will use Group Policy ACLs when supported (firmware 14+)
		- hostMode (string): Choose the Host Mode for the access policy.
		- accessPolicyType (string): Access Type of the policy. Automatically 'Hybrid authentication' when hostMode is 'Multi-Domain'.
		- increaseAccessSpeed (boolean): Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is 'Hybrid Authentication.
		- guestVlanId (integer): ID for the guest VLAN allow unauthorized devices access to limited network resources
		- voiceVlanClients (boolean): CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is 'Multi-Domain'.
		- urlRedirectWalledGardenEnabled (boolean): Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
		- urlRedirectWalledGardenRanges (array): IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication
		"""

		kwargs.update(locals())

		if 'hostMode' in kwargs:
			options = ['Single-Host', 'Multi-Domain', 'Multi-Host', 'Multi-Auth']
			assert kwargs['hostMode'] in options, f'''"hostMode" cannot be "{kwargs['hostMode']}", & must be set to one of: {options}'''
		if 'accessPolicyType' in kwargs:
			options = ['802.1x', 'MAC authentication bypass', 'Hybrid authentication']
			assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'accessPolicies'],
			'operation': 'updateNetworkSwitchAccessPolicy'
		}
		resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

		body_params = ['name', 'radiusServers', 'radiusTestingEnabled', 'radiusCoaSupportEnabled', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusGroupAttribute', 'hostMode', 'accessPolicyType', 'increaseAccessSpeed', 'guestVlanId', 'voiceVlanClients', 'urlRedirectWalledGardenEnabled', 'urlRedirectWalledGardenRanges', ]
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
		
		- networkId (string): (required)
		- accessPolicyNumber (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'accessPolicies'],
			'operation': 'deleteNetworkSwitchAccessPolicy'
		}
		resource = f'/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateNetworkSwitchAlternateManagementInterface(self, networkId: str, **kwargs):
		"""
		**Update the switch alternate management interface for the network**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-alternate-management-interface
		
		- networkId (string): (required)
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
		**Update the DHCP server policy**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy
		
		- networkId (string): (required)
		- defaultPolicy (string): 'allow' or 'block' new DHCP servers. Default value is 'allow'.
		- allowedServers (array): List the MAC addresses of DHCP servers to permit on the network. Applicable only if defaultPolicy is set to block. An empty array will clear the entries.
		- blockedServers (array): List the MAC addresses of DHCP servers to block on the network. Applicable only if defaultPolicy is set to allow. An empty array will clear the entries.
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

		body_params = ['defaultPolicy', 'allowedServers', 'blockedServers', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def updateNetworkSwitchDscpToCosMappings(self, networkId: str, mappings: list):
		"""
		**Update the DSCP to CoS mappings**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings
		
		- networkId (string): (required)
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
		
		- networkId (string): (required)
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
		
		- networkId (string): (required)
		- linkAggregationId (string): (required)
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
		
		- networkId (string): (required)
		- linkAggregationId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'linkAggregations'],
			'operation': 'deleteNetworkSwitchLinkAggregation'
		}
		resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateNetworkSwitchMtu(self, networkId: str, **kwargs):
		"""
		**Update the MTU configuration**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu
		
		- networkId (string): (required)
		- defaultMtuSize (integer): MTU size for the entire network. Default value is 9578.
		- overrides (array): Override MTU size for individual switches or switch profiles. An empty array will clear overrides.
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
		
		- networkId (string): (required)
		- portScheduleId (string): (required)
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
		
		- networkId (string): (required)
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
		
		- networkId (string): (required)
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
			"operation": "update",
			"body": payload
		}
		return action






	def deleteNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
		"""
		**Delete a quality of service rule**
		https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule
		
		- networkId (string): (required)
		- qosRuleId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'qosRules'],
			'operation': 'deleteNetworkSwitchQosRule'
		}
		resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateNetworkSwitchQosRule(self, networkId: str, qosRuleId: str, **kwargs):
		"""
		**Update a quality of service rule**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule
		
		- networkId (string): (required)
		- qosRuleId (string): (required)
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
		
		- networkId (string): (required)
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
		
		- networkId (string): (required)
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
		
		- networkId (string): (required)
		- rendezvousPointId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'routing', 'multicast', 'rendezvousPoints'],
			'operation': 'deleteNetworkSwitchRoutingMulticastRendezvousPoint'
		}
		resource = f'/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateNetworkSwitchRoutingMulticastRendezvousPoint(self, networkId: str, rendezvousPointId: str, interfaceIp: str, multicastGroup: str):
		"""
		**Update a multicast rendezvous point**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast-rendezvous-point
		
		- networkId (string): (required)
		- rendezvousPointId (string): (required)
		- interfaceIp (string): The IP address of the interface to use
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
		
		- networkId (string): (required)
		- enabled (boolean): Boolean value to enable or disable OSPF routing. OSPF routing is disabled by default.
		- helloTimerInSeconds (integer): Time interval in seconds at which hello packet will be sent to OSPF neighbors to maintain connectivity. Value must be between 1 and 255. Default is 10 seconds
		- deadTimerInSeconds (integer): Time interval to determine when the peer will be declare inactive/dead. Value must be between 1 and 65535
		- areas (array): OSPF areas
		- md5AuthenticationEnabled (boolean): Boolean value to enable or disable MD5 authentication. MD5 authentication is disabled by default.
		- md5AuthenticationKey (object): MD5 authentication credentials. This param is only relevant if md5AuthenticationEnabled is true
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['switch', 'configure', 'routing', 'ospf'],
			'operation': 'updateNetworkSwitchRoutingOspf'
		}
		resource = f'/networks/{networkId}/switch/routing/ospf'

		body_params = ['enabled', 'helloTimerInSeconds', 'deadTimerInSeconds', 'areas', 'md5AuthenticationEnabled', 'md5AuthenticationKey', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def createNetworkSwitchStackRoutingInterface(self, networkId: str, switchStackId: str, name: str, subnet: str, interfaceIp: str, vlanId: int, **kwargs):
		"""
		**Create a layer 3 interface for a switch stack**
		https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface
		
		- networkId (string): (required)
		- switchStackId (string): (required)
		- name (string): A friendly name or description for the interface or VLAN.
		- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
		- interfaceIp (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
		- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
		- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'. Default is 'disabled'.
		- defaultGateway (string): The next hop for any traffic that isn't going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface.
		- ospfSettings (object): The OSPF routing settings of the interface.
		"""

		kwargs.update(locals())

		if 'multicastRouting' in kwargs:
			options = ['disabled', 'enabled', 'IGMP snooping querier']
			assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
			'operation': 'createNetworkSwitchStackRoutingInterface'
		}
		resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces'

		body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'defaultGateway', 'ospfSettings', ]
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
		
		- networkId (string): (required)
		- switchStackId (string): (required)
		- interfaceId (string): (required)
		- name (string): A friendly name or description for the interface or VLAN.
		- subnet (string): The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24).
		- interfaceIp (string): The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch's management IP.
		- multicastRouting (string): Enable multicast support if, multicast routing between VLANs is required. Options are, 'disabled', 'enabled' or 'IGMP snooping querier'.
		- vlanId (integer): The VLAN this routed interface is on. VLAN must be between 1 and 4094.
		- ospfSettings (object): The OSPF routing settings of the interface.
		"""

		kwargs.update(locals())

		if 'multicastRouting' in kwargs:
			options = ['disabled', 'enabled', 'IGMP snooping querier']
			assert kwargs['multicastRouting'] in options, f'''"multicastRouting" cannot be "{kwargs['multicastRouting']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
			'operation': 'updateNetworkSwitchStackRoutingInterface'
		}
		resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

		body_params = ['name', 'subnet', 'interfaceIp', 'multicastRouting', 'vlanId', 'ospfSettings', ]
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
		
		- networkId (string): (required)
		- switchStackId (string): (required)
		- interfaceId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'stacks', 'routing', 'interfaces'],
			'operation': 'deleteNetworkSwitchStackRoutingInterface'
		}
		resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateNetworkSwitchStackRoutingInterfaceDhcp(self, networkId: str, switchStackId: str, interfaceId: str, **kwargs):
		"""
		**Update a layer 3 interface DHCP configuration for a switch stack**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp
		
		- networkId (string): (required)
		- switchStackId (string): (required)
		- interfaceId (string): (required)
		- dhcpMode (string): The DHCP mode options for the switch stack interface ('dhcpDisabled', 'dhcpRelay' or 'dhcpServer')
		- dhcpRelayServerIps (array): The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface
		- dhcpLeaseTime (string): The DHCP lease time config for the dhcp server running on switch stack interface ('30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week')
		- dnsNameserversOption (string): The DHCP name server option for the dhcp server running on the switch stack interface ('googlePublicDns', 'openDns' or 'custom')
		- dnsCustomNameservers (array): The DHCP name server IPs when DHCP name server option is 'custom'
		- bootOptionsEnabled (boolean): Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface
		- bootNextServer (string): The PXE boot server IP for the DHCP server running on the switch stack interface
		- bootFileName (string): The PXE boot server file name for the DHCP server running on the switch stack interface
		- dhcpOptions (array): Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface
		- reservedIpRanges (array): Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface
		- fixedIpAssignments (array): Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface
		"""

		kwargs.update(locals())

		if 'dhcpMode' in kwargs:
			options = ['dhcpDisabled', 'dhcpRelay', 'dhcpServer']
			assert kwargs['dhcpMode'] in options, f'''"dhcpMode" cannot be "{kwargs['dhcpMode']}", & must be set to one of: {options}'''
		if 'dhcpLeaseTime' in kwargs:
			options = ['30 minutes', '1 hour', '4 hours', '12 hours', '1 day', '1 week']
			assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''
		if 'dnsNameserversOption' in kwargs:
			options = ['googlePublicDns', 'openDns', 'custom']
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
		
		- networkId (string): (required)
		- switchStackId (string): (required)
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
		
		- networkId (string): (required)
		- switchStackId (string): (required)
		- staticRouteId (string): (required)
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
		resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

		body_params = ['name', 'subnet', 'nextHopIp', 'advertiseViaOspfEnabled', 'preferOverOspfRoutesEnabled', ]
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
		
		- networkId (string): (required)
		- switchStackId (string): (required)
		- staticRouteId (string): (required)
		"""

		metadata = {
			'tags': ['switch', 'configure', 'stacks', 'routing', 'staticRoutes'],
			'operation': 'deleteNetworkSwitchStackRoutingStaticRoute'
		}
		resource = f'/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}'

		action = {
			"resource": resource,
			"operation": "destroy",
			"body": payload
		}
		return action






	def updateNetworkSwitchStormControl(self, networkId: str, **kwargs):
		"""
		**Update the storm control configuration for a switch network**
		https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control
		
		- networkId (string): (required)
		- broadcastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
		- multicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
		- unknownUnicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['switch', 'configure', 'stormControl'],
			'operation': 'updateNetworkSwitchStormControl'
		}
		resource = f'/networks/{networkId}/switch/stormControl'

		body_params = ['broadcastThreshold', 'multicastThreshold', 'unknownUnicastThreshold', ]
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
		
		- networkId (string): (required)
		- rstpEnabled (boolean): The spanning tree protocol status in network
		- stpBridgePriority (array): STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.
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
		**Update a switch profile port**
		https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port
		
		- organizationId (string): (required)
		- configTemplateId (string): (required)
		- profileId (string): (required)
		- portId (string): (required)
		- name (string): The name of the switch profile port
		- tags (array): The list of tags of the switch profile port
		- enabled (boolean): The status of the switch profile port
		- type (string): The type of the switch profile port ('trunk' or 'access')
		- vlan (integer): The VLAN of the switch profile port. A null value will clear the value set for trunk ports.
		- voiceVlan (integer): The voice VLAN of the switch profile port. Only applicable to access ports
		- allowedVlans (string): The VLANs allowed on the switch profile port. Only applicable to trunk ports
		- poeEnabled (boolean): The PoE status of the switch profile port
		- isolationEnabled (boolean): The isolation status of the switch profile port
		- rstpEnabled (boolean): The rapid spanning tree protocol status
		- stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
		- linkNegotiation (string): The link speed for the switch profile port
		- portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
		- udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
		- accessPolicyType (string): The type of the access policy of the switch profile port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC allow list' or 'Sticky MAC allow list'
		- accessPolicyNumber (integer): The number of a custom access policy to configure on the switch profile port. Only applicable when 'accessPolicyType' is 'Custom access policy'
		- macAllowList (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC allow list'
		- stickyMacAllowList (array): The initial list of MAC addresses for sticky Mac allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
		- stickyMacAllowListLimit (integer): The maximum number of MAC addresses for sticky MAC allow list. Only applicable when 'accessPolicyType' is 'Sticky MAC allow list'
		- stormControlEnabled (boolean): The storm control status of the switch profile port
		- flexibleStackingEnabled (boolean): For supported switches (e.g. MS420/MS425), whether or not the port has flexible stacking enabled.
		"""

		kwargs.update(locals())

		if 'type' in kwargs:
			options = ['trunk', 'access']
			assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''
		if 'stpGuard' in kwargs:
			options = ['disabled', 'root guard', 'bpdu guard', 'loop guard']
			assert kwargs['stpGuard'] in options, f'''"stpGuard" cannot be "{kwargs['stpGuard']}", & must be set to one of: {options}'''
		if 'udld' in kwargs:
			options = ['Alert only', 'Enforce']
			assert kwargs['udld'] in options, f'''"udld" cannot be "{kwargs['udld']}", & must be set to one of: {options}'''
		if 'accessPolicyType' in kwargs:
			options = ['Open', 'Custom access policy', 'MAC allow list', 'Sticky MAC allow list']
			assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

		metadata = {
			'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
			'operation': 'updateOrganizationConfigTemplateSwitchProfilePort'
		}
		resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}'

		body_params = ['name', 'tags', 'enabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'poeEnabled', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macAllowList', 'stickyMacAllowList', 'stickyMacAllowListLimit', 'stormControlEnabled', 'flexibleStackingEnabled', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def cloneOrganizationSwitchDevices(self, organizationId: str, sourceSerial: str, targetSerials: list):
		"""
		**Clone port-level and some switch-level configuration settings from a source switch to one or more target switches**
		https://developer.cisco.com/meraki/api-v1/#!clone-organization-switch-devices
		
		- organizationId (string): (required)
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
			"operation": "create",
			"body": payload
		}
		return action




