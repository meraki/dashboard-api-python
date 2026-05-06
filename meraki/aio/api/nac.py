import urllib


class AsyncNac:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getOrganizationNacAuthorizationPolicies(self, organizationId: str, **kwargs):
        """
        **Get all nac authorization policies for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-authorization-policies

        - organizationId (string): Organization ID
        - policyIds (array): List of ids for specific authorization policies retrieval
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "authorization", "policies"],
            "operation": "getOrganizationNacAuthorizationPolicies",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/authorization/policies"

        query_params = [
            "policyIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "policyIds",
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
                    f"getOrganizationNacAuthorizationPolicies: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def createOrganizationNacAuthorizationPolicyRule(
        self, organizationId: str, policyId: str, name: str, rank: int, authorizationProfile: dict, **kwargs
    ):
        """
        **Create a rule in an authorization policy set of an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-authorization-policy-rule

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        - name (string): Name of Authorization rule
        - rank (integer): Rank of Authorization rule
        - authorizationProfile (object): Authorization profile associated with the rule
        - enabled (boolean): Enabled status of authorization rule. Default is False.
        - sourcePolicyVersion (string): Source policy version of the policy set containing this rule
        - condition (object): Condition of Authorization rule.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "authorization", "policies", "rules"],
            "operation": "createOrganizationNacAuthorizationPolicyRule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyId = urllib.parse.quote(str(policyId), safe="")
        resource = f"/organizations/{organizationId}/nac/authorization/policies/{policyId}/rules"

        body_params = [
            "name",
            "rank",
            "enabled",
            "sourcePolicyVersion",
            "authorizationProfile",
            "condition",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationNacAuthorizationPolicyRule: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationNacAuthorizationPolicyRule(
        self, organizationId: str, policyId: str, ruleId: str, name: str, rank: int, authorizationProfile: dict, **kwargs
    ):
        """
        **Update an existing rule of an authorization policy set within an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-authorization-policy-rule

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        - ruleId (string): Rule ID
        - name (string): Name of Authorization rule
        - rank (integer): Rank of Authorization rule
        - authorizationProfile (object): Authorization profile associated with the rule
        - enabled (boolean): Enabled status of authorization rule. Default is False.
        - sourcePolicyVersion (string): Source policy version of the policy set containing this rule
        - condition (object): Condition of Authorization rule.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "authorization", "policies", "rules"],
            "operation": "updateOrganizationNacAuthorizationPolicyRule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyId = urllib.parse.quote(str(policyId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/organizations/{organizationId}/nac/authorization/policies/{policyId}/rules/{ruleId}"

        body_params = [
            "name",
            "rank",
            "enabled",
            "sourcePolicyVersion",
            "authorizationProfile",
            "condition",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationNacAuthorizationPolicyRule: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationNacAuthorizationPolicyRule(self, organizationId: str, policyId: str, ruleId: str, **kwargs):
        """
        **Delete a rule in an authorization policy set of an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-nac-authorization-policy-rule

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        - ruleId (string): Rule ID
        - sourcePolicyVersion (string): Source policy version of the policy set containing this rule
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "authorization", "policies", "rules"],
            "operation": "deleteOrganizationNacAuthorizationPolicyRule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyId = urllib.parse.quote(str(policyId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/organizations/{organizationId}/nac/authorization/policies/{policyId}/rules/{ruleId}"

        return self._session.delete(metadata, resource)

    def getOrganizationNacCertificates(self, organizationId: str, **kwargs):
        """
        **Gets all certificates for an organization and can filter by certificate status, expiry date and last used date**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-certificates

        - organizationId (string): Organization ID
        - status (string): Status Parameter for GetAll request
        - expiry (boolean): Boolean indicating whether to filter by expiry in one month
        - lastUsed (boolean): Boolean indicating whether to filter by last used in over one month
        """

        kwargs.update(locals())

        if "status" in kwargs:
            options = ["Disabled", "Enabled"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["nac", "configure", "certificates"],
            "operation": "getOrganizationNacCertificates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates"

        query_params = [
            "status",
            "expiry",
            "lastUsed",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationNacCertificates: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationNacCertificatesAuthoritiesCrls(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get all the organization's CRL.It's possible to filter results by CRL issuers (CA) or CRL's ID - see caIds and crlIds query parameters.This endpoint could be used for 'show' action when you specify a single CRL ID in crlIds parameter**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-certificates-authorities-crls

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 5.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortBy (string): Optional parameter to specify the field used to sort results. (default: caId)
        - sortOrder (string): Optional parameter to specify the sort order. (default: asc)
        - crlIds (array): A list of CRL ids. The returned CRLs will be filtered to only include these ids
        - caIds (array): When ca Ids are provided, only CRLs associated to the given CA will be returned. Otherwise, all the CRLs created for an organization will be returned.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["caId", "createdAt", "lastUpdatedAt"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["nac", "configure", "certificates", "authorities", "crls"],
            "operation": "getOrganizationNacCertificatesAuthoritiesCrls",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortBy",
            "sortOrder",
            "crlIds",
            "caIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "crlIds",
            "caIds",
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
                    f"getOrganizationNacCertificatesAuthoritiesCrls: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationNacCertificatesAuthoritiesCrl(
        self, organizationId: str, caId: str, content: str, isDelta: bool, **kwargs
    ):
        """
        **Create a new CRL (either base or delta) for an existing CA**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-authorities-crl

        - organizationId (string): Organization ID
        - caId (string): ID of the CRL issuer
        - content (string): CRL content in PEM format
        - isDelta (boolean): Whether it's a delta CRL or not
        """

        kwargs = locals()

        metadata = {
            "tags": ["nac", "configure", "certificates", "authorities", "crls"],
            "operation": "createOrganizationNacCertificatesAuthoritiesCrl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls"

        body_params = [
            "caId",
            "content",
            "isDelta",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationNacCertificatesAuthoritiesCrl: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationNacCertificatesAuthoritiesCrlsDescriptors(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Get all the organization's CRL descriptors (metadata only - revocation list data is excluded)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-certificates-authorities-crls-descriptors

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortBy (string): Optional parameter to specify the field used to sort results. (default: caId)
        - sortOrder (string): Optional parameter to specify the sort order. (default: asc)
        - caIds (array): When ca Ids are provided, only CRLs associated to the given CA will be returned. Otherwise, all the CRLs created for an organization will be returned.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["caId", "createdAt", "lastUpdatedAt"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["nac", "configure", "certificates", "authorities", "crls", "descriptors"],
            "operation": "getOrganizationNacCertificatesAuthoritiesCrlsDescriptors",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls/descriptors"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortBy",
            "sortOrder",
            "caIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "caIds",
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
                    f"getOrganizationNacCertificatesAuthoritiesCrlsDescriptors: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationNacCertificatesAuthoritiesCrl(self, organizationId: str, crlId: str):
        """
        **Deletes a whole CRL, including all its deltas (in case of base CRL removal)**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-nac-certificates-authorities-crl

        - organizationId (string): Organization ID
        - crlId (string): Crl ID
        """

        metadata = {
            "tags": ["nac", "configure", "certificates", "authorities", "crls"],
            "operation": "deleteOrganizationNacCertificatesAuthoritiesCrl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        crlId = urllib.parse.quote(str(crlId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls/{crlId}"

        return self._session.delete(metadata, resource)

    def createOrganizationNacCertificatesImport(self, organizationId: str, contents: str, **kwargs):
        """
        **Import certificate for this organization or validate without persisting**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-import

        - organizationId (string): Organization ID
        - contents (string): Certificate content in valid PEM format
        - dryRun (boolean): If true, validates the certificate without persisting it
        - profile (object): Profile object containing certificate config fields
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "certificates", "import"],
            "operation": "createOrganizationNacCertificatesImport",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/import"

        body_params = [
            "contents",
            "dryRun",
            "profile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationNacCertificatesImport: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationNacCertificatesOverview(self, organizationId: str):
        """
        **Get counts of Enabled, Disabled, Expired and Last Used certificates for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-certificates-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["nac", "configure", "certificates", "overview"],
            "operation": "getOrganizationNacCertificatesOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/overview"

        return self._session.get(metadata, resource)

    def updateOrganizationNacCertificate(self, organizationId: str, certificateId: str, profile: dict, **kwargs):
        """
        **Update certificate configuration by certificateId for this organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-certificate

        - organizationId (string): Organization ID
        - certificateId (string): Certificate ID
        - profile (object): Profile object containing certificate config fields
        """

        kwargs = locals()

        metadata = {
            "tags": ["nac", "configure", "certificates"],
            "operation": "updateOrganizationNacCertificate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        certificateId = urllib.parse.quote(str(certificateId), safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/{certificateId}"

        body_params = [
            "profile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationNacCertificate: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationNacClients(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get all known clients for the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-clients

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - sortOrder (string): Query parameter for specifying the direction of sorting to use for the given sortKey.
        - sortKey (string): Query parameter to sort the clients by the value of the specified key.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - search (string): Optional parameter to fuzzy search on clients.
        - clientIds (array): List of ids for specific client retrieval
        - groupIds (array): List of group ids for client retrieval by group
        - lastNetworkName (array): List of network names for client retrieval by last login network name
        - ssid (array): List of SSID's to filter
        - classification (object): Classification filters for client retrieval
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ASC", "DESC"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "sortKey" in kwargs:
            options = ["mac"]
            assert kwargs["sortKey"] in options, (
                f'''"sortKey" cannot be "{kwargs["sortKey"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["nac", "configure", "clients"],
            "operation": "getOrganizationNacClients",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients"

        query_params = [
            "sortOrder",
            "sortKey",
            "perPage",
            "startingAfter",
            "endingBefore",
            "search",
            "clientIds",
            "groupIds",
            "lastNetworkName",
            "ssid",
            "classification",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "clientIds",
            "groupIds",
            "lastNetworkName",
            "ssid",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationNacClients: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationNacClient(self, organizationId: str, mac: str, **kwargs):
        """
        **Create a client for the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-client

        - organizationId (string): Organization ID
        - mac (string): The MAC address of the client
        - type (string): Type describes if the network client belongs to an individual user or corporate
        - owner (string): The username of the owner of the client
        - description (string): User provided description for the client
        - uuid (string): Universally unique identifier of the client
        - userDetails (array): List of users of this network client
        - oui (object): Organizationally unique identifier assigned to a vendor of the client
        - groups (array): List of group members associated with the client
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["BYOD", "corporate"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["nac", "configure", "clients"],
            "operation": "createOrganizationNacClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients"

        body_params = [
            "type",
            "owner",
            "mac",
            "description",
            "uuid",
            "userDetails",
            "oui",
            "groups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationNacClient: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationNacClientsDelete(self, organizationId: str, clientIds: list, **kwargs):
        """
        **Delete existing client(s) for the organization**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-nac-clients-delete

        - organizationId (string): Organization ID
        - clientIds (array): List of ids for specific client retrieval
        """

        kwargs = locals()

        metadata = {
            "tags": ["nac", "configure", "clients"],
            "operation": "bulkOrganizationNacClientsDelete",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/bulkDelete"

        body_params = [
            "clientIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"bulkOrganizationNacClientsDelete: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def createOrganizationNacClientsBulkEdit(self, organizationId: str, clientIds: list, **kwargs):
        """
        **Bulk Update of existing clients for the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-clients-bulk-edit

        - organizationId (string): Organization ID
        - clientIds (array): List of clients ids to apply the bulk edit operation on.
        - description (string): User provided description to be applied on the list of clients provided
        - groups (object): Client group information to be applied on the list of clients provided
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "clients", "bulkEdit"],
            "operation": "createOrganizationNacClientsBulkEdit",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/bulkEdit"

        body_params = [
            "clientIds",
            "description",
            "groups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationNacClientsBulkEdit: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def createOrganizationNacClientsBulkUpload(
        self, organizationId: str, contents: str, updateClients: bool, createClientGroups: bool, **kwargs
    ):
        """
        **Bulk upload of clients, client groups and their associations for the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-clients-bulk-upload

        - organizationId (string): Organization ID
        - contents (string): CSV file content in Base64 encoded string format
        - updateClients (boolean): The updateClients indicates whether existing clients must be updated with new data from the CSV
        - createClientGroups (boolean): The createClientGroups indicates whether new client groups must be created or not
        """

        kwargs = locals()

        metadata = {
            "tags": ["nac", "configure", "clients", "bulkUpload"],
            "operation": "createOrganizationNacClientsBulkUpload",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/bulkUpload"

        body_params = [
            "contents",
            "updateClients",
            "createClientGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationNacClientsBulkUpload: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationNacClientsGroups(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get all known client groups for the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-clients-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - sortOrder (string): Query parameter for specifying the direction of sorting to use for the given sortKey.
        - sortKey (string): Query parameter to sort the client groups by the value of the specified key.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - search (string): Optional parameter to fuzzy search on client groups.
        - groupIds (array): List of ids for specific group retrieval
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ASC", "DESC"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "sortKey" in kwargs:
            options = ["name"]
            assert kwargs["sortKey"] in options, (
                f'''"sortKey" cannot be "{kwargs["sortKey"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["nac", "configure", "clients", "groups"],
            "operation": "getOrganizationNacClientsGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups"

        query_params = [
            "sortOrder",
            "sortKey",
            "perPage",
            "startingAfter",
            "endingBefore",
            "search",
            "groupIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "groupIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationNacClientsGroups: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationNacClientsGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Create a client group for the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-clients-group

        - organizationId (string): Organization ID
        - name (string): The name of the group for access control model
        - description (string): User provided description of the group
        - members (array): List of client members associated with the group
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "clients", "groups"],
            "operation": "createOrganizationNacClientsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups"

        body_params = [
            "name",
            "description",
            "members",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationNacClientsGroup: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateOrganizationNacClientsGroup(self, organizationId: str, groupId: str, **kwargs):
        """
        **Update an existing client group for the organization with bulk member operations**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-clients-group

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        - name (string): The name of the group for access control model
        - description (string): User provided description of the group
        - members (object): Bulk member operations with addList/removeList arrays
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "clients", "groups"],
            "operation": "updateOrganizationNacClientsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups/{groupId}"

        body_params = [
            "name",
            "description",
            "members",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationNacClientsGroup: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationNacClientsGroup(self, organizationId: str, groupId: str):
        """
        **Delete an existing client group for the organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-nac-clients-group

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        """

        metadata = {
            "tags": ["nac", "configure", "clients", "groups"],
            "operation": "deleteOrganizationNacClientsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups/{groupId}"

        return self._session.delete(metadata, resource)

    def getOrganizationNacClientsOverview(self, organizationId: str):
        """
        **Get overview data for all known clients for the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-clients-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["nac", "configure", "clients", "overview"],
            "operation": "getOrganizationNacClientsOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/overview"

        return self._session.get(metadata, resource)

    def updateOrganizationNacClient(self, organizationId: str, clientId: str, mac: str, **kwargs):
        """
        **Update an existing client for the organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-client

        - organizationId (string): Organization ID
        - clientId (string): Client ID
        - mac (string): The MAC address of the client
        - type (string): Type describes if the network client belongs to an individual user or corporate
        - owner (string): The username of the owner of the client
        - description (string): User provided description for the client
        - uuid (string): Universally unique identifier of the client
        - userDetails (array): List of users of this network client
        - oui (object): Organizationally unique identifier assigned to a vendor of the client
        - groups (object): Client group membership changes
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["BYOD", "corporate"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["nac", "configure", "clients"],
            "operation": "updateOrganizationNacClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/organizations/{organizationId}/nac/clients/{clientId}"

        body_params = [
            "type",
            "owner",
            "mac",
            "description",
            "uuid",
            "userDetails",
            "oui",
            "groups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationNacClient: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationNacDictionaries(self, organizationId: str):
        """
        **Get all NAC dictionaries**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-dictionaries

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["nac", "configure", "dictionaries"],
            "operation": "getOrganizationNacDictionaries",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/dictionaries"

        return self._session.get(metadata, resource)

    def getOrganizationNacDictionaryAttributes(self, organizationId: str, dictionaryId: str, **kwargs):
        """
        **Get all attributes by dictionary ID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-dictionary-attributes

        - organizationId (string): Organization ID
        - dictionaryId (string): Dictionary ID
        - networkIds (array): An optional list of network IDs to filter the 'enum' field. Only enum values applicable to the specified networks will be returned.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "dictionaries", "attributes"],
            "operation": "getOrganizationNacDictionaryAttributes",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        dictionaryId = urllib.parse.quote(str(dictionaryId), safe="")
        resource = f"/organizations/{organizationId}/nac/dictionaries/{dictionaryId}/attributes"

        query_params = [
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationNacDictionaryAttributes: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationNacDictionaryAttributeValues(
        self, organizationId: str, dictionaryId: str, attributeName: str, **kwargs
    ):
        """
        **Search allowed values for a dictionary attribute**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-dictionary-attribute-values

        - organizationId (string): Organization ID
        - dictionaryId (string): Dictionary ID
        - attributeName (string): Attribute name
        - search (string): Optional search string for contains-match filtering of allowed values
        - networkIds (array): An optional list of network IDs to filter the allowed values.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "dictionaries", "attributes", "values"],
            "operation": "getOrganizationNacDictionaryAttributeValues",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        dictionaryId = urllib.parse.quote(str(dictionaryId), safe="")
        attributeName = urllib.parse.quote(str(attributeName), safe="")
        resource = f"/organizations/{organizationId}/nac/dictionaries/{dictionaryId}/attributes/{attributeName}/values"

        query_params = [
            "search",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationNacDictionaryAttributeValues: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationNacLicenseUsage(self, organizationId: str, startDate: str, **kwargs):
        """
        **Returns license usage data for a specific organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-license-usage

        - organizationId (string): Organization ID
        - startDate (string): Start date for the usage data in UTC timezone
        - endDate (string): End date for the usage data in UTC timezone
        - networkIds (array): List of locale and node group ids
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "license", "usage"],
            "operation": "getOrganizationNacLicenseUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/license/usage"

        query_params = [
            "startDate",
            "endDate",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationNacLicenseUsage: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationNacSessionsHistory(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the NAC Sessions for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-sessions-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 hour.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["nac", "configure", "sessions", "history"],
            "operation": "getOrganizationNacSessionsHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/nac/sessions/history"

        query_params = [
            "t0",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationNacSessionsHistory: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationNacSessionDetails(self, organizationId: str, sessionId: str):
        """
        **Return the details of selected NAC Sessions**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-nac-session-details

        - organizationId (string): Organization ID
        - sessionId (string): Session ID
        """

        metadata = {
            "tags": ["nac", "configure", "sessions", "details"],
            "operation": "getOrganizationNacSessionDetails",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        sessionId = urllib.parse.quote(str(sessionId), safe="")
        resource = f"/organizations/{organizationId}/nac/sessions/{sessionId}/details"

        return self._session.get(metadata, resource)
