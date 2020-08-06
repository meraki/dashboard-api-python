class AsyncSSIDs:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkDeviceWirelessStatus(self, networkId: str, serial: str):
        """
        **Return the SSID statuses of an access point**
        https://developer.cisco.com/meraki/api/#!get-network-device-wireless-status
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['SSIDs'],
            'operation': 'getNetworkDeviceWirelessStatus',
        }
        resource = f'/networks/{networkId}/devices/{serial}/wireless/status'

        return await self._session.get(metadata, resource)

    async def getNetworkSsids(self, networkId: str):
        """
        **List the SSIDs in a network. Supports networks with access points or wireless-enabled security appliances and teleworker gateways.**
        https://developer.cisco.com/meraki/api/#!get-network-ssids
        
        - networkId (string)
        """

        metadata = {
            'tags': ['SSIDs'],
            'operation': 'getNetworkSsids',
        }
        resource = f'/networks/{networkId}/ssids'

        return await self._session.get(metadata, resource)

    async def getNetworkSsid(self, networkId: str, number: str):
        """
        **Return a single SSID**
        https://developer.cisco.com/meraki/api/#!get-network-ssid
        
        - networkId (string)
        - number (string)
        """

        metadata = {
            'tags': ['SSIDs'],
            'operation': 'getNetworkSsid',
        }
        resource = f'/networks/{networkId}/ssids/{number}'

        return await self._session.get(metadata, resource)

    async def updateNetworkSsid(self, networkId: str, number: str, **kwargs):
        """
        **Update the attributes of an SSID**
        https://developer.cisco.com/meraki/api/#!update-network-ssid
        
        - networkId (string)
        - number (string)
        - name (string): The name of the SSID
        - enabled (boolean): Whether or not the SSID is enabled
        - authMode (string): The association control method for the SSID ('open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius', 'ipsk-with-radius' or 'ipsk-without-radius')
        - enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only')
        - splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth' or 'Sponsored guest'). This attribute is not supported for template children.
        - radiusServers (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusCoaEnabled (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
        - radiusFailoverPolicy (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
        - radiusLoadBalancingPolicy (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
        - radiusAccountingEnabled (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusAccountingServers (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
        - radiusAttributeForGroupPolicies (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
        - ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3 roaming with a concentrator' or 'VPN')
        - useVlanTagging (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - concentratorNetworkId (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
        - vlanId (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
        - defaultVlanId (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - apTagsAndVlanIds (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - walledGardenEnabled (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
        - walledGardenRanges (string): Specify your walled garden by entering space-separated addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. 192.168.1.1/24 192.168.37.10/32 www.yahoo.com *.google.com). Meraki's splash page is automatically included in your walled garden.
        - radiusOverride (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
        - minBitrate (number): The minimum bitrate in Mbps. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
        - bandSelection (string): The client-serving radio frequencies. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
        - perClientBandwidthLimitUp (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
        - perClientBandwidthLimitDown (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
        - lanIsolationEnabled (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
        - visible (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
        - availableOnAllAps (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
        - availabilityTags (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
        """

        kwargs.update(locals())

        if 'authMode' in kwargs:
            options = ['open', 'psk', 'open-with-radius', '8021x-meraki', '8021x-radius', 'ipsk-with-radius', 'ipsk-without-radius']
            assert kwargs['authMode'] in options, f'''"authMode" cannot be "{kwargs['authMode']}", & must be set to one of: {options}'''
        if 'enterpriseAdminAccess' in kwargs:
            options = ['access disabled', 'access enabled']
            assert kwargs['enterpriseAdminAccess'] in options, f'''"enterpriseAdminAccess" cannot be "{kwargs['enterpriseAdminAccess']}", & must be set to one of: {options}'''
        if 'encryptionMode' in kwargs:
            options = ['wep', 'wpa']
            assert kwargs['encryptionMode'] in options, f'''"encryptionMode" cannot be "{kwargs['encryptionMode']}", & must be set to one of: {options}'''
        if 'wpaEncryptionMode' in kwargs:
            options = ['WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only']
            assert kwargs['wpaEncryptionMode'] in options, f'''"wpaEncryptionMode" cannot be "{kwargs['wpaEncryptionMode']}", & must be set to one of: {options}'''
        if 'splashPage' in kwargs:
            options = ['None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Sponsored guest']
            assert kwargs['splashPage'] in options, f'''"splashPage" cannot be "{kwargs['splashPage']}", & must be set to one of: {options}'''
        if 'radiusFailoverPolicy' in kwargs:
            options = ['Deny access', 'Allow access']
            assert kwargs['radiusFailoverPolicy'] in options, f'''"radiusFailoverPolicy" cannot be "{kwargs['radiusFailoverPolicy']}", & must be set to one of: {options}'''
        if 'radiusLoadBalancingPolicy' in kwargs:
            options = ['Strict priority order', 'Round robin']
            assert kwargs['radiusLoadBalancingPolicy'] in options, f'''"radiusLoadBalancingPolicy" cannot be "{kwargs['radiusLoadBalancingPolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['SSIDs'],
            'operation': 'updateNetworkSsid',
        }
        resource = f'/networks/{networkId}/ssids/{number}'

        body_params = ['name', 'enabled', 'authMode', 'enterpriseAdminAccess', 'encryptionMode', 'psk', 'wpaEncryptionMode', 'splashPage', 'radiusServers', 'radiusCoaEnabled', 'radiusFailoverPolicy', 'radiusLoadBalancingPolicy', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusAttributeForGroupPolicies', 'ipAssignmentMode', 'useVlanTagging', 'concentratorNetworkId', 'vlanId', 'defaultVlanId', 'apTagsAndVlanIds', 'walledGardenEnabled', 'walledGardenRanges', 'radiusOverride', 'minBitrate', 'bandSelection', 'perClientBandwidthLimitUp', 'perClientBandwidthLimitDown', 'lanIsolationEnabled', 'visible', 'availableOnAllAps', 'availabilityTags']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

