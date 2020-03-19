class AsyncWirelessHealth:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkClientsConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by clients**
        https://api.meraki.com/api_docs#aggregated-connectivity-info-for-this-network-grouped-by-clients
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientsConnectionStats',
        }
        resource = f'/networks/{networkId}/clients/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkClientsLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by clients**
        https://api.meraki.com/api_docs#aggregated-latency-info-for-this-network-grouped-by-clients
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientsLatencyStats',
        }
        resource = f'/networks/{networkId}/clients/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkClientConnectionStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.**
        https://api.meraki.com/api_docs#aggregated-connectivity-info-for-a-given-client-on-this-network
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientConnectionStats',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkClientLatencyStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated latency info for a given client on this network. Clients are identified by their MAC.**
        https://api.meraki.com/api_docs#aggregated-latency-info-for-a-given-client-on-this-network
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientLatencyStats',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network**
        https://api.meraki.com/api_docs#aggregated-connectivity-info-for-this-network
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkConnectionStats',
        }
        resource = f'/networks/{networkId}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkDevicesConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by node**
        https://api.meraki.com/api_docs#aggregated-connectivity-info-for-this-network-grouped-by-node
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDevicesConnectionStats',
        }
        resource = f'/networks/{networkId}/devices/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkDevicesLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by node**
        https://api.meraki.com/api_docs#aggregated-latency-info-for-this-network-grouped-by-node
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDevicesLatencyStats',
        }
        resource = f'/networks/{networkId}/devices/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkDeviceConnectionStats(self, networkId: str, serial: str, **kwargs):
        """
        **Aggregated connectivity info for a given AP on this network**
        https://api.meraki.com/api_docs#aggregated-connectivity-info-for-a-given-ap-on-this-network
        
        - networkId (string)
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDeviceConnectionStats',
        }
        resource = f'/networks/{networkId}/devices/{serial}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkDeviceLatencyStats(self, networkId: str, serial: str, **kwargs):
        """
        **Aggregated latency info for a given AP on this network**
        https://api.meraki.com/api_docs#aggregated-latency-info-for-a-given-ap-on-this-network
        
        - networkId (string)
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDeviceLatencyStats',
        }
        resource = f'/networks/{networkId}/devices/{serial}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkFailedConnections(self, networkId: str, **kwargs):
        """
        **List of all failed client connection events on this network in a given time range**
        https://api.meraki.com/api_docs#list-of-all-failed-client-connection-events-on-this-network-in-a-given-time-range
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - serial (string): Filter by AP
        - clientId (string): Filter by client MAC
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkFailedConnections',
        }
        resource = f'/networks/{networkId}/failedConnections'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'serial', 'clientId']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network**
        https://api.meraki.com/api_docs#aggregated-latency-info-for-this-network
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkLatencyStats',
        }
        resource = f'/networks/{networkId}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

