import urllib


class Administered(object):
    def __init__(self, session):
        super(Administered, self).__init__()
        self._session = session
        


    def getAdministeredIdentitiesMe(self):
        """
        **Returns the identity of the current user.**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me

        """

        metadata = {
            'tags': ['administered', 'monitor', 'identities', 'me'],
            'operation': 'getAdministeredIdentitiesMe'
        }
        resource = f'/administered/identities/me'

        return self._session.get(metadata, resource)
        


    def createAdministeredIdentitiesMeEarlyAccessFeaturesOptIn(self, shortName: str):
        """
        **Enables the early access feature for the identity.**
        https://developer.cisco.com/meraki/api-v1/#!create-administered-identities-me-early-access-features-opt-in

        - shortName (string): The desired early access feature
        """

        kwargs = locals()

        if 'shortName' in kwargs:
            options = ['has_cross_org_page_access']
            assert kwargs['shortName'] in options, f'''"shortName" cannot be "{kwargs['shortName']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['administered', 'configure', 'identities', 'me', 'earlyAccess', 'features', 'optIns'],
            'operation': 'createAdministeredIdentitiesMeEarlyAccessFeaturesOptIn'
        }
        resource = f'/administered/identities/me/earlyAccess/features/optIns'

        body_params = ['shortName', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getAdministeredIdentitiesMeEarlyAccessFeaturesOptIns(self):
        """
        **Returns list of enabled early access features for the identity.**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me-early-access-features-opt-ins

        """

        metadata = {
            'tags': ['administered', 'configure', 'identities', 'me', 'earlyAccess', 'features', 'optIns'],
            'operation': 'getAdministeredIdentitiesMeEarlyAccessFeaturesOptIns'
        }
        resource = f'/administered/identities/me/earlyAccess/features/optIns'

        return self._session.get(metadata, resource)
        


    def deleteAdministeredIdentitiesMeEarlyAccessFeaturesOptIn(self, featureShortName: str):
        """
        **Disables the early access feature for the identity.**
        https://developer.cisco.com/meraki/api-v1/#!delete-administered-identities-me-early-access-features-opt-in

        - featureShortName (string): (required)
        """

        metadata = {
            'tags': ['administered', 'configure', 'identities', 'me', 'earlyAccess', 'features', 'optIns'],
            'operation': 'deleteAdministeredIdentitiesMeEarlyAccessFeaturesOptIn'
        }
        featureShortName = urllib.parse.quote(str(featureShortName), safe='')
        resource = f'/administered/identities/me/earlyAccess/features/optIns/{featureShortName}'

        return self._session.delete(metadata, resource)
        
