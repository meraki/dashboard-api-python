import urllib


class AsyncSm:
    def __init__(self, session):
        super().__init__()
        self._session = session
        


    def createNetworkSmBypassActivationLockAttempt(self, networkId: str, ids: list):
        """
        **Bypass activation lock attempt**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt

        - networkId (string): Network ID
        - ids (array): The ids of the devices to attempt activation lock bypass.
        """

        kwargs = locals()

        metadata = {
            'tags': ['sm', 'configure', 'bypassActivationLockAttempts'],
            'operation': 'createNetworkSmBypassActivationLockAttempt'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts'

        body_params = ['ids', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSmBypassActivationLockAttempt(self, networkId: str, attemptId: str):
        """
        **Bypass activation lock attempt status**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt

        - networkId (string): Network ID
        - attemptId (string): Attempt ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'bypassActivationLockAttempts'],
            'operation': 'getNetworkSmBypassActivationLockAttempt'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        attemptId = urllib.parse.quote(str(attemptId), safe='')
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}'

        return self._session.get(metadata, resource)
        


    def getNetworkSmDevices(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the devices enrolled in an SM network with various specified fields and filters**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - fields (array): Additional fields that will be displayed for each device.
    The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
    systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
    ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
    simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
    isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
    hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, androidSecurityPatchVersion, cellular, and url.
        - wifiMacs (array): Filter devices by wifi mac(s).
        - serials (array): Filter devices by serial(s).
        - ids (array): Filter devices by id(s).
        - uuids (array): Filter devices by uuid(s).
        - systemTypes (array): Filter devices by system type(s).
        - scope (array): Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'getNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices'

        query_params = ['fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['fields', 'wifiMacs', 'serials', 'ids', 'uuids', 'systemTypes', 'scope', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def checkinNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Force check-in a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!checkin-network-sm-devices

        - networkId (string): Network ID
        - wifiMacs (array): The wifiMacs of the devices to be checked-in.
        - ids (array): The ids of the devices to be checked-in.
        - serials (array): The serials of the devices to be checked-in.
        - scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be checked-in.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'checkinNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/checkin'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateNetworkSmDevicesFields(self, networkId: str, deviceFields: dict, **kwargs):
        """
        **Modify the fields of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields

        - networkId (string): Network ID
        - deviceFields (object): The new fields of the device. Each field of this object is optional.
        - wifiMac (string): The wifiMac of the device to be modified.
        - id (string): The id of the device to be modified.
        - serial (string): The serial of the device to be modified.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'fields'],
            'operation': 'updateNetworkSmDevicesFields'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/fields'

        body_params = ['wifiMac', 'id', 'serial', 'deviceFields', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def lockNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Lock a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!lock-network-sm-devices

        - networkId (string): Network ID
        - wifiMacs (array): The wifiMacs of the devices to be locked.
        - ids (array): The ids of the devices to be locked.
        - serials (array): The serials of the devices to be locked.
        - scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be locked.
        - pin (integer): The pin number for locking macOS devices (a six digit number). Required only for macOS devices.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'lockNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/lock'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'pin', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def modifyNetworkSmDevicesTags(self, networkId: str, tags: list, updateAction: str, **kwargs):
        """
        **Add, delete, or update the tags of a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags

        - networkId (string): Network ID
        - tags (array): The tags to be added, deleted, or updated.
        - updateAction (string): One of add, delete, or update. Only devices that have been modified will be returned.
        - wifiMacs (array): The wifiMacs of the devices to be modified.
        - ids (array): The ids of the devices to be modified.
        - serials (array): The serials of the devices to be modified.
        - scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'modifyNetworkSmDevicesTags'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/modifyTags'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'tags', 'updateAction', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def moveNetworkSmDevices(self, networkId: str, newNetwork: str, **kwargs):
        """
        **Move a set of devices to a new network**
        https://developer.cisco.com/meraki/api-v1/#!move-network-sm-devices

        - networkId (string): Network ID
        - newNetwork (string): The new network to which the devices will be moved.
        - wifiMacs (array): The wifiMacs of the devices to be moved.
        - ids (array): The ids of the devices to be moved.
        - serials (array): The serials of the devices to be moved.
        - scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be moved.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'moveNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/move'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'newNetwork', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def rebootNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Reboot a set of endpoints**
        https://developer.cisco.com/meraki/api-v1/#!reboot-network-sm-devices

        - networkId (string): Network ID
        - wifiMacs (array): The wifiMacs of the endpoints to be rebooted.
        - ids (array): The ids of the endpoints to be rebooted.
        - serials (array): The serials of the endpoints to be rebooted.
        - scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the endpoints to be rebooted.
        - kextPaths (array): The KextPaths of the endpoints to be rebooted. Available for macOS 11+
        - notifyUser (boolean): Whether or not to notify the user before rebooting the endpoint. Available for macOS 11.3+
        - rebuildKernelCache (boolean): Whether or not to rebuild the kernel cache when rebooting the endpoint. Available for macOS 11+
        - requestRequiresNetworkTether (boolean): Whether or not the request requires network tethering. Available for macOS and supervised iOS or tvOS
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'rebootNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/reboot'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'kextPaths', 'notifyUser', 'rebuildKernelCache', 'requestRequiresNetworkTether', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def shutdownNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Shutdown a set of endpoints**
        https://developer.cisco.com/meraki/api-v1/#!shutdown-network-sm-devices

        - networkId (string): Network ID
        - wifiMacs (array): The wifiMacs of the endpoints to be shutdown.
        - ids (array): The ids of the endpoints to be shutdown.
        - serials (array): The serials of the endpoints to be shutdown.
        - scope (array): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the endpoints to be shutdown.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'shutdownNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/shutdown'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def wipeNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Wipe a device**
        https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices

        - networkId (string): Network ID
        - wifiMac (string): The wifiMac of the device to be wiped.
        - id (string): The id of the device to be wiped.
        - serial (string): The serial of the device to be wiped.
        - pin (integer): The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'wipeNetworkSmDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/devices/wipe'

        body_params = ['wifiMac', 'id', 'serial', 'pin', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSmDeviceCellularUsageHistory(self, networkId: str, deviceId: str):
        """
        **Return the client's daily cellular data usage history**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'cellularUsageHistory'],
            'operation': 'getNetworkSmDeviceCellularUsageHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory'

        return self._session.get(metadata, resource)
        


    def getNetworkSmDeviceCerts(self, networkId: str, deviceId: str):
        """
        **List the certs on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'certs'],
            'operation': 'getNetworkSmDeviceCerts'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/certs'

        return self._session.get(metadata, resource)
        


    def getNetworkSmDeviceConnectivity(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity

        - networkId (string): Network ID
        - deviceId (string): Device ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'connectivity'],
            'operation': 'getNetworkSmDeviceConnectivity'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/connectivity'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkSmDeviceDesktopLogs(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager network connection details for desktop devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs

        - networkId (string): Network ID
        - deviceId (string): Device ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'desktopLogs'],
            'operation': 'getNetworkSmDeviceDesktopLogs'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/desktopLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkSmDeviceDeviceCommandLogs(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of commands sent to Systems Manager devices**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs

        - networkId (string): Network ID
        - deviceId (string): Device ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'deviceCommandLogs'],
            'operation': 'getNetworkSmDeviceDeviceCommandLogs'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkSmDeviceDeviceProfiles(self, networkId: str, deviceId: str):
        """
        **Get the installed profiles associated with a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'deviceProfiles'],
            'operation': 'getNetworkSmDeviceDeviceProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/deviceProfiles'

        return self._session.get(metadata, resource)
        


    def installNetworkSmDeviceApps(self, networkId: str, deviceId: str, appIds: list, **kwargs):
        """
        **Install applications on a device**
        https://developer.cisco.com/meraki/api-v1/#!install-network-sm-device-apps

        - networkId (string): Network ID
        - deviceId (string): Device ID
        - appIds (array): ids of applications to be installed
        - force (boolean): By default, installation of an app which is believed to already be present on the device will be skipped. If you'd like to force the installation of the app, set this parameter to true.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'installNetworkSmDeviceApps'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/installApps'

        body_params = ['appIds', 'force', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSmDeviceNetworkAdapters(self, networkId: str, deviceId: str):
        """
        **List the network adapters of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'networkAdapters'],
            'operation': 'getNetworkSmDeviceNetworkAdapters'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/networkAdapters'

        return self._session.get(metadata, resource)
        


    def getNetworkSmDevicePerformanceHistory(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager client metrics for desktop devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history

        - networkId (string): Network ID
        - deviceId (string): Device ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'performanceHistory'],
            'operation': 'getNetworkSmDevicePerformanceHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/performanceHistory'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def refreshNetworkSmDeviceDetails(self, networkId: str, deviceId: str):
        """
        **Refresh the details of a device**
        https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'refreshNetworkSmDeviceDetails'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/refreshDetails'

        return self._session.post(metadata, resource)
        


    def getNetworkSmDeviceRestrictions(self, networkId: str, deviceId: str):
        """
        **List the restrictions on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'restrictions'],
            'operation': 'getNetworkSmDeviceRestrictions'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/restrictions'

        return self._session.get(metadata, resource)
        


    def getNetworkSmDeviceSecurityCenters(self, networkId: str, deviceId: str):
        """
        **List the security centers on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'securityCenters'],
            'operation': 'getNetworkSmDeviceSecurityCenters'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/securityCenters'

        return self._session.get(metadata, resource)
        


    def getNetworkSmDeviceSoftwares(self, networkId: str, deviceId: str):
        """
        **Get a list of softwares associated with a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'softwares'],
            'operation': 'getNetworkSmDeviceSoftwares'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/softwares'

        return self._session.get(metadata, resource)
        


    def unenrollNetworkSmDevice(self, networkId: str, deviceId: str):
        """
        **Unenroll a device**
        https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'unenrollNetworkSmDevice'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/unenroll'

        return self._session.post(metadata, resource)
        


    def uninstallNetworkSmDeviceApps(self, networkId: str, deviceId: str, appIds: list):
        """
        **Uninstall applications on a device**
        https://developer.cisco.com/meraki/api-v1/#!uninstall-network-sm-device-apps

        - networkId (string): Network ID
        - deviceId (string): Device ID
        - appIds (array): ids of applications to be uninstalled
        """

        kwargs = locals()

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'uninstallNetworkSmDeviceApps'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/uninstallApps'

        body_params = ['appIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSmDeviceWlanLists(self, networkId: str, deviceId: str):
        """
        **List the saved SSID names on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists

        - networkId (string): Network ID
        - deviceId (string): Device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'wlanLists'],
            'operation': 'getNetworkSmDeviceWlanLists'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        deviceId = urllib.parse.quote(str(deviceId), safe='')
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/wlanLists'

        return self._session.get(metadata, resource)
        


    def getNetworkSmProfiles(self, networkId: str, **kwargs):
        """
        **List all profiles in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles

        - networkId (string): Network ID
        - payloadTypes (array): Filter by payload types
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'profiles'],
            'operation': 'getNetworkSmProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/profiles'

        query_params = ['payloadTypes', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['payloadTypes', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getNetworkSmTargetGroups(self, networkId: str, **kwargs):
        """
        **List the target groups in this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups

        - networkId (string): Network ID
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'getNetworkSmTargetGroups'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/targetGroups'

        query_params = ['withDetails', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def createNetworkSmTargetGroup(self, networkId: str, **kwargs):
        """
        **Add a target group**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group

        - networkId (string): Network ID
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'createNetworkSmTargetGroup'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/targetGroups'

        body_params = ['name', 'scope', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Return a target group**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group

        - networkId (string): Network ID
        - targetGroupId (string): Target group ID
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'getNetworkSmTargetGroup'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        targetGroupId = urllib.parse.quote(str(targetGroupId), safe='')
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        query_params = ['withDetails', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def updateNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Update a target group**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group

        - networkId (string): Network ID
        - targetGroupId (string): Target group ID
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'updateNetworkSmTargetGroup'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        targetGroupId = urllib.parse.quote(str(targetGroupId), safe='')
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        body_params = ['name', 'scope', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkSmTargetGroup(self, networkId: str, targetGroupId: str):
        """
        **Delete a target group from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group

        - networkId (string): Network ID
        - targetGroupId (string): Target group ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'deleteNetworkSmTargetGroup'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        targetGroupId = urllib.parse.quote(str(targetGroupId), safe='')
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSmTrustedAccessConfigs(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List Trusted Access Configs**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-trusted-access-configs

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'trustedAccessConfigs'],
            'operation': 'getNetworkSmTrustedAccessConfigs'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/trustedAccessConfigs'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkSmUserAccessDevices(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List User Access Devices and its Trusted Access Connections**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-access-devices

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'userAccessDevices'],
            'operation': 'getNetworkSmUserAccessDevices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/userAccessDevices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def deleteNetworkSmUserAccessDevice(self, networkId: str, userAccessDeviceId: str):
        """
        **Delete a User Access Device**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        - networkId (string): Network ID
        - userAccessDeviceId (string): User access device ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'userAccessDevices'],
            'operation': 'deleteNetworkSmUserAccessDevice'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        userAccessDeviceId = urllib.parse.quote(str(userAccessDeviceId), safe='')
        resource = f'/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkSmUsers(self, networkId: str, **kwargs):
        """
        **List the owners in an SM network with various specified fields and filters**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-users

        - networkId (string): Network ID
        - ids (array): Filter users by id(s).
        - usernames (array): Filter users by username(s).
        - emails (array): Filter users by email(s).
        - scope (array): Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure'],
            'operation': 'getNetworkSmUsers'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/sm/users'

        query_params = ['ids', 'usernames', 'emails', 'scope', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['ids', 'usernames', 'emails', 'scope', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getNetworkSmUserDeviceProfiles(self, networkId: str, userId: str):
        """
        **Get the profiles associated with a user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles

        - networkId (string): Network ID
        - userId (string): User ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'deviceProfiles'],
            'operation': 'getNetworkSmUserDeviceProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        userId = urllib.parse.quote(str(userId), safe='')
        resource = f'/networks/{networkId}/sm/users/{userId}/deviceProfiles'

        return self._session.get(metadata, resource)
        


    def getNetworkSmUserSoftwares(self, networkId: str, userId: str):
        """
        **Get a list of softwares associated with a user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares

        - networkId (string): Network ID
        - userId (string): User ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'softwares'],
            'operation': 'getNetworkSmUserSoftwares'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        userId = urllib.parse.quote(str(userId), safe='')
        resource = f'/networks/{networkId}/sm/users/{userId}/softwares'

        return self._session.get(metadata, resource)
        


    def getOrganizationSmAdminsRoles(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the Limited Access Roles for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-admins-roles

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'admins', 'roles'],
            'operation': 'getOrganizationSmAdminsRoles'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sm/admins/roles'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def createOrganizationSmAdminsRole(self, organizationId: str, name: str, **kwargs):
        """
        **Create a Limited Access Role**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-admins-role

        - organizationId (string): Organization ID
        - name (string): The name of the Limited Access Role
        - scope (string): The scope of the Limited Access Role
        - tags (array): The tags of the Limited Access Role
        """

        kwargs.update(locals())

        if 'scope' in kwargs:
            options = ['all_tags', 'some', 'without_all_tags', 'without_some']
            assert kwargs['scope'] in options, f'''"scope" cannot be "{kwargs['scope']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['sm', 'configure', 'admins', 'roles'],
            'operation': 'createOrganizationSmAdminsRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sm/admins/roles'

        body_params = ['name', 'scope', 'tags', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationSmAdminsRole(self, organizationId: str, roleId: str):
        """
        **Return a Limited Access Role**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-admins-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'admins', 'roles'],
            'operation': 'getOrganizationSmAdminsRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        roleId = urllib.parse.quote(str(roleId), safe='')
        resource = f'/organizations/{organizationId}/sm/admins/roles/{roleId}'

        return self._session.get(metadata, resource)
        


    def updateOrganizationSmAdminsRole(self, organizationId: str, roleId: str, **kwargs):
        """
        **Update a Limited Access Role**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-admins-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        - name (string): The name of the Limited Access Role
        - scope (string): The scope of the Limited Access Role
        - tags (array): The tags of the Limited Access Role
        """

        kwargs.update(locals())

        if 'scope' in kwargs:
            options = ['all_tags', 'some', 'without_all_tags', 'without_some']
            assert kwargs['scope'] in options, f'''"scope" cannot be "{kwargs['scope']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['sm', 'configure', 'admins', 'roles'],
            'operation': 'updateOrganizationSmAdminsRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        roleId = urllib.parse.quote(str(roleId), safe='')
        resource = f'/organizations/{organizationId}/sm/admins/roles/{roleId}'

        body_params = ['name', 'scope', 'tags', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationSmAdminsRole(self, organizationId: str, roleId: str):
        """
        **Delete a Limited Access Role**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'admins', 'roles'],
            'operation': 'deleteOrganizationSmAdminsRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        roleId = urllib.parse.quote(str(roleId), safe='')
        resource = f'/organizations/{organizationId}/sm/admins/roles/{roleId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationSmApnsCert(self, organizationId: str):
        """
        **Get the organization's APNS certificate**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'apnsCert'],
            'operation': 'getOrganizationSmApnsCert'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sm/apnsCert'

        return self._session.get(metadata, resource)
        


    def updateOrganizationSmSentryPoliciesAssignments(self, organizationId: str, items: list):
        """
        **Update an Organizations Sentry Policies using the provided list**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        - organizationId (string): Organization ID
        - items (array): Sentry Group Policies for the Organization keyed by Network Id
        """

        kwargs = locals()

        metadata = {
            'tags': ['sm', 'configure', 'sentry', 'policies', 'assignments'],
            'operation': 'updateOrganizationSmSentryPoliciesAssignments'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sm/sentry/policies/assignments'

        body_params = ['items', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationSmSentryPoliciesAssignmentsByNetwork(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the Sentry Policies for an organization ordered in ascending order of priority**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-sentry-policies-assignments-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter Sentry Policies by Network Id
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'sentry', 'policies', 'assignments', 'byNetwork'],
            'operation': 'getOrganizationSmSentryPoliciesAssignmentsByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sm/sentry/policies/assignments/byNetwork'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationSmVppAccounts(self, organizationId: str):
        """
        **List the VPP accounts in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'vppAccounts'],
            'operation': 'getOrganizationSmVppAccounts'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/sm/vppAccounts'

        return self._session.get(metadata, resource)
        


    def getOrganizationSmVppAccount(self, organizationId: str, vppAccountId: str):
        """
        **Get a hash containing the unparsed token of the VPP account with the given ID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account

        - organizationId (string): Organization ID
        - vppAccountId (string): Vpp account ID
        """

        metadata = {
            'tags': ['sm', 'configure', 'vppAccounts'],
            'operation': 'getOrganizationSmVppAccount'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        vppAccountId = urllib.parse.quote(str(vppAccountId), safe='')
        resource = f'/organizations/{organizationId}/sm/vppAccounts/{vppAccountId}'

        return self._session.get(metadata, resource)
        
