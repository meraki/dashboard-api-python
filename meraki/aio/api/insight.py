import urllib


class AsyncInsight:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getNetworkInsightApplicationHealthByTime(self, networkId: str, applicationId: str, **kwargs):
        """
        **Get application health by time**
        https://developer.cisco.com/meraki/api-v1/#!get-network-insight-application-health-by-time

        - networkId (string): Network ID
        - applicationId (string): Application ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 3600, 86400. The default is 300.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "monitor", "applications", "healthByTime"],
            "operation": "getNetworkInsightApplicationHealthByTime",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        applicationId = urllib.parse.quote(str(applicationId), safe="")
        resource = f"/networks/{networkId}/insight/applications/{applicationId}/healthByTime"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkInsightApplicationHealthByTime: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationInsightApplications(self, organizationId: str):
        """
        **List all Insight tracked applications**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-applications

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["insight", "configure", "applications"],
            "operation": "getOrganizationInsightApplications",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications"

        return self._session.get(metadata, resource)

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

        metadata = {
            "tags": ["insight", "configure", "applications"],
            "operation": "createOrganizationInsightApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications"

        body_params = [
            "counterSetRuleId",
            "enableSmartThresholds",
            "thresholds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationInsightApplication: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["insight", "configure", "applications"],
            "operation": "updateOrganizationInsightApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        applicationId = urllib.parse.quote(str(applicationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications/{applicationId}"

        body_params = [
            "enableSmartThresholds",
            "thresholds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationInsightApplication: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationInsightApplication(self, organizationId: str, applicationId: str):
        """
        **Delete an Insight tracked application**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-application

        - organizationId (string): Organization ID
        - applicationId (string): Application ID
        """

        metadata = {
            "tags": ["insight", "configure", "applications"],
            "operation": "deleteOrganizationInsightApplication",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        applicationId = urllib.parse.quote(str(applicationId), safe="")
        resource = f"/organizations/{organizationId}/insight/applications/{applicationId}"

        return self._session.delete(metadata, resource)

    def getOrganizationInsightMonitoredMediaServers(self, organizationId: str):
        """
        **List the monitored media servers for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-servers

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "getOrganizationInsightMonitoredMediaServers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers"

        return self._session.get(metadata, resource)

    def createOrganizationInsightMonitoredMediaServer(self, organizationId: str, name: str, address: str, **kwargs):
        """
        **Add a media server to be monitored for this organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "createOrganizationInsightMonitoredMediaServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationInsightMonitoredMediaServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Return a monitored media server for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        """

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "getOrganizationInsightMonitoredMediaServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        monitoredMediaServerId = urllib.parse.quote(str(monitoredMediaServerId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        return self._session.get(metadata, resource)

    def updateOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str, **kwargs):
        """
        **Update a monitored media server for this organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        - name (string): The name of the VoIP provider
        - address (string): The IP address (IPv4 only) or hostname of the media server to monitor
        - bestEffortMonitoringEnabled (boolean): Indicates that if the media server doesn't respond to ICMP pings, the nearest hop will be used in its stead.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "updateOrganizationInsightMonitoredMediaServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        monitoredMediaServerId = urllib.parse.quote(str(monitoredMediaServerId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        body_params = [
            "name",
            "address",
            "bestEffortMonitoringEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationInsightMonitoredMediaServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationInsightMonitoredMediaServer(self, organizationId: str, monitoredMediaServerId: str):
        """
        **Delete a monitored media server from this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-monitored-media-server

        - organizationId (string): Organization ID
        - monitoredMediaServerId (string): Monitored media server ID
        """

        metadata = {
            "tags": ["insight", "configure", "monitoredMediaServers"],
            "operation": "deleteOrganizationInsightMonitoredMediaServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        monitoredMediaServerId = urllib.parse.quote(str(monitoredMediaServerId), safe="")
        resource = f"/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}"

        return self._session.delete(metadata, resource)

    def getOrganizationInsightSpeedTestResults(self, organizationId: str, serials: list, **kwargs):
        """
        **List the speed tests for the given devices under this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-speed-test-results

        - organizationId (string): Organization ID
        - serials (array): A list of serial numbers. The returned results will be filtered to only include these serials.
        - timespan (integer): Amount of seconds ago to query for results. Only include timespan OR both t0 & t1.
        - t0 (integer): Start time to query for results in epoch seconds. Only include timespan OR both t0 & t1.
        - t1 (integer): End time to query for results in epoch seconds. Only include timespan OR both t0 & t1.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["insight", "configure", "speedTestResults"],
            "operation": "getOrganizationInsightSpeedTestResults",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/speedTestResults"

        query_params = [
            "serials",
            "timespan",
            "t0",
            "t1",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "serials",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationInsightSpeedTestResults: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationInsightWebApps(self, organizationId: str):
        """
        **Lists all default web applications rules with counter set rule ids**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-insight-web-apps

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["insight", "configure", "webApps"],
            "operation": "getOrganizationInsightWebApps",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps"

        return self._session.get(metadata, resource)

    def createOrganizationInsightWebApp(self, organizationId: str, name: str, hostname: str, **kwargs):
        """
        **Add a custom web application for Insight to be able to track**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-insight-web-app

        - organizationId (string): Organization ID
        - name (string): The name of the Web Application
        - hostname (string): The hostname of Web Application
        """

        kwargs = locals()

        metadata = {
            "tags": ["insight", "configure", "webApps"],
            "operation": "createOrganizationInsightWebApp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps"

        body_params = [
            "name",
            "hostname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createOrganizationInsightWebApp: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

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

        metadata = {
            "tags": ["insight", "configure", "webApps"],
            "operation": "updateOrganizationInsightWebApp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        customCounterSetRuleId = urllib.parse.quote(str(customCounterSetRuleId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps/{customCounterSetRuleId}"

        body_params = [
            "name",
            "hostname",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateOrganizationInsightWebApp: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationInsightWebApp(self, organizationId: str, customCounterSetRuleId: str):
        """
        **Delete a custom web application by counter set rule id.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-insight-web-app

        - organizationId (string): Organization ID
        - customCounterSetRuleId (string): Custom counter set rule ID
        """

        metadata = {
            "tags": ["insight", "configure", "webApps"],
            "operation": "deleteOrganizationInsightWebApp",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        customCounterSetRuleId = urllib.parse.quote(str(customCounterSetRuleId), safe="")
        resource = f"/organizations/{organizationId}/insight/webApps/{customCounterSetRuleId}"

        return self._session.delete(metadata, resource)
