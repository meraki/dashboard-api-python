class AsyncSwitchPorts:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getDeviceSwitchPortStatuses(self, serial: str, **kwargs):
        """
        **Return the status for all the ports of a switch**
        https://developer.cisco.com/meraki/api/#!get-device-switch-port-statuses
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'getDeviceSwitchPortStatuses',
        }
        resource = f'/devices/{serial}/switchPortStatuses'

        query_params = ['t0', 'timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceSwitchPortStatusesPackets(self, serial: str, **kwargs):
        """
        **Return the packet counters for all the ports of a switch**
        https://developer.cisco.com/meraki/api/#!get-device-switch-port-statuses-packets
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'getDeviceSwitchPortStatusesPackets',
        }
        resource = f'/devices/{serial}/switchPortStatuses/packets'

        query_params = ['t0', 'timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceSwitchPorts(self, serial: str):
        """
        **List the switch ports for a switch**
        https://developer.cisco.com/meraki/api/#!get-device-switch-ports
        
        - serial (string)
        """

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'getDeviceSwitchPorts',
        }
        resource = f'/devices/{serial}/switchPorts'

        return await self._session.get(metadata, resource)

    async def getDeviceSwitchPort(self, serial: str, number: str):
        """
        **Return a switch port**
        https://developer.cisco.com/meraki/api/#!get-device-switch-port
        
        - serial (string)
        - number (string)
        """

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'getDeviceSwitchPort',
        }
        resource = f'/devices/{serial}/switchPorts/{number}'

        return await self._session.get(metadata, resource)

    async def updateDeviceSwitchPort(self, serial: str, number: str, **kwargs):
        """
        **Update a switch port**
        https://developer.cisco.com/meraki/api/#!update-device-switch-port
        
        - serial (string)
        - number (string)
        - name (string): The name of the switch port
        - tags (string): The tags of the switch port
        - enabled (boolean): The status of the switch port
        - type (string): The type of the switch port ('trunk' or 'access')
        - vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
        - poeEnabled (boolean): The PoE status of the switch port
        - isolationEnabled (boolean): The isolation status of the switch port
        - rstpEnabled (boolean): The rapid spanning tree protocol status
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
        - accessPolicyNumber (integer): The number of the access policy of the switch port. Only applicable to access ports.
        - linkNegotiation (string): The link speed for the switch port
        - portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
        - udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
        - macWhitelist (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. To disable MAC whitelist, set accessPolicyNumber to null.
        - stickyMacWhitelist (array): The initial list of MAC addresses for sticky Mac whitelist. To reset Sticky MAC whitelist, set accessPolicyNumber to null.
        - stickyMacWhitelistLimit (integer): The maximum number of MAC addresses for sticky MAC whitelist.
        - stormControlEnabled (boolean): The storm control status of the switch port
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['trunk', 'access']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''
        if 'stpGuard' in kwargs:
            options = ['disabled', 'root guard', 'bpdu guard', 'loop guard']
            assert kwargs['stpGuard'] in options, f'''"stpGuard" cannot be "{kwargs['stpGuard']}", & must be set to one of: {options}'''
        if 'udld' in kwargs:
            options = ['Alert only', 'Enforce']
            assert kwargs['udld'] in options, f'''"udld" cannot be "{kwargs['udld']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'updateDeviceSwitchPort',
        }
        resource = f'/devices/{serial}/switchPorts/{number}'

        body_params = ['name', 'tags', 'enabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'poeEnabled', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'accessPolicyNumber', 'linkNegotiation', 'portScheduleId', 'udld', 'macWhitelist', 'stickyMacWhitelist', 'stickyMacWhitelistLimit', 'stormControlEnabled']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

