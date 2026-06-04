import urllib


class ActionBatchOrganizations(object):
    def __init__(self):
        super(ActionBatchOrganizations, self).__init__()

    def createOrganizationAdaptivePolicyAcl(self, organizationId: str, name: str, rules: list, ipVersion: str, **kwargs):
        """
        **Creates new adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - name (string): Name of the adaptive policy ACL
        - rules (array): An ordered array of the adaptive policy ACL rules.
        - ipVersion (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
        - description (string): Description of the adaptive policy ACL
        """

        kwargs.update(locals())

        if "ipVersion" in kwargs:
            options = ["any", "ipv4", "ipv6"]
            assert kwargs["ipVersion"] in options, (
                f'''"ipVersion" cannot be "{kwargs["ipVersion"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str, **kwargs):
        """
        **Updates an adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - aclId (string): Acl ID
        - name (string): Name of the adaptive policy ACL
        - description (string): Description of the adaptive policy ACL
        - rules (array): An ordered array of the adaptive policy ACL rules. An empty array will clear the rules.
        - ipVersion (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
        """

        kwargs.update(locals())

        if "ipVersion" in kwargs:
            options = ["any", "ipv4", "ipv6"]
            assert kwargs["ipVersion"] in options, (
                f'''"ipVersion" cannot be "{kwargs["ipVersion"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        aclId = urllib.parse.quote(aclId, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

        body_params = [
            "name",
            "description",
            "rules",
            "ipVersion",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str):
        """
        **Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

        - organizationId (string): Organization ID
        - aclId (string): Acl ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        aclId = urllib.parse.quote(aclId, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/acls/{aclId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationAdaptivePolicyGroup(self, organizationId: str, name: str, sgt: int, **kwargs):
        """
        **Creates a new adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - name (string): Name of the group
        - sgt (integer): SGT value of the group
        - description (string): Description of the group (default: "")
        - policyObjects (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute) (default: [])
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str, **kwargs):
        """
        **Updates an adaptive policy group. If updating "Infrastructure", only the SGT is allowed. Cannot update "Unknown".**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of the group
        - sgt (integer): SGT value of the group
        - description (string): Description of the group
        - policyObjects (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

        body_params = [
            "name",
            "sgt",
            "description",
            "policyObjects",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str):
        """
        **Deletes the specified adaptive policy group and any associated policies and references**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/groups/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationAdaptivePolicyPolicy(self, organizationId: str, sourceGroup: dict, destinationGroup: dict, **kwargs):
        """
        **Add an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - sourceGroup (object): The source adaptive policy group (requires one unique attribute)
        - destinationGroup (object): The destination adaptive policy group (requires one unique attribute)
        - acls (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])
        - lastEntryRule (string): The rule to apply if there is no matching ACL (default: "default")
        """

        kwargs.update(locals())

        if "lastEntryRule" in kwargs:
            options = ["allow", "default", "deny"]
            assert kwargs["lastEntryRule"] in options, (
                f'''"lastEntryRule" cannot be "{kwargs["lastEntryRule"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str, **kwargs):
        """
        **Update an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - id (string): ID
        - sourceGroup (object): The source adaptive policy group (requires one unique attribute)
        - destinationGroup (object): The destination adaptive policy group (requires one unique attribute)
        - acls (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy
        - lastEntryRule (string): The rule to apply if there is no matching ACL
        """

        kwargs.update(locals())

        if "lastEntryRule" in kwargs:
            options = ["allow", "default", "deny"]
            assert kwargs["lastEntryRule"] in options, (
                f'''"lastEntryRule" cannot be "{kwargs["lastEntryRule"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

        body_params = [
            "sourceGroup",
            "destinationGroup",
            "acls",
            "lastEntryRule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str):
        """
        **Delete an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/policies/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationAdaptivePolicySettings(self, organizationId: str, **kwargs):
        """
        **Update global adaptive policy settings**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

        - organizationId (string): Organization ID
        - enabledNetworks (array): List of network IDs with adaptive policy enabled
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/adaptivePolicy/settings"

        body_params = [
            "enabledNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createOrganizationAlertsProfile(
        self, organizationId: str, type: str, alertCondition: dict, recipients: dict, networkTags: list, **kwargs
    ):
        """
        **Create an organization-wide alert configuration**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

        - organizationId (string): Organization ID
        - type (string): The alert type
        - alertCondition (object): The conditions that determine if the alert triggers
        - recipients (object): List of recipients that will recieve the alert.
        - networkTags (array): Networks with these tags will be monitored for the alert
        - description (string): User supplied description of the alert
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "appOutage",
                "voipJitter",
                "voipMos",
                "voipPacketLoss",
                "wanLatency",
                "wanPacketLoss",
                "wanStatus",
                "wanUtilization",
            ]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles"

        body_params = [
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationAlertsProfile(self, organizationId: str, alertConfigId: str, **kwargs):
        """
        **Update an organization-wide alert config**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

        - organizationId (string): Organization ID
        - alertConfigId (string): Alert config ID
        - enabled (boolean): Is the alert config enabled
        - type (string): The alert type
        - alertCondition (object): The conditions that determine if the alert triggers
        - recipients (object): List of recipients that will recieve the alert.
        - networkTags (array): Networks with these tags will be monitored for the alert
        - description (string): User supplied description of the alert
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = [
                "appOutage",
                "voipJitter",
                "voipMos",
                "voipPacketLoss",
                "wanLatency",
                "wanPacketLoss",
                "wanStatus",
                "wanUtilization",
            ]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        organizationId = urllib.parse.quote(organizationId, safe="")
        alertConfigId = urllib.parse.quote(alertConfigId, safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles/{alertConfigId}"

        body_params = [
            "enabled",
            "type",
            "alertCondition",
            "recipients",
            "networkTags",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationAlertsProfile(self, organizationId: str, alertConfigId: str):
        """
        **Removes an organization-wide alert config**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

        - organizationId (string): Organization ID
        - alertConfigId (string): Alert config ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        alertConfigId = urllib.parse.quote(alertConfigId, safe="")
        resource = f"/organizations/{organizationId}/alerts/profiles/{alertConfigId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationBrandingPolicy(self, organizationId: str, name: str, **kwargs):
        """
               **Add a new branding policy to an organization**
               https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

               - organizationId (string): Organization ID
               - name (string): Name of the Dashboard branding policy.
               - enabled (boolean): Boolean indicating whether this policy is enabled.
               - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
               - helpSettings (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
             'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
             the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
             Dashboard; see the documentation for each property to see the allowed values.
        Each property defaults to 'default or inherit' when not provided.
               - customLogo (object): Properties describing the custom logo attached to the branding policy.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationBrandingPoliciesPriorities(self, organizationId: str, **kwargs):
        """
        **Update the priority ordering of an organization's branding policies.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        - organizationId (string): Organization ID
        - brandingPolicyIds (array):       An ordered list of branding policy IDs that determines the priority order of how to apply the policies

        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/priorities"

        body_params = [
            "brandingPolicyIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str, name: str, **kwargs):
        """
          **Update a branding policy**
          https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

          - organizationId (string): Organization ID
          - brandingPolicyId (string): Branding policy ID
          - name (string): Name of the Dashboard branding policy.
          - enabled (boolean): Boolean indicating whether this policy is enabled.
          - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
          - helpSettings (object):       Settings for describing the modifications to various Help page features. Each property in this object accepts one of
        'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
        the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
        Dashboard; see the documentation for each property to see the allowed values.

          - customLogo (object): Properties describing the custom logo attached to the branding policy.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        brandingPolicyId = urllib.parse.quote(brandingPolicyId, safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

        body_params = [
            "name",
            "enabled",
            "adminSettings",
            "helpSettings",
            "customLogo",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Delete a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

        - organizationId (string): Organization ID
        - brandingPolicyId (string): Branding policy ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        brandingPolicyId = urllib.parse.quote(brandingPolicyId, safe="")
        resource = f"/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationConfigTemplate(self, organizationId: str, name: str, **kwargs):
        """
        **Create a new configuration template**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        - organizationId (string): Organization ID
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
        - copyFromNetworkId (string): The ID of the network or config template to copy configuration from
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/configTemplates"

        body_params = [
            "name",
            "timeZone",
            "copyFromNetworkId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str, **kwargs):
        """
        **Update a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        - organizationId (string): Organization ID
        - configTemplateId (string): Config template ID
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        configTemplateId = urllib.parse.quote(configTemplateId, safe="")
        resource = f"/organizations/{organizationId}/configTemplates/{configTemplateId}"

        body_params = [
            "name",
            "timeZone",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createOrganizationDevicesCellularDataProfile(
        self, organizationId: str, name: str, description: str, rules: list, **kwargs
    ):
        """
        **Add a cellular data management profile to this organization. Creates a cellular data management profile in this organization and returns the created profile, including its rules and actions.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-cellular-data-profile

        - organizationId (string): Organization ID
        - name (string): Name of the profile to be added. This must be unique.
        - description (string): Description of the profile to be added.
        - rules (array): The rules associated with this profile. At least one rule and no more than two rules may be defined for a profile.
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles"

        body_params = [
            "name",
            "description",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def batchOrganizationDevicesCellularDataProfilesAssignmentsCreate(self, organizationId: str, items: list, **kwargs):
        """
        **Assign devices to a Cellular Data Management Profile in batch. Creates up to 100 device-to-profile assignments and returns the created assignment IDs.**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-devices-cellular-data-profiles-assignments-create

        - organizationId (string): Organization ID
        - items (array): List of device-to-profile assignments to create.
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/assignments/batchCreate"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def bulkOrganizationDevicesCellularDataProfilesAssignmentsDelete(self, organizationId: str, items: list, **kwargs):
        """
        **Unassign devices from a Cellular Data Management Profile in batch. Removes up to 100 device-to-profile assignments and returns no response body on success.**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-cellular-data-profiles-assignments-delete

        - organizationId (string): Organization ID
        - items (array): List of device-to-profile assignments to remove.
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/assignments/bulkDelete"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationDevicesCellularDataProfile(self, organizationId: str, rules: list, profileId: str, **kwargs):
        """
        **Update a Cellular Data Management Profile. Note that changes made to this endpoint will overwrite existing settings for the profile so the entire profile, rules and actions should be sent when making an update.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-cellular-data-profile

        - organizationId (string): Organization ID
        - rules (array): The rules associated with this profile. At least one rule and no more than two rules may be defined for a profile.
        - profileId (string): ID of the profile.
        - description (string): New description of the profile.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        profileId = urllib.parse.quote(profileId, safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/{profileId}"

        body_params = [
            "profileId",
            "description",
            "rules",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationDevicesCellularDataProfile(self, organizationId: str, profileId: str):
        """
        **Delete a cellular data management profile from this organization. Removes the profile, including its associated rules and node assignments, and notifies affected devices of the resulting configuration change.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-cellular-data-profile

        - organizationId (string): Organization ID
        - profileId (string): Profile ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        profileId = urllib.parse.quote(profileId, safe="")
        resource = f"/organizations/{organizationId}/devices/cellular/data/profiles/{profileId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationDevicesControllerMigration(self, organizationId: str, serials: list, target: str, **kwargs):
        """
        **Migrate devices to another controller or management mode**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-controller-migration

        - organizationId (string): Organization ID
        - serials (array): A list of Meraki Serials to migrate
        - target (string): The controller or management mode to which the devices will be migrated
        """

        kwargs = locals()

        if "target" in kwargs:
            options = ["wirelessController"]
            assert kwargs["target"] in options, (
                f'''"target" cannot be "{kwargs["target"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/controller/migrations"

        body_params = [
            "serials",
            "target",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "mr/actions/migrate",
            "body": payload,
        }
        return action

    def bulkUpdateOrganizationDevicesDetails(self, organizationId: str, serials: list, details: list, **kwargs):
        """
        **Updating device details (currently only used for Catalyst devices)**
        https://developer.cisco.com/meraki/api-v1/#!bulk-update-organization-devices-details

        - organizationId (string): Organization ID
        - serials (array): A list of serials of devices to update
        - details (array): An array of details
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/details/bulkUpdate"

        body_params = [
            "serials",
            "details",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "details/update",
            "body": payload,
        }
        return action

    def bulkOrganizationDevicesPacketCaptureCapturesDelete(self, organizationId: str, captureIds: list, **kwargs):
        """
        **BulkDelete packet captures from cloud**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-devices-packet-capture-captures-delete

        - organizationId (string): Organization ID
        - captureIds (array): Delete the packet captures of the specified capture ids
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/bulkDelete"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def deleteOrganizationDevicesPacketCaptureCapture(self, organizationId: str, captureId: str):
        """
        **Delete a single packet capture from cloud using captureId**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-capture

        - organizationId (string): Organization ID
        - captureId (string): Capture ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        captureId = urllib.parse.quote(captureId, safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/captures/{captureId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationDevicesPacketCaptureSchedule(self, organizationId: str, devices: list, **kwargs):
        """
        **Create a schedule for packet capture**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-devices-packet-capture-schedule

        - organizationId (string): Organization ID
        - devices (array): device details
        - name (string): Name of the packet capture file
        - notes (string): Reason for capture
        - duration (integer): Duration of the capture in seconds
        - filterExpression (string): Filter expression for the capture
        - enabled (boolean): Enable or disable the schedule
        - schedule (object): Schedule details
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules"

        body_params = [
            "devices",
            "name",
            "notes",
            "duration",
            "filterExpression",
            "enabled",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def reorderOrganizationDevicesPacketCaptureSchedules(self, organizationId: str, order: list, **kwargs):
        """
        **Bulk update priorities of pcap schedules**
        https://developer.cisco.com/meraki/api-v1/#!reorder-organization-devices-packet-capture-schedules

        - organizationId (string): Organization ID
        - order (array): Array of schedule IDs and their priorities to reorder.
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/reorder"

        body_params = [
            "order",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "reorder",
            "body": payload,
        }
        return action

    def updateOrganizationDevicesPacketCaptureSchedule(self, organizationId: str, scheduleId: str, devices: list, **kwargs):
        """
        **Update a schedule for packet capture**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-devices-packet-capture-schedule

        - organizationId (string): Organization ID
        - scheduleId (string): Schedule ID
        - devices (array): device details
        - name (string): Name of the packet capture file
        - notes (string): Reason for capture
        - duration (integer): Duration of the capture in seconds
        - filterExpression (string): Filter expression for the capture
        - enabled (boolean): Enable or disable the schedule
        - schedule (object): Schedule details
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        scheduleId = urllib.parse.quote(scheduleId, safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId}"

        body_params = [
            "devices",
            "name",
            "notes",
            "duration",
            "filterExpression",
            "enabled",
            "schedule",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationDevicesPacketCaptureSchedule(self, organizationId: str, scheduleId: str):
        """
        **Delete schedule from cloud**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-devices-packet-capture-schedule

        - organizationId (string): Organization ID
        - scheduleId (string): Delete the capture schedules of the specified capture schedule id
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        scheduleId = urllib.parse.quote(scheduleId, safe="")
        resource = f"/organizations/{organizationId}/devices/packetCapture/schedules/{scheduleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str, **kwargs):
        """
        **Update an early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

        - organizationId (string): Organization ID
        - optInId (string): Opt in ID
        - limitScopeToNetworks (array): A list of network IDs to apply the opt-in to
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        optInId = urllib.parse.quote(optInId, safe="")
        resource = f"/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}"

        body_params = [
            "limitScopeToNetworks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def disableOrganizationIntegrationsXdrNetworks(self, organizationId: str, networks: list, **kwargs):
        """
        **Disable XDR on networks**
        https://developer.cisco.com/meraki/api-v1/#!disable-organization-integrations-xdr-networks

        - organizationId (string): Organization ID
        - networks (array): List containing the network ID and the product type to disable XDR on
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/integrations/xdr/networks/disable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "disable",
            "body": payload,
        }
        return action

    def enableOrganizationIntegrationsXdrNetworks(self, organizationId: str, networks: list, **kwargs):
        """
        **Enable XDR on networks**
        https://developer.cisco.com/meraki/api-v1/#!enable-organization-integrations-xdr-networks

        - organizationId (string): Organization ID
        - networks (array): List containing the network ID and the product type to enable XDR on
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/integrations/xdr/networks/enable"

        body_params = [
            "networks",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "enable",
            "body": payload,
        }
        return action

    def claimOrganizationInventoryOrders(self, organizationId: str, claimId: str, **kwargs):
        """
        **Claim an order by the secure unique order claim number, the order claim id**
        https://developer.cisco.com/meraki/api-v1/#!claim-organization-inventory-orders

        - organizationId (string): Organization ID
        - claimId (string): The unique order claim id
        - subscriptions (array): The individual subscriptions to claim
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/inventory/orders/claim"

        body_params = [
            "claimId",
            "subscriptions",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "claim",
            "body": payload,
        }
        return action

    def assignOrganizationLicensesSeats(self, organizationId: str, licenseId: str, networkId: str, seatCount: int, **kwargs):
        """
        **Assign SM seats to a network. This will increase the managed SM device limit of the network**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        - organizationId (string): Organization ID
        - licenseId (string): The ID of the SM license to assign seats from
        - networkId (string): The ID of the SM network to assign the seats to
        - seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/licenses/assignSeats"

        body_params = [
            "licenseId",
            "networkId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "assignSeats",
            "body": payload,
        }
        return action

    def moveOrganizationLicenses(self, organizationId: str, destOrganizationId: str, licenseIds: list, **kwargs):
        """
        **Move licenses to another organization. This will also move any devices that the licenses are assigned to**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        - organizationId (string): Organization ID
        - destOrganizationId (string): The ID of the organization to move the licenses to
        - licenseIds (array): A list of IDs of licenses to move to the new organization
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/licenses/move"

        body_params = [
            "destOrganizationId",
            "licenseIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "move",
            "body": payload,
        }
        return action

    def moveOrganizationLicensesSeats(
        self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int, **kwargs
    ):
        """
        **Move SM seats to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        - organizationId (string): Organization ID
        - destOrganizationId (string): The ID of the organization to move the SM seats to
        - licenseId (string): The ID of the SM license to move the seats from
        - seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/licenses/moveSeats"

        body_params = [
            "destOrganizationId",
            "licenseId",
            "seatCount",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "moveSeats",
            "body": payload,
        }
        return action

    def renewOrganizationLicensesSeats(self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str, **kwargs):
        """
        **Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license**
        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        - organizationId (string): Organization ID
        - licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
        - unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/licenses/renewSeats"

        body_params = [
            "licenseIdToRenew",
            "unusedLicenseId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "renewSeats",
            "body": payload,
        }
        return action

    def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        - organizationId (string): Organization ID
        - licenseId (string): License ID
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to  null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        licenseId = urllib.parse.quote(licenseId, safe="")
        resource = f"/organizations/{organizationId}/licenses/{licenseId}"

        body_params = [
            "deviceSerial",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateOrganizationLoginSecurity(self, organizationId: str, **kwargs):
        """
        **Update the login security settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        - organizationId (string): Organization ID
        - enforcePasswordExpiration (boolean): Boolean indicating whether users are forced to change their password every X number of days.
        - passwordExpirationDays (integer): Number of days after which users will be forced to change their password.
        - enforceDifferentPasswords (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
        - numDifferentPasswords (integer): Number of recent passwords that new password must be distinct from.
        - enforceStrongPasswords (boolean): Deprecated. Values of 'false' are always ignored.
        - minimumPasswordLength (integer): Minimum number of characters required in admins' passwords.
        - enforceAccountLockout (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
        - accountLockoutAttempts (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
        - enforceIdleTimeout (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
        - idleTimeoutMinutes (integer): Number of minutes users can remain idle before being logged out of their accounts.
        - enforceTwoFactorAuth (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the authenticator application.
        - enforceLoginIpRanges (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
        - loginIpRanges (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
        - enforceLockedIpSessions (boolean): Boolean indicating whether Dashboard sessions are locked to the IP address from which they were established. Only applicable to organizations that support locked-IP sessions; otherwise the parameter is ignored.
        - apiAuthentication (object): Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/loginSecurity"

        body_params = [
            "enforcePasswordExpiration",
            "passwordExpirationDays",
            "enforceDifferentPasswords",
            "numDifferentPasswords",
            "enforceStrongPasswords",
            "minimumPasswordLength",
            "enforceAccountLockout",
            "accountLockoutAttempts",
            "enforceIdleTimeout",
            "idleTimeoutMinutes",
            "enforceTwoFactorAuth",
            "enforceLoginIpRanges",
            "loginIpRanges",
            "enforceLockedIpSessions",
            "apiAuthentication",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createOrganizationNetwork(self, organizationId: str, name: str, productTypes: list, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        - organizationId (string): Organization ID
        - name (string): The name of the new network
        - productTypes (array): The product type(s) of the new network. If more than one type is included, the network will be a combined network.
        - tags (array): A list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        - notes (string): Add any notes or additional information about this network here.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/networks"

        body_params = [
            "name",
            "productTypes",
            "tags",
            "timeZone",
            "copyFromNetworkId",
            "notes",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def combineOrganizationNetworks(self, organizationId: str, name: str, networkIds: list, **kwargs):
        """
        **Combine multiple networks into a single network**
        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        - organizationId (string): Organization ID
        - name (string): The name of the combined network
        - networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/networks/combine"

        body_params = [
            "name",
            "networkIds",
            "enrollmentString",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "combine",
            "body": payload,
        }
        return action

    def createOrganizationPoliciesGlobalFirewallRuleset(self, organizationId: str, name: str, **kwargs):
        """
        **Create an Organization-Wide Policy Firewall Ruleset**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-firewall-ruleset

        - organizationId (string): Organization ID
        - name (string): Name of the firewall ruleset
        - description (string): Description of the firewall ruleset
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def createOrganizationPoliciesGlobalFirewallRulesetsRule(
        self, organizationId: str, name: str, rulesetId: str, policy: str, sources: dict, destinations: dict, **kwargs
    ):
        """
        **Create an Organization-Wide Policy Firewall Rule**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-firewall-rulesets-rule

        - organizationId (string): Organization ID
        - name (string): Name of the firewall rule
        - rulesetId (string): Firewall ruleset ID to associate the rule with
        - policy (string): Rule policy - allow or deny traffic
        - sources (object): Source traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        - destinations (object): Destination traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        - enabled (boolean): Whether the rule is enabled
        - priority (integer): Rule priority (lower numbers = higher priority)
        - description (string): Description of the firewall rule
        """

        kwargs.update(locals())

        if "policy" in kwargs:
            options = ["allow", "deny"]
            assert kwargs["policy"] in options, (
                f'''"policy" cannot be "{kwargs["policy"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules"

        body_params = [
            "name",
            "rulesetId",
            "policy",
            "enabled",
            "priority",
            "description",
            "sources",
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def deleteOrganizationPoliciesGlobalFirewallRulesetsRule(self, organizationId: str, ruleId: str):
        """
        **Delete an Organization-Wide Policy Firewall Rule**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-firewall-rulesets-rule

        - organizationId (string): Organization ID
        - ruleId (string): Rule ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        ruleId = urllib.parse.quote(ruleId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules/{ruleId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationPoliciesGlobalFirewallRulesetsRule(self, organizationId: str, ruleId: str, **kwargs):
        """
        **Update an Organization-Wide Policy Firewall Rule**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-firewall-rulesets-rule

        - organizationId (string): Organization ID
        - ruleId (string): Rule ID
        - name (string): Name of the firewall rule
        - rulesetId (string): Firewall ruleset ID to associate the rule with
        - policy (string): Rule policy - allow or deny traffic
        - enabled (boolean): Whether the rule is enabled
        - priority (integer): Rule priority (lower numbers = higher priority)
        - description (string): Description of the firewall rule
        - sources (object): Source traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        - destinations (object): Destination traffic criteria. Each source or destination bloc is capped separately per rule at 100 total segment values. The count is segments_values_count: the sum of all values across every segment type in that bloc. Ports use a separate cap of 100.
        """

        kwargs.update(locals())

        if "policy" in kwargs:
            options = ["allow", "deny"]
            assert kwargs["policy"] in options, (
                f'''"policy" cannot be "{kwargs["policy"]}", & must be set to one of: {options}'''
            )

        organizationId = urllib.parse.quote(organizationId, safe="")
        ruleId = urllib.parse.quote(ruleId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/rules/{ruleId}"

        body_params = [
            "name",
            "rulesetId",
            "policy",
            "enabled",
            "priority",
            "description",
            "sources",
            "destinations",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def updateOrganizationPoliciesGlobalFirewallRuleset(self, organizationId: str, rulesetId: str, **kwargs):
        """
        **Update an Organization-Wide Policy Firewall Ruleset**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-firewall-ruleset

        - organizationId (string): Organization ID
        - rulesetId (string): Ruleset ID
        - name (string): Name of the firewall ruleset
        - description (string): Description of the firewall ruleset
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        rulesetId = urllib.parse.quote(rulesetId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/{rulesetId}"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationPoliciesGlobalFirewallRuleset(self, organizationId: str, rulesetId: str):
        """
        **Delete an Organization-Wide Policy Firewall Ruleset**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-firewall-ruleset

        - organizationId (string): Organization ID
        - rulesetId (string): Ruleset ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        rulesetId = urllib.parse.quote(rulesetId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/firewall/rulesets/{rulesetId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationPoliciesGlobalGroupPolicy(self, organizationId: str, name: str, **kwargs):
        """
        **Create an Organization-Wide Policy**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-group-policy

        - organizationId (string): Organization ID
        - name (string): Name of the policy
        - description (string): Description of the policy
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def assignOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups(
        self, organizationId: str, policy: dict, adaptivePolicyGroups: list, **kwargs
    ):
        """
        **Assign adaptive policy groups to a policy**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-policies-global-group-policies-adaptive-policy-groups

        - organizationId (string): Organization ID
        - policy (object): Policy to assign adaptive policy groups to
        - adaptivePolicyGroups (array): Adaptive policy groups to assign
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/adaptivePolicyGroups/assign"

        body_params = [
            "policy",
            "adaptivePolicyGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "assign",
            "body": payload,
        }
        return action

    def removeOrganizationPoliciesGlobalGroupPoliciesAdaptivePolicyGroups(
        self, organizationId: str, policy: dict, adaptivePolicyGroups: list, **kwargs
    ):
        """
        **Remove adaptive policy groups from a policy**
        https://developer.cisco.com/meraki/api-v1/#!remove-organization-policies-global-group-policies-adaptive-policy-groups

        - organizationId (string): Organization ID
        - policy (object): Policy to remove adaptive policy groups from
        - adaptivePolicyGroups (array): Adaptive policy groups to remove
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/adaptivePolicyGroups/remove"

        body_params = [
            "policy",
            "adaptivePolicyGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "remove",
            "body": payload,
        }
        return action

    def createOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment(
        self, organizationId: str, rulesetId: str, policyId: str, **kwargs
    ):
        """
        **Create an Organization-Wide Policy Ruleset Assignment**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policies-global-group-policies-firewall-rulesets-assignment

        - organizationId (string): Organization ID
        - rulesetId (string): ID of the ruleset to assign
        - policyId (string): ID of the policy to assign the ruleset to
        - priority (integer): Priority of the ruleset assignment (lower numbers = higher priority)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments"

        body_params = [
            "rulesetId",
            "policyId",
            "priority",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment(
        self, organizationId: str, assignmentId: str, **kwargs
    ):
        """
        **Update an Organization-Wide Policy Ruleset Assignment**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-group-policies-firewall-rulesets-assignment

        - organizationId (string): Organization ID
        - assignmentId (string): Assignment ID
        - rulesetId (string): ID of the ruleset to assign
        - policyId (string): ID of the policy to assign the ruleset to
        - priority (integer): Priority of the ruleset assignment (lower numbers = higher priority)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        assignmentId = urllib.parse.quote(assignmentId, safe="")
        resource = (
            f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/{assignmentId}"
        )

        body_params = [
            "rulesetId",
            "policyId",
            "priority",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationPoliciesGlobalGroupPoliciesFirewallRulesetsAssignment(self, organizationId: str, assignmentId: str):
        """
        **Delete an Organization-Wide Policy Ruleset Assignment**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-group-policies-firewall-rulesets-assignment

        - organizationId (string): Organization ID
        - assignmentId (string): Assignment ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        assignmentId = urllib.parse.quote(assignmentId, safe="")
        resource = (
            f"/organizations/{organizationId}/policies/global/group/policies/firewall/rulesets/assignments/{assignmentId}"
        )

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationPoliciesGlobalGroupPolicy(self, organizationId: str, policyId: str, **kwargs):
        """
        **Update an Organization-Wide Policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policies-global-group-policy

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        - name (string): Name of the policy
        - description (string): Description of the policy
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        policyId = urllib.parse.quote(policyId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/{policyId}"

        body_params = [
            "name",
            "description",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationPoliciesGlobalGroupPolicy(self, organizationId: str, policyId: str):
        """
        **Delete an Organization-Wide Policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policies-global-group-policy

        - organizationId (string): Organization ID
        - policyId (string): Policy ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        policyId = urllib.parse.quote(policyId, safe="")
        resource = f"/organizations/{organizationId}/policies/global/group/policies/{policyId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationPolicyObject(self, organizationId: str, name: str, category: str, type: str, **kwargs):
        """
        **Creates a new Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

        - organizationId (string): Organization ID
        - name (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - category (string): Category of a policy object (one of: adaptivePolicy, network)
        - type (string): Type of a policy object (one of: adaptivePolicyIpv4Cidr, cidr, fqdn, ipAndMask)
        - cidr (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
        - fqdn (string): Fully qualified domain name of policy object (e.g. "example.com")
        - mask (string): Mask of a policy object (e.g. "255.255.0.0")
        - ip (string): IP Address of a policy object (e.g. "1.2.3.4")
        - groupIds (array): The IDs of policy object groups the policy object belongs to
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policyObjects"

        body_params = [
            "name",
            "category",
            "type",
            "cidr",
            "fqdn",
            "mask",
            "ip",
            "groupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def createOrganizationPolicyObjectsGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Creates a new Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

        - organizationId (string): Organization ID
        - name (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - category (string): Category of a policy object group (one of: NetworkObjectGroup, GeoLocationGroup, PortObjectGroup, ApplicationGroup)
        - objectIds (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups"

        body_params = [
            "name",
            "category",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str, **kwargs):
        """
        **Updates a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

        - organizationId (string): Organization ID
        - policyObjectGroupId (string): Policy object group ID
        - name (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - objectIds (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        policyObjectGroupId = urllib.parse.quote(policyObjectGroupId, safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        body_params = [
            "name",
            "objectIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str):
        """
        **Deletes a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

        - organizationId (string): Organization ID
        - policyObjectGroupId (string): Policy object group ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        policyObjectGroupId = urllib.parse.quote(policyObjectGroupId, safe="")
        resource = f"/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationPolicyObject(self, organizationId: str, policyObjectId: str, **kwargs):
        """
        **Updates a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

        - organizationId (string): Organization ID
        - policyObjectId (string): Policy object ID
        - name (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - cidr (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
        - fqdn (string): Fully qualified domain name of policy object (e.g. "example.com")
        - mask (string): Mask of a policy object (e.g. "255.255.0.0")
        - ip (string): IP Address of a policy object (e.g. "1.2.3.4")
        - groupIds (array): The IDs of policy object groups the policy object belongs to
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        policyObjectId = urllib.parse.quote(policyObjectId, safe="")
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

        body_params = [
            "name",
            "cidr",
            "fqdn",
            "mask",
            "ip",
            "groupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationPolicyObject(self, organizationId: str, policyObjectId: str):
        """
        **Deletes a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

        - organizationId (string): Organization ID
        - policyObjectId (string): Policy object ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        policyObjectId = urllib.parse.quote(policyObjectId, safe="")
        resource = f"/organizations/{organizationId}/policyObjects/{policyObjectId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationSamlIdp(self, organizationId: str, x509certSha1Fingerprint: str, **kwargs):
        """
        **Create a SAML IdP for your organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        - organizationId (string): Organization ID
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - ssoLoginUrl (string): Dashboard will redirect users to this URL to log in again when their sessions expire.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/saml/idps"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationSamlIdp(self, organizationId: str, idpId: str, **kwargs):
        """
        **Update a SAML IdP in your organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - ssoLoginUrl (string): Dashboard will redirect users to this URL to log in again when their sessions expire.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        idpId = urllib.parse.quote(idpId, safe="")
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        body_params = [
            "x509certSha1Fingerprint",
            "ssoLoginUrl",
            "sloLogoutUrl",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSamlIdp(self, organizationId: str, idpId: str):
        """
        **Remove a SAML IdP in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        - organizationId (string): Organization ID
        - idpId (string): Idp ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        idpId = urllib.parse.quote(idpId, safe="")
        resource = f"/organizations/{organizationId}/saml/idps/{idpId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def batchOrganizationSaseConnectorsDelete(self, organizationId: str, **kwargs):
        """
        **Delete SSE Connectors by ID**
        https://developer.cisco.com/meraki/api-v1/#!batch-organization-sase-connectors-delete

        - organizationId (string): Organization ID
        - items (array): List of connectors to delete (maximum 20 items)
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/sase/connectors/batchDelete"

        body_params = [
            "items",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "teardown",
            "body": payload,
        }
        return action

    def createOrganizationSaseIntegration(self, organizationId: str, api: dict, **kwargs):
        """
        **Create a new Secure Access integration**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-sase-integration

        - organizationId (string): Organization ID
        - api (object): API credentials
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/sase/integrations"

        body_params = [
            "api",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def deleteOrganizationSaseIntegration(self, organizationId: str, integrationId: str):
        """
        **Remove a Secure Access integration**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-sase-integration

        - organizationId (string): Organization ID
        - integrationId (string): Integration ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        integrationId = urllib.parse.quote(integrationId, safe="")
        resource = f"/organizations/{organizationId}/sase/integrations/{integrationId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def attachOrganizationSaseSites(self, organizationId: str, **kwargs):
        """
        **Attach sites in this organization to Secure Access. For an organization, a maximum of 2500 sites can be attached if they are in spoke mode or a maximum of 10 sites can be attached in hub mode.**
        https://developer.cisco.com/meraki/api-v1/#!attach-organization-sase-sites

        - organizationId (string): Organization ID
        - items (array): List of Meraki SD-WAN sites with the associated regions to be attached.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/sase/sites/attach"

        body_params = [
            "items",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def detachOrganizationSaseSites(self, organizationId: str, **kwargs):
        """
        **Detach sites in this organization from Secure Access. This will remove the sites from Secure Access.**
        https://developer.cisco.com/meraki/api-v1/#!detach-organization-sase-sites

        - organizationId (string): Organization ID
        - items (array): List of Secure Access sites to be detached.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/sase/sites/detach"

        action = {
            "resource": resource,
            "operation": "detach",
        }
        return action

    def updateOrganizationSaseSite(self, organizationId: str, siteId: str, **kwargs):
        """
        **Update the configuration for a site. Currently, only supports updating default route enablement.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-sase-site

        - organizationId (string): Organization ID
        - siteId (string): Site ID of the site to update
        - routing (object): Routing configuration for the site
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        siteId = urllib.parse.quote(siteId, safe="")
        resource = f"/organizations/{organizationId}/sase/sites/{siteId}"

        body_params = [
            "siteId",
            "routing",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSplashAsset(self, organizationId: str, id: str):
        """
        **Delete a Splash Theme Asset**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-asset

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/splash/assets/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationSplashTheme(self, organizationId: str, **kwargs):
        """
        **Create a Splash Theme**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme

        - organizationId (string): Organization ID
        - name (string): theme name
        - baseTheme (string): base theme id
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/splash/themes"

        body_params = [
            "name",
            "baseTheme",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def deleteOrganizationSplashTheme(self, organizationId: str, id: str):
        """
        **Delete a Splash Theme**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-splash-theme

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/splash/themes/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationSplashThemeAsset(self, organizationId: str, themeIdentifier: str, **kwargs):
        """
        **Create a Splash Theme Asset**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-splash-theme-asset

        - organizationId (string): Organization ID
        - themeIdentifier (string): Theme identifier
        - name (string): File name. Will overwrite files with same name.
        - content (string): a file containing the asset content
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        themeIdentifier = urllib.parse.quote(themeIdentifier, safe="")
        resource = f"/organizations/{organizationId}/splash/themes/{themeIdentifier}/assets"

        body_params = [
            "name",
            "content",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action
