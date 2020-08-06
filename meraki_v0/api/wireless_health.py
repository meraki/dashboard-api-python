class WirelessHealth(object):
    def __init__(self, session):
        super(WirelessHealth, self).__init__()
        self._session = session
    
    def getNetworkClientsConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by clients**
        https://developer.cisco.com/meraki/api/#!get-network-clients-connection-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientsConnectionStats',
        }
        resource = f'/networks/{networkId}/clients/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkClientsLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by clients**
        https://developer.cisco.com/meraki/api/#!get-network-clients-latency-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientsLatencyStats',
        }
        resource = f'/networks/{networkId}/clients/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkClientConnectionStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.**
        https://developer.cisco.com/meraki/api/#!get-network-client-connection-stats
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientConnectionStats',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkClientLatencyStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated latency info for a given client on this network. Clients are identified by their MAC.**
        https://developer.cisco.com/meraki/api/#!get-network-client-latency-stats
        
        - networkId (string)
        - clientId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkClientLatencyStats',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network**
        https://developer.cisco.com/meraki/api/#!get-network-connection-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkConnectionStats',
        }
        resource = f'/networks/{networkId}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkDevicesConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by node**
        https://developer.cisco.com/meraki/api/#!get-network-devices-connection-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDevicesConnectionStats',
        }
        resource = f'/networks/{networkId}/devices/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkDevicesLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by node**
        https://developer.cisco.com/meraki/api/#!get-network-devices-latency-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDevicesLatencyStats',
        }
        resource = f'/networks/{networkId}/devices/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkDeviceConnectionStats(self, networkId: str, serial: str, **kwargs):
        """
        **Aggregated connectivity info for a given AP on this network**
        https://developer.cisco.com/meraki/api/#!get-network-device-connection-stats
        
        - networkId (string)
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDeviceConnectionStats',
        }
        resource = f'/networks/{networkId}/devices/{serial}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkDeviceLatencyStats(self, networkId: str, serial: str, **kwargs):
        """
        **Aggregated latency info for a given AP on this network**
        https://developer.cisco.com/meraki/api/#!get-network-device-latency-stats
        
        - networkId (string)
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkDeviceLatencyStats',
        }
        resource = f'/networks/{networkId}/devices/{serial}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkFailedConnections(self, networkId: str, **kwargs):
        """
        **List of all failed client connection events on this network in a given time range**
        https://developer.cisco.com/meraki/api/#!get-network-failed-connections
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - serial (string): Filter by AP
        - clientId (string): Filter by client MAC
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkFailedConnections',
        }
        resource = f'/networks/{networkId}/failedConnections'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network**
        https://developer.cisco.com/meraki/api/#!get-network-latency-stats
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4' or '5'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Wireless health'],
            'operation': 'getNetworkLatencyStats',
        }
        resource = f'/networks/{networkId}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

