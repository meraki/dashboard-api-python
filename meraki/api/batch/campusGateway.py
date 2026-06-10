import urllib


class ActionBatchCampusGateway(object):
    def __init__(self):
        super(ActionBatchCampusGateway, self).__init__()

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
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

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
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetworkCampusGatewayCluster(self, networkId: str, clusterId: str):
        """
        **Delete a cluster**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-campus-gateway-cluster

        - networkId (string): Network ID
        - clusterId (string): Cluster ID
        """

        networkId = urllib.parse.quote(str(networkId), safe="")
        clusterId = urllib.parse.quote(str(clusterId), safe="")
        resource = f"/networks/{networkId}/campusGateway/clusters/{clusterId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

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

        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/campusGateway/ssids/{number}/mdns"

        body_params = [
            "enabled",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

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
        action = {
            "resource": resource,
            "operation": "provision",
            "body": payload,
        }
        return action

    def batchOrganizationCampusGatewayClustersTunnelingByClusterByNetworkUpdate(self, organizationId: str, **kwargs):
        """
        **Update MCG cluster-network tunnel settings for multiple networks**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-campus-gateway-clusters-tunneling-by-cluster-by-network-update

        - organizationId (string): Organization ID
        - items (array): MCG cluster-network tunnel settings
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/campusGateway/clusters/tunneling/byCluster/byNetwork/batchUpdate"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "batch_update",
            "body": payload,
        }
        return action
