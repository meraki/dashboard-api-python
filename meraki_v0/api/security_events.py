class SecurityEvents(object):
    def __init__(self, session):
        super(SecurityEvents, self).__init__()
        self._session = session
    
    def getNetworkClientSecurityEvents(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events (intrusion detection only) for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api/#!get-network-client-security-events
        
        - networkId (string)
        - clientId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Security events'],
            'operation': 'getNetworkClientSecurityEvents',
        }
        resource = f'/networks/{networkId}/clients/{clientId}/securityEvents'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkSecurityEvents(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events (intrusion detection only) for a network**
        https://developer.cisco.com/meraki/api/#!get-network-security-events
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Security events'],
            'operation': 'getNetworkSecurityEvents',
        }
        resource = f'/networks/{networkId}/securityEvents'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getOrganizationSecurityEvents(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events (intrusion detection only) for an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-security-events
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Security events'],
            'operation': 'getOrganizationSecurityEvents',
        }
        resource = f'/organizations/{organizationId}/securityEvents'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


