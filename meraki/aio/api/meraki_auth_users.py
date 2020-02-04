class AsyncMerakiAuthUsers:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkMerakiAuthUsers(self, networkId: str):
        """
        **List the splash or RADIUS users configured under Meraki Authentication for a network**
        https://api.meraki.com/api_docs#list-the-splash-or-radius-users-configured-under-meraki-authentication-for-a-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Meraki auth users'],
            'operation': 'getNetworkMerakiAuthUsers',
        }
        resource = f'/networks/{networkId}/merakiAuthUsers'

        return await self._session.get(metadata, resource)

    async def getNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str):
        """
        **Return the Meraki Auth splash or RADIUS user**
        https://api.meraki.com/api_docs#return-the-meraki-auth-splash-or-radius-user
        
        - networkId (string)
        - merakiAuthUserId (string)
        """

        metadata = {
            'tags': ['Meraki auth users'],
            'operation': 'getNetworkMerakiAuthUser',
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        return await self._session.get(metadata, resource)

