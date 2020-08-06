class Events(object):
    def __init__(self, session):
        super(Events, self).__init__()
        self._session = session
    
    def getNetworkEvents(self, networkId: str, total_pages=1, direction='prev', **kwargs):
        """
        **List the events for the network**
        https://developer.cisco.com/meraki/api/#!get-network-events
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "prev" (default) or "next" page
        - productType (string): The product type to fetch events for. This parameter is required for networks with multiple device types. Valid types are wireless, appliance, switch, systemsManager, camera, and cellularGateway
        - includedEventTypes (array): A list of event types. The returned events will be filtered to only include events with these types.
        - excludedEventTypes (array): A list of event types. The returned events will be filtered to exclude events with these types.
        - deviceMac (string): The MAC address of the Meraki device which the list of events will be filtered with
        - deviceSerial (string): The serial of the Meraki device which the list of events will be filtered with
        - deviceName (string): The name of the Meraki device which the list of events will be filtered with
        - clientIp (string): The IP of the client which the list of events will be filtered with. Only supported for track-by-IP networks.
        - clientMac (string): The MAC address of the client which the list of events will be filtered with. Only supported for track-by-MAC networks.
        - clientName (string): The name, or partial name, of the client which the list of events will be filtered with
        - smDeviceMac (string): The MAC address of the Systems Manager device which the list of events will be filtered with
        - smDeviceName (string): The name of the Systems Manager device which the list of events will be filtered with
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Events'],
            'operation': 'getNetworkEvents',
        }
        resource = f'/networks/{networkId}/events'

        query_params = ['productType', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        array_params = ['includedEventTypes', 'excludedEventTypes']
        for (k, v) in kwargs.items():
            if k in array_params:
                params[f'{k}[]'] = kwargs[f'{k}']

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkEventsEventTypes(self, networkId: str):
        """
        **List the event type to human-readable description**
        https://developer.cisco.com/meraki/api/#!get-network-events-event-types
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Events'],
            'operation': 'getNetworkEventsEventTypes',
        }
        resource = f'/networks/{networkId}/events/eventTypes'

        return self._session.get(metadata, resource)

