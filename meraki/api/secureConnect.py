import urllib


class SecureConnect(object):
    def __init__(self, session):
        super(SecureConnect, self).__init__()
        self._session = session

    def getOrganizationSecureConnectPrivateApplicationGroups(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Provides a list of private application groups for an Organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-private-application-groups

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - nameIncludes (string): Optional parameter to search the application group list by group name, case is ignored
        - applicationGroupIds (array): List of application group ids attached to fetch
        - sortBy (string): Optional parameter to specify the field used to sort objects.
        - sortOrder (string): Optional parameter to specify the sort order. Default value is asc.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["applicationGroupId", "modifiedAt", "name"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplicationGroups"],
            "operation": "getOrganizationSecureConnectPrivateApplicationGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplicationGroups"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "nameIncludes",
            "applicationGroupIds",
            "sortBy",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "applicationGroupIds",
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
                    f"getOrganizationSecureConnectPrivateApplicationGroups: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSecureConnectPrivateApplicationGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Creates a group of private applications to apply to policy**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-private-application-group

        - organizationId (string): Organization ID
        - name (string): Application Group Name. This is required and cannot have any special characters other than spaces and hyphens
        - description (string): Optional short description for application group
        - applicationIds (array): List of application ids attached to this Private Application Group
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplicationGroups"],
            "operation": "createOrganizationSecureConnectPrivateApplicationGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplicationGroups"

        body_params = [
            "name",
            "description",
            "applicationIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSecureConnectPrivateApplicationGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationSecureConnectPrivateApplicationGroup(self, organizationId: str, id: str, name: str, **kwargs):
        """
        **Update an application group in an Organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-secure-connect-private-application-group

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Application Group Name. This is required and cannot have any special characters other than spaces and hyphens
        - description (string): Optional short description for application group
        - applicationIds (array): List of application ids attached to this Private Application Group
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplicationGroups"],
            "operation": "updateOrganizationSecureConnectPrivateApplicationGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplicationGroups/{id}"

        body_params = [
            "name",
            "description",
            "applicationIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSecureConnectPrivateApplicationGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSecureConnectPrivateApplicationGroup(self, organizationId: str, id: str, **kwargs):
        """
        **Deletes private application group from an Organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-private-application-group

        - organizationId (string): Organization ID
        - id (string): ID
        - force (boolean): Boolean flag to force delete application group, even if application group is in use by one or more rules.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplicationGroups"],
            "operation": "deleteOrganizationSecureConnectPrivateApplicationGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplicationGroups/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSecureConnectPrivateApplicationGroup(self, organizationId: str, id: str):
        """
        **Return the details of a specific private application group**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-private-application-group

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplicationGroups"],
            "operation": "getOrganizationSecureConnectPrivateApplicationGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplicationGroups/{id}"

        return self._session.get(metadata, resource)

    def getOrganizationSecureConnectPrivateApplications(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Provides a list of private applications for an Organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-private-applications

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - nameIncludes (string): Optional parameter to filter the private applications list by application and associated application group names, case is ignored
        - applicationGroupIds (array): Optional parameter for filtering the list of private applications belonging to the application group identified by the given IDs.
        - appTypes (array): Optional parameter for filtering the list of private applications by applications that contain at least one destination with the specified accessType value.
        - sortBy (string): Optional parameter to specify the field used to sort objects.
        - sortOrder (string): Optional parameter to specify the sort order. Default value is asc.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["modifiedAt", "name"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplications"],
            "operation": "getOrganizationSecureConnectPrivateApplications",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplications"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "nameIncludes",
            "applicationGroupIds",
            "appTypes",
            "sortBy",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "applicationGroupIds",
            "appTypes",
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
                    f"getOrganizationSecureConnectPrivateApplications: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSecureConnectPrivateApplication(self, organizationId: str, name: str, destinations: list, **kwargs):
        """
        **Adds a new private application to the Organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-private-application

        - organizationId (string): Organization ID
        - name (string): Name of Application. This is required and should be unique across all applications for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - destinations (array): List of IP address destinations.
        - description (string): Optional Text description for Application
        - appProtocol (string): Protocol for communication between proxy to private application. Applicable for Browser Based Access only.
        - sni (string): Optional SNI. Applicable for Browser Based Access only. SNI should be a valid domain.
        - externalFQDN (string): Cisco or Customer Managed URL for Application. Applicable for Browser Based Access only. This field is system generated based on the application name and organization ID and overrides user input in payload. This value must be unique across all applications for a given organization.
        - sslVerificationEnabled (boolean): Enable Upstream SSL verification for the internally hosted URL by the customer. Applicable for Browser Based Access only. Default is true.
        - applicationGroupIds (array): List of application group ids attached to this Private Application
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplications"],
            "operation": "createOrganizationSecureConnectPrivateApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplications"

        body_params = [
            "name",
            "description",
            "destinations",
            "appProtocol",
            "sni",
            "externalFQDN",
            "sslVerificationEnabled",
            "applicationGroupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSecureConnectPrivateApplication: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationSecureConnectPrivateApplication(
        self, organizationId: str, id: str, name: str, destinations: list, **kwargs
    ):
        """
        **Updates a specific private application**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-secure-connect-private-application

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of Application. This is required and should be unique across all applications for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - destinations (array): List of IP address destinations.
        - description (string): Optional Text description for Application
        - appProtocol (string): Protocol for communication between proxy to private application. Applicable for Browser Based Access only.
        - sni (string): Optional SNI. Applicable for Browser Based Access only. SNI should be a valid domain.
        - externalFQDN (string): Cisco or Customer Managed URL for Application. Applicable for Browser Based Access only. This field is system generated based on the application name and organization ID and overrides user input in payload. This value must be unique across all applications for a given organization.
        - sslVerificationEnabled (boolean): Enable Upstream SSL verification for the internally hosted URL by the customer. Applicable for Browser Based Access only. Default is true.
        - applicationGroupIds (array): List of application group ids attached to this Private Application
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplications"],
            "operation": "updateOrganizationSecureConnectPrivateApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplications/{id}"

        body_params = [
            "name",
            "description",
            "destinations",
            "appProtocol",
            "sni",
            "externalFQDN",
            "sslVerificationEnabled",
            "applicationGroupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSecureConnectPrivateApplication: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSecureConnectPrivateApplication(self, organizationId: str, id: str, **kwargs):
        """
        **Deletes a specific private application**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-private-application

        - organizationId (string): Organization ID
        - id (string): ID
        - force (boolean): Boolean flag to force delete application, even if application is in use by one or more rules.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplications"],
            "operation": "deleteOrganizationSecureConnectPrivateApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplications/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSecureConnectPrivateApplication(self, organizationId: str, id: str):
        """
        **Return the details of a specific private application**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-private-application

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["secureConnect", "configure", "privateApplications"],
            "operation": "getOrganizationSecureConnectPrivateApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateApplications/{id}"

        return self._session.get(metadata, resource)

    def getOrganizationSecureConnectPrivateResourceGroups(self, organizationId: str):
        """
        **Provides a list of the private resource groups in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-private-resource-groups

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["secureConnect", "configure", "privateResourceGroups"],
            "operation": "getOrganizationSecureConnectPrivateResourceGroups",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups"

        return self._session.get(metadata, resource)

    def createOrganizationSecureConnectPrivateResourceGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Adds a new private resource group to an organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-private-resource-group

        - organizationId (string): Organization ID
        - name (string): Name of group. This is required and should be unique across all groups for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - description (string): Optional text description for a group.
        - resourceIds (array): List of resource ids assigned to this group.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateResourceGroups"],
            "operation": "createOrganizationSecureConnectPrivateResourceGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups"

        body_params = [
            "name",
            "description",
            "resourceIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSecureConnectPrivateResourceGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationSecureConnectPrivateResourceGroup(self, organizationId: str, id: str, name: str, **kwargs):
        """
        **Updates a specific private resource group.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-secure-connect-private-resource-group

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of group. This is required and should be unique across all groups for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - description (string): Optional text description for a group.
        - resourceIds (array): List of resource ids assigned to this group.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateResourceGroups"],
            "operation": "updateOrganizationSecureConnectPrivateResourceGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups/{id}"

        body_params = [
            "name",
            "description",
            "resourceIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSecureConnectPrivateResourceGroup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSecureConnectPrivateResourceGroup(self, organizationId: str, id: str):
        """
        **Deletes a specific private resource group.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-private-resource-group

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["secureConnect", "configure", "privateResourceGroups"],
            "operation": "deleteOrganizationSecureConnectPrivateResourceGroup",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSecureConnectPrivateResources(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Provides a list of private resources for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-private-resources

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (string): Number of resources to return for a paginated response.
        - startingAfter (string): The name of the resource to start after for a paginated response. Use '' for the first page.
        - endingBefore (string): The name of the resource to end before for a paginated response. Use '' for the final page.
        - sortBy (string): Parameter to specify the field used to sort objects, by default, resources are returned by name asc.
        - sortOrder (string): Parameter to specify the direction used to sort objects, by default, resources are returned by name asc.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateResources"],
            "operation": "getOrganizationSecureConnectPrivateResources",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortBy",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSecureConnectPrivateResources: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSecureConnectPrivateResource(
        self, organizationId: str, name: str, accessTypes: list, resourceAddresses: list, **kwargs
    ):
        """
        **Adds a new private resource to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-private-resource

        - organizationId (string): Organization ID
        - name (string): Name of resource. This is required and should be unique across all resources for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - accessTypes (array): List of access types.
        - resourceAddresses (array): List of resource addresses Protocols must be unique in this list.
        - description (string): Optional text description for a resource.
        - resourceGroupIds (array): List of resource group ids attached to this resource.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateResources"],
            "operation": "createOrganizationSecureConnectPrivateResource",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources"

        body_params = [
            "name",
            "description",
            "accessTypes",
            "resourceAddresses",
            "resourceGroupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSecureConnectPrivateResource: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationSecureConnectPrivateResource(
        self, organizationId: str, id: str, name: str, accessTypes: list, resourceAddresses: list, **kwargs
    ):
        """
        **Updates a specific private resource.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-secure-connect-private-resource

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of resource. This is required and should be unique across all resources for a given organization.Name cannot have any special characters other than spaces and hyphens.
        - accessTypes (array): List of access types.
        - resourceAddresses (array): List of resource addresses Protocols must be unique in this list.
        - description (string): Optional text description for resource.
        - resourceGroupIds (array): List of resource group ids attached to this resource.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "privateResources"],
            "operation": "updateOrganizationSecureConnectPrivateResource",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources/{id}"

        body_params = [
            "name",
            "description",
            "accessTypes",
            "resourceAddresses",
            "resourceGroupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationSecureConnectPrivateResource: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationSecureConnectPrivateResource(self, organizationId: str, id: str):
        """
        **Deletes a specific private resource**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-private-resource

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["secureConnect", "configure", "privateResources"],
            "operation": "deleteOrganizationSecureConnectPrivateResource",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationSecureConnectPublicApplications(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Provides a list of public applications for an Organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-public-applications

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - nameIncludes (string): Optional parameter to filter the public applications list by application name, case is ignored
        - risks (array): List of risk levels to filter by
        - categories (array): List of categories to filter by
        - appTypes (array): List of app types to filter by
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - sortBy (string): Optional parameter to specify the field used to sort objects, by default, applications are returned by lastDetected desc
        - sortOrder (string): Optional parameter to specify the sort order. Default value is desc.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["appType", "category", "lastDetected", "name", "risk"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "configure", "publicApplications"],
            "operation": "getOrganizationSecureConnectPublicApplications",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/publicApplications"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "nameIncludes",
            "risks",
            "categories",
            "appTypes",
            "t0",
            "t1",
            "timespan",
            "sortBy",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "risks",
            "categories",
            "appTypes",
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
                    f"getOrganizationSecureConnectPublicApplications: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSecureConnectRegions(self, organizationId: str, **kwargs):
        """
        **List deployed cloud hubs and regions in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-regions

        - organizationId (string): Organization ID
        - regionType (string): Filter results by region type
        """

        kwargs.update(locals())

        if "regionType" in kwargs:
            options = ["CNHE", "CloudHub", "Region", "ThirdParty"]
            assert kwargs["regionType"] in options, (
                f'''"regionType" cannot be "{kwargs["regionType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "configure", "regions"],
            "operation": "getOrganizationSecureConnectRegions",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/regions"

        query_params = [
            "regionType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSecureConnectRegions: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getOrganizationSecureConnectRemoteAccessLog(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
          **List the latest 5000 events logged by remote access.**
          https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-remote-access-log

          - organizationId (string): Organization ID
          - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
          - direction (string): direction to paginate, either "next" (default) or "prev" page
          - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 50.
          - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
          - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
          - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
          - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
          - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
          - identityids (string): An identity ID or comma-delimited list of identity ID.
          - identitytypes (string): An identity type or comma-delimited list of identity type.
          - connectionevent (string): Specify the type of connection event.
          - anyconnectversions (string): Specify a comma-separated list of AnyConnect Roaming Security module
        versions to filter the data.
          - osversions (string): Specify a comma-separated list of OS versions to filter the data.
        """

        kwargs.update(locals())

        if "connectionevent" in kwargs:
            options = ["connected", "disconnected", "failed"]
            assert kwargs["connectionevent"] in options, (
                f'''"connectionevent" cannot be "{kwargs["connectionevent"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "monitor", "remoteAccessLog"],
            "operation": "getOrganizationSecureConnectRemoteAccessLog",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/remoteAccessLog"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "identityids",
            "identitytypes",
            "connectionevent",
            "anyconnectversions",
            "osversions",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSecureConnectRemoteAccessLog: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSecureConnectRemoteAccessLogsExports(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Provides a list of remote access logs exports for an Organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-remote-access-logs-exports

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - status (string): Filter exports by status.
        """

        kwargs.update(locals())

        if "status" in kwargs:
            options = ["complete", "continue", "error", "in_progress", "new", "zip"]
            assert kwargs["status"] in options, (
                f'''"status" cannot be "{kwargs["status"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "configure", "remoteAccessLogsExports"],
            "operation": "getOrganizationSecureConnectRemoteAccessLogsExports",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/remoteAccessLogsExports"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "status",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSecureConnectRemoteAccessLogsExports: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSecureConnectRemoteAccessLogsExport(self, organizationId: str, from_: int, to: int, **kwargs):
        """
        **Creates a export for a provided timestamp interval.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-remote-access-logs-export

        - organizationId (string): Organization ID
        - from (integer): The start of the interval, must be within the past 30 days.
        - to (integer): The end of the interval, must not exceed the current date.
        """

        kwargs = locals()
        if "from_" in kwargs:
            kwargs["from"] = kwargs.pop("from_")

        metadata = {
            "tags": ["secureConnect", "configure", "remoteAccessLogsExports"],
            "operation": "createOrganizationSecureConnectRemoteAccessLogsExport",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/remoteAccessLogsExports"

        body_params = [
            "from",
            "to",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationSecureConnectRemoteAccessLogsExport: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationSecureConnectRemoteAccessLogsExportsDownload(
        self, organizationId: str, id: str, fileType: str, **kwargs
    ):
        """
        **Redirects to the download link of the completed export.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-remote-access-logs-exports-download

        - organizationId (string): Organization ID
        - id (string): Export ID.
        - fileType (string): Export download file type.
        """

        kwargs = locals()

        metadata = {
            "tags": ["secureConnect", "configure", "remoteAccessLogsExports", "download"],
            "operation": "getOrganizationSecureConnectRemoteAccessLogsExportsDownload",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/remoteAccessLogsExports/download"

        query_params = [
            "id",
            "fileType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationSecureConnectRemoteAccessLogsExportsDownload: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationSecureConnectRemoteAccessLogsExport(self, organizationId: str, id: str):
        """
        **Return the details of a specific remote access logs export**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-remote-access-logs-export

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["secureConnect", "configure", "remoteAccessLogsExports"],
            "operation": "getOrganizationSecureConnectRemoteAccessLogsExport",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/remoteAccessLogsExports/{id}"

        return self._session.get(metadata, resource)

    def getOrganizationSecureConnectSites(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List sites in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-secure-connect-sites

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - search (string): If provided, filters results by search string
        - enrolledState (string): Filter results by sites that have already been enrolled or can be enrolled. Acceptable values are 'enrolled' or 'enrollable
        """

        kwargs.update(locals())

        if "enrolledState" in kwargs:
            options = ["enrollable", "enrolled"]
            assert kwargs["enrolledState"] in options, (
                f'''"enrolledState" cannot be "{kwargs["enrolledState"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["secureConnect", "configure", "sites"],
            "operation": "getOrganizationSecureConnectSites",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/sites"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "search",
            "enrolledState",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationSecureConnectSites: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationSecureConnectSite(self, organizationId: str, **kwargs):
        """
        **Enroll sites in this organization to Secure Connect**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-site

        - organizationId (string): Organization ID
        - enrollments (array): List of Meraki SD-WAN sites with the associated regions to be enrolled.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "sites"],
            "operation": "createOrganizationSecureConnectSite",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/sites"

        body_params = [
            "enrollments",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationSecureConnectSite: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationSecureConnectSites(self, organizationId: str, **kwargs):
        """
        **Detach given sites from Secure Connect**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-sites

        - organizationId (string): Organization ID
        - sites (array): List of site IDs to detach
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["secureConnect", "configure", "sites"],
            "operation": "deleteOrganizationSecureConnectSites",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/secureConnect/sites"

        return self._session.delete(metadata, resource)
