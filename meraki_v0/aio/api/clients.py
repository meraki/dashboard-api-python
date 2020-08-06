class AsyncClients:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getDeviceClients(self, serial: str, **kwargs):
        """
        **List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.**
        https://developer.cisco.com/meraki/api/#!get-device-clients
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'getDeviceClients',
        }
        resource = f'/devices/{serial}/clients'

        query_params = ['t0', 'timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkClients(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the clients that have used this network in the timespan**
        https://developer.cisco.com/meraki/api/#!get-network-clients
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClients',
        }
        resource = f'/networks/{networkId}/clients'

        query_params = ['t0', 'timespan', 'perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def provisionNetworkClients(self, networkId: str, mac: str, devicePolicy: str, **kwargs):
        """
        **Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.**
        https://developer.cisco.com/meraki/api/#!provision-network-clients
        
        - networkId (string)
        - mac (string): The MAC address of the client. Required.
        - devicePolicy (string): The policy to apply to the specified client. Can be 'Group policy', 'Whitelisted', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
        - name (string): The display name for the client. Optional. Limited to 255 bytes.
        - groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
        - policiesBySecurityAppliance (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
        - policiesBySsid (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy
        """

        kwargs.update(locals())

        if 'devicePolicy' in kwargs:
            options = ['Group policy', 'Whitelisted', 'Allowed', 'Blocked', 'Per connection', 'Normal']
            assert kwargs['devicePolicy'] in options, f'''"devicePolicy" cannot be "{kwargs['devicePolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Clients'],
            'operation': 'provisionNetworkClients',
        }
        resource = f'/networks/{networkId}/clients/provision'

        body_params = ['mac', 'name', 'devicePolicy', 'groupPolicyId', 'policiesBySecurityAppliance', 'policiesBySsid']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkClient(self, networkId: str, clientId: str):
        """
        **Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClient',
        }
        resource = f'/networks/{networkId}/clients/{clientId}'

        return await self._session.get(metadata, resource)

    async def getNetworkClientEvents(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the events associated with this client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client-events
        
        - networkId (string)
        - clientId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientEvents',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/events'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkClientLatencyHistory(self, networkId: str, clientId: str, **kwargs):
        """
        **Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.**
        https://developer.cisco.com/meraki/api/#!get-network-client-latency-history
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientLatencyHistory',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/latencyHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkClientPolicy(self, networkId: str, clientId: str):
        """
        **Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client-policy
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientPolicy',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/policy'

        return await self._session.get(metadata, resource)

    async def updateNetworkClientPolicy(self, networkId: str, clientId: str, devicePolicy: str, **kwargs):
        """
        **Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!update-network-client-policy
        
        - networkId (string)
        - clientId (string)
        - devicePolicy (string): The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.
        - groupPolicyId (string): [optional] If 'devicePolicy' is set to 'Group policy' this param is used to specify the group policy ID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'updateNetworkClientPolicy',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/policy'

        body_params = ['devicePolicy', 'groupPolicyId']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkClientSplashAuthorizationStatus(self, networkId: str, clientId: str):
        """
        **Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client-splash-authorization-status
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientSplashAuthorizationStatus',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus'

        return await self._session.get(metadata, resource)

    async def updateNetworkClientSplashAuthorizationStatus(self, networkId: str, clientId: str, ssids: dict):
        """
        **Update a client's splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!update-network-client-splash-authorization-status
        
        - networkId (string)
        - clientId (string)
        - ssids (object): The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """

        kwargs = locals()

        metadata = {
            'tags': ['Clients'],
            'operation': 'updateNetworkClientSplashAuthorizationStatus',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus'

        body_params = ['ssids']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkClientTrafficHistory(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client-traffic-history
        
        - networkId (string)
        - clientId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientTrafficHistory',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/trafficHistory'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkClientUsageHistory(self, networkId: str, clientId: str):
        """
        **Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client-usage-history
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientUsageHistory',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/usageHistory'

        return await self._session.get(metadata, resource)

