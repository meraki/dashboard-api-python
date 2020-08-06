class Sm(object):
    def __init__(self, session):
        super(Sm, self).__init__()
        self._session = session

    def createNetworkSmBypassActivationLockAttempt(self, networkId: str, ids: list):
        """
        **Bypass activation lock attempt**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-bypass-activation-lock-attempt

        - networkId (string): (required)
        - ids (array): The ids of the devices to attempt activation lock bypass.
        """

        kwargs = locals()

        metadata = {
            'tags': ['sm', 'configure', 'bypassActivationLockAttempts'],
            'operation': 'createNetworkSmBypassActivationLockAttempt'
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts'

        body_params = ['ids', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSmBypassActivationLockAttempt(self, networkId: str, attemptId: str):
        """
        **Bypass activation lock attempt status**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-bypass-activation-lock-attempt

        - networkId (string): (required)
        - attemptId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'bypassActivationLockAttempts'],
            'operation': 'getNetworkSmBypassActivationLockAttempt'
        }
        resource = f'/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}'

        return self._session.get(metadata, resource)

    def updateNetworkSmDevicesFields(self, networkId: str, deviceFields: dict, **kwargs):
        """
        **Modify the fields of a device**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-devices-fields

        - networkId (string): (required)
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
        resource = f'/networks/{networkId}/sm/devices/fields'

        body_params = ['wifiMac', 'id', 'serial', 'deviceFields', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def wipeNetworkSmDevices(self, networkId: str, **kwargs):
        """
        **Wipe a device**
        https://developer.cisco.com/meraki/api-v1/#!wipe-network-sm-devices

        - networkId (string): (required)
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
        resource = f'/networks/{networkId}/sm/devices/wipe'

        body_params = ['wifiMac', 'id', 'serial', 'pin', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSmDeviceCellularUsageHistory(self, networkId: str, deviceId: str):
        """
        **Return the client's daily cellular data usage history. Usage data is in kilobytes.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-cellular-usage-history

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'monitor', 'devices', 'cellularUsageHistory'],
            'operation': 'getNetworkSmDeviceCellularUsageHistory'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory'

        return self._session.get(metadata, resource)

    def getNetworkSmDeviceCerts(self, networkId: str, deviceId: str):
        """
        **List the certs on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-certs

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'certs'],
            'operation': 'getNetworkSmDeviceCerts'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/certs'

        return self._session.get(metadata, resource)

    def getNetworkSmDeviceConnectivity(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns historical connectivity data (whether a device is regularly checking in to Dashboard).**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-connectivity

        - networkId (string): (required)
        - deviceId (string): (required)
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
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/connectivity'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkSmDeviceDesktopLogs(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager network connection details for desktop devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-desktop-logs

        - networkId (string): (required)
        - deviceId (string): (required)
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
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/desktopLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkSmDeviceDeviceCommandLogs(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **    Return historical records of commands sent to Systems Manager devices.
    <p>Note that this will include the name of the Dashboard user who initiated the command if it was generated
    by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out
    of any reports.</p>
**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-command-logs

        - networkId (string): (required)
        - deviceId (string): (required)
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
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getNetworkSmDeviceDeviceProfiles(self, networkId: str, deviceId: str):
        """
        **Get the profiles associated with a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-device-profiles

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'deviceProfiles'],
            'operation': 'getNetworkSmDeviceDeviceProfiles'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/deviceProfiles'

        return self._session.get(metadata, resource)

    def getNetworkSmDeviceNetworkAdapters(self, networkId: str, deviceId: str):
        """
        **List the network adapters of a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-network-adapters

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'networkAdapters'],
            'operation': 'getNetworkSmDeviceNetworkAdapters'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/networkAdapters'

        return self._session.get(metadata, resource)

    def getNetworkSmDevicePerformanceHistory(self, networkId: str, deviceId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return historical records of various Systems Manager client metrics for desktop devices.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-performance-history

        - networkId (string): (required)
        - deviceId (string): (required)
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
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/performanceHistory'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def refreshNetworkSmDeviceDetails(self, networkId: str, deviceId: str):
        """
        **Refresh the details of a device**
        https://developer.cisco.com/meraki/api-v1/#!refresh-network-sm-device-details

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'refreshNetworkSmDeviceDetails'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/refreshDetails'

        return self._session.post(metadata, resource)

    def getNetworkSmDeviceRestrictions(self, networkId: str, deviceId: str):
        """
        **List the restrictions on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-restrictions

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'restrictions'],
            'operation': 'getNetworkSmDeviceRestrictions'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/restrictions'

        return self._session.get(metadata, resource)

    def getNetworkSmDeviceSecurityCenters(self, networkId: str, deviceId: str):
        """
        **List the security centers on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-security-centers

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'securityCenters'],
            'operation': 'getNetworkSmDeviceSecurityCenters'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/securityCenters'

        return self._session.get(metadata, resource)

    def getNetworkSmDeviceSoftwares(self, networkId: str, deviceId: str):
        """
        **Get a list of softwares associated with a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-softwares

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'softwares'],
            'operation': 'getNetworkSmDeviceSoftwares'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/softwares'

        return self._session.get(metadata, resource)

    def unenrollNetworkSmDevice(self, networkId: str, deviceId: str):
        """
        **Unenroll a device**
        https://developer.cisco.com/meraki/api-v1/#!unenroll-network-sm-device

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices'],
            'operation': 'unenrollNetworkSmDevice'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/unenroll'

        return self._session.post(metadata, resource)

    def getNetworkSmDeviceWlanLists(self, networkId: str, deviceId: str):
        """
        **List the saved SSID names on a device**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-device-wlan-lists

        - networkId (string): (required)
        - deviceId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'devices', 'wlanLists'],
            'operation': 'getNetworkSmDeviceWlanLists'
        }
        resource = f'/networks/{networkId}/sm/devices/{deviceId}/wlanLists'

        return self._session.get(metadata, resource)

    def getNetworkSmProfiles(self, networkId: str):
        """
        **List all profiles in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-profiles

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'profiles'],
            'operation': 'getNetworkSmProfiles'
        }
        resource = f'/networks/{networkId}/sm/profiles'

        return self._session.get(metadata, resource)

    def getNetworkSmTargetGroups(self, networkId: str, **kwargs):
        """
        **List the target groups in this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-groups

        - networkId (string): (required)
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'getNetworkSmTargetGroups'
        }
        resource = f'/networks/{networkId}/sm/targetGroups'

        query_params = ['withDetails', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def createNetworkSmTargetGroup(self, networkId: str, **kwargs):
        """
        **Add a target group**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-target-group

        - networkId (string): (required)
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'createNetworkSmTargetGroup'
        }
        resource = f'/networks/{networkId}/sm/targetGroups'

        body_params = ['name', 'scope', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Return a target group**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-target-group

        - networkId (string): (required)
        - targetGroupId (string): (required)
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'getNetworkSmTargetGroup'
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        query_params = ['withDetails', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def updateNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Update a target group**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-target-group

        - networkId (string): (required)
        - targetGroupId (string): (required)
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'updateNetworkSmTargetGroup'
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        body_params = ['name', 'scope', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSmTargetGroup(self, networkId: str, targetGroupId: str):
        """
        **Delete a target group from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-target-group

        - networkId (string): (required)
        - targetGroupId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'targetGroups'],
            'operation': 'deleteNetworkSmTargetGroup'
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        return self._session.delete(metadata, resource)

    def getNetworkSmUserDeviceProfiles(self, networkId: str, userId: str):
        """
        **Get the profiles associated with a user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-device-profiles

        - networkId (string): (required)
        - userId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'users', 'deviceProfiles'],
            'operation': 'getNetworkSmUserDeviceProfiles'
        }
        resource = f'/networks/{networkId}/sm/users/{userId}/deviceProfiles'

        return self._session.get(metadata, resource)

    def getNetworkSmUserSoftwares(self, networkId: str, userId: str):
        """
        **Get a list of softwares associated with a user**
        https://developer.cisco.com/meraki/api-v1/#!get-network-sm-user-softwares

        - networkId (string): (required)
        - userId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'users', 'softwares'],
            'operation': 'getNetworkSmUserSoftwares'
        }
        resource = f'/networks/{networkId}/sm/users/{userId}/softwares'

        return self._session.get(metadata, resource)

    def getOrganizationSmApnsCert(self, organizationId: str):
        """
        **Get the organization's APNS certificate**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-apns-cert

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'apnsCert'],
            'operation': 'getOrganizationSmApnsCert'
        }
        resource = f'/organizations/{organizationId}/sm/apnsCert'

        return self._session.get(metadata, resource)

    def getOrganizationSmVppAccounts(self, organizationId: str):
        """
        **List the VPP accounts in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-accounts

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'vppAccounts'],
            'operation': 'getOrganizationSmVppAccounts'
        }
        resource = f'/organizations/{organizationId}/sm/vppAccounts'

        return self._session.get(metadata, resource)

    def getOrganizationSmVppAccount(self, organizationId: str, vppAccountId: str):
        """
        **Get a hash containing the unparsed token of the VPP account with the given ID**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sm-vpp-account

        - organizationId (string): (required)
        - vppAccountId (string): (required)
        """

        metadata = {
            'tags': ['sm', 'configure', 'vppAccounts'],
            'operation': 'getOrganizationSmVppAccount'
        }
        resource = f'/organizations/{organizationId}/sm/vppAccounts/{vppAccountId}'

        return self._session.get(metadata, resource)