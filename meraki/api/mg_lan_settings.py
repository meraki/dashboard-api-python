class MGLANSettings(object):
    def __init__(self, session):
        super(MGLANSettings, self).__init__()
        self._session = session
    
    def getDeviceCellularGatewaySettings(self, serial: str):
        """
        **Show the LAN Settings of a MG**
        https://api.meraki.com/api_docs#show-the-lan-settings-of-a-mg
        
        - serial (string)
        """

        metadata = {
            'tags': ['MG LAN settings'],
            'operation': 'getDeviceCellularGatewaySettings',
        }
        resource = f'/devices/{serial}/cellularGateway/settings'

        return self._session.get(metadata, resource)

    def updateDeviceCellularGatewaySettings(self, serial: str, **kwargs):
        """
        **Update the LAN Settings for a single MG.**
        https://api.meraki.com/api_docs#update-the-lan-settings-for-a-single-mg
        
        - serial (string)
        - reservedIpRanges (array): list of all reserved IP ranges for a single MG
        - fixedIpAssignments (array): list of all fixed IP assignments for a single MG
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MG LAN settings'],
            'operation': 'updateDeviceCellularGatewaySettings',
        }
        resource = f'/devices/{serial}/cellularGateway/settings'

        body_params = ['reservedIpRanges', 'fixedIpAssignments']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

