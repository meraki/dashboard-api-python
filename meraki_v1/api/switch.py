class Switch(object):
    def __init__(self, session):
        super(Switch, self).__init__()
        self._session = session

    def getDeviceSwitchPorts(self, serial: str):
        """
        **List the switch ports for a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports
        
        - serial (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'ports'],
            'operation': 'getDeviceSwitchPorts',
        }
        resource = f'/devices/{serial}/switch/ports'

        return self._session.get(metadata, resource)

    def cycleDeviceSwitchPorts(self, serial: str, ports: list):
        """
        **Cycle a set of switch ports**
        https://developer.cisco.com/meraki/api-v1/#!cycle-device-switch-ports
        
        - serial (string)
        - ports (array): List of switch ports. Example: [1, 2-5, 1_MA-MOD-8X10G_1, 1_MA-MOD-8X10G_2-1_MA-MOD-8X10G_8]
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'liveTools', 'ports'],
            'operation': 'cycleDeviceSwitchPorts',
        }
        resource = f'/devices/{serial}/switch/ports/cycle'

        body_params = ['ports']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getDeviceSwitchPortsStatuses(self, serial: str, **kwargs):
        """
        **Return the status for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'monitor', 'ports', 'statuses'],
            'operation': 'getDeviceSwitchPortsStatuses',
        }
        resource = f'/devices/{serial}/switch/ports/statuses'

        query_params = ['t0', 'timespan']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getDeviceSwitchPortsStatusesPackets(self, serial: str, **kwargs):
        """
        **Return the packet counters for all the ports of a switch**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-ports-statuses-packets
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'monitor', 'ports', 'statuses', 'packets'],
            'operation': 'getDeviceSwitchPortsStatusesPackets',
        }
        resource = f'/devices/{serial}/switch/ports/statuses/packets'

        query_params = ['t0', 'timespan']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getDeviceSwitchPort(self, serial: str, portId: str):
        """
        **Return a switch port**
        https://developer.cisco.com/meraki/api-v1/#!get-device-switch-port
        
        - serial (string)
        - portId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'ports'],
            'operation': 'getDeviceSwitchPort',
        }
        resource = f'/devices/{serial}/switch/ports/{portId}'

        return self._session.get(metadata, resource)

    def updateDeviceSwitchPort(self, serial: str, portId: str, **kwargs):
        """
        **Update a switch port**
        https://developer.cisco.com/meraki/api-v1/#!update-device-switch-port
        
        - serial (string)
        - portId (string)
        - name (string): The name of the switch port
        - tags (array): The list of tags of the switch port
        - enabled (boolean): The status of the switch port
        - type (string): The type of the switch port ('trunk' or 'access')
        - vlan (integer): The VLAN of the switch port. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch port. Only applicable to access ports.
        - allowedVlans (string): The VLANs allowed on the switch port. Only applicable to trunk ports.
        - poeEnabled (boolean): The PoE status of the switch port
        - isolationEnabled (boolean): The isolation status of the switch port
        - rstpEnabled (boolean): The rapid spanning tree protocol status
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
        - linkNegotiation (string): The link speed for the switch port
        - portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
        - udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
        - accessPolicyType (string): The type of the access policy of the switch port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC whitelist' or 'Sticky MAC whitelist'
        - accessPolicyNumber (integer): The number of a custom access policy to configure on the switch port. Only applicable when 'accessPolicyType' is 'Custom access policy'
        - macWhitelist (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC whitelist'
        - stickyMacWhitelist (array): The initial list of MAC addresses for sticky Mac whitelist. Only applicable when 'accessPolicyType' is 'Sticky MAC whitelist'
        - stickyMacWhitelistLimit (integer): The maximum number of MAC addresses for sticky MAC whitelist. Only applicable when 'accessPolicyType' is 'Sticky MAC whitelist'
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
        if 'accessPolicyType' in kwargs:
            options = ['Open', 'Custom access policy', 'MAC whitelist', 'Sticky MAC whitelist']
            assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'ports'],
            'operation': 'updateDeviceSwitchPort',
        }
        resource = f'/devices/{serial}/switch/ports/{portId}'

        body_params = ['name', 'tags', 'enabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'poeEnabled', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macWhitelist', 'stickyMacWhitelist', 'stickyMacWhitelistLimit', 'stormControlEnabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchAccessControlLists(self, networkId: str):
        """
        **Return the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-control-lists
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'accessControlLists'],
            'operation': 'getNetworkSwitchAccessControlLists',
        }
        resource = f'/networks/{networkId}/switch/accessControlLists'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchAccessControlLists(self, networkId: str, rules: list):
        """
        **Update the access control lists for a MS network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-control-lists
        
        - networkId (string)
        - rules (array): An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'accessControlLists'],
            'operation': 'updateNetworkSwitchAccessControlLists',
        }
        resource = f'/networks/{networkId}/switch/accessControlLists'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchAccessPolicies(self, networkId: str):
        """
        **List the access policies for this network. Only valid for MS networks.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-access-policies
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'accessPolicies'],
            'operation': 'getNetworkSwitchAccessPolicies',
        }
        resource = f'/networks/{networkId}/switch/accessPolicies'

        return self._session.get(metadata, resource)

    def getNetworkSwitchDhcpServerPolicy(self, networkId: str):
        """
        **Return the DHCP server policy**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dhcp-server-policy
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy'],
            'operation': 'getNetworkSwitchDhcpServerPolicy',
        }
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchDhcpServerPolicy(self, networkId: str, **kwargs):
        """
        **Update the DHCP server policy**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dhcp-server-policy
        
        - networkId (string)
        - defaultPolicy (string): 'allow' or 'block' new DHCP servers. Default value is 'allow'.
        - allowedServers (array): List the MAC addresses of DHCP servers to permit on the network. Applicable only if defaultPolicy is set to block. An empty array will clear the entries.
        - blockedServers (array): List the MAC addresses of DHCP servers to block on the network. Applicable only if defaultPolicy is set to allow. An empty array will clear the entries.
        """

        kwargs.update(locals())

        if 'defaultPolicy' in kwargs:
            options = ['allow', 'block']
            assert kwargs['defaultPolicy'] in options, f'''"defaultPolicy" cannot be "{kwargs['defaultPolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'dhcpServerPolicy'],
            'operation': 'updateNetworkSwitchDhcpServerPolicy',
        }
        resource = f'/networks/{networkId}/switch/dhcpServerPolicy'

        body_params = ['defaultPolicy', 'allowedServers', 'blockedServers']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchDscpToCosMappings(self, networkId: str):
        """
        **Return the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-dscp-to-cos-mappings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'dscpToCosMappings'],
            'operation': 'getNetworkSwitchDscpToCosMappings',
        }
        resource = f'/networks/{networkId}/switch/dscpToCosMappings'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchDscpToCosMappings(self, networkId: str, mappings: list):
        """
        **Update the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-dscp-to-cos-mappings
        
        - networkId (string)
        - mappings (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'dscpToCosMappings'],
            'operation': 'updateNetworkSwitchDscpToCosMappings',
        }
        resource = f'/networks/{networkId}/switch/dscpToCosMappings'

        body_params = ['mappings']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchLinkAggregations(self, networkId: str):
        """
        **List link aggregation groups**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-link-aggregations
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'getNetworkSwitchLinkAggregations',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations'

        return self._session.get(metadata, resource)

    def createNetworkSwitchLinkAggregation(self, networkId: str, **kwargs):
        """
        **Create a link aggregation group**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-link-aggregation
        
        - networkId (string)
        - switchPorts (array): Array of switch or stack ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for creating aggregation group. Minimum 2 and maximum 8 ports are supported.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'createNetworkSwitchLinkAggregation',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations'

        body_params = ['switchPorts', 'switchProfilePorts']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def updateNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str, **kwargs):
        """
        **Update a link aggregation group**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-link-aggregation
        
        - networkId (string)
        - linkAggregationId (string)
        - switchPorts (array): Array of switch or stack ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
        - switchProfilePorts (array): Array of switch profile ports for updating aggregation group. Minimum 2 and maximum 8 ports are supported.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'updateNetworkSwitchLinkAggregation',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        body_params = ['switchPorts', 'switchProfilePorts']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSwitchLinkAggregation(self, networkId: str, linkAggregationId: str):
        """
        **Split a link aggregation group into separate ports**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-link-aggregation
        
        - networkId (string)
        - linkAggregationId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'linkAggregations'],
            'operation': 'deleteNetworkSwitchLinkAggregation',
        }
        resource = f'/networks/{networkId}/switch/linkAggregations/{linkAggregationId}'

        return self._session.delete(metadata, resource)

    def getNetworkSwitchMtu(self, networkId: str):
        """
        **Return the MTU configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-mtu
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'mtu'],
            'operation': 'getNetworkSwitchMtu',
        }
        resource = f'/networks/{networkId}/switch/mtu'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchMtu(self, networkId: str, **kwargs):
        """
        **Update the MTU configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-mtu
        
        - networkId (string)
        - defaultMtuSize (integer): MTU size for the entire network. Default value is 9578.
        - overrides (array): Override MTU size for individual switches or switch profiles. An empty array will clear overrides.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'mtu'],
            'operation': 'updateNetworkSwitchMtu',
        }
        resource = f'/networks/{networkId}/switch/mtu'

        body_params = ['defaultMtuSize', 'overrides']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchPortSchedules(self, networkId: str):
        """
        **List switch port schedules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-port-schedules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'getNetworkSwitchPortSchedules',
        }
        resource = f'/networks/{networkId}/switch/portSchedules'

        return self._session.get(metadata, resource)

    def createNetworkSwitchPortSchedule(self, networkId: str, name: str, **kwargs):
        """
        **Add a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-port-schedule
        
        - networkId (string)
        - name (string): The name for your port schedule. Required
        - portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
    When it's empty, default schedule with all days of a week are configured.
    Any unspecified day in the schedule is added as a default schedule configuration of the day.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'createNetworkSwitchPortSchedule',
        }
        resource = f'/networks/{networkId}/switch/portSchedules'

        body_params = ['name', 'portSchedule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def deleteNetworkSwitchPortSchedule(self, networkId: str, portScheduleId: str):
        """
        **Delete a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule
        
        - networkId (string)
        - portScheduleId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'deleteNetworkSwitchPortSchedule',
        }
        resource = f'/networks/{networkId}/switch/portSchedules/{portScheduleId}'

        return self._session.delete(metadata, resource)

    def updateNetworkSwitchPortSchedule(self, networkId: str, portScheduleId: str, **kwargs):
        """
        **Update a switch port schedule**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule
        
        - networkId (string)
        - portScheduleId (string)
        - name (string): The name for your port schedule.
        - portSchedule (object):     The schedule for switch port scheduling. Schedules are applied to days of the week.
    When it's empty, default schedule with all days of a week are configured.
    Any unspecified day in the schedule is added as a default schedule configuration of the day.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'portSchedules'],
            'operation': 'updateNetworkSwitchPortSchedule',
        }
        resource = f'/networks/{networkId}/switch/portSchedules/{portScheduleId}'

        body_params = ['name', 'portSchedule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchQosRules(self, networkId: str):
        """
        **List quality of service rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'getNetworkSwitchQosRules',
        }
        resource = f'/networks/{networkId}/switch/qosRules'

        return self._session.get(metadata, resource)

    def createNetworkSwitchQosRule(self, networkId: str, vlan: int, **kwargs):
        """
        **Add a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-qos-rule
        
        - networkId (string)
        - vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
        - protocol (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY"
        - srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dscp (integer): DSCP tag. Set this to -1 to trust incoming DSCP. Default value is 0
        """

        kwargs.update(locals())

        if 'protocol' in kwargs:
            options = ['ANY', 'TCP', 'UDP']
            assert kwargs['protocol'] in options, f'''"protocol" cannot be "{kwargs['protocol']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'createNetworkSwitchQosRule',
        }
        resource = f'/networks/{networkId}/switch/qosRules'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchQosRulesOrder(self, networkId: str):
        """
        **Return the quality of service rule IDs by order in which they will be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rules-order
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules', 'order'],
            'operation': 'getNetworkSwitchQosRulesOrder',
        }
        resource = f'/networks/{networkId}/switch/qosRules/order'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchQosRulesOrder(self, networkId: str, ruleIds: list):
        """
        **Update the order in which the rules should be processed by the switch**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rules-order
        
        - networkId (string)
        - ruleIds (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'qosRules', 'order'],
            'operation': 'updateNetworkSwitchQosRulesOrder',
        }
        resource = f'/networks/{networkId}/switch/qosRules/order'

        body_params = ['ruleIds']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Return a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-qos-rule
        
        - networkId (string)
        - qosRuleId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'getNetworkSwitchQosRule',
        }
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchQosRule(self, networkId: str, qosRuleId: str):
        """
        **Delete a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-qos-rule
        
        - networkId (string)
        - qosRuleId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'deleteNetworkSwitchQosRule',
        }
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        return self._session.delete(metadata, resource)

    def updateNetworkSwitchQosRule(self, networkId: str, qosRuleId: str, **kwargs):
        """
        **Update a quality of service rule**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-qos-rule
        
        - networkId (string)
        - qosRuleId (string)
        - vlan (integer): The VLAN of the incoming packet. A null value will match any VLAN.
        - protocol (string): The protocol of the incoming packet. Can be one of "ANY", "TCP" or "UDP". Default value is "ANY".
        - srcPort (integer): The source port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - srcPortRange (string): The source port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dstPort (integer): The destination port of the incoming packet. Applicable only if protocol is TCP or UDP.
        - dstPortRange (string): The destination port range of the incoming packet. Applicable only if protocol is set to TCP or UDP. Example: 70-80
        - dscp (integer): DSCP tag that should be assigned to incoming packet. Set this to -1 to trust incoming DSCP. Default value is 0.
        """

        kwargs.update(locals())

        if 'protocol' in kwargs:
            options = ['ANY', 'TCP', 'UDP']
            assert kwargs['protocol'] in options, f'''"protocol" cannot be "{kwargs['protocol']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'qosRules'],
            'operation': 'updateNetworkSwitchQosRule',
        }
        resource = f'/networks/{networkId}/switch/qosRules/{qosRuleId}'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchRoutingMulticast(self, networkId: str):
        """
        **Return multicast settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-routing-multicast
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast'],
            'operation': 'getNetworkSwitchRoutingMulticast',
        }
        resource = f'/networks/{networkId}/switch/routing/multicast'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchRoutingMulticast(self, networkId: str, **kwargs):
        """
        **Update multicast settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-routing-multicast
        
        - networkId (string)
        - defaultSettings (object): Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
        - overrides (array): Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'routing', 'multicast'],
            'operation': 'updateNetworkSwitchRoutingMulticast',
        }
        resource = f'/networks/{networkId}/switch/routing/multicast'

        body_params = ['defaultSettings', 'overrides']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettings(self, networkId: str):
        """
        **Returns the switch network settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'settings'],
            'operation': 'getNetworkSwitchSettings',
        }
        resource = f'/networks/{networkId}/switch/settings'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettings(self, networkId: str, **kwargs):
        """
        **Update switch network settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-settings
        
        - networkId (string)
        - vlan (integer): Management VLAN
        - useCombinedPower (boolean): The use Combined Power as the default behavior of secondary power supplies on supported devices.
        - powerExceptions (array): Exceptions on a per switch basis to "useCombinedPower"
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'settings'],
            'operation': 'updateNetworkSwitchSettings',
        }
        resource = f'/networks/{networkId}/switch/settings'

        body_params = ['vlan', 'useCombinedPower', 'powerExceptions']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchStormControl(self, networkId: str):
        """
        **Return the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-storm-control
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'stormControl'],
            'operation': 'getNetworkSwitchStormControl',
        }
        resource = f'/networks/{networkId}/switch/stormControl'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchStormControl(self, networkId: str, **kwargs):
        """
        **Update the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-storm-control
        
        - networkId (string)
        - broadcastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
        - multicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
        - unknownUnicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stormControl'],
            'operation': 'updateNetworkSwitchStormControl',
        }
        resource = f'/networks/{networkId}/switch/stormControl'

        body_params = ['broadcastThreshold', 'multicastThreshold', 'unknownUnicastThreshold']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchStp(self, networkId: str):
        """
        **Returns STP settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-stp
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'stp'],
            'operation': 'getNetworkSwitchStp',
        }
        resource = f'/networks/{networkId}/switch/stp'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchStp(self, networkId: str, **kwargs):
        """
        **Updates STP settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stp
        
        - networkId (string)
        - rstpEnabled (boolean): The spanning tree protocol status in network
        - stpBridgePriority (array): STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['switch', 'configure', 'stp'],
            'operation': 'updateNetworkSwitchStp',
        }
        resource = f'/networks/{networkId}/switch/stp'

        body_params = ['rstpEnabled', 'stpBridgePriority']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSwitchStacks(self, networkId: str):
        """
        **List the switch stacks in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-switch-stacks
        
        - networkId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'switchStacks'],
            'operation': 'getNetworkSwitchSwitchStacks',
        }
        resource = f'/networks/{networkId}/switch/switchStacks'

        return self._session.get(metadata, resource)

    def createNetworkSwitchSwitchStack(self, networkId: str, name: str, serials: list):
        """
        **Create a stack**
        https://developer.cisco.com/meraki/api-v1/#!create-network-switch-switch-stack
        
        - networkId (string)
        - name (string): The name of the new stack
        - serials (array): An array of switch serials to be added into the new stack
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'switchStacks'],
            'operation': 'createNetworkSwitchSwitchStack',
        }
        resource = f'/networks/{networkId}/switch/switchStacks'

        body_params = ['name', 'serials']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Show a switch stack**
        https://developer.cisco.com/meraki/api-v1/#!get-network-switch-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'switchStacks'],
            'operation': 'getNetworkSwitchSwitchStack',
        }
        resource = f'/networks/{networkId}/switch/switchStacks/{switchStackId}'

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Delete a stack**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'switchStacks'],
            'operation': 'deleteNetworkSwitchSwitchStack',
        }
        resource = f'/networks/{networkId}/switch/switchStacks/{switchStackId}'

        return self._session.delete(metadata, resource)

    def addNetworkSwitchSwitchStack(self, networkId: str, switchStackId: str, serial: str):
        """
        **Add a switch to a stack**
        https://developer.cisco.com/meraki/api-v1/#!add-network-switch-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        - serial (string): The serial of the switch to be added
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'switchStacks'],
            'operation': 'addNetworkSwitchSwitchStack',
        }
        resource = f'/networks/{networkId}/switch/switchStacks/{switchStackId}/add'

        body_params = ['serial']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def removeNetworkSwitchSwitchStack(self, networkId: str, switchStackId: str, serial: str):
        """
        **Remove a switch from a stack**
        https://developer.cisco.com/meraki/api-v1/#!remove-network-switch-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        - serial (string): The serial of the switch to be removed
        """

        kwargs = locals()

        metadata = {
            'tags': ['switch', 'configure', 'switchStacks'],
            'operation': 'removeNetworkSwitchSwitchStack',
        }
        resource = f'/networks/{networkId}/switch/switchStacks/{switchStackId}/remove'

        body_params = ['serial']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getOrganizationConfigTemplateSwitchProfiles(self, organizationId: str, configTemplateId: str):
        """
        **List the switch profiles for your switch template configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profiles
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles'],
            'operation': 'getOrganizationConfigTemplateSwitchProfiles',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles'

        return self._session.get(metadata, resource)

    def getOrganizationConfigTemplateSwitchProfilePorts(self, organizationId: str, configTemplateId: str, profileId: str):
        """
        **Return all the ports of a switch profile**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-ports
        
        - organizationId (string)
        - configTemplateId (string)
        - profileId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
            'operation': 'getOrganizationConfigTemplateSwitchProfilePorts',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports'

        return self._session.get(metadata, resource)

    def getOrganizationConfigTemplateSwitchProfilePort(self, organizationId: str, configTemplateId: str, profileId: str, portId: str):
        """
        **Return a switch profile port**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template-switch-profile-port
        
        - organizationId (string)
        - configTemplateId (string)
        - profileId (string)
        - portId (string)
        """

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
            'operation': 'getOrganizationConfigTemplateSwitchProfilePort',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}'

        return self._session.get(metadata, resource)

    def updateOrganizationConfigTemplateSwitchProfilePort(self, organizationId: str, configTemplateId: str, profileId: str, portId: str, **kwargs):
        """
        **Update a switch profile port**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template-switch-profile-port
        
        - organizationId (string)
        - configTemplateId (string)
        - profileId (string)
        - portId (string)
        - name (string): The name of the switch profile port
        - tags (array): The list of tags of the switch profile port
        - enabled (boolean): The status of the switch profile port
        - type (string): The type of the switch profile port ('trunk' or 'access')
        - vlan (integer): The VLAN of the switch profile port. A null value will clear the value set for trunk ports.
        - voiceVlan (integer): The voice VLAN of the switch profile port. Only applicable to access ports
        - allowedVlans (string): The VLANs allowed on the switch profile port. Only applicable to trunk ports
        - poeEnabled (boolean): The PoE status of the switch profile port
        - isolationEnabled (boolean): The isolation status of the switch profile port
        - rstpEnabled (boolean): The rapid spanning tree protocol status
        - stpGuard (string): The state of the STP guard ('disabled', 'root guard', 'bpdu guard' or 'loop guard')
        - linkNegotiation (string): The link speed for the switch profile port
        - portScheduleId (string): The ID of the port schedule. A value of null will clear the port schedule.
        - udld (string): The action to take when Unidirectional Link is detected (Alert only, Enforce). Default configuration is Alert only.
        - accessPolicyType (string): The type of the access policy of the switch profile port. Only applicable to access ports. Can be one of 'Open', 'Custom access policy', 'MAC whitelist' or 'Sticky MAC whitelist'
        - accessPolicyNumber (integer): The number of a custom access policy to configure on the switch profile port. Only applicable when 'accessPolicyType' is 'Custom access policy'
        - macWhitelist (array): Only devices with MAC addresses specified in this list will have access to this port. Up to 20 MAC addresses can be defined. Only applicable when 'accessPolicyType' is 'MAC whitelist'
        - stickyMacWhitelist (array): The initial list of MAC addresses for sticky Mac whitelist. Only applicable when 'accessPolicyType' is 'Sticky MAC whitelist'
        - stickyMacWhitelistLimit (integer): The maximum number of MAC addresses for sticky MAC whitelist. Only applicable when 'accessPolicyType' is 'Sticky MAC whitelist'
        - stormControlEnabled (boolean): The storm control status of the switch profile port
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
        if 'accessPolicyType' in kwargs:
            options = ['Open', 'Custom access policy', 'MAC whitelist', 'Sticky MAC whitelist']
            assert kwargs['accessPolicyType'] in options, f'''"accessPolicyType" cannot be "{kwargs['accessPolicyType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['switch', 'configure', 'configTemplates', 'profiles', 'ports'],
            'operation': 'updateOrganizationConfigTemplateSwitchProfilePort',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}'

        body_params = ['name', 'tags', 'enabled', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'poeEnabled', 'isolationEnabled', 'rstpEnabled', 'stpGuard', 'linkNegotiation', 'portScheduleId', 'udld', 'accessPolicyType', 'accessPolicyNumber', 'macWhitelist', 'stickyMacWhitelist', 'stickyMacWhitelistLimit', 'stormControlEnabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

