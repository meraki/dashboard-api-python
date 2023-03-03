import urllib


class ActionBatchSensor(object):
    def __init__(self):
        super(ActionBatchSensor, self).__init__()
        


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
        resource = f'/devices/{serial}/sensor/relationships'

        body_params = ['livestream', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/sensor/alerts/profiles'

        body_params = ['name', 'schedule', 'conditions', 'recipients', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        body_params = ['name', 'schedule', 'conditions', 'recipients', 'serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/networks/{networkId}/sensor/alerts/profiles/{id}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        



