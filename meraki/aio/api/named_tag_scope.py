class NamedTagScope(object):
    def __init__(self, session):
        super(NamedTagScope, self).__init__()
        self._session = session
    
    def getNetworkSmTargetGroups(self, networkId: str, **kwargs):
        """
        **List the target groups in this network**
        https://api.meraki.com/api_docs#list-the-target-groups-in-this-network
        
        - networkId (string)
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Named tag scope'],
            'operation': 'getNetworkSmTargetGroups',
        }
        resource = f'/networks/{networkId}/sm/targetGroups'

        query_params = ['withDetails']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def createNetworkSmTargetGroup(self, networkId: str, **kwargs):
        """
        **Add a target group**
        https://api.meraki.com/api_docs#add-a-target-group
        
        - networkId (string)
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Named tag scope'],
            'operation': 'createNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups'

        body_params = ['name', 'scope']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Return a target group**
        https://api.meraki.com/api_docs#return-a-target-group
        
        - networkId (string)
        - targetGroupId (string)
        - withDetails (boolean): Boolean indicating if the the ids of the devices or users scoped by the target group should be included in the response
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Named tag scope'],
            'operation': 'getNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        query_params = ['withDetails']
        params = {k: v for (k, v) in kwargs.items() if k in query_params}

        return self._session.get(metadata, resource, params)

    def updateNetworkSmTargetGroup(self, networkId: str, targetGroupId: str, **kwargs):
        """
        **Update a target group**
        https://api.meraki.com/api_docs#update-a-target-group
        
        - networkId (string)
        - targetGroupId (string)
        - name (string): The name of this target group
        - scope (string): The scope and tag options of the target group. Comma separated values beginning with one of withAny, withAll, withoutAny, withoutAll, all, none, followed by tags. Default to none if empty.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Named tag scope'],
            'operation': 'updateNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        body_params = ['name', 'scope']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)

    def deleteNetworkSmTargetGroup(self, networkId: str, targetGroupId: str):
        """
        **Delete a target group from a network**
        https://api.meraki.com/api_docs#delete-a-target-group-from-a-network
        
        - networkId (string)
        - targetGroupId (string)
        """

        metadata = {
            'tags': ['Named tag scope'],
            'operation': 'deleteNetworkSmTargetGroup',
        }
        resource = f'/networks/{networkId}/sm/targetGroups/{targetGroupId}'

        return self._session.delete(metadata, resource)

