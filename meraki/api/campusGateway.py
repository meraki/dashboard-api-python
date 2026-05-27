import urllib


class CampusGateway(object):
    def __init__(self, session):
        super(CampusGateway, self).__init__()
        self._session = session

    def createNetworkCampusGatewayCluster(
        self, networkId: str, name: str, uplinks: list, tunnels: list, nameservers: dict, portChannels: list, **kwargs
    ):
        """
        **Create a cluster and add campus gateways to it**
        https://developer.cisco.com/meraki/api-v1/#!create-network-campus-gateway-cluster

        - networkId (string): Network ID
        - name (string): Name of the new cluster
        - uplinks (array): Uplink interface settings of the cluster
        - tunnels (array): Tunnel interface settings of the cluster: Reuse uplink or specify tunnel interface
        - nameservers (object): Nameservers of the cluster
        - portChannels (array): Port channel settings of the cluster
        - devices (array): Devices to be added to the cluster
        - notes (string): Notes about cluster with max size of 511 characters allowed
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "createNetworkCampusGatewayCluster",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/campusGateway/clusters"

        body_params = [
            "name",
            "uplinks",
            "tunnels",
            "nameservers",
            "portChannels",
            "devices",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkCampusGatewayCluster: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateNetworkCampusGatewayCluster(self, networkId: str, clusterId: str, **kwargs):
        """
        **Update a cluster and add/remove campus gateways to/from it**
        https://developer.cisco.com/meraki/api-v1/#!update-network-campus-gateway-cluster

        - networkId (string): Network ID
        - clusterId (string): Cluster ID
        - name (string): Name of the cluster
        - uplinks (array): Uplink interface settings of the cluster
        - tunnels (array): Tunnel interface settings of the cluster: Reuse uplink or specify tunnel interface
        - nameservers (object): Nameservers of the cluster
        - portChannels (array): Port channel settings of the cluster
        - devices (array): Devices in the cluster
        - notes (string): Notes about cluster with max size of 511 characters allowed
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "updateNetworkCampusGatewayCluster",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clusterId = urllib.parse.quote(str(clusterId), safe="")
        resource = f"/networks/{networkId}/campusGateway/clusters/{clusterId}"

        body_params = [
            "name",
            "uplinks",
            "tunnels",
            "nameservers",
            "portChannels",
            "devices",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkCampusGatewayCluster: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkCampusGatewayCluster(self, networkId: str, clusterId: str):
        """
        **Delete a cluster**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-campus-gateway-cluster

        - networkId (string): Network ID
        - clusterId (string): Cluster ID
        """

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "deleteNetworkCampusGatewayCluster",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clusterId = urllib.parse.quote(str(clusterId), safe="")
        resource = f"/networks/{networkId}/campusGateway/clusters/{clusterId}"

        return self._session.delete(metadata, resource)

    def getNetworkCampusGatewaySsidMdns(self, networkId: str, number: str):
        """
        **List the currently configured mDNS settings for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-campus-gateway-ssid-mdns

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["campusGateway", "configure", "ssids", "mdns"],
            "operation": "getNetworkCampusGatewaySsidMdns",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/campusGateway/ssids/{number}/mdns"

        return self._session.get(metadata, resource)

    def updateNetworkCampusGatewaySsidMdns(self, networkId: str, number: str, **kwargs):
        """
        **Update the mDNS gateway settings and rules for a SSID and cluster**
        https://developer.cisco.com/meraki/api-v1/#!update-network-campus-gateway-ssid-mdns

        - networkId (string): Network ID
        - number (string): Number
        - enabled (boolean): If true, mDNS gateway is enabled for this SSID and cluster.
        - rules (array): List of mDNS forwarding rules.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "ssids", "mdns"],
            "operation": "updateNetworkCampusGatewaySsidMdns",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/campusGateway/ssids/{number}/mdns"

        body_params = [
            "enabled",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkCampusGatewaySsidMdns: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationCampusGatewayClientsUsageByNetworkByCluster(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns client usage details for campus gateway clusters within an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clients-usage-by-network-by-cluster

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 1 hour and be less than or equal to 7 days. The default is 2 hours.
        - networkIds (array): Filter results by a list of network IDs.
        - networkGroupIds (array): Limit the results to clients that belong to one of the provided network groups.
        - clusterIds (array): Filter results by a list of cluster IDs.
        - usageUnits (string): Usage units to use in the response.
        """

        kwargs.update(locals())

        if "usageUnits" in kwargs:
            options = ["GB", "KB", "MB", "TB"]
            assert kwargs["usageUnits"] in options, (
                f'''"usageUnits" cannot be "{kwargs["usageUnits"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["campusGateway", "monitor", "clients", "usage", "byNetwork", "byCluster"],
            "operation": "getOrganizationCampusGatewayClientsUsageByNetworkByCluster",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clients/usage/byNetwork/byCluster"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "networkGroupIds",
            "clusterIds",
            "usageUnits",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "networkGroupIds",
            "clusterIds",
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
                    f"getOrganizationCampusGatewayClientsUsageByNetworkByCluster: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationCampusGatewayClusters(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get the details of campus gateway clusters**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Networks for which information should be gathered.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "getOrganizationCampusGatewayClusters",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters"

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
                self._session._logger.warning(f"getOrganizationCampusGatewayClusters: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationCampusGatewayClustersFailoverTargets(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the details of a Failover Targets for a Campus Gateway cluster**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters-failover-targets

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter networks. This filter uses multiple exact matches.
        - clusterIds (array): Optional parameter to filter clusters. This filter uses multiple exact matches.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters", "failover", "targets"],
            "operation": "getOrganizationCampusGatewayClustersFailoverTargets",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/failover/targets"

        query_params = [
            "networkIds",
            "clusterIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "clusterIds",
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
                    f"getOrganizationCampusGatewayClustersFailoverTargets: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationCampusGatewayClustersFailoverTargetsByCluster(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Get available backup cluster targets for campus gateway failover configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters-failover-targets-by-cluster

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Networks for which backup cluster targets should be gathered.
        - clusterIds (array): Cluster IDs to filter backup cluster targets.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters", "failover", "targets", "byCluster"],
            "operation": "getOrganizationCampusGatewayClustersFailoverTargetsByCluster",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/failover/targets/byCluster"

        query_params = [
            "networkIds",
            "clusterIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "clusterIds",
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
                    f"getOrganizationCampusGatewayClustersFailoverTargetsByCluster: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationCampusGatewayClustersNetworksOverviews(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List networks tunneling through Campus Gateway clusters with their AP, ssids and client counts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters-networks-overviews

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - clusterIds (array): Optional parameter to filter by MCG cluster IDs. This filter uses multiple exact matches.
        - siteIds (array): Optional parameter to filter by site IDs. This filter uses multiple exact matches.
        - networkIds (array): Optional parameter to filter networks. This filter uses multiple exact matches.
        - tunnelingSources (array): Optional parameter to filter networks by tunneling source. 'configured' returns networks explicitly set up to tunnel through the campus gateway. 'roaming' returns networks tunneling due to AP roaming or disaster recovery. 'roaming' is only effective when 'clusterIds' is also provided; without 'clusterIds', the filter defaults to configured-only behavior. Defaults to 'configured' if omitted.
        - search (string): Optional parameter to filter networks by wireless network name. This filter uses case-insensitive substring matching.
        - sortBy (string): Optional parameter to sort results. Default is 'name'. Use 'siteName' to sort by site name.
        - sortOrder (string): Optional parameter to specify sort direction. Default is 'asc'.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["clients", "clusterId", "connections", "name", "networkId", "siteName", "ssids"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["campusGateway", "configure", "clusters", "networks", "overviews"],
            "operation": "getOrganizationCampusGatewayClustersNetworksOverviews",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/networks/overviews"

        query_params = [
            "clusterIds",
            "siteIds",
            "networkIds",
            "tunnelingSources",
            "search",
            "sortBy",
            "sortOrder",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "clusterIds",
            "siteIds",
            "networkIds",
            "tunnelingSources",
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
                    f"getOrganizationCampusGatewayClustersNetworksOverviews: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def provisionOrganizationCampusGatewayClusters(
        self,
        organizationId: str,
        clusterId: str,
        network: dict,
        name: str,
        uplinks: list,
        tunnels: list,
        nameservers: dict,
        portChannels: list,
        **kwargs,
    ):
        """
        **Provisions a cluster,adds campus gateways to it and associate/dissociate failover targets.**
        https://developer.cisco.com/meraki/api-v1/#!provision-organization-campus-gateway-clusters

        - organizationId (string): Organization ID
        - clusterId (string): ID of the cluster to be provisioned
        - network (object): Network to be provisioned
        - name (string): Name of the new cluster
        - uplinks (array): Uplink interface settings of the cluster
        - tunnels (array): Tunnel interface settings of the cluster: Reuse uplink or specify tunnel interface
        - nameservers (object): Nameservers of the cluster
        - portChannels (array): Port channel settings of the cluster
        - devices (array): Devices to be added to the cluster
        - failover (object): Failover targets for the cluster
        - notes (string): Notes about cluster with max size of 511 characters allowed
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters"],
            "operation": "provisionOrganizationCampusGatewayClusters",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/provision"

        body_params = [
            "clusterId",
            "network",
            "name",
            "uplinks",
            "tunnels",
            "nameservers",
            "portChannels",
            "devices",
            "failover",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"provisionOrganizationCampusGatewayClusters: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationCampusGatewayClustersSsids(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List SSIDs tunneling through Campus Gateway clusters**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters-ssids

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - clusterIds (array): Optional parameter to filter by MCG cluster IDs. This filter uses multiple exact matches.
        - networkIds (array): Optional parameter to filter networks. This filter uses multiple exact matches.
        - search (string): Optional parameter to filter SSIDs by name. This filter uses case-insensitive starts with string matching.
        - sortBy (string): Optional parameter to sort results. Default is 'networkId'.
        - sortOrder (string): Optional parameter to specify sort direction. Default is 'asc'.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["clusterId", "name", "networkId", "ssidId"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["campusGateway", "configure", "clusters", "ssids"],
            "operation": "getOrganizationCampusGatewayClustersSsids",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/ssids"

        query_params = [
            "clusterIds",
            "networkIds",
            "search",
            "sortBy",
            "sortOrder",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "clusterIds",
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
                    f"getOrganizationCampusGatewayClustersSsids: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationCampusGatewayClustersTunnelingByClusterByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List all the MCG cluster-network tunnel settings**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-clusters-tunneling-by-cluster-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - clusterIds (array): Optional parameter to filter MCG clusters. This filter uses multiple exact matches
        - dataEncryptionEnabled (boolean): Optional parameter to filter cluster-network tunnel settings by data encryption configuration
        - networkIds (array): Optional parameter to filter networks. This filter uses multiple exact matches
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters", "tunneling", "byCluster", "byNetwork"],
            "operation": "getOrganizationCampusGatewayClustersTunnelingByClusterByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/tunneling/byCluster/byNetwork"

        query_params = [
            "clusterIds",
            "dataEncryptionEnabled",
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "clusterIds",
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
                    f"getOrganizationCampusGatewayClustersTunnelingByClusterByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def batchOrganizationCampusGatewayClustersTunnelingByClusterByNetworkUpdate(self, organizationId: str, **kwargs):
        """
        **Update MCG cluster-network tunnel settings for multiple networks**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-campus-gateway-clusters-tunneling-by-cluster-by-network-update

        - organizationId (string): Organization ID
        - items (array): MCG cluster-network tunnel settings
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "clusters", "tunneling", "byCluster", "byNetwork"],
            "operation": "batchOrganizationCampusGatewayClustersTunnelingByClusterByNetworkUpdate",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/tunneling/byCluster/byNetwork/batchUpdate"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"batchOrganizationCampusGatewayClustersTunnelingByClusterByNetworkUpdate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationCampusGatewayConnections(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the details of APs tunneling through the Campus Gateway clusters**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-connections

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter networks. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter connections(APs) by its own serials. This filter uses multiple exact matches.
        - campusGatewaySerials (array): Optional parameter to filter connections(APs) by MCG serials. This filter uses multiple exact matches.
        - campusGatewayClusterIds (array): Optional parameter to filter connections(APs) by MCG cluster IDs. This filter uses multiple exact matches.
        - campusGatewayTunnelStatuses (array): Optional parameter to filter connections(APs) by tunnel statuses. This filter uses multiple exact matches.
        - search (string): Optional parameter to filter connections(APs) on AP name, serial, MAC address, network name, or interface IP address. This filter uses partial string matching (ILIKE).
        - models (array): Optional parameter to filter connections(APs) by device model names. This filter uses multiple exact matches.
        - dataEncryptionStatuses (array): Optional parameter to filter connections(APs) by data encryption status. This filter uses multiple exact matches.
        - sortBy (string): Optional parameter to sort results. Available options: name, serial, status, interfaces, clients, dataEncryption, networkName. Default is 'serial'.
        - sortOrder (string): Optional parameter to specify sort direction. Default is 'asc'.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["clients", "dataEncryption", "interfaces", "name", "networkName", "serial", "status"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["campusGateway", "configure", "connections"],
            "operation": "getOrganizationCampusGatewayConnections",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/connections"

        query_params = [
            "networkIds",
            "serials",
            "campusGatewaySerials",
            "campusGatewayClusterIds",
            "campusGatewayTunnelStatuses",
            "search",
            "models",
            "dataEncryptionStatuses",
            "sortBy",
            "sortOrder",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "campusGatewaySerials",
            "campusGatewayClusterIds",
            "campusGatewayTunnelStatuses",
            "models",
            "dataEncryptionStatuses",
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
                    f"getOrganizationCampusGatewayConnections: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationCampusGatewayConnectionsOverview(self, organizationId: str, **kwargs):
        """
        **List the count of connections(APs) with tunneling status up and down through the Campus Gateway clusters**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-connections-overview

        - organizationId (string): Organization ID
        - networkIds (array): Optional parameter to filter networks. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter connections(APs) by its own serials. This filter uses multiple exact matches.
        - campusGatewaySerials (array): Optional parameter to filter connections(APs) by Campus Gateway serials. This filter uses multiple exact matches.
        - campusGatewayClusterIds (array): Optional parameter to filter connections(APs) by Campus Gateway cluster IDs. This filter uses multiple exact matches.
        - campusGatewayTunnelStatuses (array): Optional parameter to filter connections(APs) by tunnel statuses. This filter uses multiple exact matches.
        - search (string): Optional setting that lets you filter access points (APs) by name, serial number, MAC address, network name, or interface IP address. The filter matches partial text, not just exact values (uses ILIKE matching).
        - models (array): Optional parameter to filter connections(APs) by device model names. This filter uses multiple exact matches.
        - dataEncryptionStatuses (array): Optional parameter to filter connections(APs) by data encryption status. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "connections", "overview"],
            "operation": "getOrganizationCampusGatewayConnectionsOverview",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/connections/overview"

        query_params = [
            "networkIds",
            "serials",
            "campusGatewaySerials",
            "campusGatewayClusterIds",
            "campusGatewayTunnelStatuses",
            "search",
            "models",
            "dataEncryptionStatuses",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "campusGatewaySerials",
            "campusGatewayClusterIds",
            "campusGatewayTunnelStatuses",
            "models",
            "dataEncryptionStatuses",
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
                    f"getOrganizationCampusGatewayConnectionsOverview: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationCampusGatewayDevicesUplinksLocalOverridesByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Uplink overrides configured locally on Campus Gateway devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-campus-gateway-devices-uplinks-local-overrides-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["campusGateway", "configure", "devices", "uplinks", "localOverrides", "byDevice"],
            "operation": "getOrganizationCampusGatewayDevicesUplinksLocalOverridesByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/devices/uplinks/localOverrides/byDevice"

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
                    f"getOrganizationCampusGatewayDevicesUplinksLocalOverridesByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
