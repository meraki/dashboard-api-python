class MXVLANPorts(object):
    def __init__(self, session):
        super(MXVLANPorts, self).__init__()
        self._session = session
    
    def getNetworkAppliancePorts(self, networkId: str):
        """
        **List per-port VLAN settings for all ports of a MX.**
        https://api.meraki.com/api_docs#list-per-port-vlan-settings-for-all-ports-of-a-mx
        
        - networkId (string)
        """

        metadata = {
            'tags': ['MX VLAN ports'],
            'operation': 'getNetworkAppliancePorts',
        }
        resource = f'/networks/{networkId}/appliancePorts'

        return self._session.get(metadata, resource)

    def getNetworkAppliancePort(self, networkId: str, appliancePortId: str):
        """
        **Return per-port VLAN settings for a single MX port.**
        https://api.meraki.com/api_docs#return-per-port-vlan-settings-for-a-single-mx-port
        
        - networkId (string)
        - appliancePortId (string)
        """

        metadata = {
            'tags': ['MX VLAN ports'],
            'operation': 'getNetworkAppliancePort',
        }
        resource = f'/networks/{networkId}/appliancePorts/{appliancePortId}'

        return self._session.get(metadata, resource)

    def updateNetworkAppliancePort(self, networkId: str, appliancePortId: str, **kwargs):
        """
        **Update the per-port VLAN settings for a single MX port.**
        https://api.meraki.com/api_docs#update-the-per-port-vlan-settings-for-a-single-mx-port
        
        - networkId (string)
        - appliancePortId (string)
        - enabled (boolean): The status of the port
        - dropUntaggedTraffic (boolean): Trunk port can Drop all Untagged traffic. When true, no VLAN is required. Access ports cannot have dropUntaggedTraffic set to true.
        - type (string): The type of the port: 'access' or 'trunk'.
        - vlan (integer): Native VLAN when the port is in Trunk mode. Access VLAN when the port is in Access mode.
        - allowedVlans (string): Comma-delimited list of the VLAN ID's allowed on the port, or 'all' to permit all VLAN's on the port.
        - accessPolicy (string): The name of the policy. Only applicable to Access ports. Valid values are: 'open', '8021x-radius', 'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting the per port authentication feature. Otherwise, 'open' is the only valid value and 'open' is the default value if the field is missing.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['MX VLAN ports'],
            'operation': 'updateNetworkAppliancePort',
        }
        resource = f'/networks/{networkId}/appliancePorts/{appliancePortId}'

        body_params = ['enabled', 'dropUntaggedTraffic', 'type', 'vlan', 'allowedVlans', 'accessPolicy']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

