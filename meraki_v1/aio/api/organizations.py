class AsyncOrganizations:
    def __init__(self, session):
        super().__init__()
        self._session = session

    async def getOrganizations(self):
        """
        **List the organizations that the user has privileges on**
        https://developer.cisco.com/meraki/api-v1/#!get-organizations
        
        """

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'getOrganizations',
        }
        resource = f'/organizations'

        return await self._session.get(metadata, resource)

    async def createOrganization(self, name: str):
        """
        **Create a new organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization
        
        - name (string): The name of the organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'createOrganization',
        }
        resource = f'/organizations'

        body_params = ['name']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganization(self, organizationId: str):
        """
        **Return an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'getOrganization',
        }
        resource = f'/organizations/{organizationId}'

        return await self._session.get(metadata, resource)

    async def updateOrganization(self, organizationId: str, **kwargs):
        """
        **Update an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization
        
        - organizationId (string)
        - name (string): The name of the organization
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'updateOrganization',
        }
        resource = f'/organizations/{organizationId}'

        body_params = ['name']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganization(self, organizationId: str):
        """
        **Delete an organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'deleteOrganization',
        }
        resource = f'/organizations/{organizationId}'

        return await self._session.delete(metadata, resource)

    async def createOrganizationActionBatch(self, organizationId: str, actions: list, **kwargs):
        """
        **Create an action batch**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-action-batch
        
        - organizationId (string)
        - actions (array): A set of changes to make as part of this action (<a href='https://developer.cisco.com/meraki/api/#/rest/guides/action-batches/'>more details</a>)
        - confirmed (boolean): Set to true for immediate execution. Set to false if the action should be previewed before executing. This property cannot be unset once it is true. Defaults to false.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch. Defaults to false.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'createOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches'

        body_params = ['confirmed', 'synchronous', 'actions']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationActionBatches(self, organizationId: str):
        """
        **Return the list of action batches in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batches
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'getOrganizationActionBatches',
        }
        resource = f'/organizations/{organizationId}/actionBatches'

        return await self._session.get(metadata, resource)

    async def getOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Return an action batch**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-action-batch
        
        - organizationId (string)
        - actionBatchId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'getOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return await self._session.get(metadata, resource)

    async def deleteOrganizationActionBatch(self, organizationId: str, actionBatchId: str):
        """
        **Delete an action batch**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-action-batch
        
        - organizationId (string)
        - actionBatchId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'deleteOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        return await self._session.delete(metadata, resource)

    async def updateOrganizationActionBatch(self, organizationId: str, actionBatchId: str, **kwargs):
        """
        **Update an action batch**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-action-batch
        
        - organizationId (string)
        - actionBatchId (string)
        - confirmed (boolean): A boolean representing whether or not the batch has been confirmed. This property cannot be unset once it is true.
        - synchronous (boolean): Set to true to force the batch to run synchronous. There can be at most 20 actions in synchronous batch.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'actionBatches'],
            'operation': 'updateOrganizationActionBatch',
        }
        resource = f'/organizations/{organizationId}/actionBatches/{actionBatchId}'

        body_params = ['confirmed', 'synchronous']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getOrganizationAdmins(self, organizationId: str):
        """
        **List the dashboard administrators in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-admins
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'getOrganizationAdmins',
        }
        resource = f'/organizations/{organizationId}/admins'

        return await self._session.get(metadata, resource)

    async def createOrganizationAdmin(self, organizationId: str, email: str, name: str, orgAccess: str, **kwargs):
        """
        **Create a new dashboard administrator**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-admin
        
        - organizationId (string)
        - email (string): The email of the dashboard administrator. This attribute can not be updated.
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
            'operation': 'createOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins'

        body_params = ['email', 'name', 'orgAccess', 'tags', 'networks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def updateOrganizationAdmin(self, organizationId: str, id: str, **kwargs):
        """
        **Update an administrator**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-admin
        
        - organizationId (string)
        - id (string)
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
            'operation': 'updateOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins/{id}'

        body_params = ['name', 'orgAccess', 'tags', 'networks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganizationAdmin(self, organizationId: str, id: str):
        """
        **Revoke all access for a dashboard administrator within this organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-admin
        
        - organizationId (string)
        - id (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'admins'],
            'operation': 'deleteOrganizationAdmin',
        }
        resource = f'/organizations/{organizationId}/admins/{id}'

        return await self._session.delete(metadata, resource)

    async def getOrganizationApiRequests(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the API requests made by an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
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
            'operation': 'getOrganizationApiRequests',
        }
        resource = f'/organizations/{organizationId}/apiRequests'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getOrganizationApiRequestsOverview(self, organizationId: str, **kwargs):
        """
        **Return an aggregated overview of API requests data**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-api-requests-overview
        
        - organizationId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'apiRequests', 'overview'],
            'operation': 'getOrganizationApiRequestsOverview',
        }
        resource = f'/organizations/{organizationId}/apiRequests/overview'

        query_params = ['t0', 't1', 'timespan']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getOrganizationBrandingPolicies(self, organizationId: str):
        """
        **List the branding policies of an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'getOrganizationBrandingPolicies',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies'

        return await self._session.get(metadata, resource)

    async def createOrganizationBrandingPolicy(self, organizationId: str, name: str, enabled: bool, adminSettings: dict, **kwargs):
        """
        **Add a new branding policy to an organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-branding-policy
        
        - organizationId (string)
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
            'operation': 'createOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationBrandingPoliciesPriorities(self, organizationId: str):
        """
        **Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policies-priorities
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies', 'priorities'],
            'operation': 'getOrganizationBrandingPoliciesPriorities',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        return await self._session.get(metadata, resource)

    async def updateOrganizationBrandingPoliciesPriorities(self, organizationId: str, brandingPolicyIds: list):
        """
        **Update the priority ordering of an organization's branding policies.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policies-priorities
        
        - organizationId (string)
        - brandingPolicyIds (array): A list of branding policy IDs arranged in ascending priority order (IDs later in the array have higher priority).
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies', 'priorities'],
            'operation': 'updateOrganizationBrandingPoliciesPriorities',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/priorities'

        body_params = ['brandingPolicyIds']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Return a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-branding-policy
        
        - organizationId (string)
        - brandingPolicyId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'getOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        return await self._session.get(metadata, resource)

    async def updateOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str, **kwargs):
        """
        **Update a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-branding-policy
        
        - organizationId (string)
        - brandingPolicyId (string)
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
            'operation': 'updateOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        body_params = ['name', 'enabled', 'adminSettings', 'helpSettings']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganizationBrandingPolicy(self, organizationId: str, brandingPolicyId: str):
        """
        **Delete a branding policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-branding-policy
        
        - organizationId (string)
        - brandingPolicyId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'brandingPolicies'],
            'operation': 'deleteOrganizationBrandingPolicy',
        }
        resource = f'/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}'

        return await self._session.delete(metadata, resource)

    async def claimIntoOrganization(self, organizationId: str, **kwargs):
        """
        **Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization's inventory.**
        https://developer.cisco.com/meraki/api-v1/#!claim-into-organization
        
        - organizationId (string)
        - orders (array): The numbers of the orders that should be claimed
        - serials (array): The serials of the devices that should be claimed
        - licenses (array): The licenses that should be claimed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'claimIntoOrganization',
        }
        resource = f'/organizations/{organizationId}/claim'

        body_params = ['orders', 'serials', 'licenses']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def cloneOrganization(self, organizationId: str, name: str):
        """
        **Create a new organization by cloning the addressed organization**
        https://developer.cisco.com/meraki/api-v1/#!clone-organization
        
        - organizationId (string)
        - name (string): The name of the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure'],
            'operation': 'cloneOrganization',
        }
        resource = f'/organizations/{organizationId}/clone'

        body_params = ['name']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationConfigTemplates(self, organizationId: str):
        """
        **List the configuration templates for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-templates
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'getOrganizationConfigTemplates',
        }
        resource = f'/organizations/{organizationId}/configTemplates'

        return await self._session.get(metadata, resource)

    async def createOrganizationConfigTemplate(self, organizationId: str, name: str, **kwargs):
        """
        **Create a new configuration template**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-config-template
        
        - organizationId (string)
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article</a>. Not applicable if copying from existing network or template
        - copyFromNetworkId (string): The ID of the network or config template to copy configuration from
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'createOrganizationConfigTemplate',
        }
        resource = f'/organizations/{organizationId}/configTemplates'

        body_params = ['name', 'timeZone', 'copyFromNetworkId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def updateOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str, **kwargs):
        """
        **Update a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-config-template
        
        - organizationId (string)
        - configTemplateId (string)
        - name (string): The name of the configuration template
        - timeZone (string): The timezone of the configuration template. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'updateOrganizationConfigTemplate',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        body_params = ['name', 'timeZone']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Remove a configuration template**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-config-template
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'deleteOrganizationConfigTemplate',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        return await self._session.delete(metadata, resource)

    async def getOrganizationConfigTemplate(self, organizationId: str, configTemplateId: str):
        """
        **Return a single configuration template**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-config-template
        
        - organizationId (string)
        - configTemplateId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'configTemplates'],
            'operation': 'getOrganizationConfigTemplate',
        }
        resource = f'/organizations/{organizationId}/configTemplates/{configTemplateId}'

        return await self._session.get(metadata, resource)

    async def getOrganizationConfigurationChanges(self, organizationId: str, total_pages=1, direction='prev', **kwargs):
        """
        **View the Change Log for your organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-configuration-changes
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "prev" (default) or "next" page
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
            'operation': 'getOrganizationConfigurationChanges',
        }
        resource = f'/organizations/{organizationId}/configurationChanges'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getOrganizationDevices(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the devices in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - configurationUpdatedAfter (string): Filter results by whether or not the device's configuration has been updated after the given timestamp
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'devices'],
            'operation': 'getOrganizationDevices',
        }
        resource = f'/organizations/{organizationId}/devices'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'configurationUpdatedAfter']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getOrganizationDevicesStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the status of every Meraki device in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-statuses
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'monitor', 'devices', 'statuses'],
            'operation': 'getOrganizationDevicesStatuses',
        }
        resource = f'/organizations/{organizationId}/devices/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getOrganizationDevicesUplinksLossAndLatency(self, organizationId: str, **kwargs):
        """
        **Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-devices-uplinks-loss-and-latency
        
        - organizationId (string)
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
            'operation': 'getOrganizationDevicesUplinksLossAndLatency',
        }
        resource = f'/organizations/{organizationId}/devices/uplinksLossAndLatency'

        query_params = ['t0', 't1', 'timespan', 'uplink', 'ip']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get(metadata, resource, params)

    async def getOrganizationInventory(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the device inventory for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'inventory'],
            'operation': 'getOrganizationInventory',
        }
        resource = f'/organizations/{organizationId}/inventory'

        query_params = ['perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getOrganizationLicenses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the licenses for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
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
            'operation': 'getOrganizationLicenses',
        }
        resource = f'/organizations/{organizationId}/licenses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'deviceSerial', 'networkId', 'state']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def assignOrganizationLicensesSeats(self, organizationId: str, licenseId: str, networkId: str, seatCount: int):
        """
        **Assign SM seats to a network. This will increase the managed SM device limit of the network**
        https://developer.cisco.com/meraki/api-v1/#!assign-organization-licenses-seats
        
        - organizationId (string)
        - licenseId (string): The ID of the SM license to assign seats from
        - networkId (string): The ID of the SM network to assign the seats to
        - seatCount (integer): The number of seats to assign to the SM network. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'assignOrganizationLicensesSeats',
        }
        resource = f'/organizations/{organizationId}/licenses/assignSeats'

        body_params = ['licenseId', 'networkId', 'seatCount']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def moveOrganizationLicenses(self, organizationId: str, destOrganizationId: str, licenseIds: list):
        """
        **Move licenses to another organization. This will also move any devices that the licenses are assigned to**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses
        
        - organizationId (string)
        - destOrganizationId (string): The ID of the organization to move the licenses to
        - licenseIds (array): A list of IDs of licenses to move to the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'moveOrganizationLicenses',
        }
        resource = f'/organizations/{organizationId}/licenses/move'

        body_params = ['destOrganizationId', 'licenseIds']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def moveOrganizationLicensesSeats(self, organizationId: str, destOrganizationId: str, licenseId: str, seatCount: int):
        """
        **Move SM seats to another organization**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licenses-seats
        
        - organizationId (string)
        - destOrganizationId (string): The ID of the organization to move the SM seats to
        - licenseId (string): The ID of the SM license to move the seats from
        - seatCount (integer): The number of seats to move to the new organization. Must be less than or equal to the total number of seats of the license
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'moveOrganizationLicensesSeats',
        }
        resource = f'/organizations/{organizationId}/licenses/moveSeats'

        body_params = ['destOrganizationId', 'licenseId', 'seatCount']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationLicensesOverview(self, organizationId: str):
        """
        **Return an overview of the license state for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licenses-overview
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'monitor', 'licenses', 'overview'],
            'operation': 'getOrganizationLicensesOverview',
        }
        resource = f'/organizations/{organizationId}/licenses/overview'

        return await self._session.get(metadata, resource)

    async def renewOrganizationLicensesSeats(self, organizationId: str, licenseIdToRenew: str, unusedLicenseId: str):
        """
        **Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license**
        https://developer.cisco.com/meraki/api-v1/#!renew-organization-licenses-seats
        
        - organizationId (string)
        - licenseIdToRenew (string): The ID of the SM license to renew. This license must already be assigned to an SM network
        - unusedLicenseId (string): The SM license to use to renew the seats on 'licenseIdToRenew'. This license must have at least as many seats available as there are seats on 'licenseIdToRenew'
        """

        kwargs = locals()

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'renewOrganizationLicensesSeats',
        }
        resource = f'/organizations/{organizationId}/licenses/renewSeats'

        body_params = ['licenseIdToRenew', 'unusedLicenseId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationLicense(self, organizationId: str, licenseId: str):
        """
        **Display a license**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-license
        
        - organizationId (string)
        - licenseId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'getOrganizationLicense',
        }
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        return await self._session.get(metadata, resource)

    async def updateOrganizationLicense(self, organizationId: str, licenseId: str, **kwargs):
        """
        **Update a license**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-license
        
        - organizationId (string)
        - licenseId (string)
        - deviceSerial (string): The serial number of the device to assign this license to. Set this to null to unassign the license. If a different license is already active on the device, this parameter will control queueing/dequeuing this license.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'licenses'],
            'operation': 'updateOrganizationLicense',
        }
        resource = f'/organizations/{organizationId}/licenses/{licenseId}'

        body_params = ['deviceSerial']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getOrganizationNetworks(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the networks that the user has privileges on in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-networks
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - configTemplateId (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'getOrganizationNetworks',
        }
        resource = f'/organizations/{organizationId}/networks'

        query_params = ['configTemplateId', 'perPage', 'startingAfter', 'endingBefore']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def createOrganizationNetwork(self, organizationId: str, name: str, productTypes: list, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-network
        
        - organizationId (string)
        - name (string): The name of the new network
        - productTypes (array): The product type(s) of the new network. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway. If more than one type is included, the network will be a combined network.
        - tags (array): A list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'createOrganizationNetwork',
        }
        resource = f'/organizations/{organizationId}/networks'

        body_params = ['name', 'productTypes', 'tags', 'timeZone', 'copyFromNetworkId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def combineOrganizationNetworks(self, organizationId: str, name: str, networkIds: list, **kwargs):
        """
        **Combine multiple networks into a single network**
        https://developer.cisco.com/meraki/api-v1/#!combine-organization-networks
        
        - organizationId (string)
        - name (string): The name of the combined network
        - networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'networks'],
            'operation': 'combineOrganizationNetworks',
        }
        resource = f'/organizations/{organizationId}/networks/combine'

        body_params = ['name', 'networkIds', 'enrollmentString']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationOpenapiSpec(self, organizationId: str):
        """
        **Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-openapi-spec
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'monitor', 'openapiSpec'],
            'operation': 'getOrganizationOpenapiSpec',
        }
        resource = f'/organizations/{organizationId}/openapiSpec'

        return await self._session.get(metadata, resource)

    async def getOrganizationSamlRoles(self, organizationId: str):
        """
        **List the SAML roles for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-roles
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'getOrganizationSamlRoles',
        }
        resource = f'/organizations/{organizationId}/samlRoles'

        return await self._session.get(metadata, resource)

    async def createOrganizationSamlRole(self, organizationId: str, **kwargs):
        """
        **Create a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-saml-role
        
        - organizationId (string)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'createOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles'

        body_params = ['role', 'orgAccess', 'tags', 'networks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Return a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-saml-role
        
        - organizationId (string)
        - samlRoleId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'getOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return await self._session.get(metadata, resource)

    async def updateOrganizationSamlRole(self, organizationId: str, samlRoleId: str, **kwargs):
        """
        **Update a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-saml-role
        
        - organizationId (string)
        - samlRoleId (string)
        - role (string): The role of the SAML administrator
        - orgAccess (string): The privilege of the SAML administrator on the organization
        - tags (array): The list of tags that the SAML administrator has privleges on
        - networks (array): The list of networks that the SAML administrator has privileges on
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'updateOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        body_params = ['role', 'orgAccess', 'tags', 'networks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteOrganizationSamlRole(self, organizationId: str, samlRoleId: str):
        """
        **Remove a SAML role**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-saml-role
        
        - organizationId (string)
        - samlRoleId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'samlRoles'],
            'operation': 'deleteOrganizationSamlRole',
        }
        resource = f'/organizations/{organizationId}/samlRoles/{samlRoleId}'

        return await self._session.delete(metadata, resource)

    async def getOrganizationSnmp(self, organizationId: str):
        """
        **Return the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-snmp
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['organizations', 'configure', 'snmp'],
            'operation': 'getOrganizationSnmp',
        }
        resource = f'/organizations/{organizationId}/snmp'

        return await self._session.get(metadata, resource)

    async def updateOrganizationSnmp(self, organizationId: str, **kwargs):
        """
        **Update the SNMP settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-snmp
        
        - organizationId (string)
        - v2cEnabled (boolean): Boolean indicating whether SNMP version 2c is enabled for the organization.
        - v3Enabled (boolean): Boolean indicating whether SNMP version 3 is enabled for the organization.
        - v3AuthMode (string): The SNMP version 3 authentication mode. Can be either 'MD5' or 'SHA'.
        - v3AuthPass (string): The SNMP version 3 authentication password. Must be at least 8 characters if specified.
        - v3PrivMode (string): The SNMP version 3 privacy mode. Can be either 'DES' or 'AES128'.
        - v3PrivPass (string): The SNMP version 3 privacy password. Must be at least 8 characters if specified.
        - peerIps (string): The IPs that are allowed to access the SNMP server. This list should be IPv4 addresses separated by semi-colons (ie. "1.2.3.4;2.3.4.5").
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
            'operation': 'updateOrganizationSnmp',
        }
        resource = f'/organizations/{organizationId}/snmp'

        body_params = ['v2cEnabled', 'v3Enabled', 'v3AuthMode', 'v3AuthPass', 'v3PrivMode', 'v3PrivPass', 'peerIps']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getOrganizationWebhookLogs(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the log of webhook POSTs sent**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-webhook-logs
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
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
            'tags': ['organizations', 'monitor', 'webhookLogs'],
            'operation': 'getOrganizationWebhookLogs',
        }
        resource = f'/organizations/{organizationId}/webhookLogs'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


