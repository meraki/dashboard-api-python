import urllib


class ActionBatchOrganizations(object):
    def __init__(self):
        super(ActionBatchOrganizations, self).__init__()
        


    def createOrganizationAdaptivePolicyAcl(self, organizationId: str, name: str, rules: list, ipVersion: str, **kwargs):
        """
        **Creates new adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-acl

        - organizationId (string): (required)
        - name (string): Name of the adaptive policy ACL
        - rules (array): An ordered array of the adaptive policy ACL rules.
        - ipVersion (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
        - description (string): Description of the adaptive policy ACL
        """

        kwargs.update(locals())

        if 'ipVersion' in kwargs:
            options = ['any', 'ipv4', 'ipv6']
            assert kwargs['ipVersion'] in options, f'''"ipVersion" cannot be "{kwargs['ipVersion']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'acls'],
            'operation': 'createOrganizationAdaptivePolicyAcl'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls'

        body_params = ['name', 'description', 'rules', 'ipVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str, **kwargs):
        """
        **Updates an adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-acl

        - organizationId (string): (required)
        - aclId (string): (required)
        - name (string): Name of the adaptive policy ACL
        - description (string): Description of the adaptive policy ACL
        - rules (array): An ordered array of the adaptive policy ACL rules. An empty array will clear the rules.
        - ipVersion (string): IP version of adpative policy ACL. One of: 'any', 'ipv4' or 'ipv6'
        """

        kwargs.update(locals())

        if 'ipVersion' in kwargs:
            options = ['any', 'ipv4', 'ipv6']
            assert kwargs['ipVersion'] in options, f'''"ipVersion" cannot be "{kwargs['ipVersion']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'acls'],
            'operation': 'updateOrganizationAdaptivePolicyAcl'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls/{aclId}'

        body_params = ['name', 'description', 'rules', 'ipVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str):
        """
        **Deletes the specified adaptive policy ACL**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-acl

        - organizationId (string): (required)
        - aclId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'acls'],
            'operation': 'deleteOrganizationAdaptivePolicyAcl'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls/{aclId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createOrganizationAdaptivePolicyGroup(self, organizationId: str, name: str, sgt: int, **kwargs):
        """
        **Creates a new adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-group

        - organizationId (string): (required)
        - name (string): Name of the group
        - sgt (integer): SGT value of the group
        - description (string): Description of the group (default: "")
        - policyObjects (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute) (default: [])
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'groups'],
            'operation': 'createOrganizationAdaptivePolicyGroup'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups'

        body_params = ['name', 'sgt', 'description', 'policyObjects', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str, **kwargs):
        """
        **Updates an adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-group

        - organizationId (string): (required)
        - id (string): (required)
        - name (string): Name of the group
        - sgt (integer): SGT value of the group
        - description (string): Description of the group
        - policyObjects (array): The policy objects that belong to this group; traffic from addresses specified by these policy objects will be tagged with this group's SGT value if no other tagging scheme is being used (each requires one unique attribute)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'groups'],
            'operation': 'updateOrganizationAdaptivePolicyGroup'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups/{id}'

        body_params = ['name', 'sgt', 'description', 'policyObjects', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str):
        """
        **Deletes the specified adaptive policy group and any associated policies and references**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-group

        - organizationId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'groups'],
            'operation': 'deleteOrganizationAdaptivePolicyGroup'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups/{id}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createOrganizationAdaptivePolicyPolicy(self, organizationId: str, sourceGroup: dict, destinationGroup: dict, **kwargs):
        """
        **Add an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-adaptive-policy-policy

        - organizationId (string): (required)
        - sourceGroup (object): The source adaptive policy group (requires one unique attribute)
        - destinationGroup (object): The destination adaptive policy group (requires one unique attribute)
        - acls (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy (default: [])
        - lastEntryRule (string): The rule to apply if there is no matching ACL (default: "default")
        """

        kwargs.update(locals())

        if 'lastEntryRule' in kwargs:
            options = ['allow', 'default', 'deny']
            assert kwargs['lastEntryRule'] in options, f'''"lastEntryRule" cannot be "{kwargs['lastEntryRule']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'policies'],
            'operation': 'createOrganizationAdaptivePolicyPolicy'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies'

        body_params = ['sourceGroup', 'destinationGroup', 'acls', 'lastEntryRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str, **kwargs):
        """
        **Update an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-policy

        - organizationId (string): (required)
        - id (string): (required)
        - sourceGroup (object): The source adaptive policy group (requires one unique attribute)
        - destinationGroup (object): The destination adaptive policy group (requires one unique attribute)
        - acls (array): An ordered array of adaptive policy ACLs (each requires one unique attribute) that apply to this policy
        - lastEntryRule (string): The rule to apply if there is no matching ACL
        """

        kwargs.update(locals())

        if 'lastEntryRule' in kwargs:
            options = ['allow', 'default', 'deny']
            assert kwargs['lastEntryRule'] in options, f'''"lastEntryRule" cannot be "{kwargs['lastEntryRule']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'policies'],
            'operation': 'updateOrganizationAdaptivePolicyPolicy'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies/{id}'

        body_params = ['sourceGroup', 'destinationGroup', 'acls', 'lastEntryRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str):
        """
        **Delete an Adaptive Policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-adaptive-policy-policy

        - organizationId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'policies'],
            'operation': 'deleteOrganizationAdaptivePolicyPolicy'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies/{id}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateOrganizationAdaptivePolicySettings(self, organizationId: str, **kwargs):
        """
        **Update global adaptive policy settings**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-adaptive-policy-settings

        - organizationId (string): (required)
        - enabledNetworks (array): List of network IDs with adaptive policy enabled
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'settings'],
            'operation': 'updateOrganizationAdaptivePolicySettings'
        }
        resource = f'/organizations/{organizationId}/adaptivePolicy/settings'

        body_params = ['enabledNetworks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createOrganizationAlertsProfile(self, organizationId: str, type: str, alertCondition: dict, recipients: dict, networkTags: list, **kwargs):
        """
        **Create an organization-wide alert configuration**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-alerts-profile

        - organizationId (string): (required)
        - type (string): The alert type
        - alertCondition (object): The conditions that determine if the alert triggers
        - recipients (object): List of recipients that will recieve the alert.
        - networkTags (array): Networks with these tags will be monitored for the alert
        - description (string): User supplied description of the alert
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['appOutage', 'voipJitter', 'voipMos', 'voipPacketLoss', 'wanLatency', 'wanPacketLoss', 'wanStatus', 'wanUtilization']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'alerts', 'profiles'],
            'operation': 'createOrganizationAlertsProfile'
        }
        resource = f'/organizations/{organizationId}/alerts/profiles'

        body_params = ['type', 'alertCondition', 'recipients', 'networkTags', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationAlertsProfile(self, organizationId: str, alertConfigId: str, **kwargs):
        """
        **Update an organization-wide alert config**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-alerts-profile

        - organizationId (string): (required)
        - alertConfigId (string): (required)
        - enabled (boolean): Is the alert config enabled
        - type (string): The alert type
        - alertCondition (object): The conditions that determine if the alert triggers
        - recipients (object): List of recipients that will recieve the alert.
        - networkTags (array): Networks with these tags will be monitored for the alert
        - description (string): User supplied description of the alert
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['appOutage', 'voipJitter', 'voipMos', 'voipPacketLoss', 'wanLatency', 'wanPacketLoss', 'wanStatus', 'wanUtilization']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'alerts', 'profiles'],
            'operation': 'updateOrganizationAlertsProfile'
        }
        resource = f'/organizations/{organizationId}/alerts/profiles/{alertConfigId}'

        body_params = ['enabled', 'type', 'alertCondition', 'recipients', 'networkTags', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationAlertsProfile(self, organizationId: str, alertConfigId: str):
        """
        **Removes an organization-wide alert config**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-alerts-profile

        - organizationId (string): (required)
        - alertConfigId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'alerts', 'profiles'],
            'operation': 'deleteOrganizationAlertsProfile'
        }
        resource = f'/organizations/{organizationId}/alerts/profiles/{alertConfigId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createOrganizationBrandingPolicy(self, organizationId: str, **kwargs):
        """
        **Add a new branding policy to an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

        - organizationId (string): (required)
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

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'createOrganizationBrandingPolicy'
        }
        resource = f'/organizations/{organizationId}/brandingPolicies'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings', 'customLogo', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationBrandingPoliciesPriorities(self, organizationId: str, **kwargs):
        """
        **Update the priority ordering of an organization's branding policies.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        - organizationId (string): (required)
        - brandingPolicyIds (array):       An ordered list of branding policy IDs that determines the priority order of how to apply the policies

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies', 'priorities'],
            'operation': 'updateOrganizationBrandingPoliciesPriorities'
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        body_params = ['brandingPolicyIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str, **kwargs):
        """
        **Update a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy

        - organizationId (string): (required)
        - brandingPolicyId (string): (required)
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

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'updateOrganizationBrandingPolicy'
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings', 'customLogo', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Delete a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy

        - organizationId (string): (required)
        - brandingPolicyId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'deleteOrganizationBrandingPolicy'
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createOrganizationConfigTemplate(self, organizationId: str, name: str, **kwargs):
        """
        **Create a new configuration template**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template

        - organizationId (string): (required)
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
        - copyFromNetworkId (string): The ID of the network or config template to copy configuration from
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'createOrganizationConfigTemplate'
        }
        resource = f'/organizations/{organizationId}/configTemplates'

        body_params = ['name', 'timeZone', 'copyFromNetworkId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str, **kwargs):
        """
        **Update a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template

        - organizationId (string): (required)
        - configTemplateId (string): (required)
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'updateOrganizationConfigTemplate'
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        body_params = ['name', 'timeZone', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str, **kwargs):
        """
        **Update an early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-early-access-features-opt-in

        - organizationId (string): (required)
        - optInId (string): (required)
        - limitScopeToNetworks (array): A list of network IDs to apply the opt-in to
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'earlyAccess', 'features', 'optIns'],
            'operation': 'updateOrganizationEarlyAccessFeaturesOptIn'
        }
        resource = f'/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}'

        body_params = ['limitScopeToNetworks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def assignOrganizationLicensesSeats(self, organizationId: str, licenseId: str, networkId: str, seatCount: int):
        """
        **Assign SM seats to a network**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats

        - organizationId (string): (required)
        - licenseId (string): The ID of the SM license to assign seats from
        - networkId (string): The ID of the SM network to assign the seats to
        - seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'assignOrganizationLicensesSeats'
        }
        resource = f'/organizations/{organizationId}/licenses/assignSeats'

        body_params = ['licenseId', 'networkId', 'seatCount', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def moveOrganizationLicenses(self, organizationId: str, destOrganizationId: str, licenseIds: list):
        """
        **Move licenses to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses

        - organizationId (string): (required)
        - destOrganizationId (string): The ID of the organization to move the licenses to
        - licenseIds (array): A list of IDs of licenses to move to the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'moveOrganizationLicenses'
        }
        resource = f'/organizations/{organizationId}/licenses/move'

        body_params = ['destOrganizationId', 'licenseIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def moveOrganizationLicensesSeats(self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int):
        """
        **Move SM seats to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats

        - organizationId (string): (required)
        - destOrganizationId (string): The ID of the organization to move the SM seats to
        - licenseId (string): The ID of the SM license to move the seats from
        - seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'moveOrganizationLicensesSeats'
        }
        resource = f'/organizations/{organizationId}/licenses/moveSeats'

        body_params = ['destOrganizationId', 'licenseId', 'seatCount', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def renewOrganizationLicensesSeats(self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str):
        """
        **Renew SM seats of a license**
        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats

        - organizationId (string): (required)
        - licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
        - unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'renewOrganizationLicensesSeats'
        }
        resource = f'/organizations/{organizationId}/licenses/renewSeats'

        body_params = ['licenseIdToRenew', 'unusedLicenseId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        - organizationId (string): (required)
        - licenseId (string): (required)
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to  null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'updateOrganizationLicense'
        }
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        body_params = ['deviceSerial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def updateOrganizationLoginSecurity(self, organizationId: str, **kwargs):
        """
        **Update the login security settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-login-security

        - organizationId (string): (required)
        - enforcePasswordExpiration (boolean): Boolean indicating whether users are forced to change their password every X number of days.
        - passwordExpirationDays (integer): Number of days after which users will be forced to change their password.
        - enforceDifferentPasswords (boolean): Boolean indicating whether users, when setting a new password, are forced to choose a new password that is different from any past passwords.
        - numDifferentPasswords (integer): Number of recent passwords that new password must be distinct from.
        - enforceStrongPasswords (boolean): Boolean indicating whether users will be forced to choose strong passwords for their accounts. Strong passwords are at least 8 characters that contain 3 of the following: number, uppercase letter, lowercase letter, and symbol
        - enforceAccountLockout (boolean): Boolean indicating whether users' Dashboard accounts will be locked out after a specified number of consecutive failed login attempts.
        - accountLockoutAttempts (integer): Number of consecutive failed login attempts after which users' accounts will be locked.
        - enforceIdleTimeout (boolean): Boolean indicating whether users will be logged out after being idle for the specified number of minutes.
        - idleTimeoutMinutes (integer): Number of minutes users can remain idle before being logged out of their accounts.
        - enforceTwoFactorAuth (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the authenticator application.
        - enforceLoginIpRanges (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
        - loginIpRanges (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
        - apiAuthentication (object): Details for indicating whether organization will restrict access to API (but not Dashboard) to certain IP addresses.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'loginSecurity'],
            'operation': 'updateOrganizationLoginSecurity'
        }
        resource = f'/organizations/{organizationId}/loginSecurity'

        body_params = ['enforcePasswordExpiration', 'passwordExpirationDays', 'enforceDifferentPasswords', 'numDifferentPasswords', 'enforceStrongPasswords', 'enforceAccountLockout', 'accountLockoutAttempts', 'enforceIdleTimeout', 'idleTimeoutMinutes', 'enforceTwoFactorAuth', 'enforceLoginIpRanges', 'loginIpRanges', 'apiAuthentication', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createOrganizationNetwork(self, organizationId: str, name: str, productTypes: list, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-network

        - organizationId (string): (required)
        - name (string): The name of the new network
        - productTypes (array): The product type(s) of the new network. If more than one type is included, the network will be a combined network.
        - tags (array): A list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        - notes (string): Add any notes or additional information about this network here.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'createOrganizationNetwork'
        }
        resource = f'/organizations/{organizationId}/networks'

        body_params = ['name', 'productTypes', 'tags', 'timeZone', 'copyFromNetworkId', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def combineOrganizationNetworks(self, organizationId: str, name: str, networkIds: list, **kwargs):
        """
        **Combine multiple networks into a single network**
        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks

        - organizationId (string): (required)
        - name (string): The name of the combined network
        - networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'combineOrganizationNetworks'
        }
        resource = f'/organizations/{organizationId}/networks/combine'

        body_params = ['name', 'networkIds', 'enrollmentString', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def createOrganizationPolicyObject(self, organizationId: str, name: str, category: str, type: str, **kwargs):
        """
        **Creates a new Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-object

        - organizationId (string): (required)
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

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects'],
            'operation': 'createOrganizationPolicyObject'
        }
        resource = f'/organizations/{organizationId}/policyObjects'

        body_params = ['name', 'category', 'type', 'cidr', 'fqdn', 'mask', 'ip', 'groupIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def createOrganizationPolicyObjectsGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Creates a new Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-policy-objects-group

        - organizationId (string): (required)
        - name (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - category (string): Category of a policy object group (one of: NetworkObjectGroup, GeoLocationGroup, PortObjectGroup, ApplicationGroup)
        - objectIds (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects', 'groups'],
            'operation': 'createOrganizationPolicyObjectsGroup'
        }
        resource = f'/organizations/{organizationId}/policyObjects/groups'

        body_params = ['name', 'category', 'objectIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str, **kwargs):
        """
        **Updates a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-objects-group

        - organizationId (string): (required)
        - policyObjectGroupId (string): (required)
        - name (string): A name for the group of network addresses, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - objectIds (array): A list of Policy Object ID's that this NetworkObjectGroup should be associated to (note: these ID's will replace the existing associated Policy Objects)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects', 'groups'],
            'operation': 'updateOrganizationPolicyObjectsGroup'
        }
        resource = f'/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}'

        body_params = ['name', 'objectIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str):
        """
        **Deletes a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-objects-group

        - organizationId (string): (required)
        - policyObjectGroupId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects', 'groups'],
            'operation': 'deleteOrganizationPolicyObjectsGroup'
        }
        resource = f'/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def updateOrganizationPolicyObject(self, organizationId: str, policyObjectId: str, **kwargs):
        """
        **Updates a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-policy-object

        - organizationId (string): (required)
        - policyObjectId (string): (required)
        - name (string): Name of a policy object, unique within the organization (alphanumeric, space, dash, or underscore characters only)
        - cidr (string): CIDR Value of a policy object (e.g. 10.11.12.1/24")
        - fqdn (string): Fully qualified domain name of policy object (e.g. "example.com")
        - mask (string): Mask of a policy object (e.g. "255.255.0.0")
        - ip (string): IP Address of a policy object (e.g. "1.2.3.4")
        - groupIds (array): The IDs of policy object groups the policy object belongs to
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects'],
            'operation': 'updateOrganizationPolicyObject'
        }
        resource = f'/organizations/{organizationId}/policyObjects/{policyObjectId}'

        body_params = ['name', 'cidr', 'fqdn', 'mask', 'ip', 'groupIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationPolicyObject(self, organizationId: str, policyObjectId: str):
        """
        **Deletes a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-policy-object

        - organizationId (string): (required)
        - policyObjectId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects'],
            'operation': 'deleteOrganizationPolicyObject'
        }
        resource = f'/organizations/{organizationId}/policyObjects/{policyObjectId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def createOrganizationSamlIdp(self, organizationId: str, x509certSha1Fingerprint: str, **kwargs):
        """
        **Create a SAML IdP for your organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-idp

        - organizationId (string): (required)
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'createOrganizationSamlIdp'
        }
        resource = f'/organizations/{organizationId}/saml/idps'

        body_params = ['x509certSha1Fingerprint', 'sloLogoutUrl', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateOrganizationSamlIdp(self, organizationId: str, idpId: str, **kwargs):
        """
        **Update a SAML IdP in your organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-idp

        - organizationId (string): (required)
        - idpId (string): (required)
        - x509certSha1Fingerprint (string): Fingerprint (SHA1) of the SAML certificate provided by your Identity Provider (IdP). This will be used for encryption / validation.
        - sloLogoutUrl (string): Dashboard will redirect users to this URL when they sign out.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'updateOrganizationSamlIdp'
        }
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        body_params = ['x509certSha1Fingerprint', 'sloLogoutUrl', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteOrganizationSamlIdp(self, organizationId: str, idpId: str):
        """
        **Remove a SAML IdP in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-idp

        - organizationId (string): (required)
        - idpId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'deleteOrganizationSamlIdp'
        }
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        





    def deleteOrganizationUser(self, organizationId: str, userId: str):
        """
        **Delete a user and all of its authentication methods.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-user

        - organizationId (string): (required)
        - userId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'users'],
            'operation': 'deleteOrganizationUser'
        }
        resource = f'/organizations/{organizationId}/users/{userId}'

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
        



