class AsyncLicenses:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationLicenses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the licenses for an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-licenses
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - deviceSerial (string): Filter the licenses to those assigned to a particular device
        - networkId (string): Filter the licenses to those assigned in a particular network
        - state (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'unused', 'unusedActive' or 'recentlyQueued'
        """

        kwargs.update(locals())

        if 'state' in kwargs:
            options = ['active', 'expired', 'expiring', 'unused', 'unusedActive', 'recentlyQueued']
            assert kwargs['state'] in options, f'''"state" cannot be "{kwargs['state']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Licenses'],
            'operation': 'getOrganizationLicenses',
        }
        resource = f'/organizations/{organizationId}/licenses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def assignOrganizationLicensesSeats(self, organizationId: str, licenseId: str, networkId: str, seatCount: int):
        """
        **Assign SM seats to a network. This will increase the managed SM device limit of the network**
        https://developer.cisco.com/meraki/api/#!assign-organization-licenses-seats
        
        - organizationId (string)
        - licenseId (string): The ID of the SM license to assign seats from
        - networkId (string): The ID of the SM network to assign the seats to
        - seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['Licenses'],
            'operation': 'assignOrganizationLicensesSeats',
        }
        resource = f'/organizations/{organizationId}/licenses/assignSeats'

        body_params = ['licenseId', 'networkId', 'seatCount']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def moveOrganizationLicenses(self, organizationId: str, destOrganizationId: str, licenseIds: list):
        """
        **Move licenses to another organization. This will also move any devices that the licenses are assigned to**
        https://developer.cisco.com/meraki/api/#!move-organization-licenses
        
        - organizationId (string)
        - destOrganizationId (string): The ID of the organization to move the licenses to
        - licenseIds (array): A list of IDs of licenses to move to the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['Licenses'],
            'operation': 'moveOrganizationLicenses',
        }
        resource = f'/organizations/{organizationId}/licenses/move'

        body_params = ['destOrganizationId', 'licenseIds']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def moveOrganizationLicensesSeats(self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int):
        """
        **Move SM seats to another organization**
        https://developer.cisco.com/meraki/api/#!move-organization-licenses-seats
        
        - organizationId (string)
        - destOrganizationId (string): The ID of the organization to move the SM seats to
        - licenseId (string): The ID of the SM license to move the seats from
        - seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['Licenses'],
            'operation': 'moveOrganizationLicensesSeats',
        }
        resource = f'/organizations/{organizationId}/licenses/moveSeats'

        body_params = ['destOrganizationId', 'licenseId', 'seatCount']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def renewOrganizationLicensesSeats(self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str):
        """
        **Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license**
        https://developer.cisco.com/meraki/api/#!renew-organization-licenses-seats
        
        - organizationId (string)
        - licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
        - unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'
        """

        kwargs = locals()

        metadata = {
            'tags': ['Licenses'],
            'operation': 'renewOrganizationLicensesSeats',
        }
        resource = f'/organizations/{organizationId}/licenses/renewSeats'

        body_params = ['licenseIdToRenew', 'unusedLicenseId']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationLicense(self, organizationId: str, licenseId: str):
        """
        **Display a license**
        https://developer.cisco.com/meraki/api/#!get-organization-license
        
        - organizationId (string)
        - licenseId (string)
        """

        metadata = {
            'tags': ['Licenses'],
            'operation': 'getOrganizationLicense',
        }
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        return await self._session.get(metadata, resource)

    async def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api/#!update-organization-license
        
        - organizationId (string)
        - licenseId (string)
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Licenses'],
            'operation': 'updateOrganizationLicense',
        }
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        body_params = ['deviceSerial']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

