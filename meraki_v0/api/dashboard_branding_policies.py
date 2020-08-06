class DashboardBrandingPolicies(object):
    def __init__(self, session):
        super(DashboardBrandingPolicies, self).__init__()
        self._session = session
    
    def getOrganizationBrandingPolicies(self, organizationId: str):
        """
        **List the branding policies of an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-branding-policies
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'getOrganizationBrandingPolicies',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies'

        return self._session.get(metadata, resource)

    def createOrganizationBrandingPolicy(self, organizationId: str, name: str, enabled: bool, adminSettings: dict, **kwargs):
        """
        **Add a new branding policy to an organization**
        https://developer.cisco.com/meraki/api/#!create-organization-branding-policy
        
        - organizationId (string)
        - name (string): Name of the Dashboard branding policy.
        - enabled (boolean): Boolean indicating whether this policy is enabled.
        - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
        - helpSettings (object):     Settings for describing the modifications to various Help page features. Each property in this object accepts one of
    'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
    the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
    Dashboard; see the documentation for each property to see the allowed values.
 Each property defaults to 'default or inherit' when not provided.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'createOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getOrganizationBrandingPoliciesPriorities(self, organizationId: str):
        """
        **Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).**
        https://developer.cisco.com/meraki/api/#!get-organization-branding-policies-priorities
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'getOrganizationBrandingPoliciesPriorities',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        return self._session.get(metadata, resource)

    def updateOrganizationBrandingPoliciesPriorities(self, organizationId: str, brandingPolicyIds: list):
        """
        **Update the priority ordering of an organization's branding policies.**
        https://developer.cisco.com/meraki/api/#!update-organization-branding-policies-priorities
        
        - organizationId (string)
        - brandingPolicyIds (array): A list of branding policy IDs arranged in ascending priority order (IDs later in the array have higher priority).
        """

        kwargs = locals()

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'updateOrganizationBrandingPoliciesPriorities',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        body_params = ['brandingPolicyIds']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Return a branding policy**
        https://developer.cisco.com/meraki/api/#!get-organization-branding-policy
        
        - organizationId (string)
        - brandingPolicyId (string)
        """

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'getOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        return self._session.get(metadata, resource)

    def updateOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str, **kwargs):
        """
        **Update a branding policy**
        https://developer.cisco.com/meraki/api/#!update-organization-branding-policy
        
        - organizationId (string)
        - brandingPolicyId (string)
        - name (string): Name of the Dashboard branding policy.
        - enabled (boolean): Boolean indicating whether this policy is enabled.
        - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
        - helpSettings (object):     Settings for describing the modifications to various Help page features. Each property in this object accepts one of
    'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
    the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
    Dashboard; see the documentation for each property to see the allowed values.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'updateOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Delete a branding policy**
        https://developer.cisco.com/meraki/api/#!delete-organization-branding-policy
        
        - organizationId (string)
        - brandingPolicyId (string)
        """

        metadata = {
            'tags': ['Dashboard branding policies'],
            'operation': 'deleteOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        return self._session.delete(metadata, resource)

