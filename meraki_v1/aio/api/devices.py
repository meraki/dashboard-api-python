class AsyncDevices:
    def __init__(self, session):
        super().__init__()
        self._session = session

    async def getDevice(self, serial: str):
        """
        **Return a single device**
        https://developer.cisco.com/meraki/api-v1/#!get-device
        
        - serial (string)
        """

        metadata = {
            'tags': ['devices', 'configure'],
            'operation': 'getDevice',
        }
        resource = f'/devices/{serial}'

        return await self._session.get(metadata, resource)

    async def updateDevice(self, serial: str, **kwargs):
        """
        **Update the attributes of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device
        
        - serial (string)
        - name (string): The name of a device
        - tags (array): The list of tags of a device
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
            'tags': ['devices', 'configure'],
            'operation': 'updateDevice',
        }
        resource = f'/devices/{serial}'

        body_params = ['name', 'tags', 'lat', 'lng', 'address', 'notes', 'moveMapMarker', 'switchProfileId', 'floorPlanId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def blinkDeviceLeds(self, serial: str, **kwargs):
        """
        **Blink the LEDs on a device**
        https://developer.cisco.com/meraki/api-v1/#!blink-device-leds
        
        - serial (string)
        - duration (integer): The duration in seconds. Must be between 5 and 120. Default is 20 seconds
        - period (integer): The period in milliseconds. Must be between 100 and 1000. Default is 160 milliseconds
        - duty (integer): The duty cycle as the percent active. Must be between 10 and 90. Default is 50.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'liveTools'],
            'operation': 'blinkDeviceLeds',
        }
        resource = f'/devices/{serial}/blinkLeds'

        body_params = ['duration', 'period', 'duty']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getDeviceClients(self, serial: str, **kwargs):
        """
        **List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-clients
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'monitor', 'clients'],
            'operation': 'getDeviceClients',
        }
        resource = f'/devices/{serial}/clients'

        query_params = ['t0', 'timespan']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceLldpCdp(self, serial: str, **kwargs):
        """
        **List LLDP and CDP information for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-lldp-cdp
        
        - serial (string)
        - timespan (integer): The timespan for which LLDP and CDP information will be fetched. Must be in seconds and less than or equal to a month (2592000 seconds). LLDP and CDP information is sent to the Meraki dashboard every 10 minutes. In instances where this LLDP and CDP information matches an existing entry in the Meraki dashboard, the data is updated once every two hours. Meraki recommends querying LLDP and CDP information at an interval slightly greater than two hours, to ensure that unchanged CDP / LLDP information can be queried consistently.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'monitor', 'lldpCdp'],
            'operation': 'getDeviceLldpCdp',
        }
        resource = f'/devices/{serial}/lldpCdp'

        query_params = ['timespan']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceLossAndLatencyHistory(self, serial: str, ip: str, **kwargs):
        """
        **Get the uplink loss percentage and latency in milliseconds for a wired network device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history
        
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
            'tags': ['devices', 'monitor', 'lossAndLatencyHistory'],
            'operation': 'getDeviceLossAndLatencyHistory',
        }
        resource = f'/devices/{serial}/lossAndLatencyHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'uplink', 'ip']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceManagementInterface(self, serial: str):
        """
        **Return the management interface settings for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface
        
        - serial (string)
        """

        metadata = {
            'tags': ['devices', 'configure', 'managementInterface'],
            'operation': 'getDeviceManagementInterface',
        }
        resource = f'/devices/{serial}/managementInterface'

        return await self._session.get(metadata, resource)

    async def updateDeviceManagementInterface(self, serial: str, **kwargs):
        """
        **Update the management interface settings for a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface
        
        - serial (string)
        - wan1 (object): WAN 1 settings
        - wan2 (object): WAN 2 settings (only for MX devices)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'configure', 'managementInterface'],
            'operation': 'updateDeviceManagementInterface',
        }
        resource = f'/devices/{serial}/managementInterface'

        body_params = ['wan1', 'wan2']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def rebootDevice(self, serial: str):
        """
        **Reboot a device**
        https://developer.cisco.com/meraki/api-v1/#!reboot-device
        
        - serial (string)
        """

        metadata = {
            'tags': ['devices', 'liveTools'],
            'operation': 'rebootDevice',
        }
        resource = f'/devices/{serial}/reboot'

        return await self._session.post(metadata, resource)

    async def getDeviceUplink(self, serial: str):
        """
        **Return the uplink information for a device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-uplink
        
        - serial (string)
        """

        metadata = {
            'tags': ['devices', 'monitor', 'uplink'],
            'operation': 'getDeviceUplink',
        }
        resource = f'/devices/{serial}/uplink'

        return await self._session.get(metadata, resource)

