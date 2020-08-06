class AsyncSNMPSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkSnmpSettings(self, networkId: str):
        """
        **Return the SNMP settings for a network**
        https://developer.cisco.com/meraki/api/#!get-network-snmp-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['SNMP settings'],
            'operation': 'getNetworkSnmpSettings',
        }
        resource = f'/networks/{networkId}/snmpSettings'

        return await self._session.get(metadata, resource)

    async def updateNetworkSnmpSettings(self, networkId: str, **kwargs):
        """
        **Update the SNMP settings for a network**
        https://developer.cisco.com/meraki/api/#!update-network-snmp-settings
        
        - networkId (string)
        - access (string): The type of SNMP access. Can be one of 'none' (disabled), 'community' (V1/V2c), or 'users' (V3).
        - communityString (string): The SNMP community string. Only relevant if 'access' is set to 'community'.
        - users (array): The list of SNMP users. Only relevant if 'access' is set to 'users'.
        """

        kwargs.update(locals())

        if 'access' in kwargs:
            options = ['none', 'community', 'users']
            assert kwargs['access'] in options, f'''"access" cannot be "{kwargs['access']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['SNMP settings'],
            'operation': 'updateNetworkSnmpSettings',
        }
        resource = f'/networks/{networkId}/snmpSettings'

        body_params = ['access', 'communityString', 'users']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getOrganizationSnmp(self, organizationId: str):
        """
        **Return the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-snmp
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['SNMP settings'],
            'operation': 'getOrganizationSnmp',
        }
        resource = f'/organizations/{organizationId}/snmp'

        return await self._session.get(metadata, resource)

    async def updateOrganizationSnmp(self, organizationId: str, **kwargs):
        """
        **Update the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api/#!update-organization-snmp
        
        - organizationId (string)
        - v2cEnabled (boolean): Boolean indicating whether SNMP version 2c is enabled for the organization.
        - v3Enabled (boolean): Boolean indicating whether SNMP version 3 is enabled for the organization.
        - v3AuthMode (string): The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
        - v3AuthPass (string): The SNMP version 3 authentication password. Must be at least 8 characters if specified.
        - v3PrivMode (string): The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
        - v3PrivPass (string): The SNMP version 3 privacy password. Must be at least 8 characters if specified.
        - peerIps (string): The IPs that are allowed to access the SNMP server. This list should be IPv4 addresses separated by semi-colons (ie. "1.2.3.4;2.3.4.5").
        """

        kwargs.update(locals())

        if 'v3AuthMode' in kwargs:
            options = ['MD5', 'SHA']
            assert kwargs['v3AuthMode'] in options, f'''"v3AuthMode" cannot be "{kwargs['v3AuthMode']}", & must be set to one of: {options}'''
        if 'v3PrivMode' in kwargs:
            options = ['DES', 'AES128']
            assert kwargs['v3PrivMode'] in options, f'''"v3PrivMode" cannot be "{kwargs['v3PrivMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['SNMP settings'],
            'operation': 'updateOrganizationSnmp',
        }
        resource = f'/organizations/{organizationId}/snmp'

        body_params = ['v2cEnabled', 'v3Enabled', 'v3AuthMode', 'v3AuthPass', 'v3PrivMode', 'v3PrivPass', 'peerIps']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

