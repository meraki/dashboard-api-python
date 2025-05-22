import urllib


class ActionBatchCampusGateway(object):
    def __init__(self):
        super(ActionBatchCampusGateway, self).__init__()
        


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
        resource = f'/networks/{networkId}/campusGateway/clusters'

        body_params = ['name', 'uplinks', 'tunnels', 'nameservers', 'portChannels', 'devices', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
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

        metadata = {
            'tags': ['campusGateway', 'configure', 'clusters'],
            'operation': 'updateNetworkCampusGatewayCluster'
        }
        resource = f'/networks/{networkId}/campusGateway/clusters/{clusterId}'

        body_params = ['name', 'uplinks', 'tunnels', 'nameservers', 'portChannels', 'devices', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        



