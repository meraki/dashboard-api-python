class AsyncMVSense:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getDeviceCameraAnalyticsLive(self, serial: str):
        """
        **Returns live state from camera of analytics zones**
        https://developer.cisco.com/meraki/api/#!get-device-camera-analytics-live
        
        - serial (string)
        """

        metadata = {
            'tags': ['MV Sense'],
            'operation': 'getDeviceCameraAnalyticsLive',
        }
        resource = f'/devices/{serial}/camera/analytics/live'

        return await self._session.get(metadata, resource)

    async def getDeviceCameraAnalyticsOverview(self, serial: str, **kwargs):
        """
        **Returns an overview of aggregate analytics data for a timespan**
        https://developer.cisco.com/meraki/api/#!get-device-camera-analytics-overview
        
        - serial (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
        - objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
        """

        kwargs.update(locals())

        if 'objectType' in kwargs:
            options = ['person', 'vehicle']
            assert kwargs['objectType'] in options, f'''"objectType" cannot be "{kwargs['objectType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['MV Sense'],
            'operation': 'getDeviceCameraAnalyticsOverview',
        }
        resource = f'/devices/{serial}/camera/analytics/overview'

        query_params = ['t0', 't1', 'timespan', 'objectType']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceCameraAnalyticsRecent(self, serial: str, **kwargs):
        """
        **Returns most recent record for analytics zones**
        https://developer.cisco.com/meraki/api/#!get-device-camera-analytics-recent
        
        - serial (string)
        - objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
        """

        kwargs.update(locals())

        if 'objectType' in kwargs:
            options = ['person', 'vehicle']
            assert kwargs['objectType'] in options, f'''"objectType" cannot be "{kwargs['objectType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['MV Sense'],
            'operation': 'getDeviceCameraAnalyticsRecent',
        }
        resource = f'/devices/{serial}/camera/analytics/recent'

        query_params = ['objectType']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def getDeviceCameraAnalyticsZones(self, serial: str):
        """
        **Returns all configured analytic zones for this camera**
        https://developer.cisco.com/meraki/api/#!get-device-camera-analytics-zones
        
        - serial (string)
        """

        metadata = {
            'tags': ['MV Sense'],
            'operation': 'getDeviceCameraAnalyticsZones',
        }
        resource = f'/devices/{serial}/camera/analytics/zones'

        return await self._session.get(metadata, resource)

    async def getDeviceCameraAnalyticsZoneHistory(self, serial: str, zoneId: str, **kwargs):
        """
        **Return historical records for analytic zones**
        https://developer.cisco.com/meraki/api/#!get-device-camera-analytics-zone-history
        
        - serial (string)
        - zoneId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
        - objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
        """

        kwargs.update(locals())

        if 'objectType' in kwargs:
            options = ['person', 'vehicle']
            assert kwargs['objectType'] in options, f'''"objectType" cannot be "{kwargs['objectType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['MV Sense'],
            'operation': 'getDeviceCameraAnalyticsZoneHistory',
        }
        resource = f'/devices/{serial}/camera/analytics/zones/{zoneId}/history'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'objectType']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

