import urllib


class AsyncOrganizations:
    def __init__(self, session):
        super().__init__()
        self._session = session
        


    def getOrganizations(self):
        """
        **List the organizations that the user has privileges on**
        https://developer.cisco.com/meraki/api-v1/#!get-organizations

        """

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'getOrganizations'
        }
        resource = f'/organizations'

        return self._session.get(metadata, resource)
        


    def createOrganization(self, name: str, **kwargs):
        """
        **Create a new organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization

        - name (string): The name of the organization
        - management (object): Information about the organization's management system
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'createOrganization'
        }
        resource = f'/organizations'

        body_params = ['name', 'management', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganization(self, organizationId: str):
        """
        **Return an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'getOrganization'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}'

        return self._session.get(metadata, resource)
        


    def updateOrganization(self, organizationId: str, **kwargs):
        """
        **Update an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization

        - organizationId (string): (required)
        - name (string): The name of the organization
        - management (object): Information about the organization's management system
        - api (object): API-specific settings
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'updateOrganization'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}'

        body_params = ['name', 'management', 'api', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganization(self, organizationId: str):
        """
        **Delete an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'deleteOrganization'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}'

        return self._session.delete(metadata, resource)
        


    def createOrganizationActionBatch(self, organizationId: str, actions: list, **kwargs):
        """
        **Create an action batch**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch

        - organizationId (string): (required)
        - actions (array): A set of changes to make as part of this action (<a href='https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/'>more details</a>)
        - confirmed (boolean): Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'createOrganizationActionBatch'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/actionBatches'

        body_params = ['confirmed', 'synchronous', 'actions', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationActionBatches(self, organizationId: str, **kwargs):
        """
        **Return the list of action batches in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches

        - organizationId (string): (required)
        - status (string): Filter batches by status. Valid types are pending, completed, and failed.
        """

        kwargs.update(locals())

        if 'status' in kwargs:
            options = ['completed', 'failed', 'pending']
            assert kwargs['status'] in options, f'''"status" cannot be "{kwargs['status']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'getOrganizationActionBatches'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/actionBatches'

        query_params = ['status', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def deleteOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Delete an action batch**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch

        - organizationId (string): (required)
        - actionBatchId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'deleteOrganizationActionBatch'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        actionBatchId = urllib.parse.quote(str(actionBatchId), safe='')
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return self._session.delete(metadata, resource)
        


    def updateOrganizationActionBatch(self, organizationId: str, actionBatchId: str, **kwargs):
        """
        **Update an action batch**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch

        - organizationId (string): (required)
        - actionBatchId (string): (required)
        - confirmed (boolean): A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'updateOrganizationActionBatch'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        actionBatchId = urllib.parse.quote(str(actionBatchId), safe='')
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        body_params = ['confirmed', 'synchronous', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Return an action batch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch

        - organizationId (string): (required)
        - actionBatchId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'getOrganizationActionBatch'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        actionBatchId = urllib.parse.quote(str(actionBatchId), safe='')
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return self._session.get(metadata, resource)
        


    def getOrganizationAdaptivePolicyAcls(self, organizationId: str):
        """
        **List adaptive policy ACLs in a organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acls

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'acls'],
            'operation': 'getOrganizationAdaptivePolicyAcls'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls'

        body_params = ['name', 'description', 'rules', 'ipVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationAdaptivePolicyAcl(self, organizationId: str, aclId: str):
        """
        **Returns the adaptive policy ACL information**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-acl

        - organizationId (string): (required)
        - aclId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'acls'],
            'operation': 'getOrganizationAdaptivePolicyAcl'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        aclId = urllib.parse.quote(str(aclId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls/{aclId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        aclId = urllib.parse.quote(str(aclId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls/{aclId}'

        body_params = ['name', 'description', 'rules', 'ipVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        aclId = urllib.parse.quote(str(aclId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/acls/{aclId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationAdaptivePolicyGroups(self, organizationId: str):
        """
        **List adaptive policy groups in a organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-groups

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'groups'],
            'operation': 'getOrganizationAdaptivePolicyGroups'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups'

        body_params = ['name', 'sgt', 'description', 'policyObjects', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationAdaptivePolicyGroup(self, organizationId: str, id: str):
        """
        **Returns an adaptive policy group**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-group

        - organizationId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'groups'],
            'operation': 'getOrganizationAdaptivePolicyGroup'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups/{id}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups/{id}'

        body_params = ['name', 'sgt', 'description', 'policyObjects', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/groups/{id}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationAdaptivePolicyOverview(self, organizationId: str):
        """
        **Returns adaptive policy aggregate statistics for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-overview

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'monitor', 'adaptivePolicy', 'overview'],
            'operation': 'getOrganizationAdaptivePolicyOverview'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/overview'

        return self._session.get(metadata, resource)
        


    def getOrganizationAdaptivePolicyPolicies(self, organizationId: str):
        """
        **List adaptive policies in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policies

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'policies'],
            'operation': 'getOrganizationAdaptivePolicyPolicies'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies'

        body_params = ['sourceGroup', 'destinationGroup', 'acls', 'lastEntryRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationAdaptivePolicyPolicy(self, organizationId: str, id: str):
        """
        **Return an adaptive policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-policy

        - organizationId (string): (required)
        - id (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'policies'],
            'operation': 'getOrganizationAdaptivePolicyPolicy'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies/{id}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies/{id}'

        body_params = ['sourceGroup', 'destinationGroup', 'acls', 'lastEntryRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        id = urllib.parse.quote(str(id), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/policies/{id}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationAdaptivePolicySettings(self, organizationId: str):
        """
        **Returns global adaptive policy settings in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-adaptive-policy-settings

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'adaptivePolicy', 'settings'],
            'operation': 'getOrganizationAdaptivePolicySettings'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/settings'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/adaptivePolicy/settings'

        body_params = ['enabledNetworks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationAdmins(self, organizationId: str):
        """
        **List the dashboard administrators in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-admins

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'getOrganizationAdmins'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/admins'

        return self._session.get(metadata, resource)
        


    def createOrganizationAdmin(self, organizationId: str, email: str, name: str, orgAccess: str, **kwargs):
        """
        **Create a new dashboard administrator**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-admin

        - organizationId (string): (required)
        - email (string): The email of the dashboard administrator. This attribute can not be updated.
        - name (string): The name of the dashboard administrator
        - orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
        - tags (array): The list of tags that the dashboard administrator has privileges on
        - networks (array): The list of networks that the dashboard administrator has privileges on
        - authenticationMethod (string): The method of authentication the user will use to sign in to the Meraki dashboard. Can be one of 'Email' or 'Cisco SecureX Sign-On'. The default is Email authentication
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['enterprise', 'full', 'none', 'read-only']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''
        if 'authenticationMethod' in kwargs:
            options = ['Cisco SecureX Sign-On', 'Email']
            assert kwargs['authenticationMethod'] in options, f'''"authenticationMethod" cannot be "{kwargs['authenticationMethod']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'createOrganizationAdmin'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/admins'

        body_params = ['email', 'name', 'orgAccess', 'tags', 'networks', 'authenticationMethod', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateOrganizationAdmin(self, organizationId: str, adminId: str, **kwargs):
        """
        **Update an administrator**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-admin

        - organizationId (string): (required)
        - adminId (string): (required)
        - name (string): The name of the dashboard administrator
        - orgAccess (string): The privilege of the dashboard administrator on the organization. Can be one of 'full', 'read-only', 'enterprise' or 'none'
        - tags (array): The list of tags that the dashboard administrator has privileges on
        - networks (array): The list of networks that the dashboard administrator has privileges on
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['enterprise', 'full', 'none', 'read-only']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'updateOrganizationAdmin'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        adminId = urllib.parse.quote(str(adminId), safe='')
        resource = f'/organizations/{organizationId}/admins/{adminId}'

        body_params = ['name', 'orgAccess', 'tags', 'networks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationAdmin(self, organizationId: str, adminId: str):
        """
        **Revoke all access for a dashboard administrator within this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin

        - organizationId (string): (required)
        - adminId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'deleteOrganizationAdmin'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        adminId = urllib.parse.quote(str(adminId), safe='')
        resource = f'/organizations/{organizationId}/admins/{adminId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationAlertsProfiles(self, organizationId: str):
        """
        **List all organization-wide alert configurations**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-alerts-profiles

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'alerts', 'profiles'],
            'operation': 'getOrganizationAlertsProfiles'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/alerts/profiles'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/alerts/profiles'

        body_params = ['type', 'alertCondition', 'recipients', 'networkTags', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        alertConfigId = urllib.parse.quote(str(alertConfigId), safe='')
        resource = f'/organizations/{organizationId}/alerts/profiles/{alertConfigId}'

        body_params = ['enabled', 'type', 'alertCondition', 'recipients', 'networkTags', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        alertConfigId = urllib.parse.quote(str(alertConfigId), safe='')
        resource = f'/organizations/{organizationId}/alerts/profiles/{alertConfigId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationApiRequests(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the API requests made by an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - adminId (string): Filter the results by the ID of the admin who made the API requests
        - path (string): Filter the results by the path of the API requests
        - method (string): Filter the results by the method of the API requests (must be 'GET', 'PUT', 'POST' or 'DELETE')
        - responseCode (integer): Filter the results by the response code of the API requests
        - sourceIp (string): Filter the results by the IP address of the originating API request
        - userAgent (string): Filter the results by the user agent string of the API request
        - version (integer): Filter the results by the API version of the API request
        - operationIds (array): Filter the results by one or more operation IDs for the API request
        """

        kwargs.update(locals())

        if 'method' in kwargs:
            options = ['DELETE', 'GET', 'POST', 'PUT']
            assert kwargs['method'] in options, f'''"method" cannot be "{kwargs['method']}", & must be set to one of: {options}'''
        if 'version' in kwargs:
            options = [0, 1]
            assert kwargs['version'] in options, f'''"version" cannot be "{kwargs['version']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'apiRequests'],
            'operation': 'getOrganizationApiRequests'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/apiRequests'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', 'userAgent', 'version', 'operationIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['operationIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationApiRequestsOverview(self, organizationId: str, **kwargs):
        """
        **Return an aggregated overview of API requests data**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'apiRequests', 'overview'],
            'operation': 'getOrganizationApiRequestsOverview'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/apiRequests/overview'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationApiRequestsOverviewResponseCodesByInterval(self, organizationId: str, **kwargs):
        """
        **Tracks organizations' API requests by response code across a given time period**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview-response-codes-by-interval

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
        - interval (integer): The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
        - version (integer): Filter by API version of the endpoint. Allowable values are: [0, 1]
        - operationIds (array): Filter by operation ID of the endpoint
        - sourceIps (array): Filter by source IP that made the API request
        - adminIds (array): Filter by admin ID of user that made the API request
        - userAgent (string): Filter by user agent string for API request. This will filter by a complete or partial match.
        """

        kwargs.update(locals())

        if 'version' in kwargs:
            options = [0, 1]
            assert kwargs['version'] in options, f'''"version" cannot be "{kwargs['version']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'apiRequests', 'overview', 'responseCodes', 'byInterval'],
            'operation': 'getOrganizationApiRequestsOverviewResponseCodesByInterval'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval'

        query_params = ['t0', 't1', 'timespan', 'interval', 'version', 'operationIds', 'sourceIps', 'adminIds', 'userAgent', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['operationIds', 'sourceIps', 'adminIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationBrandingPolicies(self, organizationId: str):
        """
        **List the branding policies of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'getOrganizationBrandingPolicies'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings', 'customLogo', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationBrandingPoliciesPriorities(self, organizationId: str):
        """
        **Return the branding policy IDs of an organization in priority order**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies', 'priorities'],
            'operation': 'getOrganizationBrandingPoliciesPriorities'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        body_params = ['brandingPolicyIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Return a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy

        - organizationId (string): (required)
        - brandingPolicyId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'getOrganizationBrandingPolicy'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        brandingPolicyId = urllib.parse.quote(str(brandingPolicyId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        brandingPolicyId = urllib.parse.quote(str(brandingPolicyId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings', 'customLogo', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        brandingPolicyId = urllib.parse.quote(str(brandingPolicyId), safe='')
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        return self._session.delete(metadata, resource)
        


    def claimIntoOrganization(self, organizationId: str, **kwargs):
        """
        **Claim a list of devices, licenses, and/or orders into an organization**
        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization

        - organizationId (string): (required)
        - orders (array): The numbers of the orders that should be claimed
        - serials (array): The serials of the devices that should be claimed
        - licenses (array): The licenses that should be claimed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'claimIntoOrganization'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/claim'

        body_params = ['orders', 'serials', 'licenses', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationClientsBandwidthUsageHistory(self, organizationId: str, **kwargs):
        """
        **Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-bandwidth-usage-history

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'clients', 'bandwidthUsageHistory'],
            'operation': 'getOrganizationClientsBandwidthUsageHistory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/clients/bandwidthUsageHistory'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationClientsOverview(self, organizationId: str, **kwargs):
        """
        **Return summary information around client data usage (in mb) across the given organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-overview

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'clients', 'overview'],
            'operation': 'getOrganizationClientsOverview'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/clients/overview'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationClientsSearch(self, organizationId: str, mac: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the client details in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-clients-search

        - organizationId (string): (required)
        - mac (string): The MAC address of the client. Required.
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'clients', 'search'],
            'operation': 'getOrganizationClientsSearch'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/clients/search'

        query_params = ['mac', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def cloneOrganization(self, organizationId: str, name: str):
        """
        **Create a new organization by cloning the addressed organization**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization

        - organizationId (string): (required)
        - name (string): The name of the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'cloneOrganization'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/clone'

        body_params = ['name', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationConfigTemplates(self, organizationId: str):
        """
        **List the configuration templates for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'getOrganizationConfigTemplates'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates'

        body_params = ['name', 'timeZone', 'copyFromNetworkId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        body_params = ['name', 'timeZone', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Remove a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template

        - organizationId (string): (required)
        - configTemplateId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'deleteOrganizationConfigTemplate'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Return a single configuration template**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template

        - organizationId (string): (required)
        - configTemplateId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'getOrganizationConfigTemplate'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        configTemplateId = urllib.parse.quote(str(configTemplateId), safe='')
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        return self._session.get(metadata, resource)
        


    def getOrganizationConfigurationChanges(self, organizationId: str, total_pages=1, direction='prev', **kwargs):
        """
        **View the Change Log for your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" or "prev" (default) page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 365 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 5000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkId (string): Filters on the given network
        - adminId (string): Filters on the given Admin
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'configurationChanges'],
            'operation': 'getOrganizationConfigurationChanges'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/configurationChanges'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationDevices(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Filter results by whether or not the device's configuration has been updated after the given timestamp
        - networkIds (array): Optional parameter to filter devices by network.
        - productTypes (array): Optional parameter to filter devices by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
        - tags (array): Optional parameter to filter devices by tags.
        - tagsFilterType (string): Optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - name (string): Optional parameter to filter devices by name. All returned devices will have a name that contains the search term or is an exact match.
        - mac (string): Optional parameter to filter devices by MAC address. All returned devices will have a MAC address that contains the search term or is an exact match.
        - serial (string): Optional parameter to filter devices by serial number. All returned devices will have a serial number that contains the search term or is an exact match.
        - model (string): Optional parameter to filter devices by model. All returned devices will have a model that contains the search term or is an exact match.
        - macs (array): Optional parameter to filter devices by one or more MAC addresses. All returned devices will have a MAC address that is an exact match.
        - serials (array): Optional parameter to filter devices by one or more serial numbers. All returned devices will have a serial number that is an exact match.
        - sensorMetrics (array): Optional parameter to filter devices by the metrics that they provide. Only applies to sensor devices.
        - sensorAlertProfileIds (array): Optional parameter to filter devices by the alert profiles that are bound to them. Only applies to sensor devices.
        - models (array): Optional parameter to filter devices by one or more models. All returned devices will have a model that is an exact match.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'devices'],
            'operation': 'getOrganizationDevices'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', 'networkIds', 'productTypes', 'tags', 'tagsFilterType', 'name', 'mac', 'serial', 'model', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'productTypes', 'tags', 'macs', 'serials', 'sensorMetrics', 'sensorAlertProfileIds', 'models', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationDevicesAvailabilities(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the availability information for devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-availabilities

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'availabilities'],
            'operation': 'getOrganizationDevicesAvailabilities'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices/availabilities'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'productTypes', 'serials', 'tags', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationDevicesPowerModulesStatusesByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the power status information for devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-power-modules-statuses-by-device

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device availabilities by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device availabilities by device product types. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'powerModules', 'statuses', 'byDevice'],
            'operation': 'getOrganizationDevicesPowerModulesStatusesByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices/powerModules/statuses/byDevice'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'productTypes', 'serials', 'tags', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationDevicesStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the status of every Meraki device in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter devices by network ids.
        - serials (array): Optional parameter to filter devices by serials.
        - statuses (array): Optional parameter to filter devices by statuses. Valid statuses are ["online", "alerting", "offline", "dormant"].
        - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
        - models (array): Optional parameter to filter devices by models.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'statuses'],
            'operation': 'getOrganizationDevicesStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', 'tagsFilterType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'statuses', 'productTypes', 'models', 'tags', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationDevicesStatusesOverview(self, organizationId: str, **kwargs):
        """
        **Return an overview of current device statuses**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses-overview

        - organizationId (string): (required)
        - productTypes (array): An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
        - networkIds (array): An optional parameter to filter device statuses by network.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'statuses', 'overview'],
            'operation': 'getOrganizationDevicesStatusesOverview'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices/statuses/overview'

        query_params = ['productTypes', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['productTypes', 'networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationDevicesUplinksAddressesByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the current uplink addresses for devices in an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-addresses-by-device

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter device uplinks by network ID. This filter uses multiple exact matches.
        - productTypes (array): Optional parameter to filter device uplinks by device product types. This filter uses multiple exact matches.
        - serials (array): Optional parameter to filter device availabilities by device serial numbers. This filter uses multiple exact matches.
        - tags (array): An optional parameter to filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below). This filter uses multiple exact matches.
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return devices which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'uplinks', 'addresses', 'byDevice'],
            'operation': 'getOrganizationDevicesUplinksAddressesByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices/uplinks/addresses/byDevice'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'productTypes', 'serials', 'tags', 'tagsFilterType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'productTypes', 'serials', 'tags', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationDevicesUplinksLossAndLatency(self, organizationId: str, **kwargs):
        """
        **Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 60 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
        - uplink (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
        - ip (string): Optional filter for a specific destination IP. Default will return all destination IPs.
        """

        kwargs.update(locals())

        if 'uplink' in kwargs:
            options = ['cellular', 'wan1', 'wan2']
            assert kwargs['uplink'] in options, f'''"uplink" cannot be "{kwargs['uplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'uplinks', 'uplinksLossAndLatency'],
            'operation': 'getOrganizationDevicesUplinksLossAndLatency'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/devices/uplinksLossAndLatency'

        query_params = ['t0', 't1', 'timespan', 'uplink', 'ip', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationEarlyAccessFeatures(self, organizationId: str):
        """
        **List the available early access features for organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'earlyAccess', 'features'],
            'operation': 'getOrganizationEarlyAccessFeatures'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/earlyAccess/features'

        return self._session.get(metadata, resource)
        


    def getOrganizationEarlyAccessFeaturesOptIns(self, organizationId: str):
        """
        **List the early access feature opt-ins for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-ins

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'earlyAccess', 'features', 'optIns'],
            'operation': 'getOrganizationEarlyAccessFeaturesOptIns'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/earlyAccess/features/optIns'

        return self._session.get(metadata, resource)
        


    def createOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, shortName: str, **kwargs):
        """
        **Create a new early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-early-access-features-opt-in

        - organizationId (string): (required)
        - shortName (string): Short name of the early access feature
        - limitScopeToNetworks (array): A list of network IDs to apply the opt-in to
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'earlyAccess', 'features', 'optIns'],
            'operation': 'createOrganizationEarlyAccessFeaturesOptIn'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/earlyAccess/features/optIns'

        body_params = ['shortName', 'limitScopeToNetworks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str):
        """
        **Show an early access feature opt-in for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-early-access-features-opt-in

        - organizationId (string): (required)
        - optInId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'earlyAccess', 'features', 'optIns'],
            'operation': 'getOrganizationEarlyAccessFeaturesOptIn'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        optInId = urllib.parse.quote(str(optInId), safe='')
        resource = f'/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        optInId = urllib.parse.quote(str(optInId), safe='')
        resource = f'/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}'

        body_params = ['limitScopeToNetworks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationEarlyAccessFeaturesOptIn(self, organizationId: str, optInId: str):
        """
        **Delete an early access feature opt-in**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-early-access-features-opt-in

        - organizationId (string): (required)
        - optInId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'earlyAccess', 'features', 'optIns'],
            'operation': 'deleteOrganizationEarlyAccessFeaturesOptIn'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        optInId = urllib.parse.quote(str(optInId), safe='')
        resource = f'/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationFirmwareUpgrades(self, organizationId: str, **kwargs):
        """
        **Get firmware upgrade information for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades

        - organizationId (string): (required)
        - status (array): The status of an upgrade 
        - productType (array): The product type in a given upgrade ID
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'firmware', 'upgrades'],
            'operation': 'getOrganizationFirmwareUpgrades'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/firmware/upgrades'

        query_params = ['status', 'productType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['status', 'productType', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationFirmwareUpgradesByDevice(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Get firmware upgrade status for the filtered devices**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-firmware-upgrades-by-device

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter by network
        - serials (array): Optional parameter to filter by serial number.  All returned devices will have a serial number that is an exact match.
        - macs (array): Optional parameter to filter by one or more MAC addresses belonging to devices. All devices returned belong to MAC addresses that are an exact match.
        - firmwareUpgradeIds (array): Optional parameter to filter by firmware upgrade ids.
        - firmwareUpgradeBatchIds (array): Optional parameter to filter by firmware upgrade batch ids.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'firmware', 'upgrades', 'byDevice'],
            'operation': 'getOrganizationFirmwareUpgradesByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/firmware/upgrades/byDevice'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'macs', 'firmwareUpgradeIds', 'firmwareUpgradeBatchIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'macs', 'firmwareUpgradeIds', 'firmwareUpgradeBatchIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def claimIntoOrganizationInventory(self, organizationId: str, **kwargs):
        """
        **Claim a list of devices, licenses, and/or orders into an organization inventory**
        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization-inventory

        - organizationId (string): (required)
        - orders (array): The numbers of the orders that should be claimed
        - serials (array): The serials of the devices that should be claimed
        - licenses (array): The licenses that should be claimed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'inventory'],
            'operation': 'claimIntoOrganizationInventory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/claim'

        body_params = ['orders', 'serials', 'licenses', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationInventoryDevices(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the device inventory for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - usedState (string): Filter results by used or unused inventory. Accepted values are 'used' or 'unused'.
        - search (string): Search for devices in inventory based on serial number, mac address, or model.
        - macs (array): Search for devices in inventory based on mac addresses.
        - networkIds (array): Search for devices in inventory based on network ids.
        - serials (array): Search for devices in inventory based on serials.
        - models (array): Search for devices in inventory based on model.
        - orderNumbers (array): Search for devices in inventory based on order numbers.
        - tags (array): Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'.
        - productTypes (array): Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
        """

        kwargs.update(locals())

        if 'usedState' in kwargs:
            options = ['unused', 'used']
            assert kwargs['usedState'] in options, f'''"usedState" cannot be "{kwargs['usedState']}", & must be set to one of: {options}'''
        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'devices'],
            'operation': 'getOrganizationInventoryDevices'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/devices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', 'macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'tagsFilterType', 'productTypes', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['macs', 'networkIds', 'serials', 'models', 'orderNumbers', 'tags', 'productTypes', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationInventoryDevice(self, organizationId: str, serial: str):
        """
        **Return a single device from the inventory of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

        - organizationId (string): (required)
        - serial (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'devices'],
            'operation': 'getOrganizationInventoryDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/organizations/{organizationId}/inventory/devices/{serial}'

        return self._session.get(metadata, resource)
        


    def createOrganizationInventoryOnboardingCloudMonitoringExportEvent(self, organizationId: str, logEvent: str, timestamp: int, **kwargs):
        """
        **Imports event logs related to the onboarding app into elastisearch**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-export-event

        - organizationId (string): (required)
        - logEvent (string): The type of log event this is recording, e.g. download or opening a banner
        - timestamp (integer): A JavaScript UTC datetime stamp for when the even occurred
        - targetOS (string): The name of the onboarding distro being downloaded
        - request (string): Used to describe if this event was the result of a redirect. E.g. a query param if an info banner is being used
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'onboarding', 'cloudMonitoring', 'exportEvents'],
            'operation': 'createOrganizationInventoryOnboardingCloudMonitoringExportEvent'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents'

        body_params = ['logEvent', 'timestamp', 'targetOS', 'request', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def createOrganizationInventoryOnboardingCloudMonitoringImport(self, organizationId: str, devices: list):
        """
        **Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-import

        - organizationId (string): (required)
        - devices (array): A set of device imports to commit
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'onboarding', 'cloudMonitoring', 'imports'],
            'operation': 'createOrganizationInventoryOnboardingCloudMonitoringImport'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports'

        body_params = ['devices', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationInventoryOnboardingCloudMonitoringImports(self, organizationId: str, importIds: list):
        """
        **Check the status of a committed Import operation**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-imports

        - organizationId (string): (required)
        - importIds (array): import ids from an imports
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'onboarding', 'cloudMonitoring', 'imports'],
            'operation': 'getOrganizationInventoryOnboardingCloudMonitoringImports'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports'

        query_params = ['importIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['importIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationInventoryOnboardingCloudMonitoringNetworks(self, organizationId: str, deviceType: str, total_pages=1, direction='next', **kwargs):
        """
        **Returns list of networks eligible for adding cloud monitored device**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-onboarding-cloud-monitoring-networks

        - organizationId (string): (required)
        - deviceType (string): Device Type switch or wireless controller
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if 'deviceType' in kwargs:
            options = ['switch', 'wireless_controller']
            assert kwargs['deviceType'] in options, f'''"deviceType" cannot be "{kwargs['deviceType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'onboarding', 'cloudMonitoring', 'networks'],
            'operation': 'getOrganizationInventoryOnboardingCloudMonitoringNetworks'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks'

        query_params = ['deviceType', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def createOrganizationInventoryOnboardingCloudMonitoringPrepare(self, organizationId: str, devices: list):
        """
        **Initiates or updates an import session**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-prepare

        - organizationId (string): (required)
        - devices (array): A set of devices to import (or update)
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'inventory', 'onboarding', 'cloudMonitoring', 'prepare'],
            'operation': 'createOrganizationInventoryOnboardingCloudMonitoringPrepare'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare'

        body_params = ['devices', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def releaseFromOrganizationInventory(self, organizationId: str, **kwargs):
        """
        **Release a list of claimed devices from an organization.**
        https://developer.cisco.com/meraki/api-v1/#!release-from-organization-inventory

        - organizationId (string): (required)
        - serials (array): Serials of the devices that should be released
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'inventory'],
            'operation': 'releaseFromOrganizationInventory'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/inventory/release'

        body_params = ['serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationLicenses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the licenses for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - deviceSerial (string): Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
        - networkId (string): Filter the licenses to those assigned in a particular network
        - state (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'
        """

        kwargs.update(locals())

        if 'state' in kwargs:
            options = ['active', 'expired', 'expiring', 'recentlyQueued', 'unused', 'unusedActive']
            assert kwargs['state'] in options, f'''"state" cannot be "{kwargs['state']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'getOrganizationLicenses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licenses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licenses/assignSeats'

        body_params = ['licenseId', 'networkId', 'seatCount', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licenses/move'

        body_params = ['destOrganizationId', 'licenseIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licenses/moveSeats'

        body_params = ['destOrganizationId', 'licenseId', 'seatCount', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationLicensesOverview(self, organizationId: str):
        """
        **Return an overview of the license state for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'monitor', 'licenses', 'overview'],
            'operation': 'getOrganizationLicensesOverview'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licenses/overview'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licenses/renewSeats'

        body_params = ['licenseIdToRenew', 'unusedLicenseId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationLicense(self, organizationId: str, licenseId: str):
        """
        **Display a license**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-license

        - organizationId (string): (required)
        - licenseId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'getOrganizationLicense'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        licenseId = urllib.parse.quote(str(licenseId), safe='')
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        licenseId = urllib.parse.quote(str(licenseId), safe='')
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        body_params = ['deviceSerial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationLoginSecurity(self, organizationId: str):
        """
        **Returns the login security settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-login-security

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'loginSecurity'],
            'operation': 'getOrganizationLoginSecurity'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/loginSecurity'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/loginSecurity'

        body_params = ['enforcePasswordExpiration', 'passwordExpirationDays', 'enforceDifferentPasswords', 'numDifferentPasswords', 'enforceStrongPasswords', 'enforceAccountLockout', 'accountLockoutAttempts', 'enforceIdleTimeout', 'idleTimeoutMinutes', 'enforceTwoFactorAuth', 'enforceLoginIpRanges', 'loginIpRanges', 'apiAuthentication', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationNetworks(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the networks that the user has privileges on in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - configTemplateId (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template.
        - isBoundToConfigTemplate (boolean): An optional parameter to filter config template bound networks. If configTemplateId is set, this cannot be false.
        - tags (array): An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAllTags', 'withAnyTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'getOrganizationNetworks'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/networks'

        query_params = ['configTemplateId', 'isBoundToConfigTemplate', 'tags', 'tagsFilterType', 'perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['tags', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/networks'

        body_params = ['name', 'productTypes', 'tags', 'timeZone', 'copyFromNetworkId', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/networks/combine'

        body_params = ['name', 'networkIds', 'enrollmentString', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationOpenapiSpec(self, organizationId: str):
        """
        **Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'monitor', 'openapiSpec'],
            'operation': 'getOrganizationOpenapiSpec'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/openapiSpec'

        return self._session.get(metadata, resource)
        


    def getOrganizationPolicyObjects(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Lists Policy Objects belonging to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 5000. Default is 5000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects'],
            'operation': 'getOrganizationPolicyObjects'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects'

        body_params = ['name', 'category', 'type', 'cidr', 'fqdn', 'mask', 'ip', 'groupIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationPolicyObjectsGroups(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Lists Policy Object Groups belonging to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-groups

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 10 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects', 'groups'],
            'operation': 'getOrganizationPolicyObjectsGroups'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/groups'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/groups'

        body_params = ['name', 'category', 'objectIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationPolicyObjectsGroup(self, organizationId: str, policyObjectGroupId: str):
        """
        **Shows details of a Policy Object Group.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-objects-group

        - organizationId (string): (required)
        - policyObjectGroupId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects', 'groups'],
            'operation': 'getOrganizationPolicyObjectsGroup'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        policyObjectGroupId = urllib.parse.quote(str(policyObjectGroupId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        policyObjectGroupId = urllib.parse.quote(str(policyObjectGroupId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}'

        body_params = ['name', 'objectIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        policyObjectGroupId = urllib.parse.quote(str(policyObjectGroupId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationPolicyObject(self, organizationId: str, policyObjectId: str):
        """
        **Shows details of a Policy Object.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-policy-object

        - organizationId (string): (required)
        - policyObjectId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'policyObjects'],
            'operation': 'getOrganizationPolicyObject'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        policyObjectId = urllib.parse.quote(str(policyObjectId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/{policyObjectId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        policyObjectId = urllib.parse.quote(str(policyObjectId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/{policyObjectId}'

        body_params = ['name', 'cidr', 'fqdn', 'mask', 'ip', 'groupIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        policyObjectId = urllib.parse.quote(str(policyObjectId), safe='')
        resource = f'/organizations/{organizationId}/policyObjects/{policyObjectId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationSaml(self, organizationId: str):
        """
        **Returns the SAML SSO enabled settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'saml'],
            'operation': 'getOrganizationSaml'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/saml'

        return self._session.get(metadata, resource)
        


    def updateOrganizationSaml(self, organizationId: str, **kwargs):
        """
        **Updates the SAML SSO enabled settings for an organization.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml

        - organizationId (string): (required)
        - enabled (boolean): Boolean for updating SAML SSO enabled settings.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'saml'],
            'operation': 'updateOrganizationSaml'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/saml'

        body_params = ['enabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationSamlIdps(self, organizationId: str):
        """
        **List the SAML IdPs in your organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idps

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'getOrganizationSamlIdps'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/saml/idps'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/saml/idps'

        body_params = ['x509certSha1Fingerprint', 'sloLogoutUrl', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        idpId = urllib.parse.quote(str(idpId), safe='')
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        body_params = ['x509certSha1Fingerprint', 'sloLogoutUrl', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationSamlIdp(self, organizationId: str, idpId: str):
        """
        **Get a SAML IdP from your organization.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-idp

        - organizationId (string): (required)
        - idpId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'saml', 'idps'],
            'operation': 'getOrganizationSamlIdp'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        idpId = urllib.parse.quote(str(idpId), safe='')
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        return self._session.get(metadata, resource)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        idpId = urllib.parse.quote(str(idpId), safe='')
        resource = f'/organizations/{organizationId}/saml/idps/{idpId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationSamlRoles(self, organizationId: str):
        """
        **List the SAML roles for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'getOrganizationSamlRoles'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/samlRoles'

        return self._session.get(metadata, resource)
        


    def createOrganizationSamlRole(self, organizationId: str, role: str, orgAccess: str, **kwargs):
        """
        **Create a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

        - organizationId (string): (required)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only', 'full' or 'enterprise'
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['enterprise', 'full', 'none', 'read-only']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'createOrganizationSamlRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/samlRoles'

        body_params = ['role', 'orgAccess', 'tags', 'networks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Return a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role

        - organizationId (string): (required)
        - samlRoleId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'getOrganizationSamlRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        samlRoleId = urllib.parse.quote(str(samlRoleId), safe='')
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return self._session.get(metadata, resource)
        


    def updateOrganizationSamlRole(self, organizationId: str, samlRoleId: str, **kwargs):
        """
        **Update a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

        - organizationId (string): (required)
        - samlRoleId (string): (required)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only', 'full' or 'enterprise'
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['enterprise', 'full', 'none', 'read-only']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'updateOrganizationSamlRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        samlRoleId = urllib.parse.quote(str(samlRoleId), safe='')
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        body_params = ['role', 'orgAccess', 'tags', 'networks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Remove a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role

        - organizationId (string): (required)
        - samlRoleId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'deleteOrganizationSamlRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        samlRoleId = urllib.parse.quote(str(samlRoleId), safe='')
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationSnmp(self, organizationId: str):
        """
        **Return the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'snmp'],
            'operation': 'getOrganizationSnmp'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/snmp'

        return self._session.get(metadata, resource)
        


    def updateOrganizationSnmp(self, organizationId: str, **kwargs):
        """
        **Update the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp

        - organizationId (string): (required)
        - v2cEnabled (boolean): Boolean indicating whether SNMP version 2c is enabled for the organization.
        - v3Enabled (boolean): Boolean indicating whether SNMP version 3 is enabled for the organization.
        - v3AuthMode (string): The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
        - v3AuthPass (string): The SNMP version 3 authentication password. Must be at least 8 characters if specified.
        - v3PrivMode (string): The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
        - v3PrivPass (string): The SNMP version 3 privacy password. Must be at least 8 characters if specified.
        - peerIps (array): The list of IPv4 addresses that are allowed to access the SNMP server.
        """

        kwargs.update(locals())

        if 'v3AuthMode' in kwargs:
            options = ['MD5', 'SHA']
            assert kwargs['v3AuthMode'] in options, f'''"v3AuthMode" cannot be "{kwargs['v3AuthMode']}", & must be set to one of: {options}'''
        if 'v3PrivMode' in kwargs:
            options = ['AES128', 'DES']
            assert kwargs['v3PrivMode'] in options, f'''"v3PrivMode" cannot be "{kwargs['v3PrivMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'snmp'],
            'operation': 'updateOrganizationSnmp'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/snmp'

        body_params = ['v2cEnabled', 'v3Enabled', 'v3AuthMode', 'v3AuthPass', 'v3PrivMode', 'v3PrivPass', 'peerIps', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationSummaryTopAppliancesByUtilization(self, organizationId: str, **kwargs):
        """
        **Return the top 10 appliances sorted by utilization over given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-appliances-by-utilization

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'appliances', 'byUtilization'],
            'operation': 'getOrganizationSummaryTopAppliancesByUtilization'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/appliances/byUtilization'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSummaryTopClientsByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 clients by data usage (in mb) over given time range.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-by-usage

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'clients', 'byUsage'],
            'operation': 'getOrganizationSummaryTopClientsByUsage'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/clients/byUsage'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSummaryTopClientsManufacturersByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-clients-manufacturers-by-usage

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'clients', 'manufacturers', 'byUsage'],
            'operation': 'getOrganizationSummaryTopClientsManufacturersByUsage'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/clients/manufacturers/byUsage'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSummaryTopDevicesByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 devices sorted by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-by-usage

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'devices', 'byUsage'],
            'operation': 'getOrganizationSummaryTopDevicesByUsage'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/devices/byUsage'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSummaryTopDevicesModelsByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 device models sorted by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-devices-models-by-usage

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'devices', 'models', 'byUsage'],
            'operation': 'getOrganizationSummaryTopDevicesModelsByUsage'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/devices/models/byUsage'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSummaryTopSsidsByUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 ssids by data usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-ssids-by-usage

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'ssids', 'byUsage'],
            'operation': 'getOrganizationSummaryTopSsidsByUsage'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/ssids/byUsage'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationSummaryTopSwitchesByEnergyUsage(self, organizationId: str, **kwargs):
        """
        **Return metrics for organization's top 10 switches by energy usage over given time range**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-summary-top-switches-by-energy-usage

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'summary', 'top', 'switches', 'byEnergyUsage'],
            'operation': 'getOrganizationSummaryTopSwitchesByEnergyUsage'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/summary/top/switches/byEnergyUsage'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationUplinksStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the uplink status of every Meraki MX, MG and Z series devices in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-uplinks-statuses

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'uplinks', 'statuses'],
            'operation': 'getOrganizationUplinksStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/uplinks/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'iccids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


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
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        userId = urllib.parse.quote(str(userId), safe='')
        resource = f'/organizations/{organizationId}/users/{userId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationWebhooksAlertTypes(self, organizationId: str, **kwargs):
        """
        **Return a list of alert types to be used with managing webhook alerts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

        - organizationId (string): (required)
        - productType (string): Filter sample alerts to a specific product type
        """

        kwargs.update(locals())

        if 'productType' in kwargs:
            options = ['appliance', 'camera', 'cellularGateway', 'health', 'platform', 'sensor', 'sm', 'switch', 'wireless']
            assert kwargs['productType'] in options, f'''"productType" cannot be "{kwargs['productType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'webhooks', 'alertTypes'],
            'operation': 'getOrganizationWebhooksAlertTypes'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/webhooks/alertTypes'

        query_params = ['productType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationWebhooksLogs(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the log of webhook POSTs sent**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-logs

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - url (string): The URL the webhook was sent to
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'webhooks', 'logs'],
            'operation': 'getOrganizationWebhooksLogs'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/webhooks/logs'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
