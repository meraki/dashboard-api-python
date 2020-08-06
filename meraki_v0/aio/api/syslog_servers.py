class AsyncSyslogServers:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetworkSyslogServers(self, networkId: str):
        """
        **List the syslog servers for a network**
        https://developer.cisco.com/meraki/api/#!get-network-syslog-servers
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Syslog servers'],
            'operation': 'getNetworkSyslogServers',
        }
        resource = f'/networks/{networkId}/syslogServers'

        return await self._session.get(metadata, resource)

    async def updateNetworkSyslogServers(self, networkId: str, servers: list):
        """
        **Update the syslog servers for a network**
        https://developer.cisco.com/meraki/api/#!update-network-syslog-servers
        
        - networkId (string)
        - servers (array): A list of the syslog servers for this network
        """

        kwargs = locals()

        metadata = {
            'tags': ['Syslog servers'],
            'operation': 'updateNetworkSyslogServers',
        }
        resource = f'/networks/{networkId}/syslogServers'

        body_params = ['servers']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

