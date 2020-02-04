class AsyncMXStaticRoutes:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkStaticRoutes(self, networkId: str):
        """
        **List the static routes for an MX or teleworker network**
        https://api.meraki.com/api_docs#list-the-static-routes-for-an-mx-or-teleworker-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'getNetworkStaticRoutes',
        }
        resource = f'/networks/{networkId}/staticRoutes'

        return await self._session.get(metadata, resource)

    async def createNetworkStaticRoute(self, networkId: str, **kwargs):
        """
        **Add a static route for an MX or teleworker network**
        https://api.meraki.com/api_docs#add-a-static-route-for-an-mx-or-teleworker-network
        
        - networkId (string)
        - name (string): The name of the new static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'createNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes'

        body_params = ['name', 'subnet', 'gatewayIp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkStaticRoute(self, networkId: str, srId: str):
        """
        **Return a static route for an MX or teleworker network**
        https://api.meraki.com/api_docs#return-a-static-route-for-an-mx-or-teleworker-network
        
        - networkId (string)
        - srId (string)
        """

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'getNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes/{srId}'

        return await self._session.get(metadata, resource)

    async def updateNetworkStaticRoute(self, networkId: str, srId: str, **kwargs):
        """
        **Update a static route for an MX or teleworker network**
        https://api.meraki.com/api_docs#update-a-static-route-for-an-mx-or-teleworker-network
        
        - networkId (string)
        - srId (string)
        - name (string): The name of the static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        - enabled (string): The enabled state of the static route
        - fixedIpAssignments (string): The DHCP fixed IP assignments on the static route
        - reservedIpRanges (string): The DHCP reserved IP ranges on the static route
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'updateNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes/{srId}'

        body_params = ['name', 'subnet', 'gatewayIp', 'enabled', 'fixedIpAssignments', 'reservedIpRanges']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteNetworkStaticRoute(self, networkId: str, srId: str):
        """
        **Delete a static route from an MX or teleworker network**
        https://api.meraki.com/api_docs#delete-a-static-route-from-an-mx-or-teleworker-network
        
        - networkId (string)
        - srId (string)
        """

        metadata = {
            'tags': ['MX static routes'],
            'operation': 'deleteNetworkStaticRoute',
        }
        resource = f'/networks/{networkId}/staticRoutes/{srId}'

        return await self._session.delete(metadata, resource)

