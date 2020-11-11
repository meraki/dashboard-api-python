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

    def createOrganization(self, name: str):
        """
        **Create a new organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization

        - name (string): The name of the organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'createOrganization'
        }
        resource = f'/organizations'

        body_params = ['name', ]
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
        resource = f'/organizations/{organizationId}'

        return self._session.get(metadata, resource)

    def updateOrganization(self, organizationId: str, **kwargs):
        """
        **Update an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization

        - organizationId (string): (required)
        - name (string): The name of the organization
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'updateOrganization'
        }
        resource = f'/organizations/{organizationId}'

        body_params = ['name', ]
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
            options = ['pending', 'completed', 'failed']
            assert kwargs['status'] in options, f'''"status" cannot be "{kwargs['status']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'getOrganizationActionBatches'
        }
        resource = f'/organizations/{organizationId}/actionBatches'

        query_params = ['status', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

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
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return self._session.get(metadata, resource)

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
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        body_params = ['confirmed', 'synchronous', ]
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
            options = ['full', 'read-only', 'enterprise', 'none']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''
        if 'authenticationMethod' in kwargs:
            options = ['Email', 'Cisco SecureX Sign-On']
            assert kwargs['authenticationMethod'] in options, f'''"authenticationMethod" cannot be "{kwargs['authenticationMethod']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'createOrganizationAdmin'
        }
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
            options = ['full', 'read-only', 'enterprise', 'none']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'updateOrganizationAdmin'
        }
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
        resource = f'/organizations/{organizationId}/admins/{adminId}'

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
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'apiRequests'],
            'operation': 'getOrganizationApiRequests'
        }
        resource = f'/organizations/{organizationId}/apiRequests'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

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
        resource = f'/organizations/{organizationId}/apiRequests/overview'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

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
        resource = f'/organizations/{organizationId}/brandingPolicies'

        return self._session.get(metadata, resource)

    def createOrganizationBrandingPolicy(self, organizationId: str, name: str, enabled: bool, adminSettings: dict, **kwargs):
        """
        **Add a new branding policy to an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy

        - organizationId (string): (required)
        - name (string): Name of the Dashboard branding policy.
        - enabled (boolean): Boolean indicating whether this policy is enabled.
        - adminSettings (object): Settings for describing which kinds of admins this policy applies to.
        - helpSettings (object):     Settings for describing the modifications to various Help page features. Each property in this object accepts one of
    'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
    the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
    Dashboard; see the documentation for each property to see the allowed values.
 Each property defaults to 'default or inherit' when not provided.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'createOrganizationBrandingPolicy'
        }
        resource = f'/organizations/{organizationId}/brandingPolicies'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings', ]
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
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        return self._session.get(metadata, resource)

    def updateOrganizationBrandingPoliciesPriorities(self, organizationId: str, brandingPolicyIds: list):
        """
        **Update the priority ordering of an organization's branding policies.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities

        - organizationId (string): (required)
        - brandingPolicyIds (array): A list of branding policy IDs arranged in ascending priority order (IDs later in the array have higher priority).
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies', 'priorities'],
            'operation': 'updateOrganizationBrandingPoliciesPriorities'
        }
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
        - helpSettings (object):     Settings for describing the modifications to various Help page features. Each property in this object accepts one of
    'default or inherit' (do not modify functionality), 'hide' (remove the section from Dashboard), or 'show' (always show
    the section on Dashboard). Some properties in this object also accept custom HTML used to replace the section on
    Dashboard; see the documentation for each property to see the allowed values.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'updateOrganizationBrandingPolicy'
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings', ]
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
        resource = f'/organizations/{organizationId}/claim'

        body_params = ['orders', 'serials', 'licenses', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

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
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'devices'],
            'operation': 'getOrganizationDevices'
        }
        resource = f'/organizations/{organizationId}/devices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

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
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'statuses'],
            'operation': 'getOrganizationDevicesStatuses'
        }
        resource = f'/organizations/{organizationId}/devices/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationDevicesUplinksLossAndLatency(self, organizationId: str, **kwargs):
        """
        **Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency

        - organizationId (string): (required)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
        - uplink (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
        - ip (string): Optional filter for a specific destination IP. Default will return all destination IPs.
        """

        kwargs.update(locals())

        if 'uplink' in kwargs:
            options = ['wan1', 'wan2', 'cellular']
            assert kwargs['uplink'] in options, f'''"uplink" cannot be "{kwargs['uplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'uplinksLossAndLatency'],
            'operation': 'getOrganizationDevicesUplinksLossAndLatency'
        }
        resource = f'/organizations/{organizationId}/devices/uplinksLossAndLatency'

        query_params = ['t0', 't1', 'timespan', 'uplink', 'ip', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

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
        - usedState (string): Filter results by used or unused inventory. Accepted values are "used" or "unused".
        - search (string): Search for devices in inventory based on serial number, mac address, or model.
        """

        kwargs.update(locals())

        if 'usedState' in kwargs:
            options = ['used', 'unused']
            assert kwargs['usedState'] in options, f'''"usedState" cannot be "{kwargs['usedState']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'inventoryDevices'],
            'operation': 'getOrganizationInventoryDevices'
        }
        resource = f'/organizations/{organizationId}/inventoryDevices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'usedState', 'search', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def getOrganizationInventoryDevice(self, organizationId: str, serial: str):
        """
        **Return a single device from the inventory of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-device

        - organizationId (string): (required)
        - serial (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'inventoryDevices'],
            'operation': 'getOrganizationInventoryDevice'
        }
        resource = f'/organizations/{organizationId}/inventoryDevices/{serial}'

        return self._session.get(metadata, resource)

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
        - deviceSerial (string): Filter the licenses to those assigned to a particular device
        - networkId (string): Filter the licenses to those assigned in a particular network
        - state (string): Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'unused', 'unusedActive' or 'recentlyQueued'
        """

        kwargs.update(locals())

        if 'state' in kwargs:
            options = ['active', 'expired', 'expiring', 'unused', 'unusedActive', 'recentlyQueued']
            assert kwargs['state'] in options, f'''"state" cannot be "{kwargs['state']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'getOrganizationLicenses'
        }
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
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        return self._session.get(metadata, resource)

    def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-license

        - organizationId (string): (required)
        - licenseId (string): (required)
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'updateOrganizationLicense'
        }
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
        - enforceTwoFactorAuth (boolean): Boolean indicating whether users in this organization will be required to use an extra verification code when logging in to Dashboard. This code will be sent to their mobile phone via SMS, or can be generated by the Google Authenticator application.
        - enforceLoginIpRanges (boolean): Boolean indicating whether organization will restrict access to Dashboard (including the API) from certain IP addresses.
        - loginIpRanges (array): List of acceptable IP ranges. Entries can be single IP addresses, IP address ranges, and CIDR subnets.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'loginSecurity'],
            'operation': 'updateOrganizationLoginSecurity'
        }
        resource = f'/organizations/{organizationId}/loginSecurity'

        body_params = ['enforcePasswordExpiration', 'passwordExpirationDays', 'enforceDifferentPasswords', 'numDifferentPasswords', 'enforceStrongPasswords', 'enforceAccountLockout', 'accountLockoutAttempts', 'enforceIdleTimeout', 'idleTimeoutMinutes', 'enforceTwoFactorAuth', 'enforceLoginIpRanges', 'loginIpRanges', ]
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
        - tags (array): An optional parameter to filter networks by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
        - tagsFilterType (string): An optional parameter of value 'withAnyTags' or 'withAllTags' to indicate whether to return networks which contain ANY or ALL of the included tags. If no type is included, 'withAnyTags' will be selected.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        if 'tagsFilterType' in kwargs:
            options = ['withAnyTags', 'withAllTags']
            assert kwargs['tagsFilterType'] in options, f'''"tagsFilterType" cannot be "{kwargs['tagsFilterType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'getOrganizationNetworks'
        }
        resource = f'/organizations/{organizationId}/networks'

        query_params = ['configTemplateId', 'tags', 'tagsFilterType', 'perPage', 'startingAfter', 'endingBefore', ]
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
        - productTypes (array): The product type(s) of the new network. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, environmental. If more than one type is included, the network will be a combined network.
        - tags (array): A list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'createOrganizationNetwork'
        }
        resource = f'/organizations/{organizationId}/networks'

        body_params = ['name', 'productTypes', 'tags', 'timeZone', 'copyFromNetworkId', ]
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
        resource = f'/organizations/{organizationId}/openapiSpec'

        return self._session.get(metadata, resource)

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
        resource = f'/organizations/{organizationId}/samlRoles'

        return self._session.get(metadata, resource)

    def createOrganizationSamlRole(self, organizationId: str, role: str, orgAccess: str, **kwargs):
        """
        **Create a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role

        - organizationId (string): (required)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only' or 'full'
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['none', 'read-only', 'full']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'createOrganizationSamlRole'
        }
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
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return self._session.get(metadata, resource)

    def updateOrganizationSamlRole(self, organizationId: str, samlRoleId: str, **kwargs):
        """
        **Update a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role

        - organizationId (string): (required)
        - samlRoleId (string): (required)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization. Can be one of 'none', 'read-only' or 'full'
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        if 'orgAccess' in kwargs:
            options = ['none', 'read-only', 'full']
            assert kwargs['orgAccess'] in options, f'''"orgAccess" cannot be "{kwargs['orgAccess']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'updateOrganizationSamlRole'
        }
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
            options = ['DES', 'AES128']
            assert kwargs['v3PrivMode'] in options, f'''"v3PrivMode" cannot be "{kwargs['v3PrivMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['organizations', 'configure', 'snmp'],
            'operation': 'updateOrganizationSnmp'
        }
        resource = f'/organizations/{organizationId}/snmp'

        body_params = ['v2cEnabled', 'v3Enabled', 'v3AuthMode', 'v3AuthPass', 'v3PrivMode', 'v3PrivPass', 'peerIps', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getOrganizationWebhooksAlertTypes(self, organizationId: str):
        """
        **Return a list of alert types to be used with managing webhook alerts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhooks-alert-types

        - organizationId (string): (required)
        """

        metadata = {
            'tags': ['organizations', 'monitor', 'webhooks', 'alertTypes'],
            'operation': 'getOrganizationWebhooksAlertTypes'
        }
        resource = f'/organizations/{organizationId}/webhooks/alertTypes'

        return self._session.get(metadata, resource)

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
        resource = f'/organizations/{organizationId}/webhooks/logs'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)