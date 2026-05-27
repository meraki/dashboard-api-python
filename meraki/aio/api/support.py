import urllib


class AsyncSupport:
    def __init__(self, session):
        super().__init__()
        self._session = session

    def getOrganizationSupportSalesRepresentatives(self, organizationId: str):
        """
        **Returns the organization's sales representatives**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-support-sales-representatives

        - organizationId (string): Organization ID
        """

        metadata = {
            "tags": ["support", "monitor", "salesRepresentatives"],
            "operation": "getOrganizationSupportSalesRepresentatives",
        }
        organizationId = urllib.parse.quote(str(organizationId), safe="")
        resource = f"/organizations/{organizationId}/support/salesRepresentatives"

        return self._session.get(metadata, resource)
