class AsyncSensor:
    def __init__(self, session):
        super().__init__()
        self._session = session
        


    def getOrganizationSensorReadingsHistory(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return all reported readings from sensors in a given timespan, sorted by timestamp**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-history

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are temperature, humidity, water, door, and battery.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'history'],
            'operation': 'getOrganizationSensorReadingsHistory'
        }
        resource = f'/organizations/{organizationId}/sensor/readings/history'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 't0', 't1', 'timespan', 'networkIds', 'serials', 'metrics', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationSensorReadingsLatest(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Return the latest available reading for each metric from each sensor, sorted by sensor serial**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter readings by network.
        - serials (array): Optional parameter to filter readings by sensor.
        - metrics (array): Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are temperature, humidity, water, door, and battery.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['sensor', 'monitor', 'readings', 'latest'],
            'operation': 'getOrganizationSensorReadingsLatest'
        }
        resource = f'/organizations/{organizationId}/sensor/readings/latest'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'metrics', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'metrics', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        
