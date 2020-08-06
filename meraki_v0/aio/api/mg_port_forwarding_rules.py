class AsyncMGPortForwardingRules:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getDeviceCellularGatewaySettingsPortForwardingRules(self, serial: str):
        """
        **Returns the port forwarding rules for a single MG.**
        https://developer.cisco.com/meraki/api/#!get-device-cellular-gateway-settings-port-forwarding-rules
        
        - serial (string)
        """

        metadata = {
            'tags': ['MG port forwarding rules'],
            'operation': 'getDeviceCellularGatewaySettingsPortForwardingRules',
        }
        resource = f'/devices/{serial}/cellularGateway/settings/portForwardingRules'

        return await self._session.get(metadata, resource)

    async def updateDeviceCellularGatewaySettingsPortForwardingRules(self, serial: str, **kwargs):
        """
        **Updates the port forwarding rules for a single MG.**
        https://developer.cisco.com/meraki/api/#!update-device-cellular-gateway-settings-port-forwarding-rules
        
        - serial (string)
        - rules (array): An array of port forwarding params
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG port forwarding rules'],
            'operation': 'updateDeviceCellularGatewaySettingsPortForwardingRules',
        }
        resource = f'/devices/{serial}/cellularGateway/settings/portForwardingRules'

        body_params = ['rules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

