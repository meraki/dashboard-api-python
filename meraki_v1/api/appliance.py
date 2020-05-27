class Appliance(object):
    def __init__(self, session):
        super(Appliance, self).__init__()
        self._session = session

    def getDeviceApplianceDhcpSubnets(self, serial: str):
        """
        **Return the DHCP subnet information for an appliance**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-dhcp-subnets
        
        - serial (string)
        """

        metadata = {
            'tags': ['appliance', 'monitor', 'dhcp', 'subnets'],
            'operation': 'getDeviceApplianceDhcpSubnets',
        }
        resource = f'/devices/{serial}/appliance/dhcp/subnets'

        return self._session.get(metadata, resource)

    def getDeviceAppliancePerformance(self, serial: str):
        """
        **Return the performance score for a single device. Only primary MX devices supported. If no data is available, a 204 error code is returned.**
        https://developer.cisco.com/meraki/api-v1/#!get-device-appliance-performance
        
        - serial (string)
        """

        metadata = {
            'tags': ['appliance', 'monitor', 'performance'],
            'operation': 'getDeviceAppliancePerformance',
        }
        resource = f'/devices/{serial}/appliance/performance'

        return self._session.get(metadata, resource)

    def getNetworkApplianceClientSecurityEvents(self, networkId: str, clientId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-client-security-events
        
        - networkId (string)
        - clientId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 791 days from today.
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
            'operation': 'getNetworkApplianceClientSecurityEvents',
        }
        resource = f'/networks/{networkId}/appliance/clients/{clientId}/security/events'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkApplianceConnectivityMonitoringDestinations(self, networkId: str):
        """
        **Return the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-connectivity-monitoring-destinations
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'getNetworkApplianceConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/appliance/connectivityMonitoringDestinations'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceConnectivityMonitoringDestinations(self, networkId: str, **kwargs):
        """
        **Update the connectivity testing destinations for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-connectivity-monitoring-destinations
        
        - networkId (string)
        - destinations (array): The list of connectivity monitoring destinations
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'connectivityMonitoringDestinations'],
            'operation': 'updateNetworkApplianceConnectivityMonitoringDestinations',
        }
        resource = f'/networks/{networkId}/appliance/connectivityMonitoringDestinations'

        body_params = ['destinations']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceContentFiltering(self, networkId: str):
        """
        **Return the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'contentFiltering'],
            'operation': 'getNetworkApplianceContentFiltering',
        }
        resource = f'/networks/{networkId}/appliance/contentFiltering'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceContentFiltering(self, networkId: str, **kwargs):
        """
        **Update the content filtering settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-content-filtering
        
        - networkId (string)
        - allowedUrlPatterns (array): A whitelist of URL patterns to allow
        - blockedUrlPatterns (array): A blacklist of URL patterns to block
        - blockedUrlCategories (array): A list of URL categories to block
        - urlCategoryListSize (string): URL category list size which is either 'topSites' or 'fullList'
        """

        kwargs.update(locals())

        if 'urlCategoryListSize' in kwargs:
            options = ['topSites', 'fullList']
            assert kwargs['urlCategoryListSize'] in options, f'''"urlCategoryListSize" cannot be "{kwargs['urlCategoryListSize']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'contentFiltering'],
            'operation': 'updateNetworkApplianceContentFiltering',
        }
        resource = f'/networks/{networkId}/appliance/contentFiltering'

        body_params = ['allowedUrlPatterns', 'blockedUrlPatterns', 'blockedUrlCategories', 'urlCategoryListSize']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceContentFilteringCategories(self, networkId: str):
        """
        **List all available content filtering categories for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-content-filtering-categories
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'contentFiltering', 'categories'],
            'operation': 'getNetworkApplianceContentFilteringCategories',
        }
        resource = f'/networks/{networkId}/appliance/contentFiltering/categories'

        return self._session.get(metadata, resource)

    def getNetworkApplianceFirewallCellularFirewallRules(self, networkId: str):
        """
        **Return the cellular firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-cellular-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'cellularFirewallRules'],
            'operation': 'getNetworkApplianceFirewallCellularFirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/cellularFirewallRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallCellularFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the cellular firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-cellular-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'cellularFirewallRules'],
            'operation': 'updateNetworkApplianceFirewallCellularFirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/cellularFirewallRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceFirewallFirewalledServices(self, networkId: str):
        """
        **List the appliance services and their accessibility rules**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-services
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'firewalledServices'],
            'operation': 'getNetworkApplianceFirewallFirewalledServices',
        }
        resource = f'/networks/{networkId}/appliance/firewall/firewalledServices'

        return self._session.get(metadata, resource)

    def getNetworkApplianceFirewallFirewalledService(self, networkId: str, service: str):
        """
        **Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-firewalled-service
        
        - networkId (string)
        - service (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'firewalledServices'],
            'operation': 'getNetworkApplianceFirewallFirewalledService',
        }
        resource = f'/networks/{networkId}/appliance/firewall/firewalledServices/{service}'

        return self._session.get(metadata, resource)

    def getNetworkApplianceFirewallInboundFirewallRules(self, networkId: str):
        """
        **Return the inbound firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-inbound-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'inboundFirewallRules'],
            'operation': 'getNetworkApplianceFirewallInboundFirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/inboundFirewallRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallInboundFirewallRules(self, networkId: str, **kwargs):
        """
        **Update the inbound firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-inbound-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'inboundFirewallRules'],
            'operation': 'updateNetworkApplianceFirewallInboundFirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/inboundFirewallRules'

        body_params = ['rules', 'syslogDefaultRule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceFirewallL3FirewallRules(self, networkId: str):
        """
        **Return the L3 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-3-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l3FirewallRules'],
            'operation': 'getNetworkApplianceFirewallL3FirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/l3FirewallRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallL3FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the L3 firewall rules of an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-3-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l3FirewallRules'],
            'operation': 'updateNetworkApplianceFirewallL3FirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/l3FirewallRules'

        body_params = ['rules', 'syslogDefaultRule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceFirewallL7FirewallRules(self, networkId: str):
        """
        **List the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules'],
            'operation': 'getNetworkApplianceFirewallL7FirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallL7FirewallRules(self, networkId: str, **kwargs):
        """
        **Update the MX L7 firewall rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-l-7-firewall-rules
        
        - networkId (string)
        - rules (array): An ordered array of the MX L7 firewall rules
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules'],
            'operation': 'updateNetworkApplianceFirewallL7FirewallRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceFirewallL7FirewallRulesApplicationCategories(self, networkId: str):
        """
        **Return the L7 firewall application categories and their associated applications for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-l-7-firewall-rules-application-categories
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'l7FirewallRules', 'applicationCategories'],
            'operation': 'getNetworkApplianceFirewallL7FirewallRulesApplicationCategories',
        }
        resource = f'/networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories'

        return self._session.get(metadata, resource)

    def getNetworkApplianceFirewallOneToManyNatRules(self, networkId: str):
        """
        **Return the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-many-nat-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToManyNatRules'],
            'operation': 'getNetworkApplianceFirewallOneToManyNatRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/oneToManyNatRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallOneToManyNatRules(self, networkId: str, rules: list):
        """
        **Set the 1:Many NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-many-nat-rules
        
        - networkId (string)
        - rules (array): An array of 1:Many nat rules
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToManyNatRules'],
            'operation': 'updateNetworkApplianceFirewallOneToManyNatRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/oneToManyNatRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceFirewallOneToOneNatRules(self, networkId: str):
        """
        **Return the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-one-to-one-nat-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToOneNatRules'],
            'operation': 'getNetworkApplianceFirewallOneToOneNatRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/oneToOneNatRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallOneToOneNatRules(self, networkId: str, rules: list):
        """
        **Set the 1:1 NAT mapping rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-one-to-one-nat-rules
        
        - networkId (string)
        - rules (array): An array of 1:1 nat rules
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'oneToOneNatRules'],
            'operation': 'updateNetworkApplianceFirewallOneToOneNatRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/oneToOneNatRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceFirewallPortForwardingRules(self, networkId: str):
        """
        **Return the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-firewall-port-forwarding-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'portForwardingRules'],
            'operation': 'getNetworkApplianceFirewallPortForwardingRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/portForwardingRules'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceFirewallPortForwardingRules(self, networkId: str, rules: list):
        """
        **Update the port forwarding rules for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-firewall-port-forwarding-rules
        
        - networkId (string)
        - rules (array): An array of port forwarding params
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'firewall', 'portForwardingRules'],
            'operation': 'updateNetworkApplianceFirewallPortForwardingRules',
        }
        resource = f'/networks/{networkId}/appliance/firewall/portForwardingRules'

        body_params = ['rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkAppliancePorts(self, networkId: str):
        """
        **List per-port VLAN settings for all ports of a MX.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-ports
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'ports'],
            'operation': 'getNetworkAppliancePorts',
        }
        resource = f'/networks/{networkId}/appliance/ports'

        return self._session.get(metadata, resource)

    def getNetworkAppliancePort(self, networkId: str, portId: str):
        """
        **Return per-port VLAN settings for a single MX port.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-port
        
        - networkId (string)
        - portId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'ports'],
            'operation': 'getNetworkAppliancePort',
        }
        resource = f'/networks/{networkId}/appliance/ports/{portId}'

        return self._session.get(metadata, resource)

    def updateNetworkAppliancePort(self, networkId: str, portId: str, **kwargs):
        """
        **Update the per-port VLAN settings for a single MX port.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-port
        
        - networkId (string)
        - portId (string)
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
            'operation': 'updateNetworkAppliancePort',
        }
        resource = f'/networks/{networkId}/appliance/ports/{portId}'

        body_params = ['enabled', 'dropUntaggedTraffic', 'type', 'vlan', 'allowedVlans', 'accessPolicy']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceSecurityEvents(self, networkId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events for a network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-events
        
        - networkId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
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
            'operation': 'getNetworkApplianceSecurityEvents',
        }
        resource = f'/networks/{networkId}/appliance/security/events'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getNetworkApplianceSecurityIntrusion(self, networkId: str):
        """
        **Returns all supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-intrusion
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'getNetworkApplianceSecurityIntrusion',
        }
        resource = f'/networks/{networkId}/appliance/security/intrusion'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceSecurityIntrusion(self, networkId: str, **kwargs):
        """
        **Set the supported intrusion settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-intrusion
        
        - networkId (string)
        - mode (string): Set mode to 'disabled'/'detection'/'prevention' (optional - omitting will leave current config unchanged)
        - idsRulesets (string): Set the detection ruleset 'connectivity'/'balanced'/'security' (optional - omitting will leave current config unchanged). Default value is 'balanced' if none currently saved
        - protectedNetworks (object): Set the included/excluded networks from the intrusion engine (optional - omitting will leave current config unchanged). This is available only in 'passthrough' mode
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['prevention', 'detection', 'disabled']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''
        if 'idsRulesets' in kwargs:
            options = ['connectivity', 'balanced', 'security']
            assert kwargs['idsRulesets'] in options, f'''"idsRulesets" cannot be "{kwargs['idsRulesets']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'updateNetworkApplianceSecurityIntrusion',
        }
        resource = f'/networks/{networkId}/appliance/security/intrusion'

        body_params = ['mode', 'idsRulesets', 'protectedNetworks']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceSecurityMalware(self, networkId: str):
        """
        **Returns all supported malware settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-security-malware
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'malware'],
            'operation': 'getNetworkApplianceSecurityMalware',
        }
        resource = f'/networks/{networkId}/appliance/security/malware'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceSecurityMalware(self, networkId: str, mode: str, **kwargs):
        """
        **Set the supported malware settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-security-malware
        
        - networkId (string)
        - mode (string): Set mode to 'enabled' to enable malware prevention, otherwise 'disabled'
        - allowedUrls (array): The urls that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP whitelisting
        - allowedFiles (array): The sha256 digests of files that should be permitted by the malware detection engine. If omitted, the current config will remain unchanged. This is available only if your network supports AMP whitelisting
        """

        kwargs.update(locals())

        if 'mode' in kwargs:
            options = ['enabled', 'disabled']
            assert kwargs['mode'] in options, f'''"mode" cannot be "{kwargs['mode']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'malware'],
            'operation': 'updateNetworkApplianceSecurityMalware',
        }
        resource = f'/networks/{networkId}/appliance/security/malware'

        body_params = ['mode', 'allowedUrls', 'allowedFiles']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceSingleLan(self, networkId: str):
        """
        **Return single LAN configuration**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-single-lan
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'singleLan'],
            'operation': 'getNetworkApplianceSingleLan',
        }
        resource = f'/networks/{networkId}/appliance/singleLan'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceSingleLan(self, networkId: str, **kwargs):
        """
        **Update single LAN configuration**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-single-lan
        
        - networkId (string)
        - subnet (string): The subnet of the single LAN configuration
        - applianceIp (string): The appliance IP address of the single LAN
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'singleLan'],
            'operation': 'updateNetworkApplianceSingleLan',
        }
        resource = f'/networks/{networkId}/appliance/singleLan'

        body_params = ['subnet', 'applianceIp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceStaticRoutes(self, networkId: str):
        """
        **List the static routes for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-routes
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'getNetworkApplianceStaticRoutes',
        }
        resource = f'/networks/{networkId}/appliance/staticRoutes'

        return self._session.get(metadata, resource)

    def createNetworkApplianceStaticRoute(self, networkId: str, name: str, subnet: str, gatewayIp: str):
        """
        **Add a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-static-route
        
        - networkId (string)
        - name (string): The name of the new static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'createNetworkApplianceStaticRoute',
        }
        resource = f'/networks/{networkId}/appliance/staticRoutes'

        body_params = ['name', 'subnet', 'gatewayIp']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkApplianceStaticRoute(self, networkId: str, staticRouteId: str):
        """
        **Return a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-static-route
        
        - networkId (string)
        - staticRouteId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'getNetworkApplianceStaticRoute',
        }
        resource = f'/networks/{networkId}/appliance/staticRoutes/{staticRouteId}'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceStaticRoute(self, networkId: str, staticRouteId: str, **kwargs):
        """
        **Update a static route for an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-static-route
        
        - networkId (string)
        - staticRouteId (string)
        - name (string): The name of the static route
        - subnet (string): The subnet of the static route
        - gatewayIp (string): The gateway IP (next hop) of the static route
        - enabled (boolean): The enabled state of the static route
        - fixedIpAssignments (object): The DHCP fixed IP assignments on the static route. This should be an object that contains mappings from MAC addresses to objects that themselves each contain "ip" and "name" string fields. See the sample request/response for more details.
        - reservedIpRanges (array): The DHCP reserved IP ranges on the static route
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'updateNetworkApplianceStaticRoute',
        }
        resource = f'/networks/{networkId}/appliance/staticRoutes/{staticRouteId}'

        body_params = ['name', 'subnet', 'gatewayIp', 'enabled', 'fixedIpAssignments', 'reservedIpRanges']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkApplianceStaticRoute(self, networkId: str, staticRouteId: str):
        """
        **Delete a static route from an MX or teleworker network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-static-route
        
        - networkId (string)
        - staticRouteId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'staticRoutes'],
            'operation': 'deleteNetworkApplianceStaticRoute',
        }
        resource = f'/networks/{networkId}/appliance/staticRoutes/{staticRouteId}'

        return self._session.delete(metadata, resource)

    def getNetworkApplianceTrafficShapingCustomPerformanceClasses(self, networkId: str):
        """
        **List all custom performance classes for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-classes
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'getNetworkApplianceTrafficShapingCustomPerformanceClasses',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses'

        return self._session.get(metadata, resource)

    def createNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, name: str, **kwargs):
        """
        **Add a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-traffic-shaping-custom-performance-class
        
        - networkId (string)
        - name (string): Name of the custom performance class
        - maxLatency (integer): Maximum latency in milliseconds
        - maxJitter (integer): Maximum jitter in milliseconds
        - maxLossPercentage (integer): Maximum percentage of packet loss
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'createNetworkApplianceTrafficShapingCustomPerformanceClass',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses'

        body_params = ['name', 'maxLatency', 'maxJitter', 'maxLossPercentage']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str):
        """
        **Return a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-custom-performance-class
        
        - networkId (string)
        - customPerformanceClassId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'getNetworkApplianceTrafficShapingCustomPerformanceClass',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str, **kwargs):
        """
        **Update a custom performance class for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-custom-performance-class
        
        - networkId (string)
        - customPerformanceClassId (string)
        - name (string): Name of the custom performance class
        - maxLatency (integer): Maximum latency in milliseconds
        - maxJitter (integer): Maximum jitter in milliseconds
        - maxLossPercentage (integer): Maximum percentage of packet loss
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'updateNetworkApplianceTrafficShapingCustomPerformanceClass',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        body_params = ['name', 'maxLatency', 'maxJitter', 'maxLossPercentage']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkApplianceTrafficShapingCustomPerformanceClass(self, networkId: str, customPerformanceClassId: str):
        """
        **Delete a custom performance class from an MX network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-traffic-shaping-custom-performance-class
        
        - networkId (string)
        - customPerformanceClassId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'customPerformanceClasses'],
            'operation': 'deleteNetworkApplianceTrafficShapingCustomPerformanceClass',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}'

        return self._session.delete(metadata, resource)

    def updateNetworkApplianceTrafficShapingRules(self, networkId: str, **kwargs):
        """
        **Update the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-rules
        
        - networkId (string)
        - defaultRulesEnabled (boolean):     Whether default traffic shaping rules are enabled (true) or disabled (false).
    There are 4 default rules, which can
    be seen on your network's traffic shaping page. Note that default rules
    count against the rule limit of 8.

        - rules (array):     An array of traffic shaping rules. Rules are applied in the order that
    they are specified in. An empty list (or null) means no rules. Note that
    you are allowed a maximum of 8 rules.

        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'rules'],
            'operation': 'updateNetworkApplianceTrafficShapingRules',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/rules'

        body_params = ['defaultRulesEnabled', 'rules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceTrafficShapingRules(self, networkId: str):
        """
        **Display the traffic shaping settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-rules
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'rules'],
            'operation': 'getNetworkApplianceTrafficShapingRules',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/rules'

        return self._session.get(metadata, resource)

    def getNetworkApplianceTrafficShapingUplinkBandwidth(self, networkId: str):
        """
        **Returns the uplink bandwidth settings for your MX network.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-bandwidth
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkBandwidth'],
            'operation': 'getNetworkApplianceTrafficShapingUplinkBandwidth',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceTrafficShapingUplinkBandwidth(self, networkId: str, **kwargs):
        """
        **Updates the uplink bandwidth settings for your MX network.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-bandwidth
        
        - networkId (string)
        - bandwidthLimits (object): A mapping of uplinks to their bandwidth settings (be sure to check which uplinks are supported for your network)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkBandwidth'],
            'operation': 'updateNetworkApplianceTrafficShapingUplinkBandwidth',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth'

        body_params = ['bandwidthLimits']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceTrafficShapingUplinkSelection(self, networkId: str):
        """
        **Show uplink selection settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-traffic-shaping-uplink-selection
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkSelection'],
            'operation': 'getNetworkApplianceTrafficShapingUplinkSelection',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkSelection'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceTrafficShapingUplinkSelection(self, networkId: str, **kwargs):
        """
        **Update uplink selection settings for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection
        
        - networkId (string)
        - activeActiveAutoVpnEnabled (boolean): Toggle for enabling or disabling active-active AutoVPN
        - defaultUplink (string): The default uplink. Must be one of: 'wan1' or 'wan2'
        - loadBalancingEnabled (boolean): Toggle for enabling or disabling load balancing
        - wanTrafficUplinkPreferences (array): Array of uplink preference rules for WAN traffic
        - vpnTrafficUplinkPreferences (array): Array of uplink preference rules for VPN traffic
        """

        kwargs.update(locals())

        if 'defaultUplink' in kwargs:
            options = ['wan1', 'wan2']
            assert kwargs['defaultUplink'] in options, f'''"defaultUplink" cannot be "{kwargs['defaultUplink']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'trafficShaping', 'uplinkSelection'],
            'operation': 'updateNetworkApplianceTrafficShapingUplinkSelection',
        }
        resource = f'/networks/{networkId}/appliance/trafficShaping/uplinkSelection'

        body_params = ['activeActiveAutoVpnEnabled', 'defaultUplink', 'loadBalancingEnabled', 'wanTrafficUplinkPreferences', 'vpnTrafficUplinkPreferences']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceVlans(self, networkId: str):
        """
        **List the VLANs for an MX network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'getNetworkApplianceVlans',
        }
        resource = f'/networks/{networkId}/appliance/vlans'

        return self._session.get(metadata, resource)

    def createNetworkApplianceVlan(self, networkId: str, id: str, name: str, subnet: str, applianceIp: str, **kwargs):
        """
        **Add a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan
        
        - networkId (string)
        - id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
        - name (string): The name of the new VLAN
        - subnet (string): The subnet of the VLAN
        - applianceIp (string): The local IP of the appliance on the VLAN
        - groupPolicyId (string): The id of the desired group policy to apply to the VLAN
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'createNetworkApplianceVlan',
        }
        resource = f'/networks/{networkId}/appliance/vlans'

        body_params = ['id', 'name', 'subnet', 'applianceIp', 'groupPolicyId']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkApplianceVlansSettings(self, networkId: str):
        """
        **Returns the enabled status of VLANs for the network**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlans-settings
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans', 'settings'],
            'operation': 'getNetworkApplianceVlansSettings',
        }
        resource = f'/networks/{networkId}/appliance/vlans/settings'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceVlansSettings(self, networkId: str, **kwargs):
        """
        **Enable/Disable VLANs for the given network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlans-settings
        
        - networkId (string)
        - vlansEnabled (boolean): Boolean indicating whether to enable (true) or disable (false) VLANs for the network
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vlans', 'settings'],
            'operation': 'updateNetworkApplianceVlansSettings',
        }
        resource = f'/networks/{networkId}/appliance/vlans/settings'

        body_params = ['vlansEnabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceVlan(self, networkId: str, vlanId: str):
        """
        **Return a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vlan
        
        - networkId (string)
        - vlanId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'getNetworkApplianceVlan',
        }
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceVlan(self, networkId: str, vlanId: str, **kwargs):
        """
        **Update a VLAN**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan
        
        - networkId (string)
        - vlanId (string)
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
        """

        kwargs.update(locals())

        if 'dhcpHandling' in kwargs:
            options = ['Run a DHCP server', 'Relay DHCP to another server', 'Do not respond to DHCP requests']
            assert kwargs['dhcpHandling'] in options, f'''"dhcpHandling" cannot be "{kwargs['dhcpHandling']}", & must be set to one of: {options}'''
        if 'dhcpLeaseTime' in kwargs:
            options = ['30 minutes', '1 hour', '4 hours', '12 hours', '1 day', '1 week']
            assert kwargs['dhcpLeaseTime'] in options, f'''"dhcpLeaseTime" cannot be "{kwargs['dhcpLeaseTime']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'updateNetworkApplianceVlan',
        }
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        body_params = ['name', 'subnet', 'applianceIp', 'groupPolicyId', 'vpnNatSubnet', 'dhcpHandling', 'dhcpRelayServerIps', 'dhcpLeaseTime', 'dhcpBootOptionsEnabled', 'dhcpBootNextServer', 'dhcpBootFilename', 'fixedIpAssignments', 'reservedIpRanges', 'dnsNameservers', 'dhcpOptions']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkApplianceVlan(self, networkId: str, vlanId: str):
        """
        **Delete a VLAN from a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan
        
        - networkId (string)
        - vlanId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vlans'],
            'operation': 'deleteNetworkApplianceVlan',
        }
        resource = f'/networks/{networkId}/appliance/vlans/{vlanId}'

        return self._session.delete(metadata, resource)

    def getNetworkApplianceVpnSiteToSiteVpn(self, networkId: str):
        """
        **Return the site-to-site VPN settings of a network. Only valid for MX networks.**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-vpn-site-to-site-vpn
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'siteToSiteVpn'],
            'operation': 'getNetworkApplianceVpnSiteToSiteVpn',
        }
        resource = f'/networks/{networkId}/appliance/vpn/siteToSiteVpn'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceVpnSiteToSiteVpn(self, networkId: str, mode: str, **kwargs):
        """
        **Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn
        
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
            'tags': ['appliance', 'configure', 'vpn', 'siteToSiteVpn'],
            'operation': 'updateNetworkApplianceVpnSiteToSiteVpn',
        }
        resource = f'/networks/{networkId}/appliance/vpn/siteToSiteVpn'

        body_params = ['mode', 'hubs', 'subnets']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getNetworkApplianceWarmSpare(self, networkId: str):
        """
        **Return MX warm spare settings**
        https://developer.cisco.com/meraki/api-v1/#!get-network-appliance-warm-spare
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'getNetworkApplianceWarmSpare',
        }
        resource = f'/networks/{networkId}/appliance/warmSpare'

        return self._session.get(metadata, resource)

    def updateNetworkApplianceWarmSpare(self, networkId: str, enabled: bool, **kwargs):
        """
        **Update MX warm spare settings**
        https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-warm-spare
        
        - networkId (string)
        - enabled (boolean): Enable warm spare
        - spareSerial (string): Serial number of the warm spare appliance
        - uplinkMode (string): Uplink mode, either virtual or public
        - virtualIp1 (string): The WAN 1 shared IP
        - virtualIp2 (string): The WAN 2 shared IP
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'updateNetworkApplianceWarmSpare',
        }
        resource = f'/networks/{networkId}/appliance/warmSpare'

        body_params = ['enabled', 'spareSerial', 'uplinkMode', 'virtualIp1', 'virtualIp2']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def swapNetworkApplianceWarmSpare(self, networkId: str):
        """
        **Swap MX primary and warm spare appliances**
        https://developer.cisco.com/meraki/api-v1/#!swap-network-appliance-warm-spare
        
        - networkId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'warmSpare'],
            'operation': 'swapNetworkApplianceWarmSpare',
        }
        resource = f'/networks/{networkId}/appliance/warmSpare/swap'

        return self._session.post(metadata, resource)

    def getOrganizationApplianceSecurityEvents(self, organizationId: str, total_pages=1, direction='next', **kwargs):
        """
        **List the security events for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-events
        
        - organizationId (string)
        - total_pages (integer or string): total number of pages to retrieve, -1 or "all" for all pages
        - direction (string): direction to paginate, either "next" (default) or "prev" page
        - t0 (string): The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
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
            'operation': 'getOrganizationApplianceSecurityEvents',
        }
        resource = f'/organizations/{organizationId}/appliance/security/events'

        query_params = ['t0', 't1', 'timespan', 'perPage', 'startingAfter', 'endingBefore', 'sortOrder']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get_pages(metadata, resource, params, total_pages, direction)


    def getOrganizationApplianceSecurityIntrusion(self, organizationId: str):
        """
        **Returns all supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-security-intrusion
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'getOrganizationApplianceSecurityIntrusion',
        }
        resource = f'/organizations/{organizationId}/appliance/security/intrusion'

        return self._session.get(metadata, resource)

    def updateOrganizationApplianceSecurityIntrusion(self, organizationId: str, whitelistedRules: list):
        """
        **Sets supported intrusion settings for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-security-intrusion
        
        - organizationId (string)
        - whitelistedRules (array): Sets a list of specific SNORT® signatures to whitelist
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'security', 'intrusion'],
            'operation': 'updateOrganizationApplianceSecurityIntrusion',
        }
        resource = f'/organizations/{organizationId}/appliance/security/intrusion'

        body_params = ['whitelistedRules']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getOrganizationApplianceThirdPartyVPNPeers(self, organizationId: str):
        """
        **Return the third party VPN peers for an organization**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-third-party-v-p-n-peers
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'thirdPartyVPNPeers'],
            'operation': 'getOrganizationApplianceThirdPartyVPNPeers',
        }
        resource = f'/organizations/{organizationId}/appliance/thirdPartyVPNPeers'

        return self._session.get(metadata, resource)

    def updateOrganizationApplianceThirdPartyVPNPeers(self, organizationId: str, peers: list):
        """
        **Update the third party VPN peers for an organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-third-party-v-p-n-peers
        
        - organizationId (string)
        - peers (array): The list of VPN peers
        """

        kwargs = locals()

        metadata = {
            'tags': ['appliance', 'configure', 'thirdPartyVPNPeers'],
            'operation': 'updateOrganizationApplianceThirdPartyVPNPeers',
        }
        resource = f'/organizations/{organizationId}/appliance/thirdPartyVPNPeers'

        body_params = ['peers']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def getOrganizationApplianceVpnVpnFirewallRules(self, organizationId: str):
        """
        **Return the firewall rules for an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api-v1/#!get-organization-appliance-vpn-vpn-firewall-rules
        
        - organizationId (string)
        """

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'vpnFirewallRules'],
            'operation': 'getOrganizationApplianceVpnVpnFirewallRules',
        }
        resource = f'/organizations/{organizationId}/appliance/vpn/vpnFirewallRules'

        return self._session.get(metadata, resource)

    def updateOrganizationApplianceVpnVpnFirewallRules(self, organizationId: str, **kwargs):
        """
        **Update the firewall rules of an organization's site-to-site VPN**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-vpn-firewall-rules
        
        - organizationId (string)
        - rules (array): An ordered array of the firewall rules (not including the default rule)
        - syslogDefaultRule (boolean): Log the special default rule (boolean value - enable only if you've configured a syslog server) (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['appliance', 'configure', 'vpn', 'vpnFirewallRules'],
            'operation': 'updateOrganizationApplianceVpnVpnFirewallRules',
        }
        resource = f'/organizations/{organizationId}/appliance/vpn/vpnFirewallRules'

        body_params = ['rules', 'syslogDefaultRule']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

