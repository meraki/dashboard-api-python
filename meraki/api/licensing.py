import urllib


class Licensing(object):
    def __init__(self, session):
        super(Licensing, self).__init__()
        self._session = session
        


    def getAdministeredLicensingSubscriptionEntitlements(self, **kwargs):
        """
        **Retrieve the list of purchasable entitlements**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-entitlements

        - skus (array): Filter to entitlements with the specified SKUs
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'subscription', 'entitlements'],
            'operation': 'getAdministeredLicensingSubscriptionEntitlements'
        }
        resource = f'/administered/licensing/subscription/entitlements'

        query_params = ['skus', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['skus', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getAdministeredLicensingSubscriptionSubscriptions(self, total_pages=1, direction='next', **kwargs):
        """
        **List available subscriptions**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-subscriptions

        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - subscriptionIds (array): List of subscription ids to fetch
        - organizationIds (array): Organizations to get associated subscriptions for
        - startDate (string): Filter subscriptions by start date, ISO 8601 format. To filter with a range of dates, use 'startDate[<option>]=?' in the request. Accepted options include lt, gt, lte, gte.
        - endDate (string): Filter subscriptions by end date, ISO 8601 format. To filter with a range of dates, use 'endDate[<option>]=?' in the request. Accepted options include lt, gt, lte, gte.
        - statuses (array): List of statuses that returned subscriptions can have
        - productTypes (array): List of product types that returned subscriptions need to have entitlements for.
        - name (string): Search for subscription name
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'subscription', 'subscriptions'],
            'operation': 'getAdministeredLicensingSubscriptionSubscriptions'
        }
        resource = f'/administered/licensing/subscription/subscriptions'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'subscriptionIds', 'organizationIds', 'startDate', 'endDate', 'statuses', 'productTypes', 'name', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['subscriptionIds', 'organizationIds', 'statuses', 'productTypes', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def claimAdministeredLicensingSubscriptionSubscriptions(self, claimKey: str, organizationId: str, **kwargs):
        """
        **Claim a subscription into an organization.**
        https://developer.cisco.com/meraki/api-v1/#!claim-administered-licensing-subscription-subscriptions

        - claimKey (string): The subscription's claim key
        - organizationId (string): The id of the organization claiming the subscription
        - validate (boolean): Check if the provided claim key is valid and can be claimed into the organization.
        - name (string): Friendly name to identify the subscription
        - description (string): Extra details or notes about the subscription
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'subscription', 'subscriptions'],
            'operation': 'claimAdministeredLicensingSubscriptionSubscriptions'
        }
        resource = f'/administered/licensing/subscription/subscriptions/claim'

        body_params = ['claimKey', 'organizationId', 'name', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def validateAdministeredLicensingSubscriptionSubscriptionsClaimKey(self, claimKey: str):
        """
        **Find a subscription by claim key**
        https://developer.cisco.com/meraki/api-v1/#!validate-administered-licensing-subscription-subscriptions-claim-key

        - claimKey (string): The subscription's claim key
        """

        kwargs = locals()

        metadata = {
            'tags': ['licensing', 'configure', 'subscription', 'subscriptions', 'claimKey'],
            'operation': 'validateAdministeredLicensingSubscriptionSubscriptionsClaimKey'
        }
        resource = f'/administered/licensing/subscription/subscriptions/claimKey/validate'

        body_params = ['claimKey', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses(self, organizationIds: list, **kwargs):
        """
        **Get compliance status for requested subscriptions**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-licensing-subscription-subscriptions-compliance-statuses

        - organizationIds (array): Organizations to get subscription compliance information for
        - subscriptionIds (array): Subscription ids
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'subscription', 'subscriptions', 'compliance', 'statuses'],
            'operation': 'getAdministeredLicensingSubscriptionSubscriptionsComplianceStatuses'
        }
        resource = f'/administered/licensing/subscription/subscriptions/compliance/statuses'

        query_params = ['organizationIds', 'subscriptionIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['organizationIds', 'subscriptionIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def bindAdministeredLicensingSubscriptionSubscription(self, subscriptionId: str, networkIds: list, **kwargs):
        """
        **Bind networks to a subscription**
        https://developer.cisco.com/meraki/api-v1/#!bind-administered-licensing-subscription-subscription

        - subscriptionId (string): Subscription ID
        - networkIds (array): List of network ids to bind to the subscription
        - validate (boolean): Check if the provided networks can be bound to the subscription. Returns any licensing problems and does not commit the results.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'subscription', 'subscriptions'],
            'operation': 'bindAdministeredLicensingSubscriptionSubscription'
        }
        subscriptionId = urllib.parse.quote(str(subscriptionId), safe='')
        resource = f'/administered/licensing/subscription/subscriptions/{subscriptionId}/bind'

        body_params = ['networkIds', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationLicensingCotermLicenses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the licenses in a coterm organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licensing-coterm-licenses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - invalidated (boolean): Filter for licenses that are invalidated
        - expired (boolean): Filter for licenses that are expired
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'coterm', 'licenses'],
            'operation': 'getOrganizationLicensingCotermLicenses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licensing/coterm/licenses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def moveOrganizationLicensingCotermLicenses(self, organizationId: str, destination: dict, licenses: list):
        """
        **Moves a license to a different organization (coterm only)**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licensing-coterm-licenses

        - organizationId (string): Organization ID
        - destination (object): Destination data for the license move
        - licenses (array): The list of licenses to move
        """

        kwargs = locals()

        metadata = {
            'tags': ['licensing', 'configure', 'coterm', 'licenses'],
            'operation': 'moveOrganizationLicensingCotermLicenses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licensing/coterm/licenses/move'

        body_params = ['destination', 'licenses', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        
