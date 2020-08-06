class Admins(object):
    def __init__(self, session):
        super(Admins, self).__init__()
        self._session = session
    
    def getOrganizationAdmins(self, organizationId: str):
        """
        **List the dashboard administrators in this organization**
        https://developer.cisco.com/meraki/api/#!get-organization-admins
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Admins'],
            'operation': 'getOrganizationAdmins',
        }
        resource = f'/organizations/{organizationId}/admins'

        return self._session.get(metadata, resource)

    def createOrganizationAdmin(self, organizationId: str, email: str, name: str, orgAccess: str, **kwargs):
        """
        **Create a new dashboard administrator**
        https://developer.cisco.com/meraki/api/#!create-organization-admin
        
        - organizationId (string)
        - email (string): The email of the dashboard administrator. This attribute can not be updated.
        - name (string): The name of the dashboard administrator
        - orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
        - tags (array): The list of tags that the dashboard administrator has privileges on
        - networks (array): The list of networks that the dashboard administrator has privileges on
        - authenticationMethod (string): The method of authentication the user will use to sign in to the Meraki dashboard. Can be one of 'Email' or 'Cisco SecureX Sign-On'. The default is Email authentication
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['full', 'read-only', 'enterprise', 'none']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''
        if 'authenticationMethod' in kwargs:
            options = ['Email', 'Cisco SecureX Sign-On']
            assert kwargs['authenticationMethod'] in options, f'''"authenticationMethod" cannot be "{kwargs['authenticationMethod']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Admins'],
            'operation': 'createOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins'

        body_params = ['email', 'name', 'orgAccess', 'tags', 'networks', 'authenticationMethod']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def updateOrganizationAdmin(self, organizationId: str, adminId: str, **kwargs):
        """
        **Update an administrator**
        https://developer.cisco.com/meraki/api/#!update-organization-admin
        
        - organizationId (string)
        - adminId (string)
        - name (string): The name of the dashboard administrator
        - orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
        - tags (array): The list of tags that the dashboard administrator has privileges on
        - networks (array): The list of networks that the dashboard administrator has privileges on
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['full', 'read-only', 'enterprise', 'none']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Admins'],
            'operation': 'updateOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins/{adminId}'

        body_params = ['name', 'orgAccess', 'tags', 'networks']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAdmin(self, organizationId: str, adminId: str):
        """
        **Revoke all access for a dashboard administrator within this organization**
        https://developer.cisco.com/meraki/api/#!delete-organization-admin
        
        - organizationId (string)
        - adminId (string)
        """

        metadata = {
            'tags': ['Admins'],
            'operation': 'deleteOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins/{adminId}'

        return self._session.delete(metadata, resource)

