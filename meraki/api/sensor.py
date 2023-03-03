import urllib


class Sensor(object):
    def __init__(self, session):
        super(Sensor, self).__init__()
        self._session = session
        


    def getDeviceSensorRelationships(self, serial: str):
        """
        **List the sensor roles for a given sensor or camera device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-relationships

        - serial (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'relationships'],
            'operation': 'getDeviceSensorRelationships'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/sensor/relationships'

        return self._session.get(metadata, resource)
        


    def updateDeviceSensorRelationships(self, serial: str, **kwargs):
        """
        **Assign one or more sensor roles to a given sensor or camera device.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-sensor-relationships

        - serial (string): (required)
        - livestream (object): A role defined between an MT sensor and an MV camera that adds the camera's livestream to the sensor's details page. Snapshots from the camera will also appear in alert notifications that the sensor triggers.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'configure', 'relationships'],
            'operation': 'updateDeviceSensorRelationships'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/sensor/relationships'

        body_params = ['livestream', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSensorAlertsCurrentOverviewByMetric(self, networkId: str):
        """
        **Return an overview of currently alerting sensors by metric**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-current-overview-by-metric

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'monitor', 'alerts', 'current', 'overview', 'byMetric'],
            'operation': 'getNetworkSensorAlertsCurrentOverviewByMetric'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/current/overview/byMetric'

        return self._session.get(metadata, resource)
        


    def getNetworkSensorAlertsOverviewByMetric(self, networkId: str, **kwargs):
        """
        **Return an overview of alert occurrences over a timespan, by metric**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-overview-by-metric

        - networkId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'alerts', 'overview', 'byMetric'],
            'operation': 'getNetworkSensorAlertsOverviewByMetric'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/overview/byMetric'

        query_params = ['t0', 't1', 'timespan', 'interval', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkSensorAlertsProfiles(self, networkId: str):
        """
        **Lists all sensor alert profiles for a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profiles

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'getNetworkSensorAlertsProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/profiles'

        return self._session.get(metadata, resource)
        


    def createNetworkSensorAlertsProfile(self, networkId: str, name: str, conditions: list, **kwargs):
        """
        **Creates a sensor alert profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sensor-alerts-profile

        - networkId (string): (required)
        - name (string): Name of the sensor alert profile.
        - conditions (array): List of conditions that will cause the profile to send an alert.
        - schedule (object): The sensor schedule to use with the alert profile.
        - recipients (object): List of recipients that will recieve the alert.
        - serials (array): List of device serials assigned to this sensor alert profile.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'createNetworkSensorAlertsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/profiles'

        body_params = ['name', 'schedule', 'conditions', 'recipients', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSensorAlertsProfile(self, networkId: str, id: str):
        """
        **Show details of a sensor alert profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-alerts-profile

        - networkId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'getNetworkSensorAlertsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        return self._session.get(metadata, resource)
        


    def updateNetworkSensorAlertsProfile(self, networkId: str, id: str, **kwargs):
        """
        **Updates a sensor alert profile for a network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-alerts-profile

        - networkId (string): (required)
        - id (string): (required)
        - name (string): Name of the sensor alert profile.
        - schedule (object): The sensor schedule to use with the alert profile.
        - conditions (array): List of conditions that will cause the profile to send an alert.
        - recipients (object): List of recipients that will recieve the alert.
        - serials (array): List of device serials assigned to this sensor alert profile.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'updateNetworkSensorAlertsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        body_params = ['name', 'schedule', 'conditions', 'recipients', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSensorAlertsProfile(self, networkId: str, id: str):
        """
        **Deletes a sensor alert profile from a network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sensor-alerts-profile

        - networkId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'deleteNetworkSensorAlertsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSensorRelationships(self, networkId: str):
        """
        **List the sensor roles for devices in a given network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-relationships

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sensor', 'configure', 'relationships'],
            'operation': 'getNetworkSensorRelationships'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sensor/relationships'

        return self._session.get(metadata, resource)
        


    def getOrganizationSensorReadingsHistory(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return all reported readings from sensors in a given timespan, sorted by timestamp**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'history'],
            'operation': 'getOrganizationSensorReadingsHistory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sensor/readings/history'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationSensorReadingsLatest(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the latest available reading for each metric from each sensor, sorted by sensor serial**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'latest'],
            'operation': 'getOrganizationSensorReadingsLatest'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sensor/readings/latest'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
