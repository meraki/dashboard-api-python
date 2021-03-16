class ActionBatchCellularGateway(object):
	def __init__(self):
		super(ActionBatchCellularGateway, self).__init__()

	def updateDeviceCellularGatewayLan(self, serial: str, **kwargs):
		"""
		**Update the LAN Settings for a single MG.**
		https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan
		
		- serial (string): (required)
		- reservedIpRanges (array): list of all reserved IP ranges for a single MG
		- fixedIpAssignments (array): list of all fixed IP assignments for a single MG
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['cellularGateway', 'configure', 'lan'],
			'operation': 'updateDeviceCellularGatewayLan'
		}
		resource = f'/devices/{serial}/cellularGateway/lan'

		body_params = ['reservedIpRanges', 'fixedIpAssignments', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def updateDeviceCellularGatewayPortForwardingRules(self, serial: str, **kwargs):
		"""
		**Updates the port forwarding rules for a single MG.**
		https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-port-forwarding-rules
		
		- serial (string): (required)
		- rules (array): An array of port forwarding params
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['cellularGateway', 'configure', 'portForwardingRules'],
			'operation': 'updateDeviceCellularGatewayPortForwardingRules'
		}
		resource = f'/devices/{serial}/cellularGateway/portForwardingRules'

		body_params = ['rules', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def updateNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
		"""
		**Update the connectivity testing destinations for an MG network**
		https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-connectivity-monitoring-destinations
		
		- networkId (string): (required)
		- destinations (array): The list of connectivity monitoring destinations
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['cellularGateway', 'configure', 'connectivityMonitoringDestinations'],
			'operation': 'updateNetworkCellularGatewayConnectivityMonitoringDestinations'
		}
		resource = f'/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations'

		body_params = ['destinations', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def updateNetworkCellularGatewayDhcp(self, networkId: str, **kwargs):
		"""
		**Update common DHCP settings of MGs**
		https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-dhcp
		
		- networkId (string): (required)
		- dhcpLeaseTime (string): DHCP Lease time for all MG of the network. It can be '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
		- dnsNameservers (string): DNS name servers mode for all MG of the network. It can take 4 different values: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
		- dnsCustomNameservers (array): list of fixed IP representing the the DNS Name servers when the mode is 'custom'
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['cellularGateway', 'configure', 'dhcp'],
			'operation': 'updateNetworkCellularGatewayDhcp'
		}
		resource = f'/networks/{networkId}/cellularGateway/dhcp'

		body_params = ['dhcpLeaseTime', 'dnsNameservers', 'dnsCustomNameservers', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def updateNetworkCellularGatewaySubnetPool(self, networkId: str, **kwargs):
		"""
		**Update the subnet pool and mask configuration for MGs in the network.**
		https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-subnet-pool
		
		- networkId (string): (required)
		- mask (integer): Mask used for the subnet of all MGs in  this network.
		- cidr (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['cellularGateway', 'configure', 'subnetPool'],
			'operation': 'updateNetworkCellularGatewaySubnetPool'
		}
		resource = f'/networks/{networkId}/cellularGateway/subnetPool'

		body_params = ['mask', 'cidr', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action






	def updateNetworkCellularGatewayUplink(self, networkId: str, **kwargs):
		"""
		**Updates the uplink settings for your MG network.**
		https://developer.cisco.com/meraki/api-v1/#!update-network-cellular-gateway-uplink
		
		- networkId (string): (required)
		- bandwidthLimits (object): The bandwidth settings for the 'cellular' uplink
		"""

		kwargs.update(locals())

		metadata = {
			'tags': ['cellularGateway', 'configure', 'uplink'],
			'operation': 'updateNetworkCellularGatewayUplink'
		}
		resource = f'/networks/{networkId}/cellularGateway/uplink'

		body_params = ['bandwidthLimits', ]
		payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
		action = {
			"resource": resource,
			"operation": "update",
			"body": payload
		}
		return action




