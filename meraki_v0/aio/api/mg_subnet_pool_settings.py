class AsyncMGSubnetPoolSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkCellularGatewaySettingsSubnetPool(self, networkId: str):
        """
        **Return the subnet pool and mask configured for MGs in the network.**
        https://developer.cisco.com/meraki/api/#!get-network-cellular-gateway-settings-subnet-pool
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MG subnet pool settings'],
            'operation': 'getNetworkCellularGatewaySettingsSubnetPool',
        }
        resource = f'/networks/{networkId}/cellularGateway/settings/subnetPool'

        return await self._session.get(metadata, resource)

    async def updateNetworkCellularGatewaySettingsSubnetPool(self, networkId: str, **kwargs):
        """
        **Update the subnet pool and mask configuration for MGs in the network.**
        https://developer.cisco.com/meraki/api/#!update-network-cellular-gateway-settings-subnet-pool
        
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
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

