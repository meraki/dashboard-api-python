import urllib


class ActionBatchCellularGateway(object):
    def __init__(self):
        super(ActionBatchCellularGateway, self).__init__()
        


    def updateDeviceCellularGatewayLan(self, serial: str, **kwargs):
        """
        **Update the LAN Settings for a single MG.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-gateway-lan

        - serial (string): Serial
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

        - serial (string): Serial
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

        - networkId (string): Network ID
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

        - networkId (string): Network ID
        - dhcpLeaseTime (string): DHCP Lease time for all MG of the network. Possible values are '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'.
        - dnsNameservers (string): DNS name servers mode for all MG of the network. Possible values are: 'upstream_dns', 'google_dns', 'opendns', 'custom'.
        - dnsCustomNameservers (array): list of fixed IPs representing the the DNS Name servers when the mode is 'custom'
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

        - networkId (string): Network ID
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

        - networkId (string): Network ID
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
        





    def updateOrganizationCellularGatewayEsimsInventory(self, organizationId: str, id: str, **kwargs):
        """
        **Toggle the status of an eSIM**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-inventory

        - organizationId (string): Organization ID
        - id (string): ID
        - status (string): Status the eSIM will be updated to
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'inventory'],
            'operation': 'updateOrganizationCellularGatewayEsimsInventory'
        }
        resource = f'/organizations/{organizationId}/cellularGateway/esims/inventory/{id}'

        body_params = ['status', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createOrganizationCellularGatewayEsimsServiceProvidersAccount(self, organizationId: str, accountId: str, apiKey: str, serviceProvider: dict, title: str, username: str):
        """
        **Add a service provider account.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-service-providers-account

        - organizationId (string): Organization ID
        - accountId (string): Service provider account ID
        - apiKey (string): Service provider account API key
        - serviceProvider (object): Service Provider information
        - title (string): Service provider account name
        - username (string): Service provider account username
        """

        kwargs = locals()

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders', 'accounts'],
            'operation': 'createOrganizationCellularGatewayEsimsServiceProvidersAccount'
        }
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts'

        body_params = ['accountId', 'apiKey', 'serviceProvider', 'title', 'username', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationCellularGatewayEsimsServiceProvidersAccount(self, organizationId: str, accountId: str, **kwargs):
        """
        **Edit service provider account info stored in Meraki's database.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-service-providers-account

        - organizationId (string): Organization ID
        - accountId (string): Account ID
        - title (string): Service provider account name used on the Meraki UI
        - apiKey (string): Service provider account API key
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders', 'accounts'],
            'operation': 'updateOrganizationCellularGatewayEsimsServiceProvidersAccount'
        }
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/{accountId}'

        body_params = ['title', 'apiKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationCellularGatewayEsimsServiceProvidersAccount(self, organizationId: str, accountId: str):
        """
        **Remove a service provider account's integration with the Dashboard.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-cellular-gateway-esims-service-providers-account

        - organizationId (string): Organization ID
        - accountId (string): Account ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders', 'accounts'],
            'operation': 'deleteOrganizationCellularGatewayEsimsServiceProvidersAccount'
        }
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/{accountId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createOrganizationCellularGatewayEsimsSwap(self, organizationId: str, swaps: list):
        """
        **Swap which profile an eSIM uses.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-cellular-gateway-esims-swap

        - organizationId (string): Organization ID
        - swaps (array): Each object represents a swap for one eSIM
        """

        kwargs = locals()

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'swap'],
            'operation': 'createOrganizationCellularGatewayEsimsSwap'
        }
        resource = f'/organizations/{organizationId}/cellularGateway/esims/swap'

        body_params = ['swaps', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "swap",
            "body": payload
        }
        return action
        





    def updateOrganizationCellularGatewayEsimsSwap(self, id: str, organizationId: str):
        """
        **Get the status of a profile swap.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-cellular-gateway-esims-swap

        - id (string): eSIM EID
        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'swap'],
            'operation': 'updateOrganizationCellularGatewayEsimsSwap'
        }
        resource = f'/organizations/{organizationId}/cellularGateway/esims/swap/{id}'

        action = {
            "resource": resource,
            "operation": "status",
        }
        return action
        



