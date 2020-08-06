class SwitchSettings(object):
    def __init__(self, session):
        super(SwitchSettings, self).__init__()
        self._session = session
    
    def getNetworkSwitchSettings(self, networkId: str):
        """
        **Returns the switch network settings**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettings',
        }
        resource = f'/networks/{networkId}/switch/settings'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettings(self, networkId: str, **kwargs):
        """
        **Update switch network settings**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings
        
        - networkId (string)
        - vlan (integer): Management VLAN
        - useCombinedPower (boolean): The use Combined Power as the default behavior of secondary power supplies on supported devices.
        - powerExceptions (array): Exceptions on a per switch basis to "useCombinedPower"
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettings',
        }
        resource = f'/networks/{networkId}/switch/settings'

        body_params = ['vlan', 'useCombinedPower', 'powerExceptions']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsDhcpServerPolicy(self, networkId: str):
        """
        **Return the DHCP server policy**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-dhcp-server-policy
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsDhcpServerPolicy',
        }
        resource = f'/networks/{networkId}/switch/settings/dhcpServerPolicy'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsDhcpServerPolicy(self, networkId: str, **kwargs):
        """
        **Update the DHCP server policy**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-dhcp-server-policy
        
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
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsDhcpServerPolicy',
        }
        resource = f'/networks/{networkId}/switch/settings/dhcpServerPolicy'

        body_params = ['defaultPolicy', 'allowedServers', 'blockedServers']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsDscpToCosMappings(self, networkId: str):
        """
        **Return the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-dscp-to-cos-mappings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsDscpToCosMappings',
        }
        resource = f'/networks/{networkId}/switch/settings/dscpToCosMappings'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsDscpToCosMappings(self, networkId: str, mappings: list):
        """
        **Update the DSCP to CoS mappings**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-dscp-to-cos-mappings
        
        - networkId (string)
        - mappings (array): An array of DSCP to CoS mappings. An empty array will reset the mappings to default.
        """

        kwargs = locals()

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsDscpToCosMappings',
        }
        resource = f'/networks/{networkId}/switch/settings/dscpToCosMappings'

        body_params = ['mappings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsMtu(self, networkId: str):
        """
        **Return the MTU configuration**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-mtu
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsMtu',
        }
        resource = f'/networks/{networkId}/switch/settings/mtu'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsMtu(self, networkId: str, **kwargs):
        """
        **Update the MTU configuration**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-mtu
        
        - networkId (string)
        - defaultMtuSize (integer): MTU size for the entire network. Default value is 9578.
        - overrides (array): Override MTU size for individual switches or switch profiles. An empty array will clear overrides.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsMtu',
        }
        resource = f'/networks/{networkId}/switch/settings/mtu'

        body_params = ['defaultMtuSize', 'overrides']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsMulticast(self, networkId: str):
        """
        **Return multicast settings for a network**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-multicast
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsMulticast',
        }
        resource = f'/networks/{networkId}/switch/settings/multicast'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsMulticast(self, networkId: str, **kwargs):
        """
        **Update multicast settings for a network**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-multicast
        
        - networkId (string)
        - defaultSettings (object): Default multicast setting for entire network. IGMP snooping and Flood unknown multicast traffic settings are enabled by default.
        - overrides (array): Array of paired switches/stacks/profiles and corresponding multicast settings. An empty array will clear the multicast settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsMulticast',
        }
        resource = f'/networks/{networkId}/switch/settings/multicast'

        body_params = ['defaultSettings', 'overrides']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsQosRules(self, networkId: str):
        """
        **List quality of service rules**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-qos-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsQosRules',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules'

        return self._session.get(metadata, resource)

    def createNetworkSwitchSettingsQosRule(self, networkId: str, vlan: int, **kwargs):
        """
        **Add a quality of service rule**
        https://developer.cisco.com/meraki/api/#!create-network-switch-settings-qos-rule
        
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
            'tags': ['Switch settings'],
            'operation': 'createNetworkSwitchSettingsQosRule',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchSettingsQosRulesOrder(self, networkId: str):
        """
        **Return the quality of service rule IDs by order in which they will be processed by the switch**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-qos-rules-order
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsQosRulesOrder',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules/order'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsQosRulesOrder(self, networkId: str, ruleIds: list):
        """
        **Update the order in which the rules should be processed by the switch**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-qos-rules-order
        
        - networkId (string)
        - ruleIds (array): A list of quality of service rule IDs arranged in order in which they should be processed by the switch.
        """

        kwargs = locals()

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsQosRulesOrder',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules/order'

        body_params = ['ruleIds']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsQosRule(self, networkId: str, qosRuleId: str):
        """
        **Return a quality of service rule**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-qos-rule
        
        - networkId (string)
        - qosRuleId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsQosRule',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules/{qosRuleId}'

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchSettingsQosRule(self, networkId: str, qosRuleId: str):
        """
        **Delete a quality of service rule**
        https://developer.cisco.com/meraki/api/#!delete-network-switch-settings-qos-rule
        
        - networkId (string)
        - qosRuleId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'deleteNetworkSwitchSettingsQosRule',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules/{qosRuleId}'

        return self._session.delete(metadata, resource)

    def updateNetworkSwitchSettingsQosRule(self, networkId: str, qosRuleId: str, **kwargs):
        """
        **Update a quality of service rule**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-qos-rule
        
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
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsQosRule',
        }
        resource = f'/networks/{networkId}/switch/settings/qosRules/{qosRuleId}'

        body_params = ['vlan', 'protocol', 'srcPort', 'srcPortRange', 'dstPort', 'dstPortRange', 'dscp']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsStormControl(self, networkId: str):
        """
        **Return the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-storm-control
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsStormControl',
        }
        resource = f'/networks/{networkId}/switch/settings/stormControl'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsStormControl(self, networkId: str, **kwargs):
        """
        **Update the storm control configuration for a switch network**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-storm-control
        
        - networkId (string)
        - broadcastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for broadcast traffic type. Default value 100 percent rate is to clear the configuration.
        - multicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for multicast traffic type. Default value 100 percent rate is to clear the configuration.
        - unknownUnicastThreshold (integer): Percentage (1 to 99) of total available port bandwidth for unknown unicast (dlf-destination lookup failure) traffic type. Default value 100 percent rate is to clear the configuration.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsStormControl',
        }
        resource = f'/networks/{networkId}/switch/settings/stormControl'

        body_params = ['broadcastThreshold', 'multicastThreshold', 'unknownUnicastThreshold']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSwitchSettingsStp(self, networkId: str):
        """
        **Returns STP settings**
        https://developer.cisco.com/meraki/api/#!get-network-switch-settings-stp
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'getNetworkSwitchSettingsStp',
        }
        resource = f'/networks/{networkId}/switch/settings/stp'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchSettingsStp(self, networkId: str, **kwargs):
        """
        **Updates STP settings**
        https://developer.cisco.com/meraki/api/#!update-network-switch-settings-stp
        
        - networkId (string)
        - rstpEnabled (boolean): The spanning tree protocol status in network
        - stpBridgePriority (array): STP bridge priority for switches/stacks or switch profiles. An empty array will clear the STP bridge priority settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Switch settings'],
            'operation': 'updateNetworkSwitchSettingsStp',
        }
        resource = f'/networks/{networkId}/switch/settings/stp'

        body_params = ['rstpEnabled', 'stpBridgePriority']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

