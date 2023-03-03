import urllib


class Licensing(object):
    def __init__(self, session):
        super(Licensing, self).__init__()
        self._session = session
        


    def getOrganizationLicensingCotermLicenses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the licenses in a coterm organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-licensing-coterm-licenses

        - organizationId (string): (required)
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - invalidated (boolean): Filter for licenses that are invalidated
        - expired (boolean): Filter for licenses that are expired
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['licensing', 'configure', 'coterm', 'licenses'],
            'operation': 'getOrganizationLicensingCotermLicenses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licensing/coterm/licenses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'invalidated', 'expired', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def moveOrganizationLicensingCotermLicenses(self, organizationId: str, destination: dict, licenses: list):
        """
        **Moves a license to a different organization (coterm only)**
        https://developer.cisco.com/meraki/api-v1/#!move-organization-licensing-coterm-licenses

        - organizationId (string): (required)
        - destination (object): Destination data for the license move
        - licenses (array): The list of licenses to move
        """

        kwargs = locals()

        metadata = {
            'tags': ['licensing', 'configure', 'coterm', 'licenses'],
            'operation': 'moveOrganizationLicensingCotermLicenses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/licensing/coterm/licenses/move'

        body_params = ['destination', 'licenses', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        
