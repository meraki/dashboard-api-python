class AsyncNetworks:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getNetwork(self, networkId: str):
        """
        **Return a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'getNetwork'
        }
        resource = f'/networks/{networkId}'

        return self._session.get(metadata, resource)

    def updateNetwork(self, networkId: str, **kwargs):
        """
        **Update a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network

        - networkId (string): (required)
        - name (string): The name of the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - tags (array): A list of tags to be applied to the network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'updateNetwork'
        }
        resource = f'/networks/{networkId}'

        body_params = ['name', 'timeZone', 'tags', 'enrollmentString', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetwork(self, networkId: str):
        """
        **Delete a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'deleteNetwork'
        }
        resource = f'/networks/{networkId}'

        return self._session.delete(metadata, resource)

    def getNetworkAlertsSettings(self, networkId: str):
        """
        **Return the alert configuration for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-alerts-settings

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'alerts', 'settings'],
            'operation': 'getNetworkAlertsSettings'
        }
        resource = f'/networks/{networkId}/alerts/settings'

        return self._session.get(metadata, resource)

    def updateNetworkAlertsSettings(self, networkId: str, **kwargs):
        """
        **Update the alert configuration for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-alerts-settings

        - networkId (string): (required)
        - defaultDestinations (object): The network-wide destinations for all alerts on the network.
        - alerts (array): Alert-specific configuration for each type. Only alerts that pertain to the network can be updated.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'alerts', 'settings'],
            'operation': 'updateNetworkAlertsSettings'
        }
        resource = f'/networks/{networkId}/alerts/settings'

        body_params = ['defaultDestinations', 'alerts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def bindNetwork(self, networkId: str, configTemplateId: str, **kwargs):
        """
        **Bind a network to a template.**
        https://developer.cisco.com/meraki/api-v1/#!bind-network

        - networkId (string): (required)
        - configTemplateId (string): The ID of the template to which the network should be bound.
        - autoBind (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'bindNetwork'
        }
        resource = f'/networks/{networkId}/bind'

        body_params = ['configTemplateId', 'autoBind', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkBluetoothClients(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the Bluetooth clients seen by APs in this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-clients

        - networkId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
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
            'tags': ['networks', 'monitor', 'bluetoothClients'],
            'operation': 'getNetworkBluetoothClients'
        }
        resource = f'/networks/{networkId}/bluetoothClients'

        query_params = ['t0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'includeConnectivityHistory', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkBluetoothClient(self, networkId: str, bluetoothClientId: str, **kwargs):
        """
        **Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-bluetooth-client

        - networkId (string): (required)
        - bluetoothClientId (string): (required)
        - includeConnectivityHistory (boolean): Include the connectivity history for this client
        - connectivityHistoryTimespan (integer): The timespan, in seconds, for the connectivityHistory data. By default 1 day, 86400, will be used.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'monitor', 'bluetoothClients'],
            'operation': 'getNetworkBluetoothClient'
        }
        resource = f'/networks/{networkId}/bluetoothClients/{bluetoothClientId}'

        query_params = ['includeConnectivityHistory', 'connectivityHistoryTimespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkClients(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the clients that have used this network in the timespan**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        - networkId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'monitor', 'clients'],
            'operation': 'getNetworkClients'
        }
        resource = f'/networks/{networkId}/clients'

        query_params = ['t0', 'timespan', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def provisionNetworkClients(self, networkId: str, clients: list, devicePolicy: str, **kwargs):
        """
        **Provisions a client with a name and policy. Clients can be provisioned before they associate to the network.**
        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        - networkId (string): (required)
        - clients (array): The array of clients to provision
        - devicePolicy (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
        - groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
        - policiesBySecurityAppliance (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
        - policiesBySsid (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy
        """

        kwargs.update(locals())

        if 'devicePolicy' in kwargs:
            options = ['Group policy', 'Allowed', 'Blocked', 'Per connection', 'Normal']
            assert kwargs['devicePolicy'] in options, f'''"devicePolicy" cannot be "{kwargs['devicePolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'clients'],
            'operation': 'provisionNetworkClients'
        }
        resource = f'/networks/{networkId}/clients/provision'

        body_params = ['clients', 'devicePolicy', 'groupPolicyId', 'policiesBySecurityAppliance', 'policiesBySsid', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkClient(self, networkId: str, clientId: str):
        """
        **Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client

        - networkId (string): (required)
        - clientId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'monitor', 'clients'],
            'operation': 'getNetworkClient'
        }
        resource = f'/networks/{networkId}/clients/{clientId}'

        return self._session.get(metadata, resource)

    def getNetworkClientPolicy(self, networkId: str, clientId: str):
        """
        **Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-policy

        - networkId (string): (required)
        - clientId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'clients', 'policy'],
            'operation': 'getNetworkClientPolicy'
        }
        resource = f'/networks/{networkId}/clients/{clientId}/policy'

        return self._session.get(metadata, resource)

    def updateNetworkClientPolicy(self, networkId: str, clientId: str, devicePolicy: str, **kwargs):
        """
        **Update the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-client-policy

        - networkId (string): (required)
        - clientId (string): (required)
        - devicePolicy (string): The policy to assign. Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'. Required.
        - groupPolicyId (string): [optional] If 'devicePolicy' is set to 'Group policy' this param is used to specify the group policy ID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'clients', 'policy'],
            'operation': 'updateNetworkClientPolicy'
        }
        resource = f'/networks/{networkId}/clients/{clientId}/policy'

        body_params = ['devicePolicy', 'groupPolicyId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkClientSplashAuthorizationStatus(self, networkId: str, clientId: str):
        """
        **Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-splash-authorization-status

        - networkId (string): (required)
        - clientId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'clients', 'splashAuthorizationStatus'],
            'operation': 'getNetworkClientSplashAuthorizationStatus'
        }
        resource = f'/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus'

        return self._session.get(metadata, resource)

    def updateNetworkClientSplashAuthorizationStatus(self, networkId: str, clientId: str, ssids: dict):
        """
        **Update a client's splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-client-splash-authorization-status

        - networkId (string): (required)
        - clientId (string): (required)
        - ssids (object): The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID's splash frequency. Not all networks support configuring all SSIDs
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'clients', 'splashAuthorizationStatus'],
            'operation': 'updateNetworkClientSplashAuthorizationStatus'
        }
        resource = f'/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus'

        body_params = ['ssids', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkClientTrafficHistory(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-traffic-history

        - networkId (string): (required)
        - clientId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'monitor', 'clients', 'trafficHistory'],
            'operation': 'getNetworkClientTrafficHistory'
        }
        resource = f'/networks/{networkId}/clients/{clientId}/trafficHistory'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkClientUsageHistory(self, networkId: str, clientId: str):
        """
        **Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-client-usage-history

        - networkId (string): (required)
        - clientId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'monitor', 'clients', 'usageHistory'],
            'operation': 'getNetworkClientUsageHistory'
        }
        resource = f'/networks/{networkId}/clients/{clientId}/usageHistory'

        return self._session.get(metadata, resource)

    def getNetworkDevices(self, networkId: str):
        """
        **List the devices in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-devices

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'devices'],
            'operation': 'getNetworkDevices'
        }
        resource = f'/networks/{networkId}/devices'

        return self._session.get(metadata, resource)

    def claimNetworkDevices(self, networkId: str, serials: list):
        """
        **Claim devices into a network**
        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        - networkId (string): (required)
        - serials (array): A list of serials of devices to claim
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'devices'],
            'operation': 'claimNetworkDevices'
        }
        resource = f'/networks/{networkId}/devices/claim'

        body_params = ['serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def removeNetworkDevices(self, networkId: str, serial: str):
        """
        **Remove a single device**
        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        - networkId (string): (required)
        - serial (string): The serial of a device
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'devices'],
            'operation': 'removeNetworkDevices'
        }
        resource = f'/networks/{networkId}/devices/remove'

        body_params = ['serial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkEvents(self, networkId: str, total_pages=1, direction='prev', **kwargs):
        """
        **List the events for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-events

        - networkId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" or "prev" (default) page
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
            'tags': ['networks', 'monitor', 'events'],
            'operation': 'getNetworkEvents'
        }
        resource = f'/networks/{networkId}/events'

        query_params = ['productType', 'includedEventTypes', 'excludedEventTypes', 'deviceMac', 'deviceSerial', 'deviceName', 'clientIp', 'clientMac', 'clientName', 'smDeviceMac', 'smDeviceName', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['includedEventTypes', 'excludedEventTypes', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkEventsEventTypes(self, networkId: str):
        """
        **List the event type to human-readable description**
        https://developer.cisco.com/meraki/api-v1/#!get-network-events-event-types

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'monitor', 'events', 'eventTypes'],
            'operation': 'getNetworkEventsEventTypes'
        }
        resource = f'/networks/{networkId}/events/eventTypes'

        return self._session.get(metadata, resource)

    def getNetworkFirmwareUpgrades(self, networkId: str):
        """
        **Get current maintenance window for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-firmware-upgrades

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'firmwareUpgrades'],
            'operation': 'getNetworkFirmwareUpgrades'
        }
        resource = f'/networks/{networkId}/firmwareUpgrades'

        return self._session.get(metadata, resource)

    def updateNetworkFirmwareUpgrades(self, networkId: str, **kwargs):
        """
        **Update current maintenance window for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        - networkId (string): (required)
        - upgradeWindow (object): Upgrade window for devices in network
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'firmwareUpgrades'],
            'operation': 'updateNetworkFirmwareUpgrades'
        }
        resource = f'/networks/{networkId}/firmwareUpgrades'

        body_params = ['upgradeWindow', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkFloorPlans(self, networkId: str):
        """
        **List the floor plans that belong to your network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plans

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'getNetworkFloorPlans'
        }
        resource = f'/networks/{networkId}/floorPlans'

        return self._session.get(metadata, resource)

    def createNetworkFloorPlan(self, networkId: str, name: str, imageContents: str, **kwargs):
        """
        **Upload a floor plan**
        https://developer.cisco.com/meraki/api-v1/#!create-network-floor-plan

        - networkId (string): (required)
        - name (string): The name of your floor plan.
        - imageContents (string): The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.
        - center (object): The longitude and latitude of the center of your floor plan. The 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'createNetworkFloorPlan'
        }
        resource = f'/networks/{networkId}/floorPlans'

        body_params = ['name', 'center', 'bottomLeftCorner', 'bottomRightCorner', 'topLeftCorner', 'topRightCorner', 'imageContents', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkFloorPlan(self, networkId: str, floorPlanId: str):
        """
        **Find a floor plan by ID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-floor-plan

        - networkId (string): (required)
        - floorPlanId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'getNetworkFloorPlan'
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        return self._session.get(metadata, resource)

    def updateNetworkFloorPlan(self, networkId: str, floorPlanId: str, **kwargs):
        """
        **Update a floor plan's geolocation and other meta data**
        https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

        - networkId (string): (required)
        - floorPlanId (string): (required)
        - name (string): The name of your floor plan.
        - center (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        - imageContents (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'updateNetworkFloorPlan'
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        body_params = ['name', 'center', 'bottomLeftCorner', 'bottomRightCorner', 'topLeftCorner', 'topRightCorner', 'imageContents', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkFloorPlan(self, networkId: str, floorPlanId: str):
        """
        **Destroy a floor plan**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

        - networkId (string): (required)
        - floorPlanId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'deleteNetworkFloorPlan'
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        return self._session.delete(metadata, resource)

    def getNetworkGroupPolicies(self, networkId: str):
        """
        **List the group policies in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policies

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'getNetworkGroupPolicies'
        }
        resource = f'/networks/{networkId}/groupPolicies'

        return self._session.get(metadata, resource)

    def createNetworkGroupPolicy(self, networkId: str, name: str, **kwargs):
        """
        **Create a group policy**
        https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

        - networkId (string): (required)
        - name (string): The name for your group policy. Required.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
        """

        kwargs.update(locals())

        if 'splashAuthSettings' in kwargs:
            options = ['network default', 'bypass']
            assert kwargs['splashAuthSettings'] in options, f'''"splashAuthSettings" cannot be "{kwargs['splashAuthSettings']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'createNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies'

        body_params = ['name', 'scheduling', 'bandwidth', 'firewallAndTrafficShaping', 'contentFiltering', 'splashAuthSettings', 'vlanTagging', 'bonjourForwarding', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkGroupPolicy(self, networkId: str, groupPolicyId: str):
        """
        **Display a group policy**
        https://developer.cisco.com/meraki/api-v1/#!get-network-group-policy

        - networkId (string): (required)
        - groupPolicyId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'getNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        return self._session.get(metadata, resource)

    def updateNetworkGroupPolicy(self, networkId: str, groupPolicyId: str, **kwargs):
        """
        **Update a group policy**
        https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

        - networkId (string): (required)
        - groupPolicyId (string): (required)
        - name (string): The name for your group policy.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
        """

        kwargs.update(locals())

        if 'splashAuthSettings' in kwargs:
            options = ['network default', 'bypass']
            assert kwargs['splashAuthSettings'] in options, f'''"splashAuthSettings" cannot be "{kwargs['splashAuthSettings']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'updateNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        body_params = ['name', 'scheduling', 'bandwidth', 'firewallAndTrafficShaping', 'contentFiltering', 'splashAuthSettings', 'vlanTagging', 'bonjourForwarding', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkGroupPolicy(self, networkId: str, groupPolicyId: str):
        """
        **Delete a group policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

        - networkId (string): (required)
        - groupPolicyId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'deleteNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        return self._session.delete(metadata, resource)

    def getNetworkMerakiAuthUsers(self, networkId: str):
        """
        **List the splash or RADIUS users configured under Meraki Authentication for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-users

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'getNetworkMerakiAuthUsers'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers'

        return self._session.get(metadata, resource)

    def createNetworkMerakiAuthUser(self, networkId: str, email: str, name: str, password: str, authorizations: list, **kwargs):
        """
        **Create a user configured with Meraki Authentication for a network (currently supports 802.1X and Splash Guest users, and currently, organizations have a 50,000 user cap)**
        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        - networkId (string): (required)
        - email (string): Email address of the user
        - name (string): Name of the user
        - password (string): The password for this user account
        - authorizations (array): Authorization zones and expiration dates for the user.
        - accountType (string): Authorization type for user. Can be either 'Guest' or '802.1X'. Defaults to '802.1X'.
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        """

        kwargs.update(locals())

        if 'accountType' in kwargs:
            options = ['Guest', '802.1X']
            assert kwargs['accountType'] in options, f'''"accountType" cannot be "{kwargs['accountType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'createNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers'

        body_params = ['email', 'name', 'password', 'accountType', 'emailPasswordToUser', 'authorizations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str):
        """
        **Return the Meraki Auth splash or RADIUS user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-meraki-auth-user

        - networkId (string): (required)
        - merakiAuthUserId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'getNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        return self._session.get(metadata, resource)

    def deleteNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str):
        """
        **Delete a user configured with Meraki Authentication (currently only 802.1X RADIUS users can be deleted)**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

        - networkId (string): (required)
        - merakiAuthUserId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'deleteNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        return self._session.delete(metadata, resource)

    def updateNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str, **kwargs):
        """
        **Update a user configured with Meraki Authentication (currently only 802.1X RADIUS users can be updated)**
        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        - networkId (string): (required)
        - merakiAuthUserId (string): (required)
        - name (string): Name of the user
        - password (string): The password for this user account
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        - authorizations (array): Authorization zones and expiration dates for the user.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'updateNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        body_params = ['name', 'password', 'emailPasswordToUser', 'authorizations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkMqttBrokers(self, networkId: str):
        """
        **List the MQTT brokers for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-brokers

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'getNetworkMqttBrokers'
        }
        resource = f'/networks/{networkId}/mqttBrokers'

        return self._session.get(metadata, resource)

    def createNetworkMqttBroker(self, networkId: str, name: str, host: str, port: int):
        """
        **Add an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

        - networkId (string): (required)
        - name (string): Name of the MQTT broker
        - host (string): Host name/IP address where MQTT broker runs
        - port (integer): Host port though which MQTT broker can be reached
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'createNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers'

        body_params = ['name', 'host', 'port', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkMqttBroker(self, networkId: str, mqttBrokerId: str):
        """
        **Return an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!get-network-mqtt-broker

        - networkId (string): (required)
        - mqttBrokerId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'getNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers/{mqttBrokerId}'

        return self._session.get(metadata, resource)

    def updateNetworkMqttBroker(self, networkId: str, mqttBrokerId: str, **kwargs):
        """
        **Update an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

        - networkId (string): (required)
        - mqttBrokerId (string): (required)
        - name (string): Name of the mqtt config
        - host (string): Host name where mqtt broker runs
        - port (integer): Host port though which mqtt broker can be reached
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'updateNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers/{mqttBrokerId}'

        body_params = ['name', 'host', 'port', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkMqttBroker(self, networkId: str, mqttBrokerId: str):
        """
        **Delete an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

        - networkId (string): (required)
        - mqttBrokerId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'deleteNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers/{mqttBrokerId}'

        return self._session.delete(metadata, resource)

    def getNetworkNetflow(self, networkId: str):
        """
        **Return the NetFlow traffic reporting settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-netflow

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'netflow'],
            'operation': 'getNetworkNetflow'
        }
        resource = f'/networks/{networkId}/netflow'

        return self._session.get(metadata, resource)

    def updateNetworkNetflow(self, networkId: str, **kwargs):
        """
        **Update the NetFlow traffic reporting settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-netflow

        - networkId (string): (required)
        - reportingEnabled (boolean): Boolean indicating whether NetFlow traffic reporting is enabled (true) or disabled (false).
        - collectorIp (string): The IPv4 address of the NetFlow collector.
        - collectorPort (integer): The port that the NetFlow collector will be listening on.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'netflow'],
            'operation': 'updateNetworkNetflow'
        }
        resource = f'/networks/{networkId}/netflow'

        body_params = ['reportingEnabled', 'collectorIp', 'collectorPort', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkNetworkHealthChannelUtilization(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get the channel utilization over each radio for all APs in a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-network-health-channel-utilization

        - networkId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600. The default is 600.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'networkHealth', 'channelUtilization'],
            'operation': 'getNetworkNetworkHealthChannelUtilization'
        }
        resource = f'/networks/{networkId}/networkHealth/channelUtilization'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkPiiPiiKeys(self, networkId: str, **kwargs):
        """
        **List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-pii-keys

        - networkId (string): (required)
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'piiKeys'],
            'operation': 'getNetworkPiiPiiKeys'
        }
        resource = f'/networks/{networkId}/pii/piiKeys'

        query_params = ['username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkPiiRequests(self, networkId: str):
        """
        **List the PII requests for this network or organization**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-requests

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'requests'],
            'operation': 'getNetworkPiiRequests'
        }
        resource = f'/networks/{networkId}/pii/requests'

        return self._session.get(metadata, resource)

    def createNetworkPiiRequest(self, networkId: str, **kwargs):
        """
        **Submit a new delete or restrict processing PII request**
        https://developer.cisco.com/meraki/api-v1/#!create-network-pii-request

        - networkId (string): (required)
        - type (string): One of "delete" or "restrict processing"
        - datasets (array): The datasets related to the provided key that should be deleted. Only applies to "delete" requests. The value "all" will be expanded to all datasets applicable to this type. The datasets by applicable to each type are: mac (usage, events, traffic), email (users, loginAttempts), username (users, loginAttempts), bluetoothMac (client, connectivity), smDeviceId (device), smUserId (user)
        - username (string): The username of a network log in. Only applies to "delete" requests.
        - email (string): The email of a network user account. Only applies to "delete" requests.
        - mac (string): The MAC of a network client device. Applies to both "restrict processing" and "delete" requests.
        - smDeviceId (string): The sm_device_id of a Systems Manager device. The only way to "restrict processing" or "delete" a Systems Manager device. Must include "device" in the dataset for a "delete" request to destroy the device.
        - smUserId (string): The sm_user_id of a Systems Manager user. The only way to "restrict processing" or "delete" a Systems Manager user. Must include "user" in the dataset for a "delete" request to destroy the user.
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['delete', 'restrict processing']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'requests'],
            'operation': 'createNetworkPiiRequest'
        }
        resource = f'/networks/{networkId}/pii/requests'

        body_params = ['type', 'datasets', 'username', 'email', 'mac', 'smDeviceId', 'smUserId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkPiiRequest(self, networkId: str, requestId: str):
        """
        **Return a PII request**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-request

        - networkId (string): (required)
        - requestId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'requests'],
            'operation': 'getNetworkPiiRequest'
        }
        resource = f'/networks/{networkId}/pii/requests/{requestId}'

        return self._session.get(metadata, resource)

    def deleteNetworkPiiRequest(self, networkId: str, requestId: str):
        """
        **Delete a restrict processing PII request**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-pii-request

        - networkId (string): (required)
        - requestId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'requests'],
            'operation': 'deleteNetworkPiiRequest'
        }
        resource = f'/networks/{networkId}/pii/requests/{requestId}'

        return self._session.delete(metadata, resource)

    def getNetworkPiiSmDevicesForKey(self, networkId: str, **kwargs):
        """
        **Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-devices-for-key

        - networkId (string): (required)
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'smDevicesForKey'],
            'operation': 'getNetworkPiiSmDevicesForKey'
        }
        resource = f'/networks/{networkId}/pii/smDevicesForKey'

        query_params = ['username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkPiiSmOwnersForKey(self, networkId: str, **kwargs):
        """
        **Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-pii-sm-owners-for-key

        - networkId (string): (required)
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'pii', 'smOwnersForKey'],
            'operation': 'getNetworkPiiSmOwnersForKey'
        }
        resource = f'/networks/{networkId}/pii/smOwnersForKey'

        query_params = ['username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkSettings(self, networkId: str):
        """
        **Return the settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-settings

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'settings'],
            'operation': 'getNetworkSettings'
        }
        resource = f'/networks/{networkId}/settings'

        return self._session.get(metadata, resource)

    def updateNetworkSettings(self, networkId: str, **kwargs):
        """
        **Update the settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): (required)
        - localStatusPageEnabled (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
        - remoteStatusPageEnabled (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'settings'],
            'operation': 'updateNetworkSettings'
        }
        resource = f'/networks/{networkId}/settings'

        body_params = ['localStatusPageEnabled', 'remoteStatusPageEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSnmp(self, networkId: str):
        """
        **Return the SNMP settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-snmp

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'snmp'],
            'operation': 'getNetworkSnmp'
        }
        resource = f'/networks/{networkId}/snmp'

        return self._session.get(metadata, resource)

    def updateNetworkSnmp(self, networkId: str, **kwargs):
        """
        **Update the SNMP settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-snmp

        - networkId (string): (required)
        - access (string): The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c), or 'users' (V3).
        - communityString (string): The SNMP community string. Only relevant if 'access' is set to 'community'.
        - users (array): The list of SNMP users. Only relevant if 'access' is set to 'users'.
        """

        kwargs.update(locals())

        if 'access' in kwargs:
            options = ['none', 'community', 'users']
            assert kwargs['access'] in options, f'''"access" cannot be "{kwargs['access']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'snmp'],
            'operation': 'updateNetworkSnmp'
        }
        resource = f'/networks/{networkId}/snmp'

        body_params = ['access', 'communityString', 'users', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSplashLoginAttempts(self, networkId: str, **kwargs):
        """
        **List the splash login attempts for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-splash-login-attempts

        - networkId (string): (required)
        - ssidNumber (integer): Only return the login attempts for the specified SSID
        - loginIdentifier (string): The username, email, or phone number used during login
        - timespan (integer): The timespan, in seconds, for the login attempts. The period will be from [timespan] seconds ago until now. The maximum timespan is 3 months
        """

        kwargs.update(locals())

        if 'ssidNumber' in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs['ssidNumber'] in options, f'''"ssidNumber" cannot be "{kwargs['ssidNumber']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'monitor', 'splashLoginAttempts'],
            'operation': 'getNetworkSplashLoginAttempts'
        }
        resource = f'/networks/{networkId}/splashLoginAttempts'

        query_params = ['ssidNumber', 'loginIdentifier', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def splitNetwork(self, networkId: str):
        """
        **Split a combined network into individual networks for each type of device**
        https://developer.cisco.com/meraki/api-v1/#!split-network

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'splitNetwork'
        }
        resource = f'/networks/{networkId}/split'

        return self._session.post(metadata, resource)

    def getNetworkSyslogServers(self, networkId: str):
        """
        **List the syslog servers for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-syslog-servers

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'syslogServers'],
            'operation': 'getNetworkSyslogServers'
        }
        resource = f'/networks/{networkId}/syslogServers'

        return self._session.get(metadata, resource)

    def updateNetworkSyslogServers(self, networkId: str, servers: list):
        """
        **Update the syslog servers for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-syslog-servers

        - networkId (string): (required)
        - servers (array): A list of the syslog servers for this network
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'syslogServers'],
            'operation': 'updateNetworkSyslogServers'
        }
        resource = f'/networks/{networkId}/syslogServers'

        body_params = ['servers', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkTraffic(self, networkId: str, **kwargs):
        """
        **    The traffic analysis data for this network.
    <a href="https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility">Traffic Analysis with Hostname Visibility</a> must be enabled on the network.
**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic

        - networkId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
        - deviceType (string):     Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'.
    When using 'combined', for each rule the data will come from the device type with the most usage.

        """

        kwargs.update(locals())

        if 'deviceType' in kwargs:
            options = ['combined', 'wireless', 'switch', 'appliance']
            assert kwargs['deviceType'] in options, f'''"deviceType" cannot be "{kwargs['deviceType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'monitor', 'traffic'],
            'operation': 'getNetworkTraffic'
        }
        resource = f'/networks/{networkId}/traffic'

        query_params = ['t0', 'timespan', 'deviceType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkTrafficAnalysis(self, networkId: str):
        """
        **Return the traffic analysis settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-analysis

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'trafficAnalysis'],
            'operation': 'getNetworkTrafficAnalysis'
        }
        resource = f'/networks/{networkId}/trafficAnalysis'

        return self._session.get(metadata, resource)

    def updateNetworkTrafficAnalysis(self, networkId: str, **kwargs):
        """
        **Update the traffic analysis settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-traffic-analysis

        - networkId (string): (required)
        - mode (string):     The traffic analysis mode for the network. Can be one of 'disabled' (do not collect traffic types),
    'basic' (collect generic traffic categories), or 'detailed' (collect destination hostnames).

        - customPieChartItems (array): The list of items that make up the custom pie chart for traffic reporting.
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['disabled', 'basic', 'detailed']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'trafficAnalysis'],
            'operation': 'updateNetworkTrafficAnalysis'
        }
        resource = f'/networks/{networkId}/trafficAnalysis'

        body_params = ['mode', 'customPieChartItems', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkTrafficShapingApplicationCategories(self, networkId: str):
        """
        **Returns the application categories for traffic shaping rules.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-application-categories

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'trafficShaping', 'applicationCategories'],
            'operation': 'getNetworkTrafficShapingApplicationCategories'
        }
        resource = f'/networks/{networkId}/trafficShaping/applicationCategories'

        return self._session.get(metadata, resource)

    def getNetworkTrafficShapingDscpTaggingOptions(self, networkId: str):
        """
        **Returns the available DSCP tagging options for your traffic shaping rules.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-traffic-shaping-dscp-tagging-options

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'trafficShaping', 'dscpTaggingOptions'],
            'operation': 'getNetworkTrafficShapingDscpTaggingOptions'
        }
        resource = f'/networks/{networkId}/trafficShaping/dscpTaggingOptions'

        return self._session.get(metadata, resource)

    def unbindNetwork(self, networkId: str):
        """
        **Unbind a network from a template.**
        https://developer.cisco.com/meraki/api-v1/#!unbind-network

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'unbindNetwork'
        }
        resource = f'/networks/{networkId}/unbind'

        return self._session.post(metadata, resource)

    def getNetworkWebhooksHttpServers(self, networkId: str):
        """
        **List the HTTP servers for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-servers

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'httpServers'],
            'operation': 'getNetworkWebhooksHttpServers'
        }
        resource = f'/networks/{networkId}/webhooks/httpServers'

        return self._session.get(metadata, resource)

    def createNetworkWebhooksHttpServer(self, networkId: str, name: str, url: str, **kwargs):
        """
        **Add an HTTP server to a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server

        - networkId (string): (required)
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'httpServers'],
            'operation': 'createNetworkWebhooksHttpServer'
        }
        resource = f'/networks/{networkId}/webhooks/httpServers'

        body_params = ['name', 'url', 'sharedSecret', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkWebhooksHttpServer(self, networkId: str, httpServerId: str):
        """
        **Return an HTTP server for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-http-server

        - networkId (string): (required)
        - httpServerId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'httpServers'],
            'operation': 'getNetworkWebhooksHttpServer'
        }
        resource = f'/networks/{networkId}/webhooks/httpServers/{httpServerId}'

        return self._session.get(metadata, resource)

    def updateNetworkWebhooksHttpServer(self, networkId: str, httpServerId: str, **kwargs):
        """
        **Update an HTTP server**
        https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server

        - networkId (string): (required)
        - httpServerId (string): (required)
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'httpServers'],
            'operation': 'updateNetworkWebhooksHttpServer'
        }
        resource = f'/networks/{networkId}/webhooks/httpServers/{httpServerId}'

        body_params = ['name', 'url', 'sharedSecret', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkWebhooksHttpServer(self, networkId: str, httpServerId: str):
        """
        **Delete an HTTP server from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-http-server

        - networkId (string): (required)
        - httpServerId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'httpServers'],
            'operation': 'deleteNetworkWebhooksHttpServer'
        }
        resource = f'/networks/{networkId}/webhooks/httpServers/{httpServerId}'

        return self._session.delete(metadata, resource)

    def createNetworkWebhooksWebhookTest(self, networkId: str, url: str, **kwargs):
        """
        **Send a test webhook for a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-webhook-test

        - networkId (string): (required)
        - url (string): The URL where the test webhook will be sent
        - sharedSecret (string): The shared secret the test webhook will send. Optional. Defaults to an empty string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'webhookTests'],
            'operation': 'createNetworkWebhooksWebhookTest'
        }
        resource = f'/networks/{networkId}/webhooks/webhookTests'

        body_params = ['url', 'sharedSecret', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkWebhooksWebhookTest(self, networkId: str, webhookTestId: str):
        """
        **Return the status of a webhook test for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-webhooks-webhook-test

        - networkId (string): (required)
        - webhookTestId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'webhooks', 'webhookTests'],
            'operation': 'getNetworkWebhooksWebhookTest'
        }
        resource = f'/networks/{networkId}/webhooks/webhookTests/{webhookTestId}'

        return self._session.get(metadata, resource)