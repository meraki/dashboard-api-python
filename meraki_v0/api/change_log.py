class ChangeLog(object):
    def __init__(self, session):
        super(ChangeLog, self).__init__()
        self._session = session
    
    def getOrganizationConfigurationChanges(self, organizationId: str, total_pages=1, direction='prev', **kwargs):
        """
        **View the Change Log for your organization**
        https://developer.cisco.com/meraki/api/#!get-organization-configuration-changes
        
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
            'tags': ['Change log'],
            'operation': 'getOrganizationConfigurationChanges',
        }
        resource = f'/organizations/{organizationId}/configurationChanges'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'networkId', 'adminId']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


