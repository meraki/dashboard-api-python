import urllib


class ActionBatchSm(object):
    def __init__(self):
        super(ActionBatchSm, self).__init__()
        


    def deleteNetworkSmUserAccessDevice(self, networkId: str, userAccessDeviceId: str):
        """
        **Delete a User Access Device**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        - networkId (string): (required)
        - userAccessDeviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'userAccessDevices'],
            'operation': 'deleteNetworkSmUserAccessDevice'
        }
        resource = f'/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        



