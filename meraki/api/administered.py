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
        
