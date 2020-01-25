class HTTPServers(object):
    def __init__(self, session):
        super(HTTPServers, self).__init__()
        self._session = session
    
    def getNetworkHttpServers(self, networkId: str):
        """
        **List the HTTP servers for a network**
        https://api.meraki.com/api_docs#list-the-http-servers-for-a-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'getNetworkHttpServers',
        }
        resource = f'/networks/{networkId}/httpServers'

        return self._session.get(metadata, resource)

    def createNetworkHttpServer(self, networkId: str, name: str, url: str, **kwargs):
        """
        **Add an HTTP server to a network**
        https://api.meraki.com/api_docs#add-an-http-server-to-a-network
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def createNetworkHttpServersWebhookTest(self, networkId: str, url: str):
        """
        **Send a test webhook for a network**
        https://api.meraki.com/api_docs#send-a-test-webhook-for-a-network
        
        - networkId (string)
        - url (string): The URL where the test webhook will be sent
        """

        kwargs = locals()

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'createNetworkHttpServersWebhookTest',
        }
        resource = f'/networks/{networkId}/httpServers/webhookTests'

        body_params = ['url']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkHttpServersWebhookTest(self, networkId: str, id: str):
        """
        **Return the status of a webhook test for a network**
        https://api.meraki.com/api_docs#return-the-status-of-a-webhook-test-for-a-network
        
        - networkId (string)
        - id (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'getNetworkHttpServersWebhookTest',
        }
        resource = f'/networks/{networkId}/httpServers/webhookTests/{id}'

        return self._session.get(metadata, resource)

    def getNetworkHttpServer(self, networkId: str, id: str):
        """
        **Return an HTTP server for a network**
        https://api.meraki.com/api_docs#return-an-http-server-for-a-network
        
        - networkId (string)
        - id (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'getNetworkHttpServer',
        }
        resource = f'/networks/{networkId}/httpServers/{id}'

        return self._session.get(metadata, resource)

    def updateNetworkHttpServer(self, networkId: str, id: str, **kwargs):
        """
        **Update an HTTP server**
        https://api.meraki.com/api_docs#update-an-http-server
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkHttpServer(self, networkId: str, id: str):
        """
        **Delete an HTTP server from a network**
        https://api.meraki.com/api_docs#delete-an-http-server-from-a-network
        
        - networkId (string)
        - id (string)
        """

        metadata = {
            'tags': ['HTTP servers'],
            'operation': 'deleteNetworkHttpServer',
        }
        resource = f'/networks/{networkId}/httpServers/{id}'

        return self._session.delete(metadata, resource)

