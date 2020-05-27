class MerakiAuthUsers(object):
    def __init__(self, session):
        super(MerakiAuthUsers, self).__init__()
        self._session = session
    
    def getNetworkMerakiAuthUsers(self, networkId: str):
        """
        **List the splash or RADIUS users configured under Meraki Authentication for a network**
        https://developer.cisco.com/meraki/api/#!get-network-meraki-auth-users
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Meraki auth users'],
            'operation': 'getNetworkMerakiAuthUsers',
        }
        resource = f'/networks/{networkId}/merakiAuthUsers'

        return self._session.get(metadata, resource)

    def getNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str):
        """
        **Return the Meraki Auth splash or RADIUS user**
        https://developer.cisco.com/meraki/api/#!get-network-meraki-auth-user
        
        - networkId (string)
        - merakiAuthUserId (string)
        """

        metadata = {
            'tags': ['Meraki auth users'],
            'operation': 'getNetworkMerakiAuthUser',
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        return self._session.get(metadata, resource)

