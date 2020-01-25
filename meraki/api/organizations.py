class Organizations(object):
    def __init__(self, session):
        super(Organizations, self).__init__()
        self._session = session
    
    def getOrganizations(self):
        """
        **List the organizations that the user has privileges on**
        https://api.meraki.com/api_docs#list-the-organizations-that-the-user-has-privileges-on
        
        """

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganizations',
        }
        resource = f'/organizations'

        return self._session.get(metadata, resource)

    def createOrganization(self, name: str):
        """
        **Create a new organization**
        https://api.meraki.com/api_docs#create-a-new-organization
        
        - name (string): The name of the organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['Organizations'],
            'operation': 'createOrganization',
        }
        resource = f'/organizations'

        body_params = ['name']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getOrganization(self, organizationId: str):
        """
        **Return an organization**
        https://api.meraki.com/api_docs#return-an-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganization',
        }
        resource = f'/organizations/{organizationId}'

        return self._session.get(metadata, resource)

    def updateOrganization(self, organizationId: str, **kwargs):
        """
        **Update an organization**
        https://api.meraki.com/api_docs#update-an-organization
        
        - organizationId (string)
        - name (string): The name of the organization
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Organizations'],
            'operation': 'updateOrganization',
        }
        resource = f'/organizations/{organizationId}'

        body_params = ['name']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteOrganization(self, organizationId: str):
        """
        **Delete an organization**
        https://api.meraki.com/api_docs#delete-an-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Organizations'],
            'operation': 'deleteOrganization',
        }
        resource = f'/organizations/{organizationId}'

        return self._session.delete(metadata, resource)

    def claimOrganization(self, organizationId: str, **kwargs):
        """
        **Claim a list of devices, licenses, and/or orders into an organization. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization's inventory.**
        https://api.meraki.com/api_docs#claim-a-list-of-devices-licenses-and/or-orders-into-an-organization
        
        - organizationId (string)
        - orders (array): The numbers of the orders that should be claimed
        - serials (array): The serials of the devices that should be claimed
        - licenses (array): The licenses that should be claimed
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Organizations'],
            'operation': 'claimOrganization',
        }
        resource = f'/organizations/{organizationId}/claim'

        body_params = ['orders', 'serials', 'licenses']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def cloneOrganization(self, organizationId: str, name: str):
        """
        **Create a new organization by cloning the addressed organization**
        https://api.meraki.com/api_docs#create-a-new-organization-by-cloning-the-addressed-organization
        
        - organizationId (string)
        - name (string): The name of the new organization
        """

        kwargs = locals()

        metadata = {
            'tags': ['Organizations'],
            'operation': 'cloneOrganization',
        }
        resource = f'/organizations/{organizationId}/clone'

        body_params = ['name']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getOrganizationDeviceStatuses(self, organizationId: str):
        """
        **List the status of every Meraki device in the organization**
        https://api.meraki.com/api_docs#list-the-status-of-every-meraki-device-in-the-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganizationDeviceStatuses',
        }
        resource = f'/organizations/{organizationId}/deviceStatuses'

        return self._session.get(metadata, resource)

    def getOrganizationInventory(self, organizationId: str, **kwargs):
        """
        **Return the inventory for an organization**
        https://api.meraki.com/api_docs#return-the-inventory-for-an-organization
        
        - organizationId (string)
        - includeLicenseInfo (boolean): When this parameter is true, each entity in the response will include the license expiration date of the device (if any). Only applies to organizations that support per-device licensing. Defaults to false.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganizationInventory',
        }
        resource = f'/organizations/{organizationId}/inventory'

        query_params = ['includeLicenseInfo']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def getOrganizationLicenseState(self, organizationId: str):
        """
        **Return the license state for an organization**
        https://api.meraki.com/api_docs#return-the-license-state-for-an-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganizationLicenseState',
        }
        resource = f'/organizations/{organizationId}/licenseState'

        return self._session.get(metadata, resource)

    def getOrganizationThirdPartyVPNPeers(self, organizationId: str):
        """
        **Return the third party VPN peers for an organization**
        https://api.meraki.com/api_docs#return-the-third-party-vpn-peers-for-an-organization
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganizationThirdPartyVPNPeers',
        }
        resource = f'/organizations/{organizationId}/thirdPartyVPNPeers'

        return self._session.get(metadata, resource)

    def updateOrganizationThirdPartyVPNPeers(self, organizationId: str, peers: list):
        """
        **Update the third party VPN peers for an organization**
        https://api.meraki.com/api_docs#update-the-third-party-vpn-peers-for-an-organization
        
        - organizationId (string)
        - peers (array): The list of VPN peers
        """

        kwargs = locals()

        metadata = {
            'tags': ['Organizations'],
            'operation': 'updateOrganizationThirdPartyVPNPeers',
        }
        resource = f'/organizations/{organizationId}/thirdPartyVPNPeers'

        body_params = ['peers']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getOrganizationUplinksLossAndLatency(self, organizationId: str, **kwargs):
        """
        **Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago**
        https://api.meraki.com/api_docs#return-the-uplink-loss-and-latency-for-every-mx-in-the-organization-from-at-latest-2-minutes-ago
        
        - organizationId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 5 minutes after t0. The latest possible time that t1 can be is 2 minutes into the past.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 5 minutes. The default is 5 minutes.
        - uplink (string): Optional filter for a specific WAN uplink. Valid uplinks are wan1, wan2, cellular. Default will return all uplinks.
        - ip (string): Optional filter for a specific destination IP. Default will return all destination IPs.
        """

        kwargs.update(locals())

        if 'uplink' in kwargs:
            options = ['wan1', 'wan2', 'cellular']
            assert kwargs['uplink'] in options, f'''"uplink" cannot be "{kwargs['uplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Organizations'],
            'operation': 'getOrganizationUplinksLossAndLatency',
        }
        resource = f'/organizations/{organizationId}/uplinksLossAndLatency'

        query_params = ['t0', 't1', 'timespan', 'uplink', 'ip']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

