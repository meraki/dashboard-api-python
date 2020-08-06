class CameraQualityRetentionProfiles(object):
    def __init__(self, session):
        super(CameraQualityRetentionProfiles, self).__init__()
        self._session = session
    
    def getNetworkCameraQualityRetentionProfiles(self, networkId: str):
        """
        **List the quality retention profiles for this network**
        https://developer.cisco.com/meraki/api/#!get-network-camera-quality-retention-profiles
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Camera quality retention profiles'],
            'operation': 'getNetworkCameraQualityRetentionProfiles',
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles'

        return self._session.get(metadata, resource)

    def createNetworkCameraQualityRetentionProfile(self, networkId: str, name: str, **kwargs):
        """
        **Creates new quality retention profile for this network.**
        https://developer.cisco.com/meraki/api/#!create-network-camera-quality-retention-profile
        
        - networkId (string)
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
            'tags': ['Camera quality retention profiles'],
            'operation': 'createNetworkCameraQualityRetentionProfile',
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles'

        body_params = ['name', 'motionBasedRetentionEnabled', 'restrictedBandwidthModeEnabled', 'audioRecordingEnabled', 'cloudArchiveEnabled', 'motionDetectorVersion', 'scheduleId', 'maxRetentionDays', 'videoSettings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str):
        """
        **Retrieve a single quality retention profile**
        https://developer.cisco.com/meraki/api/#!get-network-camera-quality-retention-profile
        
        - networkId (string)
        - qualityRetentionProfileId (string)
        """

        metadata = {
            'tags': ['Camera quality retention profiles'],
            'operation': 'getNetworkCameraQualityRetentionProfile',
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        return self._session.get(metadata, resource)

    def updateNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str, **kwargs):
        """
        **Update an existing quality retention profile for this network.**
        https://developer.cisco.com/meraki/api/#!update-network-camera-quality-retention-profile
        
        - networkId (string)
        - qualityRetentionProfileId (string)
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
            'tags': ['Camera quality retention profiles'],
            'operation': 'updateNetworkCameraQualityRetentionProfile',
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        body_params = ['name', 'motionBasedRetentionEnabled', 'restrictedBandwidthModeEnabled', 'audioRecordingEnabled', 'cloudArchiveEnabled', 'motionDetectorVersion', 'scheduleId', 'maxRetentionDays', 'videoSettings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkCameraQualityRetentionProfile(self, networkId: str, qualityRetentionProfileId: str):
        """
        **Delete an existing quality retention profile for this network.**
        https://developer.cisco.com/meraki/api/#!delete-network-camera-quality-retention-profile
        
        - networkId (string)
        - qualityRetentionProfileId (string)
        """

        metadata = {
            'tags': ['Camera quality retention profiles'],
            'operation': 'deleteNetworkCameraQualityRetentionProfile',
        }
        resource = f'/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}'

        return self._session.delete(metadata, resource)

