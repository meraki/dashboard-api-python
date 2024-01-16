import urllib


class ActionBatchCamera(object):
    def __init__(self):
        super(ActionBatchCamera, self).__init__()
        


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
        resource = f'/devices/{serial}/camera/customAnalytics'

        body_params = ['enabled', 'artifactId', 'parameters', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





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
        resource = f'/devices/{serial}/camera/sense'

        body_params = ['senseEnabled', 'mqttBrokerId', 'audioDetection', 'detectionModelId', ]
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

        - serial (string): Serial
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
        





    def updateDeviceCameraWirelessProfiles(self, serial: str, ids: dict):
        """
        **Assign wireless profiles to the given camera. Incremental updates are not supported, all profile assignment need to be supplied at once.**
        https://developer.cisco.com/meraki/api-v1/#!update-device-camera-wireless-profiles

        - serial (string): Serial
        - ids (object): The ids of the wireless profile to assign to the given camera
        """

        kwargs = locals()

        metadata = {
            'tags': ['camera', 'configure', 'wirelessProfiles'],
            'operation': 'updateDeviceCameraWirelessProfiles'
        }
        resource = f'/devices/{serial}/camera/wirelessProfiles'

        body_params = ['ids', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        



