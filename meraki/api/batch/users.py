import urllib


class ActionBatchUsers(object):
    def __init__(self):
        super(ActionBatchUsers, self).__init__()

    def createOrganizationIamUsersAuthorization(self, organizationId: str, authZone: dict, **kwargs):
        """
        **Authorize a Meraki end user for an auth zone.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-authorization

        - organizationId (string): Organization ID
        - authZone (object): Auth zone
        - email (string): Meraki end user's email
        - idpUserId (string): Meraki end user's ID
        - startsAt (string): Start time of the desired access for the authorization. Defaults to now.
        - expiresAt (string): Expiration time of the desired access for the authorization
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations"

        body_params = [
            "email",
            "idpUserId",
            "authZone",
            "startsAt",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationIamUsersAuthorizations(self, organizationId: str, **kwargs):
        """
        **Update a Meraki end user's access to an auth zone.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-iam-users-authorizations

        - organizationId (string): Organization ID
        - authorizationId (string): Authorization ID
        - email (string): Meraki end user's email
        - authZone (object): Auth zone
        - startsAt (string): Start time of the desired access for the authorization
        - expiresAt (string): Expiration time of the desired access for the authorization
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations"

        body_params = [
            "authorizationId",
            "email",
            "authZone",
            "startsAt",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def revokeOrganizationIamUsersAuthorizationsAuthorization(self, organizationId: str, authZone: dict, **kwargs):
        """
        **Revoke a Meraki end user's access to an auth zone.**
        https://developer.cisco.com/meraki/api-v1/#!revoke-organization-iam-users-authorizations-authorization

        - organizationId (string): Organization ID
        - authZone (object): Auth zone
        - email (string): Meraki end user's email
        - authorizationId (string): Authorization ID
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations/authorization/revoke"

        body_params = [
            "email",
            "authorizationId",
            "authZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "revoke",
            "body": payload,
        }
        return action

    def deleteOrganizationIamUsersAuthorization(self, organizationId: str, authorizationId: str):
        """
        **Delete an authorization for a Meraki end user.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-iam-users-authorization

        - organizationId (string): Organization ID
        - authorizationId (string): Authorization ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        authorizationId = urllib.parse.quote(authorizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations/{authorizationId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationIamUsersIdp(self, organizationId: str, name: str, type: str, idpConfig: dict, **kwargs):
        """
        **Create an identity provider for an organization. Only Entra ID(Azure AD) is supported at this time.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idp

        - organizationId (string): Organization ID
        - name (string): Name of the identity provider
        - type (string): Type of the identity provider
        - idpConfig (object): Identity provider configuration. Required for external identity providers.
        - description (string): Optional. Description of the identity provider
        - syncType (string): The synchronization method for the identity provider. Set to 'proactive' to sync all users and groups from your identity provider.
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["Azure AD"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''
        if "syncType" in kwargs and kwargs["syncType"] is not None:
            options = ["proactive"]
            assert kwargs["syncType"] in options, (
                f'''"syncType" cannot be "{kwargs["syncType"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps"

        body_params = [
            "name",
            "type",
            "description",
            "idpConfig",
            "syncType",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def createOrganizationIamUsersIdpsTestConnectivity(self, organizationId: str, **kwargs):
        """
        **Test connectivity to an Entra ID identity provider.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idps-test-connectivity

        - organizationId (string): Organization ID
        - idpId (string): Id of the identity provider
        - idpConfig (object): Identity provider configuration. Required for external identity providers.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/testConnectivity"

        body_params = [
            "idpId",
            "idpConfig",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "test_connectivity",
            "body": payload,
        }
        return action

    def createOrganizationIamUsersIdpsUser(self, organizationId: str, **kwargs):
        """
        **Create a Meraki user**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idps-user

        - organizationId (string): Organization ID
        - displayName (string): A human-readable identifier for the created user.
        - email (string): An email address identified with the user.
        - password (string): The password for the user account.
        - sendPassword (boolean): If true, sends an email with the password to the user.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/users"

        body_params = [
            "displayName",
            "email",
            "password",
            "sendPassword",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationIamUsersIdpsUser(self, organizationId: str, id: str, **kwargs):
        """
        **Update a Meraki user**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-iam-users-idps-user

        - organizationId (string): Organization ID
        - id (string): ID
        - displayName (string): A human-readable identifier for the created user.
        - email (string): An email address identified with the user.
        - password (string): The password for the user account.
        - sendPassword (boolean): If true, sends an email with the password to the user.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/users/{id}"

        body_params = [
            "displayName",
            "email",
            "password",
            "sendPassword",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationIamUsersIdpsUser(self, organizationId: str, id: str):
        """
        **Delete a Meraki end user**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-iam-users-idps-user

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/users/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationIamUsersIdpSync(self, organizationId: str, idpId: str, **kwargs):
        """
        **Trigger an IdP sync for an identity provider. Only Entra ID(Azure AD) is supported at this time.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idp-sync

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        - emails (array): List of emails to sync
        - force (boolean): Force a complete sync of all users and groups
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        idpId = urllib.parse.quote(idpId, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{idpId}/sync"

        body_params = [
            "emails",
            "force",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationIamUsersIdp(self, organizationId: str, id: str, **kwargs):
        """
        **Update an identity provider. Only Entra ID(Azure AD) is supported at this time.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-iam-users-idp

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of the identity provider
        - description (string): Description of the identity provider
        - idpConfig (object): Identity provider configuration. You can update individual attributes
        - syncType (string): The synchronization method for the identity provider. Set to 'proactive' to sync all users and groups from your identity provider. Set to 'null' for on-demand user and group provisioning.
        """

        kwargs.update(locals())

        if "syncType" in kwargs and kwargs["syncType"] is not None:
            options = ["proactive"]
            assert kwargs["syncType"] in options, (
                f'''"syncType" cannot be "{kwargs["syncType"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{id}"

        body_params = [
            "name",
            "description",
            "idpConfig",
            "syncType",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationIamUsersIdp(self, organizationId: str, id: str):
        """
        **Delete a identity provider from an organization. Only Entra ID(Azure AD) is supported at this time.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-iam-users-idp

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
