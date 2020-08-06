class Floorplans(object):
    def __init__(self, session):
        super(FloorPlans, self).__init__()
        self._session = session
    
    def getNetworkFloorPlans(self, networkId: str):
        """
        **List the floor plans that belong to your network**
        https://developer.cisco.com/meraki/api/#!get-network-floor-plans
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Floor plans'],
            'operation': 'getNetworkFloorPlans',
        }
        resource = f'/networks/{networkId}/floorPlans'

        return self._session.get(metadata, resource)

    def createNetworkFloorPlan(self, networkId: str, name: str, imageContents: str, **kwargs):
        """
        **Upload a floor plan**
        https://developer.cisco.com/meraki/api/#!create-network-floor-plan
        
        - networkId (string)
        - name (string): The name of your floor plan.
        - imageContents (string): The file contents (a base 64 encoded string) of your image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in.
        - center (object): The longitude and latitude of the center of your floor plan. The 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Floor plans'],
            'operation': 'createNetworkFloorPlan',
        }
        resource = f'/networks/{networkId}/floorPlans'

        body_params = ['name', 'center', 'bottomLeftCorner', 'bottomRightCorner', 'topLeftCorner', 'topRightCorner', 'imageContents']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkFloorPlan(self, networkId: str, floorPlanId: str):
        """
        **Find a floor plan by ID**
        https://developer.cisco.com/meraki/api/#!get-network-floor-plan
        
        - networkId (string)
        - floorPlanId (string)
        """

        metadata = {
            'tags': ['Floor plans'],
            'operation': 'getNetworkFloorPlan',
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        return self._session.get(metadata, resource)

    def updateNetworkFloorPlan(self, networkId: str, floorPlanId: str, **kwargs):
        """
        **Update a floor plan's geolocation and other meta data**
        https://developer.cisco.com/meraki/api/#!update-network-floor-plan
        
        - networkId (string)
        - floorPlanId (string)
        - name (string): The name of your floor plan.
        - center (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        - imageContents (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Floor plans'],
            'operation': 'updateNetworkFloorPlan',
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        body_params = ['name', 'center', 'bottomLeftCorner', 'bottomRightCorner', 'topLeftCorner', 'topRightCorner', 'imageContents']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkFloorPlan(self, networkId: str, floorPlanId: str):
        """
        **Destroy a floor plan**
        https://developer.cisco.com/meraki/api/#!delete-network-floor-plan
        
        - networkId (string)
        - floorPlanId (string)
        """

        metadata = {
            'tags': ['Floor plans'],
            'operation': 'deleteNetworkFloorPlan',
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        return self._session.delete(metadata, resource)

