class Cameras(object):
    def __init__(self, session):
        super(Cameras, self).__init__()
        self._session = session
    
    def generateNetworkCameraSnapshot(self, networkId: str, serial: str, **kwargs):
        """
        **Generate a snapshot of what the camera sees at the specified time and return a link to that image.**
        https://api.meraki.com/api_docs#generate-a-snapshot-of-what-the-camera-sees-at-the-specified-time-and-return-a-link-to-that-image
        - networkId (string)
        - serial (string)
        - timestamp (string): [optional] The snapshot will be taken from this time on the camera. The timestamp is expected to be in ISO 8601 format. If no timestamp is specified, we will assume current time.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Cameras'],
            'operation': 'generateNetworkCameraSnapshot',
        }
        resource = f'/networks/{networkId}/cameras/{serial}/snapshot'

        body_params = ['timestamp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkCameraVideoLink(self, networkId: str, serial: str, **kwargs):
        """
        **Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.**
        https://api.meraki.com/api_docs#returns-video-link-to-the-specified-camera
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
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

