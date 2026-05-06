import urllib


class Administered(object):
    def __init__(self, session):
        super(Administered, self).__init__()
        self._session = session

    def getAdministeredIdentitiesMe(self):
        """
        **Returns the identity of the current user.**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me

        """

        metadata = {
            "tags": ["administered", "monitor", "identities", "me"],
            "operation": "getAdministeredIdentitiesMe",
        }
        resource = "/administered/identities/me"

        return self._session.get(metadata, resource)

    def getAdministeredIdentitiesMeApiKeys(self):
        """
        **List the non-sensitive metadata associated with the API keys that belong to the user**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-identities-me-api-keys

        """

        metadata = {
            "tags": ["administered", "configure", "identities", "me", "api", "keys"],
            "operation": "getAdministeredIdentitiesMeApiKeys",
        }
        resource = "/administered/identities/me/api/keys"

        return self._session.get(metadata, resource)

    def generateAdministeredIdentitiesMeApiKeys(self):
        """
        **Generates an API key for an identity**
        https://developer.cisco.com/meraki/api-v1/#!generate-administered-identities-me-api-keys

        """

        metadata = {
            "tags": ["administered", "configure", "identities", "me", "api", "keys"],
            "operation": "generateAdministeredIdentitiesMeApiKeys",
        }
        resource = "/administered/identities/me/api/keys/generate"

        return self._session.post(metadata, resource)

    def revokeAdministeredIdentitiesMeApiKeys(self, suffix: str):
        """
        **Revokes an identity's API key, using the last four characters of the key**
        https://developer.cisco.com/meraki/api-v1/#!revoke-administered-identities-me-api-keys

        - suffix (string): Suffix
        """

        metadata = {
            "tags": ["administered", "configure", "identities", "me", "api", "keys"],
            "operation": "revokeAdministeredIdentitiesMeApiKeys",
        }
        suffix = urllib.parse.quote(str(suffix), safe="")
        resource = f"/administered/identities/me/api/keys/{suffix}/revoke"

        return self._session.post(metadata, resource)

    def getAdministeredSearchLive(self, query: str, organizationId: str, networkId: str, **kwargs):
        """
        **List the appropriate results for a given global search utilizing live_search_react**
        https://developer.cisco.com/meraki/api-v1/#!get-administered-search-live

        - query (string): Search keywords
        - organizationId (string): Id of Organization you want to search with
        - networkId (string): Id of NodeGroup you want to seach with
        """

        kwargs = locals()

        metadata = {
            "tags": ["administered", "configure", "search", "live"],
            "operation": "getAdministeredSearchLive",
        }
        resource = "/administered/search/live"

        query_params = [
            "query",
            "organizationId",
            "networkId",
        ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        if self._session._validate_kwargs:
            all_params = query_params
            invalid = [k for k in kwargs if k.strip() not in all_params and k != "self"]
            if invalid and self._session._logger:
                self._session._logger.warning(f"getAdministeredSearchLive: ignoring unrecognized kwargs: {invalid}")

        return self._session.get(metadata, resource, params)
