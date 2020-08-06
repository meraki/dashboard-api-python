class AsyncAPIUsage:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getOrganizationApiRequests(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the API requests made by an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-api-requests
        
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
            'tags': ['API usage'],
            'operation': 'getOrganizationApiRequests',
        }
        resource = f'/organizations/{organizationId}/apiRequests'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'adminId', 'path', 'method', 'responseCode', 'sourceIp']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get_pages(metadata, resource, params, total_pages, direction)


    async def getOrganizationApiRequestsOverview(self, organizationId: str, **kwargs):
        """
        **Return an aggregated overview of API requests data**
        https://developer.cisco.com/meraki/api/#!get-organization-api-requests-overview
        
        - organizationId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['API usage'],
            'operation': 'getOrganizationApiRequestsOverview',
        }
        resource = f'/organizations/{organizationId}/apiRequests/overview'

        query_params = ['t0', 't1', 'timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

