class WebhookLogs(object):
    def __init__(self, session):
        super(WebhookLogs, self).__init__()
        self._session = session
    
    def getOrganizationWebhookLogs(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the log of webhook POSTs sent**
        https://developer.cisco.com/meraki/api/#!get-organization-webhook-logs
        
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
            'tags': ['Webhook logs'],
            'operation': 'getOrganizationWebhookLogs',
        }
        resource = f'/organizations/{organizationId}/webhookLogs'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'url']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


