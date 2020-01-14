class IntrusionSettings(object):
    def __init__(self, session):
        super(IntrusionSettings, self).__init__()
        self._session = session
    
    def getNetworkSecurityIntrusionSettings(self, networkId: str):
        """
        **Returns all supported intrusion settings for an MX network**
        https://api.meraki.com/api_docs#returns-all-supported-intrusion-settings-for-an-mx-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'getNetworkSecurityIntrusionSettings',
        }
        resource = f'/networks/{networkId}/security/intrusionSettings'

        return self._session.get(metadata, resource)

    def updateNetworkSecurityIntrusionSettings(self, networkId: str, **kwargs):
        """
        **Set the supported intrusion settings for an MX network**
        https://api.meraki.com/api_docs#set-the-supported-intrusion-settings-for-an-mx-network
        
        - networkId (string)
        - mode (string): Set mode to 'disabled'/'detection'/'prevention' (optional - omitting will leave current config unchanged)
        - idsRulesets (string): Set the detection ruleset 'connectivity'/'balanced'/'security' (optional - omitting will leave current config unchanged). Default value is 'balanced' if none currently saved
        - protectedNetworks (object): Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in 'passthrough' mode
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'updateNetworkSecurityIntrusionSettings',
        }
        resource = f'/networks/{networkId}/security/intrusionSettings'

        body_params = ['mode', 'idsRulesets', 'protectedNetworks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getOrganizationSecurityIntrusionSettings(self, organizationId: str):
        """
        **Returns all supported intrusion settings for an organization**
        https://api.meraki.com/api_docs#returns-all-supported-intrusion-settings-for-an-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'getOrganizationSecurityIntrusionSettings',
        }
        resource = f'/organizations/{organizationId}/security/intrusionSettings'

        return self._session.get(metadata, resource)

    def updateOrganizationSecurityIntrusionSettings(self, organizationId: str, whitelistedRules: list):
        """
        **Sets supported intrusion settings for an organization**
        https://api.meraki.com/api_docs#sets-supported-intrusion-settings-for-an-organization
        
        - organizationId (string)
        - whitelistedRules (array): Sets a list of specific SNORT® signatures to whitelist
        """

        kwargs = locals()

        metadata = {
            'tags': ['Intrusion settings'],
            'operation': 'updateOrganizationSecurityIntrusionSettings',
        }
        resource = f'/organizations/{organizationId}/security/intrusionSettings'

        body_params = ['whitelistedRules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

