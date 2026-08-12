import urllib


class AsyncSpaces:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def createNetworkSpacesSitesBuilding(self, networkId: str, name: str, **kwargs):
        """
        **Create a new building**
        https://developer.cisco.com/meraki/api-v1/#!create-network-spaces-sites-building

        - networkId (string): Network ID
        - name (string): The name of the building
        - bounds (object): Geographic bounding box for the building, expressed as north-east and south-west corner coordinates.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["spaces", "configure", "sites", "buildings"],
            "operation": "createNetworkSpacesSitesBuilding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/spaces/sites/buildings"

        body_params = [
            "name",
            "bounds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkSpacesSitesBuilding: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateNetworkSpacesSitesBuilding(self, networkId: str, buildingId: str, **kwargs):
        """
        **Update a building**
        https://developer.cisco.com/meraki/api-v1/#!update-network-spaces-sites-building

        - networkId (string): Network ID
        - buildingId (string): Building ID
        - name (string): The name of the building
        - bounds (object): Geographic bounding box for the building, expressed as north-east and south-west corner coordinates.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["spaces", "configure", "sites", "buildings"],
            "operation": "updateNetworkSpacesSitesBuilding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        buildingId = urllib.parse.quote(str(buildingId), safe="")
        resource = f"/networks/{networkId}/spaces/sites/buildings/{buildingId}"

        body_params = [
            "name",
            "bounds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSpacesSitesBuilding: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSpacesSitesBuilding(self, networkId: str, buildingId: str):
        """
        **Delete a building**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-spaces-sites-building

        - networkId (string): Network ID
        - buildingId (string): Building ID
        """

        metadata = {
            "tags": ["spaces", "configure", "sites", "buildings"],
            "operation": "deleteNetworkSpacesSitesBuilding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        buildingId = urllib.parse.quote(str(buildingId), safe="")
        resource = f"/networks/{networkId}/spaces/sites/buildings/{buildingId}"

        return self._session.delete(metadata, resource)

    def getOrganizationSpacesIntegrateStatus(self, organizationId: str):
        """
        **Get the status of the Spaces integration in Meraki**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-integrate-status

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["spaces", "configure", "integrate", "status"],
            "operation": "getOrganizationSpacesIntegrateStatus",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/spaces/integrate/status"

        return self._session.get(metadata, resource)

    def removeOrganizationSpacesIntegration(self, organizationId: str):
        """
        **Remove the Spaces integration from Meraki**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-spaces-integration

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["spaces", "configure", "integration"],
            "operation": "removeOrganizationSpacesIntegration",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/spaces/integration/remove"

        return self._session.post(metadata, resource)

    def getOrganizationSpacesSitesBuildings(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the buildings belonging to the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-sites-buildings

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter buildings by one or more network IDs. This filter uses multiple exact matches. Maximum 100 network IDs.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["spaces", "configure", "sites", "buildings"],
            "operation": "getOrganizationSpacesSitesBuildings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/spaces/sites/buildings"

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
                self._session._logger.warning(f"getOrganizationSpacesSitesBuildings: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationSpacesSitesOverview(self, organizationId: str, **kwargs):
        """
        **Get point-in-time overview statistics for buildings, floors, maps, and wireless device placement**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-spaces-sites-overview

        - organizationId (string): Organization ID
        - networkIds (array): Optional parameter to filter statistics by one or more network IDs. This filter uses multiple exact matches. Maximum 100 network IDs.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["spaces", "monitor", "sites", "overview"],
            "operation": "getOrganizationSpacesSitesOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/spaces/sites/overview"

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
                self._session._logger.warning(f"getOrganizationSpacesSitesOverview: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)
