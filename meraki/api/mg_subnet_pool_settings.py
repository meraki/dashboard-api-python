class MGSubnetPoolSettings(object):
    def __init__(self, session):
        super(MGSubnetPoolSettings, self).__init__()
        self._session = session
    
    def getNetworkCellularGatewaySettingsSubnetPool(self, networkId: str):
        """
        **Return the subnet pool and mask configured for MGs in the network.**
        https://api.meraki.com/api_docs#return-the-subnet-pool-and-mask-configured-for-mgs-in-the-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MG subnet pool settings'],
            'operation': 'getNetworkCellularGatewaySettingsSubnetPool',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/subnetPool'

        return self._session.get(metadata, resource)

    def updateNetworkCellularGatewaySettingsSubnetPool(self, networkId: str, **kwargs):
        """
        **Update the subnet pool and mask configuration for MGs in the network.**
        https://api.meraki.com/api_docs#update-the-subnet-pool-and-mask-configuration-for-mgs-in-the-network
        
        - networkId (string)
        - mask (integer): Mask used for the subnet of all MGs in  this network.
        - cidr (string): CIDR of the pool of subnets. Each MG in this network will automatically pick a subnet from this pool.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG subnet pool settings'],
            'operation': 'updateNetworkCellularGatewaySettingsSubnetPool',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/subnetPool'

        body_params = ['mask', 'cidr']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

