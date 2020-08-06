class SwitchStacks(object):
    def __init__(self, session):
        super(SwitchStacks, self).__init__()
        self._session = session
    
    def getNetworkSwitchStacks(self, networkId: str):
        """
        **List the switch stacks in a network**
        https://developer.cisco.com/meraki/api/#!get-network-switch-stacks
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Switch stacks'],
            'operation': 'getNetworkSwitchStacks',
        }
        resource = f'/networks/{networkId}/switchStacks'

        return self._session.get(metadata, resource)

    def createNetworkSwitchStack(self, networkId: str, name: str, serials: list):
        """
        **Create a stack**
        https://developer.cisco.com/meraki/api/#!create-network-switch-stack
        
        - networkId (string)
        - name (string): The name of the new stack
        - serials (array): An array of switch serials to be added into the new stack
        """

        kwargs = locals()

        metadata = {
            'tags': ['Switch stacks'],
            'operation': 'createNetworkSwitchStack',
        }
        resource = f'/networks/{networkId}/switchStacks'

        body_params = ['name', 'serials']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Show a switch stack**
        https://developer.cisco.com/meraki/api/#!get-network-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        """

        metadata = {
            'tags': ['Switch stacks'],
            'operation': 'getNetworkSwitchStack',
        }
        resource = f'/networks/{networkId}/switchStacks/{switchStackId}'

        return self._session.get(metadata, resource)

    def deleteNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Delete a stack**
        https://developer.cisco.com/meraki/api/#!delete-network-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        """

        metadata = {
            'tags': ['Switch stacks'],
            'operation': 'deleteNetworkSwitchStack',
        }
        resource = f'/networks/{networkId}/switchStacks/{switchStackId}'

        return self._session.delete(metadata, resource)

    def addNetworkSwitchStack(self, networkId: str, switchStackId: str, serial: str):
        """
        **Add a switch to a stack**
        https://developer.cisco.com/meraki/api/#!add-network-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        - serial (string): The serial of the switch to be added
        """

        kwargs = locals()

        metadata = {
            'tags': ['Switch stacks'],
            'operation': 'addNetworkSwitchStack',
        }
        resource = f'/networks/{networkId}/switchStacks/{switchStackId}/add'

        body_params = ['serial']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def removeNetworkSwitchStack(self, networkId: str, switchStackId: str, serial: str):
        """
        **Remove a switch from a stack**
        https://developer.cisco.com/meraki/api/#!remove-network-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        - serial (string): The serial of the switch to be removed
        """

        kwargs = locals()

        metadata = {
            'tags': ['Switch stacks'],
            'operation': 'removeNetworkSwitchStack',
        }
        resource = f'/networks/{networkId}/switchStacks/{switchStackId}/remove'

        body_params = ['serial']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

