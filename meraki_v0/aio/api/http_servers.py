class AsyncHTTPServers:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkHttpServers(self, networkId: str):
        """
        **List the HTTP servers for a network**
        https://developer.cisco.com/meraki/api/#!get-network-http-servers
        
        - networkId (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'getNetworkHttpServers',
        }
        resource = f'/networks/{networkId}/httpServers'

        return await self._session.get(metadata, resource)

    async def createNetworkHttpServer(self, networkId: str, name: str, url: str, **kwargs):
        """
        **Add an HTTP server to a network**
        https://developer.cisco.com/meraki/api/#!create-network-http-server
        
        - networkId (string)
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'createNetworkHttpServer',
        }
        resource = f'/networks/{networkId}/httpServers'

        body_params = ['name', 'url', 'sharedSecret']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def createNetworkHttpServersWebhookTest(self, networkId: str, url: str, **kwargs):
        """
        **Send a test webhook for a network**
        https://developer.cisco.com/meraki/api/#!create-network-http-servers-webhook-test
        
        - networkId (string)
        - url (string): The URL where the test webhook will be sent
        - sharedSecret (string): The shared secret the test webhook will send. Optional. Defaults to an empty string.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'createNetworkHttpServersWebhookTest',
        }
        resource = f'/networks/{networkId}/httpServers/webhookTests'

        body_params = ['url', 'sharedSecret']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkHttpServersWebhookTest(self, networkId: str, id: str):
        """
        **Return the status of a webhook test for a network**
        https://developer.cisco.com/meraki/api/#!get-network-http-servers-webhook-test
        
        - networkId (string)
        - id (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'getNetworkHttpServersWebhookTest',
        }
        resource = f'/networks/{networkId}/httpServers/webhookTests/{id}'

        return await self._session.get(metadata, resource)

    async def getNetworkHttpServer(self, networkId: str, id: str):
        """
        **Return an HTTP server for a network**
        https://developer.cisco.com/meraki/api/#!get-network-http-server
        
        - networkId (string)
        - id (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'getNetworkHttpServer',
        }
        resource = f'/networks/{networkId}/httpServers/{id}'

        return await self._session.get(metadata, resource)

    async def updateNetworkHttpServer(self, networkId: str, id: str, **kwargs):
        """
        **Update an HTTP server**
        https://developer.cisco.com/meraki/api/#!update-network-http-server
        
        - networkId (string)
        - id (string)
        - name (string): A name for easy reference to the HTTP server
        - url (string): The URL of the HTTP server
        - sharedSecret (string): A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'updateNetworkHttpServer',
        }
        resource = f'/networks/{networkId}/httpServers/{id}'

        body_params = ['name', 'url', 'sharedSecret']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteNetworkHttpServer(self, networkId: str, id: str):
        """
        **Delete an HTTP server from a network**
        https://developer.cisco.com/meraki/api/#!delete-network-http-server
        
        - networkId (string)
        - id (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'deleteNetworkHttpServer',
        }
        resource = f'/networks/{networkId}/httpServers/{id}'

        return await self._session.delete(metadata, resource)

