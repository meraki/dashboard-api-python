import urllib


class AsyncDevices:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getDevice(self, serial: str):
        """
        **Return a single device**
        https://developer.cisco.com/meraki/api-v1/#!get-device

        - serial (string): Serial
        """

        metadata = {
            "tags": ["devices", "configure"],
            "operation": "getDevice",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}"

        return self._session.get(metadata, resource)

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
            "tags": ["devices", "configure"],
            "operation": "updateDevice",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}"

        body_params = [
            "name",
            "tags",
            "lat",
            "lng",
            "address",
            "notes",
            "moveMapMarker",
            "switchProfileId",
            "floorPlanId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDevice: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def blinkDeviceLeds(self, serial: str, **kwargs):
        """
        **Blink the LEDs on a device**
        https://developer.cisco.com/meraki/api-v1/#!blink-device-leds

        - serial (string): Serial
        - duration (integer): The duration in seconds. Must be between 5 and 120. Default is 20 seconds
        - period (integer): The period in milliseconds. Must be between 100 and 1000. Default is 160 milliseconds
        - duty (integer): The duty cycle as the percent active. Must be between 10 and 90. Default is 50.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools"],
            "operation": "blinkDeviceLeds",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/blinkLeds"

        body_params = [
            "duration",
            "period",
            "duty",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"blinkDeviceLeds: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateDeviceCellularGeolocations(self, serial: str, enabled: bool, **kwargs):
        """
        **Update the enablement of the geolocation feature for a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-geolocations

        - serial (string): Serial
        - enabled (boolean): Required parameter for the state to update the geolocation settings to (true to enable, false to disable)
        """

        kwargs = locals()

        metadata = {
            "tags": ["devices", "configure", "cellular", "geolocations"],
            "operation": "updateDeviceCellularGeolocations",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellular/geolocations"

        body_params = [
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceCellularGeolocations: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getDeviceCellularSims(self, serial: str):
        """
        **Return the SIM and APN configurations for a cellular device.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-cellular-sims

        - serial (string): Serial
        """

        metadata = {
            "tags": ["devices", "configure", "cellular", "sims"],
            "operation": "getDeviceCellularSims",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellular/sims"

        return self._session.get(metadata, resource)

    def updateDeviceCellularSims(self, serial: str, **kwargs):
        """
        **Updates the SIM and APN configurations for a cellular device.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-sims

        - serial (string): Serial
        - sims (array): List of SIMs. If a SIM was previously configured and not specified in this request, it will remain unchanged.
        - simOrdering (array): Specifies the ordering of all SIMs for an MG: primary, secondary, and not-in-use (when applicable). It's required for devices with 3 or more SIMs and can be used in place of 'isPrimary' for dual-SIM devices. To indicate eSIM, use 'sim3'. Sim failover will occur only between primary and secondary sim slots.
        - simFailover (object): SIM Failover settings.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "configure", "cellular", "sims"],
            "operation": "updateDeviceCellularSims",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellular/sims"

        body_params = [
            "sims",
            "simOrdering",
            "simFailover",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceCellularSims: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def createDeviceCellularUplinksBandsMasksUpdate(self, serial: str, slot: str, type: str, masked: list, **kwargs):
        """
        **Update the cellular band masks for a device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-cellular-uplinks-bands-masks-update

        - serial (string): Serial
        - slot (string): Required parameter for the SIM slot to update the cellular band mask for
        - type (string): Required parameter for the signal type to update the cellular band mask for
        - masked (array): Required parameter for the band identifiers to mask for the given SIM slot and signal type. For LTE use bands identifiers like '30' and for 5G use band identifiers like 'n30'. Maximum 256 bands.
        """

        kwargs = locals()

        if "slot" in kwargs:
            options = ["sim1", "sim2", "sim3"]
            assert kwargs["slot"] in options, f'''"slot" cannot be "{kwargs["slot"]}", & must be set to one of: {options}'''
        if "type" in kwargs:
            options = ["5GNSA", "5GSA", "LTE"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["devices", "configure", "cellular", "uplinks", "bands", "masks", "update"],
            "operation": "createDeviceCellularUplinksBandsMasksUpdate",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/cellular/uplinks/bands/masks/update"

        body_params = [
            "slot",
            "type",
            "masked",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createDeviceCellularUplinksBandsMasksUpdate: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getDeviceClients(self, serial: str, **kwargs):
        """
        **List the clients of a device, up to a maximum of a month ago**
        https://developer.cisco.com/meraki/api-v1/#!get-device-clients

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "monitor", "clients"],
            "operation": "getDeviceClients",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/clients"

        query_params = [
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceClients: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def createDeviceLiveToolsArpTable(self, serial: str, **kwargs):
        """
        **Enqueue a job to perform a ARP table request for the device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-arp-table

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "arpTable"],
            "operation": "createDeviceLiveToolsArpTable",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/arpTable"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsArpTable: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsArpTable(self, serial: str, arpTableId: str):
        """
        **Return an ARP table live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-arp-table

        - serial (string): Serial
        - arpTableId (string): Arp table ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "arpTable"],
            "operation": "getDeviceLiveToolsArpTable",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        arpTableId = urllib.parse.quote(str(arpTableId), safe="")
        resource = f"/devices/{serial}/liveTools/arpTable/{arpTableId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsCableTest(self, serial: str, ports: list, **kwargs):
        """
        **Enqueue a job to perform a cable test for the device on the specified ports**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-cable-test

        - serial (string): Serial
        - ports (array): A list of ports for which to perform the cable test.  For Catalyst switches, IOS interface names are also supported, such as "GigabitEthernet1/0/8", "Gi1/0/8", or even "1/0/8".
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "cableTest"],
            "operation": "createDeviceLiveToolsCableTest",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/cableTest"

        body_params = [
            "ports",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsCableTest: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsCableTest(self, serial: str, id: str):
        """
        **Return a cable test live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-cable-test

        - serial (string): Serial
        - id (string): ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "cableTest"],
            "operation": "getDeviceLiveToolsCableTest",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/cableTest/{id}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsLedsBlink(self, serial: str, duration: int, **kwargs):
        """
        **Enqueue a job to blink LEDs on a device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-leds-blink

        - serial (string): Serial
        - duration (integer): The duration in seconds to blink LEDs.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "leds", "blink"],
            "operation": "createDeviceLiveToolsLedsBlink",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/leds/blink"

        body_params = [
            "duration",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsLedsBlink: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsLedsBlink(self, serial: str, ledsBlinkId: str):
        """
        **Return a blink LEDs job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-leds-blink

        - serial (string): Serial
        - ledsBlinkId (string): Leds blink ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "leds", "blink"],
            "operation": "getDeviceLiveToolsLedsBlink",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        ledsBlinkId = urllib.parse.quote(str(ledsBlinkId), safe="")
        resource = f"/devices/{serial}/liveTools/leds/blink/{ledsBlinkId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsMacTable(self, serial: str, **kwargs):
        """
        **Enqueue a job to request the MAC table from the device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-mac-table

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "macTable"],
            "operation": "createDeviceLiveToolsMacTable",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/macTable"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsMacTable: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsMacTable(self, serial: str, macTableId: str):
        """
        **Return a MAC table live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-mac-table

        - serial (string): Serial
        - macTableId (string): Mac table ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "macTable"],
            "operation": "getDeviceLiveToolsMacTable",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        macTableId = urllib.parse.quote(str(macTableId), safe="")
        resource = f"/devices/{serial}/liveTools/macTable/{macTableId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsMulticastRouting(self, serial: str, **kwargs):
        """
        **Enqueue a job to perform a Multicast routing request for the device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-multicast-routing

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "multicastRouting"],
            "operation": "createDeviceLiveToolsMulticastRouting",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/multicastRouting"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createDeviceLiveToolsMulticastRouting: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsMulticastRouting(self, serial: str, multicastRoutingId: str):
        """
        **Return a Multicast routing live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-multicast-routing

        - serial (string): Serial
        - multicastRoutingId (string): Multicast routing ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "multicastRouting"],
            "operation": "getDeviceLiveToolsMulticastRouting",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        multicastRoutingId = urllib.parse.quote(str(multicastRoutingId), safe="")
        resource = f"/devices/{serial}/liveTools/multicastRouting/{multicastRoutingId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsPing(self, serial: str, target: str, **kwargs):
        """
        **Enqueue a job to ping a target host from the device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping

        - serial (string): Serial
        - target (string): FQDN, IPv4 or IPv6 address
        - count (integer): Count parameter to pass to ping. [1..5], default 5
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "ping"],
            "operation": "createDeviceLiveToolsPing",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/ping"

        body_params = [
            "target",
            "count",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsPing: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsPing(self, serial: str, id: str):
        """
        **Return a ping job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping

        - serial (string): Serial
        - id (string): ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "ping"],
            "operation": "getDeviceLiveToolsPing",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/ping/{id}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsPingDevice(self, serial: str, **kwargs):
        """
        **Enqueue a job to check connectivity status to the device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ping-device

        - serial (string): Serial
        - count (integer): Count parameter to pass to ping. [1..5], default 5
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "pingDevice"],
            "operation": "createDeviceLiveToolsPingDevice",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/pingDevice"

        body_params = [
            "count",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsPingDevice: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsPingDevice(self, serial: str, id: str):
        """
        **Return a ping device job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ping-device

        - serial (string): Serial
        - id (string): ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "pingDevice"],
            "operation": "getDeviceLiveToolsPingDevice",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/pingDevice/{id}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsPortsCycle(self, serial: str, ports: list, **kwargs):
        """
        **Enqueue a job to perform a cycle port for the device on the specified ports**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ports-cycle

        - serial (string): Serial
        - ports (array): A list of ports to cycle. For Catalyst switches, IOS interface names are also supported, such as "GigabitEthernet1/0/8", "Gi1/0/8", or even "1/0/8".
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "ports", "cycle"],
            "operation": "createDeviceLiveToolsPortsCycle",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/ports/cycle"

        body_params = [
            "ports",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsPortsCycle: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsPortsCycle(self, serial: str, id: str):
        """
        **Return a cycle port live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ports-cycle

        - serial (string): Serial
        - id (string): ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "ports", "cycle"],
            "operation": "getDeviceLiveToolsPortsCycle",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/ports/cycle/{id}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsPortsStatus(self, serial: str, **kwargs):
        """
        **Enqueue a job to retrieve port status for a device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ports-status

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "ports", "status"],
            "operation": "createDeviceLiveToolsPortsStatus",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/ports/status"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsPortsStatus: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsPortsStatus(self, serial: str, jobId: str):
        """
        **Return a port status live tool job.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-ports-status

        - serial (string): Serial
        - jobId (string): Job ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "ports", "status"],
            "operation": "getDeviceLiveToolsPortsStatus",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        jobId = urllib.parse.quote(str(jobId), safe="")
        resource = f"/devices/{serial}/liveTools/ports/status/{jobId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsPowerUsage(self, serial: str, **kwargs):
        """
        **Enqueues a live tool job that retrieves details about a device's overall power usage**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-power-usage

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "power", "usage"],
            "operation": "createDeviceLiveToolsPowerUsage",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/power/usage"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsPowerUsage: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsPowerUsage(self, serial: str, jobId: str):
        """
        **Retrieve the status and results of a previously created live tool job fetching details about a device's overall power usage.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-power-usage

        - serial (string): Serial
        - jobId (string): Job ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "power", "usage"],
            "operation": "getDeviceLiveToolsPowerUsage",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        jobId = urllib.parse.quote(str(jobId), safe="")
        resource = f"/devices/{serial}/liveTools/power/usage/{jobId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsRoutingTableLookup(self, serial: str, **kwargs):
        """
        **Enqueue a job to perform a routing table lookup request for a device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-routing-table-lookup

        - serial (string): Serial
        - type (string): The type of route defined
        - destination (object): The destination IP or subnet to lookup
        - nextHop (object): The next hop to lookup
        - vpn (object): VPN related search criteria
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "BGP",
                "EIGRP",
                "HSRP",
                "IGRP",
                "ISIS",
                "LISP",
                "NAT",
                "ND",
                "NHRP",
                "OMP",
                "OSPF",
                "RIP",
                "default WAN",
                "direct",
                "static",
            ]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        metadata = {
            "tags": ["devices", "liveTools", "routingTable", "lookups"],
            "operation": "createDeviceLiveToolsRoutingTableLookup",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/routingTable/lookups"

        body_params = [
            "type",
            "destination",
            "nextHop",
            "vpn",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createDeviceLiveToolsRoutingTableLookup: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsRoutingTableLookup(self, serial: str, id: str):
        """
        **Return a routing table live tool lookup job for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-routing-table-lookup

        - serial (string): Serial
        - id (string): ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "routingTable", "lookups"],
            "operation": "getDeviceLiveToolsRoutingTableLookup",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/routingTable/lookups/{id}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsRoutingTableSummary(self, serial: str, **kwargs):
        """
        **Enqueue a routing table summary job for a device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-routing-table-summary

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "routingTable", "summaries"],
            "operation": "createDeviceLiveToolsRoutingTableSummary",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/routingTable/summaries"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(
                    f"createDeviceLiveToolsRoutingTableSummary: ignoring unrecognized kwargs: {invalid}"
                )

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsRoutingTableSummary(self, serial: str, id: str):
        """
        **Return the status and result of a routing table summary job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-routing-table-summary

        - serial (string): Serial
        - id (string): ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "routingTable", "summaries"],
            "operation": "getDeviceLiveToolsRoutingTableSummary",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        id = urllib.parse.quote(str(id), safe="")
        resource = f"/devices/{serial}/liveTools/routingTable/summaries/{id}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsThroughputTest(self, serial: str, **kwargs):
        """
        **Enqueue a job to test a device throughput, the test will run for 10 secs to test throughput**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-throughput-test

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "throughputTest"],
            "operation": "createDeviceLiveToolsThroughputTest",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/throughputTest"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsThroughputTest: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsThroughputTest(self, serial: str, throughputTestId: str):
        """
        **Return a throughput test job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-throughput-test

        - serial (string): Serial
        - throughputTestId (string): Throughput test ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "throughputTest"],
            "operation": "getDeviceLiveToolsThroughputTest",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        throughputTestId = urllib.parse.quote(str(throughputTestId), safe="")
        resource = f"/devices/{serial}/liveTools/throughputTest/{throughputTestId}"

        return self._session.get(metadata, resource)

    def createDeviceLiveToolsWakeOnLan(self, serial: str, vlanId: int, mac: str, **kwargs):
        """
        **Enqueue a job to send a Wake-on-LAN packet from the device**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-wake-on-lan

        - serial (string): Serial
        - vlanId (integer): The target's VLAN (1 to 4094)
        - mac (string): The target's MAC address
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["devices", "liveTools", "wakeOnLan"],
            "operation": "createDeviceLiveToolsWakeOnLan",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/liveTools/wakeOnLan"

        body_params = [
            "vlanId",
            "mac",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createDeviceLiveToolsWakeOnLan: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def getDeviceLiveToolsWakeOnLan(self, serial: str, wakeOnLanId: str):
        """
        **Return a Wake-on-LAN job**
        https://developer.cisco.com/meraki/api-v1/#!get-device-live-tools-wake-on-lan

        - serial (string): Serial
        - wakeOnLanId (string): Wake on lan ID
        """

        metadata = {
            "tags": ["devices", "liveTools", "wakeOnLan"],
            "operation": "getDeviceLiveToolsWakeOnLan",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        wakeOnLanId = urllib.parse.quote(str(wakeOnLanId), safe="")
        resource = f"/devices/{serial}/liveTools/wakeOnLan/{wakeOnLanId}"

        return self._session.get(metadata, resource)

    def getDeviceLldpCdp(self, serial: str):
        """
        **List LLDP and CDP information for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-lldp-cdp

        - serial (string): Serial
        """

        metadata = {
            "tags": ["devices", "monitor", "lldpCdp"],
            "operation": "getDeviceLldpCdp",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/lldpCdp"

        return self._session.get(metadata, resource)

    def getDeviceLossAndLatencyHistory(self, serial: str, ip: str, **kwargs):
        """
        **Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for MX, MG and Z devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-loss-and-latency-history

        - serial (string): Serial
        - ip (string): The destination IP used to obtain the requested stats. This is required.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
        - uplink (string): The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, wan3, cellular, wan4. The default is wan1.
        """

        kwargs.update(locals())

        if "uplink" in kwargs:
            options = ["cellular", "wan1", "wan2", "wan3", "wan4"]
            assert kwargs["uplink"] in options, (
                f'''"uplink" cannot be "{kwargs["uplink"]}", & must be set to one of: {options}'''
            )

        metadata = {
            "tags": ["devices", "monitor", "uplinks", "lossAndLatencyHistory"],
            "operation": "getDeviceLossAndLatencyHistory",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/lossAndLatencyHistory"

        query_params = [
            "t0",
            "t1",
            "timespan",
            "resolution",
            "uplink",
            "ip",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getDeviceLossAndLatencyHistory: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def getDeviceManagementInterface(self, serial: str):
        """
        **Return the management interface settings for a device**
        https://developer.cisco.com/meraki/api-v1/#!get-device-management-interface

        - serial (string): Serial
        """

        metadata = {
            "tags": ["devices", "configure", "managementInterface"],
            "operation": "getDeviceManagementInterface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/managementInterface"

        return self._session.get(metadata, resource)

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
            "tags": ["devices", "configure", "managementInterface"],
            "operation": "updateDeviceManagementInterface",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/managementInterface"

        body_params = [
            "wan1",
            "wan2",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateDeviceManagementInterface: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def rebootDevice(self, serial: str):
        """
        **Reboot a device**
        https://developer.cisco.com/meraki/api-v1/#!reboot-device

        - serial (string): Serial
        """

        metadata = {
            "tags": ["devices", "liveTools"],
            "operation": "rebootDevice",
        }
        serial = urllib.parse.quote(str(serial), safe="")
        resource = f"/devices/{serial}/reboot"

        return self._session.post(metadata, resource)
