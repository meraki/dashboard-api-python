import urllib


class CellularGateway(object):
    def __init__(self, session):
        super(CellularGateway, self).__init__()
        self._session = session
        


    def getDeviceCellularGatewayLan(self, serial: str):
        """
        **Show the LAN Settings of a MG**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-lan

        - serial (string): Serial
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'lan'],
            'operation': 'getDeviceCellularGatewayLan'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/cellularGateway/lan'

        return self._session.get(metadata, resource)
        


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
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/cellularGateway/lan'

        body_params = ['reservedIpRanges', 'fixedIpAssignments', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCellularGatewayPortForwardingRules(self, serial: str):
        """
        **Returns the port forwarding rules for a single MG.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-gateway-port-forwarding-rules

        - serial (string): Serial
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'portForwardingRules'],
            'operation': 'getDeviceCellularGatewayPortForwardingRules'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/cellularGateway/portForwardingRules'

        return self._session.get(metadata, resource)
        


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
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/cellularGateway/portForwardingRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewayConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MG network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-connectivity-monitoring-destinations

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'getNetworkCellularGatewayConnectivityMonitoringDestinations'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)
        


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
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations'

        body_params = ['destinations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewayDhcp(self, networkId: str):
        """
        **List common DHCP settings of MGs**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-dhcp

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'dhcp'],
            'operation': 'getNetworkCellularGatewayDhcp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/dhcp'

        return self._session.get(metadata, resource)
        


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
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/dhcp'

        body_params = ['dhcpLeaseTime', 'dnsNameservers', 'dnsCustomNameservers', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewaySubnetPool(self, networkId: str):
        """
        **Return the subnet pool and mask configured for MGs in the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-subnet-pool

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'subnetPool'],
            'operation': 'getNetworkCellularGatewaySubnetPool'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/subnetPool'

        return self._session.get(metadata, resource)
        


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
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/subnetPool'

        body_params = ['mask', 'cidr', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCellularGatewayUplink(self, networkId: str):
        """
        **Returns the uplink settings for your MG network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-cellular-gateway-uplink

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'uplink'],
            'operation': 'getNetworkCellularGatewayUplink'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/uplink'

        return self._session.get(metadata, resource)
        


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
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/cellularGateway/uplink'

        body_params = ['bandwidthLimits', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationCellularGatewayEsimsInventory(self, organizationId: str, **kwargs):
        """
        **The eSIM inventory of a given organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-inventory

        - organizationId (string): Organization ID
        - eids (array): Optional parameter to filter the results by EID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'inventory'],
            'operation': 'getOrganizationCellularGatewayEsimsInventory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/inventory'

        query_params = ['eids', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['eids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/inventory/{id}'

        body_params = ['status', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationCellularGatewayEsimsServiceProviders(self, organizationId: str):
        """
        **Service providers customers can add accounts for.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders'],
            'operation': 'getOrganizationCellularGatewayEsimsServiceProviders'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders'

        return self._session.get(metadata, resource)
        


    def getOrganizationCellularGatewayEsimsServiceProvidersAccounts(self, organizationId: str, **kwargs):
        """
        **Inventory of service provider accounts tied to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts

        - organizationId (string): Organization ID
        - accountIds (array): Optional parameter to filter the results by service provider account IDs.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders', 'accounts'],
            'operation': 'getOrganizationCellularGatewayEsimsServiceProvidersAccounts'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts'

        query_params = ['accountIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['accountIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts'

        body_params = ['accountId', 'apiKey', 'serviceProvider', 'title', 'username', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans(self, organizationId: str, accountIds: list):
        """
        **The communication plans available for a given provider.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts-communication-plans

        - organizationId (string): Organization ID
        - accountIds (array): Account IDs that communication plans will be fetched for
        """

        kwargs = locals()

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders', 'accounts', 'communicationPlans'],
            'operation': 'getOrganizationCellularGatewayEsimsServiceProvidersAccountsCommunicationPlans'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/communicationPlans'

        query_params = ['accountIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['accountIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans(self, organizationId: str, accountIds: list):
        """
        **The rate plans available for a given provider.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-esims-service-providers-accounts-rate-plans

        - organizationId (string): Organization ID
        - accountIds (array): Account IDs that rate plans will be fetched for
        """

        kwargs = locals()

        metadata = {
            'tags': ['cellularGateway', 'configure', 'esims', 'serviceProviders', 'accounts', 'ratePlans'],
            'operation': 'getOrganizationCellularGatewayEsimsServiceProvidersAccountsRatePlans'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/ratePlans'

        query_params = ['accountIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['accountIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        accountId = urllib.parse.quote(str(accountId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/{accountId}'

        body_params = ['title', 'apiKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        accountId = urllib.parse.quote(str(accountId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/serviceProviders/accounts/{accountId}'

        return self._session.delete(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/swap'

        body_params = ['swaps', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        id = urllib.parse.quote(str(id), safe='')
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/esims/swap/{id}'

        return self._session.put(metadata, resource)
        


    def getOrganizationCellularGatewayUplinkStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the uplink status of every Meraki MG cellular gateway in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cellular-gateway-uplink-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['cellularGateway', 'monitor', 'uplink', 'statuses'],
            'operation': 'getOrganizationCellularGatewayUplinkStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/cellularGateway/uplink/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'iccids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
