class BluetoothSettings(object):
    def __init__(self, session):
        super(BluetoothSettings, self).__init__()
        self._session = session
    
    def getDeviceWirelessBluetoothSettings(self, serial: str):
        """
        **Return the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api/#!get-device-wireless-bluetooth-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['Bluetooth settings'],
            'operation': 'getDeviceWirelessBluetoothSettings',
        }
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        return self._session.get(metadata, resource)

    def updateDeviceWirelessBluetoothSettings(self, serial: str, **kwargs):
        """
        **Update the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api/#!update-device-wireless-bluetooth-settings
        
        - serial (string)
        - uuid (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        - major (integer): Desired major value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        - minor (integer): Desired minor value of the beacon. If the value is set to null it will reset to Dashboard's automatically generated value.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Bluetooth settings'],
            'operation': 'updateDeviceWirelessBluetoothSettings',
        }
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        body_params = ['uuid', 'major', 'minor']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkBluetoothSettings(self, networkId: str):
        """
        **Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**
        https://developer.cisco.com/meraki/api/#!get-network-bluetooth-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Bluetooth settings'],
            'operation': 'getNetworkBluetoothSettings',
        }
        resource = f'/networks/{networkId}/bluetoothSettings'

        return self._session.get(metadata, resource)

    def updateNetworkBluetoothSettings(self, networkId: str, **kwargs):
        """
        **Update the Bluetooth settings for a network. See the docs page for <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a>.**
        https://developer.cisco.com/meraki/api/#!update-network-bluetooth-settings
        
        - networkId (string)
        - scanningEnabled (boolean): Whether APs will scan for Bluetooth enabled clients. (true, false)
        - advertisingEnabled (boolean): Whether APs will advertise beacons. (true, false)
        - uuid (string): The UUID to be used in the beacon identifier.
        - majorMinorAssignmentMode (string): The way major and minor number should be assigned to nodes in the network. ('Unique', 'Non-unique')
        - major (integer): The major number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
        - minor (integer): The minor number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
        """

        kwargs.update(locals())

        if 'majorMinorAssignmentMode' in kwargs:
            options = ['Unique', 'Non-unique']
            assert kwargs['majorMinorAssignmentMode'] in options, f'''"majorMinorAssignmentMode" cannot be "{kwargs['majorMinorAssignmentMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Bluetooth settings'],
            'operation': 'updateNetworkBluetoothSettings',
        }
        resource = f'/networks/{networkId}/bluetoothSettings'

        body_params = ['scanningEnabled', 'advertisingEnabled', 'uuid', 'majorMinorAssignmentMode', 'major', 'minor']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

