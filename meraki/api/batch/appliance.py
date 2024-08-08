import urllib


class ActionBatchAppliance(object):
    def __init__(self):
        super(ActionBatchAppliance, self).__init__()
        


    def updateDeviceApplianceRadioSettings(self, serial: str, **kwargs):
        """
        **Update the radio settings of an appliance**
        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-radio-settings

        - serial (string): Serial
        - rfProfileId (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
        - twoFourGhzSettings (object): Manual radio settings for 2.4 GHz.
        - fiveGhzSettings (object): Manual radio settings for 5 GHz.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'radio', 'settings'],
            'operation': 'updateDeviceApplianceRadioSettings'
        }
        resource = f'/devices/{serial}/appliance/radio/settings'

        body_params = ['rfProfileId', 'twoFourGhzSettings', 'fiveGhzSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateDeviceApplianceUplinksSettings(self, serial: str, interfaces: dict):
        """
        **Update the uplink settings for an MX appliance**
        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings

        - serial (string): Serial
        - interfaces (object): Interface settings.
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'uplinks', 'settings'],
            'operation': 'updateDeviceApplianceUplinksSettings'
        }
        resource = f'/devices/{serial}/appliance/uplinks/settings'

        body_params = ['interfaces', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createDeviceApplianceVmxAuthenticationToken(self, serial: str):
        """
        **Generate a new vMX authentication token**
        https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-vmx-authentication-token

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vmx', 'authenticationToken'],
            'operation': 'createDeviceApplianceVmxAuthenticationToken'
        }
        resource = f'/devices/{serial}/appliance/vmx/authenticationToken'

        action = {
            "resource": resource,
            "operation": "create",
        }
        return action
        





    def updateNetworkApplianceConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

        - networkId (string): Network ID
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'updateNetworkApplianceConnectivityMonitoringDestinations'
        }
        resource = f'/networks/{networkId}/appliance/connectivityMonitoringDestinations'

        body_params = ['destinations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceFirewallL7FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

        - networkId (string): Network ID
        - rules (array): An ordered array of the MX L7 firewall rules
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules'],
            'operation': 'updateNetworkApplianceFirewallL7FirewallRules'
        }
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkAppliancePort(self, networkId: str, portId: str, **kwargs):
        """
        **Update the per-port VLAN settings for a single MX port.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

        - networkId (string): Network ID
        - portId (string): Port ID
        - enabled (boolean): The status of the port
        - dropUntaggedTraffic (boolean): Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true.
        - type (string): The type of the port: 'access' or 'trunk'.
        - vlan (integer): Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode.
        - allowedVlans (string): Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to permit all VLAN's on the port.
        - accessPolicy (string): The name of the policy. Only applicable to Access ports. Valid values are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, 'open' is the only valid value and 'open' is the default value if the field is missing.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'ports'],
            'operation': 'updateNetworkAppliancePort'
        }
        resource = f'/networks/{networkId}/appliance/ports/{portId}'

        body_params = ['enabled', 'dropUntaggedTraffic', 'type', 'vlan', 'allowedVlans', 'accessPolicy', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, prefix: str, origin: dict, **kwargs):
        """
        **Add a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - prefix (string): A static IPv6 prefix
        - origin (object): The origin of the prefix
        - description (string): A name or description for the prefix
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'createNetworkAppliancePrefixesDelegatedStatic'
        }
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics'

        body_params = ['prefix', 'origin', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, staticDelegatedPrefixId: str, **kwargs):
        """
        **Update a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - staticDelegatedPrefixId (string): Static delegated prefix ID
        - prefix (string): A static IPv6 prefix
        - origin (object): The origin of the prefix
        - description (string): A name or description for the prefix
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'updateNetworkAppliancePrefixesDelegatedStatic'
        }
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}'

        body_params = ['prefix', 'origin', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, staticDelegatedPrefixId: str):
        """
        **Delete a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - staticDelegatedPrefixId (string): Static delegated prefix ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'deleteNetworkAppliancePrefixesDelegatedStatic'
        }
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createNetworkApplianceRfProfile(self, networkId: str, name: str, **kwargs):
        """
        **Creates new RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-rf-profile

        - networkId (string): Network ID
        - name (string): The name of the new profile. Must be unique. This param is required on creation.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - perSsidSettings (object): Per-SSID radio settings by number.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'createNetworkApplianceRfProfile'
        }
        resource = f'/networks/{networkId}/appliance/rfProfiles'

        body_params = ['name', 'twoFourGhzSettings', 'fiveGhzSettings', 'perSsidSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        - name (string): The name of the new profile. Must be unique.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - perSsidSettings (object): Per-SSID radio settings by number.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'updateNetworkApplianceRfProfile'
        }
        resource = f'/networks/{networkId}/appliance/rfProfiles/{rfProfileId}'

        body_params = ['name', 'twoFourGhzSettings', 'fiveGhzSettings', 'perSsidSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkApplianceRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'deleteNetworkApplianceRfProfile'
        }
        resource = f'/networks/{networkId}/appliance/rfProfiles/{rfProfileId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkApplianceSdwanInternetPolicies(self, networkId: str, **kwargs):
        """
        **Update SDWAN internet traffic preferences for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-sdwan-internet-policies

        - networkId (string): Network ID
        - wanTrafficUplinkPreferences (array): policies with respective traffic filters for an MX network
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'sdwan', 'internetPolicies'],
            'operation': 'updateNetworkApplianceSdwanInternetPolicies'
        }
        resource = f'/networks/{networkId}/appliance/sdwan/internetPolicies'

        body_params = ['wanTrafficUplinkPreferences', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceSettings(self, networkId: str, **kwargs):
        """
        **Update the appliance settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-settings

        - networkId (string): Network ID
        - clientTrackingMethod (string): Client tracking method of a network
        - deploymentMode (string): Deployment mode of a network
        - dynamicDns (object): Dynamic DNS settings for a network
        """

        kwargs.update(locals())

        if 'clientTrackingMethod' in kwargs:
            options = ['IP address', 'MAC address', 'Unique client identifier']
            assert kwargs['clientTrackingMethod'] in options, f'''"clientTrackingMethod" cannot be "{kwargs['clientTrackingMethod']}", & must be set to one of: {options}'''
        if 'deploymentMode' in kwargs:
            options = ['passthrough', 'routed']
            assert kwargs['deploymentMode'] in options, f'''"deploymentMode" cannot be "{kwargs['deploymentMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'settings'],
            'operation': 'updateNetworkApplianceSettings'
        }
        resource = f'/networks/{networkId}/appliance/settings'

        body_params = ['clientTrackingMethod', 'deploymentMode', 'dynamicDns', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceSingleLan(self, networkId: str, **kwargs):
        """
        **Update single LAN configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

        - networkId (string): Network ID
        - subnet (string): The subnet of the single LAN configuration
        - applianceIp (string): The appliance IP address of the single LAN
        - ipv6 (object): IPv6 configuration on the VLAN
        - mandatoryDhcp (object): Mandatory DHCP will enforce that clients connecting to this LAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'singleLan'],
            'operation': 'updateNetworkApplianceSingleLan'
        }
        resource = f'/networks/{networkId}/appliance/singleLan'

        body_params = ['subnet', 'applianceIp', 'ipv6', 'mandatoryDhcp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceSsid(self, networkId: str, number: str, **kwargs):
        """
        **Update the attributes of an MX SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-ssid

        - networkId (string): Network ID
        - number (string): Number
        - name (string): The name of the SSID.
        - enabled (boolean): Whether or not the SSID is enabled.
        - defaultVlanId (integer): The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode.
        - authMode (string): The association control method for the SSID ('open', 'psk', '8021x-meraki' or '8021x-radius').
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'.
        - radiusServers (array): The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is '8021x-radius'.
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'.
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only'). This param is only valid if (1) the authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is '8021x-meraki' OR (3) the authMode is '8021x-radius'
        - visible (boolean): Boolean indicating whether the MX should advertise or hide this SSID.
        - dhcpEnforcedDeauthentication (object): DHCP Enforced Deauthentication enables the disassociation of wireless clients in addition to Mandatory DHCP. This param is only valid on firmware versions >= MX 17.0 where the associated LAN has Mandatory DHCP Enabled 
        - dot11w (object): The current setting for Protected Management Frames (802.11w).
        """

        kwargs.update(locals())

        if 'authMode' in kwargs:
            options = ['8021x-meraki', '8021x-radius', 'open', 'psk']
            assert kwargs['authMode'] in options, f'''"authMode" cannot be "{kwargs['authMode']}", & must be set to one of: {options}'''
        if 'encryptionMode' in kwargs:
            options = ['wep', 'wpa']
            assert kwargs['encryptionMode'] in options, f'''"encryptionMode" cannot be "{kwargs['encryptionMode']}", & must be set to one of: {options}'''
        if 'wpaEncryptionMode' in kwargs:
            options = ['WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only']
            assert kwargs['wpaEncryptionMode'] in options, f'''"wpaEncryptionMode" cannot be "{kwargs['wpaEncryptionMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'ssids'],
            'operation': 'updateNetworkApplianceSsid'
        }
        resource = f'/networks/{networkId}/appliance/ssids/{number}'

        body_params = ['name', 'enabled', 'defaultVlanId', 'authMode', 'psk', 'radiusServers', 'encryptionMode', 'wpaEncryptionMode', 'visible', 'dhcpEnforcedDeauthentication', 'dot11w', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, name: str, **kwargs):
        """
        **Add a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - name (string): Name of the custom performance class
        - maxLatency (integer): Maximum latency in milliseconds
        - maxJitter (integer): Maximum jitter in milliseconds
        - maxLossPercentage (integer): Maximum percentage of packet loss
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'createNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses'

        body_params = ['name', 'maxLatency', 'maxJitter', 'maxLossPercentage', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str, **kwargs):
        """
        **Update a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - customPerformanceClassId (string): Custom performance class ID
        - name (string): Name of the custom performance class
        - maxLatency (integer): Maximum latency in milliseconds
        - maxJitter (integer): Maximum jitter in milliseconds
        - maxLossPercentage (integer): Maximum percentage of packet loss
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'updateNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        body_params = ['name', 'maxLatency', 'maxJitter', 'maxLossPercentage', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str):
        """
        **Delete a custom performance class from an MX network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - customPerformanceClassId (string): Custom performance class ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'deleteNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkApplianceTrafficShapingRules(self, networkId: str, **kwargs):
        """
        **Update the traffic shaping settings rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

        - networkId (string): Network ID
        - defaultRulesEnabled (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'rules'],
            'operation': 'updateNetworkApplianceTrafficShapingRules'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/rules'

        body_params = ['defaultRulesEnabled', 'rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceTrafficShapingUplinkBandwidth(self, networkId: str, **kwargs):
        """
        **Updates the uplink bandwidth settings for your MX network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

        - networkId (string): Network ID
        - bandwidthLimits (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkBandwidth'],
            'operation': 'updateNetworkApplianceTrafficShapingUplinkBandwidth'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth'

        body_params = ['bandwidthLimits', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceTrafficShapingUplinkSelection(self, networkId: str, **kwargs):
        """
        **Update uplink selection settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

        - networkId (string): Network ID
        - activeActiveAutoVpnEnabled (boolean): Toggle for enabling or disabling active-active AutoVPN
        - defaultUplink (string): The default uplink. Must be one of: 'wan1' or 'wan2'
        - loadBalancingEnabled (boolean): Toggle for enabling or disabling load balancing
        - failoverAndFailback (object): WAN failover and failback behavior
        - wanTrafficUplinkPreferences (array): Array of uplink preference rules for WAN traffic
        - vpnTrafficUplinkPreferences (array): Array of uplink preference rules for VPN traffic
        """

        kwargs.update(locals())

        if 'defaultUplink' in kwargs:
            options = ['wan1', 'wan2']
            assert kwargs['defaultUplink'] in options, f'''"defaultUplink" cannot be "{kwargs['defaultUplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkSelection'],
            'operation': 'updateNetworkApplianceTrafficShapingUplinkSelection'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkSelection'

        body_params = ['activeActiveAutoVpnEnabled', 'defaultUplink', 'loadBalancingEnabled', 'failoverAndFailback', 'wanTrafficUplinkPreferences', 'vpnTrafficUplinkPreferences', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceTrafficShapingVpnExclusions(self, networkId: str, **kwargs):
        """
        **Update VPN exclusion rules for an MX network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-vpn-exclusions

        - networkId (string): Network ID
        - custom (array): Custom VPN exclusion rules. Pass an empty array to clear existing rules.
        - majorApplications (array): Major Application based VPN exclusion rules. Pass an empty array to clear existing rules.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'vpnExclusions'],
            'operation': 'updateNetworkApplianceTrafficShapingVpnExclusions'
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/vpnExclusions'

        body_params = ['custom', 'majorApplications', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkApplianceVlan(self, networkId: str, id: str, name: str, **kwargs):
        """
        **Add a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

        - networkId (string): Network ID
        - id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
        - name (string): The name of the new VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        - groupPolicyId (string): The id of the desired group policy to apply to the VLAN
        - templateVlanType (string): Type of subnetting of the VLAN. Applicable only for template network.
        - cidr (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
        - mask (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
        - ipv6 (object): IPv6 configuration on the VLAN
        - dhcpHandling (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
        - dhcpLeaseTime (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
        - mandatoryDhcp (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above
        - dhcpBootOptionsEnabled (boolean): Use DHCP boot options specified in other properties
        - dhcpOptions (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
        """

        kwargs.update(locals())

        if 'templateVlanType' in kwargs:
            options = ['same', 'unique']
            assert kwargs['templateVlanType'] in options, f'''"templateVlanType" cannot be "{kwargs['templateVlanType']}", & must be set to one of: {options}'''
        if 'dhcpHandling' in kwargs:
            options = ['Do not respond to DHCP requests', 'Relay DHCP to another server', 'Run a DHCP server']
            assert kwargs['dhcpHandling'] in options, f'''"dhcpHandling" cannot be "{kwargs['dhcpHandling']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['1 day', '1 hour', '1 week', '12 hours', '30 minutes', '4 hours']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'createNetworkApplianceVlan'
        }
        resource = f'/networks/{networkId}/appliance/vlans'

        body_params = ['id', 'name', 'subnet', 'applianceIp', 'groupPolicyId', 'templateVlanType', 'cidr', 'mask', 'ipv6', 'dhcpHandling', 'dhcpLeaseTime', 'mandatoryDhcp', 'dhcpBootOptionsEnabled', 'dhcpOptions', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceVlansSettings(self, networkId: str, **kwargs):
        """
        **Enable/Disable VLANs for the given network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

        - networkId (string): Network ID
        - vlansEnabled (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vlans', 'settings'],
            'operation': 'updateNetworkApplianceVlansSettings'
        }
        resource = f'/networks/{networkId}/appliance/vlans/settings'

        body_params = ['vlansEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceVlan(self, networkId: str, vlanId: str, **kwargs):
        """
        **Update a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

        - networkId (string): Network ID
        - vlanId (string): Vlan ID
        - name (string): The name of the VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        - groupPolicyId (string): The id of the desired group policy to apply to the VLAN
        - vpnNatSubnet (string): The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN
        - dhcpHandling (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
        - dhcpRelayServerIps (array): The IPs of the DHCP servers that DHCP requests should be relayed to
        - dhcpLeaseTime (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
        - dhcpBootOptionsEnabled (boolean): Use DHCP boot options specified in other properties
        - dhcpBootNextServer (string): DHCP boot option to direct boot clients to the server to load the boot file from
        - dhcpBootFilename (string): DHCP boot option for boot filename
        - fixedIpAssignments (object): The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
        - reservedIpRanges (array): The DHCP reserved IP ranges on the VLAN
        - dnsNameservers (string): The DNS nameservers used for DHCP responses, either "upstream_dns", "google_dns", "opendns", or a newline seperated string of IP addresses or domain names
        - dhcpOptions (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
        - templateVlanType (string): Type of subnetting of the VLAN. Applicable only for template network.
        - cidr (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
        - mask (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
        - ipv6 (object): IPv6 configuration on the VLAN
        - mandatoryDhcp (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above
        """

        kwargs.update(locals())

        if 'dhcpHandling' in kwargs:
            options = ['Do not respond to DHCP requests', 'Relay DHCP to another server', 'Run a DHCP server']
            assert kwargs['dhcpHandling'] in options, f'''"dhcpHandling" cannot be "{kwargs['dhcpHandling']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['1 day', '1 hour', '1 week', '12 hours', '30 minutes', '4 hours']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''
        if 'templateVlanType' in kwargs:
            options = ['same', 'unique']
            assert kwargs['templateVlanType'] in options, f'''"templateVlanType" cannot be "{kwargs['templateVlanType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'updateNetworkApplianceVlan'
        }
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        body_params = ['name', 'subnet', 'applianceIp', 'groupPolicyId', 'vpnNatSubnet', 'dhcpHandling', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dhcpBootOptionsEnabled', 'dhcpBootNextServer', 'dhcpBootFilename', 'fixedIpAssignments', 'reservedIpRanges', 'dnsNameservers', 'dhcpOptions', 'templateVlanType', 'cidr', 'mask', 'ipv6', 'mandatoryDhcp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkApplianceVlan(self, networkId: str, vlanId: str):
        """
        **Delete a VLAN from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

        - networkId (string): Network ID
        - vlanId (string): Vlan ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'deleteNetworkApplianceVlan'
        }
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkApplianceVpnBgp(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update a Hub BGP Configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

        - networkId (string): Network ID
        - enabled (boolean): Boolean value to enable or disable the BGP configuration. When BGP is enabled, the asNumber (ASN) will be autopopulated with the preconfigured ASN at other Hubs or a default value if there is no ASN configured.
        - asNumber (integer): An Autonomous System Number (ASN) is required if you are to run BGP and peer with another BGP Speaker outside of the Auto VPN domain. This ASN will be applied to the entire Auto VPN domain. The entire 4-byte ASN range is supported. So, the ASN must be an integer between 1 and 4294967295. When absent, this field is not updated. If no value exists then it defaults to 64512.
        - ibgpHoldTimer (integer): The iBGP holdtimer in seconds. The iBGP holdtimer must be an integer between 12 and 240. When absent, this field is not updated. If no value exists then it defaults to 240.
        - neighbors (array): List of BGP neighbors. This list replaces the existing set of neighbors. When absent, this field is not updated.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'bgp'],
            'operation': 'updateNetworkApplianceVpnBgp'
        }
        resource = f'/networks/{networkId}/appliance/vpn/bgp'

        body_params = ['enabled', 'asNumber', 'ibgpHoldTimer', 'neighbors', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "settings/update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceVpnSiteToSiteVpn(self, networkId: str, mode: str, **kwargs):
        """
        **Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

        - networkId (string): Network ID
        - mode (string): The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'
        - hubs (array): The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required.
        - subnets (array): The list of subnets and their VPN presence.
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['hub', 'none', 'spoke']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'siteToSiteVpn'],
            'operation': 'updateNetworkApplianceVpnSiteToSiteVpn'
        }
        resource = f'/networks/{networkId}/appliance/vpn/siteToSiteVpn'

        body_params = ['mode', 'hubs', 'subnets', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkApplianceWarmSpare(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update MX warm spare settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

        - networkId (string): Network ID
        - enabled (boolean): Enable warm spare
        - spareSerial (string): Serial number of the warm spare appliance
        - uplinkMode (string): Uplink mode, either virtual or public
        - virtualIp1 (string): The WAN 1 shared IP
        - virtualIp2 (string): The WAN 2 shared IP
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'updateNetworkApplianceWarmSpare'
        }
        resource = f'/networks/{networkId}/appliance/warmSpare'

        body_params = ['enabled', 'spareSerial', 'uplinkMode', 'virtualIp1', 'virtualIp2', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def swapNetworkApplianceWarmSpare(self, networkId: str):
        """
        **Swap MX primary and warm spare appliances**
        https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'swapNetworkApplianceWarmSpare'
        }
        resource = f'/networks/{networkId}/appliance/warmSpare/swap'

        action = {
            "resource": resource,
            "operation": "swap",
        }
        return action
        





    def updateOrganizationApplianceVpnThirdPartyVPNPeers(self, organizationId: str, peers: list):
        """
        **Update the third party VPN peers for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

        - organizationId (string): Organization ID
        - peers (array): The list of VPN peers
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'thirdPartyVPNPeers'],
            'operation': 'updateOrganizationApplianceVpnThirdPartyVPNPeers'
        }
        resource = f'/organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers'

        body_params = ['peers', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        



