import urllib


class AsyncNetworks:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getNetworkClients(self, networkId: str, total_pages=1, direction="next", **kwargs):
        """
        **List the clients that have used this network in the timespan**
        https://developer.cisco.com/meraki/api-v1/#!get-network-clients

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 5000. Default is 10.
        - startingAfter (string): A token used by the server to indicate the start of the page.
        - endingBefore (string): A token used by the server to indicate the end of the page.
        - t0 (string): The beginning of the timespan for the data.
        - timespan (number): The timespan for which the information will be fetched.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "clients"],
            "operation": "getNetworkClients",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/clients"

        query_params = [
            "perPage",
            "startingAfter",
            "endingBefore",
            "t0",
            "timespan",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)

    def updateNetworkSettings(self, networkId: str, **kwargs):
        """
        **Update the settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): Network ID
        - localStatusPageEnabled (boolean): Enables / disables the local device status pages.
        - securePort (object): A hash of SecureConnect options.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure"],
            "operation": "updateNetworkSettings",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        resource = f"/networks/{networkId}/settings"

        body_params = [
            "localStatusPageEnabled",
            "securePort",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def updateNetworkProfile(self, networkId: str, profileId: str, **kwargs):
        """
        **Update a network profile**
        https://developer.cisco.com/meraki/api-v1/#!update-network-profile

        - networkId (string): Network ID
        - profileId (string): Profile ID
        - name (string): Name of the profile.
        """

        kwargs.update(locals())

        metadata = {
            "tags": ["networks", "configure", "profiles"],
            "operation": "updateNetworkProfile",
        }
        networkId = urllib.parse.quote(str(networkId), safe="")
        profileId = urllib.parse.quote(str(profileId), safe="")
        resource = f"/networks/{networkId}/profiles/{profileId}"

        body_params = [
            "name",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

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
