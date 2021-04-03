class Camera(object):
    def __init__(self, session):
        super(Camera, self).__init__()
        self._session = session
        


    def getDeviceCameraAnalyticsLive(self, serial: str):
        """
        **Returns live state from camera of analytics zones**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-live

        - serial (string): (required)
        """

        metadata = {
            'tags': ['camera', 'monitor', 'analytics', 'live'],
            'operation': 'getDeviceCameraAnalyticsLive'
        }
        resource = f'/devices/{serial}/camera/analytics/live'

        return self._session.get(metadata, resource)
        


    def getDeviceCameraAnalyticsOverview(self, serial: str, **kwargs):
        """
        **Returns an overview of aggregate analytics data for a timespan**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-overview

        - serial (string): (required)
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
            'tags': ['camera', 'monitor', 'analytics', 'overview'],
            'operation': 'getDeviceCameraAnalyticsOverview'
        }
        resource = f'/devices/{serial}/camera/analytics/overview'

        query_params = ['t0', 't1', 'timespan', 'objectType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceCameraAnalyticsRecent(self, serial: str, **kwargs):
        """
        **Returns most recent record for analytics zones**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-recent

        - serial (string): (required)
        - objectType (string): [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
        """

        kwargs.update(locals())

        if 'objectType' in kwargs:
            options = ['person', 'vehicle']
            assert kwargs['objectType'] in options, f'''"objectType" cannot be "{kwargs['objectType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['camera', 'monitor', 'analytics', 'recent'],
            'operation': 'getDeviceCameraAnalyticsRecent'
        }
        resource = f'/devices/{serial}/camera/analytics/recent'

        query_params = ['objectType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceCameraAnalyticsZones(self, serial: str):
        """
        **Returns all configured analytic zones for this camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zones

        - serial (string): (required)
        """

        metadata = {
            'tags': ['camera', 'monitor', 'analytics', 'zones'],
            'operation': 'getDeviceCameraAnalyticsZones'
        }
        resource = f'/devices/{serial}/camera/analytics/zones'

        return self._session.get(metadata, resource)
        


    def getDeviceCameraAnalyticsZoneHistory(self, serial: str, zoneId: str, **kwargs):
        """
        **Return historical records for analytic zones**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zone-history

        - serial (string): (required)
        - zoneId (string): (required)
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
            'tags': ['camera', 'monitor', 'analytics', 'zones', 'history'],
            'operation': 'getDeviceCameraAnalyticsZoneHistory'
        }
        resource = f'/devices/{serial}/camera/analytics/zones/{zoneId}/history'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'objectType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def generateDeviceCameraSnapshot(self, serial: str, **kwargs):
        """
        **Generate a snapshot of what the camera sees at the specified time and return a link to that image.**
        https://developer.cisco.com/meraki/api-v1/#!generate-device-camera-snapshot

        - serial (string): (required)
        - timestamp (string): [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
        - fullframe (boolean): [optional] If set to "true" the snapshot will be taken at full sensor resolution. This will error if used with timestamp.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'monitor'],
            'operation': 'generateDeviceCameraSnapshot'
        }
        resource = f'/devices/{serial}/camera/generateSnapshot'

        body_params = ['timestamp', 'fullframe', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getDeviceCameraQualityAndRetention(self, serial: str):
        """
        **Returns quality and retention settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-quality-and-retention

        - serial (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityAndRetention'],
            'operation': 'getDeviceCameraQualityAndRetention'
        }
        resource = f'/devices/{serial}/camera/qualityAndRetention'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraQualityAndRetention(self, serial: str, **kwargs):
        """
        **Update quality and retention settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-quality-and-retention

        - serial (string): (required)
        - profileId (string): The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        - motionBasedRetentionEnabled (boolean): Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        - audioRecordingEnabled (boolean): Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        - restrictedBandwidthModeEnabled (boolean): Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera
        - quality (string): Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        - resolution (string): Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080' or '2058x2058'. Not all resolutions are supported by every camera model.
        - motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        """

        kwargs.update(locals())

        if 'quality' in kwargs:
            options = ['Standard', 'High', 'Enhanced']
            assert kwargs['quality'] in options, f'''"quality" cannot be "{kwargs['quality']}", & must be set to one of: {options}'''
        if 'resolution' in kwargs:
            options = ['1280x720', '1920x1080', '1080x1080', '2058x2058']
            assert kwargs['resolution'] in options, f'''"resolution" cannot be "{kwargs['resolution']}", & must be set to one of: {options}'''
        if 'motionDetectorVersion' in kwargs:
            options = [1, 2]
            assert kwargs['motionDetectorVersion'] in options, f'''"motionDetectorVersion" cannot be "{kwargs['motionDetectorVersion']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['camera', 'configure', 'qualityAndRetention'],
            'operation': 'updateDeviceCameraQualityAndRetention'
        }
        resource = f'/devices/{serial}/camera/qualityAndRetention'

        body_params = ['profileId', 'motionBasedRetentionEnabled', 'audioRecordingEnabled', 'restrictedBandwidthModeEnabled', 'quality', 'resolution', 'motionDetectorVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCameraSense(self, serial: str):
        """
        **Returns sense settings for a given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense

        - serial (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'sense'],
            'operation': 'getDeviceCameraSense'
        }
        resource = f'/devices/{serial}/camera/sense'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraSense(self, serial: str, **kwargs):
        """
        **Update sense settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-sense

        - serial (string): (required)
        - senseEnabled (boolean): Boolean indicating if sense(license) is enabled(true) or disabled(false) on the camera
        - mqttBrokerId (string): The ID of the MQTT broker to be enabled on the camera. A value of null will disable MQTT on the camera
        - detectionModelId (string): The ID of the object detection model
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'sense'],
            'operation': 'updateDeviceCameraSense'
        }
        resource = f'/devices/{serial}/camera/sense'

        body_params = ['senseEnabled', 'mqttBrokerId', 'detectionModelId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCameraSenseObjectDetectionModels(self, serial: str):
        """
        **Returns the MV Sense object detection model list for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense-object-detection-models

        - serial (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'sense', 'objectDetectionModels'],
            'operation': 'getDeviceCameraSenseObjectDetectionModels'
        }
        resource = f'/devices/{serial}/camera/sense/objectDetectionModels'

        return self._session.get(metadata, resource)
        


    def getDeviceCameraVideoSettings(self, serial: str):
        """
        **Returns video settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-settings

        - serial (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'video', 'settings'],
            'operation': 'getDeviceCameraVideoSettings'
        }
        resource = f'/devices/{serial}/camera/video/settings'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraVideoSettings(self, serial: str, **kwargs):
        """
        **Update video settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings

        - serial (string): (required)
        - externalRtspEnabled (boolean): Boolean indicating if external rtsp stream is exposed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'video', 'settings'],
            'operation': 'updateDeviceCameraVideoSettings'
        }
        resource = f'/devices/{serial}/camera/video/settings'

        body_params = ['externalRtspEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCameraVideoLink(self, serial: str, **kwargs):
        """
        **Returns video link to the specified camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-link

        - serial (string): (required)
        - timestamp (string): [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'videoLink'],
            'operation': 'getDeviceCameraVideoLink'
        }
        resource = f'/devices/{serial}/camera/videoLink'

        query_params = ['timestamp', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkCameraQualityRetentionProfiles(self, networkId: str):
        """
        **List the quality retention profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profiles

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'getNetworkCameraQualityRetentionProfiles'
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles'

        return self._session.get(metadata, resource)
        


    def createNetworkCameraQualityRetentionProfile(self, networkId: str, name: str, **kwargs):
        """
        **Creates new quality retention profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-camera-quality-retention-profile

        - networkId (string): (required)
        - name (string): The name of the new profile. Must be unique. This parameter is required.
        - motionBasedRetentionEnabled (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false.
        - restrictedBandwidthModeEnabled (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false.
        - audioRecordingEnabled (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
        - cloudArchiveEnabled (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
        - motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        - scheduleId (string): Schedule for which this camera will record video, or 'null' to always record.
        - maxRetentionDays (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days
        - videoSettings (object): Video quality and resolution settings for all the camera models.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'createNetworkCameraQualityRetentionProfile'
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles'

        body_params = ['name', 'motionBasedRetentionEnabled', 'restrictedBandwidthModeEnabled', 'audioRecordingEnabled', 'cloudArchiveEnabled', 'motionDetectorVersion', 'scheduleId', 'maxRetentionDays', 'videoSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str):
        """
        **Retrieve a single quality retention profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profile

        - networkId (string): (required)
        - qualityRetentionProfileId (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'getNetworkCameraQualityRetentionProfile'
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str, **kwargs):
        """
        **Update an existing quality retention profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-camera-quality-retention-profile

        - networkId (string): (required)
        - qualityRetentionProfileId (string): (required)
        - name (string): The name of the new profile. Must be unique.
        - motionBasedRetentionEnabled (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false.
        - restrictedBandwidthModeEnabled (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false.
        - audioRecordingEnabled (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
        - cloudArchiveEnabled (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
        - motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        - scheduleId (string): Schedule for which this camera will record video, or 'null' to always record.
        - maxRetentionDays (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days
        - videoSettings (object): Video quality and resolution settings for all the camera models.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'updateNetworkCameraQualityRetentionProfile'
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        body_params = ['name', 'motionBasedRetentionEnabled', 'restrictedBandwidthModeEnabled', 'audioRecordingEnabled', 'cloudArchiveEnabled', 'motionDetectorVersion', 'scheduleId', 'maxRetentionDays', 'videoSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str):
        """
        **Delete an existing quality retention profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-quality-retention-profile

        - networkId (string): (required)
        - qualityRetentionProfileId (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'deleteNetworkCameraQualityRetentionProfile'
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkCameraSchedules(self, networkId: str):
        """
        **Returns a list of all camera recording schedules.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-schedules

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['camera', 'configure', 'schedules'],
            'operation': 'getNetworkCameraSchedules'
        }
        resource = f'/networks/{networkId}/camera/schedules'

        return self._session.get(metadata, resource)
        
