class AsyncNetworks:
    def __init__(self, session):
        super().__init__()
        self._session = session
    
    async def getNetwork(self, networkId: str):
        """
        **Return a network**
        https://developer.cisco.com/meraki/api/#!get-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Networks'],
            'operation': 'getNetwork',
        }
        resource = f'/networks/{networkId}'

        return await self._session.get(metadata, resource)

    async def updateNetwork(self, networkId: str, **kwargs):
        """
        **Update a network**
        https://developer.cisco.com/meraki/api/#!update-network
        
        - networkId (string)
        - name (string): The name of the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - tags (string): A space-separated list of tags to be applied to the network
        - disableMyMerakiCom (boolean): Disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
        - disableRemoteStatusPage (boolean): Disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if disableMyMerakiCom is set to false
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Networks'],
            'operation': 'updateNetwork',
        }
        resource = f'/networks/{networkId}'

        body_params = ['name', 'timeZone', 'tags', 'disableMyMerakiCom', 'disableRemoteStatusPage', 'enrollmentString']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def deleteNetwork(self, networkId: str):
        """
        **Delete a network**
        https://developer.cisco.com/meraki/api/#!delete-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Networks'],
            'operation': 'deleteNetwork',
        }
        resource = f'/networks/{networkId}'

        return await self._session.delete(metadata, resource)

    async def getNetworkAirMarshal(self, networkId: str, **kwargs):
        """
        **List Air Marshal scan results from a network**
        https://developer.cisco.com/meraki/api/#!get-network-air-marshal
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Networks'],
            'operation': 'getNetworkAirMarshal',
        }
        resource = f'/networks/{networkId}/airMarshal'

        query_params = ['t0', 'timespan']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def bindNetwork(self, networkId: str, configTemplateId: str, **kwargs):
        """
        **Bind a network to a template.**
        https://developer.cisco.com/meraki/api/#!bind-network
        
        - networkId (string)
        - configTemplateId (string): The ID of the template to which the network should be bound.
        - autoBind (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Networks'],
            'operation': 'bindNetwork',
        }
        resource = f'/networks/{networkId}/bind'

        body_params = ['configTemplateId', 'autoBind']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def getNetworkSiteToSiteVpn(self, networkId: str):
        """
        **Return the site-to-site VPN settings of a network. Only valid for MX networks.**
        https://developer.cisco.com/meraki/api/#!get-network-site-to-site-vpn
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Networks'],
            'operation': 'getNetworkSiteToSiteVpn',
        }
        resource = f'/networks/{networkId}/siteToSiteVpn'

        return await self._session.get(metadata, resource)

    async def updateNetworkSiteToSiteVpn(self, networkId: str, mode: str, **kwargs):
        """
        **Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.**
        https://developer.cisco.com/meraki/api/#!update-network-site-to-site-vpn
        
        - networkId (string)
        - mode (string): The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'
        - hubs (array): The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required.
        - subnets (array): The list of subnets and their VPN presence.
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['none', 'spoke', 'hub']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Networks'],
            'operation': 'updateNetworkSiteToSiteVpn',
        }
        resource = f'/networks/{networkId}/siteToSiteVpn'

        body_params = ['mode', 'hubs', 'subnets']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.put(metadata, resource, payload)

    async def splitNetwork(self, networkId: str):
        """
        **Split a combined network into individual networks for each type of device**
        https://developer.cisco.com/meraki/api/#!split-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Networks'],
            'operation': 'splitNetwork',
        }
        resource = f'/networks/{networkId}/split'

        return await self._session.post(metadata, resource)

    async def getNetworkTraffic(self, networkId: str, **kwargs):
        """
        **    The traffic analysis data for this network.
    <a href="https://documentation.meraki.com/MR/Monitoring_and_Reporting/Hostname_Visibility">Traffic Analysis with Hostname Visibility</a> must be enabled on the network.
**
        https://developer.cisco.com/meraki/api/#!get-network-traffic
        
        - networkId (string)
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 30 days.
        - deviceType (string):     Filter the data by device type: 'combined', 'wireless', 'switch' or 'appliance'. Defaults to 'combined'.
    When using 'combined', for each rule the data will come from the device type with the most usage.

        """

        kwargs.update(locals())

        if 'deviceType' in kwargs:
            options = ['combined', 'wireless', 'switch', 'appliance']
            assert kwargs['deviceType'] in options, f'''"deviceType" cannot be "{kwargs['deviceType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Networks'],
            'operation': 'getNetworkTraffic',
        }
        resource = f'/networks/{networkId}/traffic'

        query_params = ['t0', 'timespan', 'deviceType']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def unbindNetwork(self, networkId: str):
        """
        **Unbind a network from a template.**
        https://developer.cisco.com/meraki/api/#!unbind-network
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Networks'],
            'operation': 'unbindNetwork',
        }
        resource = f'/networks/{networkId}/unbind'

        return await self._session.post(metadata, resource)

    async def getOrganizationNetworks(self, organizationId: str, **kwargs):
        """
        **List the networks in an organization**
        https://developer.cisco.com/meraki/api/#!get-organization-networks
        
        - organizationId (string)
        - configTemplateId (string): An optional parameter that is the ID of a config template. Will return all networks bound to that template.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Networks'],
            'operation': 'getOrganizationNetworks',
        }
        resource = f'/organizations/{organizationId}/networks'

        query_params = ['configTemplateId']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return await self._session.get(metadata, resource, params)

    async def createOrganizationNetwork(self, organizationId: str, name: str, type: str, **kwargs):
        """
        **Create a network**
        https://developer.cisco.com/meraki/api/#!create-organization-network
        
        - organizationId (string)
        - name (string): The name of the new network
        - type (string): The type of the new network. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, or a space-separated list of those for a combined network.
        - tags (string): A space-separated list of tags to be applied to the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - copyFromNetworkId (string): The ID of the network to copy configuration from. Other provided parameters will override the copied configuration, except type which must match this network's type exactly.
        - disableMyMerakiCom (boolean): Disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
        - disableRemoteStatusPage (boolean): Disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if disableMyMerakiCom is set to false
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Networks'],
            'operation': 'createOrganizationNetwork',
        }
        resource = f'/organizations/{organizationId}/networks'

        body_params = ['name', 'type', 'tags', 'timeZone', 'copyFromNetworkId', 'disableMyMerakiCom', 'disableRemoteStatusPage']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

    async def combineOrganizationNetworks(self, organizationId: str, name: str, networkIds: list, **kwargs):
        """
        **Combine multiple networks into a single network**
        https://developer.cisco.com/meraki/api/#!combine-organization-networks
        
        - organizationId (string)
        - name (string): The name of the combined network
        - networkIds (array): A list of the network IDs that will be combined. If an ID of a combined network is included in this list, the other networks in the list will be grouped into that network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break. All networks that are part of this combined network will have their enrollment string appended by '-network_type'. If left empty, all exisitng enrollment strings will be deleted.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Networks'],
            'operation': 'combineOrganizationNetworks',
        }
        resource = f'/organizations/{organizationId}/networks/combine'

        body_params = ['name', 'networkIds', 'enrollmentString']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return await self._session.post(metadata, resource, payload)

