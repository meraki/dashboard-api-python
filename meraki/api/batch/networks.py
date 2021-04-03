class ActionBatchNetworks(object):
    def __init__(self):
        super(ActionBatchNetworks, self).__init__()
        


    def updateNetwork(self, networkId: str, **kwargs):
        """
        **Update a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network

        - networkId (string): (required)
        - name (string): The name of the network
        - timeZone (string): The timezone of the network. For a list of allowed timezones, please see the 'TZ' column in the table in <a target='_blank' href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones'>this article.</a>
        - tags (array): A list of tags to be applied to the network
        - enrollmentString (string): A unique identifier which can be used for device enrollment or easy access through the Meraki SM Registration page or the Self Service Portal. Please note that changing this field may cause existing bookmarks to break.
        - notes (string): Add any notes or additional information about this network here.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'updateNetwork'
        }
        resource = f'/networks/{networkId}'

        body_params = ['name', 'timeZone', 'tags', 'enrollmentString', 'notes', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetwork(self, networkId: str):
        """
        **Delete a network**
        https://developer.cisco.com/meraki/api-v1/#!delete-network

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'deleteNetwork'
        }
        resource = f'/networks/{networkId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        





    def bindNetwork(self, networkId: str, configTemplateId: str, **kwargs):
        """
        **Bind a network to a template.**
        https://developer.cisco.com/meraki/api-v1/#!bind-network

        - networkId (string): (required)
        - configTemplateId (string): The ID of the template to which the network should be bound.
        - autoBind (boolean): Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model. Defaults to false if left unspecified. This option only affects switch networks and switch templates. Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'bindNetwork'
        }
        resource = f'/networks/{networkId}/bind'

        body_params = ['configTemplateId', 'autoBind', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def provisionNetworkClients(self, networkId: str, clients: list, devicePolicy: str, **kwargs):
        """
        **Provisions a client with a name and policy**
        https://developer.cisco.com/meraki/api-v1/#!provision-network-clients

        - networkId (string): (required)
        - clients (array): The array of clients to provision
        - devicePolicy (string): The policy to apply to the specified client. Can be 'Group policy', 'Allowed', 'Blocked', 'Per connection' or 'Normal'. Required.
        - groupPolicyId (string): The ID of the desired group policy to apply to the client. Required if 'devicePolicy' is set to "Group policy". Otherwise this is ignored.
        - policiesBySecurityAppliance (object): An object, describing what the policy-connection association is for the security appliance. (Only relevant if the security appliance is actually within the network)
        - policiesBySsid (object): An object, describing the policy-connection associations for each active SSID within the network. Keys should be the number of enabled SSIDs, mapping to an object describing the client's policy
        """

        kwargs.update(locals())

        if 'devicePolicy' in kwargs:
            options = ['Group policy', 'Allowed', 'Blocked', 'Per connection', 'Normal']
            assert kwargs['devicePolicy'] in options, f'''"devicePolicy" cannot be "{kwargs['devicePolicy']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'clients'],
            'operation': 'provisionNetworkClients'
        }
        resource = f'/networks/{networkId}/clients/provision'

        body_params = ['clients', 'devicePolicy', 'groupPolicyId', 'policiesBySecurityAppliance', 'policiesBySsid', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def claimNetworkDevices(self, networkId: str, serials: list):
        """
        **Claim devices into a network. (Note: for recently claimed devices, it may take a few minutes for API requsts against that device to succeed)**
        https://developer.cisco.com/meraki/api-v1/#!claim-network-devices

        - networkId (string): (required)
        - serials (array): A list of serials of devices to claim
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'devices'],
            'operation': 'claimNetworkDevices'
        }
        resource = f'/networks/{networkId}/devices/claim'

        body_params = ['serials', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def removeNetworkDevices(self, networkId: str, serial: str):
        """
        **Remove a single device**
        https://developer.cisco.com/meraki/api-v1/#!remove-network-devices

        - networkId (string): (required)
        - serial (string): The serial of a device
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'devices'],
            'operation': 'removeNetworkDevices'
        }
        resource = f'/networks/{networkId}/devices/remove'

        body_params = ['serial', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkFirmwareUpgrades(self, networkId: str, **kwargs):
        """
        **Update firmware upgrade information for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades

        - networkId (string): (required)
        - upgradeWindow (object): Upgrade window for devices in network
        - timezone (string): The timezone for the network
        - products (object): Contains information about the network to update
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'firmwareUpgrades'],
            'operation': 'updateNetworkFirmwareUpgrades'
        }
        resource = f'/networks/{networkId}/firmwareUpgrades'

        body_params = ['upgradeWindow', 'timezone', 'products', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkFirmwareUpgradesRollback(self, networkId: str, reasons: list, **kwargs):
        """
        **Rollback a Firmware Upgrade For A Network**
        https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-rollback

        - networkId (string): (required)
        - reasons (array): Reasons for the rollback
        - product (string): Product type to rollback (if the network is a combined network)
        - time (string): Scheduled time for the rollback
        - toVersion (object): Version to downgrade to (if the network has firmware flexibility)
        """

        kwargs.update(locals())

        if 'product' in kwargs:
            options = ['wireless', 'switch', 'appliance', 'camera', 'vmxHost', 'cellularGateway']
            assert kwargs['product'] in options, f'''"product" cannot be "{kwargs['product']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'firmwareUpgrades', 'rollbacks'],
            'operation': 'createNetworkFirmwareUpgradesRollback'
        }
        resource = f'/networks/{networkId}/firmwareUpgrades/rollbacks'

        body_params = ['product', 'time', 'reasons', 'toVersion', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkFloorPlan(self, networkId: str, floorPlanId: str, **kwargs):
        """
        **Update a floor plan's geolocation and other meta data**
        https://developer.cisco.com/meraki/api-v1/#!update-network-floor-plan

        - networkId (string): (required)
        - floorPlanId (string): (required)
        - name (string): The name of your floor plan.
        - center (object): The longitude and latitude of the center of your floor plan. If you want to change the geolocation data of your floor plan, either the 'center' or two adjacent corners (e.g. 'topLeftCorner' and 'bottomLeftCorner') must be specified. If 'center' is specified, the floor plan is placed over that point with no rotation. If two adjacent corners are specified, the floor plan is rotated to line up with the two specified points. The aspect ratio of the floor plan's image is preserved regardless of which corners/center are specified. (This means if that more than two corners are specified, only two corners may be used to preserve the floor plan's aspect ratio.). No two points can have the same latitude, longitude pair.
        - bottomLeftCorner (object): The longitude and latitude of the bottom left corner of your floor plan.
        - bottomRightCorner (object): The longitude and latitude of the bottom right corner of your floor plan.
        - topLeftCorner (object): The longitude and latitude of the top left corner of your floor plan.
        - topRightCorner (object): The longitude and latitude of the top right corner of your floor plan.
        - imageContents (string): The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields ('center, 'topLeftCorner', etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'updateNetworkFloorPlan'
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        body_params = ['name', 'center', 'bottomLeftCorner', 'bottomRightCorner', 'topLeftCorner', 'topRightCorner', 'imageContents', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkFloorPlan(self, networkId: str, floorPlanId: str):
        """
        **Destroy a floor plan**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-floor-plan

        - networkId (string): (required)
        - floorPlanId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'floorPlans'],
            'operation': 'deleteNetworkFloorPlan'
        }
        resource = f'/networks/{networkId}/floorPlans/{floorPlanId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        





    def createNetworkGroupPolicy(self, networkId: str, name: str, **kwargs):
        """
        **Create a group policy**
        https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy

        - networkId (string): (required)
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
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'createNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies'

        body_params = ['name', 'scheduling', 'bandwidth', 'firewallAndTrafficShaping', 'contentFiltering', 'splashAuthSettings', 'vlanTagging', 'bonjourForwarding', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkGroupPolicy(self, networkId: str, groupPolicyId: str, **kwargs):
        """
        **Update a group policy**
        https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy

        - networkId (string): (required)
        - groupPolicyId (string): (required)
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
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'updateNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        body_params = ['name', 'scheduling', 'bandwidth', 'firewallAndTrafficShaping', 'contentFiltering', 'splashAuthSettings', 'vlanTagging', 'bonjourForwarding', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkGroupPolicy(self, networkId: str, groupPolicyId: str):
        """
        **Delete a group policy**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy

        - networkId (string): (required)
        - groupPolicyId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'groupPolicies'],
            'operation': 'deleteNetworkGroupPolicy'
        }
        resource = f'/networks/{networkId}/groupPolicies/{groupPolicyId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        





    def createNetworkMerakiAuthUser(self, networkId: str, email: str, name: str, password: str, authorizations: list, **kwargs):
        """
        **Authorize a user configured with Meraki Authentication for a network (currently supports 802.1X, splash guest, and client VPN users, and currently, organizations have a 50,000 user cap)**
        https://developer.cisco.com/meraki/api-v1/#!create-network-meraki-auth-user

        - networkId (string): (required)
        - email (string): Email address of the user
        - name (string): Name of the user
        - password (string): The password for this user account
        - authorizations (array): Authorization zones and expiration dates for the user.
        - accountType (string): Authorization type for user. Can be 'Guest' or '802.1X' for wireless networks, or 'Client VPN' for wired networks. Defaults to '802.1X'.
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        """

        kwargs.update(locals())

        if 'accountType' in kwargs:
            options = ['Guest', '802.1X', 'Client VPN']
            assert kwargs['accountType'] in options, f'''"accountType" cannot be "{kwargs['accountType']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'createNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers'

        body_params = ['email', 'name', 'password', 'accountType', 'emailPasswordToUser', 'authorizations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def deleteNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str):
        """
        **Deauthorize a user**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-meraki-auth-user

        - networkId (string): (required)
        - merakiAuthUserId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'deleteNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        





    def updateNetworkMerakiAuthUser(self, networkId: str, merakiAuthUserId: str, **kwargs):
        """
        **Update a user configured with Meraki Authentication (currently, 802.1X RADIUS, splash guest, and client VPN users can be updated)**
        https://developer.cisco.com/meraki/api-v1/#!update-network-meraki-auth-user

        - networkId (string): (required)
        - merakiAuthUserId (string): (required)
        - name (string): Name of the user
        - password (string): The password for this user account
        - emailPasswordToUser (boolean): Whether or not Meraki should email the password to user. Default is false.
        - authorizations (array): Authorization zones and expiration dates for the user.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'merakiAuthUsers'],
            'operation': 'updateNetworkMerakiAuthUser'
        }
        resource = f'/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}'

        body_params = ['name', 'password', 'emailPasswordToUser', 'authorizations', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def createNetworkMqttBroker(self, networkId: str, name: str, host: str, port: int):
        """
        **Add an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!create-network-mqtt-broker

        - networkId (string): (required)
        - name (string): Name of the MQTT broker
        - host (string): Host name/IP address where MQTT broker runs
        - port (integer): Host port though which MQTT broker can be reached
        """

        kwargs = locals()

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'createNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers'

        body_params = ['name', 'host', 'port', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        





    def updateNetworkMqttBroker(self, networkId: str, mqttBrokerId: str, **kwargs):
        """
        **Update an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!update-network-mqtt-broker

        - networkId (string): (required)
        - mqttBrokerId (string): (required)
        - name (string): Name of the mqtt config
        - host (string): Host name where mqtt broker runs
        - port (integer): Host port though which mqtt broker can be reached
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'updateNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers/{mqttBrokerId}'

        body_params = ['name', 'host', 'port', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def deleteNetworkMqttBroker(self, networkId: str, mqttBrokerId: str):
        """
        **Delete an MQTT broker**
        https://developer.cisco.com/meraki/api-v1/#!delete-network-mqtt-broker

        - networkId (string): (required)
        - mqttBrokerId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure', 'mqttBrokers'],
            'operation': 'deleteNetworkMqttBroker'
        }
        resource = f'/networks/{networkId}/mqttBrokers/{mqttBrokerId}'

        action = {
            "resource": resource,
            "operation": "destroy",
            "body": payload
        }
        return action
        





    def updateNetworkSettings(self, networkId: str, **kwargs):
        """
        **Update the settings for a network**
        https://developer.cisco.com/meraki/api-v1/#!update-network-settings

        - networkId (string): (required)
        - localStatusPageEnabled (boolean): Enables / disables the local device status pages (<a target='_blank' href='http://my.meraki.com/'>my.meraki.com, </a><a target='_blank' href='http://ap.meraki.com/'>ap.meraki.com, </a><a target='_blank' href='http://switch.meraki.com/'>switch.meraki.com, </a><a target='_blank' href='http://wired.meraki.com/'>wired.meraki.com</a>). Optional (defaults to false)
        - remoteStatusPageEnabled (boolean): Enables / disables access to the device status page (<a target='_blank'>http://[device's LAN IP])</a>. Optional. Can only be set if localStatusPageEnabled is set to true
        - secureConnect (object): A hash of SecureConnect options applied to the Network.
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['networks', 'configure', 'settings'],
            'operation': 'updateNetworkSettings'
        }
        resource = f'/networks/{networkId}/settings'

        body_params = ['localStatusPageEnabled', 'remoteStatusPageEnabled', 'secureConnect', ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload
        }
        return action
        





    def splitNetwork(self, networkId: str):
        """
        **Split a combined network into individual networks for each type of device**
        https://developer.cisco.com/meraki/api-v1/#!split-network

        - networkId (string): (required)
        """

        metadata = {
            'tags': ['networks', 'configure'],
            'operation': 'splitNetwork'
        }
        resource = f'/networks/{networkId}/split'

        action = {
            "resource": resource,
            "operation": "create",
            "body": payload
        }
        return action
        



