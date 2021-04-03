class ActionBatchOrganizations(object):
    def __init__(self):
        super(ActionBatchOrganizations, self).__init__()
        


    def createOrganizationConfigTemplate(self, organizationId: str, name: str, **kwargs):
        """
        **Create a new configuration template**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        - organizationId (string): (required)
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
        - copyFromNetworkId (string): The ID of the network or config template to copy configuration from
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'createOrganizationConfigTemplate'
        }
        resource = f'/organizations/{organizationId}/configTemplates'

        body_params = ['name', 'timeZone', 'copyFromNetworkId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str, **kwargs):
        """
        **Update a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        - organizationId (string): (required)
        - configTemplateId (string): (required)
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'updateOrganizationConfigTemplate'
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        body_params = ['name', 'timeZone', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def assignOrganizationLicensesSeats(self, organizationId: str, licenseId: str, networkId: str, seatCount: int):
        """
        **Assign SM seats to a network**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        - organizationId (string): (required)
        - licenseId (string): The ID of the SM license to assign seats from
        - networkId (string): The ID of the SM network to assign the seats to
        - seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'assignOrganizationLicensesSeats'
        }
        resource = f'/organizations/{organizationId}/licenses/assignSeats'

        body_params = ['licenseId', 'networkId', 'seatCount', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def moveOrganizationLicenses(self, organizationId: str, destOrganizationId: str, licenseIds: list):
        """
        **Move licenses to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        - organizationId (string): (required)
        - destOrganizationId (string): The ID of the organization to move the licenses to
        - licenseIds (array): A list of IDs of licenses to move to the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'moveOrganizationLicenses'
        }
        resource = f'/organizations/{organizationId}/licenses/move'

        body_params = ['destOrganizationId', 'licenseIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def moveOrganizationLicensesSeats(self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int):
        """
        **Move SM seats to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        - organizationId (string): (required)
        - destOrganizationId (string): The ID of the organization to move the SM seats to
        - licenseId (string): The ID of the SM license to move the seats from
        - seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'moveOrganizationLicensesSeats'
        }
        resource = f'/organizations/{organizationId}/licenses/moveSeats'

        body_params = ['destOrganizationId', 'licenseId', 'seatCount', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def renewOrganizationLicensesSeats(self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str):
        """
        **Renew SM seats of a license**
        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        - organizationId (string): (required)
        - licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
        - unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'renewOrganizationLicensesSeats'
        }
        resource = f'/organizations/{organizationId}/licenses/renewSeats'

        body_params = ['licenseIdToRenew', 'unusedLicenseId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        - organizationId (string): (required)
        - licenseId (string): (required)
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'updateOrganizationLicense'
        }
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        body_params = ['deviceSerial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateOrganizationLoginSecurity(self, organizationId: str, **kwargs):
        """
        **Update the login security settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        - organizationId (string): (required)
        - enforcePasswordExpiration (boolean): Boolean indicating whether users are forced to change their password every X number of days.
        - passwordExpirationDays (integer): Number of days after which users will be forced to change their password.
        - enforceDifferentPasswords (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
        - numDifferentPasswords (integer): Number of recent passwords that new password must be distinct from.
        - enforceStrongPasswords (boolean): Boolean indicating whether users will be forced to choose strong passwords for their accounts. Strong passwords are at least 8 characters that contain 3 of the following: number, uppercase letter, lowercase letter, and symbol
        - enforceAccountLockout (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
        - accountLockoutAttempts (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
        - enforceIdleTimeout (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
        - idleTimeoutMinutes (integer): Number of minutes users can remain idle before being logged out of their accounts.
        - enforceTwoFactorAuth (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the Google Authenticator application.
        - enforceLoginIpRanges (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
        - loginIpRanges (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'loginSecurity'],
            'operation': 'updateOrganizationLoginSecurity'
        }
        resource = f'/organizations/{organizationId}/loginSecurity'

        body_params = ['enforcePasswordExpiration', 'passwordExpirationDays', 'enforceDifferentPasswords', 'numDifferentPasswords', 'enforceStrongPasswords', 'enforceAccountLockout', 'accountLockoutAttempts', 'enforceIdleTimeout', 'idleTimeoutMinutes', 'enforceTwoFactorAuth', 'enforceLoginIpRanges', 'loginIpRanges', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createOrganizationNetwork(self, organizationId: str, name: str, productTypes: list, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        - organizationId (string): (required)
        - name (string): The name of the new network
        - productTypes (array): The product type(s) of the new network. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, environmental. If more than one type is included, the network will be a combined network.
        - tags (array): A list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        - notes (string): Add any notes or additional information about this network here.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'createOrganizationNetwork'
        }
        resource = f'/organizations/{organizationId}/networks'

        body_params = ['name', 'productTypes', 'tags', 'timeZone', 'copyFromNetworkId', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def combineOrganizationNetworks(self, organizationId: str, name: str, networkIds: list, **kwargs):
        """
        **Combine multiple networks into a single network**
        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        - organizationId (string): (required)
        - name (string): The name of the combined network
        - networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'combineOrganizationNetworks'
        }
        resource = f'/organizations/{organizationId}/networks/combine'

        body_params = ['name', 'networkIds', 'enrollmentString', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def createOrganizationSamlIdp(self, organizationId: str, x509certSha1Fingerprint: str, **kwargs):
        """
        **Create a SAML IdP for your organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        - organizationId (string): (required)
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'createOrganizationSamlIdp'
        }
        resource = f'/organizations/{organizationId}/saml/idps'

        body_params = ['x509certSha1Fingerprint', 'sloLogoutUrl', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationSamlIdp(self, organizationId: str, idpId: str, **kwargs):
        """
        **Update a SAML IdP in your organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        - organizationId (string): (required)
        - idpId (string): (required)
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'updateOrganizationSamlIdp'
        }
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        body_params = ['x509certSha1Fingerprint', 'sloLogoutUrl', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationSamlIdp(self, organizationId: str, idpId: str):
        """
        **Remove a SAML IdP in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        - organizationId (string): (required)
        - idpId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'deleteOrganizationSamlIdp'
        }
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        



