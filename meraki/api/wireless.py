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
            "tags": ["wireless", "configure", "alternateManagementInterface", "ipv6"],
            "operation": "updateDeviceWirelessAlternateManagementInterfaceIpv6",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/alternateManagementInterface/ipv6"

        body_params = [
            "addresses",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateDeviceWirelessAlternateManagementInterfaceIpv6: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getDeviceWirelessBluetoothSettings(self, serial: str):
        """
        **Return the bluetooth settings for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-bluetooth-settings

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "getDeviceWirelessBluetoothSettings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/bluetooth/settings"

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
        - transmit (object): Transmit settings including power, interval, and advertised power.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "updateDeviceWirelessBluetoothSettings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/bluetooth/settings"

        body_params = [
            "uuid",
            "major",
            "minor",
            "transmit",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateDeviceWirelessBluetoothSettings: ignoring unrecognized kwargs: {invalid}"
                )

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
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "connectionStats"],
            "operation": "getDeviceWirelessConnectionStats",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceWirelessConnectionStats: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getDeviceWirelessElectronicShelfLabel(self, serial: str):
        """
        **Return the ESL settings of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-electronic-shelf-label

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "getDeviceWirelessElectronicShelfLabel",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/electronicShelfLabel"

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
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "updateDeviceWirelessElectronicShelfLabel",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/electronicShelfLabel"

        body_params = [
            "channel",
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateDeviceWirelessElectronicShelfLabel: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getDeviceWirelessHealthScores(self, serial: str):
        """
        **Fetch the health scores for a given AP on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-health-scores

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "monitor", "healthScores"],
            "operation": "getDeviceWirelessHealthScores",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/healthScores"

        return self._session.get(metadata, resource)

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
        - apTag (string): Filter results by AP Tag
        - vlan (integer): Filter results by VLAN
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "latencyStats"],
            "operation": "getDeviceWirelessLatencyStats",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceWirelessLatencyStats: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getDeviceWirelessRadioAfcPosition(self, serial: str):
        """
        **Return the position for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-afc-position

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "radio", "afc", "position"],
            "operation": "getDeviceWirelessRadioAfcPosition",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/afc/position"

        return self._session.get(metadata, resource)

    def updateDeviceWirelessRadioAfcPosition(self, serial: str, **kwargs):
        """
        **Update the position attributes for this device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-afc-position

        - serial (string): Serial
        - height (object): Height attributes
        - gps (object): GPS attributes
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "afc", "position"],
            "operation": "updateDeviceWirelessRadioAfcPosition",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/afc/position"

        body_params = [
            "height",
            "gps",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceWirelessRadioAfcPosition: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getDeviceWirelessRadioAfcPowerLimits(self, serial: str):
        """
        **Return the AFC power limits for a wireless device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-afc-power-limits

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "radio", "afc", "powerLimits"],
            "operation": "getDeviceWirelessRadioAfcPowerLimits",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/afc/powerLimits"

        return self._session.get(metadata, resource)

    def getDeviceWirelessRadioOverrides(self, serial: str):
        """
        **Return the radio overrides of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-overrides

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "radio", "overrides"],
            "operation": "getDeviceWirelessRadioOverrides",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/overrides"

        return self._session.get(metadata, resource)

    def updateDeviceWirelessRadioOverrides(self, serial: str, **kwargs):
        """
        **Update 2.4 GHz, 5 GHz, and 6 GHz radio settings (channel, channel width, power, and enable/disable) that override RF profiles.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-overrides

        - serial (string): Serial
        - rfProfile (object): This device's RF profile
        - radios (array): Radio overrides.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "overrides"],
            "operation": "updateDeviceWirelessRadioOverrides",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/overrides"

        body_params = [
            "rfProfile",
            "radios",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceWirelessRadioOverrides: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getDeviceWirelessRadioSettings(self, serial: str):
        """
        **Return the manually configured radio settings overrides of a device, which take precedence over RF profiles.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-settings

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "radio", "settings"],
            "operation": "getDeviceWirelessRadioSettings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/settings"

        return self._session.get(metadata, resource)

    def updateDeviceWirelessRadioSettings(self, serial: str, **kwargs):
        """
        **Update 2.4 GHz and 5 GHz radio settings (channel, channel width, power) that override RF profiles**
        https://developer.cisco.com/meraki/api-v1/#!update-device-wireless-radio-settings

        - serial (string): Serial
        - rfProfileId (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
        - twoFourGhzSettings (object): Manual radio settings for 2.4 GHz.
        - fiveGhzSettings (object): Manual radio settings for 5 GHz.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "settings"],
            "operation": "updateDeviceWirelessRadioSettings",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/settings"

        body_params = [
            "rfProfileId",
            "twoFourGhzSettings",
            "fiveGhzSettings",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceWirelessRadioSettings: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getDeviceWirelessRadioStatus(self, serial: str):
        """
        **Show the status of this device's radios**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-radio-status

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "radio", "status"],
            "operation": "getDeviceWirelessRadioStatus",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/radio/status"

        return self._session.get(metadata, resource)

    def getDeviceWirelessStatus(self, serial: str):
        """
        **Return the SSID statuses of an access point**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-status

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "monitor", "status"],
            "operation": "getDeviceWirelessStatus",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/status"

        return self._session.get(metadata, resource)

    def createDeviceWirelessZigbeeEnrollment(self, serial: str):
        """
        **Enqueue a job to start enrolling door locks on zigbee configured wireless devices**
        https://developer.cisco.com/meraki/api-v1/#!create-device-wireless-zigbee-enrollment

        - serial (string): Serial
        """

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "enrollments"],
            "operation": "createDeviceWirelessZigbeeEnrollment",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/wireless/zigbee/enrollments"

        return self._session.post(metadata, resource)

    def getDeviceWirelessZigbeeEnrollment(self, serial: str, enrollmentId: str):
        """
        **Return an enrollment**
        https://developer.cisco.com/meraki/api-v1/#!get-device-wireless-zigbee-enrollment

        - serial (string): Serial
        - enrollmentId (string): Enrollment ID
        """

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "enrollments"],
            "operation": "getDeviceWirelessZigbeeEnrollment",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        enrollmentId = urllib.parse.quote(str(enrollmentId), safe="")
        resource = f"/devices/{serial}/wireless/zigbee/enrollments/{enrollmentId}"

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
            "tags": ["wireless", "monitor", "airMarshal"],
            "operation": "getNetworkWirelessAirMarshal",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal"

        query_params = [
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessAirMarshal: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def createNetworkWirelessAirMarshalRule(self, networkId: str, type: str, match: dict, **kwargs):
        """
        **Creates a new rule**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-air-marshal-rule

        - networkId (string): Network ID
        - type (string): Indicates if this rule will allow, block, or alert.
        - match (object): Object describing the rule specification.
        """

        kwargs = locals()

        if "type" in kwargs:
            options = ["alert", "allow", "block"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "createNetworkWirelessAirMarshalRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/rules"

        body_params = [
            "type",
            "match",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkWirelessAirMarshalRule: ignoring unrecognized kwargs: {invalid}")

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

        if "type" in kwargs:
            options = ["alert", "allow", "block"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "updateNetworkWirelessAirMarshalRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/rules/{ruleId}"

        body_params = [
            "type",
            "match",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessAirMarshalRule: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkWirelessAirMarshalRule(self, networkId: str, ruleId: str):
        """
        **Delete an Air Marshal rule.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-air-marshal-rule

        - networkId (string): Network ID
        - ruleId (string): Rule ID
        """

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "deleteNetworkWirelessAirMarshalRule",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        ruleId = urllib.parse.quote(str(ruleId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/rules/{ruleId}"

        return self._session.delete(metadata, resource)

    def updateNetworkWirelessAirMarshalSettings(self, networkId: str, defaultPolicy: str, **kwargs):
        """
        **Updates Air Marshal settings.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-air-marshal-settings

        - networkId (string): Network ID
        - defaultPolicy (string): Allows clients to access rogue networks. Blocked by default.
        """

        kwargs = locals()

        if "defaultPolicy" in kwargs:
            options = ["allow", "block"]
            assert kwargs["defaultPolicy"] in options, (
                f'''"defaultPolicy" cannot be "{kwargs["defaultPolicy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "airMarshal", "settings"],
            "operation": "updateNetworkWirelessAirMarshalSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/airMarshal/settings"

        body_params = [
            "defaultPolicy",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessAirMarshalSettings: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessAlternateManagementInterface(self, networkId: str):
        """
        **Return alternate management interface and devices with IP assigned**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-alternate-management-interface

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "alternateManagementInterface"],
            "operation": "getNetworkWirelessAlternateManagementInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/alternateManagementInterface"

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
            "tags": ["wireless", "configure", "alternateManagementInterface"],
            "operation": "updateNetworkWirelessAlternateManagementInterface",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/alternateManagementInterface"

        body_params = [
            "enabled",
            "vlanId",
            "protocols",
            "accessPoints",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessAlternateManagementInterface: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessBilling(self, networkId: str):
        """
        **Return the billing settings of this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-billing

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "billing"],
            "operation": "getNetworkWirelessBilling",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/billing"

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
            "tags": ["wireless", "configure", "billing"],
            "operation": "updateNetworkWirelessBilling",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/billing"

        body_params = [
            "currency",
            "plans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessBilling: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessBluetoothSettings(self, networkId: str):
        """
        **Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-bluetooth-settings

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "getNetworkWirelessBluetoothSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/bluetooth/settings"

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
        - transmit (object): Transmit settings.
        """

        kwargs.update(locals())

        if "majorMinorAssignmentMode" in kwargs:
            options = ["Non-unique", "Unique"]
            assert kwargs["majorMinorAssignmentMode"] in options, (
                f'''"majorMinorAssignmentMode" cannot be "{kwargs["majorMinorAssignmentMode"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "bluetooth", "settings"],
            "operation": "updateNetworkWirelessBluetoothSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/bluetooth/settings"

        body_params = [
            "scanningEnabled",
            "advertisingEnabled",
            "uuid",
            "majorMinorAssignmentMode",
            "major",
            "minor",
            "transmit",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessBluetoothSettings: ignoring unrecognized kwargs: {invalid}"
                )

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

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "channelUtilizationHistory"],
            "operation": "getNetworkWirelessChannelUtilizationHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/channelUtilizationHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessChannelUtilizationHistory: ignoring unrecognized kwargs: {invalid}"
                )

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

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "clientCountHistory"],
            "operation": "getNetworkWirelessClientCountHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clientCountHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessClientCountHistory: ignoring unrecognized kwargs: {invalid}")

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
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectionStats"],
            "operation": "getNetworkWirelessClientsConnectionStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessClientsConnectionStats: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessClientsHealthScores(self, networkId: str):
        """
        **Fetch the health scores for all clients on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-health-scores

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "monitor", "clients", "healthScores"],
            "operation": "getNetworkWirelessClientsHealthScores",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/healthScores"

        return self._session.get(metadata, resource)

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
        - apTag (string): Filter results by AP Tag
        - vlan (integer): Filter results by VLAN
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyStats"],
            "operation": "getNetworkWirelessClientsLatencyStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessClientsLatencyStats: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessClientsOnboardingHistory(self, networkId: str, **kwargs):
        """
        **Return counts of distinct wireless clients connecting to a network over time**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-clients-onboarding-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300. The default is 300.
        - band (string): Filter results by band (either '2.4', '5' or '6'); this cannot be combined with the SSID filter.
        - ssid (integer): Filter results by SSID number; this cannot be combined with the band filter.
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "clients", "onboardingHistory"],
            "operation": "getNetworkWirelessClientsOnboardingHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/onboardingHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessClientsOnboardingHistory: ignoring unrecognized kwargs: {invalid}"
                )

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
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectionStats"],
            "operation": "getNetworkWirelessClientConnectionStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessClientConnectionStats: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessClientConnectivityEvents(
        self, networkId: str, clientId: str, total_pages=1, direction="next", **kwargs
    ):
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

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssidNumber" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssidNumber"] in options, (
                f'''"ssidNumber" cannot be "{kwargs["ssidNumber"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connectivityEvents"],
            "operation": "getNetworkWirelessClientConnectivityEvents",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/connectivityEvents"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "sortOrder",
            "t0",
            "t1",
            "timespan",
            "types",
            "band",
            "ssidNumber",
            "includedSeverities",
            "deviceSerial",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "types",
            "includedSeverities",
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
                    f"getNetworkWirelessClientConnectivityEvents: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkWirelessClientHealthScores(self, networkId: str, clientId: str):
        """
        **Fetch the health scores for a given client on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-health-scores

        - networkId (string): Network ID
        - clientId (string): Client ID
        """

        metadata = {
            "tags": ["wireless", "monitor", "clients", "healthScores"],
            "operation": "getNetworkWirelessClientHealthScores",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/healthScores"

        return self._session.get(metadata, resource)

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
            "tags": ["wireless", "monitor", "clients", "latencyHistory"],
            "operation": "getNetworkWirelessClientLatencyHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/latencyHistory"

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
                    f"getNetworkWirelessClientLatencyHistory: ignoring unrecognized kwargs: {invalid}"
                )

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
        - apTag (string): Filter results by AP Tag
        - vlan (integer): Filter results by VLAN
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "clients", "latencyStats"],
            "operation": "getNetworkWirelessClientLatencyStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessClientLatencyStats: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessClientRoamingHistory(self, networkId: str, clientId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get client roam events within the specified timespan.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-client-roaming-history

        - networkId (string): Network ID
        - clientId (string): Client ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "clients", "roaming", "history"],
            "operation": "getNetworkWirelessClientRoamingHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/networks/{networkId}/wireless/clients/{clientId}/roaming/history"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessClientRoamingHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

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
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "connectionStats"],
            "operation": "getNetworkWirelessConnectionStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessConnectionStats: ignoring unrecognized kwargs: {invalid}")

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

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "dataRateHistory"],
            "operation": "getNetworkWirelessDataRateHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/dataRateHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessDataRateHistory: ignoring unrecognized kwargs: {invalid}")

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
        - apTag (string): Filter results by AP Tag
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "devices", "connectionStats"],
            "operation": "getNetworkWirelessDevicesConnectionStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/devices/connectionStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessDevicesConnectionStats: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessDevicesHealthScores(self, networkId: str):
        """
        **Fetch the health scores of all APs on this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-devices-health-scores

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "monitor", "devices", "healthScores"],
            "operation": "getNetworkWirelessDevicesHealthScores",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/devices/healthScores"

        return self._session.get(metadata, resource)

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
        - apTag (string): Filter results by AP Tag
        - vlan (integer): Filter results by VLAN
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "devices", "latencyStats"],
            "operation": "getNetworkWirelessDevicesLatencyStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/devices/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessDevicesLatencyStats: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessElectronicShelfLabel(self, networkId: str):
        """
        **Return the ESL settings of a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "getNetworkWirelessElectronicShelfLabel",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel"

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

        if "mode" in kwargs:
            options = ["Bluetooth", "high frequency"]
            assert kwargs["mode"] in options, f'''"mode" cannot be "{kwargs["mode"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel"],
            "operation": "updateNetworkWirelessElectronicShelfLabel",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel"

        body_params = [
            "hostname",
            "enabled",
            "mode",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessElectronicShelfLabel: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessElectronicShelfLabelConfiguredDevices(self, networkId: str):
        """
        **Get a list of all ESL eligible devices of a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-electronic-shelf-label-configured-devices

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "electronicShelfLabel", "configuredDevices"],
            "operation": "getNetworkWirelessElectronicShelfLabelConfiguredDevices",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/electronicShelfLabel/configuredDevices"

        return self._session.get(metadata, resource)

    def getNetworkWirelessEthernetPortsProfiles(self, networkId: str):
        """
        **List the AP port profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profiles

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "getNetworkWirelessEthernetPortsProfiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles"

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
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "createNetworkWirelessEthernetPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles"

        body_params = [
            "name",
            "ports",
            "usbPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkWirelessEthernetPortsProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def assignNetworkWirelessEthernetPortsProfiles(self, networkId: str, serials: list, profileId: str, **kwargs):
        """
        **Assign AP port profile to list of APs**
        https://developer.cisco.com/meraki/api-v1/#!assign-network-wireless-ethernet-ports-profiles

        - networkId (string): Network ID
        - serials (array): List of AP serials
        - profileId (string): AP profile ID
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "assignNetworkWirelessEthernetPortsProfiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/assign"

        body_params = [
            "serials",
            "profileId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"assignNetworkWirelessEthernetPortsProfiles: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def setNetworkWirelessEthernetPortsProfilesDefault(self, networkId: str, profileId: str, **kwargs):
        """
        **Set the AP port profile to be default for this network**
        https://developer.cisco.com/meraki/api-v1/#!set-network-wireless-ethernet-ports-profiles-default

        - networkId (string): Network ID
        - profileId (string): AP profile ID
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "setNetworkWirelessEthernetPortsProfilesDefault",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/setDefault"

        body_params = [
            "profileId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"setNetworkWirelessEthernetPortsProfilesDefault: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getNetworkWirelessEthernetPortsProfile(self, networkId: str, profileId: str):
        """
        **Show the AP port profile by ID for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ethernet-ports-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        """

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "getNetworkWirelessEthernetPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

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
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "updateNetworkWirelessEthernetPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

        body_params = [
            "name",
            "ports",
            "usbPorts",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessEthernetPortsProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteNetworkWirelessEthernetPortsProfile(self, networkId: str, profileId: str):
        """
        **Delete an AP port profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-ethernet-ports-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        """

        metadata = {
            "tags": ["wireless", "configure", "ethernet", "ports", "profiles"],
            "operation": "deleteNetworkWirelessEthernetPortsProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/wireless/ethernet/ports/profiles/{profileId}"

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
        - apTag (string): Filter results by AP Tag
        - serial (string): Filter by AP
        - clientId (string): Filter by client MAC
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "failedConnections"],
            "operation": "getNetworkWirelessFailedConnections",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/failedConnections"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "serial",
            "clientId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessFailedConnections: ignoring unrecognized kwargs: {invalid}")

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

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "accessCategory" in kwargs:
            options = ["backgroundTraffic", "bestEffortTraffic", "videoTraffic", "voiceTraffic"]
            assert kwargs["accessCategory"] in options, (
                f'''"accessCategory" cannot be "{kwargs["accessCategory"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "latencyHistory"],
            "operation": "getNetworkWirelessLatencyHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/latencyHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
            "accessCategory",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessLatencyHistory: ignoring unrecognized kwargs: {invalid}")

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
        - apTag (string): Filter results by AP Tag
        - vlan (integer): Filter results by VLAN
        - fields (string): Partial selection: If present, this call will return only the selected fields of ["rawDistribution", "avg"]. All fields will be returned by default. Selected fields must be entered as a comma separated string.
        """

        kwargs.update(locals())

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''
        if "ssid" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssid"] in options, f'''"ssid" cannot be "{kwargs["ssid"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "latencyStats"],
            "operation": "getNetworkWirelessLatencyStats",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/latencyStats"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "band",
            "ssid",
            "apTag",
            "vlan",
            "fields",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessLatencyStats: ignoring unrecognized kwargs: {invalid}")

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
            "tags": ["wireless", "configure", "location", "scanning"],
            "operation": "updateNetworkWirelessLocationScanning",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/location/scanning"

        body_params = [
            "enabled",
            "api",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessLocationScanning: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def updateNetworkWirelessLocationWayfinding(self, networkId: str, **kwargs):
        """
        **Change client wayfinding settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-location-wayfinding

        - networkId (string): Network ID
        - enabled (boolean): Whether to enable client wayfinding on that network (only supported on Wireless networks).
        - maintenanceWindow (object): Maintenance window during which optimization might take place to improve location accuracy.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "location", "wayfinding"],
            "operation": "updateNetworkWirelessLocationWayfinding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/location/wayfinding"

        body_params = [
            "enabled",
            "maintenanceWindow",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessLocationWayfinding: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessMeshStatuses(self, networkId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "meshStatuses"],
            "operation": "getNetworkWirelessMeshStatuses",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/meshStatuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessMeshStatuses: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateNetworkWirelessOpportunisticPcap(self, networkId: str, **kwargs):
        """
        **Update the Opportunistic Pcap settings for a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-opportunistic-pcap

        - networkId (string): Network ID
        - enablement (object): Enablement settings
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "opportunisticPcap"],
            "operation": "updateNetworkWirelessOpportunisticPcap",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/opportunisticPcap"

        body_params = [
            "enablement",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessOpportunisticPcap: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def updateNetworkWirelessRadioAutoRf(self, networkId: str, **kwargs):
        """
        **Update the AutoRF settings for a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-radio-auto-rf

        - networkId (string): Network ID
        - busyHour (object): Busy Hour settings
        - channel (object): Channel settings
        - fra (object): FRA settings
        - aiRrm (object): AI-RRM settings
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "autoRf"],
            "operation": "updateNetworkWirelessRadioAutoRf",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/radio/autoRf"

        body_params = [
            "busyHour",
            "channel",
            "fra",
            "aiRrm",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessRadioAutoRf: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def updateNetworkWirelessRadioRrm(self, networkId: str, **kwargs):
        """
        **Update the AutoRF settings for a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-radio-rrm

        - networkId (string): Network ID
        - busyHour (object): Busy Hour settings
        - channel (object): Channel settings
        - fra (object): FRA settings
        - ai (object): AI settings
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "rrm"],
            "operation": "updateNetworkWirelessRadioRrm",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/radio/rrm"

        body_params = [
            "busyHour",
            "channel",
            "fra",
            "ai",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessRadioRrm: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessRfProfiles(self, networkId: str, **kwargs):
        """
        **List RF profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profiles

        - networkId (string): Network ID
        - includeTemplateProfiles (boolean): If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "getNetworkWirelessRfProfiles",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles"

        query_params = [
            "includeTemplateProfiles",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessRfProfiles: ignoring unrecognized kwargs: {invalid}")

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

        if "minBitrateType" in kwargs:
            options = ["band", "ssid"]
            assert kwargs["minBitrateType"] in options, (
                f'''"minBitrateType" cannot be "{kwargs["minBitrateType"]}", & must be set to one of: {options}'''
            )
        if "bandSelectionType" in kwargs:
            options = ["ap", "ssid"]
            assert kwargs["bandSelectionType"] in options, (
                f'''"bandSelectionType" cannot be "{kwargs["bandSelectionType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "createNetworkWirelessRfProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles"

        body_params = [
            "name",
            "clientBalancingEnabled",
            "minBitrateType",
            "bandSelectionType",
            "apBandSettings",
            "twoFourGhzSettings",
            "fiveGhzSettings",
            "sixGhzSettings",
            "transmission",
            "perSsidSettings",
            "flexRadios",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkWirelessRfProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        - name (string): The name of the new profile. Must be unique.
        - isIndoorDefault (boolean): Set this profile as the default indoor rf profile. If the profile ID is one of 'indoor' or 'outdoor', then a new profile will be created from the respective ID and set as the default
        - isOutdoorDefault (boolean): Set this profile as the default outdoor rf profile. If the profile ID is one of 'indoor' or 'outdoor', then a new profile will be created from the respective ID and set as the default
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

        if "minBitrateType" in kwargs:
            options = ["band", "ssid"]
            assert kwargs["minBitrateType"] in options, (
                f'''"minBitrateType" cannot be "{kwargs["minBitrateType"]}", & must be set to one of: {options}'''
            )
        if "bandSelectionType" in kwargs:
            options = ["ap", "ssid"]
            assert kwargs["bandSelectionType"] in options, (
                f'''"bandSelectionType" cannot be "{kwargs["bandSelectionType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "updateNetworkWirelessRfProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        body_params = [
            "name",
            "isIndoorDefault",
            "isOutdoorDefault",
            "clientBalancingEnabled",
            "minBitrateType",
            "bandSelectionType",
            "apBandSettings",
            "twoFourGhzSettings",
            "fiveGhzSettings",
            "sixGhzSettings",
            "transmission",
            "perSsidSettings",
            "flexRadios",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessRfProfile: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-wireless-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "deleteNetworkWirelessRfProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        return self._session.delete(metadata, resource)

    def getNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Return a RF profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            "tags": ["wireless", "configure", "rfProfiles"],
            "operation": "getNetworkWirelessRfProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe="")
        resource = f"/networks/{networkId}/wireless/rfProfiles/{rfProfileId}"

        return self._session.get(metadata, resource)

    def getNetworkWirelessSettings(self, networkId: str):
        """
        **Return the wireless settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-settings

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "settings"],
            "operation": "getNetworkWirelessSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/settings"

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
        - upgrade (object): Upgrade settings for the network
        - ledLightsOn (boolean): Toggle for enabling or disabling LED lights on all APs in the network (making them run dark)
        - multicastToUnicastConversion (object): Multicast-to-unicast conversion settings across the network
        - namedVlans (object): Named VLAN settings for wireless networks.
        """

        kwargs.update(locals())

        if "upgradeStrategy" in kwargs:
            options = ["minimizeClientDowntime", "minimizeUpgradeTime"]
            assert kwargs["upgradeStrategy"] in options, (
                f'''"upgradeStrategy" cannot be "{kwargs["upgradeStrategy"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "settings"],
            "operation": "updateNetworkWirelessSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/settings"

        body_params = [
            "meshingEnabled",
            "ipv6BridgeEnabled",
            "locationAnalyticsEnabled",
            "upgradeStrategy",
            "upgrade",
            "ledLightsOn",
            "multicastToUnicastConversion",
            "namedVlans",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSettings: ignoring unrecognized kwargs: {invalid}")

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

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "signalQualityHistory"],
            "operation": "getNetworkWirelessSignalQualityHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/signalQualityHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getNetworkWirelessSignalQualityHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getNetworkWirelessSsids(self, networkId: str):
        """
        **List the MR SSIDs in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssids

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "getNetworkWirelessSsids",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids"

        return self._session.get(metadata, resource)

    def getNetworkWirelessSsid(self, networkId: str, number: str):
        """
        **Return a single MR SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "getNetworkWirelessSsid",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}"

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
        - authMode (string): The association control method for the SSID ('open', 'open-enhanced', 'psk', 'open-with-radius', 'open-enhanced-with-radius', 'open-with-nac', '8021x-meraki', '8021x-nac', '8021x-radius', '8021x-google', '8021x-entra', '8021x-localradius', 'ipsk-with-radius', 'ipsk-without-radius', 'ipsk-with-nac' or 'ipsk-with-radius-easy-psk')
        - enterpriseAdminAccess (string): Whether or not an SSID is accessible by 'enterprise' administrators ('access disabled' or 'access enabled')
        - ssidAdminAccessible (boolean): SSID Administrator access status
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 only', 'WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only' or 'WPA3 192-bit Security')
        - dot11w (object): The current setting for Protected Management Frames (802.11w).
        - dot11r (object): The current setting for 802.11r
        - splashPage (string): The type of splash page for the SSID ('None', 'Click-through splash page', 'Billing', 'Password-protected with Meraki RADIUS', 'Password-protected with custom RADIUS', 'Password-protected with Active Directory', 'Password-protected with LDAP', 'SMS authentication', 'Systems Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth', 'Microsoft Entra ID', 'Sponsored guest', 'Cisco ISE' or 'Google Apps domain').This attribute is not supported for template children.
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
        - ipAssignmentMode (string): The client IP assignment mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Ethernet over GRE', 'Layer 3 roaming with a concentrator', 'VPN' or 'Campus Gateway')
        - campusGateway (object): Campus gateway settings
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
        - security (object): Security settings for the SSID
        - localAuthFallback (object): The current configuration for Local Authentication Fallback. Enables the Access Point (AP) to store client authentication data for a specified duration that can be adjusted as needed.
        - radiusAccountingStartDelay (integer): The delay (in seconds) before sending the first RADIUS accounting start message. Must be between 0 and 60 seconds.
        """

        kwargs.update(locals())

        if "authMode" in kwargs:
            options = [
                "8021x-entra",
                "8021x-google",
                "8021x-localradius",
                "8021x-meraki",
                "8021x-nac",
                "8021x-radius",
                "ipsk-with-nac",
                "ipsk-with-radius",
                "ipsk-with-radius-easy-psk",
                "ipsk-without-radius",
                "open",
                "open-enhanced",
                "open-enhanced-with-radius",
                "open-with-nac",
                "open-with-radius",
                "psk",
            ]
            assert kwargs["authMode"] in options, (
                f'''"authMode" cannot be "{kwargs["authMode"]}", & must be set to one of: {options}'''
            )
        if "enterpriseAdminAccess" in kwargs:
            options = ["access disabled", "access enabled"]
            assert kwargs["enterpriseAdminAccess"] in options, (
                f'''"enterpriseAdminAccess" cannot be "{kwargs["enterpriseAdminAccess"]}", & must be set to one of: {options}'''
            )
        if "encryptionMode" in kwargs:
            options = ["open", "wep", "wpa", "wpa-eap"]
            assert kwargs["encryptionMode"] in options, (
                f'''"encryptionMode" cannot be "{kwargs["encryptionMode"]}", & must be set to one of: {options}'''
            )
        if "wpaEncryptionMode" in kwargs:
            options = ["WPA1 and WPA2", "WPA1 only", "WPA2 only", "WPA3 192-bit Security", "WPA3 Transition Mode", "WPA3 only"]
            assert kwargs["wpaEncryptionMode"] in options, (
                f'''"wpaEncryptionMode" cannot be "{kwargs["wpaEncryptionMode"]}", & must be set to one of: {options}'''
            )
        if "splashPage" in kwargs:
            options = [
                "Billing",
                "Cisco ISE",
                "Click-through splash page",
                "Facebook Wi-Fi",
                "Google Apps domain",
                "Google OAuth",
                "Microsoft Entra ID",
                "None",
                "Password-protected with Active Directory",
                "Password-protected with LDAP",
                "Password-protected with Meraki RADIUS",
                "Password-protected with custom RADIUS",
                "SMS authentication",
                "Sponsored guest",
                "Systems Manager Sentry",
            ]
            assert kwargs["splashPage"] in options, (
                f'''"splashPage" cannot be "{kwargs["splashPage"]}", & must be set to one of: {options}'''
            )
        if "radiusFailoverPolicy" in kwargs:
            options = ["Allow access", "Deny access"]
            assert kwargs["radiusFailoverPolicy"] in options, (
                f'''"radiusFailoverPolicy" cannot be "{kwargs["radiusFailoverPolicy"]}", & must be set to one of: {options}'''
            )
        if "radiusLoadBalancingPolicy" in kwargs:
            options = ["Round robin", "Strict priority order"]
            assert kwargs["radiusLoadBalancingPolicy"] in options, (
                f'''"radiusLoadBalancingPolicy" cannot be "{kwargs["radiusLoadBalancingPolicy"]}", & must be set to one of: {options}'''
            )
        if "radiusAttributeForGroupPolicies" in kwargs:
            options = ["Airespace-ACL-Name", "Aruba-User-Role", "Filter-Id", "Reply-Message"]
            assert kwargs["radiusAttributeForGroupPolicies"] in options, (
                f'''"radiusAttributeForGroupPolicies" cannot be "{kwargs["radiusAttributeForGroupPolicies"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids"],
            "operation": "updateNetworkWirelessSsid",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}"

        body_params = [
            "name",
            "enabled",
            "localAuth",
            "authMode",
            "enterpriseAdminAccess",
            "ssidAdminAccessible",
            "encryptionMode",
            "psk",
            "wpaEncryptionMode",
            "dot11w",
            "dot11r",
            "splashPage",
            "splashGuestSponsorDomains",
            "oauth",
            "localRadius",
            "ldap",
            "activeDirectory",
            "radiusServers",
            "radiusProxyEnabled",
            "radiusTestingEnabled",
            "radiusCalledStationId",
            "radiusAuthenticationNasId",
            "radiusServerTimeout",
            "radiusServerAttemptsLimit",
            "radiusFallbackEnabled",
            "radiusRadsec",
            "radiusCoaEnabled",
            "radiusFailoverPolicy",
            "radiusLoadBalancingPolicy",
            "radiusAccountingEnabled",
            "radiusAccountingServers",
            "radiusAccountingInterimInterval",
            "radiusAttributeForGroupPolicies",
            "ipAssignmentMode",
            "campusGateway",
            "useVlanTagging",
            "concentratorNetworkId",
            "secondaryConcentratorNetworkId",
            "disassociateClientsOnVpnFailover",
            "vlanId",
            "defaultVlanId",
            "apTagsAndVlanIds",
            "walledGardenEnabled",
            "walledGardenRanges",
            "gre",
            "radiusOverride",
            "radiusGuestVlanEnabled",
            "radiusGuestVlanId",
            "minBitrate",
            "bandSelection",
            "perClientBandwidthLimitUp",
            "perClientBandwidthLimitDown",
            "perSsidBandwidthLimitUp",
            "perSsidBandwidthLimitDown",
            "lanIsolationEnabled",
            "visible",
            "availableOnAllAps",
            "availabilityTags",
            "adaptivePolicyGroupId",
            "mandatoryDhcpEnabled",
            "adultContentFilteringEnabled",
            "dnsRewrite",
            "speedBurst",
            "namedVlans",
            "security",
            "localAuthFallback",
            "radiusAccountingStartDelay",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsid: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidBonjourForwarding(self, networkId: str, number: str):
        """
        **List the Bonjour forwarding setting and rules for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-bonjour-forwarding

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "bonjourForwarding"],
            "operation": "getNetworkWirelessSsidBonjourForwarding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding"

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
            "tags": ["wireless", "configure", "ssids", "bonjourForwarding"],
            "operation": "updateNetworkWirelessSsidBonjourForwarding",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding"

        body_params = [
            "enabled",
            "rules",
            "exception",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidBonjourForwarding: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidDeviceTypeGroupPolicies(self, networkId: str, number: str):
        """
        **List the device type group policies for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-device-type-group-policies

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "deviceTypeGroupPolicies"],
            "operation": "getNetworkWirelessSsidDeviceTypeGroupPolicies",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies"

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
            "tags": ["wireless", "configure", "ssids", "deviceTypeGroupPolicies"],
            "operation": "updateNetworkWirelessSsidDeviceTypeGroupPolicies",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies"

        body_params = [
            "enabled",
            "deviceTypePolicies",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidDeviceTypeGroupPolicies: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidEapOverride(self, networkId: str, number: str):
        """
        **Return the EAP overridden parameters for an SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-eap-override

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "eapOverride"],
            "operation": "getNetworkWirelessSsidEapOverride",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/eapOverride"

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
            "tags": ["wireless", "configure", "ssids", "eapOverride"],
            "operation": "updateNetworkWirelessSsidEapOverride",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/eapOverride"

        body_params = [
            "timeout",
            "identity",
            "maxRetries",
            "eapolKey",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsidEapOverride: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str):
        """
        **Return the L3 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-3-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l3FirewallRules"],
            "operation": "getNetworkWirelessSsidFirewallL3FirewallRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"

        return self._session.get(metadata, resource)

    def updateNetworkWirelessSsidFirewallL3FirewallRules(self, networkId: str, number: str, **kwargs):
        """
        **Update the L3 firewall rules of an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-firewall-l-3-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        - rules (array): An ordered array of the firewall rules for this SSID.
        - allowLanAccess (boolean): Allow wireless client access to local LAN (boolean value - true allows access and false denies access) (optional)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l3FirewallRules"],
            "operation": "updateNetworkWirelessSsidFirewallL3FirewallRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules"

        body_params = [
            "rules",
            "allowLanAccess",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidFirewallL3FirewallRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidFirewallL7FirewallRules(self, networkId: str, number: str):
        """
        **Return the L7 firewall rules for an SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-firewall-l-7-firewall-rules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "l7FirewallRules"],
            "operation": "getNetworkWirelessSsidFirewallL7FirewallRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules"

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
            "tags": ["wireless", "configure", "ssids", "firewall", "l7FirewallRules"],
            "operation": "updateNetworkWirelessSsidFirewallL7FirewallRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules"

        body_params = [
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidFirewallL7FirewallRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidHotspot20(self, networkId: str, number: str):
        """
        **Return the Hotspot 2.0 settings for an SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-hotspot-2-0

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "hotspot20"],
            "operation": "getNetworkWirelessSsidHotspot20",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/hotspot20"

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

        if "networkAccessType" in kwargs:
            options = [
                "Chargeable public network",
                "Emergency services only network",
                "Free public network",
                "Personal device network",
                "Private network",
                "Private network with guest access",
                "Test or experimental",
                "Wildcard",
            ]
            assert kwargs["networkAccessType"] in options, (
                f'''"networkAccessType" cannot be "{kwargs["networkAccessType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "hotspot20"],
            "operation": "updateNetworkWirelessSsidHotspot20",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/hotspot20"

        body_params = [
            "enabled",
            "operator",
            "venue",
            "networkAccessType",
            "domains",
            "roamConsortOis",
            "mccMncs",
            "naiRealms",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsidHotspot20: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidIdentityPsks(self, networkId: str, number: str):
        """
        **List all Identity PSKs in a wireless network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-identity-psks

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "getNetworkWirelessSsidIdentityPsks",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks"

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
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "createNetworkWirelessSsidIdentityPsk",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks"

        body_params = [
            "name",
            "passphrase",
            "groupPolicyId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetworkWirelessSsidIdentityPsk: ignoring unrecognized kwargs: {invalid}")

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
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "getNetworkWirelessSsidIdentityPsk",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identityPskId = urllib.parse.quote(str(identityPskId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

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
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "updateNetworkWirelessSsidIdentityPsk",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identityPskId = urllib.parse.quote(str(identityPskId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        body_params = [
            "name",
            "passphrase",
            "groupPolicyId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsidIdentityPsk: ignoring unrecognized kwargs: {invalid}")

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
            "tags": ["wireless", "configure", "ssids", "identityPsks"],
            "operation": "deleteNetworkWirelessSsidIdentityPsk",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        identityPskId = urllib.parse.quote(str(identityPskId), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}"

        return self._session.delete(metadata, resource)

    def updateNetworkWirelessSsidOpenRoaming(self, networkId: str, number: str, **kwargs):
        """
        **Update the OpenRoaming setting for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-open-roaming

        - networkId (string): Network ID
        - number (string): Number
        - enabled (boolean): If true, OpenRoaming is enabled on this SSID.
        - tenantId (string): The OpenRoaming DNA Spaces tenant ID.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "openRoaming"],
            "operation": "updateNetworkWirelessSsidOpenRoaming",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/openRoaming"

        body_params = [
            "enabled",
            "tenantId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsidOpenRoaming: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def updateNetworkWirelessSsidPoliciesClientExclusion(self, networkId: str, number: str, static: dict, **kwargs):
        """
        **Update the client exclusion status configuration for a given SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-policies-client-exclusion

        - networkId (string): Network ID
        - number (string): Number
        - static (object): Static client exclusion status
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ssids", "policies", "clientExclusion"],
            "operation": "updateNetworkWirelessSsidPoliciesClientExclusion",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/policies/clientExclusion"

        body_params = [
            "static",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidPoliciesClientExclusion: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def updateNetworkWirelessSsidPoliciesClientExclusionStaticExclusions(
        self, networkId: str, number: str, macs: list, **kwargs
    ):
        """
        **Set the static client exclusion list for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-ssid-policies-client-exclusion-static-exclusions

        - networkId (string): Network ID
        - number (string): Number
        - macs (array): MAC addresses to set as static exclusion list
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ssids", "policies", "clientExclusion", "static", "exclusions"],
            "operation": "updateNetworkWirelessSsidPoliciesClientExclusionStaticExclusions",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/policies/clientExclusion/static/exclusions"

        body_params = [
            "macs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidPoliciesClientExclusionStaticExclusions: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def createNetworkWirelessSsidPoliciesClientExclusionStaticExclusionsBulkAdd(
        self, networkId: str, number: str, macs: list, **kwargs
    ):
        """
        **Add a list of MAC addresses to the static client exclusion list for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-policies-client-exclusion-static-exclusions-bulk-add

        - networkId (string): Network ID
        - number (string): Number
        - macs (array): MAC addresses to add to static exclusion
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ssids", "policies", "clientExclusion", "static", "exclusions", "bulkAdd"],
            "operation": "createNetworkWirelessSsidPoliciesClientExclusionStaticExclusionsBulkAdd",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/policies/clientExclusion/static/exclusions/bulkAdd"

        body_params = [
            "macs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkWirelessSsidPoliciesClientExclusionStaticExclusionsBulkAdd: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def createNetworkWirelessSsidPoliciesClientExclusionStaticExclusionsBulkRemove(
        self, networkId: str, number: str, macs: list, **kwargs
    ):
        """
        **Delete a list of MAC addresses from the static client exclusion list for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!create-network-wireless-ssid-policies-client-exclusion-static-exclusions-bulk-remove

        - networkId (string): Network ID
        - number (string): Number
        - macs (array): MAC addresses to remove from static exclusion
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "ssids", "policies", "clientExclusion", "static", "exclusions", "bulkRemove"],
            "operation": "createNetworkWirelessSsidPoliciesClientExclusionStaticExclusionsBulkRemove",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/policies/clientExclusion/static/exclusions/bulkRemove"

        body_params = [
            "macs",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createNetworkWirelessSsidPoliciesClientExclusionStaticExclusionsBulkRemove: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getNetworkWirelessSsidSchedules(self, networkId: str, number: str):
        """
        **List the outage schedule for the SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-schedules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "schedules"],
            "operation": "getNetworkWirelessSsidSchedules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/schedules"

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
            "tags": ["wireless", "configure", "ssids", "schedules"],
            "operation": "updateNetworkWirelessSsidSchedules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/schedules"

        body_params = [
            "enabled",
            "ranges",
            "rangesInSeconds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsidSchedules: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidSplashSettings(self, networkId: str, number: str):
        """
        **Display the splash page settings for the given SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-splash-settings

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "splash", "settings"],
            "operation": "getNetworkWirelessSsidSplashSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/splash/settings"

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
        - language (string): Language of splash page.
        - userConsent (object): User consent settings
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

        if "splashTimeout" in kwargs:
            options = [30, 60, 120, 240, 480, 720, 1080, 1440, 2880, 5760, 7200, 10080, 20160, 43200, 86400, 129600]
            assert kwargs["splashTimeout"] in options, (
                f'''"splashTimeout" cannot be "{kwargs["splashTimeout"]}", & must be set to one of: {options}'''
            )
        if "language" in kwargs:
            options = [
                "DA",
                "DE",
                "EL",
                "EN",
                "ES",
                "FI",
                "FR",
                "GL",
                "IT",
                "JA",
                "KO",
                "NL",
                "NO",
                "PL",
                "PT",
                "RU",
                "SK",
                "SV",
                "UK",
                "ZH",
            ]
            assert kwargs["language"] in options, (
                f'''"language" cannot be "{kwargs["language"]}", & must be set to one of: {options}'''
            )
        if "controllerDisconnectionBehavior" in kwargs:
            options = ["default", "open", "restricted"]
            assert kwargs["controllerDisconnectionBehavior"] in options, (
                f'''"controllerDisconnectionBehavior" cannot be "{kwargs["controllerDisconnectionBehavior"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "splash", "settings"],
            "operation": "updateNetworkWirelessSsidSplashSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/splash/settings"

        body_params = [
            "splashUrl",
            "useSplashUrl",
            "splashTimeout",
            "redirectUrl",
            "useRedirectUrl",
            "welcomeMessage",
            "language",
            "userConsent",
            "themeId",
            "splashLogo",
            "splashImage",
            "splashPrepaidFront",
            "blockAllTrafficBeforeSignOn",
            "controllerDisconnectionBehavior",
            "allowSimultaneousLogins",
            "guestSponsorship",
            "billing",
            "sentryEnrollment",
            "selfRegistration",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidSplashSettings: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["wireless", "configure", "ssids", "trafficShaping", "rules"],
            "operation": "updateNetworkWirelessSsidTrafficShapingRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules"

        body_params = [
            "trafficShapingEnabled",
            "defaultRulesEnabled",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateNetworkWirelessSsidTrafficShapingRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessSsidTrafficShapingRules(self, networkId: str, number: str):
        """
        **Display the traffic shaping settings for a SSID on an MR network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-traffic-shaping-rules

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "trafficShaping", "rules"],
            "operation": "getNetworkWirelessSsidTrafficShapingRules",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules"

        return self._session.get(metadata, resource)

    def getNetworkWirelessSsidVpn(self, networkId: str, number: str):
        """
        **List the VPN settings for the SSID.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-wireless-ssid-vpn

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "vpn"],
            "operation": "getNetworkWirelessSsidVpn",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/vpn"

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
            "tags": ["wireless", "configure", "ssids", "vpn"],
            "operation": "updateNetworkWirelessSsidVpn",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        number = urllib.parse.quote(str(number), safe="")
        resource = f"/networks/{networkId}/wireless/ssids/{number}/vpn"

        body_params = [
            "concentrator",
            "splitTunnel",
            "failover",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessSsidVpn: ignoring unrecognized kwargs: {invalid}")

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

        if "band" in kwargs:
            options = ["2.4", "5", "6"]
            assert kwargs["band"] in options, f'''"band" cannot be "{kwargs["band"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "monitor", "usageHistory"],
            "operation": "getNetworkWirelessUsageHistory",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/usageHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "autoResolution",
            "clientId",
            "deviceSerial",
            "apTag",
            "band",
            "ssid",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkWirelessUsageHistory: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def updateNetworkWirelessZigbee(self, networkId: str, **kwargs):
        """
        **Update Zigbee Configs for specified network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-wireless-zigbee

        - networkId (string): Network ID
        - enabled (boolean): To enable/disable Zigbee on the network
        - iotController (object): Zigbee's IoT controller details
        - lockManagement (object): Login Credentials of on-premises lock management
        - defaults (object): Default Settings for Zigbee Devices
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee"],
            "operation": "updateNetworkWirelessZigbee",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/wireless/zigbee"

        body_params = [
            "enabled",
            "iotController",
            "lockManagement",
            "defaults",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkWirelessZigbee: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getOrganizationAssuranceConnectivityWirelessRfHealthByBand(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Show the by-device RF Health score overview information for the organization in the given interval**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-connectivity-wireless-rf-health-by-band

        - organizationId (string): Organization ID
        - networkIds (array): Networks for which information should be gathered.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 day. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 3600, 14400, 86400. The default is 3600. Interval is calculated if time params are provided.
        - minimumRfHealthScore (integer): Minimum RF Health score for an AP to be retrieved.
        - maximumRfHealthScore (integer): Maximum RF Health score for an AP to be retrieved.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "connectivity", "rfHealth", "byBand"],
            "operation": "getOrganizationAssuranceConnectivityWirelessRfHealthByBand",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/connectivity/wireless/rfHealth/byBand"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "interval",
            "networkIds",
            "minimumRfHealthScore",
            "maximumRfHealthScore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationAssuranceConnectivityWirelessRfHealthByBand: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceImpactedDeviceWirelessByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns count of impacted wireless devices per network on a given organization and time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-impacted-device-wireless-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkGroupIds (array): Filter results by a list of network group IDs.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 2 hours and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "impactedDevice", "byNetwork"],
            "operation": "getOrganizationAssuranceImpactedDeviceWirelessByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/impactedDevice/wireless/byNetwork"

        query_params = [
            "networkGroupIds",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkGroupIds",
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
                    f"getOrganizationAssuranceImpactedDeviceWirelessByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByBand(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by band.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-band

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork", "byBand"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByBand",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/byBand"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByBand: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClient(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork", "byClient"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/byClient"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClientOs(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by client OS and driver version.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-client-os

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork", "byClientOs"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClientOs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/byClientOs"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClientOs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClientType(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-client-type

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork", "byClientType"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClientType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/byClientType"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByClientType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork", "byDevice"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Time-series of wireless post connection capacity successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "experience", "channelAvailability", "byNetwork", "byInterval"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "interval",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless post connection capacity successes and failures by ssid.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-by-network-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "byNetwork", "bySsid"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/byNetwork/bySsid"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityByNetworkBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceChannelAvailabilityInsightsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Provides insights into wireless capacity experience by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-channel-availability-insights-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - contributor (string): Contributor for which to retrieve insights. If not specified, returns overall insights.
        - subContributor (string): Sub-contributor for which to retrieve insights. If not specified, returns all sub contributor insights.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "contributor" in kwargs:
            options = ["Co-channel interference", "High traffic", "Non-wifi interference"]
            assert kwargs["contributor"] in options, (
                f'''"contributor" cannot be "{kwargs["contributor"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "experience", "channelAvailability", "insights", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceChannelAvailabilityInsightsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/channelAvailability/insights/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "contributor",
            "subContributor",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceChannelAvailabilityInsightsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceClientsInsights(self, organizationId: str, **kwargs):
        """
        **Returns the top wireless service-level insights for the specified time window, including each network and the impacted client count per metric.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-clients-insights

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days.
        - limit (integer): Number of top networks to return. Default is 5. Maximum is 10.
        """

        kwargs.update(locals())

        if "limit" in kwargs:
            options = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            assert kwargs["limit"] in options, f'''"limit" cannot be "{kwargs["limit"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["wireless", "configure", "experience", "clients", "insights"],
            "operation": "getOrganizationAssuranceWirelessExperienceClientsInsights",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/clients/insights"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "limit",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationAssuranceWirelessExperienceClientsInsights: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWirelessExperienceClientsOverviewHistoryByInterval(self, organizationId: str, **kwargs):
        """
        **Returns time series data for impacted and active clients for organization wireless experience metrics.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-clients-overview-history-by-interval

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 300, 600, 900, 1800, 3600, 86400. The default is 300.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "experience", "clients", "overview", "history", "byInterval"],
            "operation": "getOrganizationAssuranceWirelessExperienceClientsOverviewHistoryByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/clients/overview/history/byInterval"

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
                    f"getOrganizationAssuranceWirelessExperienceClientsOverviewHistoryByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkByBand(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by band.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-band

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork", "byBand"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkByBand",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/byBand"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkByBand: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClient(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by client.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork", "byClient"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/byClient"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClientOs(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by client OS.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-client-os

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork", "byClientOs"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClientOs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/byClientOs"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClientOs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClientType(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by client type.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-client-type

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork", "byClientType"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClientType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/byClientType"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkByClientType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork", "byDevice"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Time-series of wireless coverage successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 60, 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "experience", "coverage", "byNetwork", "byInterval"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "interval",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageByNetworkBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless coverage successes and failures by SSID.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-by-network-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "byNetwork", "bySsid"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageByNetworkBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/byNetwork/bySsid"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageByNetworkBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceCoverageInsightsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Provides insights into wireless coverage experience by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-coverage-insights-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - contributor (string): Contributor for which to retrieve insights. If not specified, returns overall insights.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "contributor" in kwargs:
            options = ["Admin power restriction", "Insufficient AP density", "Sticky client", "Transient weak signal"]
            assert kwargs["contributor"] in options, (
                f'''"contributor" cannot be "{kwargs["contributor"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "experience", "coverage", "insights", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceCoverageInsightsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/coverage/insights/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "contributor",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceCoverageInsightsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceMetricsOverviewHistoryByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns organization wireless experience metrics overview grouped by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-metrics-overview-history-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "metrics", "overview", "history", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceMetricsOverviewHistoryByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/metrics/overview/history/byNetwork"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationAssuranceWirelessExperienceMetricsOverviewHistoryByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByBand(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by band.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-band

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "byBand"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByBand",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byBand"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByBand: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClient(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by client.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 10000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "byClient"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byClient"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClientOs(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by client OS.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-client-os

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "byClientOs"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClientOs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byClientOs"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClientOs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClientType(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by client type.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-client-type

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "byClientType"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClientType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byClientType"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByClientType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "byDevice"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Time-series of wireless connection successes and failures by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 60, 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "experience", "successfulConnects", "byNetwork", "byInterval"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "interval",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByServer(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by server.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-server

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "byServer"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/byServer"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkByServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by ssid.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-by-network-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "byNetwork", "bySsid"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/byNetwork/bySsid"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsByNetworkBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceSuccessfulConnectsInsightsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Provides insights into wireless successful connects experience by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-successful-connects-insights-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - contributor (string): Contributor for which to retrieve insights. If not specified, returns overall insights.
        - subContributor (string): Sub-contributor for which to retrieve insights. If not specified, returns all sub contributor insights.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "contributor" in kwargs:
            options = ["assoc", "auth", "dhcp", "dns"]
            assert kwargs["contributor"] in options, (
                f'''"contributor" cannot be "{kwargs["contributor"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "experience", "successfulConnects", "insights", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceSuccessfulConnectsInsightsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/successfulConnects/insights/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "contributor",
            "subContributor",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceSuccessfulConnectsInsightsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless time to connect metrics by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByBand(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by band.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-band

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "byBand"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByBand",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byBand"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByBand: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClient(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless time to connect metrics by client.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 10000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "byClient"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byClient"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClientOs(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by client OS.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-client-os

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "byClientOs"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClientOs",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byClientOs"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClientOs: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClientType(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection successes and failures by client type.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-client-type

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "byClientType"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClientType",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byClientType"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByClientType: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection time to connect metrics by device.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "byDevice"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Time-series of wireless time to connect by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-interval

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 2 hours. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 60, 300, 600, 3600, 14400, 86400. The default is 300. Interval is calculated if time params are provided.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "experience", "timeToConnect", "byNetwork", "byInterval"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "interval",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByServer(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection time to connect metrics by server.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-server

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "byServer"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByServer",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/byServer"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkByServer: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarizes wireless connection time to connect metrics by ssid.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-by-network-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "byNetwork", "bySsid"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/byNetwork/bySsid"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectByNetworkBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationAssuranceWirelessExperienceTimeToConnectInsightsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Provides insights into wireless time to connect experience by network.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-assurance-wireless-experience-time-to-connect-insights-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial.
        - ssidNumbers (array): Filter results by SSID number.
        - bands (array): Filter results by band.
        - contributor (string): Contributor for which to retrieve insights. If not specified, returns overall insights.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 15 minutes and be less than or equal to 14 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 10000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "contributor" in kwargs:
            options = ["assoc", "auth", "dhcp", "dns"]
            assert kwargs["contributor"] in options, (
                f'''"contributor" cannot be "{kwargs["contributor"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "experience", "timeToConnect", "insights", "byNetwork"],
            "operation": "getOrganizationAssuranceWirelessExperienceTimeToConnectInsightsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/assurance/wireless/experience/timeToConnect/insights/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
            "contributor",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssidNumbers",
            "bands",
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
                    f"getOrganizationAssuranceWirelessExperienceTimeToConnectInsightsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessAirMarshalRules(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "configure", "airMarshal", "rules"],
            "operation": "getOrganizationWirelessAirMarshalRules",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/airMarshal/rules"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessAirMarshalRules: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessAirMarshalSettingsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "configure", "airMarshal", "settings", "byNetwork"],
            "operation": "getOrganizationWirelessAirMarshalSettingsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/airMarshal/settings/byNetwork"

        query_params = [
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessAirMarshalSettingsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessAlertsLowPowerByDevice(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Gets all low power related alerts over a given network and returns information by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-alerts-low-power-by-device

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "alerts", "lowPower", "byDevice"],
            "operation": "getOrganizationWirelessAlertsLowPowerByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/alerts/lowPower/byDevice"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessAlertsLowPowerByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessCertificatesOpenRoamingCertificateAuthority(self, organizationId: str):
        """
        **Query for details on the organization's OpenRoaming Certificate Authority certificate (CAs).**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-certificates-open-roaming-certificate-authority

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["wireless", "configure", "certificates", "openRoaming", "certificateAuthority"],
            "operation": "getOrganizationWirelessCertificatesOpenRoamingCertificateAuthority",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/certificates/openRoaming/certificateAuthority"

        return self._session.get(metadata, resource)

    def getOrganizationWirelessClientsConnectionsAssociationByClient(self, organizationId: str, **kwargs):
        """
        **Summarize association outcomes per wireless client across an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-connections-association-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connections", "association", "byClient"],
            "operation": "getOrganizationWirelessClientsConnectionsAssociationByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/connections/association/byClient"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessClientsConnectionsAssociationByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessClientsConnectionsAuthenticationByClient(self, organizationId: str, **kwargs):
        """
        **Summarize authentication outcomes per wireless client across an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-connections-authentication-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connections", "authentication", "byClient"],
            "operation": "getOrganizationWirelessClientsConnectionsAuthenticationByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/connections/authentication/byClient"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessClientsConnectionsAuthenticationByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessClientsConnectionsDhcpByClient(self, organizationId: str, **kwargs):
        """
        **Get IP assignment for all clients in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-connections-dhcp-by-client

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 7 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connections", "dhcp", "byClient"],
            "operation": "getOrganizationWirelessClientsConnectionsDhcpByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/connections/dhcp/byClient"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessClientsConnectionsDhcpByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessClientsConnectionsFailuresHistoryByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns failed wireless client connections for this organization by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-connections-failures-history-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - connectionTimeSortOrder (string): (optional) Sort order of events by connection start time. (default desc)
        - failureSteps (array): (optional) The step in the connection process that failed
        - clientMac (string): (optional) The MAC address of the client with which the list of events will be filtered.
        - serials (array): (optional) Filter devices by serial number
        - timespan (integer): (optional) The timespan, in seconds, for the failed connections. The period will be from [timespan] seconds ago until now. The maximum allowed timespan is 1 month. Default: 86400 (24 hours)
        - ssidNumber (integer): (optional) The SSID number to include
        - networkIds (array): (optional) The set of network IDs to include.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "connectionTimeSortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["connectionTimeSortOrder"] in options, (
                f'''"connectionTimeSortOrder" cannot be "{kwargs["connectionTimeSortOrder"]}", & must be set to one of: {options}'''
            )
        if "ssidNumber" in kwargs:
            options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            assert kwargs["ssidNumber"] in options, (
                f'''"ssidNumber" cannot be "{kwargs["ssidNumber"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "clients", "connections", "failures", "history", "byDevice"],
            "operation": "getOrganizationWirelessClientsConnectionsFailuresHistoryByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/connections/failures/history/byDevice"

        query_params = [
            "connectionTimeSortOrder",
            "failureSteps",
            "clientMac",
            "serials",
            "timespan",
            "ssidNumber",
            "networkIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "failureSteps",
            "serials",
            "networkIds",
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
                    f"getOrganizationWirelessClientsConnectionsFailuresHistoryByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessClientsConnectionsImpactedByNetworkBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Summarize the number of wireless clients impacted by connection failures on network SSIDs, across an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-connections-impacted-by-network-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - networkGroupIds (array): Filter results by a list of network group IDs.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 7 days. The default is 2 hours.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "clients", "connections", "impacted", "byNetwork", "bySsid"],
            "operation": "getOrganizationWirelessClientsConnectionsImpactedByNetworkBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/connections/impacted/byNetwork/bySsid"

        query_params = [
            "networkIds",
            "networkGroupIds",
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "networkGroupIds",
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
                    f"getOrganizationWirelessClientsConnectionsImpactedByNetworkBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessClientsOverviewByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "clients", "overview", "byDevice"],
            "operation": "getOrganizationWirelessClientsOverviewByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/overview/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "campusGatewayClusterIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "campusGatewayClusterIds",
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
                    f"getOrganizationWirelessClientsOverviewByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def byOrganizationWirelessClientsRfHealthOverviewNetwork(self, organizationId: str, **kwargs):
        """
        **Show the by-network client information for the organization in the given interval**
        https://developer.cisco.com/meraki/api-v1/#!by-organization-wireless-clients-rf-health-overview-network

        - organizationId (string): Organization ID
        - networkIds (array): Networks for which information should be gathered.
        - bands (array): Bands for which information should be gathered. Valid bands are 2.4, 5, and 6.
        - channels (array): Channel for which information should be gathered.
        - serials (array): Serial number of the devices for which information should be gathered.
        - gFloorplanId (string): Geoaligned floorplan ID nodes for which information is gathered belong to.
        - tags (array): Access Point tags for which information should be gathered.
        - models (array): Access Point models for which information should be gathered.
        - rfProfiles (array): Rf Profiles for which information should be gathered.
        - minimumRfHealthScore (integer): Minimum RF Health score for an AP to be retrieved.
        - maximumRfHealthScore (integer): Maximum RF Health score for an AP to be retrieved.
        - retryOnEmpty (boolean): If true, the query will be retried with a longer timeframe if the results are empty.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "clients", "rfHealth", "overview"],
            "operation": "byOrganizationWirelessClientsRfHealthOverviewNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/rfHealth/overview/byNetwork"

        query_params = [
            "networkIds",
            "bands",
            "channels",
            "serials",
            "gFloorplanId",
            "tags",
            "models",
            "rfProfiles",
            "minimumRfHealthScore",
            "maximumRfHealthScore",
            "retryOnEmpty",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "bands",
            "channels",
            "serials",
            "tags",
            "models",
            "rfProfiles",
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
                    f"byOrganizationWirelessClientsRfHealthOverviewNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessClientsStickyEvents(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get sticky client events within the specified timespan.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-sticky-events

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - clientIds (array): Filter results by client id.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "clients", "stickyEvents"],
            "operation": "getOrganizationWirelessClientsStickyEvents",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/stickyEvents"

        query_params = [
            "networkIds",
            "clientIds",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "clientIds",
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
                    f"getOrganizationWirelessClientsStickyEvents: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessClientsUsageByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns client usage details for wireless networks within an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-usage-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 1 hour and be less than or equal to 7 days. The default is 2 hours.
        - networkIds (array): Filter results by a list of network IDs.
        - networkGroupIds (array): Filter results by a list of network group IDs.
        - gatewayNetworkIds (array): Limit the results to clients tunneled to campus gateways in the provided networks.
        - usageUnits (string): Usage units to use in the response.
        """

        kwargs.update(locals())

        if "usageUnits" in kwargs:
            options = ["GB", "KB", "MB", "TB"]
            assert kwargs["usageUnits"] in options, (
                f'''"usageUnits" cannot be "{kwargs["usageUnits"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "usage", "byNetwork"],
            "operation": "getOrganizationWirelessClientsUsageByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/usage/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "networkGroupIds",
            "gatewayNetworkIds",
            "usageUnits",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "networkGroupIds",
            "gatewayNetworkIds",
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
                    f"getOrganizationWirelessClientsUsageByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessClientsUsageByNetworkBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns client usage details for wireless network SSIDs within an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-usage-by-network-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 1 hour and be less than or equal to 7 days. The default is 2 hours.
        - networkIds (array): Filter results by a list of network IDs.
        - networkGroupIds (array): Filter results by a list of network group IDs.
        - ssidIds (array): Filter results by a list of SSID IDs.
        - ssidNames (array): Filter results by a list of SSID names.
        - gatewayNetworkIds (array): Limit the results to clients tunneled to campus gateways in the provided networks.
        - usageUnits (string): Usage units to use in the response.
        """

        kwargs.update(locals())

        if "usageUnits" in kwargs:
            options = ["GB", "KB", "MB", "TB"]
            assert kwargs["usageUnits"] in options, (
                f'''"usageUnits" cannot be "{kwargs["usageUnits"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "usage", "byNetwork", "bySsid"],
            "operation": "getOrganizationWirelessClientsUsageByNetworkBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/usage/byNetwork/bySsid"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "networkGroupIds",
            "ssidIds",
            "ssidNames",
            "gatewayNetworkIds",
            "usageUnits",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "networkGroupIds",
            "ssidIds",
            "ssidNames",
            "gatewayNetworkIds",
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
                    f"getOrganizationWirelessClientsUsageByNetworkBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessClientsUsageBySsid(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns client usage details for SSIDs within an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-clients-usage-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 8 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 1 hour and be less than or equal to 7 days. The default is 2 hours.
        - ssidNames (array): Filter results by a list of SSID names.
        - networkIds (array): Limit the results to clients that belong to one of the provided networks.
        - networkGroupIds (array): Limit the results to clients that belong to one of the provided network groups.
        - gatewayNetworkIds (array): Limit the results to clients tunneled to campus gateways in the provided networks.
        - usageUnits (string): Usage units to use in the response.
        """

        kwargs.update(locals())

        if "usageUnits" in kwargs:
            options = ["GB", "KB", "MB", "TB"]
            assert kwargs["usageUnits"] in options, (
                f'''"usageUnits" cannot be "{kwargs["usageUnits"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "monitor", "clients", "usage", "bySsid"],
            "operation": "getOrganizationWirelessClientsUsageBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/clients/usage/bySsid"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "ssidNames",
            "networkIds",
            "networkGroupIds",
            "gatewayNetworkIds",
            "usageUnits",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "ssidNames",
            "networkIds",
            "networkGroupIds",
            "gatewayNetworkIds",
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
                    f"getOrganizationWirelessClientsUsageBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesAccelerometerStatuses(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the most recent AP accelerometer status information for wireless devices that support it.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-accelerometer-statuses

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
            "tags": ["wireless", "monitor", "devices", "accelerometer", "statuses"],
            "operation": "getOrganizationWirelessDevicesAccelerometerStatuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/accelerometer/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesAccelerometerStatuses: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesChannelUtilizationByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "byDevice"],
            "operation": "getOrganizationWirelessDevicesChannelUtilizationByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesChannelUtilizationByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesChannelUtilizationByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "byNetwork"],
            "operation": "getOrganizationWirelessDevicesChannelUtilizationByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesChannelUtilizationByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "history", "byDevice", "byInterval"],
            "operation": "getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/history/byDevice/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesChannelUtilizationHistoryByDeviceByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "channelUtilization", "history", "byNetwork", "byInterval"],
            "operation": "getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/channelUtilization/history/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "serials",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesChannelUtilizationHistoryByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesDataRateByClient(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get average uplink and downlink datarates for all clients in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-data-rate-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial number.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - macs (array): Filter results by client mac address(es).
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "dataRate", "byClient"],
            "operation": "getOrganizationWirelessDevicesDataRateByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/dataRate/byClient"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "macs",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "macs",
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
                    f"getOrganizationWirelessDevicesDataRateByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesEthernetStatuses(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "devices", "ethernet", "statuses"],
            "operation": "getOrganizationWirelessDevicesEthernetStatuses",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/ethernet/statuses"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesEthernetStatuses: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesLatencyByClient(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get latency summaries for all wireless devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-latency-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days.
        - networkIds (array): Filter results by network.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - ssids (array): Filter results by SSID number.
        - macs (array): Filter results by client mac address(es).
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "latency", "byClient"],
            "operation": "getOrganizationWirelessDevicesLatencyByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/latency/byClient"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "bands",
            "ssids",
            "macs",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "bands",
            "ssids",
            "macs",
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
                    f"getOrganizationWirelessDevicesLatencyByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesLatencyByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get latency summaries for all wireless devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-latency-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days.
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - ssids (array): Filter results by SSID number.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "latency", "byDevice"],
            "operation": "getOrganizationWirelessDevicesLatencyByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/latency/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "serials",
            "bands",
            "ssids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "bands",
            "ssids",
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
                    f"getOrganizationWirelessDevicesLatencyByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesLatencyByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Get per-network latency summaries for all wireless networks in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-latency-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 90 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 90 days. The default is 7 days.
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - ssids (array): Filter results by SSID number.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "latency", "byNetwork"],
            "operation": "getOrganizationWirelessDevicesLatencyByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/latency/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "serials",
            "bands",
            "ssids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "bands",
            "ssids",
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
                    f"getOrganizationWirelessDevicesLatencyByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationWirelessDevicesLiveToolsClientDisconnect(self, organizationId: str, clientId: str, **kwargs):
        """
        **Enqueue a job to disconnect a client from an AP**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-live-tools-client-disconnect

        - organizationId (string): Organization ID
        - clientId (string): Client ID
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "liveTools", "devices", "clients", "disconnect"],
            "operation": "createOrganizationWirelessDevicesLiveToolsClientDisconnect",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        clientId = urllib.parse.quote(str(clientId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/liveTools/clients/{clientId}/disconnect"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessDevicesLiveToolsClientDisconnect: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationWirelessDevicesPacketLossByClient(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byClient"],
            "operation": "getOrganizationWirelessDevicesPacketLossByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/packetLoss/byClient"

        query_params = [
            "networkIds",
            "ssids",
            "bands",
            "macs",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssids",
            "bands",
            "macs",
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
                    f"getOrganizationWirelessDevicesPacketLossByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesPacketLossByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byDevice"],
            "operation": "getOrganizationWirelessDevicesPacketLossByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/packetLoss/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
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
                    f"getOrganizationWirelessDevicesPacketLossByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesPacketLossByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "packetLoss", "byNetwork"],
            "operation": "getOrganizationWirelessDevicesPacketLossByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/packetLoss/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
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
                    f"getOrganizationWirelessDevicesPacketLossByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesPowerModeHistory(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "devices", "power", "mode", "history"],
            "operation": "getOrganizationWirelessDevicesPowerModeHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/power/mode/history"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesPowerModeHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesProvisioningDeployments(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the zero touch deployments for wireless access points in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-provisioning-deployments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 20.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - search (string): Filter by MAC address, serial number, new device name, old device name, or model.
        - sortBy (string): Field used to sort results. Default is 'status'.
        - sortOrder (string): Sort order. Default is 'asc'.
        - deploymentType (string): Filter deployments by type.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["afterAction", "createdAt", "deploymentId", "name", "status"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )
        if "deploymentType" in kwargs:
            options = ["deploy", "replace"]
            assert kwargs["deploymentType"] in options, (
                f'''"deploymentType" cannot be "{kwargs["deploymentType"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "devices", "provisioning", "deployments"],
            "operation": "getOrganizationWirelessDevicesProvisioningDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/provisioning/deployments"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "search",
            "sortBy",
            "sortOrder",
            "deploymentType",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"getOrganizationWirelessDevicesProvisioningDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationWirelessDevicesProvisioningDeployment(self, organizationId: str, items: list, **kwargs):
        """
        **Create a zero touch deployment for a wireless access point**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-provisioning-deployment

        - organizationId (string): Organization ID
        - items (array): List of zero touch deployments to create
        - meta (object): Metadata relevant to the paginated dataset
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "provisioning", "deployments"],
            "operation": "createOrganizationWirelessDevicesProvisioningDeployment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/provisioning/deployments"

        body_params = [
            "items",
            "meta",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessDevicesProvisioningDeployment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def updateOrganizationWirelessDevicesProvisioningDeployments(self, organizationId: str, items: list, **kwargs):
        """
        **Update a zero touch deployment**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-devices-provisioning-deployments

        - organizationId (string): Organization ID
        - items (array): List of zero touch deployments to create
        - meta (object): Metadata relevant to the paginated dataset
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "provisioning", "deployments"],
            "operation": "updateOrganizationWirelessDevicesProvisioningDeployments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/provisioning/deployments"

        body_params = [
            "items",
            "meta",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessDevicesProvisioningDeployments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationWirelessDevicesProvisioningDeploymentsByNewDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns deployment IDs for the given new node serial numbers**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-provisioning-deployments-by-new-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 80.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - serials (array): Array of new device serial numbers to query
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "provisioning", "deployments", "byNewDevice"],
            "operation": "getOrganizationWirelessDevicesProvisioningDeploymentsByNewDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/provisioning/deployments/byNewDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "serials",
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
                    f"getOrganizationWirelessDevicesProvisioningDeploymentsByNewDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def deleteOrganizationWirelessDevicesProvisioningDeployment(self, organizationId: str, deploymentId: str):
        """
        **Delete a zero touch deployment**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-devices-provisioning-deployment

        - organizationId (string): Organization ID
        - deploymentId (string): Deployment ID
        """

        metadata = {
            "tags": ["wireless", "configure", "devices", "provisioning", "deployments"],
            "operation": "deleteOrganizationWirelessDevicesProvisioningDeployment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        deploymentId = urllib.parse.quote(str(deploymentId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/provisioning/deployments/{deploymentId}"

        return self._session.delete(metadata, resource)

    def getOrganizationWirelessDevicesProvisioningRecommendationsTags(self, organizationId: str, **kwargs):
        """
        **List the recommended device tags for zero touch deployments available for the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-provisioning-recommendations-tags

        - organizationId (string): Organization ID
        - networkIds (array): The list of networks to use as hints for device tags recommendations.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "provisioning", "recommendations", "tags"],
            "operation": "getOrganizationWirelessDevicesProvisioningRecommendationsTags",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/provisioning/recommendations/tags"

        query_params = [
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesProvisioningRecommendationsTags: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessDevicesRadsecCertificatesAuthorities(self, organizationId: str, **kwargs):
        """
        **Query for details on the organization's RADSEC device Certificate Authority certificates (CAs)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-radsec-certificates-authorities

        - organizationId (string): Organization ID
        - certificateAuthorityIds (array): Optional parameter to filter CAs by one or more CA IDs. All returned CAs will have an ID that is an exact match.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "getOrganizationWirelessDevicesRadsecCertificatesAuthorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities"

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
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
                    f"getOrganizationWirelessDevicesRadsecCertificatesAuthorities: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "updateOrganizationWirelessDevicesRadsecCertificatesAuthorities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities"

        body_params = [
            "status",
            "certificateAuthorityId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessDevicesRadsecCertificatesAuthorities: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def createOrganizationWirelessDevicesRadsecCertificatesAuthority(self, organizationId: str):
        """
        **Create an organization's RADSEC device Certificate Authority (CA)**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-devices-radsec-certificates-authority

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities"],
            "operation": "createOrganizationWirelessDevicesRadsecCertificatesAuthority",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities"

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
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities", "crls"],
            "operation": "getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrls",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities/crls"

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
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
                    f"getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrls: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["wireless", "configure", "devices", "radsec", "certificates", "authorities", "crls", "deltas"],
            "operation": "getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrlsDeltas",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/radsec/certificates/authorities/crls/deltas"

        query_params = [
            "certificateAuthorityIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "certificateAuthorityIds",
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
                    f"getOrganizationWirelessDevicesRadsecCertificatesAuthoritiesCrlsDeltas: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessDevicesSignalQualityByClient(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Get average signal quality for all clients in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-signal-quality-by-client

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial number.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - macs (array): Filter results by client mac address(es).
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "signalQuality", "byClient"],
            "operation": "getOrganizationWirelessDevicesSignalQualityByClient",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/signalQuality/byClient"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "macs",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "macs",
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
                    f"getOrganizationWirelessDevicesSignalQualityByClient: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesSignalQualityByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Get average signal quality for all devices in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-signal-quality-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial number.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "signalQuality", "byDevice"],
            "operation": "getOrganizationWirelessDevicesSignalQualityByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/signalQuality/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
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
                    f"getOrganizationWirelessDevicesSignalQualityByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesSignalQualityByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Get average signal quality for all networks in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-signal-quality-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter results by network.
        - serials (array): Filter results by device serial number.
        - ssids (array): Filter results by SSID number.
        - bands (array): Filter results by band. Valid bands are: 2.4, 5, and 6.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "signalQuality", "byNetwork"],
            "operation": "getOrganizationWirelessDevicesSignalQualityByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/signalQuality/byNetwork"

        query_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "ssids",
            "bands",
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
                    f"getOrganizationWirelessDevicesSignalQualityByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesSystemCpuLoadHistory(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "system", "cpu", "load", "history"],
            "operation": "getOrganizationWirelessDevicesSystemCpuLoadHistory",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/system/cpu/load/history"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesSystemCpuLoadHistory: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesTelemetry(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the wireless device telemetry of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-devices-telemetry

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 200. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 3 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 minutes after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 5 minutes and be less than or equal to 30 minutes. The default is 30 minutes.
        - networkIds (array): Optional parameter to filter results by network.
        - serials (array): Optional parameter to filter results by device serial.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "devices", "telemetry"],
            "operation": "getOrganizationWirelessDevicesTelemetry",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/telemetry"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "t1",
            "timespan",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessDevicesTelemetry: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessDevicesWirelessControllersByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "monitor", "devices", "wirelessControllers", "byDevice"],
            "operation": "getOrganizationWirelessDevicesWirelessControllersByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/devices/wirelessControllers/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "controllerSerials",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "controllerSerials",
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
                    f"getOrganizationWirelessDevicesWirelessControllersByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessLocationScanningByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "configure", "location", "scanning", "byNetwork"],
            "operation": "getOrganizationWirelessLocationScanningByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessLocationScanningByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessLocationScanningReceivers(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "getOrganizationWirelessLocationScanningReceivers",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessLocationScanningReceivers: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationWirelessLocationScanningReceiver(
        self, organizationId: str, network: dict, url: str, version: str, radio: dict, sharedSecret: str, **kwargs
    ):
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
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "createOrganizationWirelessLocationScanningReceiver",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers"

        body_params = [
            "network",
            "url",
            "version",
            "radio",
            "sharedSecret",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessLocationScanningReceiver: ignoring unrecognized kwargs: {invalid}"
                )

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
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "updateOrganizationWirelessLocationScanningReceiver",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        receiverId = urllib.parse.quote(str(receiverId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}"

        body_params = [
            "url",
            "version",
            "radio",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessLocationScanningReceiver: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationWirelessLocationScanningReceiver(self, organizationId: str, receiverId: str):
        """
        **Delete a scanning API receiver**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-location-scanning-receiver

        - organizationId (string): Organization ID
        - receiverId (string): Receiver ID
        """

        metadata = {
            "tags": ["wireless", "configure", "location", "scanning", "receivers"],
            "operation": "deleteOrganizationWirelessLocationScanningReceiver",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        receiverId = urllib.parse.quote(str(receiverId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/scanning/receivers/{receiverId}"

        return self._session.delete(metadata, resource)

    def getOrganizationWirelessLocationWayfindingByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Return Client wayfinding settings**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-location-wayfinding-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter wayfinding settings by network ID.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "location", "wayfinding", "byNetwork"],
            "operation": "getOrganizationWirelessLocationWayfindingByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/location/wayfinding/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessLocationWayfindingByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessMqttSettings(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return MQTT Settings for networks**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-mqtt-settings

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 250. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter mqtt settings by network ID.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "mqtt", "settings"],
            "operation": "getOrganizationWirelessMqttSettings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/mqtt/settings"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationWirelessMqttSettings: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateOrganizationWirelessMqttSettings(self, organizationId: str, network: dict, mqtt: dict, **kwargs):
        """
        **Add new broker config for wireless MQTT**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-mqtt-settings

        - organizationId (string): Organization ID
        - network (object): Add MQTT Settings for network
        - mqtt (object): MQTT Settings for network
        - ble (object): MQTT BLE Settings for network
        - wifi (object): MQTT Wi-Fi Settings for network
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "mqtt", "settings"],
            "operation": "updateOrganizationWirelessMqttSettings",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/mqtt/settings"

        body_params = [
            "network",
            "mqtt",
            "ble",
            "wifi",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessMqttSettings: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def byOrganizationWirelessOpportunisticPcapLicenseNetwork(self, organizationId: str, **kwargs):
        """
        **Check the Opportunistic Pcap license status of an organization by network**
        https://developer.cisco.com/meraki/api-v1/#!by-organization-wireless-opportunistic-pcap-license-network

        - organizationId (string): Organization ID
        - networkIds (array): Optional parameter to filter results by network.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "opportunisticPcap", "license"],
            "operation": "byOrganizationWirelessOpportunisticPcapLicenseNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/opportunisticPcap/license/byNetwork"

        query_params = [
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"byOrganizationWirelessOpportunisticPcapLicenseNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessRadioAfcPositionByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the AFC power limits of an organization by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-afc-position-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device's AFC position by network ID.         This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device's AFC position by device serial numbers.         This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "afc", "position", "byDevice"],
            "operation": "getOrganizationWirelessRadioAfcPositionByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/afc/position/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRadioAfcPositionByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessRadioAfcPowerLimitsByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the AFC power limits of an organization by device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-afc-power-limits-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device's AFC power limits by network ID. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device's AFC power limits by device serial numbers. This filter uses multiple exact matches.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "afc", "powerLimits", "byDevice"],
            "operation": "getOrganizationWirelessRadioAfcPowerLimitsByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/afc/powerLimits/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRadioAfcPowerLimitsByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessRadioAutoRfByNetwork(self, organizationId: str, **kwargs):
        """
        **List the AutoRF settings of an organization by network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-auto-rf-by-network

        - organizationId (string): Organization ID
        - networkIds (array): Optional parameter to filter results by network.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "autoRf", "byNetwork"],
            "operation": "getOrganizationWirelessRadioAutoRfByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/autoRf/byNetwork"

        query_params = [
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRadioAutoRfByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessRadioAutoRfChannelsPlanningActivities(self, organizationId: str, **kwargs):
        """
        **List the channel planning activities of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-auto-rf-channels-planning-activities

        - organizationId (string): Organization ID
        - networkIds (array): Optional parameter to filter results by network.
        - deviceSerials (array): Optional parameter to filter results by device serial.
        - bands (array): Optional parameter to filter results by bands. Valid bands are 2.4, 5, and 6.
        - channels (array): Optional parameter to filter results by channels.
        - serials (array): Serial number of the devices for which information should be gathered.
        - gFloorplanId (string): Geoaligned floorplan ID nodes for which information is gathered belong to.
        - tags (array): Optional parameter to filter results by node tags.
        - models (array): Optional parameter to filter results by access point models.
        - rfProfiles (array): Optional parameter to filter results by RF Profiles.
        - minimumRfHealthScore (integer): Minimum RF Health score for an AP to be retrieved.
        - maximumRfHealthScore (integer): Maximum RF Health score for an AP to be retrieved.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "autoRf", "channels", "planning", "activities"],
            "operation": "getOrganizationWirelessRadioAutoRfChannelsPlanningActivities",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/autoRf/channels/planning/activities"

        query_params = [
            "networkIds",
            "deviceSerials",
            "bands",
            "channels",
            "serials",
            "gFloorplanId",
            "tags",
            "models",
            "rfProfiles",
            "minimumRfHealthScore",
            "maximumRfHealthScore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "deviceSerials",
            "bands",
            "channels",
            "serials",
            "tags",
            "models",
            "rfProfiles",
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
                    f"getOrganizationWirelessRadioAutoRfChannelsPlanningActivities: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def recalculateOrganizationWirelessRadioAutoRfChannels(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Recalculates automatically assigned channels for every AP within specified the specified network(s)**
        https://developer.cisco.com/meraki/api-v1/#!recalculate-organization-wireless-radio-auto-rf-channels

        - organizationId (string): Organization ID
        - networkIds (array): A list of network ids (limit: 15).
        """

        kwargs = locals()

        metadata = {
            "tags": ["wireless", "configure", "radio", "autoRf", "channels"],
            "operation": "recalculateOrganizationWirelessRadioAutoRfChannels",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/autoRf/channels/recalculate"

        body_params = [
            "networkIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"recalculateOrganizationWirelessRadioAutoRfChannels: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationWirelessRadioOverridesByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return a list of radio overrides**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-overrides-by-device

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of network IDs. The returned radio overrides will be filtered to only include these networks.
        - serials (array): A list of serial numbers. The returned radio overrides will be filtered to only include these serials.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "overrides", "byDevice"],
            "operation": "getOrganizationWirelessRadioOverridesByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/overrides/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRadioOverridesByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def byOrganizationWirelessRadioRfHealthNeighborsRssiDevice(self, organizationId: str, **kwargs):
        """
        **Show the by-device neighbor rssi information for the organization in the given interval**
        https://developer.cisco.com/meraki/api-v1/#!by-organization-wireless-radio-rf-health-neighbors-rssi-device

        - organizationId (string): Organization ID
        - networkIds (array): Networks for which information should be gathered.
        - bands (array): Bands for which information should be gathered. Valid bands are 2.4, 5, and 6.
        - channels (array): Channel for which information should be gathered.
        - serials (array): Serial number of the devices for which information should be gathered.
        - tags (array): Access Point tags for which information should be gathered.
        - models (array): Access Point models for which information should be gathered.
        - rfProfiles (array): Rf Profiles for which information should be gathered.
        - gFloorplanId (string): Geoaligned floorplan ID nodes for which information is gathered belong to.
        - minimumNeighborRssi (integer): Minimum Neighbor RSSI score for a neighbor entry to be retrieved.
        - maximumNeighborRssi (integer): Maximum Neighbor RSSI score for a neighbor entry to be retrieved.
        - minimumRfHealthScore (integer): Minimum RF Health score for an AP to be retrieved.
        - maximumRfHealthScore (integer): Maximum RF Health score for an AP to be retrieved.
        - rfScoreInterval (integer): Size of the rf score interval in seconds.
        - rfScoreRetryOnEmpty (boolean): If true, the query will be retried further back if no data is present in the latest rf score interval.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "rfHealth", "neighbors", "rssi"],
            "operation": "byOrganizationWirelessRadioRfHealthNeighborsRssiDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/rfHealth/neighbors/rssi/byDevice"

        query_params = [
            "networkIds",
            "bands",
            "channels",
            "serials",
            "tags",
            "models",
            "rfProfiles",
            "gFloorplanId",
            "minimumNeighborRssi",
            "maximumNeighborRssi",
            "minimumRfHealthScore",
            "maximumRfHealthScore",
            "rfScoreInterval",
            "rfScoreRetryOnEmpty",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "bands",
            "channels",
            "serials",
            "tags",
            "models",
            "rfProfiles",
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
                    f"byOrganizationWirelessRadioRfHealthNeighborsRssiDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessRadioRfHealthOverviewByNetworkByInterval(self, organizationId: str, **kwargs):
        """
        **Show the by-network RF Health score overview information for the organization in the given interval**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-rf-health-overview-by-network-by-interval

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 182 days, 14 hours, 54 minutes, and 36 seconds from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 30 days, 10 hours, 29 minutes, and 6 seconds after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 30 days, 10 hours, 29 minutes, and 6 seconds. The default is 14 days. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 7200, 86400. The default is 7200. Interval is calculated if time params are provided.
        - networkIds (array): Networks for which information should be gathered.
        - bands (array): Bands for which information should be gathered. Valid bands are 2.4, 5, and 6.
        - minimumRfHealthScore (integer): Minimum RF Health score for a network to be retrieved.
        - maximumRfHealthScore (integer): Maximum RF Health score for a network to be retrieved.
        - minimumHighCciPercentage (integer): Minimum percentage of radios with high CCI for a network to be retrieved.
        - maximumHighCciPercentage (integer): Maximum percentage of radios with high CCI for a network to be retrieved.
        - minimumChannelChanges (integer): Minimum number of channel changes for a network to be retrieved.
        - maximumChannelChanges (integer): Maximum number of channel changes for a network to be retrieved.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "rfHealth", "overview", "byNetwork", "byInterval"],
            "operation": "getOrganizationWirelessRadioRfHealthOverviewByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/rfHealth/overview/byNetwork/byInterval"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "interval",
            "networkIds",
            "bands",
            "minimumRfHealthScore",
            "maximumRfHealthScore",
            "minimumHighCciPercentage",
            "maximumHighCciPercentage",
            "minimumChannelChanges",
            "maximumChannelChanges",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "bands",
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
                    f"getOrganizationWirelessRadioRfHealthOverviewByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessRadioRrmByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the AutoRF settings of an organization by network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-rrm-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Optional parameter to filter results by network.
        - startingAfter (string): Retrieving items after this network ID
        - endingBefore (string): Retrieving items before this network ID
        - perPage (integer): Number of items per page
        - sortOrder (string): The sort order of items
        """

        kwargs.update(locals())

        if "sortOrder" in kwargs:
            options = ["ascending", "descending"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "radio", "rrm", "byNetwork"],
            "operation": "getOrganizationWirelessRadioRrmByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/rrm/byNetwork"

        query_params = [
            "networkIds",
            "startingAfter",
            "endingBefore",
            "perPage",
            "sortOrder",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRadioRrmByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessRadioStatusByNetwork(self, organizationId: str, **kwargs):
        """
        **Show the status of this organization's radios, categorized by network and device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-radio-status-by-network

        - organizationId (string): Organization ID
        - networkIds (array): Networks for which radio status should be returned.
        - serials (array): Serials for which radio status should be returned.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "radio", "status", "byNetwork"],
            "operation": "getOrganizationWirelessRadioStatusByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/radio/status/byNetwork"

        query_params = [
            "networkIds",
            "serials",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRadioStatusByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessRfProfilesAssignmentsByDevice(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "configure", "rfProfiles", "assignments", "byDevice"],
            "operation": "getOrganizationWirelessRfProfilesAssignmentsByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/rfProfiles/assignments/byDevice"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "productTypes",
            "name",
            "mac",
            "serial",
            "model",
            "macs",
            "serials",
            "models",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "productTypes",
            "macs",
            "serials",
            "models",
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
                    f"getOrganizationWirelessRfProfilesAssignmentsByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessRoamingByNetworkByInterval(self, organizationId: str, networkIds: list, **kwargs):
        """
        **Get all wireless clients' roam events within the specified timespan grouped by network and time interval.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-roaming-by-network-by-interval

        - organizationId (string): Organization ID
        - networkIds (array): Filter results by network.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 14 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 7 days.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 300, 600, 1800, 3600, 7200, 10800, 14400, 18000, 21600, 25200, 28800, 32400, 36000, 39600, 43200, 86400, 604800. The default is 7200.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "monitor", "roaming", "byNetwork", "byInterval"],
            "operation": "getOrganizationWirelessRoamingByNetworkByInterval",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/roaming/byNetwork/byInterval"

        query_params = [
            "networkIds",
            "t0",
            "t1",
            "timespan",
            "interval",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessRoamingByNetworkByInterval: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get(metadata, resource, params)

    def getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
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
            "tags": ["wireless", "configure", "ssids", "firewall", "isolation", "allowlist", "entries"],
            "operation": "getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "ssids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssids",
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
                    f"getOrganizationWirelessSsidsFirewallIsolationAllowlistEntries: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(
        self, organizationId: str, client: dict, ssid: dict, network: dict, **kwargs
    ):
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
            "tags": ["wireless", "configure", "ssids", "firewall", "isolation", "allowlist", "entries"],
            "operation": "createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries"

        body_params = [
            "description",
            "client",
            "ssid",
            "network",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessSsidsFirewallIsolationAllowlistEntry: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry(self, organizationId: str, entryId: str):
        """
        **Destroy isolation allow list MAC entry for this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-firewall-isolation-allowlist-entry

        - organizationId (string): Organization ID
        - entryId (string): Entry ID
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "firewall", "isolation", "allowlist", "entries"],
            "operation": "deleteOrganizationWirelessSsidsFirewallIsolationAllowlistEntry",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        entryId = urllib.parse.quote(str(entryId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}"

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
            "tags": ["wireless", "configure", "ssids", "firewall", "isolation", "allowlist", "entries"],
            "operation": "updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        entryId = urllib.parse.quote(str(entryId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/firewall/isolation/allowlist/entries/{entryId}"

        body_params = [
            "description",
            "client",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessSsidsFirewallIsolationAllowlistEntry: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def getOrganizationWirelessSsidsOpenRoamingByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns an array of objects, each containing SSID OpenRoaming configs for the corresponding network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-open-roaming-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter OpenRoaming configuration by Network Id.
        - includeDisabledSsids (boolean): Optional parameter to include OpenRoaming configuration for disabled ssids.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "openRoaming", "byNetwork"],
            "operation": "getOrganizationWirelessSsidsOpenRoamingByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/openRoaming/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "includeDisabledSsids",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessSsidsOpenRoamingByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessSsidsPoliciesClientExclusionBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns an array of objects, each containing client exclusion enablement statuses for one SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-policies-client-exclusion-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter by Network ID.
        - includeDisabledSsids (boolean): Optional parameter to include disabled SSID's.
        - ssidNumbers (array): Optional parameter to filter by SSID numbers.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "policies", "clientExclusion", "bySsid"],
            "operation": "getOrganizationWirelessSsidsPoliciesClientExclusionBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/policies/clientExclusion/bySsid"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "includeDisabledSsids",
            "ssidNumbers",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssidNumbers",
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
                    f"getOrganizationWirelessSsidsPoliciesClientExclusionBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessSsidsPoliciesClientExclusionStaticExclusionsBySsid(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **Returns an array of objects, each containing a list of MAC's excluded from a given SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-policies-client-exclusion-static-exclusions-by-ssid

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter Network ID.
        - includeDisabledSsids (boolean): Optional parameter to include disabled SSID's.
        - ssidNumbers (array): Optional parameter to filter by SSID numbers.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "policies", "clientExclusion", "static", "exclusions", "bySsid"],
            "operation": "getOrganizationWirelessSsidsPoliciesClientExclusionStaticExclusionsBySsid",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/policies/clientExclusion/static/exclusions/bySsid"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "includeDisabledSsids",
            "ssidNumbers",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssidNumbers",
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
                    f"getOrganizationWirelessSsidsPoliciesClientExclusionStaticExclusionsBySsid: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessSsidsProfiles(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns the SSID profiles for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-profiles

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - name (string): (Optional) Filter results by name. Case insensitive substring match.
        - sortBy (string): Column to sort results by. Default is `name`.
        - sortOrder (string): Direction to sort results by. Default is `asc`.
        - profileIds (array): (Optional) Filter results by a list of SSID profile IDs.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["name"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles"],
            "operation": "getOrganizationWirelessSsidsProfiles",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles"

        query_params = [
            "name",
            "sortBy",
            "sortOrder",
            "profileIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "profileIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationWirelessSsidsProfiles: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationWirelessSsidsProfile(self, organizationId: str, name: str, ssid: dict, **kwargs):
        """
        **Create a new SSID profile in an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-profile

        - organizationId (string): Organization ID
        - name (string): Name of the SSID profile
        - ssid (object): SSID configuration for the profile
        - precedence (object): Precedence configuration for the SSID profile
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles"],
            "operation": "createOrganizationWirelessSsidsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles"

        body_params = [
            "name",
            "precedence",
            "ssid",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessSsidsProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationWirelessSsidsProfilesAssignments(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the SSID profile assignments in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-profiles-assignments

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): The network IDs to include in the result set.
        - ssidIds (array): The SSID IDs to include in the result set.
        - profileIds (array): The SSID profile IDs to include in the result set.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles", "assignments"],
            "operation": "getOrganizationWirelessSsidsProfilesAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/assignments"

        query_params = [
            "networkIds",
            "ssidIds",
            "profileIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "ssidIds",
            "profileIds",
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
                    f"getOrganizationWirelessSsidsProfilesAssignments: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def createOrganizationWirelessSsidsProfilesAssignment(self, organizationId: str, profile: dict, ssid: dict, **kwargs):
        """
        **Assigns an SSID profile to an SSID in the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-ssids-profiles-assignment

        - organizationId (string): Organization ID
        - profile (object): SSID profile to assign
        - ssid (object): SSID to assign the SSID profile to
        - network (object): Network containing the SSID (required if SSID number is used)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles", "assignments"],
            "operation": "createOrganizationWirelessSsidsProfilesAssignment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/assignments"

        body_params = [
            "profile",
            "ssid",
            "network",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessSsidsProfilesAssignment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def deleteOrganizationWirelessSsidsProfilesAssignments(self, organizationId: str, ssid: dict, **kwargs):
        """
        **Unassigns the SSID profile assigned to an SSID**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-profiles-assignments

        - organizationId (string): Organization ID
        - ssid (object): SSID to delete the SSID profile assignment of
        - network (object): Network containing the SSID (required if SSID number is used)
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles", "assignments"],
            "operation": "deleteOrganizationWirelessSsidsProfilesAssignments",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/assignments"

        return self._session.delete(metadata, resource)

    def getOrganizationWirelessSsidsProfilesAssignmentsByNetwork(
        self, organizationId: str, total_pages=1, direction="next", **kwargs
    ):
        """
        **List the SSID profile assignments in an organization, grouped by network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-profiles-assignments-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): The network IDs to include in the result set.
        - profileIds (array): The SSID profile IDs to include in the result set.
        - networkGroupIds (array): The network group IDs to include in the result set.
        - includeAllNetworks (boolean): When set to true, include all networks in the organization, even those without any SSID profile assignments. Defaults to false.
        - excludeProfileIds (array): The SSID profile IDs to exclude from the result set.
        - sortBy (string): Optional parameter to specify the field used to sort results. (default: network)
        - sortOrder (string): Optional parameter to specify the sort order. Default value is asc.
        - search (string): Optional parameter to search on network name or network group name.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["group", "network"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles", "assignments", "byNetwork"],
            "operation": "getOrganizationWirelessSsidsProfilesAssignmentsByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/assignments/byNetwork"

        query_params = [
            "networkIds",
            "profileIds",
            "networkGroupIds",
            "includeAllNetworks",
            "excludeProfileIds",
            "sortBy",
            "sortOrder",
            "search",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "profileIds",
            "networkGroupIds",
            "excludeProfileIds",
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
                    f"getOrganizationWirelessSsidsProfilesAssignmentsByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessSsidsProfilesOverviews(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Returns the SSID profiles' overview information for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-ssids-profiles-overviews

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - name (string): (Optional) Filter results by name. Case insensitive substring match.
        - sortBy (string): Column to sort results by. Default is `name`.
        - sortOrder (string): Direction to sort results by. Default is `asc`.
        - profileIds (array): (Optional) Filter results by a list of SSID profile IDs.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if "sortBy" in kwargs:
            options = ["name"]
            assert kwargs["sortBy"] in options, (
                f'''"sortBy" cannot be "{kwargs["sortBy"]}", & must be set to one of: {options}'''
            )
        if "sortOrder" in kwargs:
            options = ["asc", "desc"]
            assert kwargs["sortOrder"] in options, (
                f'''"sortOrder" cannot be "{kwargs["sortOrder"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles", "overviews"],
            "operation": "getOrganizationWirelessSsidsProfilesOverviews",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/overviews"

        query_params = [
            "name",
            "sortBy",
            "sortOrder",
            "profileIds",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "profileIds",
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
                    f"getOrganizationWirelessSsidsProfilesOverviews: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateOrganizationWirelessSsidsProfile(self, organizationId: str, id: str, **kwargs):
        """
        **Update this SSID profile**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-ssids-profile

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of the SSID profile
        - ssid (object): SSID configuration for the profile
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles"],
            "operation": "updateOrganizationWirelessSsidsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/{id}"

        body_params = [
            "name",
            "ssid",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessSsidsProfile: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def deleteOrganizationWirelessSsidsProfile(self, organizationId: str, id: str):
        """
        **Delete an SSID profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-wireless-ssids-profile

        - organizationId (string): Organization ID
        - id (string): ID
        """

        metadata = {
            "tags": ["wireless", "configure", "ssids", "profiles"],
            "operation": "deleteOrganizationWirelessSsidsProfile",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/profiles/{id}"

        return self._session.delete(metadata, resource)

    def getOrganizationWirelessSsidsStatusesByDevice(self, organizationId: str, total_pages=1, direction="next", **kwargs):
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
            "tags": ["wireless", "monitor", "ssids", "statuses", "byDevice"],
            "operation": "getOrganizationWirelessSsidsStatusesByDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/ssids/statuses/byDevice"

        query_params = [
            "networkIds",
            "serials",
            "bssids",
            "hideDisabled",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
            "serials",
            "bssids",
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
                    f"getOrganizationWirelessSsidsStatusesByDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessZigbeeByNetwork(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return list of Zigbee configs**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Filter by specified Network IDs
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "byNetwork"],
            "operation": "getOrganizationWirelessZigbeeByNetwork",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/byNetwork"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessZigbeeByNetwork: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationWirelessZigbeeDevices(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the Zigbee wireless devices for an organization or the supplied network(s)**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-devices

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Parameter of networks you want the zigbee devices for. E.g.: networkIds[]=N_12345678&networkIds[]=N_3456
        - isEnrolled (boolean): Filter devices based on if they are enrolled or not
        - search (string): Filter devices by their name, tag or serial
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "devices"],
            "operation": "getOrganizationWirelessZigbeeDevices",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/devices"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "networkIds",
            "isEnrolled",
            "search",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
        ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f"{k.strip()}[]"] = kwargs[f"{k}"]
                params.pop(k.strip())

        if self._session._validate_kwargs:
            all_params = query_params + array_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getOrganizationWirelessZigbeeDevices: ignoring unrecognized kwargs: {invalid}")

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateOrganizationWirelessZigbeeDevice(self, organizationId: str, id: str, enrolled: bool, **kwargs):
        """
        **Endpoint to update zigbee gateways**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-device

        - organizationId (string): Organization ID
        - id (string): ID
        - enrolled (boolean): Parameter to enroll or unenroll the zigbee devices
        - channel (string): The new channel for the zigbee device
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "devices"],
            "operation": "updateOrganizationWirelessZigbeeDevice",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/devices/{id}"

        body_params = [
            "enrolled",
            "channel",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessZigbeeDevice: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)

    def createOrganizationWirelessZigbeeDisenrollment(self, organizationId: str, **kwargs):
        """
        **Enqueue a job to start disenrolling door locks on zigbee configured wireless devices**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-wireless-zigbee-disenrollment

        - organizationId (string): Organization ID
        - doorLockIds (array): A list of Meraki door lock ids to disenroll from the device
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "disenrollments"],
            "operation": "createOrganizationWirelessZigbeeDisenrollment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/disenrollments"

        body_params = [
            "doorLockIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createOrganizationWirelessZigbeeDisenrollment: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getOrganizationWirelessZigbeeDisenrollment(self, organizationId: str, disenrollmentId: str):
        """
        **Return a disenrollment**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-disenrollment

        - organizationId (string): Organization ID
        - disenrollmentId (string): Disenrollment ID
        """

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "disenrollments"],
            "operation": "getOrganizationWirelessZigbeeDisenrollment",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        disenrollmentId = urllib.parse.quote(str(disenrollmentId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/disenrollments/{disenrollmentId}"

        return self._session.get(metadata, resource)

    def getOrganizationWirelessZigbeeDoorLocks(self, organizationId: str, total_pages=1, direction="next", **kwargs):
        """
        **Return the list of door locks for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-wireless-zigbee-door-locks

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - networkIds (array): Filter by specified Network IDs
        - serial (string): Filter by device serial
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 500. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "doorLocks"],
            "operation": "getOrganizationWirelessZigbeeDoorLocks",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/doorLocks"

        query_params = [
            "networkIds",
            "serial",
            "perPage",
            "startingAfter",
            "endingBefore",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = [
            "networkIds",
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
                    f"getOrganizationWirelessZigbeeDoorLocks: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateOrganizationWirelessZigbeeDoorLock(self, organizationId: str, doorLockId: str, **kwargs):
        """
        **Endpoint to batch update door locks params**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-wireless-zigbee-door-lock

        - organizationId (string): Organization ID
        - doorLockId (string): Door lock ID
        - name (string): Door lock name to update
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["wireless", "configure", "zigbee", "doorLocks"],
            "operation": "updateOrganizationWirelessZigbeeDoorLock",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        doorLockId = urllib.parse.quote(str(doorLockId), safe="")
        resource = f"/organizations/{organizationId}/wireless/zigbee/doorLocks/{doorLockId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"updateOrganizationWirelessZigbeeDoorLock: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.put(metadata, resource, payload)
