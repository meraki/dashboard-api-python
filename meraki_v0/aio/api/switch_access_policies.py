class AsyncSwitchAccessPolicies:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkAccessPolicies(self, networkId: str):
        """
        **List the access policies for this network. Only valid for MS networks.**
        https://developer.cisco.com/meraki/api/#!get-network-access-policies
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch access policies'],
            'operation': 'getNetworkAccessPolicies',
        }
        resource = f'/networks/{networkId}/accessPolicies'

        return await self._session.get(metadata, resource)

