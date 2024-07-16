import urllib


class AsyncAppliance:
    def __init__(self, session):
        super().__init__()
        self._session = session
        


    def getDeviceApplianceDhcpSubnets(self, serial: str):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'monitor', 'dhcp', 'subnets'],
            'operation': 'getDeviceApplianceDhcpSubnets'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/dhcp/subnets'

        return self._session.get(metadata, resource)
        


    def getDeviceAppliancePerformance(self, serial: str, **kwargs):
        """
        **Return the performance score for a single MX**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance

        - serial (string): Serial
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 30 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be greater than or equal to 30 minutes and be less than or equal to 14 days. The default is 30 minutes.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'monitor', 'performance'],
            'operation': 'getDeviceAppliancePerformance'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/performance'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getDeviceAppliancePrefixesDelegated(self, serial: str):
        """
        **Return current delegated IPv6 prefixes on an appliance.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'monitor', 'prefixes', 'delegated'],
            'operation': 'getDeviceAppliancePrefixesDelegated'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/prefixes/delegated'

        return self._session.get(metadata, resource)
        


    def getDeviceAppliancePrefixesDelegatedVlanAssignments(self, serial: str):
        """
        **Return prefixes assigned to all IPv6 enabled VLANs on an appliance.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-prefixes-delegated-vlan-assignments

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'monitor', 'prefixes', 'delegated', 'vlanAssignments'],
            'operation': 'getDeviceAppliancePrefixesDelegatedVlanAssignments'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/prefixes/delegated/vlanAssignments'

        return self._session.get(metadata, resource)
        


    def getDeviceApplianceRadioSettings(self, serial: str):
        """
        **Return the radio settings of an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-radio-settings

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'configure', 'radio', 'settings'],
            'operation': 'getDeviceApplianceRadioSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/radio/settings'

        return self._session.get(metadata, resource)
        


    def updateDeviceApplianceRadioSettings(self, serial: str, **kwargs):
        """
        **Update the radio settings of an appliance**
        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-radio-settings

        - serial (string): Serial
        - rfProfileId (string): The ID of an RF profile to assign to the device. If the value of this parameter is null, the appropriate basic RF profile (indoor or outdoor) will be assigned to the device. Assigning an RF profile will clear ALL manually configured overrides on the device (channel width, channel, power).
        - twoFourGhzSettings (object): Manual radio settings for 2.4 GHz.
        - fiveGhzSettings (object): Manual radio settings for 5 GHz.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'radio', 'settings'],
            'operation': 'updateDeviceApplianceRadioSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/radio/settings'

        body_params = ['rfProfileId', 'twoFourGhzSettings', 'fiveGhzSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getDeviceApplianceUplinksSettings(self, serial: str):
        """
        **Return the uplink settings for an MX appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-uplinks-settings

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'configure', 'uplinks', 'settings'],
            'operation': 'getDeviceApplianceUplinksSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/uplinks/settings'

        return self._session.get(metadata, resource)
        


    def updateDeviceApplianceUplinksSettings(self, serial: str, interfaces: dict):
        """
        **Update the uplink settings for an MX appliance**
        https://developer.cisco.com/meraki/api-v1/#!update-device-appliance-uplinks-settings

        - serial (string): Serial
        - interfaces (object): Interface settings.
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'uplinks', 'settings'],
            'operation': 'updateDeviceApplianceUplinksSettings'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/uplinks/settings'

        body_params = ['interfaces', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def createDeviceApplianceVmxAuthenticationToken(self, serial: str):
        """
        **Generate a new vMX authentication token**
        https://developer.cisco.com/meraki/api-v1/#!create-device-appliance-vmx-authentication-token

        - serial (string): Serial
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vmx', 'authenticationToken'],
            'operation': 'createDeviceApplianceVmxAuthenticationToken'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/appliance/vmx/authenticationToken'

        return self._session.post(metadata, resource)
        


    def getNetworkApplianceClientSecurityEvents(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events for a client**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-client-security-events

        - networkId (string): Network ID
        - clientId (string): Client ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 791 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 791 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 791 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.
        """

        kwargs.update(locals())

        if 'sortOrder' in kwargs:
            options = ['ascending', 'descending']
            assert kwargs['sortOrder'] in options, f'''"sortOrder" cannot be "{kwargs['sortOrder']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'monitor', 'clients', 'security', 'events'],
            'operation': 'getNetworkApplianceClientSecurityEvents'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        clientId = urllib.parse.quote(str(clientId), safe='')
        resource = f'/networks/{networkId}/appliance/clients/{clientId}/security/events'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkApplianceConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-connectivity-monitoring-destinations

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'getNetworkApplianceConnectivityMonitoringDestinations'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations

        - networkId (string): Network ID
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'updateNetworkApplianceConnectivityMonitoringDestinations'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/connectivityMonitoringDestinations'

        body_params = ['destinations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceContentFiltering(self, networkId: str):
        """
        **Return the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'contentFiltering'],
            'operation': 'getNetworkApplianceContentFiltering'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/contentFiltering'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceContentFiltering(self, networkId: str, **kwargs):
        """
        **Update the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-content-filtering

        - networkId (string): Network ID
        - allowedUrlPatterns (array): A list of URL patterns that are allowed
        - blockedUrlPatterns (array): A list of URL patterns that are blocked
        - blockedUrlCategories (array): A list of URL categories to block
        - urlCategoryListSize (string): URL category list size which is either 'topSites' or 'fullList'
        """

        kwargs.update(locals())

        if 'urlCategoryListSize' in kwargs:
            options = ['fullList', 'topSites']
            assert kwargs['urlCategoryListSize'] in options, f'''"urlCategoryListSize" cannot be "{kwargs['urlCategoryListSize']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'contentFiltering'],
            'operation': 'updateNetworkApplianceContentFiltering'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/contentFiltering'

        body_params = ['allowedUrlPatterns', 'blockedUrlPatterns', 'blockedUrlCategories', 'urlCategoryListSize', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceContentFilteringCategories(self, networkId: str):
        """
        **List all available content filtering categories for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering-categories

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'contentFiltering', 'categories'],
            'operation': 'getNetworkApplianceContentFilteringCategories'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/contentFiltering/categories'

        return self._session.get(metadata, resource)
        


    def getNetworkApplianceFirewallCellularFirewallRules(self, networkId: str):
        """
        **Return the cellular firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-cellular-firewall-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'cellularFirewallRules'],
            'operation': 'getNetworkApplianceFirewallCellularFirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/cellularFirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallCellularFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the cellular firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-cellular-firewall-rules

        - networkId (string): Network ID
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'cellularFirewallRules'],
            'operation': 'updateNetworkApplianceFirewallCellularFirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/cellularFirewallRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallFirewalledServices(self, networkId: str):
        """
        **List the appliance services and their accessibility rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-services

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'firewalledServices'],
            'operation': 'getNetworkApplianceFirewallFirewalledServices'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/firewalledServices'

        return self._session.get(metadata, resource)
        


    def getNetworkApplianceFirewallFirewalledService(self, networkId: str, service: str):
        """
        **Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-service

        - networkId (string): Network ID
        - service (string): Service
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'firewalledServices'],
            'operation': 'getNetworkApplianceFirewallFirewalledService'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        service = urllib.parse.quote(str(service), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/firewalledServices/{service}'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallFirewalledService(self, networkId: str, service: str, access: str, **kwargs):
        """
        **Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-firewalled-service

        - networkId (string): Network ID
        - service (string): Service
        - access (string): A string indicating the rule for which IPs are allowed to use the specified service. Acceptable values are "blocked" (no remote IPs can access the service), "restricted" (only allowed IPs can access the service), and "unrestriced" (any remote IP can access the service). This field is required
        - allowedIps (array): An array of allowed IPs that can access the service. This field is required if "access" is set to "restricted". Otherwise this field is ignored
        """

        kwargs.update(locals())

        if 'access' in kwargs:
            options = ['blocked', 'restricted', 'unrestricted']
            assert kwargs['access'] in options, f'''"access" cannot be "{kwargs['access']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'firewalledServices'],
            'operation': 'updateNetworkApplianceFirewallFirewalledService'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        service = urllib.parse.quote(str(service), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/firewalledServices/{service}'

        body_params = ['access', 'allowedIps', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallInboundCellularFirewallRules(self, networkId: str):
        """
        **Return the inbound cellular firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-cellular-firewall-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'inboundCellularFirewallRules'],
            'operation': 'getNetworkApplianceFirewallInboundCellularFirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/inboundCellularFirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallInboundCellularFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the inbound cellular firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-cellular-firewall-rules

        - networkId (string): Network ID
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'inboundCellularFirewallRules'],
            'operation': 'updateNetworkApplianceFirewallInboundCellularFirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/inboundCellularFirewallRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallInboundFirewallRules(self, networkId: str):
        """
        **Return the inbound firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-firewall-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'inboundFirewallRules'],
            'operation': 'getNetworkApplianceFirewallInboundFirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/inboundFirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallInboundFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the inbound firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-firewall-rules

        - networkId (string): Network ID
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'inboundFirewallRules'],
            'operation': 'updateNetworkApplianceFirewallInboundFirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/inboundFirewallRules'

        body_params = ['rules', 'syslogDefaultRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallL3FirewallRules(self, networkId: str):
        """
        **Return the L3 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-3-firewall-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l3FirewallRules'],
            'operation': 'getNetworkApplianceFirewallL3FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/l3FirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallL3FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the L3 firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-3-firewall-rules

        - networkId (string): Network ID
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l3FirewallRules'],
            'operation': 'updateNetworkApplianceFirewallL3FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/l3FirewallRules'

        body_params = ['rules', 'syslogDefaultRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallL7FirewallRules(self, networkId: str):
        """
        **List the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules'],
            'operation': 'getNetworkApplianceFirewallL7FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallL7FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules

        - networkId (string): Network ID
        - rules (array): An ordered array of the MX L7 firewall rules
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules'],
            'operation': 'updateNetworkApplianceFirewallL7FirewallRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(self, networkId: str):
        """
        **Return the L7 firewall application categories and their associated applications for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules-application-categories

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules', 'applicationCategories'],
            'operation': 'getNetworkApplianceFirewallL7FirewallRulesApplicationCategories'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories'

        return self._session.get(metadata, resource)
        


    def getNetworkApplianceFirewallOneToManyNatRules(self, networkId: str):
        """
        **Return the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-many-nat-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToManyNatRules'],
            'operation': 'getNetworkApplianceFirewallOneToManyNatRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/oneToManyNatRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallOneToManyNatRules(self, networkId: str, rules: list):
        """
        **Set the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-many-nat-rules

        - networkId (string): Network ID
        - rules (array): An array of 1:Many nat rules
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToManyNatRules'],
            'operation': 'updateNetworkApplianceFirewallOneToManyNatRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/oneToManyNatRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallOneToOneNatRules(self, networkId: str):
        """
        **Return the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-one-nat-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToOneNatRules'],
            'operation': 'getNetworkApplianceFirewallOneToOneNatRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/oneToOneNatRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallOneToOneNatRules(self, networkId: str, rules: list):
        """
        **Set the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-one-nat-rules

        - networkId (string): Network ID
        - rules (array): An array of 1:1 nat rules
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToOneNatRules'],
            'operation': 'updateNetworkApplianceFirewallOneToOneNatRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/oneToOneNatRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallPortForwardingRules(self, networkId: str):
        """
        **Return the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-port-forwarding-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'portForwardingRules'],
            'operation': 'getNetworkApplianceFirewallPortForwardingRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/portForwardingRules'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallPortForwardingRules(self, networkId: str, rules: list):
        """
        **Update the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-port-forwarding-rules

        - networkId (string): Network ID
        - rules (array): An array of port forwarding params
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'portForwardingRules'],
            'operation': 'updateNetworkApplianceFirewallPortForwardingRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/portForwardingRules'

        body_params = ['rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceFirewallSettings(self, networkId: str):
        """
        **Return the firewall settings for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-settings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'settings'],
            'operation': 'getNetworkApplianceFirewallSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceFirewallSettings(self, networkId: str, **kwargs):
        """
        **Update the firewall settings for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-settings

        - networkId (string): Network ID
        - spoofingProtection (object): Spoofing protection settings
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'settings'],
            'operation': 'updateNetworkApplianceFirewallSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/firewall/settings'

        body_params = ['spoofingProtection', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkAppliancePorts(self, networkId: str):
        """
        **List per-port VLAN settings for all ports of a MX.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ports

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'ports'],
            'operation': 'getNetworkAppliancePorts'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/ports'

        return self._session.get(metadata, resource)
        


    def getNetworkAppliancePort(self, networkId: str, portId: str):
        """
        **Return per-port VLAN settings for a single MX port.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-port

        - networkId (string): Network ID
        - portId (string): Port ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'ports'],
            'operation': 'getNetworkAppliancePort'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        portId = urllib.parse.quote(str(portId), safe='')
        resource = f'/networks/{networkId}/appliance/ports/{portId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkAppliancePort(self, networkId: str, portId: str, **kwargs):
        """
        **Update the per-port VLAN settings for a single MX port.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port

        - networkId (string): Network ID
        - portId (string): Port ID
        - enabled (boolean): The status of the port
        - dropUntaggedTraffic (boolean): Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true.
        - type (string): The type of the port: 'access' or 'trunk'.
        - vlan (integer): Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode.
        - allowedVlans (string): Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to permit all VLAN's on the port.
        - accessPolicy (string): The name of the policy. Only applicable to Access ports. Valid values are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, 'open' is the only valid value and 'open' is the default value if the field is missing.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'ports'],
            'operation': 'updateNetworkAppliancePort'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        portId = urllib.parse.quote(str(portId), safe='')
        resource = f'/networks/{networkId}/appliance/ports/{portId}'

        body_params = ['enabled', 'dropUntaggedTraffic', 'type', 'vlan', 'allowedVlans', 'accessPolicy', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkAppliancePrefixesDelegatedStatics(self, networkId: str):
        """
        **List static delegated prefixes for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-statics

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'getNetworkAppliancePrefixesDelegatedStatics'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics'

        return self._session.get(metadata, resource)
        


    def createNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, prefix: str, origin: dict, **kwargs):
        """
        **Add a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - prefix (string): A static IPv6 prefix
        - origin (object): The origin of the prefix
        - description (string): A name or description for the prefix
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'createNetworkAppliancePrefixesDelegatedStatic'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics'

        body_params = ['prefix', 'origin', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, staticDelegatedPrefixId: str):
        """
        **Return a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - staticDelegatedPrefixId (string): Static delegated prefix ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'getNetworkAppliancePrefixesDelegatedStatic'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        staticDelegatedPrefixId = urllib.parse.quote(str(staticDelegatedPrefixId), safe='')
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, staticDelegatedPrefixId: str, **kwargs):
        """
        **Update a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - staticDelegatedPrefixId (string): Static delegated prefix ID
        - prefix (string): A static IPv6 prefix
        - origin (object): The origin of the prefix
        - description (string): A name or description for the prefix
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'updateNetworkAppliancePrefixesDelegatedStatic'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        staticDelegatedPrefixId = urllib.parse.quote(str(staticDelegatedPrefixId), safe='')
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}'

        body_params = ['prefix', 'origin', 'description', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkAppliancePrefixesDelegatedStatic(self, networkId: str, staticDelegatedPrefixId: str):
        """
        **Delete a static delegated prefix from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-prefixes-delegated-static

        - networkId (string): Network ID
        - staticDelegatedPrefixId (string): Static delegated prefix ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'prefixes', 'delegated', 'statics'],
            'operation': 'deleteNetworkAppliancePrefixesDelegatedStatic'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        staticDelegatedPrefixId = urllib.parse.quote(str(staticDelegatedPrefixId), safe='')
        resource = f'/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkApplianceRfProfiles(self, networkId: str):
        """
        **List the RF profiles for this network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-rf-profiles

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'getNetworkApplianceRfProfiles'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/rfProfiles'

        return self._session.get(metadata, resource)
        


    def createNetworkApplianceRfProfile(self, networkId: str, name: str, **kwargs):
        """
        **Creates new RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-rf-profile

        - networkId (string): Network ID
        - name (string): The name of the new profile. Must be unique. This param is required on creation.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - perSsidSettings (object): Per-SSID radio settings by number.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'createNetworkApplianceRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/rfProfiles'

        body_params = ['name', 'twoFourGhzSettings', 'fiveGhzSettings', 'perSsidSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def updateNetworkApplianceRfProfile(self, networkId: str, rfProfileId: str, **kwargs):
        """
        **Updates specified RF profile for this network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        - name (string): The name of the new profile. Must be unique.
        - twoFourGhzSettings (object): Settings related to 2.4Ghz band
        - fiveGhzSettings (object): Settings related to 5Ghz band
        - perSsidSettings (object): Per-SSID radio settings by number.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'updateNetworkApplianceRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe='')
        resource = f'/networks/{networkId}/appliance/rfProfiles/{rfProfileId}'

        body_params = ['name', 'twoFourGhzSettings', 'fiveGhzSettings', 'perSsidSettings', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkApplianceRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Delete a RF Profile**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'deleteNetworkApplianceRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe='')
        resource = f'/networks/{networkId}/appliance/rfProfiles/{rfProfileId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkApplianceRfProfile(self, networkId: str, rfProfileId: str):
        """
        **Return a RF profile**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-rf-profile

        - networkId (string): Network ID
        - rfProfileId (string): Rf profile ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'rfProfiles'],
            'operation': 'getNetworkApplianceRfProfile'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        rfProfileId = urllib.parse.quote(str(rfProfileId), safe='')
        resource = f'/networks/{networkId}/appliance/rfProfiles/{rfProfileId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceSdwanInternetPolicies(self, networkId: str, **kwargs):
        """
        **Update SDWAN internet traffic preferences for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-sdwan-internet-policies

        - networkId (string): Network ID
        - wanTrafficUplinkPreferences (array): policies with respective traffic filters for an MX network
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'sdwan', 'internetPolicies'],
            'operation': 'updateNetworkApplianceSdwanInternetPolicies'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/sdwan/internetPolicies'

        body_params = ['wanTrafficUplinkPreferences', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceSecurityEvents(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events

        - networkId (string): Network ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.
        """

        kwargs.update(locals())

        if 'sortOrder' in kwargs:
            options = ['ascending', 'descending']
            assert kwargs['sortOrder'] in options, f'''"sortOrder" cannot be "{kwargs['sortOrder']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'monitor', 'security', 'events'],
            'operation': 'getNetworkApplianceSecurityEvents'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/security/events'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getNetworkApplianceSecurityIntrusion(self, networkId: str):
        """
        **Returns all supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-intrusion

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'getNetworkApplianceSecurityIntrusion'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/security/intrusion'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceSecurityIntrusion(self, networkId: str, **kwargs):
        """
        **Set the supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-intrusion

        - networkId (string): Network ID
        - mode (string): Set mode to 'disabled'/'detection'/'prevention' (optional - omitting will leave current config unchanged)
        - idsRulesets (string): Set the detection ruleset 'connectivity'/'balanced'/'security' (optional - omitting will leave current config unchanged). Default value is 'balanced' if none currently saved
        - protectedNetworks (object): Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in 'passthrough' mode
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['detection', 'disabled', 'prevention']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''
        if 'idsRulesets' in kwargs:
            options = ['balanced', 'connectivity', 'security']
            assert kwargs['idsRulesets'] in options, f'''"idsRulesets" cannot be "{kwargs['idsRulesets']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'updateNetworkApplianceSecurityIntrusion'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/security/intrusion'

        body_params = ['mode', 'idsRulesets', 'protectedNetworks', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceSecurityMalware(self, networkId: str):
        """
        **Returns all supported malware settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-malware

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'malware'],
            'operation': 'getNetworkApplianceSecurityMalware'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/security/malware'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceSecurityMalware(self, networkId: str, mode: str, **kwargs):
        """
        **Set the supported malware settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-malware

        - networkId (string): Network ID
        - mode (string): Set mode to 'enabled' to enable malware prevention, otherwise 'disabled'
        - allowedUrls (array): The urls that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP allow listing
        - allowedFiles (array): The sha256 digests of files that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP allow listing
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['disabled', 'enabled']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'malware'],
            'operation': 'updateNetworkApplianceSecurityMalware'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/security/malware'

        body_params = ['mode', 'allowedUrls', 'allowedFiles', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceSettings(self, networkId: str):
        """
        **Return the appliance settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-settings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'settings'],
            'operation': 'getNetworkApplianceSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceSettings(self, networkId: str, **kwargs):
        """
        **Update the appliance settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-settings

        - networkId (string): Network ID
        - clientTrackingMethod (string): Client tracking method of a network
        - deploymentMode (string): Deployment mode of a network
        - dynamicDns (object): Dynamic DNS settings for a network
        """

        kwargs.update(locals())

        if 'clientTrackingMethod' in kwargs:
            options = ['IP address', 'MAC address', 'Unique client identifier']
            assert kwargs['clientTrackingMethod'] in options, f'''"clientTrackingMethod" cannot be "{kwargs['clientTrackingMethod']}", & must be set to one of: {options}'''
        if 'deploymentMode' in kwargs:
            options = ['passthrough', 'routed']
            assert kwargs['deploymentMode'] in options, f'''"deploymentMode" cannot be "{kwargs['deploymentMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'settings'],
            'operation': 'updateNetworkApplianceSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/settings'

        body_params = ['clientTrackingMethod', 'deploymentMode', 'dynamicDns', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceSingleLan(self, networkId: str):
        """
        **Return single LAN configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-single-lan

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'singleLan'],
            'operation': 'getNetworkApplianceSingleLan'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/singleLan'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceSingleLan(self, networkId: str, **kwargs):
        """
        **Update single LAN configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan

        - networkId (string): Network ID
        - subnet (string): The subnet of the single LAN configuration
        - applianceIp (string): The appliance IP address of the single LAN
        - ipv6 (object): IPv6 configuration on the VLAN
        - mandatoryDhcp (object): Mandatory DHCP will enforce that clients connecting to this LAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'singleLan'],
            'operation': 'updateNetworkApplianceSingleLan'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/singleLan'

        body_params = ['subnet', 'applianceIp', 'ipv6', 'mandatoryDhcp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceSsids(self, networkId: str):
        """
        **List the MX SSIDs in a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssids

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'ssids'],
            'operation': 'getNetworkApplianceSsids'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/ssids'

        return self._session.get(metadata, resource)
        


    def getNetworkApplianceSsid(self, networkId: str, number: str):
        """
        **Return a single MX SSID**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ssid

        - networkId (string): Network ID
        - number (string): Number
        """

        metadata = {
            'tags': ['appliance', 'configure', 'ssids'],
            'operation': 'getNetworkApplianceSsid'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/appliance/ssids/{number}'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceSsid(self, networkId: str, number: str, **kwargs):
        """
        **Update the attributes of an MX SSID**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-ssid

        - networkId (string): Network ID
        - number (string): Number
        - name (string): The name of the SSID.
        - enabled (boolean): Whether or not the SSID is enabled.
        - defaultVlanId (integer): The VLAN ID of the VLAN associated to this SSID. This parameter is only valid if the network is in routed mode.
        - authMode (string): The association control method for the SSID ('open', 'psk', '8021x-meraki' or '8021x-radius').
        - psk (string): The passkey for the SSID. This param is only valid if the authMode is 'psk'.
        - radiusServers (array): The RADIUS 802.1x servers to be used for authentication. This param is only valid if the authMode is '8021x-radius'.
        - encryptionMode (string): The psk encryption mode for the SSID ('wep' or 'wpa'). This param is only valid if the authMode is 'psk'.
        - wpaEncryptionMode (string): The types of WPA encryption. ('WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode' or 'WPA3 only'). This param is only valid if (1) the authMode is 'psk' & the encryptionMode is 'wpa' OR (2) the authMode is '8021x-meraki' OR (3) the authMode is '8021x-radius'
        - visible (boolean): Boolean indicating whether the MX should advertise or hide this SSID.
        - dhcpEnforcedDeauthentication (object): DHCP Enforced Deauthentication enables the disassociation of wireless clients in addition to Mandatory DHCP. This param is only valid on firmware versions >= MX 17.0 where the associated LAN has Mandatory DHCP Enabled 
        - dot11w (object): The current setting for Protected Management Frames (802.11w).
        """

        kwargs.update(locals())

        if 'authMode' in kwargs:
            options = ['8021x-meraki', '8021x-radius', 'open', 'psk']
            assert kwargs['authMode'] in options, f'''"authMode" cannot be "{kwargs['authMode']}", & must be set to one of: {options}'''
        if 'encryptionMode' in kwargs:
            options = ['wep', 'wpa']
            assert kwargs['encryptionMode'] in options, f'''"encryptionMode" cannot be "{kwargs['encryptionMode']}", & must be set to one of: {options}'''
        if 'wpaEncryptionMode' in kwargs:
            options = ['WPA1 and WPA2', 'WPA2 only', 'WPA3 Transition Mode', 'WPA3 only']
            assert kwargs['wpaEncryptionMode'] in options, f'''"wpaEncryptionMode" cannot be "{kwargs['wpaEncryptionMode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'ssids'],
            'operation': 'updateNetworkApplianceSsid'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        number = urllib.parse.quote(str(number), safe='')
        resource = f'/networks/{networkId}/appliance/ssids/{number}'

        body_params = ['name', 'enabled', 'defaultVlanId', 'authMode', 'psk', 'radiusServers', 'encryptionMode', 'wpaEncryptionMode', 'visible', 'dhcpEnforcedDeauthentication', 'dot11w', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceStaticRoutes(self, networkId: str):
        """
        **List the static routes for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-routes

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'getNetworkApplianceStaticRoutes'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/staticRoutes'

        return self._session.get(metadata, resource)
        


    def createNetworkApplianceStaticRoute(self, networkId: str, name: str, subnet: str, gatewayIp: str, **kwargs):
        """
        **Add a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route

        - networkId (string): Network ID
        - name (string): Name of the route
        - subnet (string): Subnet of the route
        - gatewayIp (string): Gateway IP address (next hop)
        - gatewayVlanId (string): Gateway VLAN ID
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'createNetworkApplianceStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/staticRoutes'

        body_params = ['name', 'subnet', 'gatewayIp', 'gatewayVlanId', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkApplianceStaticRoute(self, networkId: str, staticRouteId: str):
        """
        **Return a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-route

        - networkId (string): Network ID
        - staticRouteId (string): Static route ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'getNetworkApplianceStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/networks/{networkId}/appliance/staticRoutes/{staticRouteId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceStaticRoute(self, networkId: str, staticRouteId: str, **kwargs):
        """
        **Update a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-static-route

        - networkId (string): Network ID
        - staticRouteId (string): Static route ID
        - name (string): Name of the route
        - subnet (string): Subnet of the route
        - gatewayIp (string): Gateway IP address (next hop)
        - gatewayVlanId (string): Gateway VLAN ID
        - enabled (boolean): Whether the route should be enabled or not
        - fixedIpAssignments (object): Fixed DHCP IP assignments on the route
        - reservedIpRanges (array): DHCP reserved IP ranges
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'updateNetworkApplianceStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/networks/{networkId}/appliance/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'gatewayIp', 'gatewayVlanId', 'enabled', 'fixedIpAssignments', 'reservedIpRanges', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkApplianceStaticRoute(self, networkId: str, staticRouteId: str):
        """
        **Delete a static route from an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-static-route

        - networkId (string): Network ID
        - staticRouteId (string): Static route ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'deleteNetworkApplianceStaticRoute'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        staticRouteId = urllib.parse.quote(str(staticRouteId), safe='')
        resource = f'/networks/{networkId}/appliance/staticRoutes/{staticRouteId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkApplianceTrafficShaping(self, networkId: str):
        """
        **Display the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping'],
            'operation': 'getNetworkApplianceTrafficShaping'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceTrafficShaping(self, networkId: str, **kwargs):
        """
        **Update the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping

        - networkId (string): Network ID
        - globalBandwidthLimits (object): Global per-client bandwidth limit
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping'],
            'operation': 'updateNetworkApplianceTrafficShaping'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping'

        body_params = ['globalBandwidthLimits', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceTrafficShapingCustomPerformanceClasses(self, networkId: str):
        """
        **List all custom performance classes for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-classes

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'getNetworkApplianceTrafficShapingCustomPerformanceClasses'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses'

        return self._session.get(metadata, resource)
        


    def createNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, name: str, **kwargs):
        """
        **Add a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - name (string): Name of the custom performance class
        - maxLatency (integer): Maximum latency in milliseconds
        - maxJitter (integer): Maximum jitter in milliseconds
        - maxLossPercentage (integer): Maximum percentage of packet loss
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'createNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses'

        body_params = ['name', 'maxLatency', 'maxJitter', 'maxLossPercentage', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str):
        """
        **Return a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - customPerformanceClassId (string): Custom performance class ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'getNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        customPerformanceClassId = urllib.parse.quote(str(customPerformanceClassId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str, **kwargs):
        """
        **Update a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - customPerformanceClassId (string): Custom performance class ID
        - name (string): Name of the custom performance class
        - maxLatency (integer): Maximum latency in milliseconds
        - maxJitter (integer): Maximum jitter in milliseconds
        - maxLossPercentage (integer): Maximum percentage of packet loss
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'updateNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        customPerformanceClassId = urllib.parse.quote(str(customPerformanceClassId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        body_params = ['name', 'maxLatency', 'maxJitter', 'maxLossPercentage', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str):
        """
        **Delete a custom performance class from an MX network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class

        - networkId (string): Network ID
        - customPerformanceClassId (string): Custom performance class ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'deleteNetworkApplianceTrafficShapingCustomPerformanceClass'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        customPerformanceClassId = urllib.parse.quote(str(customPerformanceClassId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        return self._session.delete(metadata, resource)
        


    def updateNetworkApplianceTrafficShapingRules(self, networkId: str, **kwargs):
        """
        **Update the traffic shaping settings rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules

        - networkId (string): Network ID
        - defaultRulesEnabled (boolean): Whether default traffic shaping rules are enabled (true) or disabled (false). There are 4 default rules, which can be seen on your network's traffic shaping page. Note that default rules count against the rule limit of 8.
        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'rules'],
            'operation': 'updateNetworkApplianceTrafficShapingRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/rules'

        body_params = ['defaultRulesEnabled', 'rules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceTrafficShapingRules(self, networkId: str):
        """
        **Display the traffic shaping settings rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-rules

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'rules'],
            'operation': 'getNetworkApplianceTrafficShapingRules'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/rules'

        return self._session.get(metadata, resource)
        


    def getNetworkApplianceTrafficShapingUplinkBandwidth(self, networkId: str):
        """
        **Returns the uplink bandwidth limits for your MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkBandwidth'],
            'operation': 'getNetworkApplianceTrafficShapingUplinkBandwidth'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceTrafficShapingUplinkBandwidth(self, networkId: str, **kwargs):
        """
        **Updates the uplink bandwidth settings for your MX network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth

        - networkId (string): Network ID
        - bandwidthLimits (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkBandwidth'],
            'operation': 'updateNetworkApplianceTrafficShapingUplinkBandwidth'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth'

        body_params = ['bandwidthLimits', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceTrafficShapingUplinkSelection(self, networkId: str):
        """
        **Show uplink selection settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-selection

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkSelection'],
            'operation': 'getNetworkApplianceTrafficShapingUplinkSelection'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkSelection'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceTrafficShapingUplinkSelection(self, networkId: str, **kwargs):
        """
        **Update uplink selection settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection

        - networkId (string): Network ID
        - activeActiveAutoVpnEnabled (boolean): Toggle for enabling or disabling active-active AutoVPN
        - defaultUplink (string): The default uplink. Must be one of: 'wan1' or 'wan2'
        - loadBalancingEnabled (boolean): Toggle for enabling or disabling load balancing
        - failoverAndFailback (object): WAN failover and failback behavior
        - wanTrafficUplinkPreferences (array): Array of uplink preference rules for WAN traffic
        - vpnTrafficUplinkPreferences (array): Array of uplink preference rules for VPN traffic
        """

        kwargs.update(locals())

        if 'defaultUplink' in kwargs:
            options = ['wan1', 'wan2']
            assert kwargs['defaultUplink'] in options, f'''"defaultUplink" cannot be "{kwargs['defaultUplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkSelection'],
            'operation': 'updateNetworkApplianceTrafficShapingUplinkSelection'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkSelection'

        body_params = ['activeActiveAutoVpnEnabled', 'defaultUplink', 'loadBalancingEnabled', 'failoverAndFailback', 'wanTrafficUplinkPreferences', 'vpnTrafficUplinkPreferences', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def updateNetworkApplianceTrafficShapingVpnExclusions(self, networkId: str, **kwargs):
        """
        **Update VPN exclusion rules for an MX network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-vpn-exclusions

        - networkId (string): Network ID
        - custom (array): Custom VPN exclusion rules. Pass an empty array to clear existing rules.
        - majorApplications (array): Major Application based VPN exclusion rules. Pass an empty array to clear existing rules.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'vpnExclusions'],
            'operation': 'updateNetworkApplianceTrafficShapingVpnExclusions'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/trafficShaping/vpnExclusions'

        body_params = ['custom', 'majorApplications', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceUplinksUsageHistory(self, networkId: str, **kwargs):
        """
        **Get the sent and received bytes for each uplink of a network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-uplinks-usage-history

        - networkId (string): Network ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 10 minutes.
        - resolution (integer): The time resolution in seconds for returned data. The valid resolutions are: 60, 300, 600, 1800, 3600, 86400. The default is 60.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'monitor', 'uplinks', 'usageHistory'],
            'operation': 'getNetworkApplianceUplinksUsageHistory'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/uplinks/usageHistory'

        query_params = ['t0', 't1', 'timespan', 'resolution', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getNetworkApplianceVlans(self, networkId: str):
        """
        **List the VLANs for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'getNetworkApplianceVlans'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans'

        return self._session.get(metadata, resource)
        


    def createNetworkApplianceVlan(self, networkId: str, id: str, name: str, **kwargs):
        """
        **Add a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan

        - networkId (string): Network ID
        - id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
        - name (string): The name of the new VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        - groupPolicyId (string): The id of the desired group policy to apply to the VLAN
        - templateVlanType (string): Type of subnetting of the VLAN. Applicable only for template network.
        - cidr (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
        - mask (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
        - ipv6 (object): IPv6 configuration on the VLAN
        - dhcpHandling (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
        - dhcpLeaseTime (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
        - mandatoryDhcp (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above
        - dhcpBootOptionsEnabled (boolean): Use DHCP boot options specified in other properties
        - dhcpOptions (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
        """

        kwargs.update(locals())

        if 'templateVlanType' in kwargs:
            options = ['same', 'unique']
            assert kwargs['templateVlanType'] in options, f'''"templateVlanType" cannot be "{kwargs['templateVlanType']}", & must be set to one of: {options}'''
        if 'dhcpHandling' in kwargs:
            options = ['Do not respond to DHCP requests', 'Relay DHCP to another server', 'Run a DHCP server']
            assert kwargs['dhcpHandling'] in options, f'''"dhcpHandling" cannot be "{kwargs['dhcpHandling']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['1 day', '1 hour', '1 week', '12 hours', '30 minutes', '4 hours']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'createNetworkApplianceVlan'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans'

        body_params = ['id', 'name', 'subnet', 'applianceIp', 'groupPolicyId', 'templateVlanType', 'cidr', 'mask', 'ipv6', 'dhcpHandling', 'dhcpLeaseTime', 'mandatoryDhcp', 'dhcpBootOptionsEnabled', 'dhcpOptions', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)
        


    def getNetworkApplianceVlansSettings(self, networkId: str):
        """
        **Returns the enabled status of VLANs for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans-settings

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans', 'settings'],
            'operation': 'getNetworkApplianceVlansSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans/settings'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceVlansSettings(self, networkId: str, **kwargs):
        """
        **Enable/Disable VLANs for the given network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings

        - networkId (string): Network ID
        - vlansEnabled (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vlans', 'settings'],
            'operation': 'updateNetworkApplianceVlansSettings'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans/settings'

        body_params = ['vlansEnabled', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceVlan(self, networkId: str, vlanId: str):
        """
        **Return a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlan

        - networkId (string): Network ID
        - vlanId (string): Vlan ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'getNetworkApplianceVlan'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        vlanId = urllib.parse.quote(str(vlanId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceVlan(self, networkId: str, vlanId: str, **kwargs):
        """
        **Update a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan

        - networkId (string): Network ID
        - vlanId (string): Vlan ID
        - name (string): The name of the VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        - groupPolicyId (string): The id of the desired group policy to apply to the VLAN
        - vpnNatSubnet (string): The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN
        - dhcpHandling (string): The appliance's handling of DHCP requests on this VLAN. One of: 'Run a DHCP server', 'Relay DHCP to another server' or 'Do not respond to DHCP requests'
        - dhcpRelayServerIps (array): The IPs of the DHCP servers that DHCP requests should be relayed to
        - dhcpLeaseTime (string): The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of: '30 minutes', '1 hour', '4 hours', '12 hours', '1 day' or '1 week'
        - dhcpBootOptionsEnabled (boolean): Use DHCP boot options specified in other properties
        - dhcpBootNextServer (string): DHCP boot option to direct boot clients to the server to load the boot file from
        - dhcpBootFilename (string): DHCP boot option for boot filename
        - fixedIpAssignments (object): The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
        - reservedIpRanges (array): The DHCP reserved IP ranges on the VLAN
        - dnsNameservers (string): The DNS nameservers used for DHCP responses, either "upstream_dns", "google_dns", "opendns", or a newline seperated string of IP addresses or domain names
        - dhcpOptions (array): The list of DHCP options that will be included in DHCP responses. Each object in the list should have "code", "type", and "value" properties.
        - templateVlanType (string): Type of subnetting of the VLAN. Applicable only for template network.
        - cidr (string): CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN.
        - mask (integer): Mask used for the subnet of all bound to the template networks. Applicable only for template network.
        - ipv6 (object): IPv6 configuration on the VLAN
        - mandatoryDhcp (object): Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won't be able to associate. Only available on firmware versions 17.0 and above
        """

        kwargs.update(locals())

        if 'dhcpHandling' in kwargs:
            options = ['Do not respond to DHCP requests', 'Relay DHCP to another server', 'Run a DHCP server']
            assert kwargs['dhcpHandling'] in options, f'''"dhcpHandling" cannot be "{kwargs['dhcpHandling']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['1 day', '1 hour', '1 week', '12 hours', '30 minutes', '4 hours']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''
        if 'templateVlanType' in kwargs:
            options = ['same', 'unique']
            assert kwargs['templateVlanType'] in options, f'''"templateVlanType" cannot be "{kwargs['templateVlanType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'updateNetworkApplianceVlan'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        vlanId = urllib.parse.quote(str(vlanId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        body_params = ['name', 'subnet', 'applianceIp', 'groupPolicyId', 'vpnNatSubnet', 'dhcpHandling', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dhcpBootOptionsEnabled', 'dhcpBootNextServer', 'dhcpBootFilename', 'fixedIpAssignments', 'reservedIpRanges', 'dnsNameservers', 'dhcpOptions', 'templateVlanType', 'cidr', 'mask', 'ipv6', 'mandatoryDhcp', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def deleteNetworkApplianceVlan(self, networkId: str, vlanId: str):
        """
        **Delete a VLAN from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan

        - networkId (string): Network ID
        - vlanId (string): Vlan ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'deleteNetworkApplianceVlan'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        vlanId = urllib.parse.quote(str(vlanId), safe='')
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        return self._session.delete(metadata, resource)
        


    def getNetworkApplianceVpnBgp(self, networkId: str):
        """
        **Return a Hub BGP Configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-bgp

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'bgp'],
            'operation': 'getNetworkApplianceVpnBgp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vpn/bgp'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceVpnBgp(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update a Hub BGP Configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp

        - networkId (string): Network ID
        - enabled (boolean): Boolean value to enable or disable the BGP configuration. When BGP is enabled, the asNumber (ASN) will be autopopulated with the preconfigured ASN at other Hubs or a default value if there is no ASN configured.
        - asNumber (integer): An Autonomous System Number (ASN) is required if you are to run BGP and peer with another BGP Speaker outside of the Auto VPN domain. This ASN will be applied to the entire Auto VPN domain. The entire 4-byte ASN range is supported. So, the ASN must be an integer between 1 and 4294967295. When absent, this field is not updated. If no value exists then it defaults to 64512.
        - ibgpHoldTimer (integer): The iBGP holdtimer in seconds. The iBGP holdtimer must be an integer between 12 and 240. When absent, this field is not updated. If no value exists then it defaults to 240.
        - neighbors (array): List of BGP neighbors. This list replaces the existing set of neighbors. When absent, this field is not updated.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'bgp'],
            'operation': 'updateNetworkApplianceVpnBgp'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vpn/bgp'

        body_params = ['enabled', 'asNumber', 'ibgpHoldTimer', 'neighbors', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceVpnSiteToSiteVpn(self, networkId: str):
        """
        **Return the site-to-site VPN settings of a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-site-to-site-vpn

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'siteToSiteVpn'],
            'operation': 'getNetworkApplianceVpnSiteToSiteVpn'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vpn/siteToSiteVpn'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceVpnSiteToSiteVpn(self, networkId: str, mode: str, **kwargs):
        """
        **Update the site-to-site VPN settings of a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn

        - networkId (string): Network ID
        - mode (string): The site-to-site VPN mode. Can be one of 'none', 'spoke' or 'hub'
        - hubs (array): The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required.
        - subnets (array): The list of subnets and their VPN presence.
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['hub', 'none', 'spoke']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'siteToSiteVpn'],
            'operation': 'updateNetworkApplianceVpnSiteToSiteVpn'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/vpn/siteToSiteVpn'

        body_params = ['mode', 'hubs', 'subnets', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getNetworkApplianceWarmSpare(self, networkId: str):
        """
        **Return MX warm spare settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-warm-spare

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'getNetworkApplianceWarmSpare'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/warmSpare'

        return self._session.get(metadata, resource)
        


    def updateNetworkApplianceWarmSpare(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update MX warm spare settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare

        - networkId (string): Network ID
        - enabled (boolean): Enable warm spare
        - spareSerial (string): Serial number of the warm spare appliance
        - uplinkMode (string): Uplink mode, either virtual or public
        - virtualIp1 (string): The WAN 1 shared IP
        - virtualIp2 (string): The WAN 2 shared IP
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'updateNetworkApplianceWarmSpare'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/warmSpare'

        body_params = ['enabled', 'spareSerial', 'uplinkMode', 'virtualIp1', 'virtualIp2', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def swapNetworkApplianceWarmSpare(self, networkId: str):
        """
        **Swap MX primary and warm spare appliances**
        https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare

        - networkId (string): Network ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'swapNetworkApplianceWarmSpare'
        }
        networkId = urllib.parse.quote(str(networkId), safe='')
        resource = f'/networks/{networkId}/appliance/warmSpare/swap'

        return self._session.post(metadata, resource)
        


    def getOrganizationApplianceSecurityEvents(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. Data is gathered after the specified t0 value. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 365 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 365 days. The default is 31 days.
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - sortOrder (string): Sorted order of security events based on event detection time. Order options are 'ascending' or 'descending'. Default is ascending order.
        """

        kwargs.update(locals())

        if 'sortOrder' in kwargs:
            options = ['ascending', 'descending']
            assert kwargs['sortOrder'] in options, f'''"sortOrder" cannot be "{kwargs['sortOrder']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'monitor', 'security', 'events'],
            'operation': 'getOrganizationApplianceSecurityEvents'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/security/events'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationApplianceSecurityIntrusion(self, organizationId: str):
        """
        **Returns all supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'getOrganizationApplianceSecurityIntrusion'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/security/intrusion'

        return self._session.get(metadata, resource)
        


    def updateOrganizationApplianceSecurityIntrusion(self, organizationId: str, allowedRules: list):
        """
        **Sets supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion

        - organizationId (string): Organization ID
        - allowedRules (array): Sets a list of specific SNORT signatures to allow
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'updateOrganizationApplianceSecurityIntrusion'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/security/intrusion'

        body_params = ['allowedRules', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Display VPN exclusion rules for MX networks.**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-traffic-shaping-vpn-exclusions-by-network

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): Optional parameter to filter the results by network IDs
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'vpnExclusions', 'byNetwork'],
            'operation': 'getOrganizationApplianceTrafficShapingVpnExclusionsByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/trafficShaping/vpnExclusions/byNetwork'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationApplianceUplinkStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the uplink status of every Meraki MX and Z series appliances in the organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplink-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of network IDs. The returned devices will be filtered to only include these networks.
        - serials (array): A list of serial numbers. The returned devices will be filtered to only include these serials.
        - iccids (array): A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'monitor', 'uplinks', 'statuses'],
            'operation': 'getOrganizationApplianceUplinkStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/uplink/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 'serials', 'iccids', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', 'serials', 'iccids', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationApplianceUplinksStatusesOverview(self, organizationId: str):
        """
        **Returns an overview of uplink statuses**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplinks-statuses-overview

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'uplinks', 'statuses', 'overview'],
            'operation': 'getOrganizationApplianceUplinksStatusesOverview'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/uplinks/statuses/overview'

        return self._session.get(metadata, resource)
        


    def getOrganizationApplianceUplinksUsageByNetwork(self, organizationId: str, **kwargs):
        """
        **Get the sent and received bytes for each uplink of all MX and Z networks within an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-uplinks-usage-by-network

        - organizationId (string): Organization ID
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 14 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'monitor', 'uplinks', 'usage', 'byNetwork'],
            'operation': 'getOrganizationApplianceUplinksUsageByNetwork'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/uplinks/usage/byNetwork'

        query_params = ['t0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)
        


    def getOrganizationApplianceVpnStats(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Show VPN history stat for networks in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-stats

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
        - t1 (string): The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
        - timespan (number): The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'monitor', 'vpn', 'stats'],
            'operation': 'getOrganizationApplianceVpnStats'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/stats'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', 't0', 't1', 'timespan', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationApplianceVpnStatuses(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **Show VPN status for networks in an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-statuses

        - organizationId (string): Organization ID
        - total_pages (integer or string): use with perPage to get total results up to total_pages*perPage; -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - perPage (integer): The number of entries per page returned. Acceptable range is 3 - 300. Default is 300.
        - startingAfter (string): A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - endingBefore (string): A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
        - networkIds (array): A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]=N_12345678&networkIds[]=L_3456
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'monitor', 'vpn', 'statuses'],
            'operation': 'getOrganizationApplianceVpnStatuses'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/statuses'

        query_params = ['perPage', 'startingAfter', 'endingBefore', 'networkIds', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        array_params = ['networkIds', ]
        for k, v in kwargs.items():
            if k.strip() in array_params:
                params[f'{k.strip()}[]'] = kwargs[f'{k}']
                params.pop(k.strip())

        return self._session.get_pages(metadata, resource, params, total_pages, direction)
        


    def getOrganizationApplianceVpnThirdPartyVPNPeers(self, organizationId: str):
        """
        **Return the third party VPN peers for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-third-party-v-p-n-peers

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'thirdPartyVPNPeers'],
            'operation': 'getOrganizationApplianceVpnThirdPartyVPNPeers'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers'

        return self._session.get(metadata, resource)
        


    def updateOrganizationApplianceVpnThirdPartyVPNPeers(self, organizationId: str, peers: list):
        """
        **Update the third party VPN peers for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-v-p-n-peers

        - organizationId (string): Organization ID
        - peers (array): The list of VPN peers
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'thirdPartyVPNPeers'],
            'operation': 'updateOrganizationApplianceVpnThirdPartyVPNPeers'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers'

        body_params = ['peers', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        


    def getOrganizationApplianceVpnVpnFirewallRules(self, organizationId: str):
        """
        **Return the firewall rules for an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules

        - organizationId (string): Organization ID
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'vpnFirewallRules'],
            'operation': 'getOrganizationApplianceVpnVpnFirewallRules'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/vpnFirewallRules'

        return self._session.get(metadata, resource)
        


    def updateOrganizationApplianceVpnVpnFirewallRules(self, organizationId: str, **kwargs):
        """
        **Update the firewall rules of an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-vpn-firewall-rules

        - organizationId (string): Organization ID
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'vpnFirewallRules'],
            'operation': 'updateOrganizationApplianceVpnVpnFirewallRules'
        }
        organizationId = urllib.parse.quote(str(organizationId), safe='')
        resource = f'/organizations/{organizationId}/appliance/vpn/vpnFirewallRules'

        body_params = ['rules', 'syslogDefaultRule', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)
        
