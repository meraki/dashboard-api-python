class RadioSettings(object):
    def __init__(self, session):
        super(RadioSettings, self).__init__()
        self._session = session
    
    def getNetworkDeviceWirelessRadioSettings(self, networkId: str, serial: str):
        """
        **Return the radio settings of a device**
        https://developer.cisco.com/meraki/api/#!get-network-device-wireless-radio-settings
        
        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'getNetworkDeviceWirelessRadioSettings',
        }
        resource = f'/networks/{networkId}/devices/{serial}/wireless/radioSettings'

        return self._session.get(metadata, resource)

    def updateNetworkDeviceWirelessRadioSettings(self, networkId: str, serial: str, **kwargs):
        """
        **Update the radio settings of a device**
        https://developer.cisco.com/meraki/api/#!update-network-device-wireless-radio-settings
        
        - networkId (string)
        - serial (string)
        - rfProfileId (integer):     The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile
    (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides
    on the device (channel width, channel, power).

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'updateNetworkDeviceWirelessRadioSettings',
        }
        resource = f'/networks/{networkId}/devices/{serial}/wireless/radioSettings'

        body_params = ['rfProfileId']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkWirelessRfProfiles(self, networkId: str, **kwargs):
        """
        **List the non-basic RF profiles for this network**
        https://developer.cisco.com/meraki/api/#!get-network-wireless-rf-profiles
        
        - networkId (string)
        - includeTemplateProfiles (boolean):     If the network is bound to a template, this parameter controls whether or not the non-basic RF profiles defined on the template
    should be included in the response alongside the non-basic profiles defined on the bound network. Defaults to false.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'getNetworkWirelessRfProfiles',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        query_params = ['includeTemplateProfiles']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def createNetworkWirelessRfProfile(self, networkId: str, name: str, bandSelectionType: str, **kwargs):
        """
        **Creates new RF profile for this network**
        https://developer.cisco.com/meraki/api/#!create-network-wireless-rf-profile
        
        - networkId (string)
        - name (string): The name of the new profile. Must be unique. This param is required on creation.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'. This param is required on creation.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false. Defaults to true.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'. Defaults to band.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ssid', 'ap']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'createNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def updateNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/meraki/api/#!update-network-wireless-rf-profile
        
        - networkId (string)
        - rfProfileId (string)
        - name (string): The name of the new profile. Must be unique.
        - clientBalancingEnabled (boolean): Steers client to best available access point. Can be either true or false.
        - minBitrateType (string): Minimum bitrate can be set to either 'band' or 'ssid'.
        - bandSelectionType (string): Band selection can be set to either 'ssid' or 'ap'.
        - apBandSettings (object): Settings that will be enabled if selectionType is set to 'ap'.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        """

        kwargs.update(locals())

        if 'minBitrateType' in kwargs:
            options = ['band', 'ssid']
            assert kwargs['minBitrateType'] in options, f'''"minBitrateType" cannot be "{kwargs['minBitrateType']}", & must be set to one of: {options}'''
        if 'bandSelectionType' in kwargs:
            options = ['ssid', 'ap']
            assert kwargs['bandSelectionType'] in options, f'''"bandSelectionType" cannot be "{kwargs['bandSelectionType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'updateNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        body_params = ['name', 'clientBalancingEnabled', 'minBitrateType', 'bandSelectionType', 'apBandSettings', 'twoFourGhzSettings', 'fiveGhzSettings']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/meraki/api/#!delete-network-wireless-rf-profile
        
        - networkId (string)
        - rfProfileId (string)
        """

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'deleteNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        return self._session.delete(metadata, resource)

    def getNetworkWirelessRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Return a RF profile**
        https://developer.cisco.com/meraki/api/#!get-network-wireless-rf-profile
        
        - networkId (string)
        - rfProfileId (string)
        """

        metadata = {
            'tags': ['Radio settings'],
            'operation': 'getNetworkWirelessRfProfile',
        }
        resource = f'/networks/{networkId}/wireless/rfProfiles/{rfProfileId}'

        return self._session.get(metadata, resource)

