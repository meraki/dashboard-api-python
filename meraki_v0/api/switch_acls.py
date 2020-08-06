class SwitchACLs(object):
    def __init__(self, session):
        super(SwitchACLs, self).__init__()
        self._session = session
    
    def getNetworkSwitchAccessControlLists(self, networkId: str):
        """
        **Return the access control lists for a MS network**
        https://developer.cisco.com/meraki/api/#!get-network-switch-access-control-lists
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch ACLs'],
            'operation': 'getNetworkSwitchAccessControlLists',
        }
        resource = f'/networks/{networkId}/switch/accessControlLists'

        return self._session.get(metadata, resource)

    def updateNetworkSwitchAccessControlLists(self, networkId: str, rules: list):
        """
        **Update the access control lists for a MS network**
        https://developer.cisco.com/meraki/api/#!update-network-switch-access-control-lists
        
        - networkId (string)
        - rules (array): An ordered array of the access control list rules (not including the default rule). An empty array will clear the rules.
        """

        kwargs = locals()

        metadata = {
            'tags': ['Switch ACLs'],
            'operation': 'updateNetworkSwitchAccessControlLists',
        }
        resource = f'/networks/{networkId}/switch/accessControlLists'

        body_params = ['rules']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

