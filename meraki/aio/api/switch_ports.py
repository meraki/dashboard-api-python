class SwitchPorts(object):
    def __init__(self, session):
        super(SwitchPorts, self).__init__()
        self._session = session
    
    def getDeviceSwitchPortStatuses(self, serial: str, **kwargs):
        """
        **Return the status for all the ports of a switch**
        https://api.meraki.com/api_docs#return-the-status-for-all-the-ports-of-a-switch
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getDeviceSwitchPorts(self, serial: str):
        """
        **List the switch ports for a switch**
        https://api.meraki.com/api_docs#list-the-switch-ports-for-a-switch
        
        - serial (string)
        """

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'getDeviceSwitchPorts',
        }
        resource = f'/devices/{serial}/switchPorts'

        return self._session.get(metadata, resource)

    def getDeviceSwitchPort(self, serial: str, number: str):
        """
        **Return a switch port**
        https://api.meraki.com/api_docs#return-a-switch-port
        
        - serial (string)
        - number (string)
        """

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'getDeviceSwitchPort',
        }
        resource = f'/devices/{serial}/switchPorts/{number}'

        return self._session.get(metadata, resource)

    def updateDeviceSwitchPort(self, serial: str, number: str, **kwargs):
        """
        **Update a switch port**
        https://api.meraki.com/api_docs#update-a-switch-port
        
        - serial (string)
        - number (string)
        - name (string): The name of the switch port
        - tags (string): The tags of the switch port
        - enabled (boolean): The status of the switch port
        - type (string): The type of the switch port ("access" or "trunk")
        - vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
        - poeEnabled (boolean): The PoE status of the switch port
        - isolationEnabled (boolean): The isolation status of the switch port
        - rstpEnabled (boolean): The rapid spanning tree protocol status
        - stpGuard (string): The state of the STP guard ("disabled", "Root guard", "BPDU guard", "Loop guard")
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

        if 'udld' in kwargs:
            options = ['Alert only', 'Enforce']
            assert kwargs['udld'] in options, f'''"udld" cannot be "{kwargs['udld']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Switch ports'],
            'operation': 'updateDeviceSwitchPort',
        }
        resource = f'/devices/{serial}/switchPorts/{number}'

        body_params = ['name', 'tags', 'enabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'poeEnabled', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'accessPolicyNumber', 'linkNegotiation', 'portScheduleId', 'udld', 'macWhitelist', 'stickyMacWhitelist', 'stickyMacWhitelistLimit', 'stormControlEnabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

