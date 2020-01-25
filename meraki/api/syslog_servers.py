class SyslogServers(object):
    def __init__(self, session):
        super(SyslogServers, self).__init__()
        self._session = session
    
    def getNetworkSyslogServers(self, networkId: str):
        """
        **List the syslog servers for a network**
        https://api.meraki.com/api_docs#list-the-syslog-servers-for-a-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Syslog servers'],
            'operation': 'getNetworkSyslogServers',
        }
        resource = f'/networks/{networkId}/syslogServers'

        return self._session.get(metadata, resource)

    def updateNetworkSyslogServers(self, networkId: str, servers: list):
        """
        **Update the syslog servers for a network**
        https://api.meraki.com/api_docs#update-the-syslog-servers-for-a-network
        
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
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

