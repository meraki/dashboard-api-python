class FirewalledServices(object):
    def __init__(self, session):
        super(FirewalledServices, self).__init__()
        self._session = session
    
    def getNetworkFirewalledServices(self, networkId: str):
        """
        **List the appliance services and their accessibility rules**
        https://developer.cisco.com/meraki/api/#!get-network-firewalled-services
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Firewalled services'],
            'operation': 'getNetworkFirewalledServices',
        }
        resource = f'/networks/{networkId}/firewalledServices'

        return self._session.get(metadata, resource)

    def getNetworkFirewalledService(self, networkId: str, service: str):
        """
        **Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')**
        https://developer.cisco.com/meraki/api/#!get-network-firewalled-service
        
        - networkId (string)
        - service (string)
        """

        metadata = {
            'tags': ['Firewalled services'],
            'operation': 'getNetworkFirewalledService',
        }
        resource = f'/networks/{networkId}/firewalledServices/{service}'

        return self._session.get(metadata, resource)

    def updateNetworkFirewalledService(self, networkId: str, service: str, access: str, **kwargs):
        """
        **Updates the accessibility settings for the given service ('ICMP', 'web', or 'SNMP')**
        https://developer.cisco.com/meraki/api/#!update-network-firewalled-service
        
        - networkId (string)
        - service (string)
        - access (string): A string indicating the rule for which IPs are allowed to use the specified service. Acceptable values are "blocked" (no remote IPs can access the service), "restricted" (only whitelisted IPs can access the service), and "unrestriced" (any remote IP can access the service). This field is required
        - allowedIps (array): An array of whitelisted IPs that can access the service. This field is required if "access" is set to "restricted". Otherwise this field is ignored
        """

        kwargs.update(locals())

        if 'access' in kwargs:
            options = ['blocked', 'restricted', 'unrestricted']
            assert kwargs['access'] in options, f'''"access" cannot be "{kwargs['access']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Firewalled services'],
            'operation': 'updateNetworkFirewalledService',
        }
        resource = f'/networks/{networkId}/firewalledServices/{service}'

        body_params = ['access', 'allowedIps']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

