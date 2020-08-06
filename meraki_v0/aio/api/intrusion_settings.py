class AsyncIntrusionSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkSecurityIntrusionSettings(self, networkId: str):
        """
        **Returns all supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api/#!get-network-security-intrusion-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'getNetworkSecurityIntrusionSettings',
        }
        resource = f'/networks/{networkId}/security/intrusionSettings'

        return await self._session.get(metadata, resource)

    async def updateNetworkSecurityIntrusionSettings(self, networkId: str, **kwargs):
        """
        **Set the supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api/#!update-network-security-intrusion-settings
        
        - networkId (string)
        - mode (string): Set mode to 'disabled'/'detection'/'prevention' (optional - omitting will leave current config unchanged)
        - idsRulesets (string): Set the detection ruleset 'connectivity'/'balanced'/'security' (optional - omitting will leave current config unchanged). Default value is 'balanced' if none currently saved
        - protectedNetworks (object): Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in 'passthrough' mode
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['prevention', 'detection', 'disabled']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''
        if 'idsRulesets' in kwargs:
            options = ['connectivity', 'balanced', 'security']
            assert kwargs['idsRulesets'] in options, f'''"idsRulesets" cannot be "{kwargs['idsRulesets']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'updateNetworkSecurityIntrusionSettings',
        }
        resource = f'/networks/{networkId}/security/intrusionSettings'

        body_params = ['mode', 'idsRulesets', 'protectedNetworks']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getOrganizationSecurityIntrusionSettings(self, organizationId: str):
        """
        **Returns all supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-security-intrusion-settings
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'getOrganizationSecurityIntrusionSettings',
        }
        resource = f'/organizations/{organizationId}/security/intrusionSettings'

        return await self._session.get(metadata, resource)

    async def updateOrganizationSecurityIntrusionSettings(self, organizationId: str, whitelistedRules: list):
        """
        **Sets supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api/#!update-organization-security-intrusion-settings
        
        - organizationId (string)
        - whitelistedRules (array): Sets a list of specific SNORT® signatures to allow
        """

        kwargs = locals()

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'updateOrganizationSecurityIntrusionSettings',
        }
        resource = f'/organizations/{organizationId}/security/intrusionSettings'

        body_params = ['whitelistedRules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

