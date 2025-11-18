import urllib


class CampusGateway(object):
    def __init__(self, session):
        super(CampusGateway, self).__init__()
        self._session = session
        


    def createNetworkCampusGatewayCluster(self, networkId: str, name: str, uplinks: list, tunnels: list, nameservers: dict, portChannels: list, **kwargs):
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
            'tags': ['campusGateway', 'configure', 'clusters'],
            'operation': 'createNetworkCampusGatewayCluster'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/campusGateway/clusters'

        body_params = ['name', 'uplinks', 'tunnels', 'nameservers', 'portChannels', 'devices', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

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
            'tags': ['campusGateway', 'configure', 'clusters'],
            'operation': 'updateNetworkCampusGatewayCluster'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        clusterId = urllib.parse.quote(str(clusterId), safe='')
        resource = f'/networks/{networkId}/campusGateway/clusters/{clusterId}'

        body_params = ['name', 'uplinks', 'tunnels', 'nameservers', 'portChannels', 'devices', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationCampusGatewayDevicesUplinksLocalOverridesByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
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
            'tags': ['campusGateway', 'configure', 'devices', 'uplinks', 'localOverrides', 'byDevice'],
            'operation': 'getOrganizationCampusGatewayDevicesUplinksLocalOverridesByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/campusGateway/devices/uplinks/localOverrides/byDevice'

        query_params = ['serials', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
