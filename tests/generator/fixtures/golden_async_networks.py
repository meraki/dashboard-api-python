import urllib


class AsyncNetworks:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getNetwork(self, networkId: str, **kwargs):
        """
        **Get network details**
        https://developer.cisco.com/meraki/api-v1/#!get-network

        - networkId (string): Network ID
        - name (string): Optional name filter
        """

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "getNetwork",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}"

        query_params = [
            "name",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetwork: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def updateNetwork(self, networkId: str, name: str, **kwargs):
        """
        **Update a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network

        - networkId (string): Network ID
        - name (string): Network name
        - tags (array): Network tags
        """

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "updateNetwork",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}"

        body_params = [
            "name",
            "tags",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetwork: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def deleteNetwork(self, networkId: str):
        """
        **Delete a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): Network ID
        """

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "deleteNetwork",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}"

        return self._session.delete(metadata, resource)

    def createNetwork(self, name: str, type: str, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network

        - name (string): Network name
        - type (string): Network type
        """

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "createNetwork",
        }
        resource = "/networks"

        body_params = [
            "name",
            "type",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"createNetwork: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)

    def updateNetworkSettings(self, networkId: str, **kwargs):
        """
        **Update a network's settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): Network ID
        - localStatusPageEnabled (boolean): Enable local status page
        """

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "updateNetworkSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/settings"

        body_params = [
            "localStatusPageEnabled",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"updateNetworkSettings: ignoring unrecognized kwargs: {invalid}")

        return self._session.put(metadata, resource, payload)

    def getNetworkClients(self, networkId: str, count: int, **kwargs):
        """
        **List clients on a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        - networkId (string): Network ID
        - count (integer): Maximum number of clients to return
        - filter (object or string): Client filter by string or object (object supports: mac)
        """

        metadata = {
            "tags": ["networks", "monitor"],
            "operation": "getNetworkClients",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients"

        query_params = [
            "count",
            "filter",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getNetworkClients: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)

    def provisionNetworkClients(self, networkId: str, deviceName: str, mac: str, **kwargs):
        """
        **Provision network clients**
        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        - networkId (string): Network ID
        - deviceName (string): Device name (nullable)
        - mac (string): Device MAC address
        """

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "provisionNetworkClients",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients"

        body_params = [
            "deviceName",
            "mac",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        if self._session._validate_kwargs:
            all_params = [] + body_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"provisionNetworkClients: ignoring unrecognized kwargs: {invalid}")

        return self._session.post(metadata, resource, payload)
