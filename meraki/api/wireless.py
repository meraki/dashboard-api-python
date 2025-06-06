import urllib


class Wireless(object):
    def __init__(self, session):
        super(Wireless, self).__init__()
        self._session = session
        


    def updateDeviceWirelessAlternateManagementInterfaceIpv6(self, serial: str, **kwargs):
        """
        **Update alternate management interface IPv6 address**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-alternate-management-interface-ipv-6

        - serial (string): Serial
        - addresses (array): configured alternate management interface addresses
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'alternateManagementInterface', 'ipv6'],
            'operation': 'updateDeviceWirelessAlternateManagementInterfaceIpv6'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/alternateManagementInterface/ipv6'

        body_params = ['addresses', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceWirelessBluetoothSettings(self, serial: str):
        """
        **Return the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-bluetooth-settings

        - serial (string): Serial
        """

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'getDeviceWirelessBluetoothSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        return self._session.get(metadata, resource)
        


    def updateDeviceWirelessBluetoothSettings(self, serial: str, **kwargs):
        """
        **Update the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-bluetooth-settings

        - serial (string): Serial
        - uuid (string): Desired UUID of the beacon. If the value is set to null it will reset to Dashboard's
          automatically generated value.
        - major (integer): Desired major value of the beacon. If the value is set to null it will reset to
          Dashboard's automatically generated value.
        - minor (integer): Desired minor value of the beacon. If the value is set to null it will reset to
          Dashboard's automatically generated value.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'updateDeviceWirelessBluetoothSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/bluetooth/settings'

        body_params = ['uuid', 'major', 'minor', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceWirelessConnectionStats(self, serial: str, **kwargs):
        """
        **Aggregated connectivity info for a given AP on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-connection-stats

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'connectionStats'],
            'operation': 'getDeviceWirelessConnectionStats'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceWirelessElectronicShelfLabel(self, serial: str):
        """
        **Return the ESL settings of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-electronic-shelf-label

        - serial (string): Serial
        """

        metadata = {
            'tags': ['wireless', 'configure', 'electronicShelfLabel'],
            'operation': 'getDeviceWirelessElectronicShelfLabel'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/electronicShelfLabel'

        return self._session.get(metadata, resource)
        


    def updateDeviceWirelessElectronicShelfLabel(self, serial: str, **kwargs):
        """
        **Update the ESL settings of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-electronic-shelf-label

        - serial (string): Serial
        - channel (string): Desired ESL channel for the device, or 'Auto' (case insensitive) to use the recommended channel
        - enabled (boolean): Turn ESL features on and off for this device
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'electronicShelfLabel'],
            'operation': 'updateDeviceWirelessElectronicShelfLabel'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/electronicShelfLabel'

        body_params = ['channel', 'enabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceWirelessLatencyStats(self, serial: str, **kwargs):
        """
        **Aggregated latency info for a given AP on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-latency-stats

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'latencyStats'],
            'operation': 'getDeviceWirelessLatencyStats'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceWirelessRadioSettings(self, serial: str):
        """
        **Return the manually configured radio settings overrides of a device, which take precedence over RF profiles.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-settings

        - serial (string): Serial
        """

        metadata = {
            'tags': ['wireless', 'configure', 'radio', 'settings'],
            'operation': 'getDeviceWirelessRadioSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/radio/settings'

        return self._session.get(metadata, resource)
        


    def updateDeviceWirelessRadioSettings(self, serial: str, **kwargs):
        """
        **Update the radio settings overrides of a device, which take precedence over RF profiles.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

        - serial (string): Serial
        - rfProfileId (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
        - twoFourGhzSettings (object): Manual radio settings for 2.4 GHz.
        - fiveGhzSettings (object): Manual radio settings for 5 GHz.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'radio', 'settings'],
            'operation': 'updateDeviceWirelessRadioSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/radio/settings'

        body_params = ['rfProfileId', 'twoFourGhzSettings', 'fiveGhzSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceWirelessStatus(self, serial: str):
        """
        **Return the SSID statuses of an access point**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-status

        - serial (string): Serial
        """

        metadata = {
            'tags': ['wireless', 'monitor', 'status'],
            'operation': 'getDeviceWirelessStatus'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/wireless/status'

        return self._session.get(metadata, resource)
        


    def getNetworkWirelessAirMarshal(self, networkId: str, **kwargs):
        """
        **List Air Marshal scan results from a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-air-marshal

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'airMarshal'],
            'operation': 'getNetworkWirelessAirMarshal'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/airMarshal'

        query_params = ['t0', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def createNetworkWirelessAirMarshalRule(self, networkId: str, type: str, match: dict):
        """
        **Creates a new rule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-air-marshal-rule

        - networkId (string): Network ID
        - type (string): Indicates if this rule will allow, block, or alert.
        - match (object): Object describing the rule specification.
        """

        kwargs = locals()

        if 'type' in kwargs:
            options = ['alert', 'allow', 'block']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'airMarshal', 'rules'],
            'operation': 'createNetworkWirelessAirMarshalRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/airMarshal/rules'

        body_params = ['type', 'match', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateNetworkWirelessAirMarshalRule(self, networkId: str, ruleId: str, **kwargs):
        """
        **Update a rule**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-rule

        - networkId (string): Network ID
        - ruleId (string): Rule ID
        - type (string): Indicates if this rule will allow, block, or alert.
        - match (object): Object describing the rule specification.
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['alert', 'allow', 'block']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'airMarshal', 'rules'],
            'operation': 'updateNetworkWirelessAirMarshalRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        ruleId = urllib.parse.quote(str(ruleId), safe='')
        resource = f'/networks/{networkId}/wireless/airMarshal/rules/{ruleId}'

        body_params = ['type', 'match', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkWirelessAirMarshalRule(self, networkId: str, ruleId: str):
        """
        **Delete an Air Marshal rule.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-air-marshal-rule

        - networkId (string): Network ID
        - ruleId (string): Rule ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'airMarshal', 'rules'],
            'operation': 'deleteNetworkWirelessAirMarshalRule'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        ruleId = urllib.parse.quote(str(ruleId), safe='')
        resource = f'/networks/{networkId}/wireless/airMarshal/rules/{ruleId}'

        return self._session.delete(metadata, resource)
        


    def updateNetworkWirelessAirMarshalSettings(self, networkId: str, defaultPolicy: str):
        """
        **Updates Air Marshal settings.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-settings

        - networkId (string): Network ID
        - defaultPolicy (string): Allows clients to access rogue networks. Blocked by default.
        """

        kwargs = locals()

        if 'defaultPolicy' in kwargs:
            options = ['allow', 'block']
            assert kwargs['defaultPolicy'] in options, f'''"defaultPolicy" cannot be "{kwargs['defaultPolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'airMarshal', 'settings'],
            'operation': 'updateNetworkWirelessAirMarshalSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/airMarshal/settings'

        body_params = ['defaultPolicy', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessAlternateManagementInterface(self, networkId: str):
        """
        **Return alternate management interface and devices with IP assigned**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'alternateManagementInterface'],
            'operation': 'getNetworkWirelessAlternateManagementInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/alternateManagementInterface'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessAlternateManagementInterface(self, networkId: str, **kwargs):
        """
        **Update alternate management interface and device static IP**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-alternate-management-interface

        - networkId (string): Network ID
        - enabled (boolean): Boolean value to enable or disable alternate management interface
        - vlanId (integer): Alternate management interface VLAN, must be between 1 and 4094
        - protocols (array): Can be one or more of the following values: 'radius', 'snmp', 'syslog' or 'ldap'
        - accessPoints (array): Array of access point serial number and IP assignment. Note: accessPoints IP assignment is not applicable for template networks, in other words, do not put 'accessPoints' in the body when updating template networks. Also, an empty 'accessPoints' array will remove all previous static IP assignments
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'alternateManagementInterface'],
            'operation': 'updateNetworkWirelessAlternateManagementInterface'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/alternateManagementInterface'

        body_params = ['enabled', 'vlanId', 'protocols', 'accessPoints', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessBilling(self, networkId: str):
        """
        **Return the billing settings of this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-billing

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'billing'],
            'operation': 'getNetworkWirelessBilling'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/billing'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessBilling(self, networkId: str, **kwargs):
        """
        **Update the billing settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-billing

        - networkId (string): Network ID
        - currency (string): The currency code of this node group's billing plans
        - plans (array): Array of billing plans in the node group. (Can configure a maximum of 5)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'billing'],
            'operation': 'updateNetworkWirelessBilling'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/billing'

        body_params = ['currency', 'plans', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessBluetoothSettings(self, networkId: str):
        """
        **Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'getNetworkWirelessBluetoothSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/bluetooth/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessBluetoothSettings(self, networkId: str, **kwargs):
        """
        **Update the Bluetooth settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-bluetooth-settings

        - networkId (string): Network ID
        - scanningEnabled (boolean): Whether APs will scan for Bluetooth enabled clients.
        - advertisingEnabled (boolean): Whether APs will advertise beacons.
        - uuid (string): The UUID to be used in the beacon identifier.
        - majorMinorAssignmentMode (string): The way major and minor number should be assigned to nodes in the network. ('Unique', 'Non-unique')
        - major (integer): The major number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
        - minor (integer): The minor number to be used in the beacon identifier. Only valid in 'Non-unique' mode.
        """

        kwargs.update(locals())

        if 'majorMinorAssignmentMode' in kwargs:
            options = ['Non-unique', 'Unique']
            assert kwargs['majorMinorAssignmentMode'] in options, f'''"majorMinorAssignmentMode" cannot be "{kwargs['majorMinorAssignmentMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'bluetooth', 'settings'],
            'operation': 'updateNetworkWirelessBluetoothSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/bluetooth/settings'

        body_params = ['scanningEnabled', 'advertisingEnabled', 'uuid', 'majorMinorAssignmentMode', 'major', 'minor', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessChannelUtilizationHistory(self, networkId: str, **kwargs):
        """
        **Return AP channel utilization over time for a device or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-channel-utilization-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 600, 1200, 3600, 14400, 86400. The default is 86400.
        - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        - clientId (string): Filter results by network client to return per-device, per-band AP channel utilization metrics inner joined by the queried client's connection history.
        - deviceSerial (string): Filter results by device to return AP channel utilization metrics for the queried device; either :band or :clientId must be jointly specified.
        - apTag (string): Filter results by AP tag to return AP channel utilization metrics for devices labeled with the given tag; either :clientId or :deviceSerial must be jointly specified.
        - band (string): Filter results by band (either '2.4', '5' or '6').
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'channelUtilizationHistory'],
            'operation': 'getNetworkWirelessChannelUtilizationHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/channelUtilizationHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessClientCountHistory(self, networkId: str, **kwargs):
        """
        **Return wireless client counts over time for a network, device, or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-count-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
        - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        - clientId (string): Filter results by network client to return per-device client counts over time inner joined by the queried client's connection history.
        - deviceSerial (string): Filter results by device.
        - apTag (string): Filter results by AP tag.
        - band (string): Filter results by band (either '2.4', '5' or '6').
        - ssid (integer): Filter results by SSID number.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'clientCountHistory'],
            'operation': 'getNetworkWirelessClientCountHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/clientCountHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessClientsConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by clients**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-connection-stats

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'connectionStats'],
            'operation': 'getNetworkWirelessClientsConnectionStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/clients/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessClientsLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by clients**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-latency-stats

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'latencyStats'],
            'operation': 'getNetworkWirelessClientsLatencyStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/clients/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessClientConnectionStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated connectivity info for a given client on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connection-stats

        - networkId (string): Network ID
        - clientId (string): Client ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'connectionStats'],
            'operation': 'getNetworkWirelessClientConnectionStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        clientId = urllib.parse.quote(str(clientId), safe='')
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessClientConnectivityEvents(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the wireless connectivity events for a client within a network in the timespan.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-connectivity-events

        - networkId (string): Network ID
        - clientId (string): Client ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of entries. Order options are 'ascending' and 'descending'. Default is 'ascending'.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - types (array): A list of event types to include. If not specified, events of all types will be returned. Valid types are 'assoc', 'disassoc', 'auth', 'deauth', 'dns', 'dhcp', 'roam', 'connection' and/or 'sticky'.
        - band (string): Filter results by band. Valid bands are '2.4', '5' or '6'.
        - ssidNumber (integer): Filter results by SSID. If not specified, events for all SSIDs will be returned.
        - includedSeverities (array): A list of severities to include. If not specified, events of all severities will be returned. Valid severities are 'good', 'info', 'warn' and/or 'bad'.
        - deviceSerial (string): Filter results by an AP's serial number.
        """

        kwargs.update(locals())

        if 'sortOrder' in kwargs:
            options = ['ascending', 'descending']
            assert kwargs['sortOrder'] in options, f'''"sortOrder" cannot be "{kwargs['sortOrder']}", & must be set to one of: {options}'''
        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''
        if 'ssidNumber' in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs['ssidNumber'] in options, f'''"ssidNumber" cannot be "{kwargs['ssidNumber']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'connectivityEvents'],
            'operation': 'getNetworkWirelessClientConnectivityEvents'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        clientId = urllib.parse.quote(str(clientId), safe='')
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/connectivityEvents'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'sortOrder', 't0', 't1', 'timespan', 'types', 'band', 'ssidNumber', 'includedSeverities', 'deviceSerial', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['types', 'includedSeverities', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkWirelessClientLatencyHistory(self, networkId: str, clientId: str, **kwargs):
        """
        **Return the latency history for a client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-history

        - networkId (string): Network ID
        - clientId (string): Client ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 86400. The default is 86400.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'latencyHistory'],
            'operation': 'getNetworkWirelessClientLatencyHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        clientId = urllib.parse.quote(str(clientId), safe='')
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/latencyHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessClientLatencyStats(self, networkId: str, clientId: str, **kwargs):
        """
        **Aggregated latency info for a given client on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-latency-stats

        - networkId (string): Network ID
        - clientId (string): Client ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'latencyStats'],
            'operation': 'getNetworkWirelessClientLatencyStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        clientId = urllib.parse.quote(str(clientId), safe='')
        resource = f'/networks/{networkId}/wireless/clients/{clientId}/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-connection-stats

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'connectionStats'],
            'operation': 'getNetworkWirelessConnectionStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessDataRateHistory(self, networkId: str, **kwargs):
        """
        **Return PHY data rates over time for a network, device, or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-data-rate-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
        - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        - clientId (string): Filter results by network client.
        - deviceSerial (string): Filter results by device.
        - apTag (string): Filter results by AP tag.
        - band (string): Filter results by band (either '2.4', '5' or '6').
        - ssid (integer): Filter results by SSID number.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'dataRateHistory'],
            'operation': 'getNetworkWirelessDataRateHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/dataRateHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessDevicesConnectionStats(self, networkId: str, **kwargs):
        """
        **Aggregated connectivity info for this network, grouped by node**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-connection-stats

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'connectionStats'],
            'operation': 'getNetworkWirelessDevicesConnectionStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/devices/connectionStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessDevicesLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network, grouped by node**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-latency-stats

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'latencyStats'],
            'operation': 'getNetworkWirelessDevicesLatencyStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/devices/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessElectronicShelfLabel(self, networkId: str):
        """
        **Return the ESL settings of a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'electronicShelfLabel'],
            'operation': 'getNetworkWirelessElectronicShelfLabel'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/electronicShelfLabel'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessElectronicShelfLabel(self, networkId: str, **kwargs):
        """
        **Update the ESL settings of a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-electronic-shelf-label

        - networkId (string): Network ID
        - hostname (string): Desired ESL hostname of the network
        - enabled (boolean): Turn ESL features on and off for this network
        - mode (string): Electronic shelf label mode of the network. Valid options are 'Bluetooth', 'high frequency'
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['Bluetooth', 'high frequency']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'electronicShelfLabel'],
            'operation': 'updateNetworkWirelessElectronicShelfLabel'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/electronicShelfLabel'

        body_params = ['hostname', 'enabled', 'mode', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessElectronicShelfLabelConfiguredDevices(self, networkId: str):
        """
        **Get a list of all ESL eligible devices of a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label-configured-devices

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'electronicShelfLabel', 'configuredDevices'],
            'operation': 'getNetworkWirelessElectronicShelfLabelConfiguredDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/electronicShelfLabel/configuredDevices'

        return self._session.get(metadata, resource)
        


    def getNetworkWirelessEthernetPortsProfiles(self, networkId: str):
        """
        **List the AP port profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profiles

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'getNetworkWirelessEthernetPortsProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles'

        return self._session.get(metadata, resource)
        


    def createNetworkWirelessEthernetPortsProfile(self, networkId: str, name: str, ports: list, **kwargs):
        """
        **Create an AP port profile**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ethernet-ports-profile

        - networkId (string): Network ID
        - name (string): AP port profile name
        - ports (array): AP ports configuration
        - usbPorts (array): AP usb ports configuration
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'createNetworkWirelessEthernetPortsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles'

        body_params = ['name', 'ports', 'usbPorts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def assignNetworkWirelessEthernetPortsProfiles(self, networkId: str, serials: list, profileId: str):
        """
        **Assign AP port profile to list of APs**
        https://developer.cisco.com/meraki/api-v1/#!assign-network-wireless-ethernet-ports-profiles

        - networkId (string): Network ID
        - serials (array): List of AP serials
        - profileId (string): AP profile ID
        """

        kwargs = locals()

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'assignNetworkWirelessEthernetPortsProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles/assign'

        body_params = ['serials', 'profileId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def setNetworkWirelessEthernetPortsProfilesDefault(self, networkId: str, profileId: str):
        """
        **Set the AP port profile to be default for this network**
        https://developer.cisco.com/meraki/api-v1/#!set-network-wireless-ethernet-ports-profiles-default

        - networkId (string): Network ID
        - profileId (string): AP profile ID
        """

        kwargs = locals()

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'setNetworkWirelessEthernetPortsProfilesDefault'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles/setDefault'

        body_params = ['profileId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkWirelessEthernetPortsProfile(self, networkId: str, profileId: str):
        """
        **Show the AP port profile by ID for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'getNetworkWirelessEthernetPortsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        profileId = urllib.parse.quote(str(profileId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessEthernetPortsProfile(self, networkId: str, profileId: str, **kwargs):
        """
        **Update the AP port profile by ID for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ethernet-ports-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        - name (string): AP port profile name
        - ports (array): AP ports configuration
        - usbPorts (array): AP usb ports configuration
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'updateNetworkWirelessEthernetPortsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        profileId = urllib.parse.quote(str(profileId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}'

        body_params = ['name', 'ports', 'usbPorts', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkWirelessEthernetPortsProfile(self, networkId: str, profileId: str):
        """
        **Delete an AP port profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ethernet-ports-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ethernet', 'ports', 'profiles'],
            'operation': 'deleteNetworkWirelessEthernetPortsProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        profileId = urllib.parse.quote(str(profileId), safe='')
        resource = f'/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkWirelessFailedConnections(self, networkId: str, **kwargs):
        """
        **List of all failed client connection events on this network in a given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-failed-connections

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - serial (string): Filter by AP
        - clientId (string): Filter by client MAC
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'failedConnections'],
            'operation': 'getNetworkWirelessFailedConnections'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/failedConnections'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'serial', 'clientId', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessLatencyHistory(self, networkId: str, **kwargs):
        """
        **Return average wireless latency over time for a network, device, or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
        - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        - clientId (string): Filter results by network client.
        - deviceSerial (string): Filter results by device.
        - apTag (string): Filter results by AP tag.
        - band (string): Filter results by band (either '2.4', '5' or '6').
        - ssid (integer): Filter results by SSID number.
        - accessCategory (string): Filter by access category.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''
        if 'accessCategory' in kwargs:
            options = ['backgroundTraffic', 'bestEffortTraffic', 'videoTraffic', 'voiceTraffic']
            assert kwargs['accessCategory'] in options, f'''"accessCategory" cannot be "{kwargs['accessCategory']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'latencyHistory'],
            'operation': 'getNetworkWirelessLatencyHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/latencyHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', 'accessCategory', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessLatencyStats(self, networkId: str, **kwargs):
        """
        **Aggregated latency info for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-latency-stats

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 180 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days.
        - band (string): Filter results by band (either '2.4', '5' or '6'). Note that data prior to February 2020 will not have band information.
        - ssid (integer): Filter results by SSID
        - vlan (integer): Filter results by VLAN
        - apTag (string): Filter results by AP Tag
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'latencyStats'],
            'operation': 'getNetworkWirelessLatencyStats'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/latencyStats'

        query_params = ['t0', 't1', 'timespan', 'band', 'ssid', 'vlan', 'apTag', 'fields', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def updateNetworkWirelessLocationScanning(self, networkId: str, **kwargs):
        """
        **Change scanning API settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-location-scanning

        - networkId (string): Network ID
        - enabled (boolean): Collect location and scanning analytics
        - api (object): Enable push API for scanning events, analytics must be enabled
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'location', 'scanning'],
            'operation': 'updateNetworkWirelessLocationScanning'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/location/scanning'

        body_params = ['enabled', 'api', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessMeshStatuses(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List wireless mesh statuses for repeaters**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-mesh-statuses

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'meshStatuses'],
            'operation': 'getNetworkWirelessMeshStatuses'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/meshStatuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkWirelessRfProfiles(self, networkId: str, **kwargs):
        """
        **List RF profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

        - networkId (string): Network ID
        - includeTemplateProfiles (boolean): If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'getNetworkWirelessRfProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        query_params = ['includeTemplateProfiles', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def createNetworkWirelessRfProfile(self, networkId: str, name: str, bandSelectionType: str, **kwargs):
        """
        **Creates new RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-rf-profile

        - networkId (string): Network ID
        - name (string): The name of the new profile. Must be unique. This param is required on creation.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - sixGhzSettings (object): Settings related to 6Ghz band. Only applicable to networks with 6Ghz capable APs
        - transmission (object): Settings related to radio transmission.
        - perSsidSettings (object): Per-SSID radio settings by number.
        - flexRadios (object): Flex radio settings.
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ap', 'ssid']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'createNetworkWirelessRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings', 'sixGhzSettings', 'transmission', 'perSsidSettings', 'flexRadios', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        - name (string): The name of the new profile. Must be unique.
        - isIndoorDefault (boolean): Set this profile as the default indoor rf profile. If the profile ID is one of 'indoor' or 'outdoor',   then a new profile will be created from the respective ID and set as the default
        - isOutdoorDefault (boolean): Set this profile as the default outdoor rf profile. If the profile ID is one of 'indoor' or 'outdoor',   then a new profile will be created from the respective ID and set as the default
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - sixGhzSettings (object): Settings related to 6Ghz band. Only applicable to networks with 6Ghz capable APs
        - transmission (object): Settings related to radio transmission.
        - perSsidSettings (object): Per-SSID radio settings by number.
        - flexRadios (object): Flex radio settings.
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ap', 'ssid']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'updateNetworkWirelessRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe='')
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        body_params = ['name', 'isIndoorDefault', 'isOutdoorDefault', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings', 'sixGhzSettings', 'transmission', 'perSsidSettings', 'flexRadios', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'deleteNetworkWirelessRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe='')
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Return a RF profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles'],
            'operation': 'getNetworkWirelessRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe='')
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        return self._session.get(metadata, resource)
        


    def getNetworkWirelessSettings(self, networkId: str):
        """
        **Return the wireless settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'settings'],
            'operation': 'getNetworkWirelessSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSettings(self, networkId: str, **kwargs):
        """
        **Update the wireless settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-settings

        - networkId (string): Network ID
        - meshingEnabled (boolean): Toggle for enabling or disabling meshing in a network
        - ipv6BridgeEnabled (boolean): Toggle for enabling or disabling IPv6 bridging in a network (Note: if enabled, SSIDs must also be configured to use bridge mode)
        - locationAnalyticsEnabled (boolean): Toggle for enabling or disabling location analytics for your network
        - upgradeStrategy (string): The default strategy that network devices will use to perform an upgrade. Requires firmware version MR 26.8 or higher.
        - ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
        - namedVlans (object): Named VLAN settings for wireless networks.
        """

        kwargs.update(locals())

        if 'upgradeStrategy' in kwargs:
            options = ['minimizeClientDowntime', 'minimizeUpgradeTime']
            assert kwargs['upgradeStrategy'] in options, f'''"upgradeStrategy" cannot be "{kwargs['upgradeStrategy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'settings'],
            'operation': 'updateNetworkWirelessSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/settings'

        body_params = ['meshingEnabled', 'ipv6BridgeEnabled', 'locationAnalyticsEnabled', 'upgradeStrategy', 'ledLightsOn', 'namedVlans', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSignalQualityHistory(self, networkId: str, **kwargs):
        """
        **Return signal quality (SNR/RSSI) over time for a device or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-signal-quality-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
        - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        - clientId (string): Filter results by network client.
        - deviceSerial (string): Filter results by device.
        - apTag (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
        - band (string): Filter results by band (either '2.4', '5' or '6').
        - ssid (integer): Filter results by SSID number.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'signalQualityHistory'],
            'operation': 'getNetworkWirelessSignalQualityHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/signalQualityHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkWirelessSsids(self, networkId: str):
        """
        **List the MR SSIDs in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'getNetworkWirelessSsids'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/ssids'

        return self._session.get(metadata, resource)
        


    def getNetworkWirelessSsid(self, networkId: str, number: str):
        """
        **Return a single MR SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'getNetworkWirelessSsid'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsid(self, networkId: str, number: str, **kwargs):
        """
        **Update the attributes of an MR SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid

        - networkId (string): Network ID
        - number (string): Number
        - name (string): The name of the SSID
        - enabled (boolean): Whether or not the SSID is enabled
        - localAuth (boolean): Extended local auth flag for Enterprise NAC
        - authMode (string): The association control method for the SSID ('open', 'open-enhanced', 'psk', 'open-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac', '8021x-radius', '8021x-google', '8021x-entra', '8021x-localradius', 'ipsk-with-radius', 'ipsk-without-radius', 'ipsk-with-nac' or 'ipsk-with-radius-easy-psk')
        - enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security')
        - dot11w (object): The current setting for Protected Management Frames (802.11w).
        - dot11r (object): The current setting for 802.11r
        - splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Microsoft Entra ID', 'Sponsored guest', 'Cisco ISE' or 'Google Apps domain'). This attribute is not supported for template children.
        - splashGuestSponsorDomains (array): Array of valid sponsor email domains for sponsored guest splash type.
        - oauth (object): The OAuth settings of this SSID. Only valid if splashPage is 'Google OAuth'.
        - localRadius (object): The current setting for Local Authentication, a built-in RADIUS server on the access point. Only valid if authMode is '8021x-localradius'.
        - ldap (object): The current setting for LDAP. Only valid if splashPage is 'Password-protected with LDAP'.
        - activeDirectory (object): The current setting for Active Directory. Only valid if splashPage is 'Password-protected with Active Directory'
        - radiusServers (array): The RADIUS 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusProxyEnabled (boolean): If true, Meraki devices will proxy RADIUS messages through the Meraki cloud to the configured RADIUS auth and accounting servers.
        - radiusTestingEnabled (boolean): If true, Meraki devices will periodically send Access-Request messages to configured RADIUS servers using identity 'meraki_8021x_test' to ensure that the RADIUS servers are reachable.
        - radiusCalledStationId (string): The template of the called station identifier to be used for RADIUS (ex. $NODE_MAC$:$VAP_NUM$).
        - radiusAuthenticationNasId (string): The template of the NAS identifier to be used for RADIUS authentication (ex. $NODE_MAC$:$VAP_NUM$).
        - radiusServerTimeout (integer): The amount of time for which a RADIUS client waits for a reply from the RADIUS server (must be between 1-10 seconds).
        - radiusServerAttemptsLimit (integer): The maximum number of transmit attempts after which a RADIUS server is failed over (must be between 1-5).
        - radiusFallbackEnabled (boolean): Whether or not higher priority RADIUS servers should be retried after 60 seconds.
        - radiusRadsec (object): The current settings for RADIUS RADSec
        - radiusCoaEnabled (boolean): If true, Meraki devices will act as a RADIUS Dynamic Authorization Server and will respond to RADIUS Change-of-Authorization and Disconnect messages sent by the RADIUS server.
        - radiusFailoverPolicy (string): This policy determines how authentication requests should be handled in the event that all of the configured RADIUS servers are unreachable ('Deny access' or 'Allow access')
        - radiusLoadBalancingPolicy (string): This policy determines which RADIUS server will be contacted first in an authentication attempt and the ordering of any necessary retry attempts ('Strict priority order' or 'Round robin')
        - radiusAccountingEnabled (boolean): Whether or not RADIUS accounting is enabled. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius'
        - radiusAccountingServers (array): The RADIUS accounting 802.1X servers to be used for authentication. This param is only valid if the authMode is 'open-with-radius', '8021x-radius' or 'ipsk-with-radius' and radiusAccountingEnabled is 'true'
        - radiusAccountingInterimInterval (integer): The interval (in seconds) in which accounting information is updated and sent to the RADIUS accounting server.
        - radiusAttributeForGroupPolicies (string): Specify the RADIUS attribute used to look up group policies ('Filter-Id', 'Reply-Message', 'Airespace-ACL-Name' or 'Aruba-User-Role'). Access points must receive this attribute in the RADIUS Access-Accept message
        - ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator' or 'VPN')
        - useVlanTagging (boolean): Whether or not traffic should be directed to use specific VLANs. This param is only valid if the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - concentratorNetworkId (string): The concentrator to use when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'.
        - secondaryConcentratorNetworkId (string): The secondary concentrator to use when the ipAssignmentMode is 'VPN'. If configured, the APs will switch to using this concentrator if the primary concentrator is unreachable. This param is optional. ('disabled' represents no secondary concentrator.)
        - disassociateClientsOnVpnFailover (boolean): Disassociate clients when 'VPN' concentrator failover occurs in order to trigger clients to re-associate and generate new DHCP requests. This param is only valid if ipAssignmentMode is 'VPN'.
        - vlanId (integer): The VLAN ID used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Layer 3 roaming with a concentrator' or 'VPN'
        - defaultVlanId (integer): The default VLAN ID used for 'all other APs'. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - apTagsAndVlanIds (array): The list of tags and VLAN IDs used for VLAN tagging. This param is only valid when the ipAssignmentMode is 'Bridge mode' or 'Layer 3 roaming'
        - walledGardenEnabled (boolean): Allow access to a configurable list of IP ranges, which users may access prior to sign-on.
        - walledGardenRanges (array): Specify your walled garden by entering an array of addresses, ranges using CIDR notation, domain names, and domain wildcards (e.g. '192.168.1.1/24', '192.168.37.10/32', 'www.yahoo.com', '*.google.com']). Meraki's splash page is automatically included in your walled garden.
        - gre (object): Ethernet over GRE settings
        - radiusOverride (boolean): If true, the RADIUS response can override VLAN tag. This is not valid when ipAssignmentMode is 'NAT mode'.
        - radiusGuestVlanEnabled (boolean): Whether or not RADIUS Guest VLAN is enabled. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
        - radiusGuestVlanId (integer): VLAN ID of the RADIUS Guest VLAN. This param is only valid if the authMode is 'open-with-radius' and addressing mode is not set to 'isolated' or 'nat' mode
        - minBitrate (number): The minimum bitrate in Mbps of this SSID in the default indoor RF profile. ('1', '2', '5.5', '6', '9', '11', '12', '18', '24', '36', '48' or '54')
        - bandSelection (string): The client-serving radio frequencies of this SSID in the default indoor RF profile. ('Dual band operation', '5 GHz band only' or 'Dual band operation with Band Steering')
        - perClientBandwidthLimitUp (integer): The upload bandwidth limit in Kbps. (0 represents no limit.)
        - perClientBandwidthLimitDown (integer): The download bandwidth limit in Kbps. (0 represents no limit.)
        - perSsidBandwidthLimitUp (integer): The total upload bandwidth limit in Kbps. (0 represents no limit.)
        - perSsidBandwidthLimitDown (integer): The total download bandwidth limit in Kbps. (0 represents no limit.)
        - lanIsolationEnabled (boolean): Boolean indicating whether Layer 2 LAN isolation should be enabled or disabled. Only configurable when ipAssignmentMode is 'Bridge mode'.
        - visible (boolean): Boolean indicating whether APs should advertise or hide this SSID. APs will only broadcast this SSID if set to true
        - availableOnAllAps (boolean): Boolean indicating whether all APs should broadcast the SSID or if it should be restricted to APs matching any availability tags. Can only be false if the SSID has availability tags.
        - availabilityTags (array): Accepts a list of tags for this SSID. If availableOnAllAps is false, then the SSID will only be broadcast by APs with tags matching any of the tags in this list.
        - adaptivePolicyGroupId (string): Adaptive policy group ID this SSID is assigned to.
        - mandatoryDhcpEnabled (boolean): If true, Mandatory DHCP will enforce that clients connecting to this SSID must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate.
        - adultContentFilteringEnabled (boolean): Boolean indicating whether or not adult content will be blocked
        - dnsRewrite (object): DNS servers rewrite settings
        - speedBurst (object): The SpeedBurst setting for this SSID'
        - namedVlans (object): Named VLAN settings.
        """

        kwargs.update(locals())

        if 'authMode' in kwargs:
            options = ['8021x-entra', '8021x-google', '8021x-localradius', '8021x-meraki', '8021x-nac', '8021x-radius', 'ipsk-with-nac', 'ipsk-with-radius', 'ipsk-with-radius-easy-psk', 'ipsk-without-radius', 'open', 'open-enhanced', 'open-with-nac', 'open-with-radius', 'psk']
            assert kwargs['authMode'] in options, f'''"authMode" cannot be "{kwargs['authMode']}", & must be set to one of: {options}'''
        if 'enterpriseAdminAccess' in kwargs:
            options = ['access disabled', 'access enabled']
            assert kwargs['enterpriseAdminAccess'] in options, f'''"enterpriseAdminAccess" cannot be "{kwargs['enterpriseAdminAccess']}", & must be set to one of: {options}'''
        if 'encryptionMode' in kwargs:
            options = ['open', 'wep', 'wpa', 'wpa-eap']
            assert kwargs['encryptionMode'] in options, f'''"encryptionMode" cannot be "{kwargs['encryptionMode']}", & must be set to one of: {options}'''
        if 'wpaEncryptionMode' in kwargs:
            options = ['WPA1 and WPA2', 'WPA1 only', 'WPA2 only', 'WPA3 192-bit Security', 'WPA3 Transition Mode', 'WPA3 only']
            assert kwargs['wpaEncryptionMode'] in options, f'''"wpaEncryptionMode" cannot be "{kwargs['wpaEncryptionMode']}", & must be set to one of: {options}'''
        if 'splashPage' in kwargs:
            options = ['Billing', 'Cisco ISE', 'Click-through splash page', 'Facebook Wi-Fi', 'Google Apps domain', 'Google OAuth', 'Microsoft Entra ID', 'None', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'SMS authentication', 'Sponsored guest', 'Systems Manager Sentry']
            assert kwargs['splashPage'] in options, f'''"splashPage" cannot be "{kwargs['splashPage']}", & must be set to one of: {options}'''
        if 'radiusFailoverPolicy' in kwargs:
            options = ['Allow access', 'Deny access']
            assert kwargs['radiusFailoverPolicy'] in options, f'''"radiusFailoverPolicy" cannot be "{kwargs['radiusFailoverPolicy']}", & must be set to one of: {options}'''
        if 'radiusLoadBalancingPolicy' in kwargs:
            options = ['Round robin', 'Strict priority order']
            assert kwargs['radiusLoadBalancingPolicy'] in options, f'''"radiusLoadBalancingPolicy" cannot be "{kwargs['radiusLoadBalancingPolicy']}", & must be set to one of: {options}'''
        if 'radiusAttributeForGroupPolicies' in kwargs:
            options = ['Airespace-ACL-Name', 'Aruba-User-Role', 'Filter-Id', 'Reply-Message']
            assert kwargs['radiusAttributeForGroupPolicies'] in options, f'''"radiusAttributeForGroupPolicies" cannot be "{kwargs['radiusAttributeForGroupPolicies']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids'],
            'operation': 'updateNetworkWirelessSsid'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}'

        body_params = ['name', 'enabled', 'localAuth', 'authMode', 'enterpriseAdminAccess', 'encryptionMode', 'psk', 'wpaEncryptionMode', 'dot11w', 'dot11r', 'splashPage', 'splashGuestSponsorDomains', 'oauth', 'localRadius', 'ldap', 'activeDirectory', 'radiusServers', 'radiusProxyEnabled', 'radiusTestingEnabled', 'radiusCalledStationId', 'radiusAuthenticationNasId', 'radiusServerTimeout', 'radiusServerAttemptsLimit', 'radiusFallbackEnabled', 'radiusRadsec', 'radiusCoaEnabled', 'radiusFailoverPolicy', 'radiusLoadBalancingPolicy', 'radiusAccountingEnabled', 'radiusAccountingServers', 'radiusAccountingInterimInterval', 'radiusAttributeForGroupPolicies', 'ipAssignmentMode', 'useVlanTagging', 'concentratorNetworkId', 'secondaryConcentratorNetworkId', 'disassociateClientsOnVpnFailover', 'vlanId', 'defaultVlanId', 'apTagsAndVlanIds', 'walledGardenEnabled', 'walledGardenRanges', 'gre', 'radiusOverride', 'radiusGuestVlanEnabled', 'radiusGuestVlanId', 'minBitrate', 'bandSelection', 'perClientBandwidthLimitUp', 'perClientBandwidthLimitDown', 'perSsidBandwidthLimitUp', 'perSsidBandwidthLimitDown', 'lanIsolationEnabled', 'visible', 'availableOnAllAps', 'availabilityTags', 'adaptivePolicyGroupId', 'mandatoryDhcpEnabled', 'adultContentFilteringEnabled', 'dnsRewrite', 'speedBurst', 'namedVlans', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidBonjourForwarding(self, networkId: str, number: str):
        """
        **List the Bonjour forwarding setting and rules for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-bonjour-forwarding

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'bonjourForwarding'],
            'operation': 'getNetworkWirelessSsidBonjourForwarding'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidBonjourForwarding(self, networkId: str, number: str, **kwargs):
        """
        **Update the bonjour forwarding setting and rules for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-bonjour-forwarding

        - networkId (string): Network ID
        - number (string): Number
        - enabled (boolean): If true, Bonjour forwarding is enabled on this SSID.
        - rules (array): List of bonjour forwarding rules.
        - exception (object): Bonjour forwarding exception
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'bonjourForwarding'],
            'operation': 'updateNetworkWirelessSsidBonjourForwarding'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding'

        body_params = ['enabled', 'rules', 'exception', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidDeviceTypeGroupPolicies(self, networkId: str, number: str):
        """
        **List the device type group policies for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-device-type-group-policies

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'deviceTypeGroupPolicies'],
            'operation': 'getNetworkWirelessSsidDeviceTypeGroupPolicies'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidDeviceTypeGroupPolicies(self, networkId: str, number: str, **kwargs):
        """
        **Update the device type group policies for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-device-type-group-policies

        - networkId (string): Network ID
        - number (string): Number
        - enabled (boolean): If true, the SSID device type group policies are enabled.
        - deviceTypePolicies (array): List of device type policies.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'deviceTypeGroupPolicies'],
            'operation': 'updateNetworkWirelessSsidDeviceTypeGroupPolicies'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies'

        body_params = ['enabled', 'deviceTypePolicies', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidEapOverride(self, networkId: str, number: str):
        """
        **Return the EAP overridden parameters for an SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-eap-override

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'eapOverride'],
            'operation': 'getNetworkWirelessSsidEapOverride'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/eapOverride'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidEapOverride(self, networkId: str, number: str, **kwargs):
        """
        **Update the EAP overridden parameters for an SSID.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-eap-override

        - networkId (string): Network ID
        - number (string): Number
        - timeout (integer): General EAP timeout in seconds.
        - identity (object): EAP settings for identity requests.
        - maxRetries (integer): Maximum number of general EAP retries.
        - eapolKey (object): EAPOL Key settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'eapOverride'],
            'operation': 'updateNetworkWirelessSsidEapOverride'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/eapOverride'

        body_params = ['timeout', 'identity', 'maxRetries', 'eapolKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str):
        """
        **Return the L3 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l3FirewallRules'],
            'operation': 'getNetworkWirelessSsidFirewallL3FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L3 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        - rules (array): An ordered array of the firewall rules for this SSID (not including the local LAN access rule or the default rule).
        - allowLanAccess (boolean): Allow wireless client access to local LAN (boolean value - true allows access and false denies access) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l3FirewallRules'],
            'operation': 'updateNetworkWirelessSsidFirewallL3FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules'

        body_params = ['rules', 'allowLanAccess', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidFirewallL7FirewallRules(self, networkId: str, number: str):
        """
        **Return the L7 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l7FirewallRules'],
            'operation': 'getNetworkWirelessSsidFirewallL7FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidFirewallL7FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L7 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-7-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        - rules (array): An array of L7 firewall rules for this SSID. Rules will get applied in the same order user has specified in request. Empty array will clear the L7 firewall rule configuration.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'l7FirewallRules'],
            'operation': 'updateNetworkWirelessSsidFirewallL7FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidHotspot20(self, networkId: str, number: str):
        """
        **Return the Hotspot 2.0 settings for an SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot-2-0

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'hotspot20'],
            'operation': 'getNetworkWirelessSsidHotspot20'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/hotspot20'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidHotspot20(self, networkId: str, number: str, **kwargs):
        """
        **Update the Hotspot 2.0 settings of an SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-hotspot-2-0

        - networkId (string): Network ID
        - number (string): Number
        - enabled (boolean): Whether or not Hotspot 2.0 for this SSID is enabled
        - operator (object): Operator settings for this SSID
        - venue (object): Venue settings for this SSID
        - networkAccessType (string): The network type of this SSID ('Private network', 'Private network with guest access', 'Chargeable public network', 'Free public network', 'Personal device network', 'Emergency services only network', 'Test or experimental', 'Wildcard')
        - domains (array): An array of domain names
        - roamConsortOis (array): An array of roaming consortium OIs (hexadecimal number 3-5 octets in length)
        - mccMncs (array): An array of MCC/MNC pairs
        - naiRealms (array): An array of NAI realms
        """

        kwargs.update(locals())

        if 'networkAccessType' in kwargs:
            options = ['Chargeable public network', 'Emergency services only network', 'Free public network', 'Personal device network', 'Private network', 'Private network with guest access', 'Test or experimental', 'Wildcard']
            assert kwargs['networkAccessType'] in options, f'''"networkAccessType" cannot be "{kwargs['networkAccessType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'hotspot20'],
            'operation': 'updateNetworkWirelessSsidHotspot20'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/hotspot20'

        body_params = ['enabled', 'operator', 'venue', 'networkAccessType', 'domains', 'roamConsortOis', 'mccMncs', 'naiRealms', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidIdentityPsks(self, networkId: str, number: str):
        """
        **List all Identity PSKs in a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'getNetworkWirelessSsidIdentityPsks'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks'

        return self._session.get(metadata, resource)
        


    def createNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, name: str, groupPolicyId: str, **kwargs):
        """
        **Create an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-identity-psk

        - networkId (string): Network ID
        - number (string): Number
        - name (string): The name of the Identity PSK
        - groupPolicyId (string): The group policy to be applied to clients
        - passphrase (string): The passphrase for client authentication. If left blank, one will be auto-generated.
        - expiresAt (string): Timestamp for when the Identity PSK expires. Will not expire if left blank.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'createNetworkWirelessSsidIdentityPsk'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks'

        body_params = ['name', 'passphrase', 'groupPolicyId', 'expiresAt', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, identityPskId: str):
        """
        **Return an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psk

        - networkId (string): Network ID
        - number (string): Number
        - identityPskId (string): Identity psk ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'getNetworkWirelessSsidIdentityPsk'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        identityPskId = urllib.parse.quote(str(identityPskId), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, identityPskId: str, **kwargs):
        """
        **Update an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-identity-psk

        - networkId (string): Network ID
        - number (string): Number
        - identityPskId (string): Identity psk ID
        - name (string): The name of the Identity PSK
        - passphrase (string): The passphrase for client authentication
        - groupPolicyId (string): The group policy to be applied to clients
        - expiresAt (string): Timestamp for when the Identity PSK expires, or 'null' to never expire
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'updateNetworkWirelessSsidIdentityPsk'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        identityPskId = urllib.parse.quote(str(identityPskId), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}'

        body_params = ['name', 'passphrase', 'groupPolicyId', 'expiresAt', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkWirelessSsidIdentityPsk(self, networkId: str, number: str, identityPskId: str):
        """
        **Delete an Identity PSK**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ssid-identity-psk

        - networkId (string): Network ID
        - number (string): Number
        - identityPskId (string): Identity psk ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'identityPsks'],
            'operation': 'deleteNetworkWirelessSsidIdentityPsk'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        identityPskId = urllib.parse.quote(str(identityPskId), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkWirelessSsidSchedules(self, networkId: str, number: str):
        """
        **List the outage schedule for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-schedules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'schedules'],
            'operation': 'getNetworkWirelessSsidSchedules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/schedules'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidSchedules(self, networkId: str, number: str, **kwargs):
        """
        **Update the outage schedule for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-schedules

        - networkId (string): Network ID
        - number (string): Number
        - enabled (boolean): If true, the SSID outage schedule is enabled.
        - ranges (array): List of outage ranges. Has a start date and time, and end date and time. If this parameter is passed in along with rangesInSeconds parameter, this will take precedence.
        - rangesInSeconds (array): List of outage ranges in seconds since Sunday at Midnight. Has a start and end. If this parameter is passed in along with the ranges parameter, ranges will take precedence.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'schedules'],
            'operation': 'updateNetworkWirelessSsidSchedules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/schedules'

        body_params = ['enabled', 'ranges', 'rangesInSeconds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidSplashSettings(self, networkId: str, number: str):
        """
        **Display the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'splash', 'settings'],
            'operation': 'getNetworkWirelessSsidSplashSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/splash/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidSplashSettings(self, networkId: str, number: str, **kwargs):
        """
        **Modify the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-splash-settings

        - networkId (string): Network ID
        - number (string): Number
        - splashUrl (string): [optional] The custom splash URL of the click-through splash page. Note that the URL can be configured without necessarily being used. In order to enable the custom URL, see 'useSplashUrl'
        - useSplashUrl (boolean): [optional] Boolean indicating whether the users will be redirected to the custom splash url. A custom splash URL must be set if this is true. Note that depending on your SSID's access control settings, it may not be possible to use the custom splash URL.
        - splashTimeout (integer): Splash timeout in minutes. This will determine how often users will see the splash page.
        - redirectUrl (string): The custom redirect URL where the users will go after the splash page.
        - useRedirectUrl (boolean): The Boolean indicating whether the the user will be redirected to the custom redirect URL after the splash page. A custom redirect URL must be set if this is true.
        - welcomeMessage (string): The welcome message for the users on the splash page.
        - themeId (string): The id of the selected splash theme.
        - splashLogo (object): The logo used in the splash page.
        - splashImage (object): The image used in the splash page.
        - splashPrepaidFront (object): The prepaid front image used in the splash page.
        - blockAllTrafficBeforeSignOn (boolean): How restricted allowing traffic should be. If true, all traffic types are blocked until the splash page is acknowledged. If false, all non-HTTP traffic is allowed before the splash page is acknowledged.
        - controllerDisconnectionBehavior (string): How login attempts should be handled when the controller is unreachable. Can be either 'open', 'restricted', or 'default'.
        - allowSimultaneousLogins (boolean): Whether or not to allow simultaneous logins from different devices.
        - guestSponsorship (object): Details associated with guest sponsored splash.
        - billing (object): Details associated with billing splash.
        - sentryEnrollment (object): Systems Manager sentry enrollment splash settings.
        - selfRegistration (object): Self-registration settings for splash with Meraki authentication.
        """

        kwargs.update(locals())

        if 'splashTimeout' in kwargs:
            options = [30, 60, 120, 240, 480, 720, 1080, 1440, 2880, 5760, 7200, 10080, 20160, 43200, 86400, 129600]
            assert kwargs['splashTimeout'] in options, f'''"splashTimeout" cannot be "{kwargs['splashTimeout']}", & must be set to one of: {options}'''
        if 'controllerDisconnectionBehavior' in kwargs:
            options = ['default', 'open', 'restricted']
            assert kwargs['controllerDisconnectionBehavior'] in options, f'''"controllerDisconnectionBehavior" cannot be "{kwargs['controllerDisconnectionBehavior']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'splash', 'settings'],
            'operation': 'updateNetworkWirelessSsidSplashSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/splash/settings'

        body_params = ['splashUrl', 'useSplashUrl', 'splashTimeout', 'redirectUrl', 'useRedirectUrl', 'welcomeMessage', 'themeId', 'splashLogo', 'splashImage', 'splashPrepaidFront', 'blockAllTrafficBeforeSignOn', 'controllerDisconnectionBehavior', 'allowSimultaneousLogins', 'guestSponsorship', 'billing', 'sentryEnrollment', 'selfRegistration', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def updateNetworkWirelessSsidTrafficShapingRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the traffic shaping rules for an SSID on an MR network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-traffic-shaping-rules

        - networkId (string): Network ID
        - number (string): Number
        - trafficShapingEnabled (boolean): Whether traffic shaping rules are applied to clients on your SSID.
        - defaultRulesEnabled (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'trafficShaping', 'rules'],
            'operation': 'updateNetworkWirelessSsidTrafficShapingRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules'

        body_params = ['trafficShapingEnabled', 'defaultRulesEnabled', 'rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessSsidTrafficShapingRules(self, networkId: str, number: str):
        """
        **Display the traffic shaping settings for a SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'trafficShaping', 'rules'],
            'operation': 'getNetworkWirelessSsidTrafficShapingRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules'

        return self._session.get(metadata, resource)
        


    def getNetworkWirelessSsidVpn(self, networkId: str, number: str):
        """
        **List the VPN settings for the SSID.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-vpn

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'vpn'],
            'operation': 'getNetworkWirelessSsidVpn'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/vpn'

        return self._session.get(metadata, resource)
        


    def updateNetworkWirelessSsidVpn(self, networkId: str, number: str, **kwargs):
        """
        **Update the VPN settings for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-vpn

        - networkId (string): Network ID
        - number (string): Number
        - concentrator (object): The VPN concentrator settings for this SSID.
        - splitTunnel (object): The VPN split tunnel settings for this SSID.
        - failover (object): Secondary VPN concentrator settings. This is only used when two VPN concentrators are configured on the SSID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'vpn'],
            'operation': 'updateNetworkWirelessSsidVpn'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/wireless/ssids/{number}/vpn'

        body_params = ['concentrator', 'splitTunnel', 'failover', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkWirelessUsageHistory(self, networkId: str, **kwargs):
        """
        **Return AP usage over time for a device or network client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-usage-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 1200, 3600, 14400, 86400. The default is 86400.
        - autoResolution (boolean): Automatically select a data resolution based on the given timespan; this overrides the value specified by the 'resolution' parameter. The default setting is false.
        - clientId (string): Filter results by network client to return per-device AP usage over time inner joined by the queried client's connection history.
        - deviceSerial (string): Filter results by device. Requires :band.
        - apTag (string): Filter results by AP tag; either :clientId or :deviceSerial must be jointly specified.
        - band (string): Filter results by band (either '2.4', '5' or '6').
        - ssid (integer): Filter results by SSID number.
        """

        kwargs.update(locals())

        if 'band' in kwargs:
            options = ['2.4', '5', '6']
            assert kwargs['band'] in options, f'''"band" cannot be "{kwargs['band']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['wireless', 'monitor', 'usageHistory'],
            'operation': 'getNetworkWirelessUsageHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/wireless/usageHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'autoResolution', 'clientId', 'deviceSerial', 'apTag', 'band', 'ssid', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationWirelessAirMarshalRules(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns the current Air Marshal rules for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-air-marshal-rules

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): (optional) The set of network IDs to include.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'airMarshal', 'rules'],
            'operation': 'getOrganizationWirelessAirMarshalRules'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/airMarshal/rules'

        query_params = ['networkIds', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessAirMarshalSettingsByNetwork(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns the current Air Marshal settings for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-air-marshal-settings-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): The network IDs to include in the result set.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'airMarshal', 'settings', 'byNetwork'],
            'operation': 'getOrganizationWirelessAirMarshalSettingsByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/airMarshal/settings/byNetwork'

        query_params = ['networkIds', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessClientsOverviewByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List access point client count at the moment in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-overview-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter access points client counts by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter access points client counts by its serial numbers. This filter uses multiple exact matches.
        - campusGatewayClusterIds (array): Optional parameter to filter access points client counts by MCG cluster IDs. This filter uses multiple exact matches.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'clients', 'overview', 'byDevice'],
            'operation': 'getOrganizationWirelessClientsOverviewByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/clients/overview/byDevice'

        query_params = ['networkIds', 'serials', 'campusGatewayClusterIds', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'campusGatewayClusterIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesChannelUtilizationByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get average channel utilization for all bands in a network, split by AP**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'channelUtilization', 'byDevice'],
            'operation': 'getOrganizationWirelessDevicesChannelUtilizationByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/channelUtilization/byDevice'

        query_params = ['networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesChannelUtilizationByNetwork(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get average channel utilization across all bands for all networks in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'channelUtilization', 'byNetwork'],
            'operation': 'getOrganizationWirelessDevicesChannelUtilizationByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/channelUtilization/byNetwork'

        query_params = ['networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get a time-series of average channel utilization for all bands, segmented by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-device-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'channelUtilization', 'history', 'byDevice', 'byInterval'],
            'operation': 'getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/channelUtilization/history/byDevice/byInterval'

        query_params = ['networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get a time-series of average channel utilization for all bands**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-channel-utilization-history-by-network-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 7200, 14400, 21600. The default is 3600.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'channelUtilization', 'history', 'byNetwork', 'byInterval'],
            'operation': 'getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/channelUtilization/history/byNetwork/byInterval'

        query_params = ['networkIds', 'serials', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'interval', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesEthernetStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the most recent Ethernet link speed, duplex, aggregation and power mode and status information for wireless devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-ethernet-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'ethernet', 'statuses'],
            'operation': 'getOrganizationWirelessDevicesEthernetStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/ethernet/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesPacketLossByClient(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get average packet loss for the given timespan for all clients in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - macs (array): Filter results by client mac address(es).
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'packetLoss', 'byClient'],
            'operation': 'getOrganizationWirelessDevicesPacketLossByClient'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/packetLoss/byClient'

        query_params = ['networkIds', 'ssids', 'bands', 'macs', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'ssids', 'bands', 'macs', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesPacketLossByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get average packet loss for the given timespan for all devices in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'packetLoss', 'byDevice'],
            'operation': 'getOrganizationWirelessDevicesPacketLossByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/packetLoss/byDevice'

        query_params = ['networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'ssids', 'bands', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesPacketLossByNetwork(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get average packet loss for the given timespan for all networks in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-packet-loss-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 90 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'packetLoss', 'byNetwork'],
            'operation': 'getOrganizationWirelessDevicesPacketLossByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/packetLoss/byNetwork'

        query_params = ['networkIds', 'serials', 'ssids', 'bands', 'perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'ssids', 'bands', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesPowerModeHistory(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return a record of power mode changes for wireless devices in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-power-mode-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        - serials (array): Optional parameter to filter device availabilities history by device serial numbers
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'power', 'mode', 'history'],
            'operation': 'getOrganizationWirelessDevicesPowerModeHistory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/power/mode/history'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesRadsecCertificatesAuthorities(self, organizationId: str, **kwargs):
        """
        **Query for details on the organization's RADSEC device Certificate Authority certificates (CAs)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities

        - organizationId (string): Organization ID
        - certificateAuthorityIds (array): Optional parameter to filter CAs by one or more CA IDs. All returned CAs will have an ID that is an exact match.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'devices', 'radsec', 'certificates', 'authorities'],
            'operation': 'getOrganizationWirelessDevicesRadsecCertificatesAuthorities'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities'

        query_params = ['certificateAuthorityIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['certificateAuthorityIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def updateOrganizationWirelessDevicesRadsecCertificatesAuthorities(self, organizationId: str, **kwargs):
        """
        **Update an organization's RADSEC device Certificate Authority (CA) state**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-devices-radsec-certificates-authorities

        - organizationId (string): Organization ID
        - status (string): The "status" to update the Certificate Authority to. Only valid option is "trusted".
        - certificateAuthorityId (string): The ID of the Certificate Authority to update.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'devices', 'radsec', 'certificates', 'authorities'],
            'operation': 'updateOrganizationWirelessDevicesRadsecCertificatesAuthorities'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities'

        body_params = ['status', 'certificateAuthorityId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def createOrganizationWirelessDevicesRadsecCertificatesAuthority(self, organizationId: str):
        """
        **Create an organization's RADSEC device Certificate Authority (CA)**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-radsec-certificates-authority

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'devices', 'radsec', 'certificates', 'authorities'],
            'operation': 'createOrganizationWirelessDevicesRadsecCertificatesAuthority'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities'

        return self._session.post(metadata, resource)
        


    def getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrls(self, organizationId: str, **kwargs):
        """
        **Query for certificate revocation list (CRL) for the organization's RADSEC device Certificate Authorities (CAs).**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities-crls

        - organizationId (string): Organization ID
        - certificateAuthorityIds (array): Optional parameter to filter CAs by one or more CA IDs. All returned CAs will have an ID that is an exact match.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'devices', 'radsec', 'certificates', 'authorities', 'crls'],
            'operation': 'getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrls'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities/crls'

        query_params = ['certificateAuthorityIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['certificateAuthorityIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrlsDeltas(self, organizationId: str, **kwargs):
        """
        **Query for all delta certificate revocation list (CRL) for the organization's RADSEC device Certificate Authority (CA) with the given id.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities-crls-deltas

        - organizationId (string): Organization ID
        - certificateAuthorityIds (array): Parameter to filter CAs by one or more CA IDs. All returned CAs will have an ID that is an exact match.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'devices', 'radsec', 'certificates', 'authorities', 'crls', 'deltas'],
            'operation': 'getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrlsDeltas'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities/crls/deltas'

        query_params = ['certificateAuthorityIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['certificateAuthorityIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationWirelessDevicesSystemCpuLoadHistory(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the CPU Load history for a list of wireless devices in the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-system-cpu-load-history

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 1 day from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 1 day after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 1 day. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 20. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        - serials (array): Optional parameter to filter device availabilities history by device serial numbers
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'system', 'cpu', 'load', 'history'],
            'operation': 'getOrganizationWirelessDevicesSystemCpuLoadHistory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/system/cpu/load/history'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessDevicesWirelessControllersByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List of Catalyst access points information**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-wireless-controllers-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter access points by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter access points by its cloud ID. This filter uses multiple exact matches.
        - controllerSerials (array): Optional parameter to filter access points by its wireless LAN controller cloud ID. This filter uses multiple exact matches.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'devices', 'wirelessControllers', 'byDevice'],
            'operation': 'getOrganizationWirelessDevicesWirelessControllersByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/devices/wirelessControllers/byDevice'

        query_params = ['networkIds', 'serials', 'controllerSerials', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'controllerSerials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessLocationScanningByNetwork(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return scanning API settings**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-scanning-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 250. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter scanning settings by network ID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'location', 'scanning', 'byNetwork'],
            'operation': 'getOrganizationWirelessLocationScanningByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/location/scanning/byNetwork'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessLocationScanningReceivers(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return scanning API receivers**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-scanning-receivers

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 250. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter scanning API receivers by network ID.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'location', 'scanning', 'receivers'],
            'operation': 'getOrganizationWirelessLocationScanningReceivers'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/location/scanning/receivers'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def createOrganizationWirelessLocationScanningReceiver(self, organizationId: str, network: dict, url: str, version: str, radio: dict, sharedSecret: str):
        """
        **Add new receiver for scanning API**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-location-scanning-receiver

        - organizationId (string): Organization ID
        - network (object): Add scanning API receiver for network
        - url (string): Receiver Url
        - version (string): Scanning API Version
        - radio (object): Add scanning API Radio
        - sharedSecret (string): Secret Value for Receiver
        """

        kwargs = locals()

        metadata = {
            'tags': ['wireless', 'configure', 'location', 'scanning', 'receivers'],
            'operation': 'createOrganizationWirelessLocationScanningReceiver'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/location/scanning/receivers'

        body_params = ['network', 'url', 'version', 'radio', 'sharedSecret', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateOrganizationWirelessLocationScanningReceiver(self, organizationId: str, receiverId: str, **kwargs):
        """
        **Change scanning API receiver settings**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-location-scanning-receiver

        - organizationId (string): Organization ID
        - receiverId (string): Receiver ID
        - url (string): Receiver Url
        - version (string): Scanning API Version
        - radio (object): Add scanning API Radio
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'location', 'scanning', 'receivers'],
            'operation': 'updateOrganizationWirelessLocationScanningReceiver'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        receiverId = urllib.parse.quote(str(receiverId), safe='')
        resource = f'/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}'

        body_params = ['url', 'version', 'radio', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationWirelessLocationScanningReceiver(self, organizationId: str, receiverId: str):
        """
        **Delete a scanning API receiver**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-location-scanning-receiver

        - organizationId (string): Organization ID
        - receiverId (string): Receiver ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'location', 'scanning', 'receivers'],
            'operation': 'deleteOrganizationWirelessLocationScanningReceiver'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        receiverId = urllib.parse.quote(str(receiverId), safe='')
        resource = f'/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}'

        return self._session.delete(metadata, resource)
        


    def recalculateOrganizationWirelessRadioAutoRfChannels(self, organizationId: str, networkIds: list):
        """
        **Recalculates automatically assigned channels for every AP within specified the specified network(s)**
        https://developer.cisco.com/meraki/api-v1/#!recalculate-organization-wireless-radio-auto-rf-channels

        - organizationId (string): Organization ID
        - networkIds (array): A list of network ids (limit: 15).
        """

        kwargs = locals()

        metadata = {
            'tags': ['wireless', 'configure', 'radio', 'autoRf', 'channels'],
            'operation': 'recalculateOrganizationWirelessRadioAutoRfChannels'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/radio/autoRf/channels/recalculate'

        body_params = ['networkIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationWirelessRfProfilesAssignmentsByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the RF profiles of an organization by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-rf-profiles-assignments-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter devices by network.
        - productTypes (array): Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, sensor, wirelessController, campusGateway, and secureConnect.
        - name (string): Optional parameter to filter RF profiles by device name. All returned devices will have a name that contains the search term or is an exact match.
        - mac (string): Optional parameter to filter RF profiles by device MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
        - serial (string): Optional parameter to filter RF profiles by device serial number. All returned devices will have a serial number that contains the search term or is an exact match.
        - model (string): Optional parameter to filter RF profiles by device model. All returned devices will have a model that contains the search term or is an exact match.
        - macs (array): Optional parameter to filter RF profiles by one or more device MAC addresses. All returned devices will have a MAC address that is an exact match.
        - serials (array): Optional parameter to filter RF profiles by one or more device serial numbers. All returned devices will have a serial number that is an exact match.
        - models (array): Optional parameter to filter RF profiles by one or more device models. All returned devices will have a model that is an exact match.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'rfProfiles', 'assignments', 'byDevice'],
            'operation': 'getOrganizationWirelessRfProfilesAssignmentsByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/rfProfiles/assignments/byDevice'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'models', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'productTypes', 'macs', 'serials', 'models', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the L2 isolation allow list MAC entry in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-firewall-isolation-allowlist-entries

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): networkIds array to filter out results
        - ssids (array): ssids number array to filter out results
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'isolation', 'allowlist', 'entries'],
            'operation': 'getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'ssids', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'ssids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(self, organizationId: str, client: dict, ssid: dict, network: dict, **kwargs):
        """
        **Create isolation allow list MAC entry for this organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-firewall-isolation-allowlist-entry

        - organizationId (string): Organization ID
        - client (object): The client of allowlist
        - ssid (object): The SSID that allowlist belongs to
        - network (object): The Network that allowlist belongs to
        - description (string): The description of mac address
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'isolation', 'allowlist', 'entries'],
            'operation': 'createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries'

        body_params = ['description', 'client', 'ssid', 'network', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(self, organizationId: str, entryId: str):
        """
        **Destroy isolation allow list MAC entry for this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-firewall-isolation-allowlist-entry

        - organizationId (string): Organization ID
        - entryId (string): Entry ID
        """

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'isolation', 'allowlist', 'entries'],
            'operation': 'deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        entryId = urllib.parse.quote(str(entryId), safe='')
        resource = f'/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}'

        return self._session.delete(metadata, resource)
        


    def updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(self, organizationId: str, entryId: str, **kwargs):
        """
        **Update isolation allow list MAC entry info**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-ssids-firewall-isolation-allowlist-entry

        - organizationId (string): Organization ID
        - entryId (string): Entry ID
        - description (string): The description of mac address
        - client (object): The client of allowlist
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'configure', 'ssids', 'firewall', 'isolation', 'allowlist', 'entries'],
            'operation': 'updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        entryId = urllib.parse.quote(str(entryId), safe='')
        resource = f'/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}'

        body_params = ['description', 'client', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationWirelessSsidsStatusesByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List status information of all BSSIDs in your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-statuses-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter the result set by the included set of network IDs
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - bssids (array): A list of BSSIDs. The returned devices will be filtered to only include these BSSIDs.
        - hideDisabled (boolean): If true, the returned devices will not include disabled SSIDs. (default: true)
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['wireless', 'monitor', 'ssids', 'statuses', 'byDevice'],
            'operation': 'getOrganizationWirelessSsidsStatusesByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/wireless/ssids/statuses/byDevice'

        query_params = ['networkIds', 'serials', 'bssids', 'hideDisabled', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'bssids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
