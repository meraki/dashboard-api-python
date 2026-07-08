import urllib


class ActionBatchSm(object):
    def __init__(self):
        super(ActionBatchSm, self).__init__()

    def createNetworkSmScript(self, networkId: str, name: str, platform: str, **kwargs):
        """
        **Create a new script**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-script

        - networkId (string): Network ID
        - name (string): Unique name to identify this script.
        - platform (string): Platform that this script will run on.
        - scope (string): The target scope of the script. (Either scope or targetGroupId must be present.)
        - tags (array): The target tags of the script as an array of strings. Required if scope is one of withAny, withoutAny, withAll, withoutAll.
        - targetGroupId (string): The tag target group ID that should be used to scope devices. Either scope or targetGroupId must be present.
        - description (string): Description of this script.
        - runAsUsername (string): Username that script should run as.
        - externalSource (object): Properties for a script provided by a url instead of an upload
        - upload (object): Properties for a script provided as an upload instead of a url
        - schedule (object): When the script is intended to run
        """

        kwargs.update(locals())

        if "platform" in kwargs and kwargs["platform"] is not None:
            options = ["Windows", "macOS"]
            assert kwargs["platform"] in options, (
                f'''"platform" cannot be "{kwargs["platform"]}", & must be set to one of: {options}'''
            )
        if "scope" in kwargs:
            options = ["all", "none", "withAll", "withAny", "withoutAll", "withoutAny"]
            assert kwargs["scope"] in options, f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''

        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/scripts"

        body_params = [
            "name",
            "platform",
            "scope",
            "tags",
            "targetGroupId",
            "description",
            "runAsUsername",
            "externalSource",
            "upload",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def createNetworkSmScriptsJob(self, networkId: str, scriptId: str, **kwargs):
        """
        **Create a job that will run a script on a set of devices**
        https://developer.cisco.com/meraki/api-v1/#!create-network-sm-scripts-job

        - networkId (string): Network ID
        - scriptId (string): ID of script that should be run on the matching devices
        - deviceIds (array): List of device IDs to run that should run this script
        - deviceFilter (string): Create job on all devices in-scope or devices that have failed to run this script
        """

        kwargs.update(locals())

        if "deviceFilter" in kwargs:
            options = ["All", "Failed"]
            assert kwargs["deviceFilter"] in options, (
                f'''"deviceFilter" cannot be "{kwargs["deviceFilter"]}", & must be set to one of: {options}'''
            )

        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/sm/scripts/jobs"

        body_params = [
            "scriptId",
            "deviceIds",
            "deviceFilter",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateNetworkSmScript(self, networkId: str, scriptId: str, **kwargs):
        """
        **Update an existing script**
        https://developer.cisco.com/meraki/api-v1/#!update-network-sm-script

        - networkId (string): Network ID
        - scriptId (string): Script ID
        - name (string): Unique name to identify this script.
        - platform (string): Platform that this script will run on.
        - scope (string): The target scope of the script. (Either scope or targetGroupId must be present.)
        - tags (array): The target tags of the script as an array of strings. Required if scope is one of withAny, withoutAny, withAll, withoutAll.
        - targetGroupId (string): The tag target group ID that should be used to scope devices. Either scope or targetGroupId must be present.
        - description (string): Description of this script.
        - runAsUsername (string): Username that script should run as.
        - externalSource (object): Properties for a script provided by a url instead of an upload
        - upload (object): Properties for a script provided as an upload instead of a url
        - schedule (object): When the script is intended to run
        """

        kwargs.update(locals())

        if "platform" in kwargs and kwargs["platform"] is not None:
            options = ["Windows", "macOS"]
            assert kwargs["platform"] in options, (
                f'''"platform" cannot be "{kwargs["platform"]}", & must be set to one of: {options}'''
            )
        if "scope" in kwargs:
            options = ["all", "none", "withAll", "withAny", "withoutAll", "withoutAny"]
            assert kwargs["scope"] in options, f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''

        networkId = urllib.parse.quote(str(networkId), safe="")
        scriptId = urllib.parse.quote(str(scriptId), safe="")
        resource = f"/networks/{networkId}/sm/scripts/{scriptId}"

        body_params = [
            "name",
            "platform",
            "scope",
            "tags",
            "targetGroupId",
            "description",
            "runAsUsername",
            "externalSource",
            "upload",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteNetworkSmScript(self, networkId: str, scriptId: str):
        """
        **Delete a script**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-script

        - networkId (string): Network ID
        - scriptId (string): Script ID
        """

        networkId = urllib.parse.quote(str(networkId), safe="")
        scriptId = urllib.parse.quote(str(scriptId), safe="")
        resource = f"/networks/{networkId}/sm/scripts/{scriptId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def deleteNetworkSmUserAccessDevice(self, networkId: str, userAccessDeviceId: str):
        """
        **Delete a User Access Device**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-sm-user-access-device

        - networkId (string): Network ID
        - userAccessDeviceId (string): User access device ID
        """

        networkId = urllib.parse.quote(str(networkId), safe="")
        userAccessDeviceId = urllib.parse.quote(str(userAccessDeviceId), safe="")
        resource = f"/networks/{networkId}/sm/userAccessDevices/{userAccessDeviceId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

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

        if "scope" in kwargs:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert kwargs["scope"] in options, f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

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

        if "scope" in kwargs:
            options = ["all_tags", "some", "without_all_tags", "without_some"]
            assert kwargs["scope"] in options, f'''"scope" cannot be "{kwargs["scope"]}", & must be set to one of: {options}'''

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        roleId = urllib.parse.quote(str(roleId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        body_params = [
            "name",
            "scope",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSmAdminsRole(self, organizationId: str, roleId: str):
        """
        **Delete a Limited Access Role**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-admins-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        """

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        roleId = urllib.parse.quote(str(roleId), safe="")
        resource = f"/organizations/{organizationId}/sm/admins/roles/{roleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationSmAppleCloudEnrollmentSyncJob(self, organizationId: str, **kwargs):
        """
        **Enqueue a sync job for an ADE account**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-apple-cloud-enrollment-sync-job

        - organizationId (string): Organization ID
        - adeAccountId (string): ADE Account ID
        - fullSync (boolean): Whether or not job is full sync (defaults to full sync)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/apple/cloudEnrollment/syncJobs"

        body_params = [
            "adeAccountId",
            "fullSync",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def createOrganizationSmBulkEnrollmentToken(self, organizationId: str, networkId: str, expiresAt: str, **kwargs):
        """
        **Create a PccBulkEnrollmentToken**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-sm-bulk-enrollment-token

        - organizationId (string): Organization ID
        - networkId (string): The id of the associated node_group.
        - expiresAt (string): The expiration date.
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/bulkEnrollment/token"

        body_params = [
            "networkId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationSmBulkEnrollmentToken(self, organizationId: str, tokenId: str, **kwargs):
        """
        **Update a PccBulkEnrollmentToken**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-bulk-enrollment-token

        - organizationId (string): Organization ID
        - tokenId (string): Token ID
        - networkId (string): The id of the associated node_group.
        - expiresAt (string): The expiration date.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        tokenId = urllib.parse.quote(str(tokenId), safe="")
        resource = f"/organizations/{organizationId}/sm/bulkEnrollment/token/{tokenId}"

        body_params = [
            "networkId",
            "expiresAt",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSmBulkEnrollmentToken(self, organizationId: str, tokenId: str):
        """
        **Delete a PccBulkEnrollmentToken**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sm-bulk-enrollment-token

        - organizationId (string): Organization ID
        - tokenId (string): Token ID
        """

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        tokenId = urllib.parse.quote(str(tokenId), safe="")
        resource = f"/organizations/{organizationId}/sm/bulkEnrollment/token/{tokenId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationSmSentryPoliciesAssignments(self, organizationId: str, items: list, **kwargs):
        """
        **Update an Organizations Sentry Policies using the provided list. Sentry Policies are ordered in descending order of priority (i.e. highest priority at the bottom, this is opposite the Dashboard UI). Policies not present in the request will be deleted.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sm-sentry-policies-assignments

        - organizationId (string): Organization ID
        - items (array): Sentry Group Policies for the Organization keyed by Network Id
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/sm/sentry/policies/assignments"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action
