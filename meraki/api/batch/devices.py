import urllib


class ActionBatchDevices(object):
    def __init__(self):
        super(ActionBatchDevices, self).__init__()
        


    def updateDevice(self, serial: str, **kwargs):
        """
        **Update the attributes of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device

        - serial (string): Serial
        - name (string): The name of a device
        - tags (array): The list of tags of a device
        - lat (number): The latitude of a device
        - lng (number): The longitude of a device
        - address (string): The address of a device
        - notes (string): The notes for the device. String. Limited to 255 characters.
        - moveMapMarker (boolean): Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified.
        - switchProfileId (string): The ID of a switch template to bind to the device (for available switch templates, see the 'Switch Templates' endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch template, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template.
        - floorPlanId (string): The floor plan to associate to this device. null disassociates the device from the floorplan.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'configure'],
            'operation': 'updateDevice'
        }
        resource = f'/devices/{serial}'

        body_params = ['name', 'tags', 'lat', 'lng', 'address', 'notes', 'moveMapMarker', 'switchProfileId', 'floorPlanId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createDeviceLiveToolsThroughputTest(self, serial: str, **kwargs):
        """
        **Enqueue a job to test a device throughput, the test will run for 10 secs to test throughput. This endpoint has a rate limit of one request every five seconds per device.**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-throughput-test

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'liveTools', 'throughputTest'],
            'operation': 'createDeviceLiveToolsThroughputTest'
        }
        resource = f'/devices/{serial}/liveTools/throughputTest'

        body_params = ['callback', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "test",
            "body": payload
        }
        return action
        





    def updateDeviceManagementInterface(self, serial: str, **kwargs):
        """
        **Update the management interface settings for a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-management-interface

        - serial (string): Serial
        - wan1 (object): WAN 1 settings
        - wan2 (object): WAN 2 settings (only for MX devices)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['devices', 'configure', 'managementInterface'],
            'operation': 'updateDeviceManagementInterface'
        }
        resource = f'/devices/{serial}/managementInterface'

        body_params = ['wan1', 'wan2', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        



