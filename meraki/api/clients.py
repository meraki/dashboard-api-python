class Clients(object):
    def __init__(self, session):
        super(Clients, self).__init__()
        self._session = session
    
    def getDeviceClients(self, serial: str, **kwargs):
        """
        **List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.**
        https://api.meraki.com/api_docs#list-the-clients-of-a-device-up-to-a-maximum-of-a-month-ago
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkClients(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the clients that have used this network in the timespan**
        https://api.meraki.com/api_docs#list-the-clients-that-have-used-this-network-in-the-timespan
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def provisionNetworkClients(self, networkId: str, **kwargs):
        """
        **Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.**
        https://api.meraki.com/api_docs#provisions-a-client-with-a-name-and-policy
        
        - networkId (string)
        - mac (string): The MAC address of the client. Required.
        - name (string): The display name for the client. Optional. Limited to 255 bytes.
        - devicePolicy (string): The policy to apply to the specified client. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.
        - groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'provisionNetworkClients',
        }
        resource = f'/networks/{networkId}/clients/provision'

        body_params = ['mac', 'name', 'devicePolicy', 'groupPolicyId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkClient(self, networkId: str, clientId: str):
        """
        **Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#return-the-client-associated-with-the-given-identifier
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClient',
        }
        resource = f'/networks/{networkId}/clients/{clientId}'

        return self._session.get(metadata, resource)

    def getNetworkClientEvents(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the events associated with this client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#return-the-events-associated-with-this-client
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkClientLatencyHistory(self, networkId: str, clientId: str, **kwargs):
        """
        **Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.**
        https://api.meraki.com/api_docs#return-the-latency-history-for-a-client
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkClientPolicy(self, networkId: str, clientId: str):
        """
        **Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#return-the-policy-assigned-to-a-client-on-the-network
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientPolicy',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/policy'

        return self._session.get(metadata, resource)

    def updateNetworkClientPolicy(self, networkId: str, clientId: str, **kwargs):
        """
        **Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#update-the-policy-assigned-to-a-client-on-the-network
        
        - networkId (string)
        - clientId (string)
        - devicePolicy (string): The group policy (Whitelisted, Blocked, Normal, Group policy)
        - groupPolicyId (string): [optional] If devicePolicy param is set to 'Group policy' this param is used to specify the group ID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'updateNetworkClientPolicy',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/policy'

        body_params = ['devicePolicy', 'groupPolicyId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkClientSplashAuthorizationStatus(self, networkId: str, clientId: str):
        """
        **Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#return-the-splash-authorization-for-a-client-for-each-ssid-theyve-associated-with-through-splash
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientSplashAuthorizationStatus',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus'

        return self._session.get(metadata, resource)

    def updateNetworkClientSplashAuthorizationStatus(self, networkId: str, clientId: str, **kwargs):
        """
        **Update a client's splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#update-a-clients-splash-authorization
        
        - networkId (string)
        - clientId (string)
        - ssids (object): The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Clients'],
            'operation': 'updateNetworkClientSplashAuthorizationStatus',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus'

        body_params = ['ssids']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkClientTrafficHistory(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#return-the-clients-network-traffic-data-over-time
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkClientUsageHistory(self, networkId: str, clientId: str):
        """
        **Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://api.meraki.com/api_docs#return-the-clients-daily-usage-history
        
        - networkId (string)
        - clientId (string)
        """

        metadata = {
            'tags': ['Clients'],
            'operation': 'getNetworkClientUsageHistory',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/usageHistory'

        return self._session.get(metadata, resource)

