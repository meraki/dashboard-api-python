import urllib


class Sensor(object):
    def __init__(self, session):
        super(Sensor, self).__init__()
        self._session = session
        


    def getDeviceSensorCommands(self, serial: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns a historical log of all commands**
        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-commands

        - serial (string): Serial
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - operations (array): Optional parameter to filter commands by operation. Allowed values are disableDownstreamPower, enableDownstreamPower, cycleDownstreamPower, and refreshData.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'descending'.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 30 days.
        """

        kwargs.update(locals())

        if 'sortOrder' in kwargs:
            options = ['ascending', 'descending']
            assert kwargs['sortOrder'] in options, f'''"sortOrder" cannot be "{kwargs['sortOrder']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['sensor', 'configure', 'commands'],
            'operation': 'getDeviceSensorCommands'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/sensor/commands'

        query_params = ['operations', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['operations', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def createDeviceSensorCommand(self, serial: str, operation: str):
        """
        **Sends a command to a sensor**
        https://developer.cisco.com/meraki/api-v1/#!create-device-sensor-command

        - serial (string): Serial
        - operation (string): Operation to run on the sensor. 'enableDownstreamPower', 'disableDownstreamPower', and 'cycleDownstreamPower' turn power on/off to the device that is connected downstream of an MT40 power monitor. 'refreshData' causes an MT15 or MT40 device to upload its latest readings so that they are immediately available in the Dashboard API.
        """

        kwargs = locals()

        metadata = {
            'tags': ['sensor', 'configure', 'commands'],
            'operation': 'createDeviceSensorCommand'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/sensor/commands'

        body_params = ['operation', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getDeviceSensorCommand(self, serial: str, commandId: str):
        """
        **Returns information about the command's execution, including the status**
        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-command

        - serial (string): Serial
        - commandId (string): Command ID
        """

        metadata = {
            'tags': ['sensor', 'configure', 'commands'],
            'operation': 'getDeviceSensorCommand'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        commandId = urllib.parse.quote(str(commandId), safe='')
        resource = f'/devices/{serial}/sensor/commands/{commandId}'

        return self._session.get(metadata, resource)
        


    def getDeviceSensorRelationships(self, serial: str):
        """
        **List the sensor roles for a given sensor or camera device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-sensor-relationships

        - serial (string): Serial
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

        - serial (string): Serial
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

        - networkId (string): Network ID
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

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 731 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 366 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 366 days. The default is 7 days. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 900, 3600, 86400, 604800, 2592000. The default is 604800. Interval is calculated if time params are provided.
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

        - networkId (string): Network ID
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

        - networkId (string): Network ID
        - name (string): Name of the sensor alert profile.
        - conditions (array): List of conditions that will cause the profile to send an alert.
        - schedule (object): The sensor schedule to use with the alert profile.
        - recipients (object): List of recipients that will receive the alert.
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

        - networkId (string): Network ID
        - id (string): ID
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

        - networkId (string): Network ID
        - id (string): ID
        - name (string): Name of the sensor alert profile.
        - schedule (object): The sensor schedule to use with the alert profile.
        - conditions (array): List of conditions that will cause the profile to send an alert.
        - recipients (object): List of recipients that will receive the alert.
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

        - networkId (string): Network ID
        - id (string): ID
        """

        metadata = {
            'tags': ['sensor', 'configure', 'alerts', 'profiles'],
            'operation': 'deleteNetworkSensorAlertsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSensorMqttBrokers(self, networkId: str):
        """
        **List the sensor settings of all MQTT brokers for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-mqtt-brokers

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['sensor', 'configure', 'mqttBrokers'],
            'operation': 'getNetworkSensorMqttBrokers'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sensor/mqttBrokers'

        return self._session.get(metadata, resource)
        


    def getNetworkSensorMqttBroker(self, networkId: str, mqttBrokerId: str):
        """
        **Return the sensor settings of an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID
        """

        metadata = {
            'tags': ['sensor', 'configure', 'mqttBrokers'],
            'operation': 'getNetworkSensorMqttBroker'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        mqttBrokerId = urllib.parse.quote(str(mqttBrokerId), safe='')
        resource = f'/networks/{networkId}/sensor/mqttBrokers/{mqttBrokerId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkSensorMqttBroker(self, networkId: str, mqttBrokerId: str, enabled: bool):
        """
        **Update the sensor settings of an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sensor-mqtt-broker

        - networkId (string): Network ID
        - mqttBrokerId (string): Mqtt broker ID
        - enabled (boolean): Set to true to enable MQTT broker for sensor network
        """

        kwargs = locals()

        metadata = {
            'tags': ['sensor', 'configure', 'mqttBrokers'],
            'operation': 'updateNetworkSensorMqttBroker'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        mqttBrokerId = urllib.parse.quote(str(mqttBrokerId), safe='')
        resource = f'/networks/{networkId}/sensor/mqttBrokers/{mqttBrokerId}'

        body_params = ['enabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkSensorRelationships(self, networkId: str):
        """
        **List the sensor roles for devices in a given network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sensor-relationships

        - networkId (string): Network ID
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

        - organizationId (string): Organization ID
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
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are apparentPower, battery, button, co2, current, door, downstreamPower, frequency, humidity, indoorAirQuality, noise, pm25, powerFactor, realPower, remoteLockoutSwitch, temperature, tvoc, voltage, and water.
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

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are apparentPower, battery, button, co2, current, door, downstreamPower, frequency, humidity, indoorAirQuality, noise, pm25, powerFactor, realPower, remoteLockoutSwitch, temperature, tvoc, voltage, and water.
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
        
