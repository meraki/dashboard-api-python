import urllib


class ActionBatchWireless(object):
    def __init__(self):
        super(ActionBatchWireless, self).__init__()
        


    def updateDeviceWirelessBluetoothSettings(self, serial: str, **kwargs):
        """
        **Update the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

        - serial (string): (required)
        - uuid (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        - major (integer): Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        - minor (integer): Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'updateDeviceWirelessBluetoothSettings'
        }
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        body_params = ['uuid', 'major', 'minor', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateDeviceWirelessRadioSettings(self, serial: str, **kwargs):
        """
        **Update the radio settings of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

        - serial (string): (required)
        - rfProfileId (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
        - twoFourGhzSettings (object): Manual radio settings for 2.4 GHz.
        - fiveGhzSettings (object): Manual radio settings for 5 GHz.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'radio', 'settings'],
            'operation': 'updateDeviceWirelessRadioSettings'
        }
        resource = f'/devices/{serial}/wireless/radio/settings'

        body_params = ['rfProfileId', 'twoFourGhzSettings', 'fiveGhzSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessAlternateManagementInterface(self, networkId: str, **kwargs):
        """
        **Update alternate management interface and device static IP**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

        - networkId (string): (required)
        - enabled (boolean): Boolean value to enable or disable alternate management interface
        - vlanId (integer): Alternate management interface VLAN, must be between 1 and 4094
        - protocols (array): Can be one or more of the following values: 'radius', 'snmp', 'syslog' or 'ldap'
        - accessPoints (array): Array of access point serial number and IP assignment. Note: accessPoints IP assignment is not applicable for template networks, in other words, do not put 'accessPoints' in the body when updating template networks. Also, an empty 'accessPoints' array will remove all previous static IP assignments
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'alternateManagementInterface'],
            'operation': 'updateNetworkWirelessAlternateManagementInterface'
        }
        resource = f'/networks/{networkId}/wireless/alternateManagementInterface'

        body_params = ['enabled', 'vlanId', 'protocols', 'accessPoints', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessBilling(self, networkId: str, **kwargs):
        """
        **Update the billing settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-billing

        - networkId (string): (required)
        - currency (string): The currency code of this node group's billing plans
        - plans (array): Array of billing plans in the node group. (Can configure a maximum of 5)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'billing'],
            'operation': 'updateNetworkWirelessBilling'
        }
        resource = f'/networks/{networkId}/wireless/billing'

        body_params = ['currency', 'plans', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkWirelessRfProfile(self, networkId: str, name: str, bandSelectionType: str, **kwargs):
        """
        **Creates new RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

        - networkId (string): (required)
        - name (string): The name of the new profile. Must be unique. This param is required on creation.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - transmission (object): Settings related to radio transmission.
        - perSsidSettings (object): Per-SSID radio settings by number.
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ap', 'ssid']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'createNetworkWirelessRfProfile'
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings', 'transmission', 'perSsidSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

        - networkId (string): (required)
        - rfProfileId (string): (required)
        - name (string): The name of the new profile. Must be unique.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - transmission (object): Settings related to radio transmission.
        - perSsidSettings (object): Per-SSID radio settings by number.
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ap', 'ssid']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'updateNetworkWirelessRfProfile'
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings', 'transmission', 'perSsidSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

        - networkId (string): (required)
        - rfProfileId (string): (required)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'deleteNetworkWirelessRfProfile'
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkWirelessSettings(self, networkId: str, **kwargs):
        """
        **Update the wireless settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

        - networkId (string): (required)
        - meshingEnabled (boolean): Toggle for enabling or disabling meshing in a network
        - ipv6BridgeEnabled (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
        - locationAnalyticsEnabled (boolean): Toggle for enabling or disabling location analytics for your network
        - upgradeStrategy (string): The upgrade strategy to apply to the network. Must be one of 'minimizeUpgradeTime' or 'minimizeClientDowntime'. Requires firmware version MR 26.8 or higher'
        - ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
        """

        kwargs.update(locals())

        if 'upgradeStrategy' in kwargs:
            options = ['minimizeClientDowntime', 'minimizeUpgradeTime']
            assert kwargs['upgradeStrategy'] in options, f'''"upgradeStrategy" cannot be "{kwargs['upgradeStrategy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'settings'],
            'operation': 'updateNetworkWirelessSettings'
        }
        resource = f'/networks/{networkId}/wireless/settings'

        body_params = ['meshingEnabled', 'ipv6BridgeEnabled', 'locationAnalyticsEnabled', 'upgradeStrategy', 'ledLightsOn', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsid(self, networkId: str, number: str, **kwargs):
        """
        **Update the attributes of an MR SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

        - networkId (string): (required)
        - number (string): (required)
        - name (string): The name of the SSID
        - enabled (boolean): Whether or not the SSID is enabled
        - authMode (string): The association control method for the SSID ('open', 'open-enhanced', 'psk', 'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac', '8021x-radius', '8021x-google', '8021x-localradius', 'ipsk-with-radius' or 'ipsk-without-radius')
        - enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security')
        - dot11w (object): The current setting for Protected Management Frames (802.11w).
        - dot11r (object): The current setting for 802.11r
        - splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest', 'Cisco ISE' or 'Google Apps domain'). This attribute is not supported for template children.
        - splashGuestSponsorDomains (array): Array of valid sponsor email domains for sponsored guest splash type.
        - oauth (object): The OAuth settings of this SSID. Only valid if splashPage is 'Google OAuth'.
        - localRadius (object): The current setting for Local Authentication, a built-in RADIUS server on the access point. Only valid if authMode is '8021x-localradius'.
        - ldap (object): The current setting for LDAP. Only valid if splashPage is 'Password-protected with LDAP'.
        - activeDirectory (object): The current setting for Active Directory. Only valid if splashPage is 'Password-protected with Active Directory'
        - radiusServers (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusProxyEnabled (boolean): If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers.
        - radiusTestingEnabled (boolean): If true, Meraki devices will periodically send Access-Request messages to configured RADIUS servers using identity 'meraki_8021x_test' to ensure that the RADIUS servers are reachable.
        - radiusCalledStationId (string): The template of the called station identifier to be used for RADIUS (ex. $NODE_MAC$:$VAP_NUM$).
        - radiusAuthenticationNasId (string): The template of the NAS identifier to be used for RADIUS authentication (ex. $NODE_MAC$:$VAP_NUM$).
        - radiusServerTimeout (integer): The amount of time for which a RADIUS client waits for a reply from the RADIUS server (must be between 1-10 seconds).
        - radiusServerAttemptsLimit (integer): The maximum number of transmit attempts after which a RADIUS server is failed over (must be between 1-5).
        - radiusFallbackEnabled (boolean): Whether or not higher priority RADIUS servers should be retried after 60 seconds.
        - radiusCoaEnabled (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
        - radiusFailoverPolicy (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
        - radiusLoadBalancingPolicy (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
        - radiusAccountingEnabled (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusAccountingServers (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
        - radiusAccountingInterimInterval (integer): The interval (in seconds) in which accounting information is updated and sent to the RADIUS accounting server.
        - radiusAttributeForGroupPolicies (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
        - ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator' or 'VPN')
        - useVlanTagging (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - concentratorNetworkId (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
        - secondaryConcentratorNetworkId (string): The secondary concentrator to use when the ipAssignmentMode is 'VPN'. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. ('disabled' represents no secondary concentrator.)
        - disassociateClientsOnVpnFailover (boolean): Disassociate clients when 'VPN' concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is 'VPN'.
        - vlanId (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
        - defaultVlanId (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - apTagsAndVlanIds (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - walledGardenEnabled (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
        - walledGardenRanges (array): Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']). Meraki's splash page is automatically included in your walled garden.
        - gre (object): Ethernet over GRE settings
        - radiusOverride (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
        - radiusGuestVlanEnabled (boolean): Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
        - radiusGuestVlanId (integer): VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
        - minBitrate (number): The minimum bitrate in Mbps of this SSID in the default indoor RF profile. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
        - bandSelection (string): The client-serving radio frequencies of this SSID in the default indoor RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
        - perClientBandwidthLimitUp (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
        - perClientBandwidthLimitDown (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
        - perSsidBandwidthLimitUp (integer): The total upload bandwidth limit in Kbps. (0 represents no limit.)
        - perSsidBandwidthLimitDown (integer): The total download bandwidth limit in Kbps. (0 represents no limit.)
        - lanIsolationEnabled (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
        - visible (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
        - availableOnAllAps (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
        - availabilityTags (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
        - mandatoryDhcpEnabled (boolean): If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate.
        - adultContentFilteringEnabled (boolean): Boolean indicating whether or not adult content will be blocked
        - dnsRewrite (object): DNS servers rewrite settings
        - speedBurst (object): The SpeedBurst setting for this SSID'
        """

        kwargs.update(locals())

        if 'authMode' in kwargs:
            options = ['8021x-google', '8021x-localradius', '8021x-meraki', '8021x-nac', '8021x-radius', 'ipsk-with-radius', 'ipsk-without-radius', 'open', 'open-enhanced', 'open-with-nac', 'open-with-radius', 'psk']
            assert kwargs['authMode'] in options, f'''"authMode" cannot be "{kwargs['authMode']}", & must be set to one of: {options}'''
        if 'enterpriseAdminAccess' in kwargs:
            options = ['access disabled', 'access enabled']
            assert kwargs['enterpriseAdminAccess'] in options, f'''"enterpriseAdminAccess" cannot be "{kwargs['enterpriseAdminAccess']}", & must be set to one of: {options}'''
        if 'encryptionMode' in kwargs:
            options = ['wep', 'wpa']
            assert kwargs['encryptionMode'] in options, f'''"encryptionMode" cannot be "{kwargs['encryptionMode']}", & must be set to one of: {options}'''
        if 'wpaEncryptionMode' in kwargs:
            options = ['WPA1 and WPA2', 'WPA1 only', 'WPA2 only', 'WPA3 192-bit Security', 'WPA3 Transition Mode', 'WPA3 only']
            assert kwargs['wpaEncryptionMode'] in options, f'''"wpaEncryptionMode" cannot be "{kwargs['wpaEncryptionMode']}", & must be set to one of: {options}'''
        if 'splashPage' in kwargs:
            options = ['Billing', 'Cisco ISE', 'Click-through splash page', 'Facebook Wi-Fi', 'Google Apps domain', 'Google OAuth', 'None', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'SMS authentication', 'Sponsored guest', 'Systems Manager Sentry']
            assert kwargs['splashPage'] in options, f'''"splashPage" cannot be "{kwargs['splashPage']}", & must be set to one of: {options}'''
        if 'radiusFailoverPolicy' in kwargs:
            options = ['Allow access', 'Deny access']
            assert kwargs['radiusFailoverPolicy'] in options, f'''"radiusFailoverPolicy" cannot be "{kwargs['radiusFailoverPolicy']}", & must be set to one of: {options}'''
        if 'radiusLoadBalancingPolicy' in kwargs:
            options = ['Round robin', 'Strict priority order']
            assert kwargs['radiusLoadBalancingPolicy'] in options, f'''"radiusLoadBalancingPolicy" cannot be "{kwargs['radiusLoadBalancingPolicy']}", & must be set to one of: {options}'''
        if 'radiusAttributeForGroupPolicies' in kwargs:
            options = ['Airespace-ACL-Name', 'Aruba-User-Role', 'Filter-Id', 'Reply-Message']
            assert kwargs['radiusAttributeForGroupPolicies'] in options, f'''"radiusAttributeForGroupPolicies" cannot be "{kwargs['radiusAttributeForGroupPolicies']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'updateNetworkWirelessSsid'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}'

        body_params = ['name', 'enabled', 'authMode', 'enterpriseAdminAccess', 'encryptionMode', 'psk', 'wpaEncryptionMode', 'dot11w', 'dot11r', 'splashPage', 'splashGuestSponsorDomains', 'oauth', 'localRadius', 'ldap', 'activeDirectory', 'radiusServers', 'radiusProxyEnabled', 'radiusTestingEnabled', 'radiusCalledStationId', 'radiusAuthenticationNasId', 'radiusServerTimeout', 'radiusServerAttemptsLimit', 'radiusFallbackEnabled', 'radiusCoaEnabled', 'radiusFailoverPolicy', 'radiusLoadBalancingPolicy', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusAccountingInterimInterval', 'radiusAttributeForGroupPolicies', 'ipAssignmentMode', 'useVlanTagging', 'concentratorNetworkId', 'secondaryConcentratorNetworkId', 'disassociateClientsOnVpnFailover', 'vlanId', 'defaultVlanId', 'apTagsAndVlanIds', 'walledGardenEnabled', 'walledGardenRanges', 'gre', 'radiusOverride', 'radiusGuestVlanEnabled', 'radiusGuestVlanId', 'minBitrate', 'bandSelection', 'perClientBandwidthLimitUp', 'perClientBandwidthLimitDown', 'perSsidBandwidthLimitUp', 'perSsidBandwidthLimitDown', 'lanIsolationEnabled', 'visible', 'availableOnAllAps', 'availabilityTags', 'mandatoryDhcpEnabled', 'adultContentFilteringEnabled', 'dnsRewrite', 'speedBurst', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidBonjourForwarding(self, networkId: str, number: str, **kwargs):
        """
        **Update the bonjour forwarding setting and rules for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-bonjour-forwarding

        - networkId (string): (required)
        - number (string): (required)
        - enabled (boolean): If true, Bonjour forwarding is enabled on this SSID.
        - rules (array): List of bonjour forwarding rules.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'bonjourForwarding'],
            'operation': 'updateNetworkWirelessSsidBonjourForwarding'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding'

        body_params = ['enabled', 'rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidDeviceTypeGroupPolicies(self, networkId: str, number: str, **kwargs):
        """
        **Update the device type group policies for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-device-type-group-policies

        - networkId (string): (required)
        - number (string): (required)
        - enabled (boolean): If true, the SSID device type group policies are enabled.
        - deviceTypePolicies (array): List of device type policies.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'deviceTypeGroupPolicies'],
            'operation': 'updateNetworkWirelessSsidDeviceTypeGroupPolicies'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies'

        body_params = ['enabled', 'deviceTypePolicies', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidEapOverride(self, networkId: str, number: str, **kwargs):
        """
        **Update the EAP overridden parameters for an SSID.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-eap-override

        - networkId (string): (required)
        - number (string): (required)
        - timeout (integer): General EAP timeout in seconds.
        - identity (object): EAP settings for identity requests.
        - maxRetries (integer): Maximum number of general EAP retries.
        - eapolKey (object): EAPOL Key settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'eapOverride'],
            'operation': 'updateNetworkWirelessSsidEapOverride'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/eapOverride'

        body_params = ['timeout', 'identity', 'maxRetries', 'eapolKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L3 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

        - networkId (string): (required)
        - number (string): (required)
        - rules (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule)
        - allowLanAccess (boolean): Allow wireless client access to local LAN (boolean value - true allows access and false denies access) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l3FirewallRules'],
            'operation': 'updateNetworkWirelessSsidFirewallL3FirewallRules'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules'

        body_params = ['rules', 'allowLanAccess', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidFirewallL7FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L7 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

        - networkId (string): (required)
        - number (string): (required)
        - rules (array): An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l7FirewallRules'],
            'operation': 'updateNetworkWirelessSsidFirewallL7FirewallRules'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidHotspot20(self, networkId: str, number: str, **kwargs):
        """
        **Update the Hotspot 2.0 settings of an SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot-2-0

        - networkId (string): (required)
        - number (string): (required)
        - enabled (boolean): Whether or not Hotspot 2.0 for this SSID is enabled
        - operator (object): Operator settings for this SSID
        - venue (object): Venue settings for this SSID
        - networkAccessType (string): The network type of this SSID ('Private network', 'Private network with guest access', 'Chargeable public network', 'Free public network', 'Personal device network', 'Emergency services only network', 'Test or experimental', 'Wildcard')
        - domains (array): An array of domain names
        - roamConsortOis (array): An array of roaming consortium OIs (hexadecimal number 3-5 octets in length)
        - mccMncs (array): An array of MCC/MNC pairs
        - naiRealms (array): An array of NAI realms
        """

        kwargs.update(locals())

        if 'networkAccessType' in kwargs:
            options = ['Chargeable public network', 'Emergency services only network', 'Free public network', 'Personal device network', 'Private network', 'Private network with guest access', 'Test or experimental', 'Wildcard']
            assert kwargs['networkAccessType'] in options, f'''"networkAccessType" cannot be "{kwargs['networkAccessType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'hotspot20'],
            'operation': 'updateNetworkWirelessSsidHotspot20'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/hotspot20'

        body_params = ['enabled', 'operator', 'venue', 'networkAccessType', 'domains', 'roamConsortOis', 'mccMncs', 'naiRealms', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, name: str, groupPolicyId: str, **kwargs):
        """
        **Create an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

        - networkId (string): (required)
        - number (string): (required)
        - name (string): The name of the Identity PSK
        - groupPolicyId (string): The group policy to be applied to clients
        - passphrase (string): The passphrase for client authentication. If left blank, one will be auto-generated.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'createNetworkWirelessSsidIdentityPsk'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks'

        body_params = ['name', 'passphrase', 'groupPolicyId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, identityPskId: str, **kwargs):
        """
        **Update an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

        - networkId (string): (required)
        - number (string): (required)
        - identityPskId (string): (required)
        - name (string): The name of the Identity PSK
        - passphrase (string): The passphrase for client authentication
        - groupPolicyId (string): The group policy to be applied to clients
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'updateNetworkWirelessSsidIdentityPsk'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}'

        body_params = ['name', 'passphrase', 'groupPolicyId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, identityPskId: str):
        """
        **Delete an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

        - networkId (string): (required)
        - number (string): (required)
        - identityPskId (string): (required)
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'deleteNetworkWirelessSsidIdentityPsk'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateNetworkWirelessSsidSchedules(self, networkId: str, number: str, **kwargs):
        """
        **Update the outage schedule for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-schedules

        - networkId (string): (required)
        - number (string): (required)
        - enabled (boolean): If true, the SSID outage schedule is enabled.
        - ranges (array): List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence.
        - rangesInSeconds (array): List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'schedules'],
            'operation': 'updateNetworkWirelessSsidSchedules'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/schedules'

        body_params = ['enabled', 'ranges', 'rangesInSeconds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidSplashSettings(self, networkId: str, number: str, **kwargs):
        """
        **Modify the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

        - networkId (string): (required)
        - number (string): (required)
        - splashUrl (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
        - useSplashUrl (boolean): [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
        - splashTimeout (integer): Splash timeout in minutes. This will determine how often users will see the splash page.
        - redirectUrl (string): The custom redirect URL where the users will go after the splash page.
        - useRedirectUrl (boolean): The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.
        - welcomeMessage (string): The welcome message for the users on the splash page.
        - splashLogo (object): The logo used in the splash page.
        - splashImage (object): The image used in the splash page.
        - splashPrepaidFront (object): The prepaid front image used in the splash page.
        - blockAllTrafficBeforeSignOn (boolean): How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.
        - controllerDisconnectionBehavior (string): How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.
        - allowSimultaneousLogins (boolean): Whether or not to allow simultaneous logins from different devices.
        - guestSponsorship (object): Details associated with guest sponsored splash.
        - billing (object): Details associated with billing splash.
        - sentryEnrollment (object): Systems Manager sentry enrollment splash settings.
        """

        kwargs.update(locals())

        if 'controllerDisconnectionBehavior' in kwargs:
            options = ['default', 'open', 'restricted']
            assert kwargs['controllerDisconnectionBehavior'] in options, f'''"controllerDisconnectionBehavior" cannot be "{kwargs['controllerDisconnectionBehavior']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'splash', 'settings'],
            'operation': 'updateNetworkWirelessSsidSplashSettings'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/splash/settings'

        body_params = ['splashUrl', 'useSplashUrl', 'splashTimeout', 'redirectUrl', 'useRedirectUrl', 'welcomeMessage', 'splashLogo', 'splashImage', 'splashPrepaidFront', 'blockAllTrafficBeforeSignOn', 'controllerDisconnectionBehavior', 'allowSimultaneousLogins', 'guestSponsorship', 'billing', 'sentryEnrollment', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidTrafficShapingRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the traffic shaping settings for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

        - networkId (string): (required)
        - number (string): (required)
        - trafficShapingEnabled (boolean): Whether traffic shaping rules are applied to clients on your SSID.
        - defaultRulesEnabled (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'trafficShaping', 'rules'],
            'operation': 'updateNetworkWirelessSsidTrafficShapingRules'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules'

        body_params = ['trafficShapingEnabled', 'defaultRulesEnabled', 'rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateNetworkWirelessSsidVpn(self, networkId: str, number: str, **kwargs):
        """
        **Update the VPN settings for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-vpn

        - networkId (string): (required)
        - number (string): (required)
        - concentrator (object): The VPN concentrator settings for this SSID.
        - splitTunnel (object): The VPN split tunnel settings for this SSID.
        - failover (object): Secondary VPN concentrator settings. This is only used when two VPN concentrators are configured on the SSID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'vpn'],
            'operation': 'updateNetworkWirelessSsidVpn'
        }
        resource = f'/networks/{networkId}/wireless/ssids/{number}/vpn'

        body_params = ['concentrator', 'splitTunnel', 'failover', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        



