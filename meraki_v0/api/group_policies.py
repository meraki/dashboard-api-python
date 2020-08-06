class GroupPolicies(object):
    def __init__(self, session):
        super(GroupPolicies, self).__init__()
        self._session = session
    
    def getNetworkGroupPolicies(self, networkId: str):
        """
        **List the group policies in a network**
        https://developer.cisco.com/meraki/api/#!get-network-group-policies
        
        - networkId (string)
        """

        metadata = {
            'tags': ['Group policies'],
            'operation': 'getNetworkGroupPolicies',
        }
        resource = f'/networks/{networkId}/groupPolicies'

        return self._session.get(metadata, resource)

    def createNetworkGroupPolicy(self, networkId: str, name: str, **kwargs):
        """
        **Create a group policy**
        https://developer.cisco.com/meraki/api/#!create-network-group-policy
        
        - networkId (string)
        - name (string): The name for your group policy. Required.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
        """

        kwargs.update(locals())

        if 'splashAuthSettings' in kwargs:
            options = ['network default', 'bypass']
            assert kwargs['splashAuthSettings'] in options, f'''"splashAuthSettings" cannot be "{kwargs['splashAuthSettings']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Group policies'],
            'operation': 'createNetworkGroupPolicy',
        }
        resource = f'/networks/{networkId}/groupPolicies'

        body_params = ['name', 'scheduling', 'bandwidth', 'firewallAndTrafficShaping', 'contentFiltering', 'splashAuthSettings', 'vlanTagging', 'bonjourForwarding']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkGroupPolicy(self, networkId: str, groupPolicyId: str):
        """
        **Display a group policy**
        https://developer.cisco.com/meraki/api/#!get-network-group-policy
        
        - networkId (string)
        - groupPolicyId (string)
        """

        metadata = {
            'tags': ['Group policies'],
            'operation': 'getNetworkGroupPolicy',
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        return self._session.get(metadata, resource)

    def updateNetworkGroupPolicy(self, networkId: str, groupPolicyId: str, **kwargs):
        """
        **Update a group policy**
        https://developer.cisco.com/meraki/api/#!update-network-group-policy
        
        - networkId (string)
        - groupPolicyId (string)
        - name (string): The name for your group policy.
        - scheduling (object):     The schedule for the group policy. Schedules are applied to days of the week.

        - bandwidth (object):     The bandwidth settings for clients bound to your group policy.

        - firewallAndTrafficShaping (object):     The firewall and traffic shaping rules and settings for your policy.

        - contentFiltering (object): The content filtering settings for your group policy
        - splashAuthSettings (string): Whether clients bound to your policy will bypass splash authorization or behave according to the network's rules. Can be one of 'network default' or 'bypass'. Only available if your network has a wireless configuration.
        - vlanTagging (object): The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration.
        - bonjourForwarding (object): The Bonjour settings for your group policy. Only valid if your network has a wireless configuration.
        """

        kwargs.update(locals())

        if 'splashAuthSettings' in kwargs:
            options = ['network default', 'bypass']
            assert kwargs['splashAuthSettings'] in options, f'''"splashAuthSettings" cannot be "{kwargs['splashAuthSettings']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['Group policies'],
            'operation': 'updateNetworkGroupPolicy',
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        body_params = ['name', 'scheduling', 'bandwidth', 'firewallAndTrafficShaping', 'contentFiltering', 'splashAuthSettings', 'vlanTagging', 'bonjourForwarding']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkGroupPolicy(self, networkId: str, groupPolicyId: str):
        """
        **Delete a group policy**
        https://developer.cisco.com/meraki/api/#!delete-network-group-policy
        
        - networkId (string)
        - groupPolicyId (string)
        """

        metadata = {
            'tags': ['Group policies'],
            'operation': 'deleteNetworkGroupPolicy',
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        return self._session.delete(metadata, resource)

