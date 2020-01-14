class AsyncSwitchStacks(object):
    def __init__(self, session):
        super().__init__()
        self._session = session

    async def getNetworkSwitchStacks(self, networkId: str):
        """
        **List the switch stacks in a network**
        https://api.meraki.com/api_docs#list-the-switch-stacks-in-a-network
        
        - networkId (string)
        """

        metadata = {
            "tags": ["Switch stacks"],
            "operation": "getNetworkSwitchStacks",
        }
        resource = f"/networks/{networkId}/switchStacks"

        return await self._session.get(metadata, resource)

    async def createNetworkSwitchStack(self, networkId: str, name: str, serials: list):
        """
        **Create a stack**
        https://api.meraki.com/api_docs#create-a-stack
        
        - networkId (string)
        - name (string): The name of the new stack
        - serials (array): An array of switch serials to be added into the new stack
        """

        kwargs = locals()

        metadata = {
            "tags": ["Switch stacks"],
            "operation": "createNetworkSwitchStack",
        }
        resource = f"/networks/{networkId}/switchStacks"

        body_params = ["name", "serials"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Show a switch stack**
        https://api.meraki.com/api_docs#show-a-switch-stack
        
        - networkId (string)
        - switchStackId (string)
        """

        metadata = {
            "tags": ["Switch stacks"],
            "operation": "getNetworkSwitchStack",
        }
        resource = f"/networks/{networkId}/switchStacks/{switchStackId}"

        return await self._session.get(metadata, resource)

    async def deleteNetworkSwitchStack(self, networkId: str, switchStackId: str):
        """
        **Delete a stack**
        https://api.meraki.com/api_docs#delete-a-stack
        
        - networkId (string)
        - switchStackId (string)
        """

        metadata = {
            "tags": ["Switch stacks"],
            "operation": "deleteNetworkSwitchStack",
        }
        resource = f"/networks/{networkId}/switchStacks/{switchStackId}"

        return await self._session.delete(metadata, resource)

    async def addNetworkSwitchStack(
        self, networkId: str, switchStackId: str, serial: str
    ):
        """
        **Add a switch to a stack**
        https://api.meraki.com/api_docs#add-a-switch-to-a-stack
        
        - networkId (string)
        - switchStackId (string)
        - serial (string): The serial of the switch to be added
        """

        kwargs = locals()

        metadata = {
            "tags": ["Switch stacks"],
            "operation": "addNetworkSwitchStack",
        }
        resource = f"/networks/{networkId}/switchStacks/{switchStackId}/add"

        body_params = ["serial"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)

    async def removeNetworkSwitchStack(
        self, networkId: str, switchStackId: str, serial: str
    ):
        """
        **Remove a switch from a stack**
        https://api.meraki.com/api_docs#remove-a-switch-from-a-stack
        
        - networkId (string)
        - switchStackId (string)
        - serial (string): The serial of the switch to be removed
        """

        kwargs = locals()

        metadata = {
            "tags": ["Switch stacks"],
            "operation": "removeNetworkSwitchStack",
        }
        resource = f"/networks/{networkId}/switchStacks/{switchStackId}/remove"

        body_params = ["serial"]
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return await self._session.post(metadata, resource, payload)
