import urllib


class AsyncCamera:
    def __init__(self, session):
        super().__init__()
        self._session = session
        


    def getDeviceCameraAnalyticsLive(self, serial: str):
        """
        **Returns live state from camera analytics zones**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-live

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'monitor', 'analytics', 'live'],
            'operation': 'getDeviceCameraAnalyticsLive'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/analytics/live'

        return self._session.get(metadata, resource)
        


    def getDeviceCameraAnalyticsOverview(self, serial: str, **kwargs):
        """
        **Returns an overview of aggregate analytics data for a timespan**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-overview

        - serial (string): Serial
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
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/analytics/overview'

        query_params = ['t0', 't1', 'timespan', 'objectType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceCameraAnalyticsRecent(self, serial: str, **kwargs):
        """
        **Returns most recent record for analytics zones**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-recent

        - serial (string): Serial
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
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/analytics/recent'

        query_params = ['objectType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceCameraAnalyticsZones(self, serial: str):
        """
        **Returns all configured analytic zones for this camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zones

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'monitor', 'analytics', 'zones'],
            'operation': 'getDeviceCameraAnalyticsZones'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/analytics/zones'

        return self._session.get(metadata, resource)
        


    def getDeviceCameraAnalyticsZoneHistory(self, serial: str, zoneId: str, **kwargs):
        """
        **Return historical records for analytic zones**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-analytics-zone-history

        - serial (string): Serial
        - zoneId (string): Zone ID
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
        serial = urllib.parse.quote(str(serial), safe='')
        zoneId = urllib.parse.quote(str(zoneId), safe='')
        resource = f'/devices/{serial}/camera/analytics/zones/{zoneId}/history'

        query_params = ['t0', 't1', 'timespan', 'resolution', 'objectType', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceCameraCustomAnalytics(self, serial: str):
        """
        **Return custom analytics settings for a camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-custom-analytics

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'configure', 'customAnalytics'],
            'operation': 'getDeviceCameraCustomAnalytics'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/customAnalytics'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraCustomAnalytics(self, serial: str, **kwargs):
        """
        **Update custom analytics settings for a camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-custom-analytics

        - serial (string): Serial
        - enabled (boolean): Enable custom analytics
        - artifactId (string): The ID of the custom analytics artifact
        - parameters (array): Parameters for the custom analytics workload
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'customAnalytics'],
            'operation': 'updateDeviceCameraCustomAnalytics'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/customAnalytics'

        body_params = ['enabled', 'artifactId', 'parameters', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def generateDeviceCameraSnapshot(self, serial: str, **kwargs):
        """
        **Generate a snapshot of what the camera sees at the specified time and return a link to that image.**
        https://developer.cisco.com/meraki/api-v1/#!generate-device-camera-snapshot

        - serial (string): Serial
        - timestamp (string): [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
        - fullframe (boolean): [optional] If set to "true" the snapshot will be taken at full sensor resolution. This will error if used with timestamp.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'monitor'],
            'operation': 'generateDeviceCameraSnapshot'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/generateSnapshot'

        body_params = ['timestamp', 'fullframe', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getDeviceCameraQualityAndRetention(self, serial: str):
        """
        **Returns quality and retention settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-quality-and-retention

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityAndRetention'],
            'operation': 'getDeviceCameraQualityAndRetention'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/qualityAndRetention'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraQualityAndRetention(self, serial: str, **kwargs):
        """
        **Update quality and retention settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-quality-and-retention

        - serial (string): Serial
        - profileId (string): The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        - motionBasedRetentionEnabled (boolean): Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera.
        - audioRecordingEnabled (boolean): Boolean indicating if audio recording is enabled(true) or disabled(false) on the camera
        - restrictedBandwidthModeEnabled (boolean): Boolean indicating if restricted bandwidth is enabled(true) or disabled(false) on the camera. This setting does not apply to MV2 cameras.
        - quality (string): Quality of the camera. Can be one of 'Standard', 'High' or 'Enhanced'. Not all qualities are supported by every camera model.
        - resolution (string): Resolution of the camera. Can be one of '1280x720', '1920x1080', '1080x1080', '2112x2112', '2880x2880', '2688x1512' or '3840x2160'.Not all resolutions are supported by every camera model.
        - motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        """

        kwargs.update(locals())

        if 'quality' in kwargs:
            options = ['Enhanced', 'High', 'Standard']
            assert kwargs['quality'] in options, f'''"quality" cannot be "{kwargs['quality']}", & must be set to one of: {options}'''
        if 'resolution' in kwargs:
            options = ['1080x1080', '1280x720', '1920x1080', '2112x2112', '2688x1512', '2880x2880', '3840x2160']
            assert kwargs['resolution'] in options, f'''"resolution" cannot be "{kwargs['resolution']}", & must be set to one of: {options}'''
        if 'motionDetectorVersion' in kwargs:
            options = [1, 2]
            assert kwargs['motionDetectorVersion'] in options, f'''"motionDetectorVersion" cannot be "{kwargs['motionDetectorVersion']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['camera', 'configure', 'qualityAndRetention'],
            'operation': 'updateDeviceCameraQualityAndRetention'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/qualityAndRetention'

        body_params = ['profileId', 'motionBasedRetentionEnabled', 'audioRecordingEnabled', 'restrictedBandwidthModeEnabled', 'quality', 'resolution', 'motionDetectorVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCameraSense(self, serial: str):
        """
        **Returns sense settings for a given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'configure', 'sense'],
            'operation': 'getDeviceCameraSense'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/sense'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraSense(self, serial: str, **kwargs):
        """
        **Update sense settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-sense

        - serial (string): Serial
        - senseEnabled (boolean): Boolean indicating if sense(license) is enabled(true) or disabled(false) on the camera
        - mqttBrokerId (string): The ID of the MQTT broker to be enabled on the camera. A value of null will disable MQTT on the camera
        - audioDetection (object): The details of the audio detection config.
        - detectionModelId (string): The ID of the object detection model
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'sense'],
            'operation': 'updateDeviceCameraSense'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/sense'

        body_params = ['senseEnabled', 'mqttBrokerId', 'audioDetection', 'detectionModelId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCameraSenseObjectDetectionModels(self, serial: str):
        """
        **Returns the MV Sense object detection model list for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-sense-object-detection-models

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'configure', 'sense', 'objectDetectionModels'],
            'operation': 'getDeviceCameraSenseObjectDetectionModels'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/sense/objectDetectionModels'

        return self._session.get(metadata, resource)
        


    def getDeviceCameraVideoSettings(self, serial: str):
        """
        **Returns video settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-settings

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'configure', 'video', 'settings'],
            'operation': 'getDeviceCameraVideoSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/video/settings'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraVideoSettings(self, serial: str, **kwargs):
        """
        **Update video settings for the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-video-settings

        - serial (string): Serial
        - externalRtspEnabled (boolean): Boolean indicating if external rtsp stream is exposed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'video', 'settings'],
            'operation': 'updateDeviceCameraVideoSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/video/settings'

        body_params = ['externalRtspEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceCameraVideoLink(self, serial: str, **kwargs):
        """
        **Returns video link to the specified camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-video-link

        - serial (string): Serial
        - timestamp (string): [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'videoLink'],
            'operation': 'getDeviceCameraVideoLink'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/videoLink'

        query_params = ['timestamp', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceCameraWirelessProfiles(self, serial: str):
        """
        **Returns wireless profile assigned to the given camera**
        https://developer.cisco.com/meraki/api-v1/#!get-device-camera-wireless-profiles

        - serial (string): Serial
        """

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'getDeviceCameraWirelessProfiles'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/wirelessProfiles'

        return self._session.get(metadata, resource)
        


    def updateDeviceCameraWirelessProfiles(self, serial: str, ids: dict):
        """
        **Assign wireless profiles to the given camera**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-wireless-profiles

        - serial (string): Serial
        - ids (object): The ids of the wireless profile to assign to the given camera
        """

        kwargs = locals()

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'updateDeviceCameraWirelessProfiles'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/wirelessProfiles'

        body_params = ['ids', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkCameraQualityRetentionProfiles(self, networkId: str):
        """
        **List the quality retention profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profiles

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'getNetworkCameraQualityRetentionProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles'

        return self._session.get(metadata, resource)
        


    def createNetworkCameraQualityRetentionProfile(self, networkId: str, name: str, **kwargs):
        """
        **Creates new quality retention profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-camera-quality-retention-profile

        - networkId (string): Network ID
        - name (string): The name of the new profile. Must be unique. This parameter is required.
        - motionBasedRetentionEnabled (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
        - restrictedBandwidthModeEnabled (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
        - audioRecordingEnabled (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
        - cloudArchiveEnabled (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
        - motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        - smartRetention (object): Smart Retention records footage in two qualities and intelligently retains higher quality when motion, people or vehicles are detected.
        - scheduleId (string): Schedule for which this camera will record video, or 'null' to always record.
        - maxRetentionDays (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days.
        - videoSettings (object): Video quality and resolution settings for all the camera models.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'createNetworkCameraQualityRetentionProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles'

        body_params = ['name', 'motionBasedRetentionEnabled', 'restrictedBandwidthModeEnabled', 'audioRecordingEnabled', 'cloudArchiveEnabled', 'motionDetectorVersion', 'smartRetention', 'scheduleId', 'maxRetentionDays', 'videoSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str):
        """
        **Retrieve a single quality retention profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-quality-retention-profile

        - networkId (string): Network ID
        - qualityRetentionProfileId (string): Quality retention profile ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'getNetworkCameraQualityRetentionProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        qualityRetentionProfileId = urllib.parse.quote(str(qualityRetentionProfileId), safe='')
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str, **kwargs):
        """
        **Update an existing quality retention profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-camera-quality-retention-profile

        - networkId (string): Network ID
        - qualityRetentionProfileId (string): Quality retention profile ID
        - name (string): The name of the new profile. Must be unique.
        - motionBasedRetentionEnabled (boolean): Deletes footage older than 3 days in which no motion was detected. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
        - restrictedBandwidthModeEnabled (boolean): Disable features that require additional bandwidth such as Motion Recap. Can be either true or false. Defaults to false. This setting does not apply to MV2 cameras.
        - audioRecordingEnabled (boolean): Whether or not to record audio. Can be either true or false. Defaults to false.
        - cloudArchiveEnabled (boolean): Create redundant video backup using Cloud Archive. Can be either true or false. Defaults to false.
        - motionDetectorVersion (integer): The version of the motion detector that will be used by the camera. Only applies to Gen 2 cameras. Defaults to v2.
        - smartRetention (object): Smart Retention records footage in two qualities and intelligently retains higher quality when motion, people or vehicles are detected.
        - scheduleId (string): Schedule for which this camera will record video, or 'null' to always record.
        - maxRetentionDays (integer): The maximum number of days for which the data will be stored, or 'null' to keep data until storage space runs out. If the former, it can be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 30, 60, 90] days.
        - videoSettings (object): Video quality and resolution settings for all the camera models.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'updateNetworkCameraQualityRetentionProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        qualityRetentionProfileId = urllib.parse.quote(str(qualityRetentionProfileId), safe='')
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        body_params = ['name', 'motionBasedRetentionEnabled', 'restrictedBandwidthModeEnabled', 'audioRecordingEnabled', 'cloudArchiveEnabled', 'motionDetectorVersion', 'smartRetention', 'scheduleId', 'maxRetentionDays', 'videoSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str):
        """
        **Delete an existing quality retention profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-quality-retention-profile

        - networkId (string): Network ID
        - qualityRetentionProfileId (string): Quality retention profile ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'qualityRetentionProfiles'],
            'operation': 'deleteNetworkCameraQualityRetentionProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        qualityRetentionProfileId = urllib.parse.quote(str(qualityRetentionProfileId), safe='')
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkCameraSchedules(self, networkId: str):
        """
        **Returns a list of all camera recording schedules.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-schedules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'schedules'],
            'operation': 'getNetworkCameraSchedules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/camera/schedules'

        return self._session.get(metadata, resource)
        


    def createNetworkCameraWirelessProfile(self, networkId: str, name: str, ssid: dict, **kwargs):
        """
        **Creates a new camera wireless profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!create-network-camera-wireless-profile

        - networkId (string): Network ID
        - name (string): The name of the camera wireless profile. This parameter is required.
        - ssid (object): The details of the SSID config.
        - identity (object): The identity of the wireless profile. Required for creating wireless profiles in 8021x-radius auth mode.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'createNetworkCameraWirelessProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/camera/wirelessProfiles'

        body_params = ['name', 'ssid', 'identity', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkCameraWirelessProfiles(self, networkId: str):
        """
        **List the camera wireless profiles for this network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-wireless-profiles

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'getNetworkCameraWirelessProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/camera/wirelessProfiles'

        return self._session.get(metadata, resource)
        


    def getNetworkCameraWirelessProfile(self, networkId: str, wirelessProfileId: str):
        """
        **Retrieve a single camera wireless profile.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-camera-wireless-profile

        - networkId (string): Network ID
        - wirelessProfileId (string): Wireless profile ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'getNetworkCameraWirelessProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        wirelessProfileId = urllib.parse.quote(str(wirelessProfileId), safe='')
        resource = f'/networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkCameraWirelessProfile(self, networkId: str, wirelessProfileId: str, **kwargs):
        """
        **Update an existing camera wireless profile in this network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-camera-wireless-profile

        - networkId (string): Network ID
        - wirelessProfileId (string): Wireless profile ID
        - name (string): The name of the camera wireless profile.
        - ssid (object): The details of the SSID config.
        - identity (object): The identity of the wireless profile. Required for creating wireless profiles in 8021x-radius auth mode.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'updateNetworkCameraWirelessProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        wirelessProfileId = urllib.parse.quote(str(wirelessProfileId), safe='')
        resource = f'/networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId}'

        body_params = ['name', 'ssid', 'identity', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkCameraWirelessProfile(self, networkId: str, wirelessProfileId: str):
        """
        **Delete an existing camera wireless profile for this network.**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-camera-wireless-profile

        - networkId (string): Network ID
        - wirelessProfileId (string): Wireless profile ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'deleteNetworkCameraWirelessProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        wirelessProfileId = urllib.parse.quote(str(wirelessProfileId), safe='')
        resource = f'/networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationCameraBoundariesAreasByDevice(self, organizationId: str, **kwargs):
        """
        **Returns all configured area boundaries of cameras**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-boundaries-areas-by-device

        - organizationId (string): Organization ID
        - serials (array): A list of serial numbers. The returned cameras will be filtered to only include these serials.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'boundaries', 'areas', 'byDevice'],
            'operation': 'getOrganizationCameraBoundariesAreasByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/boundaries/areas/byDevice'

        query_params = ['serials', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationCameraBoundariesLinesByDevice(self, organizationId: str, **kwargs):
        """
        **Returns all configured crossingline boundaries of cameras**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-boundaries-lines-by-device

        - organizationId (string): Organization ID
        - serials (array): A list of serial numbers. The returned cameras will be filtered to only include these serials.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'boundaries', 'lines', 'byDevice'],
            'operation': 'getOrganizationCameraBoundariesLinesByDevice'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/boundaries/lines/byDevice'

        query_params = ['serials', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def getOrganizationCameraCustomAnalyticsArtifacts(self, organizationId: str):
        """
        **List Custom Analytics Artifacts**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-custom-analytics-artifacts

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'customAnalytics', 'artifacts'],
            'operation': 'getOrganizationCameraCustomAnalyticsArtifacts'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/customAnalytics/artifacts'

        return self._session.get(metadata, resource)
        


    def createOrganizationCameraCustomAnalyticsArtifact(self, organizationId: str, **kwargs):
        """
        **Create custom analytics artifact**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-camera-custom-analytics-artifact

        - organizationId (string): Organization ID
        - name (string): Unique name of the artifact
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'customAnalytics', 'artifacts'],
            'operation': 'createOrganizationCameraCustomAnalyticsArtifact'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/customAnalytics/artifacts'

        body_params = ['name', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationCameraCustomAnalyticsArtifact(self, organizationId: str, artifactId: str):
        """
        **Get Custom Analytics Artifact**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-custom-analytics-artifact

        - organizationId (string): Organization ID
        - artifactId (string): Artifact ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'customAnalytics', 'artifacts'],
            'operation': 'getOrganizationCameraCustomAnalyticsArtifact'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        artifactId = urllib.parse.quote(str(artifactId), safe='')
        resource = f'/organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId}'

        return self._session.get(metadata, resource)
        


    def deleteOrganizationCameraCustomAnalyticsArtifact(self, organizationId: str, artifactId: str):
        """
        **Delete Custom Analytics Artifact**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-camera-custom-analytics-artifact

        - organizationId (string): Organization ID
        - artifactId (string): Artifact ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'customAnalytics', 'artifacts'],
            'operation': 'deleteOrganizationCameraCustomAnalyticsArtifact'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        artifactId = urllib.parse.quote(str(artifactId), safe='')
        resource = f'/organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId}'

        return self._session.delete(metadata, resource)
        


    def getOrganizationCameraDetectionsHistoryByBoundaryByInterval(self, organizationId: str, boundaryIds: list, total_pages=1, direction='next', **kwargs):
        """
        **Returns analytics data for timespans**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-detections-history-by-boundary-by-interval

        - organizationId (string): Organization ID
        - boundaryIds (array): A list of boundary ids. The returned cameras will be filtered to only include these ids.
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - duration (integer): The minimum time, in seconds, that the person or car remains in the area to be counted. Defaults to boundary configuration or 60.
        - perPage (integer): The number of entries per page returned. Acceptable range is 1 - 1000. Defaults to 1000.
        - boundaryTypes (array): The detection types. Defaults to 'person'.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'detections', 'history', 'byBoundary', 'byInterval'],
            'operation': 'getOrganizationCameraDetectionsHistoryByBoundaryByInterval'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/detections/history/byBoundary/byInterval'

        query_params = ['boundaryIds', 'duration', 'perPage', 'boundaryTypes', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['boundaryIds', 'boundaryTypes', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationCameraOnboardingStatuses(self, organizationId: str, **kwargs):
        """
        **Fetch onboarding status of cameras**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-onboarding-statuses

        - organizationId (string): Organization ID
        - serials (array): A list of serial numbers. The returned cameras will be filtered to only include these serials.
        - networkIds (array): A list of network IDs. The returned cameras will be filtered to only include these networks.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'onboarding', 'statuses'],
            'operation': 'getOrganizationCameraOnboardingStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/onboarding/statuses'

        query_params = ['serials', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['serials', 'networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get(metadata, resource, params)
        


    def updateOrganizationCameraOnboardingStatuses(self, organizationId: str, **kwargs):
        """
        **Notify that credential handoff to camera has completed**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-camera-onboarding-statuses

        - organizationId (string): Organization ID
        - serial (string): Serial of camera
        - wirelessCredentialsSent (boolean): Note whether credentials were sent successfully
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'onboarding', 'statuses'],
            'operation': 'updateOrganizationCameraOnboardingStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/onboarding/statuses'

        body_params = ['serial', 'wirelessCredentialsSent', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationCameraPermissions(self, organizationId: str):
        """
        **List the permissions scopes for this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-permissions

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'permissions'],
            'operation': 'getOrganizationCameraPermissions'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/permissions'

        return self._session.get(metadata, resource)
        


    def getOrganizationCameraPermission(self, organizationId: str, permissionScopeId: str):
        """
        **Retrieve a single permission scope**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-permission

        - organizationId (string): Organization ID
        - permissionScopeId (string): Permission scope ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'permissions'],
            'operation': 'getOrganizationCameraPermission'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        permissionScopeId = urllib.parse.quote(str(permissionScopeId), safe='')
        resource = f'/organizations/{organizationId}/camera/permissions/{permissionScopeId}'

        return self._session.get(metadata, resource)
        


    def getOrganizationCameraRoles(self, organizationId: str):
        """
        **List all the roles in this organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-roles

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'roles'],
            'operation': 'getOrganizationCameraRoles'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/roles'

        return self._session.get(metadata, resource)
        


    def createOrganizationCameraRole(self, organizationId: str, name: str, **kwargs):
        """
        **Creates new role for this organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-camera-role

        - organizationId (string): Organization ID
        - name (string): The name of the new role. Must be unique. This parameter is required.
        - appliedOnDevices (array): Device tag on which this specified permission is applied.
        - appliedOnNetworks (array): Network tag on which this specified permission is applied.
        - appliedOrgWide (array): Permissions to be applied org wide.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'roles'],
            'operation': 'createOrganizationCameraRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/camera/roles'

        body_params = ['name', 'appliedOnDevices', 'appliedOnNetworks', 'appliedOrgWide', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getOrganizationCameraRole(self, organizationId: str, roleId: str):
        """
        **Retrieve a single role.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-camera-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'roles'],
            'operation': 'getOrganizationCameraRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        roleId = urllib.parse.quote(str(roleId), safe='')
        resource = f'/organizations/{organizationId}/camera/roles/{roleId}'

        return self._session.get(metadata, resource)
        


    def deleteOrganizationCameraRole(self, organizationId: str, roleId: str):
        """
        **Delete an existing role for this organization.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-camera-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        """

        metadata = {
            'tags': ['camera', 'configure', 'roles'],
            'operation': 'deleteOrganizationCameraRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        roleId = urllib.parse.quote(str(roleId), safe='')
        resource = f'/organizations/{organizationId}/camera/roles/{roleId}'

        return self._session.delete(metadata, resource)
        


    def updateOrganizationCameraRole(self, organizationId: str, roleId: str, **kwargs):
        """
        **Update an existing role in this organization.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-camera-role

        - organizationId (string): Organization ID
        - roleId (string): Role ID
        - name (string): The name of the new role. Must be unique.
        - appliedOnDevices (array): Device tag on which this specified permission is applied.
        - appliedOnNetworks (array): Network tag on which this specified permission is applied.
        - appliedOrgWide (array): Permissions to be applied org wide.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'roles'],
            'operation': 'updateOrganizationCameraRole'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        roleId = urllib.parse.quote(str(roleId), safe='')
        resource = f'/organizations/{organizationId}/camera/roles/{roleId}'

        body_params = ['name', 'appliedOnDevices', 'appliedOnNetworks', 'appliedOrgWide', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        
