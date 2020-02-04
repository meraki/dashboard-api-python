class AsyncMonitoredMediaServers:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationInsightMonitoredMediaServers(self, organizationId: str):
        """
        **List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.**
        https://api.meraki.com/api_docs#list-the-monitored-media-servers-for-this-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'getOrganizationInsightMonitoredMediaServers',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers'

        return await self._session.get(metadata, resource)

    async def createOrganizationInsightMonitoredMediaServer(self, organizationId: str, name: str, address: str):
        """
        **Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.**
        https://api.meraki.com/api_docs#add-a-media-server-to-be-monitored-for-this-organization
        
        - organizationId (string)
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        """

        kwargs = locals()

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'createOrganizationInsightMonitoredMediaServer',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers'

        body_params = ['name', 'address']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.**
        https://api.meraki.com/api_docs#return-a-monitored-media-server-for-this-organization
        
        - organizationId (string)
        - monitoredMediaServerId (string)
        """

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'getOrganizationInsightMonitoredMediaServer',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        return await self._session.get(metadata, resource)

    async def updateOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str, **kwargs):
        """
        **Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.**
        https://api.meraki.com/api_docs#update-a-monitored-media-server-for-this-organization
        
        - organizationId (string)
        - monitoredMediaServerId (string)
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'updateOrganizationInsightMonitoredMediaServer',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        body_params = ['name', 'address']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.**
        https://api.meraki.com/api_docs#delete-a-monitored-media-server-from-this-organization
        
        - organizationId (string)
        - monitoredMediaServerId (string)
        """

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'deleteOrganizationInsightMonitoredMediaServer',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        return await self._session.delete(metadata, resource)

