class ActionBatchCamera(object):
    def __init__(self):
        super(ActionBatchCamera, self).__init__()
        


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
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        



