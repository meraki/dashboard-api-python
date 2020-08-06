class Devices(object):
    def __init__(self, session):
        super(Devices, self).__init__()
        self._session = session
    
    def cycleDeviceSwitchPorts(self, serial: str, ports: list):
        """
        **Cycle a set of switch ports**
        https://developer.cisco.com/meraki/api/#!cycle-device-switch-ports
        
        - serial (string)
        - ports (array): List of switch ports. Example: [1, 2-5, 1_MA-MOD-8X10G_1, 1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8]
        """

        kwargs = locals()

        metadata = {
            'tags': ['Devices'],
            'operation': 'cycleDeviceSwitchPorts',
        }
        resource = f'/devices/{serial}/switch/ports/cycle'

        body_params = ['ports']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkDevices(self, networkId: str):
        """
        **List the devices in a network**
        https://developer.cisco.com/meraki/api/#!get-network-devices
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Devices'],
            'operation': 'getNetworkDevices',
        }
        resource = f'/networks/{networkId}/devices'

        return self._session.get(metadata, resource)

    def claimNetworkDevices(self, networkId: str, **kwargs):
        """
        **Claim devices into a network**
        https://developer.cisco.com/meraki/api/#!claim-network-devices
        
        - networkId (string)
        - serials (array): A list of serials of devices to claim
        - serial (string): [DEPRECATED] The serial of a device to claim
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Devices'],
            'operation': 'claimNetworkDevices',
        }
        resource = f'/networks/{networkId}/devices/claim'

        body_params = ['serials', 'serial']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkDevice(self, networkId: str, serial: str):
        """
        **Return a single device**
        https://developer.cisco.com/meraki/api/#!get-network-device
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Devices'],
            'operation': 'getNetworkDevice',
        }
        resource = f'/networks/{networkId}/devices/{serial}'

        return self._session.get(metadata, resource)

    def updateNetworkDevice(self, networkId: str, serial: str, **kwargs):
        """
        **Update the attributes of a device**
        https://developer.cisco.com/meraki/api/#!update-network-device
        
        - networkId (string)
        - serial (string)
        - name (string): The name of a device
        - tags (string): The tags of a device
        - lat (number): The latitude of a device
        - lng (number): The longitude of a device
        - address (string): The address of a device
        - notes (string): The notes for the device. String. Limited to 255 characters.
        - moveMapMarker (boolean): Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        - switchProfileId (string): The ID of a switch profile to bind to the device (for available switch profiles, see the 'Switch Profiles' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch profile, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        - floorPlanId (string): The floor plan to associate to this device. null disassociates the device from the floorplan.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Devices'],
            'operation': 'updateNetworkDevice',
        }
        resource = f'/networks/{networkId}/devices/{serial}'

        body_params = ['name', 'tags', 'lat', 'lng', 'address', 'notes', 'moveMapMarker', 'switchProfileId', 'floorPlanId']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def blinkNetworkDeviceLeds(self, networkId: str, serial: str, **kwargs):
        """
        **Blink the LEDs on a device**
        https://developer.cisco.com/meraki/api/#!blink-network-device-leds
        
        - networkId (string)
        - serial (string)
        - duration (integer): The duration in seconds. Must be between 5 and 120. Default is 20 seconds
        - period (integer): The period in milliseconds. Must be between 100 and 1000. Default is 160 milliseconds
        - duty (integer): The duty cycle as the percent active. Must be between 10 and 90. Default is 50.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Devices'],
            'operation': 'blinkNetworkDeviceLeds',
        }
        resource = f'/networks/{networkId}/devices/{serial}/blinkLeds'

        body_params = ['duration', 'period', 'duty']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkDeviceLldp_cdp(self, networkId: str, serial: str, **kwargs):
        """
        **List LLDP and CDP information for a device**
        https://developer.cisco.com/meraki/api/#!get-network-device-lldp-_cdp
        
        - networkId (string)
        - serial (string)
        - timespan (integer): The timespan for which LLDP and CDP information will be fetched. Must be in seconds and less than or equal to a month (2592000 seconds). LLDP and CDP information is sent to the Meraki dashboard every 10 minutes. In instances where this LLDP and CDP information matches an existing entry in the Meraki dashboard, the data is updated once every two hours. Meraki recommends querying LLDP and CDP information at an interval slightly greater than two hours, to ensure that unchanged CDP / LLDP information can be queried consistently.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Devices'],
            'operation': 'getNetworkDeviceLldp_cdp',
        }
        resource = f'/networks/{networkId}/devices/{serial}/lldp_cdp'

        query_params = ['timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkDeviceLossAndLatencyHistory(self, networkId: str, serial: str, ip: str, **kwargs):
        """
        **Get the uplink loss percentage and latency in milliseconds for a wired network device.**
        https://developer.cisco.com/meraki/api/#!get-network-device-loss-and-latency-history
        
        - networkId (string)
        - serial (string)
        - ip (string): The destination IP used to obtain the requested stats. This is required.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
        - uplink (string): The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
        """

        kwargs.update(locals())

        if 'uplink' in kwargs:
            options = ['wan1', 'wan2', 'cellular']
            assert kwargs['uplink'] in options, f'''"uplink" cannot be "{kwargs['uplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Devices'],
            'operation': 'getNetworkDeviceLossAndLatencyHistory',
        }
        resource = f'/networks/{networkId}/devices/{serial}/lossAndLatencyHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'uplink', 'ip']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkDevicePerformance(self, networkId: str, serial: str):
        """
        **Return the performance score for a single device. Only primary MX devices supported. If no data is available, a 204 error code is returned.**
        https://developer.cisco.com/meraki/api/#!get-network-device-performance
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Devices'],
            'operation': 'getNetworkDevicePerformance',
        }
        resource = f'/networks/{networkId}/devices/{serial}/performance'

        return self._session.get(metadata, resource)

    def rebootNetworkDevice(self, networkId: str, serial: str):
        """
        **Reboot a device**
        https://developer.cisco.com/meraki/api/#!reboot-network-device
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Devices'],
            'operation': 'rebootNetworkDevice',
        }
        resource = f'/networks/{networkId}/devices/{serial}/reboot'

        return self._session.post(metadata, resource)

    def removeNetworkDevice(self, networkId: str, serial: str):
        """
        **Remove a single device**
        https://developer.cisco.com/meraki/api/#!remove-network-device
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Devices'],
            'operation': 'removeNetworkDevice',
        }
        resource = f'/networks/{networkId}/devices/{serial}/remove'

        return self._session.post(metadata, resource)

    def getNetworkDeviceUplink(self, networkId: str, serial: str):
        """
        **Return the uplink information for a device.**
        https://developer.cisco.com/meraki/api/#!get-network-device-uplink
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Devices'],
            'operation': 'getNetworkDeviceUplink',
        }
        resource = f'/networks/{networkId}/devices/{serial}/uplink'

        return self._session.get(metadata, resource)

    def getOrganizationDevices(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the devices in an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-devices
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Filter results by whether or not the device's configuration has been updated after the given timestamp
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Devices'],
            'operation': 'getOrganizationDevices',
        }
        resource = f'/organizations/{organizationId}/devices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


