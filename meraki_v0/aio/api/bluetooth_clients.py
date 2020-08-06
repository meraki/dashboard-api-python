class AsyncBluetoothClients:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkBluetoothClients(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the Bluetooth clients seen by APs in this network**
        https://developer.cisco.com/meraki/api/#!get-network-bluetooth-clients
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 7 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 5 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - includeConnectivityHistory (boolean): Include the connectivity history for this client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Bluetooth clients'],
            'operation': 'getNetworkBluetoothClients',
        }
        resource = f'/networks/{networkId}/bluetoothClients'

        query_params = ['t0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkBluetoothClient(self, networkId: str, bluetoothClientId: str, **kwargs):
        """
        **Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.**
        https://developer.cisco.com/meraki/api/#!get-network-bluetooth-client
        
        - networkId (string)
        - bluetoothClientId (string)
        - includeConnectivityHistory (boolean): Include the connectivity history for this client
        - connectivityHistoryTimespan (integer): The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Bluetooth clients'],
            'operation': 'getNetworkBluetoothClient',
        }
        resource = f'/networks/{networkId}/bluetoothClients/{bluetoothClientId}'

        query_params = ['includeConnectivityHistory', 'connectivityHistoryTimespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

