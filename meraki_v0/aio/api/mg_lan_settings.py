class AsyncMGLANSettings:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getDeviceCellularGatewaySettings(self, serial: str):
        """
        **Show the LAN Settings of a MG**
        https://developer.cisco.com/meraki/api/#!get-device-cellular-gateway-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['MG LAN settings'],
            'operation': 'getDeviceCellularGatewaySettings',
        }
        resource = f'/devices/{serial}/cellularGateway/settings'

        return await self._session.get(metadata, resource)

    async def updateDeviceCellularGatewaySettings(self, serial: str, **kwargs):
        """
        **Update the LAN Settings for a single MG.**
        https://developer.cisco.com/meraki/api/#!update-device-cellular-gateway-settings
        
        - serial (string)
        - reservedIpRanges (array): list of all reserved IP ranges for a single MG
        - fixedIpAssignments (array): list of all fixed IP assignments for a single MG
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG LAN settings'],
            'operation': 'updateDeviceCellularGatewaySettings',
        }
        resource = f'/devices/{serial}/cellularGateway/settings'

        body_params = ['reservedIpRanges', 'fixedIpAssignments']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

