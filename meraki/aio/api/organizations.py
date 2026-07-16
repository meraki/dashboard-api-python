import urllib


class AsyncOrganizations:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getOrganizations(self, total_pages=1, direction="next", **kwargs):
        """
        **List the organizations that the user has privileges on**
        https://developer.cisco.com/meraki/api-v1/#!get-organizations

        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 9000. Default is 9000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "getOrganizations",
        }
        resource = "/organizations"

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
                self._session._logger.warning(f"getOrganizations: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganization(self, name: str, **kwargs):
        """
        **Create a new organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization

        - name (string): The name of the organization
        - management (object): Information about the organization's management system
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "createOrganization",
        }
        resource = "/organizations"

        body_params = [
            "name",
            "management",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganization: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganization(self, organizationId: str):
        """
        **Return an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "getOrganization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}"

        return self._session.get(metadata, resource)

    def updateOrganization(self, organizationId: str, **kwargs):
        """
        **Update an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization

        - organizationId (string): Organization ID
        - name (string): The name of the organization
        - management (object): Information about the organization's management system
        - api (object): API-specific settings
        - privacy (object): Privacy-related settings for the organization.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "updateOrganization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}"

        body_params = [
            "name",
            "management",
            "api",
            "privacy",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganization: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganization(self, organizationId: str):
        """
        **Delete an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "deleteOrganization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}"

        return self._session.delete(metadata, resource)

    def createOrganizationActionBatch(self, organizationId: str, actions: list, **kwargs):
        """
        **Create an action batch**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch

        - organizationId (string): Organization ID
        - actions (array): A set of changes to make as part of this action (<a href='https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/'>more details</a>)
        - confirmed (boolean): Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "createOrganizationActionBatch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/actionBatches"

        body_params = [
            "confirmed",
            "synchronous",
            "actions",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationActionBatch: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationActionBatches(self, organizationId: str, **kwargs):
        """
        **Return the list of action batches in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

        - organizationId (string): Organization ID
        - status (string): Filter batches by status. Valid types are pending, completed, and failed.
        """

        kwargs.update(locals())

        if "status" in kwargs:
            options = ["completed", "failed", "pending"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "getOrganizationActionBatches",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/actionBatches"

        query_params = [
            "status",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationActionBatches: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Return an action batch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

        - organizationId (string): Organization ID
        - actionBatchId (string): Action batch ID
        """

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "getOrganizationActionBatch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        actionBatchId = urllib.parse.quote(str(actionBatchId), safe="")
        resource = f"/organizations/{organizationId}/actionBatches/{actionBatchId}"

        return self._session.get(metadata, resource)

    def deleteOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Delete an action batch**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch

        - organizationId (string): Organization ID
        - actionBatchId (string): Action batch ID
        """

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "deleteOrganizationActionBatch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        actionBatchId = urllib.parse.quote(str(actionBatchId), safe="")
        resource = f"/organizations/{organizationId}/actionBatches/{actionBatchId}"

        return self._session.delete(metadata, resource)

    def updateOrganizationActionBatch(self, organizationId: str, actionBatchId: str, **kwargs):
        """
        **Update an action batch**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch

        - organizationId (string): Organization ID
        - actionBatchId (string): Action batch ID
        - confirmed (boolean): A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "actionBatches"],
            "operation": "updateOrganizationActionBatch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        actionBatchId = urllib.parse.quote(str(actionBatchId), safe="")
        resource = f"/organizations/{organizationId}/actionBatches/{actionBatchId}"

        body_params = [
            "confirmed",
            "synchronous",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationActionBatch: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationAdaptivePolicyAcls(self, organizationId: str):
        """
        **List adaptive policy ACLs in a organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "getOrganizationAdaptivePolicyAcls",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls"

        return self._session.get(metadata, resource)

    def createOrganizationAdaptivePolicyAcl(self, organizationId: str, name: str, rules: list, ipVersion: str, **kwargs):
        """
        **Creates new adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - name (string): Name of the adaptive policy ACL
        - rules (array): An ordered array of the adaptive policy ACL rules.
        - ipVersion (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
        - description (string): Description of the adaptive policy ACL
        """

        kwargs.update(locals())

        if "ipVersion" in kwargs:
            options = ["any", "ipv4", "ipv6"]
            assert kwargs["ipVersion"] in options, (
                f'''"ipVersion" cannot be "{kwargs["ipVersion"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "createOrganizationAdaptivePolicyAcl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationAdaptivePolicyAcl: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str):
        """
        **Returns the adaptive policy ACL information**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - aclId (string): Acl ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "getOrganizationAdaptivePolicyAcl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        aclId = urllib.parse.quote(str(aclId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

        return self._session.get(metadata, resource)

    def updateOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str, **kwargs):
        """
        **Updates an adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - aclId (string): Acl ID
        - name (string): Name of the adaptive policy ACL
        - description (string): Description of the adaptive policy ACL
        - rules (array): An ordered array of the adaptive policy ACL rules. An empty array will clear the rules.
        - ipVersion (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
        """

        kwargs.update(locals())

        if "ipVersion" in kwargs:
            options = ["any", "ipv4", "ipv6"]
            assert kwargs["ipVersion"] in options, (
                f'''"ipVersion" cannot be "{kwargs["ipVersion"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "updateOrganizationAdaptivePolicyAcl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        aclId = urllib.parse.quote(str(aclId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationAdaptivePolicyAcl: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str):
        """
        **Deletes the specified adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - aclId (string): Acl ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "acls"],
            "operation": "deleteOrganizationAdaptivePolicyAcl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        aclId = urllib.parse.quote(str(aclId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

        return self._session.delete(metadata, resource)

    def getOrganizationAdaptivePolicyGroups(self, organizationId: str):
        """
        **List adaptive policy groups in a organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-groups

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "getOrganizationAdaptivePolicyGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups"

        return self._session.get(metadata, resource)

    def createOrganizationAdaptivePolicyGroup(self, organizationId: str, name: str, sgt: int, **kwargs):
        """
        **Creates a new adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - name (string): Name of the group
        - sgt (integer): SGT value of the group
        - description (string): Description of the group (default: "")
        - policyObjects (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute) (default: [])
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "createOrganizationAdaptivePolicyGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationAdaptivePolicyGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str):
        """
        **Returns an adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "getOrganizationAdaptivePolicyGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

        return self._session.get(metadata, resource)

    def updateOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str, **kwargs):
        """
        **Updates an adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of the group
        - sgt (integer): SGT value of the group
        - description (string): Description of the group
        - policyObjects (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "updateOrganizationAdaptivePolicyGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationAdaptivePolicyGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str):
        """
        **Deletes the specified adaptive policy group and any associated policies and references**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "groups"],
            "operation": "deleteOrganizationAdaptivePolicyGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationAdaptivePolicyOverview(self, organizationId: str):
        """
        **Returns adaptive policy aggregate statistics for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "adaptivePolicy", "overview"],
            "operation": "getOrganizationAdaptivePolicyOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/overview"

        return self._session.get(metadata, resource)

    def getOrganizationAdaptivePolicyPolicies(self, organizationId: str):
        """
        **List adaptive policies in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policies

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "getOrganizationAdaptivePolicyPolicies",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies"

        return self._session.get(metadata, resource)

    def createOrganizationAdaptivePolicyPolicy(self, organizationId: str, sourceGroup: dict, destinationGroup: dict, **kwargs):
        """
        **Add an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - sourceGroup (object): The source adaptive policy group (requires one unique attribute)
        - destinationGroup (object): The destination adaptive policy group (requires one unique attribute)
        - acls (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])
        - lastEntryRule (string): The rule to apply if there is no matching ACL (default: "default")
        """

        kwargs.update(locals())

        if "lastEntryRule" in kwargs:
            options = ["allow", "default", "deny"]
            assert kwargs["lastEntryRule"] in options, (
                f'''"lastEntryRule" cannot be "{kwargs["lastEntryRule"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "createOrganizationAdaptivePolicyPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationAdaptivePolicyPolicy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str):
        """
        **Return an adaptive policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "getOrganizationAdaptivePolicyPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

        return self._session.get(metadata, resource)

    def updateOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str, **kwargs):
        """
        **Update an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - id (string): ID
        - sourceGroup (object): The source adaptive policy group (requires one unique attribute)
        - destinationGroup (object): The destination adaptive policy group (requires one unique attribute)
        - acls (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy
        - lastEntryRule (string): The rule to apply if there is no matching ACL
        """

        kwargs.update(locals())

        if "lastEntryRule" in kwargs:
            options = ["allow", "default", "deny"]
            assert kwargs["lastEntryRule"] in options, (
                f'''"lastEntryRule" cannot be "{kwargs["lastEntryRule"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "updateOrganizationAdaptivePolicyPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationAdaptivePolicyPolicy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str):
        """
        **Delete an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "policies"],
            "operation": "deleteOrganizationAdaptivePolicyPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationAdaptivePolicySettings(self, organizationId: str):
        """
        **Returns global adaptive policy settings in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-settings

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "settings"],
            "operation": "getOrganizationAdaptivePolicySettings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/settings"

        return self._session.get(metadata, resource)

    def updateOrganizationAdaptivePolicySettings(self, organizationId: str, **kwargs):
        """
        **Update global adaptive policy settings**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

        - organizationId (string): Organization ID
        - enabledNetworks (array): List of network IDs with adaptive policy enabled
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "adaptivePolicy", "settings"],
            "operation": "updateOrganizationAdaptivePolicySettings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/settings"

        body_params = [
            "enabledNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationAdaptivePolicySettings: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationAdmins(self, organizationId: str, **kwargs):
        """
        **List the dashboard administrators in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

        - organizationId (string): Organization ID
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "getOrganizationAdmins",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/admins"

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
                self._session._logger.warning(f"getOrganizationAdmins: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def createOrganizationAdmin(self, organizationId: str, email: str, name: str, orgAccess: str, **kwargs):
        """
        **Create a new dashboard administrator**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-admin

        - organizationId (string): Organization ID
        - email (string): The email of the dashboard administrator. This attribute can not be updated.
        - name (string): The name of the dashboard administrator
        - orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
        - tags (array): The list of tags that the dashboard administrator has privileges on
        - networks (array): The list of networks that the dashboard administrator has privileges on
        - authenticationMethod (string): No longer used as of Cisco SecureX end-of-life. Can be one of 'Email'. The default is Email authentication.
        """

        kwargs.update(locals())

        if "orgAccess" in kwargs:
            options = ["enterprise", "full", "none", "read-only"]
            assert kwargs["orgAccess"] in options, (
                f'''"orgAccess" cannot be "{kwargs["orgAccess"]}", & must be set to one of: {options}'''
            )
        if "authenticationMethod" in kwargs:
            options = ["Email"]
            assert kwargs["authenticationMethod"] in options, (
                f'''"authenticationMethod" cannot be "{kwargs["authenticationMethod"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "createOrganizationAdmin",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/admins"

        body_params = [
            "email",
            "name",
            "orgAccess",
            "tags",
            "networks",
            "authenticationMethod",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationAdmin: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateOrganizationAdmin(self, organizationId: str, adminId: str, **kwargs):
        """
        **Update an administrator**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-admin

        - organizationId (string): Organization ID
        - adminId (string): Admin ID
        - name (string): The name of the dashboard administrator
        - orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
        - tags (array): The list of tags that the dashboard administrator has privileges on
        - networks (array): The list of networks that the dashboard administrator has privileges on
        """

        kwargs.update(locals())

        if "orgAccess" in kwargs:
            options = ["enterprise", "full", "none", "read-only"]
            assert kwargs["orgAccess"] in options, (
                f'''"orgAccess" cannot be "{kwargs["orgAccess"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "updateOrganizationAdmin",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        adminId = urllib.parse.quote(str(adminId), safe="")
        resource = f"/organizations/{organizationId}/admins/{adminId}"

        body_params = [
            "name",
            "orgAccess",
            "tags",
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationAdmin: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAdmin(self, organizationId: str, adminId: str):
        """
        **Revoke all access for a dashboard administrator within this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin

        - organizationId (string): Organization ID
        - adminId (string): Admin ID
        """

        metadata = {
            "tags": ["organizations", "configure", "admins"],
            "operation": "deleteOrganizationAdmin",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        adminId = urllib.parse.quote(str(adminId), safe="")
        resource = f"/organizations/{organizationId}/admins/{adminId}"

        return self._session.delete(metadata, resource)

    def getOrganizationAlertsProfiles(self, organizationId: str):
        """
        **List all organization-wide alert configurations**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-alerts-profiles

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "getOrganizationAlertsProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles"

        return self._session.get(metadata, resource)

    def createOrganizationAlertsProfile(
        self, organizationId: str, type: str, alertCondition: dict, recipients: dict, networkTags: list, **kwargs
    ):
        """
        **Create an organization-wide alert configuration**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

        - organizationId (string): Organization ID
        - type (string): The alert type
        - alertCondition (object): The conditions that determine if the alert triggers
        - recipients (object): List of recipients that will recieve the alert.
        - networkTags (array): Networks with these tags will be monitored for the alert
        - description (string): User supplied description of the alert
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "appOutage",
                "voipJitter",
                "voipMos",
                "voipPacketLoss",
                "wanLatency",
                "wanPacketLoss",
                "wanStatus",
                "wanUtilization",
            ]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "createOrganizationAlertsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles"

        body_params = [
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationAlertsProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateOrganizationAlertsProfile(self, organizationId: str, alertConfigId: str, **kwargs):
        """
        **Update an organization-wide alert config**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

        - organizationId (string): Organization ID
        - alertConfigId (string): Alert config ID
        - enabled (boolean): Is the alert config enabled
        - type (string): The alert type
        - alertCondition (object): The conditions that determine if the alert triggers
        - recipients (object): List of recipients that will recieve the alert.
        - networkTags (array): Networks with these tags will be monitored for the alert
        - description (string): User supplied description of the alert
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "appOutage",
                "voipJitter",
                "voipMos",
                "voipPacketLoss",
                "wanLatency",
                "wanPacketLoss",
                "wanStatus",
                "wanUtilization",
            ]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "updateOrganizationAlertsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        alertConfigId = urllib.parse.quote(str(alertConfigId), safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles/{alertConfigId}"

        body_params = [
            "enabled",
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationAlertsProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAlertsProfile(self, organizationId: str, alertConfigId: str):
        """
        **Removes an organization-wide alert config**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

        - organizationId (string): Organization ID
        - alertConfigId (string): Alert config ID
        """

        metadata = {
            "tags": ["organizations", "configure", "alerts", "profiles"],
            "operation": "deleteOrganizationAlertsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        alertConfigId = urllib.parse.quote(str(alertConfigId), safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles/{alertConfigId}"

        return self._session.delete(metadata, resource)

    def getOrganizationApiPushProfiles(self, organizationId: str, **kwargs):
        """
        **List the Push API profiles in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-push-profiles

        - organizationId (string): Organization ID
        - inames (array): Optional parameter to filter the result set by the included set of push profile inames
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "profiles"],
            "operation": "getOrganizationApiPushProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/push/profiles"

        query_params = [
            "inames",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "inames",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationApiPushProfiles: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def createOrganizationApiPushProfile(self, organizationId: str, iname: str, topic: dict, receiver: dict, **kwargs):
        """
        **Create a Push API profile to subscribe to a topic and send its messages to a receiver profile.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-api-push-profile

        - organizationId (string): Organization ID
        - iname (string): Immutable name of the resource. Must be unique within resources of this type.
        - topic (object): Push topic
        - receiver (object): Push receiver profile
        - name (string): Name of push profile
        - description (string): Description of push profile
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "profiles"],
            "operation": "createOrganizationApiPushProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/push/profiles"

        body_params = [
            "iname",
            "name",
            "description",
            "topic",
            "receiver",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationApiPushProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateOrganizationApiPushProfile(self, organizationId: str, iname: str, **kwargs):
        """
        **Update a Push API profile's name, description, topic, receiver profile or other configuration.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-api-push-profile

        - organizationId (string): Organization ID
        - iname (string): Iname
        - name (string): Name of push profile
        - description (string): Description of push profile
        - topic (object): Push topic
        - receiver (object): Push receiver profile
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "profiles"],
            "operation": "updateOrganizationApiPushProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/organizations/{organizationId}/api/push/profiles/{iname}"

        body_params = [
            "name",
            "description",
            "topic",
            "receiver",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationApiPushProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationApiPushProfile(self, organizationId: str, iname: str):
        """
        **Delete a Push API profile to unsubscribe from a topic, ending that topic's message delivery to a receiver profile.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-api-push-profile

        - organizationId (string): Organization ID
        - iname (string): Iname
        """

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "profiles"],
            "operation": "deleteOrganizationApiPushProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/organizations/{organizationId}/api/push/profiles/{iname}"

        return self._session.delete(metadata, resource)

    def getOrganizationApiPushReceiversProfiles(self, organizationId: str):
        """
        **List the Push API receiver profiles in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-push-receivers-profiles

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "receivers", "profiles"],
            "operation": "getOrganizationApiPushReceiversProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/push/receivers/profiles"

        return self._session.get(metadata, resource)

    def createOrganizationApiPushReceiversProfile(self, organizationId: str, iname: str, receiver: dict, **kwargs):
        """
        **Create a Push API receiver profile to define an external receiver for Push API messages**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-api-push-receivers-profile

        - organizationId (string): Organization ID
        - iname (string): Immutable name of the resource. Must be unique within resources of this type.
        - receiver (object): Webhook receiver
        - name (string): Name of receiver profile
        - description (string): Description of receiver profile
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "receivers", "profiles"],
            "operation": "createOrganizationApiPushReceiversProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/push/receivers/profiles"

        body_params = [
            "iname",
            "name",
            "description",
            "receiver",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationApiPushReceiversProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationApiPushReceiversProfile(self, organizationId: str, iname: str):
        """
        **Delete a Push API receiver profile.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-api-push-receivers-profile

        - organizationId (string): Organization ID
        - iname (string): Iname
        """

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "receivers", "profiles"],
            "operation": "deleteOrganizationApiPushReceiversProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/organizations/{organizationId}/api/push/receivers/profiles/{iname}"

        return self._session.delete(metadata, resource)

    def updateOrganizationApiPushReceiversProfile(self, organizationId: str, iname: str, **kwargs):
        """
        **Update a Push API receiver profile's name, description, or receiver configuration.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-api-push-receivers-profile

        - organizationId (string): Organization ID
        - iname (string): Iname
        - name (string): Name of the receiver profile
        - description (string): Description of the receiver profile
        - receiver (object): API Push Receiver details
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "receivers", "profiles"],
            "operation": "updateOrganizationApiPushReceiversProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        iname = urllib.parse.quote(str(iname), safe="")
        resource = f"/organizations/{organizationId}/api/push/receivers/profiles/{iname}"

        body_params = [
            "name",
            "description",
            "receiver",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationApiPushReceiversProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationApiPushTopics(self, organizationId: str):
        """
        **List the topics in an organization that are eligible for message delivery via Push API.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-push-topics

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "api", "push", "topics"],
            "operation": "getOrganizationApiPushTopics",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/push/topics"

        return self._session.get(metadata, resource)

    def getOrganizationApiRestProvisioningPipelines(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List pipelines with operation and status metadata, sorted by pipeline ID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-rest-provisioning-pipelines

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'.
        - status (string): If provided, filters pipelines by status. If omitted, pipelines of all statuses are returned. `pending` pipelines have not started, `active` pipelines have started but not finished, `success` pipelines completed successfully, and `error` pipelines failed.
        - timespan (integer): Created-at lookback for matching pipelines, in seconds. Defaults to 7200 seconds. The maximum is 30 days.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "status" in kwargs:
            options = ["active", "error", "pending", "success"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "api", "rest", "provisioning", "pipelines"],
            "operation": "getOrganizationApiRestProvisioningPipelines",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/rest/provisioning/pipelines"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "status",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationApiRestProvisioningPipelines: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationApiRestProvisioningPipelinesJobs(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List pipeline jobs, with optional status filtering**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-rest-provisioning-pipelines-jobs

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - pipelineIds (array): Pipeline IDs to retrieve jobs for
        - status (string): If provided, filters jobs by status
        """

        kwargs.update(locals())

        if "status" in kwargs:
            options = ["complete", "deferred", "failed", "new", "ready", "running", "scheduled"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "api", "rest", "provisioning", "pipelines", "jobs"],
            "operation": "getOrganizationApiRestProvisioningPipelinesJobs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/rest/provisioning/pipelines/jobs"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "pipelineIds",
            "status",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "pipelineIds",
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
                    f"getOrganizationApiRestProvisioningPipelinesJobs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationApiRestProvisioningPipelinesJobsOverviewsByPipeline(self, organizationId: str, **kwargs):
        """
        **Retrieves pipeline overviews with aggregated job status counts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-rest-provisioning-pipelines-jobs-overviews-by-pipeline

        - organizationId (string): Organization ID
        - pipelineIds (array): Pipeline IDs to retrieve overviews for
        """

        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "api",
                "rest",
                "provisioning",
                "pipelines",
                "jobs",
                "overviews",
                "byPipeline",
            ],
            "operation": "getOrganizationApiRestProvisioningPipelinesJobsOverviewsByPipeline",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/api/rest/provisioning/pipelines/jobs/overviews/byPipeline"

        query_params = [
            "pipelineIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "pipelineIds",
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
                    f"getOrganizationApiRestProvisioningPipelinesJobsOverviewsByPipeline: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationApiRequests(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the API requests made by an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - adminId (string): Filter the results by the ID of the admin who made the API requests
        - path (string): Filter the results by the path of the API requests
        - method (string): Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE')
        - responseCode (integer): Filter the results by the response code of the API requests
        - sourceIp (string): Filter the results by the IP address of the originating API request
        - userAgent (string): Filter the results by the user agent string of the API request
        - version (integer): Filter the results by the API version of the API request
        - operationIds (array): Filter the results by one or more operation IDs for the API request
        """

        kwargs.update(locals())

        if "method" in kwargs:
            options = ["DELETE", "GET", "POST", "PUT"]
            assert kwargs["method"] in options, (
                f'''"method" cannot be "{kwargs["method"]}", & must be set to one of: {options}'''
            )
        if "version" in kwargs:
            options = [0, 1]
            assert kwargs["version"] in options, (
                f'''"version" cannot be "{kwargs["version"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests"],
            "operation": "getOrganizationApiRequests",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "adminId",
            "path",
            "method",
            "responseCode",
            "sourceIp",
            "userAgent",
            "version",
            "operationIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "operationIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationApiRequests: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationApiRequestsOverview(self, organizationId: str, **kwargs):
        """
        **Return an aggregated overview of API requests data**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "overview"],
            "operation": "getOrganizationApiRequestsOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationApiRequestsOverview: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationApiRequestsOverviewResponseCodesByInterval(self, organizationId: str, **kwargs):
        """
        **Tracks organizations' API requests by response code across a given time period**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview-response-codes-by-interval

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
        - version (integer): Filter by API version of the endpoint. Allowable values are: [0, 1]
        - operationIds (array): Filter by operation ID of the endpoint
        - sourceIps (array): Filter by source IP that made the API request
        - adminIds (array): Filter by admin ID of user that made the API request
        - userAgent (string): Filter by user agent string for API request. This will filter by a complete or partial match.
        """

        kwargs.update(locals())

        if "version" in kwargs:
            options = [0, 1]
            assert kwargs["version"] in options, (
                f'''"version" cannot be "{kwargs["version"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "overview", "responseCodes", "byInterval"],
            "operation": "getOrganizationApiRequestsOverviewResponseCodesByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "interval",
            "version",
            "operationIds",
            "sourceIps",
            "adminIds",
            "userAgent",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "operationIds",
            "sourceIps",
            "adminIds",
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
                    f"getOrganizationApiRequestsOverviewResponseCodesByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationApiRequestsResponseCodesHistoryByAdmin(self, organizationId: str, **kwargs):
        """
        **Lists API request response codes and their counts aggregated by admin**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-response-codes-history-by-admin

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "responseCodes", "history", "byAdmin"],
            "operation": "getOrganizationApiRequestsResponseCodesHistoryByAdmin",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests/responseCodes/history/byAdmin"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationApiRequestsResponseCodesHistoryByAdmin: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationApiRequestsResponseCodesHistoryByApplication(self, organizationId: str, **kwargs):
        """
        **Lists API request response codes and their counts aggregated by application**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-response-codes-history-by-application

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "responseCodes", "history", "byApplication"],
            "operation": "getOrganizationApiRequestsResponseCodesHistoryByApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests/responseCodes/history/byApplication"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationApiRequestsResponseCodesHistoryByApplication: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationApiRequestsResponseCodesHistoryByOperation(self, organizationId: str, **kwargs):
        """
        **Aggregates API usage data by operationId**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-response-codes-history-by-operation

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "responseCodes", "history", "byOperation"],
            "operation": "getOrganizationApiRequestsResponseCodesHistoryByOperation",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests/responseCodes/history/byOperation"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationApiRequestsResponseCodesHistoryByOperation: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationApiRequestsResponseCodesHistoryBySourceIp(self, organizationId: str, **kwargs):
        """
        **Aggregates API usage by source ip**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-response-codes-history-by-source-ip

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "apiRequests", "responseCodes", "history", "bySourceIp"],
            "operation": "getOrganizationApiRequestsResponseCodesHistoryBySourceIp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/apiRequests/responseCodes/history/bySourceIp"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationApiRequestsResponseCodesHistoryBySourceIp: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceAlerts(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return all health alerts for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 4 - 300. Default is 30.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'.
        - networkId (string): Optional parameter to filter alerts by network ids.
        - severity (string): Optional parameter to filter by severity type.
        - types (array): Optional parameter to filter by alert type.
        - tsStart (string): Optional parameter to filter by starting timestamp
        - tsEnd (string): Optional parameter to filter by end timestamp
        - category (string): Optional parameter to filter by category.
        - sortBy (string): Optional parameter to set column to sort by.
        - serials (array): Optional parameter to filter by primary device serial
        - deviceTypes (array): Optional parameter to filter by device types
        - deviceTags (array): Optional parameter to filter by device tags
        - active (boolean): Optional parameter to filter by active alerts defaults to true
        - dismissed (boolean): Optional parameter to filter by dismissed alerts defaults to false
        - resolved (boolean): Optional parameter to filter by resolved alerts defaults to false
        - suppressAlertsForOfflineNodes (boolean): When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "experience_metrics", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )
        if "sortBy" in kwargs:
            options = ["category", "dismissedAt", "resolvedAt", "severity", "startedAt"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "getOrganizationAssuranceAlerts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "sortBy",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationAssuranceAlerts: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def dismissOrganizationAssuranceAlerts(self, organizationId: str, alertIds: list, **kwargs):
        """
        **Dismiss health alerts**
        https://developer.cisco.com/meraki/api-v1/#!dismiss-organization-assurance-alerts

        - organizationId (string): Organization ID
        - alertIds (array): Array of alert IDs in this organization to dismiss. Missing or inaccessible alert IDs return 404.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "dismissOrganizationAssuranceAlerts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/dismiss"

        body_params = [
            "alertIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"dismissOrganizationAssuranceAlerts: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationAssuranceAlertsOverview(self, organizationId: str, **kwargs):
        """
        **Return overview of active health alerts for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview

        - organizationId (string): Organization ID
        - networkId (string): Optional parameter to filter alerts overview by network ids.
        - severity (string): Optional parameter to filter alerts overview by severity type.
        - types (array): Optional parameter to filter by alert type.
        - tsStart (string): Optional parameter to filter by starting timestamp
        - tsEnd (string): Optional parameter to filter by end timestamp
        - category (string): Optional parameter to filter by category.
        - serials (array): Optional parameter to filter by primary device serial
        - deviceTypes (array): Optional parameter to filter by device types
        - deviceTags (array): Optional parameter to filter by device tags
        - active (boolean): Optional parameter to filter by active alerts defaults to true
        - dismissed (boolean): Optional parameter to filter by dismissed alerts defaults to false
        - resolved (boolean): Optional parameter to filter by resolved alerts defaults to false
        - suppressAlertsForOfflineNodes (boolean): When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false.
        """

        kwargs.update(locals())

        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "experience_metrics", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview"],
            "operation": "getOrganizationAssuranceAlertsOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/overview"

        query_params = [
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
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
                    f"getOrganizationAssuranceAlertsOverview: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceAlertsOverviewByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return a Summary of Alerts grouped by network and severity**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'.
        - networkId (string): Optional parameter to filter alerts overview by network id.
        - severity (string): Optional parameter to filter alerts overview by severity type.
        - types (array): Optional parameter to filter by alert type.
        - tsStart (string): Optional parameter to filter by starting timestamp
        - tsEnd (string): Optional parameter to filter by end timestamp
        - category (string): Optional parameter to filter by category.
        - serials (array): Optional parameter to filter by primary device serial
        - deviceTypes (array): Optional parameter to filter by device types
        - deviceTags (array): Optional parameter to filter by device tags
        - active (boolean): Optional parameter to filter by active alerts defaults to true
        - dismissed (boolean): Optional parameter to filter by dismissed alerts defaults to false
        - resolved (boolean): Optional parameter to filter by resolved alerts defaults to false
        - suppressAlertsForOfflineNodes (boolean): When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "experience_metrics", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview", "byNetwork"],
            "operation": "getOrganizationAssuranceAlertsOverviewByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/overview/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
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
                    f"getOrganizationAssuranceAlertsOverviewByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceAlertsOverviewByType(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return a Summary of Alerts grouped by type and severity**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-by-type

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'.
        - networkId (string): Optional parameter to filter alerts overview by network ids.
        - severity (string): Optional parameter to filter alerts overview by severity type.
        - types (array): Optional parameter to filter by alert type.
        - tsStart (string): Optional parameter to filter by starting timestamp
        - tsEnd (string): Optional parameter to filter by end timestamp
        - category (string): Optional parameter to filter by category.
        - sortBy (string): Optional parameter to set column to sort by.
        - serials (array): Optional parameter to filter by primary device serial
        - deviceTypes (array): Optional parameter to filter by device types
        - deviceTags (array): Optional parameter to filter by device tags
        - active (boolean): Optional parameter to filter by active alerts defaults to true
        - dismissed (boolean): Optional parameter to filter by dismissed alerts defaults to false
        - resolved (boolean): Optional parameter to filter by resolved alerts defaults to false
        - includeDeviceTags (boolean): Include grouped device tags for each alert type in the response.
        - includeNetworks (boolean): Include affected networks for each alert type in the response.
        - suppressAlertsForOfflineNodes (boolean): When set to true the api will only return connectivity alerts for a given device if that device is in an offline state. This only applies to devices. This is ignored when resolved is true. Example:  If a Switch has a VLan Mismatch and is Unreachable. only the Unreachable alert will be returned. Defaults to false.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "experience_metrics", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )
        if "sortBy" in kwargs:
            options = ["count", "lastAlertedAt", "networkCount", "severity", "startedAt"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview", "byType"],
            "operation": "getOrganizationAssuranceAlertsOverviewByType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/overview/byType"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "sortBy",
            "serials",
            "deviceTypes",
            "deviceTags",
            "active",
            "dismissed",
            "resolved",
            "includeDeviceTags",
            "includeNetworks",
            "suppressAlertsForOfflineNodes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
            "deviceTags",
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
                    f"getOrganizationAssuranceAlertsOverviewByType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceAlertsOverviewHistorical(
        self, organizationId: str, segmentDuration: int, tsStart: str, **kwargs
    ):
        """
        **Returns historical health alert overviews**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-overview-historical

        - organizationId (string): Organization ID
        - segmentDuration (integer): Amount of time in seconds for each segment in the returned dataset
        - tsStart (string): Parameter to define starting timestamp of historical totals
        - networkId (string): Optional parameter to filter alerts overview by network ids.
        - severity (string): Optional parameter to filter alerts overview by severity type.
        - types (array): Optional parameter to filter by alert type.
        - tsEnd (string): Optional parameter to filter by end timestamp defaults to the current time
        - category (string): Optional parameter to filter by category.
        - serials (array): Optional parameter to filter by primary device serial
        - deviceTypes (array): Optional parameter to filter by device types
        """

        kwargs.update(locals())

        if "category" in kwargs:
            options = ["configuration", "connectivity", "device_health", "experience_metrics", "insights"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "overview", "historical"],
            "operation": "getOrganizationAssuranceAlertsOverviewHistorical",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/overview/historical"

        query_params = [
            "segmentDuration",
            "networkId",
            "severity",
            "types",
            "tsStart",
            "tsEnd",
            "category",
            "serials",
            "deviceTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "serials",
            "deviceTypes",
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
                    f"getOrganizationAssuranceAlertsOverviewHistorical: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def restoreOrganizationAssuranceAlerts(self, organizationId: str, alertIds: list, **kwargs):
        """
        **Restore health alerts from dismissed**
        https://developer.cisco.com/meraki/api-v1/#!restore-organization-assurance-alerts

        - organizationId (string): Organization ID
        - alertIds (array): Array of alert IDs in this organization to restore. Missing or inaccessible alert IDs return 404.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "restoreOrganizationAssuranceAlerts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/restore"

        body_params = [
            "alertIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"restoreOrganizationAssuranceAlerts: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationAssuranceAlertsTaxonomyCategories(self, organizationId: str):
        """
        **Return a list of Category Types**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-taxonomy-categories

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "taxonomy", "categories"],
            "operation": "getOrganizationAssuranceAlertsTaxonomyCategories",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/taxonomy/categories"

        return self._session.get(metadata, resource)

    def getOrganizationAssuranceAlertsTaxonomyTypes(self, organizationId: str):
        """
        **Return a list of alert types**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alerts-taxonomy-types

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "alerts", "taxonomy", "types"],
            "operation": "getOrganizationAssuranceAlertsTaxonomyTypes",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/taxonomy/types"

        return self._session.get(metadata, resource)

    def getOrganizationAssuranceAlert(self, organizationId: str, id: str):
        """
        **Return a singular Health Alert by its id**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-alert

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "alerts"],
            "operation": "getOrganizationAssuranceAlert",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/assurance/alerts/{id}"

        return self._session.get(metadata, resource)

    def getOrganizationAssuranceClientsConnectedCountHistory(self, organizationId: str, networkId: str, **kwargs):
        """
        **Return combined wireless and wired connected client counts over time for a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-clients-connected-count-history

        - organizationId (string): Organization ID
        - networkId (string): Network ID to query.
        - serials (array): A list of serials of wireless AP or wired switch devices
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - ssidNumbers (array): Filter results by SSID number
        - deviceType (string): Filter connected client counts by device type.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 8 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600. The default is 600. Interval is calculated if time params are provided.
        """

        kwargs.update(locals())

        if "deviceType" in kwargs:
            options = ["access_point", "switch"]
            assert kwargs["deviceType"] in options, (
                f'''"deviceType" cannot be "{kwargs["deviceType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "clients", "connectedCountHistory"],
            "operation": "getOrganizationAssuranceClientsConnectedCountHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/clients/connectedCountHistory"

        query_params = [
            "networkId",
            "serials",
            "bands",
            "ssidNumbers",
            "deviceType",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "bands",
            "ssidNumbers",
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
                    f"getOrganizationAssuranceClientsConnectedCountHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceClientsEvents(self, organizationId: str, clientId: str, networkId: str, **kwargs):
        """
        **Given a client, get all alerts and events for a given timespan**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-clients-events

        - organizationId (string): Organization ID
        - clientId (string): ID of client to query
        - networkId (string): Network ID where client is connected
        - filter (array): Optional parameter to filter by issue
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "clients", "events"],
            "operation": "getOrganizationAssuranceClientsEvents",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/clients/events"

        query_params = [
            "filter",
            "clientId",
            "networkId",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "filter",
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
                    f"getOrganizationAssuranceClientsEvents: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceClientsEventsCorrelated(
        self, organizationId: str, clientId: str, category: str, networkId: str, timestamp: str, **kwargs
    ):
        """
        **Given a client, category, and timespan, return events that have a close connection to each other.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-clients-events-correlated

        - organizationId (string): Organization ID
        - clientId (string): Client ID
        - category (string): Category of events
        - networkId (string): Network used by the client
        - timestamp (string): Timestamp for the event
        - lookback (integer): Amount of time in minutes to look back
        - lookforward (integer): Amount of time in minutes to look forwards
        """

        kwargs.update(locals())

        if "category" in kwargs:
            options = ["application", "association", "authentication", "dhcp", "dns"]
            assert kwargs["category"] in options, (
                f'''"category" cannot be "{kwargs["category"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "clients", "events", "correlated"],
            "operation": "getOrganizationAssuranceClientsEventsCorrelated",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/clients/events/correlated"

        query_params = [
            "clientId",
            "category",
            "networkId",
            "timestamp",
            "lookback",
            "lookforward",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationAssuranceClientsEventsCorrelated: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceClientsTopologyCurrent(self, organizationId: str, clientId: str, networkId: str, **kwargs):
        """
        **Given a client, return current topology**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-clients-topology-current

        - organizationId (string): Organization ID
        - clientId (string): ID of client to query
        - networkId (string): Network ID where client is connected
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "clients", "topology", "current"],
            "operation": "getOrganizationAssuranceClientsTopologyCurrent",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/clients/topology/current"

        query_params = [
            "clientId",
            "networkId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationAssuranceClientsTopologyCurrent: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceClientsTopologyNew(self, organizationId: str, clientIds: list, networkId: str, **kwargs):
        """
        **Given a client, return current topology**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-clients-topology-new

        - organizationId (string): Organization ID
        - clientIds (array): List of IDs for client retrieval for a given network. Limited to 1 client for now
        - networkId (string): Network ID where client is connected
        - timestamp (string): Timestamp for client topology path
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "clients", "topology", "new"],
            "operation": "getOrganizationAssuranceClientsTopologyNew",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/clients/topology/new"

        query_params = [
            "clientIds",
            "networkId",
            "timestamp",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "clientIds",
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
                    f"getOrganizationAssuranceClientsTopologyNew: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceDevicesStatusesOverview(self, organizationId: str, **kwargs):
        """
        **Returns counts of online, offline, and recovered devices by product type, along with offline intervals for impacted devices in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-devices-statuses-overview

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "statuses", "overview"],
            "operation": "getOrganizationAssuranceDevicesStatusesOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/devices/statuses/overview"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
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
                    f"getOrganizationAssuranceDevicesStatusesOverview: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceFetchTableQuery(self, organizationId: str, tableName: str, **kwargs):
        """
        **Returns the table data for a given timespan**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-fetch-table-query

        - organizationId (string): Organization ID
        - tableName (string): The table from which we want to get data
        - t0 (string): The beginning of the timespan for the data.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 365 days, 5 hours, 49 minutes, and 12 seconds. The default is 30 days, 10 hours, 29 minutes, and 6 seconds.
        - userEmail (string): The user email for whom we want to calculate lookback
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "fetchTableQuery"],
            "operation": "getOrganizationAssuranceFetchTableQuery",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/fetchTableQuery"

        query_params = [
            "t0",
            "timespan",
            "tableName",
            "userEmail",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationAssuranceFetchTableQuery: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceNetworkServicesServerHealthByServer(self, organizationId: str, **kwargs):
        """
        **Returns network server health in organization by server.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-network-services-server-health-by-server

        - organizationId (string): Organization ID
        - networkIds (array): Filter results for these networks.
        - serverTypes (array): Filter results for these server types.
        - serverIps (array): Filter results for these server IP addresses.
        - ssidNumbers (array): Filter results for these SSID Numbers.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networkServices", "serverHealth", "byServer"],
            "operation": "getOrganizationAssuranceNetworkServicesServerHealthByServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/networkServices/serverHealth/byServer"

        query_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
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
                    f"getOrganizationAssuranceNetworkServicesServerHealthByServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceNetworkServicesServerHealthByServerByInterval(self, organizationId: str, **kwargs):
        """
        **Returns network server health in organization by server and by interval.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-network-services-server-health-by-server-by-interval

        - organizationId (string): Organization ID
        - networkIds (array): Filter results for these networks.
        - serverTypes (array): Filter results for these server types.
        - serverIps (array): Filter results for these server IP addresses.
        - ssidNumbers (array): Filter results for these SSID Numbers.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networkServices", "serverHealth", "byServer", "byInterval"],
            "operation": "getOrganizationAssuranceNetworkServicesServerHealthByServerByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/networkServices/serverHealth/byServer/byInterval"

        query_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
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
                    f"getOrganizationAssuranceNetworkServicesServerHealthByServerByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceNetworkServicesServerHealthByServerType(self, organizationId: str, **kwargs):
        """
        **Returns network server health in organization by server type.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-network-services-server-health-by-server-type

        - organizationId (string): Organization ID
        - networkIds (array): Filter results for these networks.
        - serverTypes (array): Filter results for these server types.
        - serverIps (array): Filter results for these server IP addresses.
        - ssidNumbers (array): Filter results for these SSID Numbers.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networkServices", "serverHealth", "byServerType"],
            "operation": "getOrganizationAssuranceNetworkServicesServerHealthByServerType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/networkServices/serverHealth/byServerType"

        query_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
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
                    f"getOrganizationAssuranceNetworkServicesServerHealthByServerType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceNetworkServicesServerHealthByServerTypeByInterval(self, organizationId: str, **kwargs):
        """
        **Returns network server health in organization by server type and by interval.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-network-services-server-health-by-server-type-by-interval

        - organizationId (string): Organization ID
        - networkIds (array): Filter results for these networks.
        - serverTypes (array): Filter results for these server types.
        - serverIps (array): Filter results for these server IP addresses.
        - ssidNumbers (array): Filter results for these SSID Numbers.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networkServices", "serverHealth", "byServerType", "byInterval"],
            "operation": "getOrganizationAssuranceNetworkServicesServerHealthByServerTypeByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/networkServices/serverHealth/byServerType/byInterval"

        query_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serverTypes",
            "serverIps",
            "ssidNumbers",
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
                    f"getOrganizationAssuranceNetworkServicesServerHealthByServerTypeByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def checkupOrganizationAssuranceOptimization(self, organizationId: str, **kwargs):
        """
        **Returns an array of checkup results for the organization**
        https://developer.cisco.com/meraki/api-v1/#!checkup-organization-assurance-optimization

        - organizationId (string): Organization ID
        - forceRefresh (boolean): Optional parameter to reassess best practices
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "optimization"],
            "operation": "checkupOrganizationAssuranceOptimization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/optimization/checkup"

        query_params = [
            "forceRefresh",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"checkupOrganizationAssuranceOptimization: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceOptimizationCheckupByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns an array of checkup results for the networks**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-optimization-checkup-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 7.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter checkups by Network Id
        - forceRefresh (boolean): Optional parameter to reassess best practices
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "optimization", "checkup", "byNetwork"],
            "operation": "getOrganizationAssuranceOptimizationCheckupByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/optimization/checkup/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "forceRefresh",
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
                    f"getOrganizationAssuranceOptimizationCheckupByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceProductAnnouncements(self, organizationId: str, **kwargs):
        """
        **Gets relevant product announcements for a user**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-product-announcements

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 365 days, 5 hours, 49 minutes, and 12 seconds. The default is 91 days, 7 hours, 27 minutes, and 18 seconds.
        - onlyRelevant (boolean): Limits product announcements that are considered relevant to this user when true
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "productAnnouncements"],
            "operation": "getOrganizationAssuranceProductAnnouncements",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/productAnnouncements"

        query_params = [
            "t0",
            "timespan",
            "onlyRelevant",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationAssuranceProductAnnouncements: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceScores(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get network health scores for a list of networks.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-scores

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 2 hours and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "scores"],
            "operation": "getOrganizationAssuranceScores",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/scores"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
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
                self._session._logger.warning(f"getOrganizationAssuranceScores: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceThousandEyesApplications(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Get a list of Thousand Eyes applications with their alerts.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-thousand-eyes-applications

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - clientId (string): Filter results by client.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "thousandEyes", "applications"],
            "operation": "getOrganizationAssuranceThousandEyesApplications",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/thousandEyes/applications"

        query_params = [
            "networkIds",
            "clientId",
            "t0",
            "t1",
            "timespan",
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
                    f"getOrganizationAssuranceThousandEyesApplications: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wired connection successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "wired", "experience", "successfulConnections", "byNetwork"],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClient(self, organizationId: str, **kwargs):
        """
        **Summarizes wired connection successes and failures by client.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "wired", "experience", "successfulConnections", "byNetwork", "byClient"],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork/byClient"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClientOs(self, organizationId: str, **kwargs):
        """
        **Summarizes wired connection successes and failures by client OS.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network-by-client-os

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "wired", "experience", "successfulConnections", "byNetwork", "byClientOs"],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClientOs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork/byClientOs"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClientOs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClientType(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wired connection successes and failures by client type.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network-by-client-type

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": [
                "organizations",
                "configure",
                "wired",
                "experience",
                "successfulConnections",
                "byNetwork",
                "byClientType",
            ],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClientType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork/byClientType"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByClientType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wired connection successes and failures by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "wired", "experience", "successfulConnections", "byNetwork", "byDevice"],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByInterval(self, organizationId: str, **kwargs):
        """
        **Time-series of wired connection successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network-by-interval

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 60, 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "wired", "experience", "successfulConnections", "byNetwork", "byInterval"],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByServer(self, organizationId: str, **kwargs):
        """
        **Summarizes wired connection successes and failures by server.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wired-experience-successful-connections-by-network-by-server

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "wired", "experience", "successfulConnections", "byNetwork", "byServer"],
            "operation": "getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wired/experience/successfulConnections/byNetwork/byServer"

        query_params = [
            "networkIds",
            "serials",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationAssuranceWiredExperienceSuccessfulConnectionsByNetworkByServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWorkflows(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return workflows filtered by organization ID, network ID, type, and category**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-workflows

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 30.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'.
        - networkIds (array): Optional parameter to filter by network ID
        - types (array): Optional parameter to filter workflows by types
        - categories (array): Optional parameter to filter workflows by categories
        - scopeTypes (array): Optional parameter to filter workflows by scope types
        - networkTags (array): Optional parameter to filter workflows by network tags
        - clientTags (array): Optional parameter to filter workflows by client tags
        - nodeTags (array): Optional parameter to filter workflows by node tags
        - state (string): Optional parameter to filter workflows by state
        - tsStart (string): Start time to filter workflows
        - tsEnd (string): End time to filter workflows
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "workflows"],
            "operation": "getOrganizationAssuranceWorkflows",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/workflows"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "networkIds",
            "types",
            "categories",
            "scopeTypes",
            "networkTags",
            "clientTags",
            "nodeTags",
            "state",
            "tsStart",
            "tsEnd",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "types",
            "categories",
            "scopeTypes",
            "networkTags",
            "clientTags",
            "nodeTags",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationAssuranceWorkflows: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAuthRadiusServers(self, organizationId: str):
        """
        **List the organization-wide RADIUS servers in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-auth-radius-servers

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "auth", "radius", "servers"],
            "operation": "getOrganizationAuthRadiusServers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/auth/radius/servers"

        return self._session.get(metadata, resource)

    def createOrganizationAuthRadiusServer(self, organizationId: str, address: str, secret: str, **kwargs):
        """
        **Add an organization-wide RADIUS server**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-auth-radius-server

        - organizationId (string): Organization ID
        - address (string): The IP address or FQDN of the RADIUS server
        - secret (string): Shared secret of the RADIUS server
        - name (string): The name of the RADIUS server
        - modes (array): Available server modes
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "auth", "radius", "servers"],
            "operation": "createOrganizationAuthRadiusServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/auth/radius/servers"

        body_params = [
            "name",
            "address",
            "modes",
            "secret",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationAuthRadiusServer: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationAuthRadiusServersAssignments(self, organizationId: str):
        """
        **Return list of network and policies that organization-wide RADIUS servers are bing used**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-auth-radius-servers-assignments

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "auth", "radius", "servers", "assignments"],
            "operation": "getOrganizationAuthRadiusServersAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/auth/radius/servers/assignments"

        return self._session.get(metadata, resource)

    def getOrganizationAuthRadiusServer(self, organizationId: str, serverId: str):
        """
        **Return an organization-wide RADIUS server**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-auth-radius-server

        - organizationId (string): Organization ID
        - serverId (string): Server ID
        """

        metadata = {
            "tags": ["organizations", "configure", "auth", "radius", "servers"],
            "operation": "getOrganizationAuthRadiusServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        serverId = urllib.parse.quote(str(serverId), safe="")
        resource = f"/organizations/{organizationId}/auth/radius/servers/{serverId}"

        return self._session.get(metadata, resource)

    def updateOrganizationAuthRadiusServer(self, organizationId: str, serverId: str, **kwargs):
        """
        **Update an organization-wide RADIUS server**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-auth-radius-server

        - organizationId (string): Organization ID
        - serverId (string): Server ID
        - name (string): The name of the RADIUS server
        - address (string): The IP address or FQDN of the RADIUS server
        - modes (array): Available server modes
        - secret (string): Shared secret of the RADIUS server
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "auth", "radius", "servers"],
            "operation": "updateOrganizationAuthRadiusServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        serverId = urllib.parse.quote(str(serverId), safe="")
        resource = f"/organizations/{organizationId}/auth/radius/servers/{serverId}"

        body_params = [
            "name",
            "address",
            "modes",
            "secret",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationAuthRadiusServer: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationAuthRadiusServer(self, organizationId: str, serverId: str):
        """
        **Delete an organization-wide RADIUS server from a organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-auth-radius-server

        - organizationId (string): Organization ID
        - serverId (string): Server ID
        """

        metadata = {
            "tags": ["organizations", "configure", "auth", "radius", "servers"],
            "operation": "deleteOrganizationAuthRadiusServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        serverId = urllib.parse.quote(str(serverId), safe="")
        resource = f"/organizations/{organizationId}/auth/radius/servers/{serverId}"

        return self._session.delete(metadata, resource)

    def codeOrganizationAutomateIdentity(self, organizationId: str):
        """
        **Generate a single use short lived code that can be used to retrieve the identity of the current user in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!code-organization-automate-identity

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "automate", "identity"],
            "operation": "codeOrganizationAutomateIdentity",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/automate/identity/code"

        return self._session.post(metadata, resource)

    def getOrganizationBrandingPolicies(self, organizationId: str):
        """
        **List the branding policies of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "getOrganizationBrandingPolicies",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies"

        return self._session.get(metadata, resource)

    def createOrganizationBrandingPolicy(self, organizationId: str, name: str, **kwargs):
        """
               **Add a new branding policy to an organization**
               https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

               - organizationId (string): Organization ID
               - name (string): Name of the Dashboard branding policy.
               - enabled (boolean): Boolean indicating whether this policy is enabled.
               - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
               - helpSettings (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
             'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
             the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
             Dashboard; see the documentation for each property to see the allowed values.
        Each property defaults to 'default or inherit' when not provided.
               - customLogo (object): Properties describing the custom logo attached to the branding policy.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "createOrganizationBrandingPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationBrandingPolicy: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationBrandingPoliciesPriorities(self, organizationId: str):
        """
        **Return the branding policy IDs of an organization in priority order**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies", "priorities"],
            "operation": "getOrganizationBrandingPoliciesPriorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/priorities"

        return self._session.get(metadata, resource)

    def updateOrganizationBrandingPoliciesPriorities(self, organizationId: str, **kwargs):
        """
        **Update the priority ordering of an organization's branding policies.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        - organizationId (string): Organization ID
        - brandingPolicyIds (array):       An ordered list of branding policy IDs that determines the priority order of how to apply the policies

        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies", "priorities"],
            "operation": "updateOrganizationBrandingPoliciesPriorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/priorities"

        body_params = [
            "brandingPolicyIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationBrandingPoliciesPriorities: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Return a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

        - organizationId (string): Organization ID
        - brandingPolicyId (string): Branding policy ID
        """

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "getOrganizationBrandingPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        brandingPolicyId = urllib.parse.quote(str(brandingPolicyId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

        return self._session.get(metadata, resource)

    def updateOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str, name: str, **kwargs):
        """
          **Update a branding policy**
          https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

          - organizationId (string): Organization ID
          - brandingPolicyId (string): Branding policy ID
          - name (string): Name of the Dashboard branding policy.
          - enabled (boolean): Boolean indicating whether this policy is enabled.
          - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
          - helpSettings (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
        'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
        the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
        Dashboard; see the documentation for each property to see the allowed values.

          - customLogo (object): Properties describing the custom logo attached to the branding policy.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "updateOrganizationBrandingPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        brandingPolicyId = urllib.parse.quote(str(brandingPolicyId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationBrandingPolicy: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Delete a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

        - organizationId (string): Organization ID
        - brandingPolicyId (string): Branding policy ID
        """

        metadata = {
            "tags": ["organizations", "configure", "brandingPolicies"],
            "operation": "deleteOrganizationBrandingPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        brandingPolicyId = urllib.parse.quote(str(brandingPolicyId), safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

        return self._session.delete(metadata, resource)

    def getOrganizationCertificates(self, organizationId: str, **kwargs):
        """
        **Gets all or specific certificates for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-certificates

        - organizationId (string): Organization ID
        - certificateIds (array): List of ids for specific certificate retrieval
        - certManagedBy (array): List of cert managed by types
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "certificates"],
            "operation": "getOrganizationCertificates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates"

        query_params = [
            "certificateIds",
            "certManagedBy",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateIds",
            "certManagedBy",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationCertificates: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationCertificatesAuthorities(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List certificate authorities for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-certificates-authorities

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - authorityIds (array): Feature certificate authority IDs to filter by (exact match on each id; duplicates are ignored)
        - sortBy (string): Field to sort by (default: authorityId)
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["authorityId", "featureType", "status"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "certificates", "authorities"],
            "operation": "getOrganizationCertificatesAuthorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/authorities"

        query_params = [
            "authorityIds",
            "sortBy",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "authorityIds",
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
                    f"getOrganizationCertificatesAuthorities: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationCertificatesAuthority(self, organizationId: str, featureType: str, **kwargs):
        """
        **Create a certificate authority for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-certificates-authority

        - organizationId (string): Organization ID
        - featureType (string): Feature this CA serves (e.g., radsec, openroaming, zigbee)
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "certificates", "authorities"],
            "operation": "createOrganizationCertificatesAuthority",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/authorities"

        body_params = [
            "featureType",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationCertificatesAuthority: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationCertificatesAuthorities(self, organizationId: str, authorityId: str, **kwargs):
        """
        **Trust a newly created certificate authority (transition from untrusted to trusted).**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-certificates-authorities

        - organizationId (string): Organization ID
        - authorityId (string): ID of the certificate authority to trust. The CA must currently be untrusted.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "certificates", "authorities"],
            "operation": "updateOrganizationCertificatesAuthorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/authorities"

        body_params = [
            "authorityId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationCertificatesAuthorities: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationCertificatesAuthorities(self, organizationId: str, authorityId: str, name: str):
        """
        **Delete a certificate authority**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-certificates-authorities

        - organizationId (string): Organization ID
        - authorityId (string): ID of the certificate authority to delete
        - name (string): Certificate authority name
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "certificates", "authorities"],
            "operation": "deleteOrganizationCertificatesAuthorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/authorities"

        return self._session.delete(metadata, resource)

    def getOrganizationCertificatesAuthoritiesJob(self, organizationId: str, jobId: str):
        """
        **Return the status and result of a certificate authority job.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-certificates-authorities-job

        - organizationId (string): Organization ID
        - jobId (string): Job ID
        """

        metadata = {
            "tags": ["organizations", "configure", "certificates", "authorities", "jobs"],
            "operation": "getOrganizationCertificatesAuthoritiesJob",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        jobId = urllib.parse.quote(str(jobId), safe="")
        resource = f"/organizations/{organizationId}/certificates/authorities/jobs/{jobId}"

        return self._session.get(metadata, resource)

    def revokeOrganizationCertificatesAuthorities(self, organizationId: str, authorityId: str, **kwargs):
        """
        **Revoke a trusted feature certificate authority.**
        https://developer.cisco.com/meraki/api-v1/#!revoke-organization-certificates-authorities

        - organizationId (string): Organization ID
        - authorityId (string): ID of the feature certificate authority to revoke
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "certificates", "authorities"],
            "operation": "revokeOrganizationCertificatesAuthorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/authorities/revoke"

        body_params = [
            "authorityId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"revokeOrganizationCertificatesAuthorities: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def importOrganizationCertificates(self, organizationId: str, managedBy: str, contents: str, description: str, **kwargs):
        """
        **Import certificate for this organization**
        https://developer.cisco.com/meraki/api-v1/#!import-organization-certificates

        - organizationId (string): Organization ID
        - managedBy (string): Certificate managed by type [system_manager, mr, encrypted_syslog, grpc_dial_out]
        - contents (string): Certificate content in valid PEM format
        - description (string): Certificate description
        """

        kwargs = locals()

        if "managedBy" in kwargs:
            options = ["encrypted_syslog", "grpc_dial_out", "mr", "system_manager"]
            assert kwargs["managedBy"] in options, (
                f'''"managedBy" cannot be "{kwargs["managedBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "certificates"],
            "operation": "importOrganizationCertificates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/import"

        body_params = [
            "managedBy",
            "contents",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"importOrganizationCertificates: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationCertificatesMerakiAuthContents(self, organizationId: str):
        """
        **Download the public RADIUS certificate.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-certificates-meraki-auth-contents

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "certificates", "merakiAuth", "contents"],
            "operation": "getOrganizationCertificatesMerakiAuthContents",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/merakiAuth/contents"

        return self._session.get(metadata, resource)

    def getOrganizationCertificatesRevocationLists(self, organizationId: str, **kwargs):
        """
        **Return full certificate revocation lists (CRLs) for the organization's certificate authorities**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-certificates-revocation-lists

        - organizationId (string): Organization ID
        - certificateAuthorityIds (array): Optional filter: feature certificate authority IDs (base-10 integers). Every value must exist for this organization; otherwise the request fails. Omit to return CRLs for all feature CAs in the organization.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "certificates", "revocationLists"],
            "operation": "getOrganizationCertificatesRevocationLists",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/certificates/revocationLists"

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
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
                    f"getOrganizationCertificatesRevocationLists: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def deleteOrganizationCertificate(self, organizationId: str, certificateId: str):
        """
        **Delete a certificate for an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-certificate

        - organizationId (string): Organization ID
        - certificateId (string): Certificate ID
        """

        metadata = {
            "tags": ["organizations", "configure", "certificates"],
            "operation": "deleteOrganizationCertificate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        certificateId = urllib.parse.quote(str(certificateId), safe="")
        resource = f"/organizations/{organizationId}/certificates/{certificateId}"

        return self._session.delete(metadata, resource)

    def updateOrganizationCertificate(self, organizationId: str, certificateId: str, **kwargs):
        """
        **Update a certificate's description for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-certificate

        - organizationId (string): Organization ID
        - certificateId (string): Certificate ID
        - description (string): Description of a certificate that already exist in your org
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "certificates"],
            "operation": "updateOrganizationCertificate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        certificateId = urllib.parse.quote(str(certificateId), safe="")
        resource = f"/organizations/{organizationId}/certificates/{certificateId}"

        body_params = [
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationCertificate: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationCertificateContents(self, organizationId: str, certificateId: str, **kwargs):
        """
        **Download the trusted certificate by certificate id.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-certificate-contents

        - organizationId (string): Organization ID
        - certificateId (string): Certificate ID
        - chainId (string): chainId that represent which certificate chain is being requested
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "certificates", "contents"],
            "operation": "getOrganizationCertificateContents",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        certificateId = urllib.parse.quote(str(certificateId), safe="")
        resource = f"/organizations/{organizationId}/certificates/{certificateId}/contents"

        query_params = [
            "chainId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationCertificateContents: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def claimIntoOrganization(self, organizationId: str, **kwargs):
        """
        **Claim a list of devices, licenses, and/or orders into an organization inventory**
        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization

        - organizationId (string): Organization ID
        - orders (array): The numbers of the orders that should be claimed
        - serials (array): The serials of the devices that should be claimed
        - licenses (array): The licenses that should be claimed
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "claimIntoOrganization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/claim"

        body_params = [
            "orders",
            "serials",
            "licenses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"claimIntoOrganization: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationClientsBandwidthUsageHistory(self, organizationId: str, **kwargs):
        """
        **Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "clients", "bandwidthUsageHistory"],
            "operation": "getOrganizationClientsBandwidthUsageHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/clients/bandwidthUsageHistory"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationClientsBandwidthUsageHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationClientsOverview(self, organizationId: str, **kwargs):
        """
        **Return summary information around client data usage (in kb) across the given organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-overview

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "clients", "overview"],
            "operation": "getOrganizationClientsOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/clients/overview"

        query_params = [
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationClientsOverview: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationClientsSearch(self, organizationId: str, mac: str, total_pages=1, direction="next", **kwargs):
        """
        **Return the client details in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-search

        - organizationId (string): Organization ID
        - mac (string): The MAC address of the client. Required.
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "clients", "search"],
            "operation": "getOrganizationClientsSearch",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/clients/search"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "mac",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationClientsSearch: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def cloneOrganization(self, organizationId: str, name: str, **kwargs):
        """
        **Create a new organization by cloning the addressed organization**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization

        - organizationId (string): Organization ID
        - name (string): The name of the new organization
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure"],
            "operation": "cloneOrganization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/clone"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"cloneOrganization: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationCloudConnectivityRequirements(self, organizationId: str):
        """
        **List of source/destination traffic rules**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-cloud-connectivity-requirements

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "cloud", "connectivity", "requirements"],
            "operation": "getOrganizationCloudConnectivityRequirements",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/cloud/connectivity/requirements"

        return self._session.get(metadata, resource)

    def getOrganizationComputeApplicationDeployments(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the Application Deployment agent configurations for all hosts under this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-compute-application-deployments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - developerNames (array): Filters deployments by application developer name
        - applicationNames (array): Filters deployments by application name
        - enabled (boolean): Filters deployments by their enabled status
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "compute", "application", "deployments"],
            "operation": "getOrganizationComputeApplicationDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/compute/application/deployments"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "developerNames",
            "applicationNames",
            "enabled",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "developerNames",
            "applicationNames",
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
                    f"getOrganizationComputeApplicationDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationComputeApplicationDeploymentsBulkCreate(
        self, organizationId: str, hosts: list, application: dict, enabled: bool, **kwargs
    ):
        """
        **Add Application Deployment agents for a list of hosts**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-compute-application-deployments-bulk-create

        - organizationId (string): Organization ID
        - hosts (array): List of hosts to deploy applications on
        - application (object): Application information
        - enabled (boolean): Whether the deployment should be enabled
        - applicationConfiguration (object): Optional: Generic object for application-specific configuration
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "compute", "application", "deployments", "bulkCreate"],
            "operation": "createOrganizationComputeApplicationDeploymentsBulkCreate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/compute/application/deployments/bulkCreate"

        body_params = [
            "hosts",
            "application",
            "enabled",
            "applicationConfiguration",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationComputeApplicationDeploymentsBulkCreate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationComputeApplicationDeployment(self, organizationId: str, deploymentId: str, enabled: bool, **kwargs):
        """
        **Update a Deployment agent configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-compute-application-deployment

        - organizationId (string): Organization ID
        - deploymentId (string): Deployment ID
        - enabled (boolean): Whether or not the Application Deployment agent is enabled for the host.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "compute", "application", "deployments"],
            "operation": "updateOrganizationComputeApplicationDeployment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        deploymentId = urllib.parse.quote(str(deploymentId), safe="")
        resource = f"/organizations/{organizationId}/compute/application/deployments/{deploymentId}"

        body_params = [
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationComputeApplicationDeployment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationComputeApplicationDeployment(self, organizationId: str, deploymentId: str):
        """
        **Delete a Application Deployment agent from the host**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-compute-application-deployment

        - organizationId (string): Organization ID
        - deploymentId (string): Deployment ID
        """

        metadata = {
            "tags": ["organizations", "configure", "compute", "application", "deployments"],
            "operation": "deleteOrganizationComputeApplicationDeployment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        deploymentId = urllib.parse.quote(str(deploymentId), safe="")
        resource = f"/organizations/{organizationId}/compute/application/deployments/{deploymentId}"

        return self._session.delete(metadata, resource)

    def getOrganizationComputeHosts(
        self, organizationId: str, developerName: str, applicationName: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Retrieves a list of compute hosts eligible for application deployment within a given organization, filtered by the specified application developer and application name, with optional network ID filtering.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-compute-hosts

        - organizationId (string): Organization ID
        - developerName (string): Filters hosts by application developer name
        - applicationName (string): Filters hosts by application name
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Filters hosts by the network ID they belong to
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "compute", "hosts"],
            "operation": "getOrganizationComputeHosts",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/compute/hosts"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "developerName",
            "applicationName",
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
                self._session._logger.warning(f"getOrganizationComputeHosts: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationConfigTemplates(self, organizationId: str):
        """
        **List the configuration templates for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "getOrganizationConfigTemplates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates"

        return self._session.get(metadata, resource)

    def createOrganizationConfigTemplate(self, organizationId: str, name: str, **kwargs):
        """
        **Create a new configuration template**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        - organizationId (string): Organization ID
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
        - copyFromNetworkId (string): The ID of the network or config template to copy configuration from
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "createOrganizationConfigTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates"

        body_params = [
            "name",
            "timeZone",
            "copyFromNetworkId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationConfigTemplate: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Return a single configuration template**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        """

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "getOrganizationConfigTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}"

        return self._session.get(metadata, resource)

    def updateOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str, **kwargs):
        """
        **Update a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "updateOrganizationConfigTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}"

        body_params = [
            "name",
            "timeZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationConfigTemplate: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Remove a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        """

        metadata = {
            "tags": ["organizations", "configure", "configTemplates"],
            "operation": "deleteOrganizationConfigTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe="")
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}"

        return self._session.delete(metadata, resource)

    def getOrganizationConfigurationChanges(self, organizationId: str, total_pages=1, direction="prev", **kwargs):
        """
        **View the Change Log for your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" or "prev" (default) page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 5000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkId (string): Filters on the given network
        - adminId (string): Filters on the given Admin
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "configurationChanges"],
            "operation": "getOrganizationConfigurationChanges",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/configurationChanges"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkId",
            "adminId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationConfigurationChanges: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevices(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the devices in an organization that have been assigned to a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Filter results by whether or not the device's configuration has been updated after the given timestamp
        - networkIds (array): Optional parameter to filter devices by network.
        - productTypes (array): Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        - tags (array): Optional parameter to filter devices by tags.
        - tagsFilterType (string): Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - name (string): Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
        - mac (string): Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
        - serial (string): Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
        - model (string): Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
        - macs (array): Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
        - serials (array): Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
        - sensorMetrics (array): Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
        - sensorAlertProfileIds (array): Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
        - models (array): Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
        """

        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices"],
            "operation": "getOrganizationDevices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "configurationUpdatedAfter",
            "networkIds",
            "productTypes",
            "tags",
            "tagsFilterType",
            "name",
            "mac",
            "serial",
            "model",
            "macs",
            "serials",
            "sensorMetrics",
            "sensorAlertProfileIds",
            "models",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "tags",
            "macs",
            "serials",
            "sensorMetrics",
            "sensorAlertProfileIds",
            "models",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationDevices: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesAvailabilities(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the availability information for devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches. Valid types are wireless, appliance, switch, camera, cellularGateway, sensor, wirelessController, and campusGateway
        - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - statuses (array): Optional parameter to filter device availabilities by device status. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "availabilities"],
            "operation": "getOrganizationDevicesAvailabilities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/availabilities"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "tagsFilterType",
            "statuses",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "statuses",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationDevicesAvailabilities: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesAvailabilitiesChangeHistory(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the availability history information for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities-change-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - serials (array): Optional parameter to filter device availabilities history by device serial numbers
        - productTypes (array): Optional parameter to filter device availabilities history by device product types
        - networkIds (array): Optional parameter to filter device availabilities history by network IDs
        - statuses (array): Optional parameter to filter device availabilities history by device statuses
        - categories (array): Optional parameter to filter device availabilities history by categories of status, reboot, or upgrade
        - networkTags (array): Optional parameter to filter device availabilities history by network tags. The filtering is case-sensitive. If tags are included, 'networkTagsFilterType' should also be included (see below).
        - networkTagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - deviceTags (array): Optional parameter to filter device availabilities history by device tags. The filtering is case-sensitive. If tags are included, 'deviceTagsFilterType' should also be included (see below).
        - deviceTagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if "networkTagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["networkTagsFilterType"] in options, (
                f'''"networkTagsFilterType" cannot be "{kwargs["networkTagsFilterType"]}", & must be set to one of: {options}'''
            )
        if "deviceTagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["deviceTagsFilterType"] in options, (
                f'''"deviceTagsFilterType" cannot be "{kwargs["deviceTagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "availabilities", "changeHistory"],
            "operation": "getOrganizationDevicesAvailabilitiesChangeHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/availabilities/changeHistory"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "serials",
            "productTypes",
            "networkIds",
            "statuses",
            "categories",
            "networkTags",
            "networkTagsFilterType",
            "deviceTags",
            "deviceTagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "productTypes",
            "networkIds",
            "statuses",
            "categories",
            "networkTags",
            "deviceTags",
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
                    f"getOrganizationDevicesAvailabilitiesChangeHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesBootsHistory(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns the history of device boots in reverse chronological order (most recent first)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-boots-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 730 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 730 days.
        - serials (array): Optional parameter to filter device by device serial numbers. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        - mostRecentPerDevice (boolean): If true, only the most recent boot for each device is returned.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "boots", "history"],
            "operation": "getOrganizationDevicesBootsHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/boots/history"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "serials",
            "productTypes",
            "mostRecentPerDevice",
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "productTypes",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationDevicesBootsHistory: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesBootsOverviewByDevice(self, organizationId: str, **kwargs):
        """
        **Summarizes device reboots across an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-boots-overview-by-device

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "boots", "overview", "byDevice"],
            "operation": "getOrganizationDevicesBootsOverviewByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/boots/overview/byDevice"

        query_params = [
            "networkIds",
            "productTypes",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
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
                    f"getOrganizationDevicesBootsOverviewByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationDevicesCellularDataDevices(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List devices eligible for Cellular Data Management profile assignment in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-data-devices

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - includeAssigned (boolean): Whether to include devices that have already been assigned to a Cellular Data Management Profile
        - includedSerials (array): List of device serials to force-include in the response when the devices would otherwise be filtered out. This override is primarily useful for keeping selected devices visible while paging through results. Maximum 1000 serials.
        - excludedSerials (array): List of device serials to force-exclude from the response when the devices would otherwise be returned. This override is primarily useful for hiding selected devices while paging through results. Maximum 1000 serials.
        - includedProfileIds (array): List of Cellular Data Management Profile IDs to include in the results. Maximum 1000 profile IDs.
        - excludedProfileIds (array): List of Cellular Data Management Profile IDs to exclude from the results. Maximum 1000 profile IDs.
        - deviceTypes (array): List of device types to filter by. Maximum 1000 device types.
        - slots (array): List of SIM slot types that devices must support. Accepted values are sim1, sim2, and esim. Maximum 3 slots.
        - name (string): Name of the device to filter by (partial matches allowed)
        - serials (array): List of device serials to filter by. Maximum 1000 serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "cellular", "data"],
            "operation": "getOrganizationDevicesCellularDataDevices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/devices"

        query_params = [
            "includeAssigned",
            "includedSerials",
            "excludedSerials",
            "includedProfileIds",
            "excludedProfileIds",
            "deviceTypes",
            "slots",
            "name",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "includedSerials",
            "excludedSerials",
            "includedProfileIds",
            "excludedProfileIds",
            "deviceTypes",
            "slots",
            "serials",
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
                    f"getOrganizationDevicesCellularDataDevices: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesCellularDataProfiles(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List cellular data management profiles in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-data-profiles

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - profileIds (array): Optional parameter to filter the results by Data Management Profile ID.
        - serials (array): Devices to find Cellular Data Management Profiles for.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles"],
            "operation": "getOrganizationDevicesCellularDataProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles"

        query_params = [
            "profileIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "profileIds",
            "serials",
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
                    f"getOrganizationDevicesCellularDataProfiles: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationDevicesCellularDataProfile(
        self, organizationId: str, name: str, description: str, rules: list, **kwargs
    ):
        """
        **Add a cellular data management profile to this organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-cellular-data-profile

        - organizationId (string): Organization ID
        - name (string): Name of the profile to be added. This must be unique.
        - description (string): Description of the profile to be added.
        - rules (array): The rules associated with this profile. At least one rule and no more than two rules may be defined for a profile.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles"],
            "operation": "createOrganizationDevicesCellularDataProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles"

        body_params = [
            "name",
            "description",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationDevicesCellularDataProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationDevicesCellularDataProfilesAssignments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List Cellular Data Management Profile assignments in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-data-profiles-assignments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - profileIds (array): Optional parameter to find assignments by Profile IDs. Maximum 1000 profile IDs.
        - serials (array): Optional parameter to find assignments by Device Serials. Maximum 1000 serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles", "assignments"],
            "operation": "getOrganizationDevicesCellularDataProfilesAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/assignments"

        query_params = [
            "profileIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "profileIds",
            "serials",
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
                    f"getOrganizationDevicesCellularDataProfilesAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def batchOrganizationDevicesCellularDataProfilesAssignmentsCreate(self, organizationId: str, items: list, **kwargs):
        """
        **Assign devices to a Cellular Data Management Profile in batch**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-devices-cellular-data-profiles-assignments-create

        - organizationId (string): Organization ID
        - items (array): List of device-to-profile assignments to create.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles", "assignments"],
            "operation": "batchOrganizationDevicesCellularDataProfilesAssignmentsCreate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/assignments/batchCreate"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"batchOrganizationDevicesCellularDataProfilesAssignmentsCreate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationDevicesCellularDataProfilesAssignmentsDelete(self, organizationId: str, items: list, **kwargs):
        """
        **Unassign devices from a Cellular Data Management Profile in batch**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-cellular-data-profiles-assignments-delete

        - organizationId (string): Organization ID
        - items (array): List of device-to-profile assignments to remove.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles", "assignments"],
            "operation": "bulkOrganizationDevicesCellularDataProfilesAssignmentsDelete",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/assignments/bulkDelete"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationDevicesCellularDataProfilesAssignmentsDelete: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationDevicesCellularDataProfile(self, organizationId: str, rules: list, profileId: str, **kwargs):
        """
        **Update a Cellular Data Management Profile**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-cellular-data-profile

        - organizationId (string): Organization ID
        - rules (array): The rules associated with this profile. At least one rule and no more than two rules may be defined for a profile.
        - profileId (string): ID of the profile.
        - description (string): New description of the profile.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles"],
            "operation": "updateOrganizationDevicesCellularDataProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/{profileId}"

        body_params = [
            "profileId",
            "description",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationDevicesCellularDataProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationDevicesCellularDataProfile(self, organizationId: str, profileId: str):
        """
        **Delete a cellular data management profile from this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-cellular-data-profile

        - organizationId (string): Organization ID
        - profileId (string): Profile ID
        """

        metadata = {
            "tags": ["organizations", "configure", "devices", "cellular", "data", "profiles"],
            "operation": "deleteOrganizationDevicesCellularDataProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/{profileId}"

        return self._session.delete(metadata, resource)

    def getOrganizationDevicesCellularDataUsageByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List current cellular data usage for devices in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-data-usage-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Filter the results by device serials. Maximum 1000 serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "cellular", "data", "usage", "byDevice"],
            "operation": "getOrganizationDevicesCellularDataUsageByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/usage/byDevice"

        query_params = [
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
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
                    f"getOrganizationDevicesCellularDataUsageByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesCellularDataUsageHistoryByDeviceByInterval(
        self, organizationId: str, serials: list, total_pages=1, direction="next", **kwargs
    ):
        """
        **List historical cellular data usage grouped by device and interval in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-data-usage-history-by-device-by-interval

        - organizationId (string): Organization ID
        - serials (array): Required parameter to filter the results by device serials. Maximum 10 serials.
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10. Default is 5.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 366 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 1200, 14400, 86400. The default is 86400. Interval is calculated if time params are provided.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "cellular", "data", "usage", "history", "byDevice", "byInterval"],
            "operation": "getOrganizationDevicesCellularDataUsageHistoryByDeviceByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/usage/history/byDevice/byInterval"

        query_params = [
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
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
                    f"getOrganizationDevicesCellularDataUsageHistoryByDeviceByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesCellularGeolocations(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the latest cellular geolocation telemetry for devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-geolocations

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter the results by device serials. Maximum 1000 serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "cellular", "geolocations"],
            "operation": "getOrganizationDevicesCellularGeolocations",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/geolocations"

        query_params = [
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
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
                    f"getOrganizationDevicesCellularGeolocations: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesCellularUplinksBandsByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the latest cellular uplink signal information for devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-uplinks-bands-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter the results by device serials. Maximum 1000 serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "cellular", "uplinks", "bands", "byDevice"],
            "operation": "getOrganizationDevicesCellularUplinksBandsByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/uplinks/bands/byDevice"

        query_params = [
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
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
                    f"getOrganizationDevicesCellularUplinksBandsByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesCellularUplinksTowersByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the latest cellular tower information for devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-cellular-uplinks-towers-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Optional parameter to filter the results by device serials. Maximum 1000 serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "cellular", "uplinks", "towers", "byDevice"],
            "operation": "getOrganizationDevicesCellularUplinksTowersByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/uplinks/towers/byDevice"

        query_params = [
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
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
                    f"getOrganizationDevicesCellularUplinksTowersByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesCertificates(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List device certificates for the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-certificates

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): Device serial numbers to filter by (exact match; duplicates are ignored)
        - featureTypes (array): Feature types these device certificates serve (exact match; e.g., radsec, openroaming, zigbee)
        - sortBy (string): Field to sort by (default: authorityId)
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["authorityId", "featureType", "status"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "certificates"],
            "operation": "getOrganizationDevicesCertificates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/certificates"

        query_params = [
            "serials",
            "featureTypes",
            "sortBy",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
            "featureTypes",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationDevicesCertificates: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationDevicesControllerMigration(self, organizationId: str, serials: list, target: str, **kwargs):
        """
        **Migrate devices to another controller or management mode**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-controller-migration

        - organizationId (string): Organization ID
        - serials (array): A list of Meraki Serials to migrate
        - target (string): The controller or management mode to which the devices will be migrated
        """

        kwargs = locals()

        if "target" in kwargs:
            options = ["wirelessController"]
            assert kwargs["target"] in options, (
                f'''"target" cannot be "{kwargs["target"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "controller", "migrations"],
            "operation": "createOrganizationDevicesControllerMigration",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/controller/migrations"

        body_params = [
            "serials",
            "target",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationDevicesControllerMigration: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationDevicesControllerMigrations(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Retrieve device migration statuses in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-controller-migrations

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): A list of Meraki Serials for which to retrieve migrations
        - networkIds (array): Filter device migrations by network IDs
        - target (string): Filter device migrations by target destination
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "target" in kwargs:
            options = ["wirelessController"]
            assert kwargs["target"] in options, (
                f'''"target" cannot be "{kwargs["target"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "controller", "migrations"],
            "operation": "getOrganizationDevicesControllerMigrations",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/controller/migrations"

        query_params = [
            "serials",
            "networkIds",
            "target",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
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
                    f"getOrganizationDevicesControllerMigrations: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def bulkUpdateOrganizationDevicesDetails(self, organizationId: str, serials: list, details: list, **kwargs):
        """
        **Updating device details (currently only used for Catalyst devices)**
        https://developer.cisco.com/meraki/api-v1/#!bulk-update-organization-devices-details

        - organizationId (string): Organization ID
        - serials (array): A list of serials of devices to update
        - details (array): An array of details
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "details", "bulkUpdate"],
            "operation": "bulkUpdateOrganizationDevicesDetails",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/details/bulkUpdate"

        body_params = [
            "serials",
            "details",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"bulkUpdateOrganizationDevicesDetails: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationDevicesMemoryByDevice(self, organizationId: str, networkIds: list, productTypes: list, **kwargs):
        """
        **Summarizes memory status across devices of a given network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-memory-by-device

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - productTypes (array): Parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
        - usageThreshold (number): Threshold of device memory utilization expressed as a percent. Filters out all devices below this value.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 1 hour and be less than or equal to 7 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "memory", "byDevice"],
            "operation": "getOrganizationDevicesMemoryByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/memory/byDevice"

        query_params = [
            "networkIds",
            "productTypes",
            "usageThreshold",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationDevicesMemoryByDevice: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationDevicesOverviewByModel(self, organizationId: str, **kwargs):
        """
        **Lists the count for each device model**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-overview-by-model

        - organizationId (string): Organization ID
        - models (array): Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
        - networkIds (array): Optional parameter to filter devices by networkId.
        - productTypes (array): Optional parameter to filter device by device product types. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "overview", "byModel"],
            "operation": "getOrganizationDevicesOverviewByModel",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/overview/byModel"

        query_params = [
            "models",
            "networkIds",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "models",
            "networkIds",
            "productTypes",
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
                    f"getOrganizationDevicesOverviewByModel: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationDevicesPacketCaptureCaptures(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List Packet Captures**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-captures

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - captureIds (array): Return the packet captures of the specified capture ids
        - networkIds (array): Return the packet captures of the specified network(s)
        - serials (array): Return the packet captures of the specified device(s)
        - process (array): Return the packet captures of the specified process
        - captureStatus (array): Return the packet captures of the specified capture status
        - name (array): Return the packet captures matching the specified name
        - clientMac (array): Return the packet captures matching the specified client macs
        - notes (string): Return the packet captures matching the specified notes
        - deviceName (string): Return the packet captures matching the specified device name
        - adminName (string): Return the packet captures matching the admin name
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "getOrganizationDevicesPacketCaptureCaptures",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures"

        query_params = [
            "captureIds",
            "networkIds",
            "serials",
            "process",
            "captureStatus",
            "name",
            "clientMac",
            "notes",
            "deviceName",
            "adminName",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "captureIds",
            "networkIds",
            "serials",
            "process",
            "captureStatus",
            "name",
            "clientMac",
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
                    f"getOrganizationDevicesPacketCaptureCaptures: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationDevicesPacketCaptureCapture(self, organizationId: str, serials: list, name: str, **kwargs):
        """
        **Perform a packet capture on a device and store in Meraki Cloud**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-capture

        - organizationId (string): Organization ID
        - serials (array): The serial(s) of the device(s)
        - name (string): Name of packet capture file
        - outputType (string): Output type of packet capture file. Possible values: text, pcap, cloudshark, or upload_to_cloud
        - destination (string): Destination of packet capture file. Possible values: [upload_to_cloud]
        - ports (string): Ports of packet capture file, comma-separated
        - notes (string): Reason for taking the packet capture
        - duration (integer): Duration in seconds of packet capture
        - filterExpression (string): Filter expression for packet capture
        - interface (string): Interface of the device
        - advanced (object): Advanced filters for IOSXE devices (supported for Campus Gateway devices only)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "createOrganizationDevicesPacketCaptureCapture",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures"

        body_params = [
            "serials",
            "name",
            "outputType",
            "destination",
            "ports",
            "notes",
            "duration",
            "filterExpression",
            "interface",
            "advanced",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationDevicesPacketCaptureCapture: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationDevicesPacketCaptureCapturesCreate(self, organizationId: str, devices: list, name: str, **kwargs):
        """
        **Perform a packet capture on multiple devices and store in Meraki Cloud.**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-create

        - organizationId (string): Organization ID
        - devices (array): Device details (maximum of 20 devices allowed)
        - name (string): Name of packet capture file
        - notes (string): Reason for capture
        - duration (integer): Duration of the capture in seconds
        - filterExpression (string): Filter expression for the capture
        - advanced (object): Advanced capture options (optional)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "bulkOrganizationDevicesPacketCaptureCapturesCreate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/bulkCreate"

        body_params = [
            "devices",
            "notes",
            "duration",
            "filterExpression",
            "name",
            "advanced",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationDevicesPacketCaptureCapturesCreate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationDevicesPacketCaptureCapturesDelete(self, organizationId: str, captureIds: list, **kwargs):
        """
        **BulkDelete packet captures from cloud**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-delete

        - organizationId (string): Organization ID
        - captureIds (array): Delete the packet captures of the specified capture ids
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "bulkOrganizationDevicesPacketCaptureCapturesDelete",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/bulkDelete"

        body_params = [
            "captureIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationDevicesPacketCaptureCapturesDelete: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationDevicesPacketCaptureCapture(self, organizationId: str, captureId: str):
        """
        **Delete a single packet capture from cloud using captureId**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-capture

        - organizationId (string): Organization ID
        - captureId (string): Capture ID
        """

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "deleteOrganizationDevicesPacketCaptureCapture",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        captureId = urllib.parse.quote(str(captureId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/{captureId}"

        return self._session.delete(metadata, resource)

    def generateOrganizationDevicesPacketCaptureCaptureDownloadUrl(self, organizationId: str, captureId: str):
        """
        **Get presigned download URL for given packet capture id**
        https://developer.cisco.com/meraki/api-v1/#!generate-organization-devices-packet-capture-capture-download-url

        - organizationId (string): Organization ID
        - captureId (string): Capture ID
        """

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures", "downloadUrl"],
            "operation": "generateOrganizationDevicesPacketCaptureCaptureDownloadUrl",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        captureId = urllib.parse.quote(str(captureId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/{captureId}/downloadUrl/generate"

        return self._session.post(metadata, resource)

    def stopOrganizationDevicesPacketCaptureCapture(self, organizationId: str, captureId: str, serials: list, **kwargs):
        """
        **Stop a specific packet capture (not supported for Catalyst devices)**
        https://developer.cisco.com/meraki/api-v1/#!stop-organization-devices-packet-capture-capture

        - organizationId (string): Organization ID
        - captureId (string): Capture ID
        - serials (array): The serial(s) of the device(s) to stop the capture on
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "captures"],
            "operation": "stopOrganizationDevicesPacketCaptureCapture",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        captureId = urllib.parse.quote(str(captureId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/{captureId}/stop"

        body_params = [
            "serials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"stopOrganizationDevicesPacketCaptureCapture: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationDevicesPacketCaptureOpportunisticByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the Opportunistic Pcap settings of an organization by network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-opportunistic-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter results by network.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "opportunistic", "byNetwork"],
            "operation": "getOrganizationDevicesPacketCaptureOpportunisticByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/opportunistic/byNetwork"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
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
                    f"getOrganizationDevicesPacketCaptureOpportunisticByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesPacketCaptureSchedules(self, organizationId: str, **kwargs):
        """
        **List the Packet Capture Schedules**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-schedules

        - organizationId (string): Organization ID
        - scheduleIds (array): Return the packet captures schedules of the specified packet capture schedule ids
        - networkIds (array): Return the scheduled packet captures of the specified network(s)
        - deviceIds (array): Return the scheduled packet captures of the specified device(s)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "getOrganizationDevicesPacketCaptureSchedules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules"

        query_params = [
            "scheduleIds",
            "networkIds",
            "deviceIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "scheduleIds",
            "networkIds",
            "deviceIds",
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
                    f"getOrganizationDevicesPacketCaptureSchedules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def createOrganizationDevicesPacketCaptureSchedule(self, organizationId: str, devices: list, **kwargs):
        """
        **Create a schedule for packet capture**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-schedule

        - organizationId (string): Organization ID
        - devices (array): device details
        - name (string): Name of the packet capture file
        - notes (string): Reason for capture
        - duration (integer): Duration of the capture in seconds
        - filterExpression (string): Filter expression for the capture
        - enabled (boolean): Enable or disable the schedule
        - schedule (object): Schedule details
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "createOrganizationDevicesPacketCaptureSchedule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules"

        body_params = [
            "devices",
            "name",
            "notes",
            "duration",
            "filterExpression",
            "enabled",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationDevicesPacketCaptureSchedule: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationDevicesPacketCaptureSchedulesDelete(self, organizationId: str, scheduleIds: list, **kwargs):
        """
        **Delete packet capture schedules**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-schedules-delete

        - organizationId (string): Organization ID
        - scheduleIds (array): Delete the packet capture schedules of the specified schedule ids
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "bulkOrganizationDevicesPacketCaptureSchedulesDelete",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/bulkDelete"

        body_params = [
            "scheduleIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationDevicesPacketCaptureSchedulesDelete: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def reorderOrganizationDevicesPacketCaptureSchedules(self, organizationId: str, order: list, **kwargs):
        """
        **Bulk update priorities of pcap schedules**
        https://developer.cisco.com/meraki/api-v1/#!reorder-organization-devices-packet-capture-schedules

        - organizationId (string): Organization ID
        - order (array): Array of schedule IDs and their priorities to reorder.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "reorderOrganizationDevicesPacketCaptureSchedules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/reorder"

        body_params = [
            "order",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"reorderOrganizationDevicesPacketCaptureSchedules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationDevicesPacketCaptureSchedule(self, organizationId: str, scheduleId: str, devices: list, **kwargs):
        """
        **Update a schedule for packet capture**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-packet-capture-schedule

        - organizationId (string): Organization ID
        - scheduleId (string): Schedule ID
        - devices (array): device details
        - name (string): Name of the packet capture file
        - notes (string): Reason for capture
        - duration (integer): Duration of the capture in seconds
        - filterExpression (string): Filter expression for the capture
        - enabled (boolean): Enable or disable the schedule
        - schedule (object): Schedule details
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "updateOrganizationDevicesPacketCaptureSchedule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        scheduleId = urllib.parse.quote(str(scheduleId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId}"

        body_params = [
            "devices",
            "name",
            "notes",
            "duration",
            "filterExpression",
            "enabled",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationDevicesPacketCaptureSchedule: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationDevicesPacketCaptureSchedule(self, organizationId: str, scheduleId: str):
        """
        **Delete schedule from cloud**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-schedule

        - organizationId (string): Organization ID
        - scheduleId (string): Delete the capture schedules of the specified capture schedule id
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCapture", "schedules"],
            "operation": "deleteOrganizationDevicesPacketCaptureSchedule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        scheduleId = urllib.parse.quote(str(scheduleId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId}"

        return self._session.delete(metadata, resource)

    def tasksOrganizationDevicesPacketCapture(self, organizationId: str, packetId: str, task: str, **kwargs):
        """
        **Enqueues a task for a specific packet capture**
        https://developer.cisco.com/meraki/api-v1/#!tasks-organization-devices-packet-capture

        - organizationId (string): Organization ID
        - packetId (string): Packet ID
        - task (string): Type of task to enqueue. It can be one of: ["analysis", "reasoning", "summary", "highlights", "title", "flow"]
        - networkId (string): Parameter to validate authorization by network access
        """

        kwargs.update(locals())

        if "task" in kwargs:
            options = ["analysis", "flow", "highlights", "reasoning", "summary", "title"]
            assert kwargs["task"] in options, f'''"task" cannot be "{kwargs["task"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCaptures"],
            "operation": "tasksOrganizationDevicesPacketCapture",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        packetId = urllib.parse.quote(str(packetId), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCaptures/{packetId}/tasks"

        body_params = [
            "networkId",
            "task",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"tasksOrganizationDevicesPacketCapture: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationDevicesPacketCaptureTask(self, organizationId: str, packetId: str, id: str, **kwargs):
        """
        **Retrieves packet capture analysis result for a specific packet capture task.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-packet-capture-task

        - organizationId (string): Organization ID
        - packetId (string): Packet ID
        - id (string): ID
        - networkId (string): Optional parameter to validate authorization by network access
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "packetCaptures", "tasks"],
            "operation": "getOrganizationDevicesPacketCaptureTask",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        packetId = urllib.parse.quote(str(packetId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/devices/packetCaptures/{packetId}/tasks/{id}"

        query_params = [
            "networkId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationDevicesPacketCaptureTask: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def bulkOrganizationDevicesPlacementPositionsUpdate(self, organizationId: str, serials: list, **kwargs):
        """
        **Bulk update the attributes related to positions for provided devices**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-placement-positions-update

        - organizationId (string): Organization ID
        - serials (array): List of device serials on a floor plan to update
        - height (object): Height of the devices on the floor plan
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "placement", "positions"],
            "operation": "bulkOrganizationDevicesPlacementPositionsUpdate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/placement/positions/bulkUpdate"

        body_params = [
            "serials",
            "height",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationDevicesPlacementPositionsUpdate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationDevicesPowerModulesStatusesByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the most recent status information for power modules in rackmount MX and MS devices that support them**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-power-modules-statuses-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "powerModules", "statuses", "byDevice"],
            "operation": "getOrganizationDevicesPowerModulesStatusesByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/powerModules/statuses/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
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
                    f"getOrganizationDevicesPowerModulesStatusesByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesProvisioningStatuses(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the provisioning statuses information for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-provisioning-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device by device product types. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device by device serial numbers. This filter uses multiple exact matches.
        - status (string): An optional parameter to filter devices by the provisioning status. Accepted statuses: unprovisioned, incomplete, complete.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if "status" in kwargs:
            options = ["complete", "incomplete", "unprovisioned"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )
        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "provisioning", "statuses"],
            "operation": "getOrganizationDevicesProvisioningStatuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/provisioning/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "status",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
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
                    f"getOrganizationDevicesProvisioningStatuses: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesSoftwareUpdatesOverviewsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns details about software updates for networks within an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-software-updates-overviews-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 30.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'.
        - sortKey (string): Specify key to order the list of networks.
        - configSource (string): Limit the list of networks to those that contain devices with the specified config source
        - networkIds (array): Limit the list of networks to those that match the provided network IDs
        - networkGroupIds (array): Limit the list of networks to those that belong to one of the provided network group IDs.
        - productTypes (array): Limit the list of product types included for each network
        - networkName (string): Limit the list of networks to those whose name contains the given search string.
        - versionIds (array): Limit the list of networks to those that are currently on one of the provided version IDs.
        - firmwareStatus (string): Limit the list of networks to those whose current firmware version has the specified end-of-support status.
        - firmwareType (string): Limit the list of networks to those whose current firmware version has the specified release type.
        - upgradeDependencyIds (array): Limit the list of networks to those that belong to one of the provided upgrade dependencies.
        - upgradeAvailable (boolean): Limit the list of networks by upgrade availability.
        - templateRole (string): Limit the list of networks by config template role: non-template only, templates only, or templates and bound networks.
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "sortKey" in kwargs:
            options = [
                "availability",
                "currentVersion",
                "firmwareStatus",
                "firmwareType",
                "lastUpgrade",
                "networkGroup",
                "networkName",
                "networkType",
                "scheduledTime",
                "scheduledUpgradeVersion",
                "upgradeDependency",
            ]
            assert kwargs["sortKey"] in options, (
                f'''"sortKey" cannot be "{kwargs["sortKey"]}", & must be set to one of: {options}'''
            )
        if "configSource" in kwargs:
            options = ["cloud", "local"]
            assert kwargs["configSource"] in options, (
                f'''"configSource" cannot be "{kwargs["configSource"]}", & must be set to one of: {options}'''
            )
        if "firmwareStatus" in kwargs:
            options = ["critical", "good", "warning"]
            assert kwargs["firmwareStatus"] in options, (
                f'''"firmwareStatus" cannot be "{kwargs["firmwareStatus"]}", & must be set to one of: {options}'''
            )
        if "firmwareType" in kwargs:
            options = ["beta", "candidate", "stable"]
            assert kwargs["firmwareType"] in options, (
                f'''"firmwareType" cannot be "{kwargs["firmwareType"]}", & must be set to one of: {options}'''
            )
        if "templateRole" in kwargs:
            options = ["bound-templates", "non-template", "templates"]
            assert kwargs["templateRole"] in options, (
                f'''"templateRole" cannot be "{kwargs["templateRole"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "software", "updates", "overviews", "byNetwork"],
            "operation": "getOrganizationDevicesSoftwareUpdatesOverviewsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/software/updates/overviews/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "sortKey",
            "configSource",
            "networkIds",
            "networkGroupIds",
            "productTypes",
            "networkName",
            "versionIds",
            "firmwareStatus",
            "firmwareType",
            "upgradeDependencyIds",
            "upgradeAvailable",
            "templateRole",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "networkGroupIds",
            "productTypes",
            "versionIds",
            "upgradeDependencyIds",
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
                    f"getOrganizationDevicesSoftwareUpdatesOverviewsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesSoftwareVersions(self, organizationId: str, releaseType: str, **kwargs):
        """
        **List the available software upgrade versions for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-software-versions

        - organizationId (string): Organization ID
        - releaseType (string): Filter by release type
        """

        kwargs = locals()

        if "releaseType" in kwargs:
            options = ["beta", "generallyAvailable", "recommended"]
            assert kwargs["releaseType"] in options, (
                f'''"releaseType" cannot be "{kwargs["releaseType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "devices", "software", "versions"],
            "operation": "getOrganizationDevicesSoftwareVersions",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/software/versions"

        query_params = [
            "releaseType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationDevicesSoftwareVersions: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationDevicesSoftwareVersionsChangelogs(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Provide changelogs for specified versions or, if unspecified, for all versions in the organization, including reference to the last and next versions.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-software-versions-changelogs

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - versionIds (array): Array of version IDs for filtering
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 30.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "software", "versions", "changelogs"],
            "operation": "getOrganizationDevicesSoftwareVersionsChangelogs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/software/versions/changelogs"

        query_params = [
            "versionIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "versionIds",
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
                    f"getOrganizationDevicesSoftwareVersionsChangelogs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesStatuses(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the status of every Meraki device in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter devices by network ids.
        - serials (array): Optional parameter to filter devices by serials.
        - statuses (array): Optional parameter to filter devices by statuses. Valid statuses are ["online", "alerting", "offline", "dormant"].
        - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        - models (array): Optional parameter to filter devices by models.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - configurationUpdatedAfter (string): Optional parameter to filter results by whether or not the device's configuration has been updated after the given timestamp
        """

        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "statuses"],
            "operation": "getOrganizationDevicesStatuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "statuses",
            "productTypes",
            "models",
            "tags",
            "tagsFilterType",
            "configurationUpdatedAfter",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "statuses",
            "productTypes",
            "models",
            "tags",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationDevicesStatuses: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesStatusesOverview(self, organizationId: str, **kwargs):
        """
        **Return an overview of current device statuses**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses-overview

        - organizationId (string): Organization ID
        - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        - networkIds (array): An optional parameter to filter device statuses by network.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "statuses", "overview"],
            "operation": "getOrganizationDevicesStatusesOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/statuses/overview"

        query_params = [
            "productTypes",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "productTypes",
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
                    f"getOrganizationDevicesStatusesOverview: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationDevicesSyslogServersByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns syslog servers configured for the networks within an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-syslog-servers-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): IDs of the networks for which to fetch syslog servers; suggested maximum array size is 100
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "syslog", "servers", "byNetwork"],
            "operation": "getOrganizationDevicesSyslogServersByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/syslog/servers/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
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
                    f"getOrganizationDevicesSyslogServersByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesSyslogServersRolesByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns roles that can be assigned to a syslog server for a given network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-syslog-servers-roles-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): IDs of the networks for which to fetch valid syslog server roles; suggested maximum array size is 100
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "devices", "syslog", "servers", "roles", "byNetwork"],
            "operation": "getOrganizationDevicesSyslogServersRolesByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/syslog/servers/roles/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
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
                    f"getOrganizationDevicesSyslogServersRolesByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesSystemMemoryUsageHistoryByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Return the memory utilization history in kB for devices in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-system-memory-usage-history-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 1200, 3600, 14400. The default is 300. Interval is calculated if time params are provided.
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        - serials (array): Optional parameter to filter device availabilities history by device serial numbers
        - productTypes (array): Optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "system", "memory", "usage", "history", "byInterval"],
            "operation": "getOrganizationDevicesSystemMemoryUsageHistoryByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/system/memory/usage/history/byInterval"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
            "networkIds",
            "serials",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "productTypes",
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
                    f"getOrganizationDevicesSystemMemoryUsageHistoryByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesTopologyInterfaces(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List topology interfaces in an organization, including layer 2 and layer 3 metadata when available.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-topology-interfaces

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter interfaces by network ID. This filter uses multiple exact matches. Query array syntax follows the standard bracket form, for example: networkIds[]=L_1234&networkIds[]=L_5678.
        - serials (array): Optional parameter to filter interfaces by device serial. This filter uses multiple exact matches. Query array syntax follows the standard bracket form, for example: serials[]=Q234-ABCD-5678&serials[]=Q234-ABCD-9012.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "topology", "interfaces"],
            "operation": "getOrganizationDevicesTopologyInterfaces",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/topology/interfaces"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
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
                    f"getOrganizationDevicesTopologyInterfaces: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesTopologyL2Links(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List layer 2 topology links originating from devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-topology-l-2-links

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "topology", "l2", "links"],
            "operation": "getOrganizationDevicesTopologyL2Links",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/topology/l2/links"

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
                    f"getOrganizationDevicesTopologyL2Links: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesTopologyNodesDiscovered(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List topology nodes discovered by LLDP/CDP from devices in an organization, including reported metadata when available.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-topology-nodes-discovered

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "devices", "topology", "nodes", "discovered"],
            "operation": "getOrganizationDevicesTopologyNodesDiscovered",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/topology/nodes/discovered"

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
                    f"getOrganizationDevicesTopologyNodesDiscovered: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesUplinksAddressesByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the current uplink addresses for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-addresses-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "uplinks", "addresses", "byDevice"],
            "operation": "getOrganizationDevicesUplinksAddressesByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/uplinks/addresses/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "serials",
            "tags",
            "tagsFilterType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "serials",
            "tags",
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
                    f"getOrganizationDevicesUplinksAddressesByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesUplinksLossAndLatency(self, organizationId: str, **kwargs):
        """
        **Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
        - uplink (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, wan3, cellular. Default will return all uplinks.
        - ip (string): Optional filter for a specific destination IP. Default will return all destination IPs.
        """

        kwargs.update(locals())

        if "uplink" in kwargs:
            options = ["cellular", "wan1", "wan2", "wan3"]
            assert kwargs["uplink"] in options, (
                f'''"uplink" cannot be "{kwargs["uplink"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "devices", "uplinks", "uplinksLossAndLatency"],
            "operation": "getOrganizationDevicesUplinksLossAndLatency",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/devices/uplinksLossAndLatency"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "uplink",
            "ip",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationDevicesUplinksLossAndLatency: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationEarlyAccessFeatures(self, organizationId: str):
        """
        **List the available early access features for organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features"],
            "operation": "getOrganizationEarlyAccessFeatures",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features"

        return self._session.get(metadata, resource)

    def getOrganizationEarlyAccessFeaturesOptIns(self, organizationId: str):
        """
        **List the early access feature opt-ins for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-ins

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "getOrganizationEarlyAccessFeaturesOptIns",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns"

        return self._session.get(metadata, resource)

    def createOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, shortName: str, **kwargs):
        """
        **Create a new early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-early-access-features-opt-in

        - organizationId (string): Organization ID
        - shortName (string): Short name of the early access feature
        - limitScopeToNetworks (array): A list of network IDs to apply the opt-in to
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "createOrganizationEarlyAccessFeaturesOptIn",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns"

        body_params = [
            "shortName",
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationEarlyAccessFeaturesOptIn: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str):
        """
        **Show an early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-in

        - organizationId (string): Organization ID
        - optInId (string): Opt in ID
        """

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "getOrganizationEarlyAccessFeaturesOptIn",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        optInId = urllib.parse.quote(str(optInId), safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}"

        return self._session.get(metadata, resource)

    def updateOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str, **kwargs):
        """
        **Update an early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

        - organizationId (string): Organization ID
        - optInId (string): Opt in ID
        - limitScopeToNetworks (array): A list of network IDs to apply the opt-in to
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "updateOrganizationEarlyAccessFeaturesOptIn",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        optInId = urllib.parse.quote(str(optInId), safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}"

        body_params = [
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationEarlyAccessFeaturesOptIn: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str):
        """
        **Delete an early access feature opt-in**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-early-access-features-opt-in

        - organizationId (string): Organization ID
        - optInId (string): Opt in ID
        """

        metadata = {
            "tags": ["organizations", "configure", "earlyAccess", "features", "optIns"],
            "operation": "deleteOrganizationEarlyAccessFeaturesOptIn",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        optInId = urllib.parse.quote(str(optInId), safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}"

        return self._session.delete(metadata, resource)

    def updateOrganizationExtensionsSdwanmanagerInterconnect(
        self, organizationId: str, interconnectId: str, name: str, status: str, **kwargs
    ):
        """
        **Update name and status of an Interconnect**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-extensions-sdwanmanager-interconnect

        - organizationId (string): Organization ID
        - interconnectId (string): Interconnect ID
        - name (string): Interconnect name
        - status (string): Interconnect status
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "extensions", "sdwanmanager", "interconnects"],
            "operation": "updateOrganizationExtensionsSdwanmanagerInterconnect",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        interconnectId = urllib.parse.quote(str(interconnectId), safe="")
        resource = f"/organizations/{organizationId}/extensions/sdwanmanager/interconnects/{interconnectId}"

        body_params = [
            "name",
            "status",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationExtensionsSdwanmanagerInterconnect: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationExtensionsThousandEyesNetworks(self, organizationId: str):
        """
        **List the ThousandEyes agent configurations under this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-extensions-thousand-eyes-networks

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "networks"],
            "operation": "getOrganizationExtensionsThousandEyesNetworks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/networks"

        return self._session.get(metadata, resource)

    def createOrganizationExtensionsThousandEyesNetwork(self, organizationId: str, enabled: bool, networkId: str, **kwargs):
        """
        **Add a ThousandEyes agent for this network**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-extensions-thousand-eyes-network

        - organizationId (string): Organization ID
        - enabled (boolean): Whether or not the ThousandEyes agent is enabled for the network.
        - networkId (string): Network that will have the ThousandEyes agent installed on.
        - tests (array): An array of tests to be created
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "networks"],
            "operation": "createOrganizationExtensionsThousandEyesNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/networks"

        body_params = [
            "enabled",
            "networkId",
            "tests",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationExtensionsThousandEyesNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationExtensionsThousandEyesNetworksSupported(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List all the networks eligible for ThousandEyes agent activation under this organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-extensions-thousand-eyes-networks-supported

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - agentInstalled (boolean): Set to true to get only networks with installed ThousandEyes agent; set to false to get networks without agents.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "networks", "supported"],
            "operation": "getOrganizationExtensionsThousandEyesNetworksSupported",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/networks/supported"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "agentInstalled",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationExtensionsThousandEyesNetworksSupported: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationExtensionsThousandEyesNetwork(self, organizationId: str, networkId: str):
        """
        **List the ThousandEyes agent configuration under this network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-extensions-thousand-eyes-network

        - organizationId (string): Organization ID
        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "networks"],
            "operation": "getOrganizationExtensionsThousandEyesNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/networks/{networkId}"

        return self._session.get(metadata, resource)

    def updateOrganizationExtensionsThousandEyesNetwork(self, organizationId: str, networkId: str, enabled: bool, **kwargs):
        """
        **Update a ThousandEyes agent from this network**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-extensions-thousand-eyes-network

        - organizationId (string): Organization ID
        - networkId (string): Network ID
        - enabled (boolean): Whether or not the ThousandEyes agent is enabled for the network.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "networks"],
            "operation": "updateOrganizationExtensionsThousandEyesNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/networks/{networkId}"

        body_params = [
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationExtensionsThousandEyesNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationExtensionsThousandEyesNetwork(self, organizationId: str, networkId: str):
        """
        **Delete a ThousandEyes agent from this network**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-extensions-thousand-eyes-network

        - organizationId (string): Organization ID
        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "networks"],
            "operation": "deleteOrganizationExtensionsThousandEyesNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/networks/{networkId}"

        return self._session.delete(metadata, resource)

    def createOrganizationExtensionsThousandEyesTest(self, organizationId: str, **kwargs):
        """
        **Create a ThousandEyes test based on a provided test template**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-extensions-thousand-eyes-test

        - organizationId (string): Organization ID
        - tests (array): An array of tests to be created
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "extensions", "thousandEyes", "tests"],
            "operation": "createOrganizationExtensionsThousandEyesTest",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/extensions/thousandEyes/tests"

        body_params = [
            "tests",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationExtensionsThousandEyesTest: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationFirmwareUpgrades(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get firmware upgrade information for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - status (array): Optional parameter to filter the upgrade by status.
        - productTypes (array): Optional parameter to filter the upgrade by product type.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "firmware", "upgrades"],
            "operation": "getOrganizationFirmwareUpgrades",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/firmware/upgrades"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "status",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "status",
            "productTypes",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationFirmwareUpgrades: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationFirmwareUpgradesByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get firmware upgrade status for the filtered devices**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter by network
        - serials (array): Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
        - macs (array): Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
        - firmwareUpgradeBatchIds (array): Optional parameter to filter by firmware upgrade batch ids.
        - upgradeStatuses (array): Optional parameter to filter by firmware upgrade statuses.
        - currentUpgradesOnly (boolean): Optional parameter to filter to only current or pending upgrade statuses.
        - limitPerDevice (integer): Optional parameter to limit the number of upgrade statuses returned per device. If omitted, a value of 5 is used.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "firmware", "upgrades", "byDevice"],
            "operation": "getOrganizationFirmwareUpgradesByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/firmware/upgrades/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "macs",
            "firmwareUpgradeBatchIds",
            "upgradeStatuses",
            "currentUpgradesOnly",
            "limitPerDevice",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "macs",
            "firmwareUpgradeBatchIds",
            "upgradeStatuses",
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
                    f"getOrganizationFirmwareUpgradesByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationFloorPlansAutoLocateDevices(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List auto locate details for each device in your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-floor-plans-auto-locate-devices

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter devices by one or more network IDs
        - floorPlanIds (array): Optional parameter to filter devices by one or more floorplan IDs
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "floorPlans", "autoLocate", "devices"],
            "operation": "getOrganizationFloorPlansAutoLocateDevices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/floorPlans/autoLocate/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "floorPlanIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "floorPlanIds",
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
                    f"getOrganizationFloorPlansAutoLocateDevices: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationFloorPlansAutoLocateStatuses(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the status of auto locate for each floorplan in your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-floor-plans-auto-locate-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter floorplans by one or more network IDs
        - floorPlanIds (array): Optional parameter to filter floorplans by one or more floorplan IDs
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "floorPlans", "autoLocate", "statuses"],
            "operation": "getOrganizationFloorPlansAutoLocateStatuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/floorPlans/autoLocate/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "floorPlanIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "floorPlanIds",
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
                    f"getOrganizationFloorPlansAutoLocateStatuses: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAccessGroups(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List effective Catalyst Center access groups for the requested Catalyst Center administrators in the specified organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-access-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): Number of access groups to return per page. Range: 1-50. Defaults to 50 when omitted.
        - startingAfter (string): Cursor token to retrieve access groups after the specified access group identifier.
        - endingBefore (string): Cursor token to retrieve access groups before the specified access group identifier.
        - assignedAdminEmails (array): Catalyst Center administrator email addresses used by federation to filter access groups for the requested administrators.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "iam", "admins", "accessGroups"],
            "operation": "getOrganizationAccessGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/admins/accessGroups"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "assignedAdminEmails",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "assignedAdminEmails",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationAccessGroups: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def resolveOrganizationIamAdminsAdministratorsMePermissions(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the authenticated caller admin's permissions for an organization**
        https://developer.cisco.com/meraki/api-v1/#!resolve-organization-iam-admins-administrators-me-permissions

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "iam", "admins", "administrators", "me", "permissions"],
            "operation": "resolveOrganizationIamAdminsAdministratorsMePermissions",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/iam/admins/administrators/me/permissions/resolve"

        body_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"resolveOrganizationIamAdminsAdministratorsMePermissions: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationIntegrationsDeployable(self, organizationId: str):
        """
        **Provides a list of integrations that can be enabled for an Organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-integrations-deployable

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "integrations", "deployable"],
            "operation": "getOrganizationIntegrationsDeployable",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/integrations/deployable"

        return self._session.get(metadata, resource)

    def getOrganizationIntegrationsDeployed(self, organizationId: str):
        """
        **Provides a list of integrations enabled for an Organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-integrations-deployed

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "integrations", "deployed"],
            "operation": "getOrganizationIntegrationsDeployed",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/integrations/deployed"

        return self._session.get(metadata, resource)

    def getOrganizationIntegrationsXdrNetworks(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns the networks in the organization that have XDR enabled**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-integrations-xdr-networks

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter the results by network IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "getOrganizationIntegrationsXdrNetworks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/integrations/xdr/networks"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
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
                    f"getOrganizationIntegrationsXdrNetworks: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def disableOrganizationIntegrationsXdrNetworks(self, organizationId: str, networks: list, **kwargs):
        """
        **Disable XDR on networks**
        https://developer.cisco.com/meraki/api-v1/#!disable-organization-integrations-xdr-networks

        - organizationId (string): Organization ID
        - networks (array): List containing the network ID and the product type to disable XDR on
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "disableOrganizationIntegrationsXdrNetworks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/integrations/xdr/networks/disable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"disableOrganizationIntegrationsXdrNetworks: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def enableOrganizationIntegrationsXdrNetworks(self, organizationId: str, networks: list, **kwargs):
        """
        **Enable XDR on networks**
        https://developer.cisco.com/meraki/api-v1/#!enable-organization-integrations-xdr-networks

        - organizationId (string): Organization ID
        - networks (array): List containing the network ID and the product type to enable XDR on
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "integrations", "xdr", "networks"],
            "operation": "enableOrganizationIntegrationsXdrNetworks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/integrations/xdr/networks/enable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"enableOrganizationIntegrationsXdrNetworks: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def claimIntoOrganizationInventory(self, organizationId: str, **kwargs):
        """
        **Claim a list of devices, licenses, and/or orders into an organization inventory**
        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization-inventory

        - organizationId (string): Organization ID
        - orders (array): The numbers of the orders that should be claimed
        - serials (array): The serials of the devices that should be claimed
        - licenses (array): The licenses that should be claimed
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory"],
            "operation": "claimIntoOrganizationInventory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/claim"

        body_params = [
            "orders",
            "serials",
            "licenses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"claimIntoOrganizationInventory: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationInventoryDevices(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return the device inventory for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - usedState (string): Filter results by used or unused inventory. Accepted values are 'used' or 'unused'.
        - search (string): Search for devices in inventory based on serial number, mac address, or model.
        - macs (array): Search for devices in inventory based on mac addresses.
        - networkIds (array): Search for devices in inventory based on network ids. Use explicit 'null' value to get available devices only.
        - serials (array): Search for devices in inventory based on serials.
        - models (array): Search for devices in inventory based on model.
        - orderNumbers (array): Search for devices in inventory based on order numbers.
        - tags (array): Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'.
        - productTypes (array): Filter devices by product type. Accepted values are appliance, camera, campusGateway, cellularGateway, secureConnect, sensor, switch, systemsManager, wireless, and wirelessController.
        - eoxStatuses (array): Filter devices by EoX status. Accepted values are 'endOfSale', 'endOfSupport', 'nearEndOfSupport', or 'null'. Use 'null' to filter for devices with no EOX data. Supports multiple values for multi-select filtering.
        """

        kwargs.update(locals())

        if "usedState" in kwargs:
            options = ["unused", "used"]
            assert kwargs["usedState"] in options, (
                f'''"usedState" cannot be "{kwargs["usedState"]}", & must be set to one of: {options}'''
            )
        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices"],
            "operation": "getOrganizationInventoryDevices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "usedState",
            "search",
            "macs",
            "networkIds",
            "serials",
            "models",
            "orderNumbers",
            "tags",
            "tagsFilterType",
            "productTypes",
            "eoxStatuses",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "macs",
            "networkIds",
            "serials",
            "models",
            "orderNumbers",
            "tags",
            "productTypes",
            "eoxStatuses",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationInventoryDevices: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationInventoryDevicesDetails(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return inventory devices with additional site, geolocation, software, licensing, lifecycle, and Catalyst Center-specific fields**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices-details

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter devices by network IDs. Matches devices in any of the provided network IDs. When multiple filter parameters are provided, a device must match each provided filter. Query array syntax follows the standard bracket form, for example: networkIds[]=L_1234&networkIds[]=L_5678. Maximum 100 network IDs.
        - serials (array): Optional parameter to filter devices by serials. Matches devices with any of the provided serials. When multiple filter parameters are provided, a device must match each provided filter. Query array syntax follows the standard bracket form, for example: serials[]=Q234-ABCD-5678&serials[]=Q234-ABCD-9012. Maximum 100 serials.
        - productTypes (array): Optional parameter to filter devices by product type. Matches devices with any of the provided product types. When multiple filter parameters are provided, a device must match each provided filter. Query array syntax follows the standard bracket form, for example: productTypes[]=switch&productTypes[]=wireless. Maximum 100 product types.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "inventory", "devices", "details"],
            "operation": "getOrganizationInventoryDevicesDetails",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/devices/details"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "productTypes",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "productTypes",
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
                    f"getOrganizationInventoryDevicesDetails: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationInventoryDevicesEoxOverview(self, organizationId: str):
        """
        **Fetch the EOX summary for an organization, including counts of devices that are end-of-sale, end-of-support, and end-of-support-soon.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices-eox-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices", "eox"],
            "operation": "getOrganizationInventoryDevicesEoxOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/devices/eox/overview"

        return self._session.get(metadata, resource)

    def createOrganizationInventoryDevicesSwapsBulk(self, organizationId: str, swaps: list, **kwargs):
        """
        **Swap the devices identified by devices.old with a devices.new, then perform the :afterAction on the devices.old.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-devices-swaps-bulk

        - organizationId (string): Organization ID
        - swaps (array): List of replacments to perform
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices", "swaps", "bulk"],
            "operation": "createOrganizationInventoryDevicesSwapsBulk",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/devices/swaps/bulk"

        body_params = [
            "swaps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationInventoryDevicesSwapsBulk: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationInventoryDevicesSwapsBulk(self, organizationId: str, id: str):
        """
        **List of device swaps for a given request ID ({id}).**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices-swaps-bulk

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices", "swaps", "bulk"],
            "operation": "getOrganizationInventoryDevicesSwapsBulk",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/inventory/devices/swaps/bulk/{id}"

        return self._session.get(metadata, resource)

    def getOrganizationInventoryDevice(self, organizationId: str, serial: str):
        """
        **Return a single device from the inventory of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

        - organizationId (string): Organization ID
        - serial (string): Serial
        """

        metadata = {
            "tags": ["organizations", "configure", "inventory", "devices"],
            "operation": "getOrganizationInventoryDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/organizations/{organizationId}/inventory/devices/{serial}"

        return self._session.get(metadata, resource)

    def claimOrganizationInventoryOrders(self, organizationId: str, claimId: str, **kwargs):
        """
        **Claim an order by the secure unique order claim number, the order claim id**
        https://developer.cisco.com/meraki/api-v1/#!claim-organization-inventory-orders

        - organizationId (string): Organization ID
        - claimId (string): The unique order claim id
        - subscriptions (array): The individual subscriptions to claim
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory", "orders"],
            "operation": "claimOrganizationInventoryOrders",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/orders/claim"

        body_params = [
            "claimId",
            "subscriptions",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"claimOrganizationInventoryOrders: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def previewOrganizationInventoryOrders(self, organizationId: str, claimId: str, **kwargs):
        """
        **Preview the results and status of an order claim by the secure order id**
        https://developer.cisco.com/meraki/api-v1/#!preview-organization-inventory-orders

        - organizationId (string): Organization ID
        - claimId (string): The unique order claim id
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "inventory", "orders"],
            "operation": "previewOrganizationInventoryOrders",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/orders/preview"

        body_params = [
            "claimId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"previewOrganizationInventoryOrders: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def releaseFromOrganizationInventory(self, organizationId: str, **kwargs):
        """
        **Release a list of claimed devices from an organization.**
        https://developer.cisco.com/meraki/api-v1/#!release-from-organization-inventory

        - organizationId (string): Organization ID
        - serials (array): Serials of the devices that should be released
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "inventory"],
            "operation": "releaseFromOrganizationInventory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/inventory/release"

        body_params = [
            "serials",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"releaseFromOrganizationInventory: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationLicenses(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the licenses for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - deviceSerial (string): Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
        - networkId (string): Filter the licenses to those assigned in a particular network
        - state (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'
        """

        kwargs.update(locals())

        if "state" in kwargs:
            options = ["active", "expired", "expiring", "recentlyQueued", "unused", "unusedActive"]
            assert kwargs["state"] in options, f'''"state" cannot be "{kwargs["state"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "getOrganizationLicenses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/licenses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "deviceSerial",
            "networkId",
            "state",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationLicenses: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def assignOrganizationLicensesSeats(self, organizationId: str, licenseId: str, networkId: str, seatCount: int, **kwargs):
        """
        **Assign SM seats to a network**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        - organizationId (string): Organization ID
        - licenseId (string): The ID of the SM license to assign seats from
        - networkId (string): The ID of the SM network to assign the seats to
        - seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "assignOrganizationLicensesSeats",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/licenses/assignSeats"

        body_params = [
            "licenseId",
            "networkId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"assignOrganizationLicensesSeats: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def moveOrganizationLicenses(self, organizationId: str, destOrganizationId: str, licenseIds: list, **kwargs):
        """
        **Move licenses to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        - organizationId (string): Organization ID
        - destOrganizationId (string): The ID of the organization to move the licenses to
        - licenseIds (array): A list of IDs of licenses to move to the new organization
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "moveOrganizationLicenses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/licenses/move"

        body_params = [
            "destOrganizationId",
            "licenseIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"moveOrganizationLicenses: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def moveOrganizationLicensesSeats(
        self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int, **kwargs
    ):
        """
        **Move SM seats to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        - organizationId (string): Organization ID
        - destOrganizationId (string): The ID of the organization to move the SM seats to
        - licenseId (string): The ID of the SM license to move the seats from
        - seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "moveOrganizationLicensesSeats",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/licenses/moveSeats"

        body_params = [
            "destOrganizationId",
            "licenseId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"moveOrganizationLicensesSeats: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationLicensesOverview(self, organizationId: str):
        """
        **Return an overview of the license state for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "monitor", "licenses", "overview"],
            "operation": "getOrganizationLicensesOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/licenses/overview"

        return self._session.get(metadata, resource)

    def renewOrganizationLicensesSeats(self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str, **kwargs):
        """
        **Renew SM seats of a license**
        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        - organizationId (string): Organization ID
        - licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
        - unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "renewOrganizationLicensesSeats",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/licenses/renewSeats"

        body_params = [
            "licenseIdToRenew",
            "unusedLicenseId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"renewOrganizationLicensesSeats: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationLicense(self, organizationId: str, licenseId: str):
        """
        **Display a license**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-license

        - organizationId (string): Organization ID
        - licenseId (string): License ID
        """

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "getOrganizationLicense",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        licenseId = urllib.parse.quote(str(licenseId), safe="")
        resource = f"/organizations/{organizationId}/licenses/{licenseId}"

        return self._session.get(metadata, resource)

    def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        - organizationId (string): Organization ID
        - licenseId (string): License ID
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to  null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "licenses"],
            "operation": "updateOrganizationLicense",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        licenseId = urllib.parse.quote(str(licenseId), safe="")
        resource = f"/organizations/{organizationId}/licenses/{licenseId}"

        body_params = [
            "deviceSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationLicense: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationLoginSecurity(self, organizationId: str):
        """
        **Returns the login security settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "loginSecurity"],
            "operation": "getOrganizationLoginSecurity",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/loginSecurity"

        return self._session.get(metadata, resource)

    def updateOrganizationLoginSecurity(self, organizationId: str, **kwargs):
        """
        **Update the login security settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        - organizationId (string): Organization ID
        - enforcePasswordExpiration (boolean): Boolean indicating whether users are forced to change their password every X number of days.
        - passwordExpirationDays (integer): Number of days after which users will be forced to change their password.
        - enforceDifferentPasswords (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
        - numDifferentPasswords (integer): Number of recent passwords that new password must be distinct from.
        - enforceStrongPasswords (boolean): Deprecated. Values of 'false' are always ignored.
        - minimumPasswordLength (integer): Minimum number of characters required in admins' passwords.
        - enforceAccountLockout (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
        - accountLockoutAttempts (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
        - enforceIdleTimeout (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
        - idleTimeoutMinutes (integer): Number of minutes users can remain idle before being logged out of their accounts.
        - enforceTwoFactorAuth (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the authenticator application.
        - enforceLoginIpRanges (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
        - loginIpRanges (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
        - enforceLockedIpSessions (boolean): Boolean indicating whether Dashboard sessions are locked to the IP address from which they were established. Only applicable to organizations that support locked-IP sessions; otherwise the parameter is ignored.
        - apiAuthentication (object): Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "loginSecurity"],
            "operation": "updateOrganizationLoginSecurity",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/loginSecurity"

        body_params = [
            "enforcePasswordExpiration",
            "passwordExpirationDays",
            "enforceDifferentPasswords",
            "numDifferentPasswords",
            "enforceStrongPasswords",
            "minimumPasswordLength",
            "enforceAccountLockout",
            "accountLockoutAttempts",
            "enforceIdleTimeout",
            "idleTimeoutMinutes",
            "enforceTwoFactorAuth",
            "enforceLoginIpRanges",
            "loginIpRanges",
            "enforceLockedIpSessions",
            "apiAuthentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationLoginSecurity: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationNetworks(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the networks that the user has privileges on in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - configTemplateId (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template.
        - isBoundToConfigTemplate (boolean): An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
        - tags (array): An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - productTypes (array): An optional parameter to filter networks by product type. Results will have at least one of the included product types.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "tagsFilterType" in kwargs:
            options = ["withAllTags", "withAnyTags"]
            assert kwargs["tagsFilterType"] in options, (
                f'''"tagsFilterType" cannot be "{kwargs["tagsFilterType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "getOrganizationNetworks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks"

        query_params = [
            "configTemplateId",
            "isBoundToConfigTemplate",
            "tags",
            "tagsFilterType",
            "productTypes",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "tags",
            "productTypes",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationNetworks: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationNetwork(self, organizationId: str, name: str, productTypes: list, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        - organizationId (string): Organization ID
        - name (string): The name of the new network
        - productTypes (array): The product type(s) of the new network. If more than one type is included, the network will be a combined network.
        - tags (array): A list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        - notes (string): Add any notes or additional information about this network here.
        - details (array): An array of details
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "createOrganizationNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks"

        body_params = [
            "name",
            "productTypes",
            "tags",
            "timeZone",
            "copyFromNetworkId",
            "notes",
            "details",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationNetwork: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def combineOrganizationNetworks(self, organizationId: str, name: str, networkIds: list, **kwargs):
        """
        **Combine multiple networks into a single network**
        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        - organizationId (string): Organization ID
        - name (string): The name of the combined network
        - networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "combineOrganizationNetworks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks/combine"

        body_params = [
            "name",
            "networkIds",
            "enrollmentString",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"combineOrganizationNetworks: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationNetworksGroups(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the network groups in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - groupIds (array): Optional parameter to filter network groups by ID
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks", "groups"],
            "operation": "getOrganizationNetworksGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups"

        query_params = [
            "groupIds",
            "perPage",
            "startingAfter",
            "endingBefore",
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
                self._session._logger.warning(f"getOrganizationNetworksGroups: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationNetworksGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Create a network group**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-networks-group

        - organizationId (string): Organization ID
        - name (string): The name of the network group
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "networks", "groups"],
            "operation": "createOrganizationNetworksGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationNetworksGroup: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationNetworksGroupsOverviewByGroup(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the client and status overview information for the network groups in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks-groups-overview-by-group

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - sortBy (string): Field by which to sort the results
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["status"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "networks", "groups", "overview", "byGroup"],
            "operation": "getOrganizationNetworksGroupsOverviewByGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups/overview/byGroup"

        query_params = [
            "sortBy",
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
                    f"getOrganizationNetworksGroupsOverviewByGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateOrganizationNetworksGroup(self, organizationId: str, groupId: str, name: str, **kwargs):
        """
        **Update a network group**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-networks-group

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        - name (string): The new name of the network group
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "networks", "groups"],
            "operation": "updateOrganizationNetworksGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups/{groupId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationNetworksGroup: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationNetworksGroup(self, organizationId: str, groupId: str):
        """
        **Delete a network group**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-networks-group

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        """

        metadata = {
            "tags": ["organizations", "configure", "networks", "groups"],
            "operation": "deleteOrganizationNetworksGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups/{groupId}"

        return self._session.delete(metadata, resource)

    def bulkOrganizationNetworksGroupAssign(self, organizationId: str, groupId: str, networkIds: list, **kwargs):
        """
        **Add networks to a network group**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-networks-group-assign

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        - networkIds (array): A list of network IDs to add to the network group
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "networks", "groups"],
            "operation": "bulkOrganizationNetworksGroupAssign",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups/{groupId}/bulkAssign"

        body_params = [
            "networkIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"bulkOrganizationNetworksGroupAssign: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def bulkOrganizationNetworksGroupUnassign(self, organizationId: str, groupId: str, networkIds: list, **kwargs):
        """
        **Remove networks from a network group**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-networks-group-unassign

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        - networkIds (array): A list of network IDs to remove from the network group
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "networks", "groups"],
            "operation": "bulkOrganizationNetworksGroupUnassign",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        groupId = urllib.parse.quote(str(groupId), safe="")
        resource = f"/organizations/{organizationId}/networks/groups/{groupId}/bulkUnassign"

        body_params = [
            "networkIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"bulkOrganizationNetworksGroupUnassign: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def createNetworkMove(self, organizationId: str, network: dict, organizations: dict, **kwargs):
        """
        **Move networks from one organization to another**
        https://developer.cisco.com/meraki/api-v1/#!create-network-move

        - organizationId (string): Organization ID
        - network (object): Network to be moved
        - organizations (object): Organizations involved in the network move
        - simulate (boolean): If true, simulates the network move and validates the operation without committing changes. The network will remain in the source organization.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks"],
            "operation": "createNetworkMove",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks/moves"

        body_params = [
            "network",
            "organizations",
            "simulate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkMove: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getNetworkMoves(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return a list of network move operations in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-network-moves

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - moveIds (array): Array of network move operation IDs to include. If not specified, all network moves will be returned.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "networks", "moves"],
            "operation": "getNetworkMoves",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/networks/moves"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "moveIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "moveIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkMoves: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationOpenRoamingCertificate(self, organizationId: str, id: str):
        """
        **Delete an open roaming certificate.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-open-roaming-certificate

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "openRoaming", "certificates"],
            "operation": "deleteOrganizationOpenRoamingCertificate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/openRoaming/certificates/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationOpenapiSpec(self, organizationId: str, **kwargs):
        """
        **Return the OpenAPI Specification of the organization's API documentation in JSON**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

        - organizationId (string): Organization ID
        - version (integer): OpenAPI Specification version to return. Default is 2
        """

        kwargs.update(locals())

        if "version" in kwargs:
            options = [2, 3]
            assert kwargs["version"] in options, (
                f'''"version" cannot be "{kwargs["version"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "openapiSpec"],
            "operation": "getOrganizationOpenapiSpec",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/openapiSpec"

        query_params = [
            "version",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationOpenapiSpec: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationPoliciesAssignmentsByClient(
        self, organizationId: str, networkIds: list, total_pages=1, direction="next", **kwargs
    ):
        """
        **Get policies for all clients with policies**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-assignments-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Network Ids (minimum: 1, maximum: 30)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - includeUndetectedClients (boolean): Include provisioned clients that have not associated to the network. Default: false
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "assignments", "byClient"],
            "operation": "getOrganizationPoliciesAssignmentsByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/assignments/byClient"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "timespan",
            "includeUndetectedClients",
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
                    f"getOrganizationPoliciesAssignmentsByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationPoliciesGlobalFirewallApplicationCategories(self, organizationId: str):
        """
        **List application categories with their associated applications**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-global-firewall-application-categories

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "applicationCategories"],
            "operation": "getOrganizationPoliciesGlobalFirewallApplicationCategories",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/applicationCategories"

        return self._session.get(metadata, resource)

    def getOrganizationPoliciesGlobalFirewallRulesets(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List Organization-Wide Policy Firewall Rulesets**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-global-firewall-rulesets

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - rulesetIds (array): Filter rulesets by IDs
        - name (string): Filter rulesets by name (partial match, case-insensitive). If multiple instances are provided, only the last one is used.
        - excludedPolicyIds (array): Filter out rulesets that are associated with the specified policy IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets"],
            "operation": "getOrganizationPoliciesGlobalFirewallRulesets",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets"

        query_params = [
            "rulesetIds",
            "name",
            "excludedPolicyIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "rulesetIds",
            "excludedPolicyIds",
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
                    f"getOrganizationPoliciesGlobalFirewallRulesets: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationPoliciesGlobalFirewallRuleset(self, organizationId: str, name: str, **kwargs):
        """
        **Create an Organization-Wide Policy Firewall Ruleset**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-firewall-ruleset

        - organizationId (string): Organization ID
        - name (string): Name of the firewall ruleset
        - description (string): Description of the firewall ruleset
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets"],
            "operation": "createOrganizationPoliciesGlobalFirewallRuleset",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationPoliciesGlobalFirewallRuleset: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def createOrganizationPoliciesGlobalFirewallRulesetsRule(
        self, organizationId: str, name: str, rulesetId: str, policy: str, sources: dict, destinations: dict, **kwargs
    ):
        """
        **Create an Organization-Wide Policy Firewall Rule**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-firewall-rulesets-rule

        - organizationId (string): Organization ID
        - name (string): Name of the firewall rule
        - rulesetId (string): Firewall ruleset ID to associate the rule with
        - policy (string): Rule policy - allow or deny traffic
        - sources (object): Source traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        - destinations (object): Destination traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        - enabled (boolean): Whether the rule is enabled
        - priority (integer): Rule priority (lower numbers = higher priority)
        - description (string): Description of the firewall rule
        """

        kwargs.update(locals())

        if "policy" in kwargs:
            options = ["allow", "deny"]
            assert kwargs["policy"] in options, (
                f'''"policy" cannot be "{kwargs["policy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets", "rules"],
            "operation": "createOrganizationPoliciesGlobalFirewallRulesetsRule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules"

        body_params = [
            "name",
            "rulesetId",
            "policy",
            "enabled",
            "priority",
            "description",
            "sources",
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationPoliciesGlobalFirewallRulesetsRule: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationPoliciesGlobalFirewallRulesetsRules(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List Organization-Wide Policy Firewall Rules**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-global-firewall-rulesets-rules

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - rulesetIds (array): Filter rules by firewall ruleset IDs
        - ruleIds (array): Filter rules by rule IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets", "rules"],
            "operation": "getOrganizationPoliciesGlobalFirewallRulesetsRules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules"

        query_params = [
            "rulesetIds",
            "ruleIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "rulesetIds",
            "ruleIds",
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
                    f"getOrganizationPoliciesGlobalFirewallRulesetsRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationPoliciesGlobalFirewallRulesetsRule(self, organizationId: str, ruleId: str):
        """
        **Delete an Organization-Wide Policy Firewall Rule**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-firewall-rulesets-rule

        - organizationId (string): Organization ID
        - ruleId (string): Rule ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets", "rules"],
            "operation": "deleteOrganizationPoliciesGlobalFirewallRulesetsRule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules/{ruleId}"

        return self._session.delete(metadata, resource)

    def updateOrganizationPoliciesGlobalFirewallRulesetsRule(self, organizationId: str, ruleId: str, **kwargs):
        """
        **Update an Organization-Wide Policy Firewall Rule**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-firewall-rulesets-rule

        - organizationId (string): Organization ID
        - ruleId (string): Rule ID
        - name (string): Name of the firewall rule
        - rulesetId (string): Firewall ruleset ID to associate the rule with
        - policy (string): Rule policy - allow or deny traffic
        - enabled (boolean): Whether the rule is enabled
        - priority (integer): Rule priority (lower numbers = higher priority)
        - description (string): Description of the firewall rule
        - sources (object): Source traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        - destinations (object): Destination traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        """

        kwargs.update(locals())

        if "policy" in kwargs:
            options = ["allow", "deny"]
            assert kwargs["policy"] in options, (
                f'''"policy" cannot be "{kwargs["policy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets", "rules"],
            "operation": "updateOrganizationPoliciesGlobalFirewallRulesetsRule",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules/{ruleId}"

        body_params = [
            "name",
            "rulesetId",
            "policy",
            "enabled",
            "priority",
            "description",
            "sources",
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationPoliciesGlobalFirewallRulesetsRule: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def updateOrganizationPoliciesGlobalFirewallRuleset(self, organizationId: str, rulesetId: str, **kwargs):
        """
        **Update an Organization-Wide Policy Firewall Ruleset**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-firewall-ruleset

        - organizationId (string): Organization ID
        - rulesetId (string): Ruleset ID
        - name (string): Name of the firewall ruleset
        - description (string): Description of the firewall ruleset
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets"],
            "operation": "updateOrganizationPoliciesGlobalFirewallRuleset",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        rulesetId = urllib.parse.quote(str(rulesetId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/{rulesetId}"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationPoliciesGlobalFirewallRuleset: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationPoliciesGlobalFirewallRuleset(self, organizationId: str, rulesetId: str):
        """
        **Delete an Organization-Wide Policy Firewall Ruleset**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-firewall-ruleset

        - organizationId (string): Organization ID
        - rulesetId (string): Ruleset ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "firewall", "rulesets"],
            "operation": "deleteOrganizationPoliciesGlobalFirewallRuleset",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        rulesetId = urllib.parse.quote(str(rulesetId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/{rulesetId}"

        return self._session.delete(metadata, resource)

    def getOrganizationPoliciesGlobalGroupPolicies(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List Organization-Wide Policies**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-global-group-policies

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - name (string): Filter policies by name (partial match, case-insensitive). If multiple instances are provided, only the last one is used.
        - policyIds (array): Filter policies by IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group"],
            "operation": "getOrganizationPoliciesGlobalGroupPolicies",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies"

        query_params = [
            "name",
            "policyIds",
            "perPage",
            "startingAfter",
            "endingBefore",
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
                    f"getOrganizationPoliciesGlobalGroupPolicies: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationPoliciesGlobalGroupPolicy(self, organizationId: str, name: str, **kwargs):
        """
        **Create an Organization-Wide Policy**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-group-policy

        - organizationId (string): Organization ID
        - name (string): Name of the policy
        - description (string): Description of the policy
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group"],
            "operation": "createOrganizationPoliciesGlobalGroupPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationPoliciesGlobalGroupPolicy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def assignOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups(
        self, organizationId: str, policy: dict, adaptivePolicyGroups: list, **kwargs
    ):
        """
        **Assign adaptive policy groups to a policy**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-policies-global-group-policies-adaptive-policy-groups

        - organizationId (string): Organization ID
        - policy (object): Policy to assign adaptive policy groups to
        - adaptivePolicyGroups (array): Adaptive policy groups to assign
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "adaptivePolicyGroups"],
            "operation": "assignOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/adaptivePolicyGroups/assign"

        body_params = [
            "policy",
            "adaptivePolicyGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"assignOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroupsAssignments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List adaptive policy group assignments**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-global-group-policies-adaptive-policy-groups-assignments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - assignmentIds (array): Filter assignments by assignment IDs
        - policyIds (array): Filter assignments by policy IDs
        - adaptivePolicyGroupIds (array): Filter assignments by adaptive policy group IDs
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "adaptivePolicyGroups", "assignments"],
            "operation": "getOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroupsAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/adaptivePolicyGroups/assignments"

        query_params = [
            "assignmentIds",
            "policyIds",
            "adaptivePolicyGroupIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "assignmentIds",
            "policyIds",
            "adaptivePolicyGroupIds",
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
                    f"getOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroupsAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def removeOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups(
        self, organizationId: str, policy: dict, adaptivePolicyGroups: list, **kwargs
    ):
        """
        **Remove adaptive policy groups from a policy**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-policies-global-group-policies-adaptive-policy-groups

        - organizationId (string): Organization ID
        - policy (object): Policy to remove adaptive policy groups from
        - adaptivePolicyGroups (array): Adaptive policy groups to remove
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "adaptivePolicyGroups"],
            "operation": "removeOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/adaptivePolicyGroups/remove"

        body_params = [
            "policy",
            "adaptivePolicyGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"removeOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List Organization-Wide Policy Ruleset Assignments**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policies-global-group-policies-firewall-rulesets-assignments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - rulesetIds (array): Filter assignments by ruleset IDs
        - policyIds (array): Filter assignments by policy IDs
        - assignmentIds (array): Filter assignments by assignment IDs
        - staged (boolean): Filter assignments by whether or not they are staged
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "firewall", "rulesets", "assignments"],
            "operation": "getOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments"

        query_params = [
            "rulesetIds",
            "policyIds",
            "assignmentIds",
            "staged",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "rulesetIds",
            "policyIds",
            "assignmentIds",
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
                    f"getOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment(
        self, organizationId: str, rulesetId: str, policyId: str, **kwargs
    ):
        """
        **Create an Organization-Wide Policy Ruleset Assignment**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-group-policies-firewall-rulesets-assignment

        - organizationId (string): Organization ID
        - rulesetId (string): ID of the ruleset to assign
        - policyId (string): ID of the policy to assign the ruleset to
        - priority (integer): Priority of the ruleset assignment (lower numbers = higher priority)
        - staged (boolean): Stage an assignment without applying it immediately to the policy
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "firewall", "rulesets", "assignments"],
            "operation": "createOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments"

        body_params = [
            "rulesetId",
            "policyId",
            "priority",
            "staged",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def commitOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignments(
        self, organizationId: str, policy: dict, **kwargs
    ):
        """
        **Commit staged Organization-Wide Policy Ruleset Assignments**
        https://developer.cisco.com/meraki/api-v1/#!commit-organization-policies-global-group-policies-firewall-rulesets-assignments

        - organizationId (string): Organization ID
        - policy (object): Policy in which all staged rulesets will be committed
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "firewall", "rulesets", "assignments"],
            "operation": "commitOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/commit"

        body_params = [
            "policy",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"commitOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment(
        self, organizationId: str, assignmentId: str, **kwargs
    ):
        """
        **Update an Organization-Wide Policy Ruleset Assignment**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-group-policies-firewall-rulesets-assignment

        - organizationId (string): Organization ID
        - assignmentId (string): Assignment ID
        - rulesetId (string): ID of the ruleset to assign
        - policyId (string): ID of the policy to assign the ruleset to
        - priority (integer): Priority of the ruleset assignment (lower numbers = higher priority)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "firewall", "rulesets", "assignments"],
            "operation": "updateOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        assignmentId = urllib.parse.quote(str(assignmentId), safe="")
        resource = (
            f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/{assignmentId}"
        )

        body_params = [
            "rulesetId",
            "policyId",
            "priority",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment(self, organizationId: str, assignmentId: str):
        """
        **Delete an Organization-Wide Policy Ruleset Assignment**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-group-policies-firewall-rulesets-assignment

        - organizationId (string): Organization ID
        - assignmentId (string): Assignment ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group", "firewall", "rulesets", "assignments"],
            "operation": "deleteOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        assignmentId = urllib.parse.quote(str(assignmentId), safe="")
        resource = (
            f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/{assignmentId}"
        )

        return self._session.delete(metadata, resource)

    def updateOrganizationPoliciesGlobalGroupPolicy(self, organizationId: str, policyId: str, **kwargs):
        """
        **Update an Organization-Wide Policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-group-policy

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        - name (string): Name of the policy
        - description (string): Description of the policy
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group"],
            "operation": "updateOrganizationPoliciesGlobalGroupPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyId = urllib.parse.quote(str(policyId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/{policyId}"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationPoliciesGlobalGroupPolicy: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationPoliciesGlobalGroupPolicy(self, organizationId: str, policyId: str):
        """
        **Delete an Organization-Wide Policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-group-policy

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policies", "global", "group"],
            "operation": "deleteOrganizationPoliciesGlobalGroupPolicy",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyId = urllib.parse.quote(str(policyId), safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/{policyId}"

        return self._session.delete(metadata, resource)

    def getOrganizationPolicyObjects(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Lists Policy Objects belonging to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "getOrganizationPolicyObjects",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects"

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
                self._session._logger.warning(f"getOrganizationPolicyObjects: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationPolicyObject(self, organizationId: str, name: str, category: str, type: str, **kwargs):
        """
        **Creates a new Policy Object**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

        - organizationId (string): Organization ID
        - name (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - category (string): Category of a policy object (one of: adaptivePolicy, network)
        - type (string): Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn). DEPRECATED: `ipAndMask` is deprecated and will be removed in a future release. Use `cidr` instead.
        - cidr (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
        - fqdn (string): Fully qualified domain name of policy object (e.g. "example.com")
        - mask (string): Mask of a policy object (e.g. "255.255.0.0"). Used only with deprecated `type=ipAndMask`.
        - ip (string): IP Address of a policy object (e.g. "1.2.3.4"). Used only with deprecated `type=ipAndMask`.
        - groupIds (array): The IDs of policy object groups the policy object belongs to
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["adaptivePolicyIpv4Cidr", "cidr", "fqdn"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "createOrganizationPolicyObject",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects"

        body_params = [
            "name",
            "category",
            "type",
            "cidr",
            "fqdn",
            "mask",
            "ip",
            "groupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationPolicyObject: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationPolicyObjectsGroups(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Lists Policy Object Groups belonging to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "getOrganizationPolicyObjectsGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups"

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
                self._session._logger.warning(f"getOrganizationPolicyObjectsGroups: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationPolicyObjectsGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Creates a new Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

        - organizationId (string): Organization ID
        - name (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - category (string): Category of a policy object group (one of: NetworkObjectGroup, GeoLocationGroup, PortObjectGroup, ApplicationGroup)
        - objectIds (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "createOrganizationPolicyObjectsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups"

        body_params = [
            "name",
            "category",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationPolicyObjectsGroup: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str):
        """
        **Shows details of a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-group

        - organizationId (string): Organization ID
        - policyObjectGroupId (string): Policy object group ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "getOrganizationPolicyObjectsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyObjectGroupId = urllib.parse.quote(str(policyObjectGroupId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        return self._session.get(metadata, resource)

    def updateOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str, **kwargs):
        """
        **Updates a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

        - organizationId (string): Organization ID
        - policyObjectGroupId (string): Policy object group ID
        - name (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - objectIds (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "updateOrganizationPolicyObjectsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyObjectGroupId = urllib.parse.quote(str(policyObjectGroupId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        body_params = [
            "name",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationPolicyObjectsGroup: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str):
        """
        **Deletes a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

        - organizationId (string): Organization ID
        - policyObjectGroupId (string): Policy object group ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policyObjects", "groups"],
            "operation": "deleteOrganizationPolicyObjectsGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyObjectGroupId = urllib.parse.quote(str(policyObjectGroupId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        return self._session.delete(metadata, resource)

    def getOrganizationPolicyObject(self, organizationId: str, policyObjectId: str):
        """
        **Shows details of a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-object

        - organizationId (string): Organization ID
        - policyObjectId (string): Policy object ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "getOrganizationPolicyObject",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyObjectId = urllib.parse.quote(str(policyObjectId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

        return self._session.get(metadata, resource)

    def updateOrganizationPolicyObject(self, organizationId: str, policyObjectId: str, **kwargs):
        """
        **Updates a Policy Object**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

        - organizationId (string): Organization ID
        - policyObjectId (string): Policy object ID
        - name (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - cidr (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
        - fqdn (string): Fully qualified domain name of policy object (e.g. "example.com")
        - mask (string): Mask of a policy object (e.g. "255.255.0.0"). Used only with deprecated `type=ipAndMask`.
        - ip (string): IP Address of a policy object (e.g. "1.2.3.4"). Used only with deprecated `type=ipAndMask`.
        - groupIds (array): The IDs of policy object groups the policy object belongs to
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "updateOrganizationPolicyObject",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyObjectId = urllib.parse.quote(str(policyObjectId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

        body_params = [
            "name",
            "cidr",
            "fqdn",
            "mask",
            "ip",
            "groupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationPolicyObject: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationPolicyObject(self, organizationId: str, policyObjectId: str):
        """
        **Deletes a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

        - organizationId (string): Organization ID
        - policyObjectId (string): Policy object ID
        """

        metadata = {
            "tags": ["organizations", "configure", "policyObjects"],
            "operation": "deleteOrganizationPolicyObject",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        policyObjectId = urllib.parse.quote(str(policyObjectId), safe="")
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

        return self._session.delete(metadata, resource)

    def getOrganizationRoutingVrfs(self, organizationId: str, **kwargs):
        """
        **List existing organization-wide VRFs (Virtual Routing and Forwarding).**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-routing-vrfs

        - organizationId (string): Organization ID
        - vrfIds (array): IDs of the desired VRFs.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "routing", "vrfs"],
            "operation": "getOrganizationRoutingVrfs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/routing/vrfs"

        query_params = [
            "vrfIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "vrfIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationRoutingVrfs: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def createOrganizationRoutingVrf(self, organizationId: str, name: str, **kwargs):
        """
        **Add an organization-wide VRF (Virtual Routing and Forwarding)**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-routing-vrf

        - organizationId (string): Organization ID
        - name (string): The name of the VRF (Virtual Routing and Forwarding)
        - description (string): Description of the VRF (Virtual Routing and Forwarding)
        - routeDistinguisher (string): RD (Route Distinguisher) for the VRF (Virtual Routing and Forwarding)
        - routeTarget (string): Route target are used to control the import and export of routes between VRFs
        - appliance (object): This parameter is used to enable or disable the VRF on the WAN appliance
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "routing", "vrfs"],
            "operation": "createOrganizationRoutingVrf",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/routing/vrfs"

        body_params = [
            "name",
            "description",
            "routeDistinguisher",
            "routeTarget",
            "appliance",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationRoutingVrf: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationRoutingVrfsOverviewByVrf(self, organizationId: str, **kwargs):
        """
        **List existing organization-wide VRFs (Virtual Routing and Forwarding) overviews.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-routing-vrfs-overview-by-vrf

        - organizationId (string): Organization ID
        - vrfIds (array): IDs of the desired VRFs.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "routing", "vrfs", "overview", "byVrf"],
            "operation": "getOrganizationRoutingVrfsOverviewByVrf",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/routing/vrfs/overview/byVrf"

        query_params = [
            "vrfIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "vrfIds",
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
                    f"getOrganizationRoutingVrfsOverviewByVrf: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def updateOrganizationRoutingVrf(self, organizationId: str, vrfId: str, **kwargs):
        """
        **Update an organization-wide VRF (Virtual Routing and Forwarding)**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-routing-vrf

        - organizationId (string): Organization ID
        - vrfId (string): Vrf ID
        - name (string): The name of the VRF (Virtual Routing and Forwarding)
        - description (string): Description of the VRF (Virtual Routing and Forwarding)
        - routeDistinguisher (string): RD (Route Distinguisher) for the VRF (Virtual Routing and Forwarding)
        - routeTarget (string): Route target are used to control the import and export of routes between VRFs
        - appliance (object): This parameter is used to enable or disable the VRF on the WAN appliance
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "routing", "vrfs"],
            "operation": "updateOrganizationRoutingVrf",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        vrfId = urllib.parse.quote(str(vrfId), safe="")
        resource = f"/organizations/{organizationId}/routing/vrfs/{vrfId}"

        body_params = [
            "name",
            "description",
            "routeDistinguisher",
            "routeTarget",
            "appliance",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationRoutingVrf: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationRoutingVrf(self, organizationId: str, vrfId: str):
        """
        **Delete a VRF (Virtual Routing and Forwarding) from a organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-routing-vrf

        - organizationId (string): Organization ID
        - vrfId (string): Vrf ID
        """

        metadata = {
            "tags": ["organizations", "configure", "routing", "vrfs"],
            "operation": "deleteOrganizationRoutingVrf",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        vrfId = urllib.parse.quote(str(vrfId), safe="")
        resource = f"/organizations/{organizationId}/routing/vrfs/{vrfId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSaml(self, organizationId: str):
        """
        **Returns the SAML SSO enabled settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "saml"],
            "operation": "getOrganizationSaml",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/saml"

        return self._session.get(metadata, resource)

    def updateOrganizationSaml(self, organizationId: str, **kwargs):
        """
        **Updates the SAML SSO enabled settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml

        - organizationId (string): Organization ID
        - enabled (boolean): Boolean for updating SAML SSO enabled settings.
        - spInitiated (object): SP-Initiated SSO settings
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "saml"],
            "operation": "updateOrganizationSaml",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/saml"

        body_params = [
            "enabled",
            "spInitiated",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationSaml: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationSamlIdps(self, organizationId: str):
        """
        **List the SAML IdPs in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "getOrganizationSamlIdps",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/saml/idps"

        return self._session.get(metadata, resource)

    def createOrganizationSamlIdp(self, organizationId: str, x509certSha1Fingerprint: str, **kwargs):
        """
        **Create a SAML IdP for your organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        - organizationId (string): Organization ID
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - ssoLoginUrl (string): Dashboard will redirect users to this URL to log in again when their sessions expire.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "createOrganizationSamlIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/saml/idps"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSamlIdp: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateOrganizationSamlIdp(self, organizationId: str, idpId: str, **kwargs):
        """
        **Update a SAML IdP in your organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - ssoLoginUrl (string): Dashboard will redirect users to this URL to log in again when their sessions expire.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "updateOrganizationSamlIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        idpId = urllib.parse.quote(str(idpId), safe="")
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationSamlIdp: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationSamlIdp(self, organizationId: str, idpId: str):
        """
        **Get a SAML IdP from your organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        """

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "getOrganizationSamlIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        idpId = urllib.parse.quote(str(idpId), safe="")
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        return self._session.get(metadata, resource)

    def deleteOrganizationSamlIdp(self, organizationId: str, idpId: str):
        """
        **Remove a SAML IdP in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        """

        metadata = {
            "tags": ["organizations", "configure", "saml", "idps"],
            "operation": "deleteOrganizationSamlIdp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        idpId = urllib.parse.quote(str(idpId), safe="")
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSamlRoles(self, organizationId: str):
        """
        **List the SAML roles for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "getOrganizationSamlRoles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/samlRoles"

        return self._session.get(metadata, resource)

    def createOrganizationSamlRole(self, organizationId: str, role: str, orgAccess: str, **kwargs):
        """
        **Create a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

        - organizationId (string): Organization ID
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only', 'full' or 'enterprise' or a custom role in the format custom-role:ID:NAME.
        - tags (array): The list of tags that the SAML administrator has privileges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "createOrganizationSamlRole",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/samlRoles"

        body_params = [
            "role",
            "orgAccess",
            "tags",
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSamlRole: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Return a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

        - organizationId (string): Organization ID
        - samlRoleId (string): Saml role ID
        """

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "getOrganizationSamlRole",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        samlRoleId = urllib.parse.quote(str(samlRoleId), safe="")
        resource = f"/organizations/{organizationId}/samlRoles/{samlRoleId}"

        return self._session.get(metadata, resource)

    def updateOrganizationSamlRole(self, organizationId: str, samlRoleId: str, **kwargs):
        """
        **Update a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

        - organizationId (string): Organization ID
        - samlRoleId (string): Saml role ID
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only', 'full' or 'enterprise' or a custom role in the format custom-role:ID:NAME.
        - tags (array): The list of tags that the SAML administrator has privileges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "updateOrganizationSamlRole",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        samlRoleId = urllib.parse.quote(str(samlRoleId), safe="")
        resource = f"/organizations/{organizationId}/samlRoles/{samlRoleId}"

        body_params = [
            "role",
            "orgAccess",
            "tags",
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationSamlRole: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Remove a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role

        - organizationId (string): Organization ID
        - samlRoleId (string): Saml role ID
        """

        metadata = {
            "tags": ["organizations", "configure", "samlRoles"],
            "operation": "deleteOrganizationSamlRole",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        samlRoleId = urllib.parse.quote(str(samlRoleId), safe="")
        resource = f"/organizations/{organizationId}/samlRoles/{samlRoleId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSaseConnectors(self, organizationId: str):
        """
        **List SSE Connectors for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-connectors

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "sase", "connectors"],
            "operation": "getOrganizationSaseConnectors",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/connectors"

        return self._session.get(metadata, resource)

    def batchOrganizationSaseConnectorsDelete(self, organizationId: str, **kwargs):
        """
        **Delete SSE Connectors by ID**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-sase-connectors-delete

        - organizationId (string): Organization ID
        - items (array): List of connectors to delete (maximum 20 items)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "sase", "connectors"],
            "operation": "batchOrganizationSaseConnectorsDelete",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/connectors/batchDelete"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"batchOrganizationSaseConnectorsDelete: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def createOrganizationSaseIntegration(self, organizationId: str, api: dict, **kwargs):
        """
        **Create a new Secure Access integration**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-sase-integration

        - organizationId (string): Organization ID
        - api (object): API credentials
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "sase", "integrations"],
            "operation": "createOrganizationSaseIntegration",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/integrations"

        body_params = [
            "api",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSaseIntegration: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationSaseIntegration(self, organizationId: str, integrationId: str):
        """
        **Get details of a Secure Access integration**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-integration

        - organizationId (string): Organization ID
        - integrationId (string): Integration ID
        """

        metadata = {
            "tags": ["organizations", "configure", "sase", "integrations"],
            "operation": "getOrganizationSaseIntegration",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        integrationId = urllib.parse.quote(str(integrationId), safe="")
        resource = f"/organizations/{organizationId}/sase/integrations/{integrationId}"

        return self._session.get(metadata, resource)

    def deleteOrganizationSaseIntegration(self, organizationId: str, integrationId: str):
        """
        **Remove a Secure Access integration**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sase-integration

        - organizationId (string): Organization ID
        - integrationId (string): Integration ID
        """

        metadata = {
            "tags": ["organizations", "configure", "sase", "integrations"],
            "operation": "deleteOrganizationSaseIntegration",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        integrationId = urllib.parse.quote(str(integrationId), safe="")
        resource = f"/organizations/{organizationId}/sase/integrations/{integrationId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSaseNetworksEligible(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List of MX networks or templates that can be enrolled into Secure Access**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-networks-eligible

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 5.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - search (string): If provided, filters results by network name
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "sase", "networks", "eligible"],
            "operation": "getOrganizationSaseNetworksEligible",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/networks/eligible"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "search",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSaseNetworksEligible: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSaseRegions(self, organizationId: str):
        """
        **List regions**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-regions

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "sase", "regions"],
            "operation": "getOrganizationSaseRegions",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/regions"

        return self._session.get(metadata, resource)

    def getOrganizationSaseSites(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List of enrolled SASE sites in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-sites

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - search (string): If provided, filters results by search string
        - status (string): If provided, filters results by site status label (e.g., 'good')
        - siteId (string): If provided, returns only the site matching this ID
        """

        kwargs.update(locals())

        if "status" in kwargs:
            options = ["bad NAT", "bad tunnel", "dormant", "good", "many bad tunnels", "no registry", "offline"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "sase", "sites"],
            "operation": "getOrganizationSaseSites",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/sites"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "search",
            "status",
            "siteId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSaseSites: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def attachOrganizationSaseSites(self, organizationId: str, items: list, **kwargs):
        """
        **Attach sites in this organization to Secure Access**
        https://developer.cisco.com/meraki/api-v1/#!attach-organization-sase-sites

        - organizationId (string): Organization ID
        - items (array): List of Meraki SD-WAN sites with the associated regions to be attached.
        """

        kwargs = locals()

        metadata = {
            "tags": ["organizations", "configure", "sase", "sites"],
            "operation": "attachOrganizationSaseSites",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/sites/attach"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"attachOrganizationSaseSites: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationSaseSitesConnectivityHistoryBySite(self, organizationId: str, **kwargs):
        """
        **Get the connectivity history of SASE sites in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-sites-connectivity-history-by-site

        - organizationId (string): Organization ID
        - siteIds (array): Array of site IDs to fetch connectivity status data (maximum 100 values)
        - timespan (string): Timespan for the status data (e.g., '-2hours')
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "sase", "sites", "connectivity", "history", "bySite"],
            "operation": "getOrganizationSaseSitesConnectivityHistoryBySite",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/sites/connectivity/history/bySite"

        query_params = [
            "siteIds",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "siteIds",
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
                    f"getOrganizationSaseSitesConnectivityHistoryBySite: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSaseSitesConnectivityOverview(self, organizationId: str):
        """
        **List high-level SASE site statuses (healthy, degraded, offline)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sase-sites-connectivity-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "sase", "sites", "connectivity", "overview"],
            "operation": "getOrganizationSaseSitesConnectivityOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/sites/connectivity/overview"

        return self._session.get(metadata, resource)

    def detachOrganizationSaseSites(self, organizationId: str, **kwargs):
        """
        **Detach sites in this organization from Secure Access**
        https://developer.cisco.com/meraki/api-v1/#!detach-organization-sase-sites

        - organizationId (string): Organization ID
        - items (array): List of Secure Access sites to be detached.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "sase", "sites"],
            "operation": "detachOrganizationSaseSites",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sase/sites/detach"

        return self._session.delete(metadata, resource)

    def updateOrganizationSaseSite(self, organizationId: str, siteId: str, **kwargs):
        """
        **Update the configuration for a site**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sase-site

        - organizationId (string): Organization ID
        - siteId (string): Site ID of the site to update
        - routing (object): Routing configuration for the site
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "sase", "sites"],
            "operation": "updateOrganizationSaseSite",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        siteId = urllib.parse.quote(str(siteId), safe="")
        resource = f"/organizations/{organizationId}/sase/sites/{siteId}"

        body_params = [
            "siteId",
            "routing",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationSaseSite: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationSites(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Lists unified site resources for an organization across Meraki networks and Catalyst Center sites**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sites

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 500.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - ids (array): Optional parameter to filter resources by unified resource ID. This filter uses multiple exact matches.
        - resourceTypes (array): Optional parameter to filter resources by returned resource type.
        - resourceTags (array): Optional parameter to filter resources by tag. By default all provided tags must match.
        - resourceName (string): Optional parameter to filter resources by case-insensitive partial name match.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "sites"],
            "operation": "getOrganizationSites",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sites"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "ids",
            "resourceTypes",
            "resourceTags",
            "resourceName",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "ids",
            "resourceTypes",
            "resourceTags",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSites: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSitesBuildings(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the buildings belonging to the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sites-buildings

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter buildings by one or more network IDs
        - buildingIds (array): Optional parameter to filter buildings by one or more building IDs
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "sites", "buildings"],
            "operation": "getOrganizationSitesBuildings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sites/buildings"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "buildingIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "buildingIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSitesBuildings: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSnmp(self, organizationId: str):
        """
        **Return the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "snmp"],
            "operation": "getOrganizationSnmp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/snmp"

        return self._session.get(metadata, resource)

    def updateOrganizationSnmp(self, organizationId: str, **kwargs):
        """
        **Update the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp

        - organizationId (string): Organization ID
        - v2cEnabled (boolean): Boolean indicating whether SNMP version 2c is enabled for the organization.
        - v3Enabled (boolean): Boolean indicating whether SNMP version 3 is enabled for the organization.
        - v3AuthMode (string): The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
        - v3AuthPass (string): The SNMP version 3 authentication password. Must be at least 8 characters if specified.
        - v3PrivMode (string): The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
        - v3PrivPass (string): The SNMP version 3 privacy password. Must be at least 8 characters if specified.
        - peerIps (array): The list of IPv4 addresses that are allowed to access the SNMP server.
        """

        kwargs.update(locals())

        if "v3AuthMode" in kwargs:
            options = ["MD5", "SHA"]
            assert kwargs["v3AuthMode"] in options, (
                f'''"v3AuthMode" cannot be "{kwargs["v3AuthMode"]}", & must be set to one of: {options}'''
            )
        if "v3PrivMode" in kwargs:
            options = ["AES128", "DES"]
            assert kwargs["v3PrivMode"] in options, (
                f'''"v3PrivMode" cannot be "{kwargs["v3PrivMode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "configure", "snmp"],
            "operation": "updateOrganizationSnmp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/snmp"

        body_params = [
            "v2cEnabled",
            "v3Enabled",
            "v3AuthMode",
            "v3AuthPass",
            "v3PrivMode",
            "v3PrivPass",
            "peerIps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationSnmp: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationSnmpTrapsByNetwork(self, organizationId: str, **kwargs):
        """
        **Retrieve the SNMP trap configuration for the networks in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp-traps-by-network

        - organizationId (string): Organization ID
        - networkIds (array): An optional parameter to filter SNMP trap configs by network IDs
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "snmp", "traps", "byNetwork"],
            "operation": "getOrganizationSnmpTrapsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/snmp/traps/byNetwork"

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
                self._session._logger.warning(f"getOrganizationSnmpTrapsByNetwork: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationSplashAsset(self, organizationId: str, id: str):
        """
        **Get a Splash Theme Asset**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-splash-asset

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "splash", "assets"],
            "operation": "getOrganizationSplashAsset",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/splash/assets/{id}"

        return self._session.get(metadata, resource)

    def deleteOrganizationSplashAsset(self, organizationId: str, id: str):
        """
        **Delete a Splash Theme Asset**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-asset

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "splash", "assets"],
            "operation": "deleteOrganizationSplashAsset",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/splash/assets/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSplashThemes(self, organizationId: str):
        """
        **List Splash Themes**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-splash-themes

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "getOrganizationSplashThemes",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/splash/themes"

        return self._session.get(metadata, resource)

    def createOrganizationSplashTheme(self, organizationId: str, **kwargs):
        """
        **Create a Splash Theme**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme

        - organizationId (string): Organization ID
        - name (string): theme name
        - baseTheme (string): base theme id
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "createOrganizationSplashTheme",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/splash/themes"

        body_params = [
            "name",
            "baseTheme",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSplashTheme: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationSplashTheme(self, organizationId: str, id: str):
        """
        **Delete a Splash Theme**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-theme

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes"],
            "operation": "deleteOrganizationSplashTheme",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/splash/themes/{id}"

        return self._session.delete(metadata, resource)

    def createOrganizationSplashThemeAsset(self, organizationId: str, themeIdentifier: str, **kwargs):
        """
        **Create a Splash Theme Asset**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme-asset

        - organizationId (string): Organization ID
        - themeIdentifier (string): Theme identifier
        - name (string): File name. Will overwrite files with same name.
        - content (string): a file containing the asset content
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "splash", "themes", "assets"],
            "operation": "createOrganizationSplashThemeAsset",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        themeIdentifier = urllib.parse.quote(str(themeIdentifier), safe="")
        resource = f"/organizations/{organizationId}/splash/themes/{themeIdentifier}/assets"

        body_params = [
            "name",
            "content",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSplashThemeAsset: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationSummaryTopAppliancesByUtilization(self, organizationId: str, **kwargs):
        """
        **Return the top 10 appliances sorted by utilization over given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-appliances-by-utilization

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "appliances", "byUtilization"],
            "operation": "getOrganizationSummaryTopAppliancesByUtilization",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/appliances/byUtilization"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopAppliancesByUtilization: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopApplicationsByUsage(self, organizationId: str, **kwargs):
        """
        **Return the top applications sorted by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-applications-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - device (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "applications", "byUsage"],
            "operation": "getOrganizationSummaryTopApplicationsByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/applications/byUsage"

        query_params = [
            "networkTag",
            "device",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopApplicationsByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopApplicationsCategoriesByUsage(self, organizationId: str, **kwargs):
        """
        **Return the top application categories sorted by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-applications-categories-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "applications", "categories", "byUsage"],
            "operation": "getOrganizationSummaryTopApplicationsCategoriesByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/applications/categories/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopApplicationsCategoriesByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopClientsByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 clients by data usage (in mb) over given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "clients", "byUsage"],
            "operation": "getOrganizationSummaryTopClientsByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/clients/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopClientsByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopClientsManufacturersByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-manufacturers-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "clients", "manufacturers", "byUsage"],
            "operation": "getOrganizationSummaryTopClientsManufacturersByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/clients/manufacturers/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopClientsManufacturersByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopDevicesByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 devices sorted by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "devices", "byUsage"],
            "operation": "getOrganizationSummaryTopDevicesByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/devices/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopDevicesByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopDevicesModelsByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 device models sorted by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-models-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "devices", "models", "byUsage"],
            "operation": "getOrganizationSummaryTopDevicesModelsByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/devices/models/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopDevicesModelsByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopNetworksByStatus(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the client and status overview information for the networks in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-networks-by-status

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "networks", "byStatus"],
            "operation": "getOrganizationSummaryTopNetworksByStatus",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/networks/byStatus"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
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
                    f"getOrganizationSummaryTopNetworksByStatus: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSummaryTopSsidsByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 ssids by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-ssids-by-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 8 hours and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "ssids", "byUsage"],
            "operation": "getOrganizationSummaryTopSsidsByUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/ssids/byUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopSsidsByUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSummaryTopSwitchesByEnergyUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 switches by energy usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-switches-by-energy-usage

        - organizationId (string): Organization ID
        - networkTag (string): Match result to an exact network tag
        - deviceTag (string): Match result to an exact device tag
        - networkId (string): Match result to an exact network id
        - quantity (integer): Set number of desired results to return. Default is 10. Maximum is 50
        - ssidName (string): Filter results by ssid name
        - usageUplink (string): Filter results by usage uplink
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 186 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 25 minutes and be less than or equal to 186 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "summary", "top", "switches", "byEnergyUsage"],
            "operation": "getOrganizationSummaryTopSwitchesByEnergyUsage",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/summary/top/switches/byEnergyUsage"

        query_params = [
            "networkTag",
            "deviceTag",
            "networkId",
            "quantity",
            "ssidName",
            "usageUplink",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSummaryTopSwitchesByEnergyUsage: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationUplinksStatuses(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the uplink status of every Meraki MX, MG and Z series devices in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "uplinks", "statuses"],
            "operation": "getOrganizationUplinksStatuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/uplinks/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
            "iccids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "iccids",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationUplinksStatuses: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWebhooksAlertTypes(self, organizationId: str, **kwargs):
        """
        **Return a list of alert types to be used with managing webhook alerts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

        - organizationId (string): Organization ID
        - productType (string): Filter sample alerts to a specific product type
        """

        kwargs.update(locals())

        if "productType" in kwargs:
            options = ["appliance", "camera", "cellularGateway", "platform", "sensor", "sm", "switch", "wireless"]
            assert kwargs["productType"] in options, (
                f'''"productType" cannot be "{kwargs["productType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["organizations", "monitor", "webhooks", "alertTypes"],
            "operation": "getOrganizationWebhooksAlertTypes",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/alertTypes"

        query_params = [
            "productType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationWebhooksAlertTypes: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationWebhooksCallbacksStatus(self, organizationId: str, callbackId: str):
        """
        **Return the status of an API callback**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-callbacks-status

        - organizationId (string): Organization ID
        - callbackId (string): Callback ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "callbacks", "statuses"],
            "operation": "getOrganizationWebhooksCallbacksStatus",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        callbackId = urllib.parse.quote(str(callbackId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/callbacks/statuses/{callbackId}"

        return self._session.get(metadata, resource)

    def getOrganizationWebhooksHttpServers(self, organizationId: str):
        """
        **List the HTTP servers for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-http-servers

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "httpServers"],
            "operation": "getOrganizationWebhooksHttpServers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/httpServers"

        return self._session.get(metadata, resource)

    def createOrganizationWebhooksHttpServer(self, organizationId: str, name: str, url: str, **kwargs):
        """
        **Add an HTTP server to an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-webhooks-http-server

        - organizationId (string): Organization ID
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        - payloadTemplate (object): The payload template to use when posting data to the HTTP server.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "httpServers"],
            "operation": "createOrganizationWebhooksHttpServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/httpServers"

        body_params = [
            "name",
            "url",
            "sharedSecret",
            "payloadTemplate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationWebhooksHttpServer: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getOrganizationWebhooksHttpServer(self, organizationId: str, id: str):
        """
        **Return an HTTP server for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-http-server

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "httpServers"],
            "operation": "getOrganizationWebhooksHttpServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/webhooks/httpServers/{id}"

        return self._session.get(metadata, resource)

    def updateOrganizationWebhooksHttpServer(self, organizationId: str, id: str, **kwargs):
        """
        **Update an HTTP server for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-webhooks-http-server

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        - payloadTemplate (object): The payload template to use when posting data to the HTTP server.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "httpServers"],
            "operation": "updateOrganizationWebhooksHttpServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/webhooks/httpServers/{id}"

        body_params = [
            "name",
            "url",
            "sharedSecret",
            "payloadTemplate",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationWebhooksHttpServer: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationWebhooksHttpServer(self, organizationId: str, id: str):
        """
        **Delete an HTTP server from an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-webhooks-http-server

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "httpServers"],
            "operation": "deleteOrganizationWebhooksHttpServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/webhooks/httpServers/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationWebhooksLogs(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return the log of webhook POSTs sent**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - url (string): The URL the webhook was sent to
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "monitor", "webhooks", "logs"],
            "operation": "getOrganizationWebhooksLogs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/logs"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "url",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationWebhooksLogs: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWebhooksPayloadTemplates(self, organizationId: str):
        """
        **List the webhook payload templates for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-payload-templates

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "payloadTemplates"],
            "operation": "getOrganizationWebhooksPayloadTemplates",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/payloadTemplates"

        return self._session.get(metadata, resource)

    def createOrganizationWebhooksPayloadTemplate(self, organizationId: str, name: str, **kwargs):
        """
        **Create a webhook payload template for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-webhooks-payload-template

        - organizationId (string): Organization ID
        - name (string): The name of the new template
        - body (string): The liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
        - headers (array): The liquid template used with the webhook headers.
        - bodyFile (string): A file containing liquid template used for the body of the webhook message. Either `body` or `bodyFile` must be specified.
        - headersFile (string): A file containing the liquid template used with the webhook headers.
        - sharing (object): Information on which entities have access to the template
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "payloadTemplates"],
            "operation": "createOrganizationWebhooksPayloadTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/payloadTemplates"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
            "sharing",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWebhooksPayloadTemplate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationWebhooksPayloadTemplate(self, organizationId: str, payloadTemplateId: str):
        """
        **Get the webhook payload template for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-payload-template

        - organizationId (string): Organization ID
        - payloadTemplateId (string): Payload template ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "payloadTemplates"],
            "operation": "getOrganizationWebhooksPayloadTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        payloadTemplateId = urllib.parse.quote(str(payloadTemplateId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/payloadTemplates/{payloadTemplateId}"

        return self._session.get(metadata, resource)

    def deleteOrganizationWebhooksPayloadTemplate(self, organizationId: str, payloadTemplateId: str):
        """
        **Destroy a webhook payload template for an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-webhooks-payload-template

        - organizationId (string): Organization ID
        - payloadTemplateId (string): Payload template ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "payloadTemplates"],
            "operation": "deleteOrganizationWebhooksPayloadTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        payloadTemplateId = urllib.parse.quote(str(payloadTemplateId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/payloadTemplates/{payloadTemplateId}"

        return self._session.delete(metadata, resource)

    def updateOrganizationWebhooksPayloadTemplate(self, organizationId: str, payloadTemplateId: str, **kwargs):
        """
        **Update a webhook payload template for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-webhooks-payload-template

        - organizationId (string): Organization ID
        - payloadTemplateId (string): Payload template ID
        - name (string): The name of the template
        - body (string): The liquid template used for the body of the webhook message.
        - headers (array): The liquid template used with the webhook headers.
        - bodyFile (string): A file containing liquid template used for the body of the webhook message.
        - headersFile (string): A file containing the liquid template used with the webhook headers.
        - sharing (object): Information on which entities have access to the template
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "payloadTemplates"],
            "operation": "updateOrganizationWebhooksPayloadTemplate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        payloadTemplateId = urllib.parse.quote(str(payloadTemplateId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/payloadTemplates/{payloadTemplateId}"

        body_params = [
            "name",
            "body",
            "headers",
            "bodyFile",
            "headersFile",
            "sharing",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWebhooksPayloadTemplate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def createOrganizationWebhooksWebhookTest(self, organizationId: str, url: str, **kwargs):
        """
        **Send a test webhook for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-webhooks-webhook-test

        - organizationId (string): Organization ID
        - url (string): The URL where the test webhook will be sent
        - sharedSecret (string): The shared secret the test webhook will send. Optional. Defaults to HTTP server's shared secret. Otherwise, defaults to an empty string.
        - payloadTemplateId (string): The ID of the payload template of the test webhook. Defaults to the HTTP server's template ID if one exists for the given URL, or Generic template ID otherwise
        - payloadTemplateName (string): The name of the payload template.
        - alertTypeId (string): The type of alert which the test webhook will send. Optional. Defaults to insight_app_outage_start.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "webhookTests"],
            "operation": "createOrganizationWebhooksWebhookTest",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/webhookTests"

        body_params = [
            "url",
            "sharedSecret",
            "payloadTemplateId",
            "payloadTemplateName",
            "alertTypeId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWebhooksWebhookTest: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationWebhooksWebhookTest(self, organizationId: str, webhookTestId: str):
        """
        **Return the status of a webhook test for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-webhook-test

        - organizationId (string): Organization ID
        - webhookTestId (string): Webhook test ID
        """

        metadata = {
            "tags": ["organizations", "configure", "webhooks", "webhookTests"],
            "operation": "getOrganizationWebhooksWebhookTest",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        webhookTestId = urllib.parse.quote(str(webhookTestId), safe="")
        resource = f"/organizations/{organizationId}/webhooks/webhookTests/{webhookTestId}"

        return self._session.get(metadata, resource)
