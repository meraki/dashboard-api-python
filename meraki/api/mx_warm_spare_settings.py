class MXWarmSpareSettings(object):
    def __init__(self, session):
        super(MXWarmSpareSettings, self).__init__()
        self._session = session
    
    def swapNetworkWarmspare(self, networkId: str):
        """
        **Swap MX primary and warm spare appliances**
        https://api.meraki.com/api_docs#swap-mx-primary-and-warm-spare-appliances
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX warm spare settings'],
            'operation': 'swapNetworkWarmspare',
        }
        resource = f'/networks/{networkId}/swapWarmSpare'

        return self._session.post(metadata, resource)

    def getNetworkWarmSpareSettings(self, networkId: str):
        """
        **Return MX warm spare settings**
        https://api.meraki.com/api_docs#return-mx-warm-spare-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX warm spare settings'],
            'operation': 'getNetworkWarmSpareSettings',
        }
        resource = f'/networks/{networkId}/warmSpareSettings'

        return self._session.get(metadata, resource)

    def updateNetworkWarmSpareSettings(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update MX warm spare settings**
        https://api.meraki.com/api_docs#update-mx-warm-spare-settings
        
        - networkId (string)
        - enabled (boolean): Enable warm spare
        - spareSerial (string): Serial number of the warm spare appliance
        - uplinkMode (string): Uplink mode, either virtual or public
        - virtualIp1 (string): The WAN 1 shared IP
        - virtualIp2 (string): The WAN 2 shared IP
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX warm spare settings'],
            'operation': 'updateNetworkWarmSpareSettings',
        }
        resource = f'/networks/{networkId}/warmSpareSettings'

        body_params = ['enabled', 'spareSerial', 'uplinkMode', 'virtualIp1', 'virtualIp2']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

