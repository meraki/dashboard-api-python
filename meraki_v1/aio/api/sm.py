class AsyncSm:
    def __init__(self, session):
        super().__init__()
        self._session = session

    async def createNetworkSmBypassActivationLockAttempt(self, networkId: str, ids: list):
        """
        **Bypass activation lock attempt**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt
        
        - networkId (string)
        - ids (array): The ids of the devices to attempt activation lock bypass.
        """

        kwargs = locals()

        metadata = {
            'tags': ['sm', 'configure', 'bypassActivationLockAttempts'],
            'operation': 'createNetworkSmBypassActivationLockAttempt',
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts'

        body_params = ['ids']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkSmBypassActivationLockAttempt(self, networkId: str, attemptId: str):
        """
        **Bypass activation lock attempt status**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt
        
        - networkId (string)
        - attemptId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'bypassActivationLockAttempts'],
            'operation': 'getNetworkSmBypassActivationLockAttempt',
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDevices(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the devices enrolled in an SM network with various specified fields and filters**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-devices
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - fields (string): Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.
    The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
    systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
    ownerEmail, ownerUsername, osBuild, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
    simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
    isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
    hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion.
        - wifiMacs (string): Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values.
        - serials (string): Filter devices by serial(s). Multiple serials can be passed in as comma separated values.
        - ids (string): Filter devices by id(s). Multiple ids can be passed in as comma separated values.
        - scope (string): Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'getNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices'

        query_params = ['fields', 'wifiMacs', 'serials', 'ids', 'scope', 'perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def checkinNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Force check-in a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!checkin-network-sm-devices
        
        - networkId (string)
        - wifiMacs (string): The wifiMacs of the devices to be checked-in.
        - ids (string): The ids of the devices to be checked-in.
        - serials (string): The serials of the devices to be checked-in.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be checked-in.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'checkinNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices/checkin'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def updateNetworkSmDevicesFields(self, networkId: str, deviceFields: dict, **kwargs):
        """
        **Modify the fields of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields
        
        - networkId (string)
        - deviceFields (object): The new fields of the device. Each field of this object is optional.
        - wifiMac (string): The wifiMac of the device to be modified.
        - id (string): The id of the device to be modified.
        - serial (string): The serial of the device to be modified.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'fields'],
            'operation': 'updateNetworkSmDevicesFields',
        }
        resource = f'/networks/{networkId}/sm/devices/fields'

        body_params = ['wifiMac', 'id', 'serial', 'deviceFields']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def lockNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Lock a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!lock-network-sm-devices
        
        - networkId (string)
        - wifiMacs (string): The wifiMacs of the devices to be locked.
        - ids (string): The ids of the devices to be locked.
        - serials (string): The serials of the devices to be locked.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped.
        - pin (integer): The pin number for locking macOS devices (a six digit number). Required only for macOS devices.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'lockNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices/lock'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'pin']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def modifyNetworkSmDevicesTags(self, networkId: str, tags: str, updateAction: str, **kwargs):
        """
        **Add, delete, or update the tags of a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!modify-network-sm-devices-tags
        
        - networkId (string)
        - tags (string): The tags to be added, deleted, or updated.
        - updateAction (string): One of add, delete, or update. Only devices that have been modified will be returned.
        - wifiMacs (string): The wifiMacs of the devices to be modified.
        - ids (string): The ids of the devices to be modified.
        - serials (string): The serials of the devices to be modified.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be modified.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'modifyNetworkSmDevicesTags',
        }
        resource = f'/networks/{networkId}/sm/devices/modifyTags'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'tags', 'updateAction']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def moveNetworkSmDevices(self, networkId: str, newNetwork: str, **kwargs):
        """
        **Move a set of devices to a new network**
        https://developer.cisco.com/meraki/api-v1/#!move-network-sm-devices
        
        - networkId (string)
        - newNetwork (string): The new network to which the devices will be moved.
        - wifiMacs (string): The wifiMacs of the devices to be moved.
        - ids (string): The ids of the devices to be moved.
        - serials (string): The serials of the devices to be moved.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be moved.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'moveNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices/move'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'newNetwork']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def wipeNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Wipe a device**
        https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices
        
        - networkId (string)
        - wifiMac (string): The wifiMac of the device to be wiped.
        - id (string): The id of the device to be wiped.
        - serial (string): The serial of the device to be wiped.
        - pin (integer): The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'wipeNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices/wipe'

        body_params = ['wifiMac', 'id', 'serial', 'pin']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkSmDeviceCellularUsageHistory(self, networkId: str, deviceId: str):
        """
        **Return the client's daily cellular data usage history. Usage data is in kilobytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'cellularUsageHistory'],
            'operation': 'getNetworkSmDeviceCellularUsageHistory',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDeviceCerts(self, networkId: str, deviceId: str):
        """
        **List the certs on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'certs'],
            'operation': 'getNetworkSmDeviceCerts',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/certs'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDeviceConnectivity(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity
        
        - networkId (string)
        - deviceId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'connectivity'],
            'operation': 'getNetworkSmDeviceConnectivity',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/connectivity'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkSmDeviceDesktopLogs(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager network connection details for desktop devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs
        
        - networkId (string)
        - deviceId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'desktopLogs'],
            'operation': 'getNetworkSmDeviceDesktopLogs',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/desktopLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkSmDeviceDeviceCommandLogs(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **    Return historical records of commands sent to Systems Manager devices.
    <p>Note that this will include the name of the Dashboard user who initiated the command if it was generated
    by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out
    of any reports.</p>
**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs
        
        - networkId (string)
        - deviceId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'deviceCommandLogs'],
            'operation': 'getNetworkSmDeviceDeviceCommandLogs',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkSmDeviceDeviceProfiles(self, networkId: str, deviceId: str):
        """
        **Get the profiles associated with a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'deviceProfiles'],
            'operation': 'getNetworkSmDeviceDeviceProfiles',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/deviceProfiles'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDeviceNetworkAdapters(self, networkId: str, deviceId: str):
        """
        **List the network adapters of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'networkAdapters'],
            'operation': 'getNetworkSmDeviceNetworkAdapters',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/networkAdapters'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDevicePerformanceHistory(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager client metrics for desktop devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history
        
        - networkId (string)
        - deviceId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'performanceHistory'],
            'operation': 'getNetworkSmDevicePerformanceHistory',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/performanceHistory'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def refreshNetworkSmDeviceDetails(self, networkId: str, deviceId: str):
        """
        **Refresh the details of a device**
        https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'refreshNetworkSmDeviceDetails',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/refreshDetails'

        return await self._session.post(metadata, resource)

    async def getNetworkSmDeviceRestrictions(self, networkId: str, deviceId: str):
        """
        **List the restrictions on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'restrictions'],
            'operation': 'getNetworkSmDeviceRestrictions',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/restrictions'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDeviceSecurityCenters(self, networkId: str, deviceId: str):
        """
        **List the security centers on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'securityCenters'],
            'operation': 'getNetworkSmDeviceSecurityCenters',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/securityCenters'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDeviceSoftwares(self, networkId: str, deviceId: str):
        """
        **Get a list of softwares associated with a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'softwares'],
            'operation': 'getNetworkSmDeviceSoftwares',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/softwares'

        return await self._session.get(metadata, resource)

    async def unenrollNetworkSmDevice(self, networkId: str, deviceId: str):
        """
        **Unenroll a device**
        https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'unenrollNetworkSmDevice',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/unenroll'

        return await self._session.post(metadata, resource)

    async def getNetworkSmDeviceWlanLists(self, networkId: str, deviceId: str):
        """
        **List the saved SSID names on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'wlanLists'],
            'operation': 'getNetworkSmDeviceWlanLists',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/wlanLists'

        return await self._session.get(metadata, resource)

    async def getNetworkSmProfiles(self, networkId: str):
        """
        **List all profiles in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles
        
        - networkId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'profiles'],
            'operation': 'getNetworkSmProfiles',
        }
        resource = f'/networks/{networkId}/sm/profiles'

        return await self._session.get(metadata, resource)

    async def getNetworkSmTargetGroups(self, networkId: str, **kwargs):
        """
        **List the target groups in this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups
        
        - networkId (string)
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'getNetworkSmTargetGroups',
        }
        resource = f'/networks/{networkId}/sm/targetGroups'

        query_params = ['withDetails']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def createNetworkSmTargetGroup(self, networkId: str, **kwargs):
        """
        **Add a target group**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group
        
        - networkId (string)
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'createNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups'

        body_params = ['name', 'scope']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Return a target group**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group
        
        - networkId (string)
        - targetGroupId (string)
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'getNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        query_params = ['withDetails']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def updateNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Update a target group**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group
        
        - networkId (string)
        - targetGroupId (string)
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'updateNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        body_params = ['name', 'scope']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteNetworkSmTargetGroup(self, networkId: str, targetGroupId: str):
        """
        **Delete a target group from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group
        
        - networkId (string)
        - targetGroupId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'deleteNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        return await self._session.delete(metadata, resource)

    async def getNetworkSmUsers(self, networkId: str, **kwargs):
        """
        **List the owners in an SM network with various specified fields and filters**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-users
        
        - networkId (string)
        - ids (string): Filter users by id(s). Multiple ids can be passed in as comma separated values.
        - usernames (string): Filter users by username(s). Multiple usernames can be passed in as comma separated values.
        - emails (string): Filter users by email(s). Multiple emails can be passed in as comma separated values.
        - scope (string): Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'users'],
            'operation': 'getNetworkSmUsers',
        }
        resource = f'/networks/{networkId}/sm/users'

        query_params = ['ids', 'usernames', 'emails', 'scope']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkSmUserDeviceProfiles(self, networkId: str, userId: str):
        """
        **Get the profiles associated with a user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles
        
        - networkId (string)
        - userId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'users', 'deviceProfiles'],
            'operation': 'getNetworkSmUserDeviceProfiles',
        }
        resource = f'/networks/{networkId}/sm/users/{userId}/deviceProfiles'

        return await self._session.get(metadata, resource)

    async def getNetworkSmUserSoftwares(self, networkId: str, userId: str):
        """
        **Get a list of softwares associated with a user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares
        
        - networkId (string)
        - userId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'users', 'softwares'],
            'operation': 'getNetworkSmUserSoftwares',
        }
        resource = f'/networks/{networkId}/sm/users/{userId}/softwares'

        return await self._session.get(metadata, resource)

    async def getOrganizationSmApnsCert(self, organizationId: str):
        """
        **Get the organization's APNS certificate**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'apnsCert'],
            'operation': 'getOrganizationSmApnsCert',
        }
        resource = f'/organizations/{organizationId}/sm/apnsCert'

        return await self._session.get(metadata, resource)

    async def getOrganizationSmVppAccounts(self, organizationId: str):
        """
        **List the VPP accounts in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'vppAccounts'],
            'operation': 'getOrganizationSmVppAccounts',
        }
        resource = f'/organizations/{organizationId}/sm/vppAccounts'

        return await self._session.get(metadata, resource)

    async def getOrganizationSmVppAccount(self, organizationId: str, vppAccountId: str):
        """
        **Get a hash containing the unparsed token of the VPP account with the given ID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account
        
        - organizationId (string)
        - vppAccountId (string)
        """

        metadata = {
            'tags': ['sm', 'configure', 'vppAccounts'],
            'operation': 'getOrganizationSmVppAccount',
        }
        resource = f'/organizations/{organizationId}/sm/vppAccounts/{vppAccountId}'

        return await self._session.get(metadata, resource)

