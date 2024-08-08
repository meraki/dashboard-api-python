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
        


    def getAdministeredIdentitiesMeApiKeys(self):
        """
        **List the non-sensitive metadata associated with the API keys that belong to the user**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me-api-keys

        """

        metadata = {
            'tags': ['administered', 'configure', 'identities', 'me', 'api', 'keys'],
            'operation': 'getAdministeredIdentitiesMeApiKeys'
        }
        resource = f'/administered/identities/me/api/keys'

        return self._session.get(metadata, resource)
        


    def generateAdministeredIdentitiesMeApiKeys(self):
        """
        **Generates an API key for an identity**
        https://developer.cisco.com/meraki/api-v1/#!generate-administered-identities-me-api-keys

        """

        metadata = {
            'tags': ['administered', 'configure', 'identities', 'me', 'api', 'keys'],
            'operation': 'generateAdministeredIdentitiesMeApiKeys'
        }
        resource = f'/administered/identities/me/api/keys/generate'

        return self._session.post(metadata, resource)
        


    def revokeAdministeredIdentitiesMeApiKeys(self, suffix: str):
        """
        **Revokes an identity's API key, using the last four characters of the key**
        https://developer.cisco.com/meraki/api-v1/#!revoke-administered-identities-me-api-keys

        - suffix (string): Suffix
        """

        metadata = {
            'tags': ['administered', 'configure', 'identities', 'me', 'api', 'keys'],
            'operation': 'revokeAdministeredIdentitiesMeApiKeys'
        }
        suffix = urllib.parse.quote(str(suffix), safe='')
        resource = f'/administered/identities/me/api/keys/{suffix}/revoke'

        return self._session.post(metadata, resource)
        
