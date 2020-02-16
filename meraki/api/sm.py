class SM(object):
    def __init__(self, session):
        super(SM, self).__init__()
        self._session = session
    
    def createNetworkSmAppPolaris(self, networkId: str, scope: str, **kwargs):
        """
        **Create a new Polaris app**
        https://api.meraki.com/api_docs#create-a-new-polaris-app
        
        - networkId (string)
        - scope (string): The scope (one of all, none, automatic, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be assigned
        - manifestUrl (string): The manifest URL of the Polaris app (one of manifestUrl and bundleId must be provided)
        - bundleId (string): The bundleId of the Polaris app (one of manifestUrl and bundleId must be provided)
        - preventAutoInstall (boolean): (optional) Whether or not SM should auto-install this app (one of true or false). False by default.
        - usesVPP (boolean): (optional) Whether or not the app should use VPP by device assignment (one of true or false). False by default.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'createNetworkSmAppPolaris',
        }
        resource = f'/networks/{networkId}/sm/app/polaris'

        body_params = ['scope', 'manifestUrl', 'bundleId', 'preventAutoInstall', 'usesVPP']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSmAppPolaris(self, networkId: str, **kwargs):
        """
        **Get details for a Cisco Polaris app if it exists**
        https://api.meraki.com/api_docs#get-details-for-a-cisco-polaris-app-if-it-exists
        
        - networkId (string)
        - bundleId (string): The bundle ID of the app to be found, defaults to com.cisco.ciscosecurity.app
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmAppPolaris',
        }
        resource = f'/networks/{networkId}/sm/app/polaris'

        query_params = ['bundleId']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def updateNetworkSmAppPolaris(self, networkId: str, appId: str, **kwargs):
        """
        **Update an existing Polaris app**
        https://api.meraki.com/api_docs#update-an-existing-polaris-app
        
        - networkId (string)
        - appId (string)
        - scope (string): optional: The scope (one of all, none, automatic, withAny, withAll, withoutAny, or withoutAll) and a set of tags of the devices to be assigned
        - preventAutoInstall (boolean): optional: Whether or not SM should auto-install this app (one of true or false)
        - usesVPP (boolean): optional: Whether or not the app should use VPP by device assignment (one of true or false)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['SM'],
            'operation': 'updateNetworkSmAppPolaris',
        }
        resource = f'/networks/{networkId}/sm/app/polaris/{appId}'

        body_params = ['scope', 'preventAutoInstall', 'usesVPP']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSmAppPolaris(self, networkId: str, appId: str):
        """
        **Delete a Cisco Polaris app**
        https://api.meraki.com/api_docs#delete-a-cisco-polaris-app
        
        - networkId (string)
        - appId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'deleteNetworkSmAppPolaris',
        }
        resource = f'/networks/{networkId}/sm/app/polaris/{appId}'

        return self._session.delete(metadata, resource)

    def createNetworkSmBypassActivationLockAttempt(self, networkId: str, ids: list):
        """
        **Bypass activation lock attempt**
        https://api.meraki.com/api_docs#bypass-activation-lock-attempt
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSmBypassActivationLockAttempt(self, networkId: str, attemptId: str):
        """
        **Bypass activation lock attempt status**
        https://api.meraki.com/api_docs#bypass-activation-lock-attempt-status
        
        - networkId (string)
        - attemptId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmBypassActivationLockAttempt',
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}'

        return self._session.get(metadata, resource)

    def updateNetworkSmDeviceFields(self, networkId: str, deviceFields: dict, **kwargs):
        """
        **Modify the fields of a device**
        https://api.meraki.com/api_docs#modify-the-fields-of-a-device
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def wipeNetworkSmDevice(self, networkId: str, **kwargs):
        """
        **Wipe a device**
        https://api.meraki.com/api_docs#wipe-a-device
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def refreshNetworkSmDeviceDetails(self, networkId: str, deviceId: str):
        """
        **Refresh the details of a device**
        https://api.meraki.com/api_docs#refresh-the-details-of-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'refreshNetworkSmDeviceDetails',
        }
        resource = f'/networks/{networkId}/sm/device/{deviceId}/refreshDetails'

        return self._session.post(metadata, resource)

    def getNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **List the devices enrolled in an SM network with various specified fields and filters**
        https://api.meraki.com/api_docs#list-the-devices-enrolled-in-an-sm-network-with-various-specified-fields-and-filters
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def checkinNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Force check-in a set of devices**
        https://api.meraki.com/api_docs#force-check-in-a-set-of-devices
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def moveNetworkSmDevices(self, networkId: str, newNetwork: str, **kwargs):
        """
        **Move a set of devices to a new network**
        https://api.meraki.com/api_docs#move-a-set-of-devices-to-a-new-network
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def updateNetworkSmDevicesTags(self, networkId: str, tags: str, updateAction: str, **kwargs):
        """
        **Add, delete, or update the tags of a set of devices**
        https://api.meraki.com/api_docs#add-delete-or-update-the-tags-of-a-set-of-devices
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def unenrollNetworkSmDevice(self, networkId: str, deviceId: str):
        """
        **Unenroll a device**
        https://api.meraki.com/api_docs#unenroll-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'unenrollNetworkSmDevice',
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/unenroll'

        return self._session.post(metadata, resource)

    def getNetworkSmProfiles(self, networkId: str):
        """
        **List all the profiles in the network**
        https://api.meraki.com/api_docs#list-all-the-profiles-in-the-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmProfiles',
        }
        resource = f'/networks/{networkId}/sm/profiles'

        return self._session.get(metadata, resource)

    def getNetworkSmUserDeviceProfiles(self, networkId: str, userId: str):
        """
        **Get the profiles associated with a user**
        https://api.meraki.com/api_docs#get-the-profiles-associated-with-a-user
        
        - networkId (string)
        - userId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmUserDeviceProfiles',
        }
        resource = f'/networks/{networkId}/sm/user/{userId}/deviceProfiles'

        return self._session.get(metadata, resource)

    def getNetworkSmUserSoftwares(self, networkId: str, userId: str):
        """
        **Get a list of softwares associated with a user**
        https://api.meraki.com/api_docs#get-a-list-of-softwares-associated-with-a-user
        
        - networkId (string)
        - userId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmUserSoftwares',
        }
        resource = f'/networks/{networkId}/sm/user/{userId}/softwares'

        return self._session.get(metadata, resource)

    def getNetworkSmUsers(self, networkId: str, **kwargs):
        """
        **List the owners in an SM network with various specified fields and filters**
        https://api.meraki.com/api_docs#list-the-owners-in-an-sm-network-with-various-specified-fields-and-filters
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkSmCellularUsageHistory(self, networkId: str, deviceId: str):
        """
        **Return the client's daily cellular data usage history. Usage data is in kilobytes.**
        https://api.meraki.com/api_docs#return-the-clients-daily-cellular-data-usage-history
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmCellularUsageHistory',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/cellularUsageHistory'

        return self._session.get(metadata, resource)

    def getNetworkSmCerts(self, networkId: str, deviceId: str):
        """
        **List the certs on a device**
        https://api.meraki.com/api_docs#list-the-certs-on-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmCerts',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/certs'

        return self._session.get(metadata, resource)

    def getNetworkSmDeviceProfiles(self, networkId: str, deviceId: str):
        """
        **Get the profiles associated with a device**
        https://api.meraki.com/api_docs#get-the-profiles-associated-with-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmDeviceProfiles',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/deviceProfiles'

        return self._session.get(metadata, resource)

    def getNetworkSmNetworkAdapters(self, networkId: str, deviceId: str):
        """
        **List the network adapters of a device**
        https://api.meraki.com/api_docs#list-the-network-adapters-of-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmNetworkAdapters',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/networkAdapters'

        return self._session.get(metadata, resource)

    def getNetworkSmRestrictions(self, networkId: str, deviceId: str):
        """
        **List the restrictions on a device**
        https://api.meraki.com/api_docs#list-the-restrictions-on-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmRestrictions',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/restrictions'

        return self._session.get(metadata, resource)

    def getNetworkSmSecurityCenters(self, networkId: str, deviceId: str):
        """
        **List the security centers on a device**
        https://api.meraki.com/api_docs#list-the-security-centers-on-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmSecurityCenters',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/securityCenters'

        return self._session.get(metadata, resource)

    def getNetworkSmSoftwares(self, networkId: str, deviceId: str):
        """
        **Get a list of softwares associated with a device**
        https://api.meraki.com/api_docs#get-a-list-of-softwares-associated-with-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmSoftwares',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/softwares'

        return self._session.get(metadata, resource)

    def getNetworkSmWlanLists(self, networkId: str, deviceId: str):
        """
        **List the saved SSID names on a device**
        https://api.meraki.com/api_docs#list-the-saved-ssid-names-on-a-device
        
        - networkId (string)
        - deviceId (string)
        """

        metadata = {
            'tags': ['SM'],
            'operation': 'getNetworkSmWlanLists',
        }
        resource = f'/networks/{networkId}/sm/{deviceId}/wlanLists'

        return self._session.get(metadata, resource)

    def lockNetworkSmDevices(self, network_id: str, **kwargs):
        """
        **Lock a set of devices**
        https://api.meraki.com/api_docs#lock-a-set-of-devices
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkSmConnectivity(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**
        https://api.meraki.com/api_docs#returns-historical-connectivity-data-whether-a-device-is-regularly-checking-in-to-dashboard
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkSmDesktopLogs(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager network connection details for desktop devices.**
        https://api.meraki.com/api_docs#return-historical-records-of-various-systems-manager-network-connection-details-for-desktop-devices
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkSmDeviceCommandLogs(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **    Return historical records of commands sent to Systems Manager devices.
    <p>Note that this will include the name of the Dashboard user who initiated the command if it was generated
    by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out
    of any reports.</p>
**
        https://api.meraki.com/api_docs#----return-historical-records-of-commands-sent-to-systems-manager-devices
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkSmPerformanceHistory(self, network_id: str, id: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager client metrics for desktop devices.**
        https://api.meraki.com/api_docs#return-historical-records-of-various-systems-manager-client-metrics-for-desktop-devices
        
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


