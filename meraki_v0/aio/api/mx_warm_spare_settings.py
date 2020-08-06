class AsyncMXWarmSpareSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def swapNetworkWarmSpare(self, networkId: str):
        """
        **Swap MX primary and warm spare appliances**
        https://developer.cisco.com/meraki/api/#!swap-network-warm-spare
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX warm spare settings'],
            'operation': 'swapNetworkWarmSpare',
        }
        resource = f'/networks/{networkId}/swapWarmSpare'

        return await self._session.post(metadata, resource)

    async def getNetworkWarmSpareSettings(self, networkId: str):
        """
        **Return MX warm spare settings**
        https://developer.cisco.com/meraki/api/#!get-network-warm-spare-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX warm spare settings'],
            'operation': 'getNetworkWarmSpareSettings',
        }
        resource = f'/networks/{networkId}/warmSpareSettings'

        return await self._session.get(metadata, resource)

    async def updateNetworkWarmSpareSettings(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update MX warm spare settings**
        https://developer.cisco.com/meraki/api/#!update-network-warm-spare-settings
        
        - networkId (string)
        - enabled (boolean): Enable warm spare
        - spareSerial (string): Serial number of the warm spare appliance
        - uplinkMode (string): Uplink mode, either virtual or public
        - virtualIp1 (string): The WAN 1 shared IP
        - virtualIp2 (string): The WAN 2 shared IP
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX warm spare settings'],
            'operation': 'updateNetworkWarmSpareSettings',
        }
        resource = f'/networks/{networkId}/warmSpareSettings'

        body_params = ['enabled', 'spareSerial', 'uplinkMode', 'virtualIp1', 'virtualIp2']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

