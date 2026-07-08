import urllib


class Users(object):
    def __init__(self, session):
        super(Users, self).__init__()
        self._session = session

    def getOrganizationIamUsersAuthorizations(
        self, organizationId: str, userIds: list, total_pages=1, direction="next", **kwargs
    ):
        """
        **List specific authorizations for the list of Meraki end users.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-authorizations

        - organizationId (string): Organization ID
        - userIds (array): Meraki end user IDs
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["users", "configure", "iam", "authorizations"],
            "operation": "getOrganizationIamUsersAuthorizations",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "userIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "userIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationIamUsersAuthorizations: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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

        metadata = {
            "tags": ["users", "configure", "iam", "authorizations"],
            "operation": "createOrganizationIamUsersAuthorization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations"

        body_params = [
            "email",
            "idpUserId",
            "authZone",
            "startsAt",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationIamUsersAuthorization: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["users", "configure", "iam", "authorizations"],
            "operation": "updateOrganizationIamUsersAuthorizations",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations"

        body_params = [
            "authorizationId",
            "email",
            "authZone",
            "startsAt",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationIamUsersAuthorizations: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

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

        metadata = {
            "tags": ["users", "configure", "iam", "authorizations", "authorization"],
            "operation": "revokeOrganizationIamUsersAuthorizationsAuthorization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations/authorization/revoke"

        body_params = [
            "email",
            "authorizationId",
            "authZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"revokeOrganizationIamUsersAuthorizationsAuthorization: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationIamUsersAuthorizationsZones(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List all of the available auth zones for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-authorizations-zones

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["users", "configure", "iam", "authorizations", "zones"],
            "operation": "getOrganizationIamUsersAuthorizationsZones",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations/zones"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationIamUsersAuthorizationsZones: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationIamUsersAuthorization(self, organizationId: str, authorizationId: str):
        """
        **Delete an authorization for a Meraki end user.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-iam-users-authorization

        - organizationId (string): Organization ID
        - authorizationId (string): Authorization ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "authorizations"],
            "operation": "deleteOrganizationIamUsersAuthorization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        authorizationId = urllib.parse.quote(str(authorizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/authorizations/{authorizationId}"

        return self._session.delete(metadata, resource)

    def createOrganizationIamUsersIdp(self, organizationId: str, name: str, type: str, idpConfig: dict, **kwargs):
        """
        **Create an identity provider for an organization**
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

        metadata = {
            "tags": ["users", "configure", "iam", "idps"],
            "operation": "createOrganizationIamUsersIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps"

        body_params = [
            "name",
            "type",
            "description",
            "idpConfig",
            "syncType",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationIamUsersIdp: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def searchOrganizationIdpGroups(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Search all IdP groups for an organization**
        https://developer.cisco.com/meraki/api-v1/#!search-organization-idp-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - idpIds (array): Filter IdP groups by IdP ID(s). Multiple IdP IDs can be passed as a comma separated list.
        - authZone (object): Auth zone
        - searchQuery (string): Fuzzy filter by group name
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "groups", "search"],
            "operation": "searchOrganizationIdpGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/groups/search"

        body_params = [
            "idpIds",
            "authZone",
            "searchQuery",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"searchOrganizationIdpGroups: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationIamUsersIdpsProductIntegrations(self, organizationId: str):
        """
        **List all available IdP Product Integration urls for the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-idps-product-integrations

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "productIntegrations"],
            "operation": "getOrganizationIamUsersIdpsProductIntegrations",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/productIntegrations"

        return self._session.get(metadata, resource)

    def createOrganizationIamUsersIdpsSearch(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Search all IdPs for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idps-search

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - idpIds (array): Filter identity providers by id(s). Multiple ids can be passed as a comma separated list.
        - type (string): Filter identity providers by idp type.
        - authZone (object): Filter by auth zone
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["Azure AD"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "search"],
            "operation": "createOrganizationIamUsersIdpsSearch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/search"

        body_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "idpIds",
            "type",
            "authZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationIamUsersIdpsSearch: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationIamUsersIdpsSyncHistory(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get the IdP sync status records for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-idps-sync-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - idpId (string): Identity provider ID. Optional.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "sync", "history"],
            "operation": "getOrganizationIamUsersIdpsSyncHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/sync/history"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "idpId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationIamUsersIdpsSyncHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationIamUsersIdpsSyncLatest(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get the latest IdP sync status records for all IdPs in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-idps-sync-latest

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - idpIds (array): Identity provider IDs. Optional.
        - authZoneId (string): Auth Zone ID
        - authZoneType (string): Auth Zone type
        """

        kwargs.update(locals())

        if "authZoneType" in kwargs:
            options = ["access_policy", "node_group", "product", "ssid"]
            assert kwargs["authZoneType"] in options, (
                f'''"authZoneType" cannot be "{kwargs["authZoneType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "sync", "latest"],
            "operation": "getOrganizationIamUsersIdpsSyncLatest",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/sync/latest"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "idpIds",
            "authZoneId",
            "authZoneType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "idpIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationIamUsersIdpsSyncLatest: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationIamUsersIdpsTestConnectivity(self, organizationId: str, **kwargs):
        """
        **Test connectivity to an Entra ID identity provider.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idps-test-connectivity

        - organizationId (string): Organization ID
        - idpId (string): Id of the identity provider
        - idpConfig (object): Identity provider configuration. Required for external identity providers.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "testConnectivity"],
            "operation": "createOrganizationIamUsersIdpsTestConnectivity",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/testConnectivity"

        body_params = [
            "idpId",
            "idpConfig",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationIamUsersIdpsTestConnectivity: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["users", "configure", "iam", "idps"],
            "operation": "createOrganizationIamUsersIdpsUser",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/users"

        body_params = [
            "displayName",
            "email",
            "password",
            "sendPassword",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationIamUsersIdpsUser: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["users", "configure", "iam", "idps"],
            "operation": "updateOrganizationIamUsersIdpsUser",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/users/{id}"

        body_params = [
            "displayName",
            "email",
            "password",
            "sendPassword",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationIamUsersIdpsUser: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationIamUsersIdpsUser(self, organizationId: str, id: str):
        """
        **Delete a Meraki end user**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-iam-users-idps-user

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "idps"],
            "operation": "deleteOrganizationIamUsersIdpsUser",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/users/{id}"

        return self._session.delete(metadata, resource)

    def createOrganizationIamUsersIdpSync(self, organizationId: str, idpId: str, **kwargs):
        """
        **Trigger an IdP sync for an identity provider**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-iam-users-idp-sync

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        - emails (array): List of emails to sync
        - force (boolean): Force a complete sync of all users and groups
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "sync"],
            "operation": "createOrganizationIamUsersIdpSync",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        idpId = urllib.parse.quote(str(idpId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{idpId}/sync"

        body_params = [
            "emails",
            "force",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationIamUsersIdpSync: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationIamUsersIdpSyncLatest(self, organizationId: str, idpId: str):
        """
        **Get the latest IdP sync status for an identity provider**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-idp-sync-latest

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "sync", "latest"],
            "operation": "getOrganizationIamUsersIdpSyncLatest",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        idpId = urllib.parse.quote(str(idpId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{idpId}/sync/latest"

        return self._session.get(metadata, resource)

    def updateOrganizationIamUsersIdp(self, organizationId: str, id: str, **kwargs):
        """
        **Update an identity provider**
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

        metadata = {
            "tags": ["users", "configure", "iam", "idps"],
            "operation": "updateOrganizationIamUsersIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{id}"

        body_params = [
            "name",
            "description",
            "idpConfig",
            "syncType",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationIamUsersIdp: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationIamUsersIdp(self, organizationId: str, id: str):
        """
        **Delete a identity provider from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-iam-users-idp

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "idps"],
            "operation": "deleteOrganizationIamUsersIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationIamUsersIdpAuthZones(self, organizationId: str, id: str):
        """
        **List all auth zones for an identity provider**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-idp-auth-zones

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "idps", "authZones"],
            "operation": "getOrganizationIamUsersIdpAuthZones",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/iam/users/idps/{id}/authZones"

        return self._session.get(metadata, resource)

    def searchOrganizationUsers(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the end users and their associated identity providers for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!search-organization-users

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - userIds (array): Filter end users by id(s).
        - idpIds (array): Filter by identity provider id(s).
        - groupIds (array): Filter by identity provider group id(s).
        - accessTypes (array): Filter by access type(s).
        - searchQuery (string): Fuzzy filter by display name, user name and email.
        - statuses (array): Filter by user status(es).
        - sortKey (string): Optional parameter to specify the field used to sort results. (default: username)
        - sortOrder (string): Optional parameter to specify the sort order. (default: asc)
        """

        kwargs.update(locals())

        if "sortKey" in kwargs:
            options = ["created_at", "updated_at", "username"]
            assert kwargs["sortKey"] in options, (
                f'''"sortKey" cannot be "{kwargs["sortKey"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["users", "configure", "iam", "search"],
            "operation": "searchOrganizationUsers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/search"

        body_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "userIds",
            "idpIds",
            "groupIds",
            "accessTypes",
            "searchQuery",
            "statuses",
            "sortKey",
            "sortOrder",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"searchOrganizationUsers: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationIamUsersSummaryPanel(self, organizationId: str):
        """
        **Get the count of users and user groups for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-iam-users-summary-panel

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["users", "configure", "iam", "summaryPanel"],
            "operation": "getOrganizationIamUsersSummaryPanel",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/users/summaryPanel"

        return self._session.get(metadata, resource)
