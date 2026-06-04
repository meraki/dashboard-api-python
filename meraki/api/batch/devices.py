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

        serial = urllib.parse.quote(serial, safe="")
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
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateDeviceCellularGeolocations(self, serial: str, enabled: bool, **kwargs):
        """
        **Update the enablement of the geolocation feature for a device**
        https://developer.cisco.com/meraki/api-v1/#!update-device-cellular-geolocations

        - serial (string): Serial
        - enabled (boolean): Required parameter for the state to update the geolocation settings to (true to enable, false to disable)
        """

        kwargs = locals()

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/cellular/geolocations"

        body_params = [
            "enabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

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

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/cellular/uplinks/bands/masks/update"

        body_params = [
            "slot",
            "type",
            "masked",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createDeviceLiveToolsLedsBlink(self, serial: str, duration: int, **kwargs):
        """
        **Enqueue a job to blink LEDs on a device. This endpoint has a rate limit of one request every 10 seconds.**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-leds-blink

        - serial (string): Serial
        - duration (integer): The duration in seconds to blink LEDs.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/liveTools/leds/blink"

        body_params = [
            "duration",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "blink",
            "body": payload,
        }
        return action

    def createDeviceLiveToolsPortsStatus(self, serial: str, **kwargs):
        """
        **Enqueue a job to retrieve port status for a device. This endpoint has a sustained rate limit of one request every five seconds per device, with an allowed burst of five requests.**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-ports-status

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/liveTools/ports/status"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "status",
            "body": payload,
        }
        return action

    def createDeviceLiveToolsPowerUsage(self, serial: str, **kwargs):
        """
        **Enqueues a live tool job that retrieves details about a device's overall power usage. This endpoint has a sustained rate limit of one request every five seconds per device, with an allowed burst of five requests.**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-power-usage

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/liveTools/power/usage"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "job",
            "body": payload,
        }
        return action

    def createDeviceLiveToolsRoutingTableLookup(self, serial: str, **kwargs):
        """
        **Enqueue a job to perform a routing table lookup request for a device. The routing table lookup request fetches a specific set of routes based on filters. Any combination of search filters can be applied. Only Cisco Secure Routers are supported.**
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

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/liveTools/routingTable/lookups"

        body_params = [
            "type",
            "destination",
            "nextHop",
            "vpn",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "lookup",
            "body": payload,
        }
        return action

    def createDeviceLiveToolsRoutingTableSummary(self, serial: str, **kwargs):
        """
        **Enqueue a routing table summary job for a device. The job fetches summary data such as route counts by VRF and protocol. Only Cisco Secure Routers are supported.**
        https://developer.cisco.com/meraki/api-v1/#!create-device-live-tools-routing-table-summary

        - serial (string): Serial
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/liveTools/routingTable/summaries"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "summary",
            "body": payload,
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

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/liveTools/throughputTest"

        body_params = [
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "test",
            "body": payload,
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

        serial = urllib.parse.quote(serial, safe="")
        resource = f"/devices/{serial}/managementInterface"

        body_params = [
            "wan1",
            "wan2",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action
