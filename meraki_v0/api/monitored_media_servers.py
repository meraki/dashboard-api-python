class MonitoredMediaServers(object):
    def __init__(self, session):
        super(MonitoredMediaServers, self).__init__()
        self._session = session
    
    def getOrganizationInsightMonitoredMediaServers(self, organizationId: str):
        """
        **List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api/#!get-organization-insight-monitored-media-servers
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'getOrganizationInsightMonitoredMediaServers',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers'

        return self._session.get(metadata, resource)

    def createOrganizationInsightMonitoredMediaServer(self, organizationId: str, name: str, address: str):
        """
        **Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api/#!create-organization-insight-monitored-media-server
        
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
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api/#!get-organization-insight-monitored-media-server
        
        - organizationId (string)
        - monitoredMediaServerId (string)
        """

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'getOrganizationInsightMonitoredMediaServer',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        return self._session.get(metadata, resource)

    def updateOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str, **kwargs):
        """
        **Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api/#!update-organization-insight-monitored-media-server
        
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
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api/#!delete-organization-insight-monitored-media-server
        
        - organizationId (string)
        - monitoredMediaServerId (string)
        """

        metadata = {
            'tags': ['Monitored media servers'],
            'operation': 'deleteOrganizationInsightMonitoredMediaServer',
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        return self._session.delete(metadata, resource)

