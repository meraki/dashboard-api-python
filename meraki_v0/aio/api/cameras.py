class AsyncCameras:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getDeviceCameraQualityAndRetentionSettings(self, serial: str):
        """
        **Returns quality and retention settings for the given camera**
        https://developer.cisco.com/meraki/api/#!get-device-camera-quality-and-retention-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['Cameras'],
            'operation': 'getDeviceCameraQualityAndRetentionSettings',
        }
        resource = f'/devices/{serial}/camera/qualityAndRetentionSettings'

        return await self._session.get(metadata, resource)

    async def updateDeviceCameraQualityAndRetentionSettings(self, serial: str, **kwargs):
        """
        **Update quality and retention settings for the given camera**
        https://developer.cisco.com/meraki/api/#!update-device-camera-quality-and-retention-settings
        
        - serial (string)
        - profileId (string): The ID of a quality and retention profile to assign to the camera. The profile's settings will override all of the per-camera quality and retention settings. If the value of this parameter is null, any existing profile will be unassigned from the camera.
        - motionBasedRetentionEnabled (boolean): Boolean indicating if motion-based retention is enabled(true) or disabled(false) on the camera
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
            'tags': ['Cameras'],
            'operation': 'updateDeviceCameraQualityAndRetentionSettings',
        }
        resource = f'/devices/{serial}/camera/qualityAndRetentionSettings'

        body_params = ['profileId', 'motionBasedRetentionEnabled', 'audioRecordingEnabled', 'restrictedBandwidthModeEnabled', 'quality', 'resolution', 'motionDetectorVersion']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getDeviceCameraVideoSettings(self, serial: str):
        """
        **Returns video settings for the given camera**
        https://developer.cisco.com/meraki/api/#!get-device-camera-video-settings
        
        - serial (string)
        """

        metadata = {
            'tags': ['Cameras'],
            'operation': 'getDeviceCameraVideoSettings',
        }
        resource = f'/devices/{serial}/camera/video/settings'

        return await self._session.get(metadata, resource)

    async def updateDeviceCameraVideoSettings(self, serial: str, **kwargs):
        """
        **Update video settings for the given camera**
        https://developer.cisco.com/meraki/api/#!update-device-camera-video-settings
        
        - serial (string)
        - externalRtspEnabled (boolean): Boolean indicating if external rtsp stream is exposed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Cameras'],
            'operation': 'updateDeviceCameraVideoSettings',
        }
        resource = f'/devices/{serial}/camera/video/settings'

        body_params = ['externalRtspEnabled']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def getNetworkCameraSchedules(self, networkId: str):
        """
        **Returns a list of all camera recording schedules.**
        https://developer.cisco.com/meraki/api/#!get-network-camera-schedules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Cameras'],
            'operation': 'getNetworkCameraSchedules',
        }
        resource = f'/networks/{networkId}/camera/schedules'

        return await self._session.get(metadata, resource)

    async def generateNetworkCameraSnapshot(self, networkId: str, serial: str, **kwargs):
        """
        **Generate a snapshot of what the camera sees at the specified time and return a link to that image.**
        https://developer.cisco.com/meraki/api/#!generate-network-camera-snapshot
        
        - networkId (string)
        - serial (string)
        - timestamp (string): [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
        - fullframe (boolean): [optional] If set to "true" the snapshot will be taken at full sensor resolution. This will error if used with timestamp.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Cameras'],
            'operation': 'generateNetworkCameraSnapshot',
        }
        resource = f'/networks/{networkId}/cameras/{serial}/snapshot'

        body_params = ['timestamp', 'fullframe']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkCameraVideoLink(self, networkId: str, serial: str, **kwargs):
        """
        **Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.**
        https://developer.cisco.com/meraki/api/#!get-network-camera-video-link
        
        - networkId (string)
        - serial (string)
        - timestamp (string): [optional] The video link will start at this timestamp. The timestamp is in UNIX Epoch time (milliseconds). If no timestamp is specified, we will assume current time.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Cameras'],
            'operation': 'getNetworkCameraVideoLink',
        }
        resource = f'/networks/{networkId}/cameras/{serial}/videoLink'

        query_params = ['timestamp']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

