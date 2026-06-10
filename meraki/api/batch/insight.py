import urllib


class ActionBatchInsight(object):
    def __init__(self):
        super(ActionBatchInsight, self).__init__()

    def createOrganizationInsightApplication(self, organizationId: str, counterSetRuleId: int, **kwargs):
        """
        **Add an Insight tracked application**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-application

        - organizationId (string): Organization ID
        - counterSetRuleId (integer): The id of the counter set rule
        - enableSmartThresholds (boolean): Enable Smart Thresholds
        - thresholds (object): Thresholds defined by a user for each application
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications"

        body_params = [
            "counterSetRuleId",
            "enableSmartThresholds",
            "thresholds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationInsightApplication(self, organizationId: str, applicationId: str, **kwargs):
        """
        **Update an Insight tracked application**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-application

        - organizationId (string): Organization ID
        - applicationId (string): Application ID
        - enableSmartThresholds (boolean): Enable Smart Thresholds
        - thresholds (object): Thresholds defined by a user for each application
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        applicationId = urllib.parse.quote(str(applicationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications/{applicationId}"

        body_params = [
            "enableSmartThresholds",
            "thresholds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationInsightApplication(self, organizationId: str, applicationId: str):
        """
        **Delete an Insight tracked application**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-application

        - organizationId (string): Organization ID
        - applicationId (string): Application ID
        """

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        applicationId = urllib.parse.quote(str(applicationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications/{applicationId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationInsightMonitoredMediaServer(self, organizationId: str, name: str, address: str, **kwargs):
        """
        **Add a media server to be monitored for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str, **kwargs):
        """
        **Update a monitored media server for this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        monitoredMediaServerId = urllib.parse.quote(str(monitoredMediaServerId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Delete a monitored media server from this organization. Only valid for organizations with Meraki Insight.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        """

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        monitoredMediaServerId = urllib.parse.quote(str(monitoredMediaServerId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationInsightWebApp(self, organizationId: str, name: str, hostname: str, **kwargs):
        """
        **Add a custom web application for Insight to be able to track**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-web-app

        - organizationId (string): Organization ID
        - name (string): The name of the Web Application
        - hostname (string): The hostname of Web Application
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps"

        body_params = [
            "name",
            "hostname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationInsightWebApp(self, organizationId: str, customCounterSetRuleId: str, **kwargs):
        """
        **Update a custom web application for Insight to be able to track**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-web-app

        - organizationId (string): Organization ID
        - customCounterSetRuleId (string): Custom counter set rule ID
        - name (string): The name of the Web Application
        - hostname (string): The hostname of Web Application
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        customCounterSetRuleId = urllib.parse.quote(str(customCounterSetRuleId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps/{customCounterSetRuleId}"

        body_params = [
            "name",
            "hostname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationInsightWebApp(self, organizationId: str, customCounterSetRuleId: str):
        """
        **Delete a custom web application by counter set rule id.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-web-app

        - organizationId (string): Organization ID
        - customCounterSetRuleId (string): Custom counter set rule ID
        """

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        customCounterSetRuleId = urllib.parse.quote(str(customCounterSetRuleId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps/{customCounterSetRuleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
