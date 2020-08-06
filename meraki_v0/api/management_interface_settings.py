class ManagementInterfaceSettings(object):
    def __init__(self, session):
        super(ManagementInterfaceSettings, self).__init__()
        self._session = session
    
    def getNetworkDeviceManagementInterfaceSettings(self, networkId: str, serial: str):
        """
        **Return the management interface settings for a device**
        https://developer.cisco.com/meraki/api/#!get-network-device-management-interface-settings
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Management interface settings'],
            'operation': 'getNetworkDeviceManagementInterfaceSettings',
        }
        resource = f'/networks/{networkId}/devices/{serial}/managementInterfaceSettings'

        return self._session.get(metadata, resource)

    def updateNetworkDeviceManagementInterfaceSettings(self, networkId: str, serial: str, **kwargs):
        """
        **Update the management interface settings for a device**
        https://developer.cisco.com/meraki/api/#!update-network-device-management-interface-settings
        
        - networkId (string)
        - serial (string)
        - wan1 (object): WAN 1 settings
        - wan2 (object): WAN 2 settings (only for MX devices)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Management interface settings'],
            'operation': 'updateNetworkDeviceManagementInterfaceSettings',
        }
        resource = f'/networks/{networkId}/devices/{serial}/managementInterfaceSettings'

        body_params = ['wan1', 'wan2']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

