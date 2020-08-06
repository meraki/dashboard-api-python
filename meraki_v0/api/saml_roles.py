class SAMLRoles(object):
    def __init__(self, session):
        super(SAMLRoles, self).__init__()
        self._session = session
    
    def getOrganizationSamlRoles(self, organizationId: str):
        """
        **List the SAML roles for this organization**
        https://developer.cisco.com/meraki/api/#!get-organization-saml-roles
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['SAML roles'],
            'operation': 'getOrganizationSamlRoles',
        }
        resource = f'/organizations/{organizationId}/samlRoles'

        return self._session.get(metadata, resource)

    def createOrganizationSamlRole(self, organizationId: str, role: str, orgAccess: str, **kwargs):
        """
        **Create a SAML role**
        https://developer.cisco.com/meraki/api/#!create-organization-saml-role
        
        - organizationId (string)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SAML roles'],
            'operation': 'createOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles'

        body_params = ['role', 'orgAccess', 'tags', 'networks']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Return a SAML role**
        https://developer.cisco.com/meraki/api/#!get-organization-saml-role
        
        - organizationId (string)
        - samlRoleId (string)
        """

        metadata = {
            'tags': ['SAML roles'],
            'operation': 'getOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return self._session.get(metadata, resource)

    def updateOrganizationSamlRole(self, organizationId: str, samlRoleId: str, **kwargs):
        """
        **Update a SAML role**
        https://developer.cisco.com/meraki/api/#!update-organization-saml-role
        
        - organizationId (string)
        - samlRoleId (string)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SAML roles'],
            'operation': 'updateOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        body_params = ['role', 'orgAccess', 'tags', 'networks']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Remove a SAML role**
        https://developer.cisco.com/meraki/api/#!delete-organization-saml-role
        
        - organizationId (string)
        - samlRoleId (string)
        """

        metadata = {
            'tags': ['SAML roles'],
            'operation': 'deleteOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return self._session.delete(metadata, resource)

