class ActionBatchInsight(object):
    def __init__(self):
        super(ActionBatchInsight, self).__init__()
        


    def createOrganizationInsightMonitoredMediaServer(self, organizationId: str, name: str, address: str, **kwargs):
        """
        **Add a media server to be monitored for this organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        - organizationId (string): (required)
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'createOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers'

        body_params = ['name', 'address', 'bestEffortMonitoringEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str, **kwargs):
        """
        **Update a monitored media server for this organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        - organizationId (string): (required)
        - monitoredMediaServerId (string): (required)
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'updateOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        body_params = ['name', 'address', 'bestEffortMonitoringEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Delete a monitored media server from this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

        - organizationId (string): (required)
        - monitoredMediaServerId (string): (required)
        """

        metadata = {
            'tags': ['insight', 'configure', 'monitoredMediaServers'],
            'operation': 'deleteOrganizationInsightMonitoredMediaServer'
        }
        resource = f'/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        



