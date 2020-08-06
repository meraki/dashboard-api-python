class AsyncSM:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def createNetworkSmBypassActivationLockAttempt(self, networkId: str, ids: list):
        """
        **Bypass activation lock attempt**
        https://developer.cisco.com/meraki/api/#!create-network-sm-bypass-activation-lock-attempt
        
        - networkId (string)
        - ids (array): The ids of the devices to attempt activation lock bypass.
        """

        kwargs = locals()

        metadata = {
            'tags': ['SM'],
            'operation': 'createNetworkSmBypassActivationLockAttempt',
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts'

        body_params = ['ids']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkSmBypassActivationLockAttempt(self, networkId: str, attemptId: str):
        """
        **Bypass activation lock attempt status**
        https://developer.cisco.com/meraki/api/#!get-network-sm-bypass-activation-lock-attempt
        
        - networkId (string)
        - attemptId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmBypassActivationLockAttempt',
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}'

        return await self._session.get(metadata, resource)

    async def updateNetworkSmDeviceFields(self, networkId: str, deviceFields: dict, **kwargs):
        """
        **Modify the fields of a device**
        https://developer.cisco.com/meraki/api/#!update-network-sm-device-fields
        
        - networkId (string)
        - deviceFields (object): The new fields of the device. Each field of this object is optional.
        - wifiMac (string): The wifiMac of the device to be modified.
        - id (string): The id of the device to be modified.
        - serial (string): The serial of the device to be modified.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'updateNetworkSmDeviceFields',
        }
        resource = f'/networks/{networkId}/sm/device/fields'

        body_params = ['wifiMac', 'id', 'serial', 'deviceFields']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def wipeNetworkSmDevice(self, networkId: str, **kwargs):
        """
        **Wipe a device**
        https://developer.cisco.com/meraki/api/#!wipe-network-sm-device
        
        - networkId (string)
        - wifiMac (string): The wifiMac of the device to be wiped.
        - id (string): The id of the device to be wiped.
        - serial (string): The serial of the device to be wiped.
        - pin (integer): The pin number (a six digit value) for wiping a macOS device. Required only for macOS devices.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'wipeNetworkSmDevice',
        }
        resource = f'/networks/{networkId}/sm/device/wipe'

        body_params = ['wifiMac', 'id', 'serial', 'pin']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def refreshNetworkSmDeviceDetails(self, networkId: str, deviceId: str):
        """
        **Refresh the details of a device**
        https://developer.cisco.com/meraki/api/#!refresh-network-sm-device-details
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'refreshNetworkSmDeviceDetails',
        }
        resource = f'/networks/{networkId}/sm/device/{deviceId}/refreshDetails'

        return await self._session.post(metadata, resource)

    async def getNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **List the devices enrolled in an SM network with various specified fields and filters**
        https://developer.cisco.com/meraki/api/#!get-network-sm-devices
        
        - networkId (string)
        - fields (string): Additional fields that will be displayed for each device. Multiple fields can be passed in as comma separated values.
    The default fields are: id, name, tags, ssid, wifiMac, osName, systemModel, uuid, and serialNumber. The additional fields are: ip,
    systemType, availableDeviceCapacity, kioskAppName, biosVersion, lastConnected, missingAppsCount, userSuppliedAddress, location, lastUser,
    ownerEmail, ownerUsername, publicIp, phoneNumber, diskInfoJson, deviceCapacity, isManaged, hadMdm, isSupervised, meid, imei, iccid,
    simCarrierNetwork, cellularDataUsed, isHotspotEnabled, createdAt, batteryEstCharge, quarantined, avName, avRunning, asName, fwName,
    isRooted, loginRequired, screenLockEnabled, screenLockDelay, autoLoginDisabled, autoTags, hasMdm, hasDesktopAgent, diskEncryptionEnabled,
    hardwareEncryptionCaps, passCodeLock, usesHardwareKeystore, and androidSecurityPatchVersion.
        - wifiMacs (string): Filter devices by wifi mac(s). Multiple wifi macs can be passed in as comma separated values.
        - serials (string): Filter devices by serial(s). Multiple serials can be passed in as comma separated values.
        - ids (string): Filter devices by id(s). Multiple ids can be passed in as comma separated values.
        - scope (string): Specify a scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags as comma separated values.
        - batchSize (integer): Number of devices to return, 1000 is the default as well as the max.
        - batchToken (string): If the network has more devices than the batch size, a batch token will be returned
    as a part of the device list. To see the remainder of the devices, pass in the batchToken as a parameter in the next request.
    Requests made with the batchToken do not require additional parameters as the batchToken includes the parameters passed in
    with the original request. Additional parameters passed in with the batchToken will be ignored.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices'

        query_params = ['fields', 'wifiMacs', 'serials', 'ids', 'scope', 'batchSize', 'batchToken']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def checkinNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Force check-in a set of devices**
        https://developer.cisco.com/meraki/api/#!checkin-network-sm-devices
        
        - networkId (string)
        - wifiMacs (string): The wifiMacs of the devices to be checked-in.
        - ids (string): The ids of the devices to be checked-in.
        - serials (string): The serials of the devices to be checked-in.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be checked-in.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'checkinNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices/checkin'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def moveNetworkSmDevices(self, networkId: str, newNetwork: str, **kwargs):
        """
        **Move a set of devices to a new network**
        https://developer.cisco.com/meraki/api/#!move-network-sm-devices
        
        - networkId (string)
        - newNetwork (string): The new network to which the devices will be moved.
        - wifiMacs (string): The wifiMacs of the devices to be moved.
        - ids (string): The ids of the devices to be moved.
        - serials (string): The serials of the devices to be moved.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be moved.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'moveNetworkSmDevices',
        }
        resource = f'/networks/{networkId}/sm/devices/move'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'newNetwork']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def updateNetworkSmDevicesTags(self, networkId: str, tags: str, updateAction: str, **kwargs):
        """
        **Add, delete, or update the tags of a set of devices**
        https://developer.cisco.com/meraki/api/#!update-network-sm-devices-tags
        
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
            'tags': ['SM'],
            'operation': 'updateNetworkSmDevicesTags',
        }
        resource = f'/networks/{networkId}/sm/devices/tags'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'tags', 'updateAction']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def unenrollNetworkSmDevice(self, networkId: str, deviceId: str):
        """
        **Unenroll a device**
        https://developer.cisco.com/meraki/api/#!unenroll-network-sm-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'unenrollNetworkSmDevice',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/unenroll'

        return await self._session.post(metadata, resource)

    async def getNetworkSmProfiles(self, networkId: str):
        """
        **List all the profiles in the network**
        https://developer.cisco.com/meraki/api/#!get-network-sm-profiles
        
        - networkId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmProfiles',
        }
        resource = f'/networks/{networkId}/sm/profiles'

        return await self._session.get(metadata, resource)

    async def getNetworkSmUserDeviceProfiles(self, networkId: str, userId: str):
        """
        **Get the profiles associated with a user**
        https://developer.cisco.com/meraki/api/#!get-network-sm-user-device-profiles
        
        - networkId (string)
        - userId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmUserDeviceProfiles',
        }
        resource = f'/networks/{networkId}/sm/user/{userId}/deviceProfiles'

        return await self._session.get(metadata, resource)

    async def getNetworkSmUserSoftwares(self, networkId: str, userId: str):
        """
        **Get a list of softwares associated with a user**
        https://developer.cisco.com/meraki/api/#!get-network-sm-user-softwares
        
        - networkId (string)
        - userId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmUserSoftwares',
        }
        resource = f'/networks/{networkId}/sm/user/{userId}/softwares'

        return await self._session.get(metadata, resource)

    async def getNetworkSmUsers(self, networkId: str, **kwargs):
        """
        **List the owners in an SM network with various specified fields and filters**
        https://developer.cisco.com/meraki/api/#!get-network-sm-users
        
        - networkId (string)
        - ids (string): Filter users by id(s). Multiple ids can be passed in as comma separated values.
        - usernames (string): Filter users by username(s). Multiple usernames can be passed in as comma separated values.
        - emails (string): Filter users by email(s). Multiple emails can be passed in as comma separated values.
        - scope (string): Specifiy a scope (one of all, none, withAny, withAll, withoutAny, withoutAll) and a set of tags as comma separated values.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmUsers',
        }
        resource = f'/networks/{networkId}/sm/users'

        query_params = ['ids', 'usernames', 'emails', 'scope']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getNetworkSmCellularUsageHistory(self, networkId: str, deviceId: str):
        """
        **Return the client's daily cellular data usage history. Usage data is in kilobytes.**
        https://developer.cisco.com/meraki/api/#!get-network-sm-cellular-usage-history
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmCellularUsageHistory',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/cellularUsageHistory'

        return await self._session.get(metadata, resource)

    async def getNetworkSmCerts(self, networkId: str, deviceId: str):
        """
        **List the certs on a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-certs
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmCerts',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/certs'

        return await self._session.get(metadata, resource)

    async def getNetworkSmDeviceProfiles(self, networkId: str, deviceId: str):
        """
        **Get the profiles associated with a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-device-profiles
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmDeviceProfiles',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/deviceProfiles'

        return await self._session.get(metadata, resource)

    async def getNetworkSmNetworkAdapters(self, networkId: str, deviceId: str):
        """
        **List the network adapters of a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-network-adapters
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmNetworkAdapters',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/networkAdapters'

        return await self._session.get(metadata, resource)

    async def getNetworkSmRestrictions(self, networkId: str, deviceId: str):
        """
        **List the restrictions on a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-restrictions
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmRestrictions',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/restrictions'

        return await self._session.get(metadata, resource)

    async def getNetworkSmSecurityCenters(self, networkId: str, deviceId: str):
        """
        **List the security centers on a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-security-centers
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmSecurityCenters',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/securityCenters'

        return await self._session.get(metadata, resource)

    async def getNetworkSmSoftwares(self, networkId: str, deviceId: str):
        """
        **Get a list of softwares associated with a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-softwares
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmSoftwares',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/softwares'

        return await self._session.get(metadata, resource)

    async def getNetworkSmWlanLists(self, networkId: str, deviceId: str):
        """
        **List the saved SSID names on a device**
        https://developer.cisco.com/meraki/api/#!get-network-sm-wlan-lists
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmWlanLists',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/wlanLists'

        return await self._session.get(metadata, resource)

    async def lockNetworkSmDevices(self, network_id: str, **kwargs):
        """
        **Lock a set of devices**
        https://developer.cisco.com/meraki/api/#!lock-network-sm-devices
        
        - network_id (string)
        - wifiMacs (string): The wifiMacs of the devices to be locked.
        - ids (string): The ids of the devices to be locked.
        - serials (string): The serials of the devices to be locked.
        - scope (string): The scope (one of all, none, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be wiped.
        - pin (integer): The pin number for locking macOS devices (a six digit number). Required only for macOS devices.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'lockNetworkSmDevices',
        }
        resource = f'/networks/{network_id}/sm/devices/lock'

        body_params = ['wifiMacs', 'ids', 'serials', 'scope', 'pin']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkSmConnectivity(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**
        https://developer.cisco.com/meraki/api/#!get-network-sm-connectivity
        
        - network_id (string)
        - id (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmConnectivity',
        }
        resource = f'/networks/{network_id}/sm/{id}/connectivity'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkSmDesktopLogs(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager network connection details for desktop devices.**
        https://developer.cisco.com/meraki/api/#!get-network-sm-desktop-logs
        
        - network_id (string)
        - id (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmDesktopLogs',
        }
        resource = f'/networks/{network_id}/sm/{id}/desktopLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkSmDeviceCommandLogs(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **    Return historical records of commands sent to Systems Manager devices.
    <p>Note that this will include the name of the Dashboard user who initiated the command if it was generated
    by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out
    of any reports.</p>
**
        https://developer.cisco.com/meraki/api/#!get-network-sm-device-command-logs
        
        - network_id (string)
        - id (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmDeviceCommandLogs',
        }
        resource = f'/networks/{network_id}/sm/{id}/deviceCommandLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getNetworkSmPerformanceHistory(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager client metrics for desktop devices.**
        https://developer.cisco.com/meraki/api/#!get-network-sm-performance-history
        
        - network_id (string)
        - id (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmPerformanceHistory',
        }
        resource = f'/networks/{network_id}/sm/{id}/performanceHistory'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


