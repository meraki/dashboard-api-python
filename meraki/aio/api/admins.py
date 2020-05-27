class AsyncAdmins:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationAdmins(self, organizationId: str):
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

        return await self._session.get(metadata, resource)

    async def createOrganizationAdmin(self, organizationId: str, email: str, name: str, orgAccess: str, **kwargs):
        """
        **Create a new dashboard administrator**
        https://developer.cisco.com/meraki/api/#!create-organization-admin
        
        - organizationId (string)
        - email (string): The email of the dashboard administrator. This attribute can not be updated.
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
            'operation': 'createOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins'

        body_params = ['email', 'name', 'orgAccess', 'tags', 'networks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def updateOrganizationAdmin(self, organizationId: str, id: str, **kwargs):
        """
        **Update an administrator**
        https://developer.cisco.com/meraki/api/#!update-organization-admin
        
        - organizationId (string)
        - id (string)
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
        resource = f'/organizations/{organizationId}/admins/{id}'

        body_params = ['name', 'orgAccess', 'tags', 'networks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganizationAdmin(self, organizationId: str, id: str):
        """
        **Revoke all access for a dashboard administrator within this organization**
        https://developer.cisco.com/meraki/api/#!delete-organization-admin
        
        - organizationId (string)
        - id (string)
        """

        metadata = {
            'tags': ['Admins'],
            'operation': 'deleteOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins/{id}'

        return await self._session.delete(metadata, resource)

