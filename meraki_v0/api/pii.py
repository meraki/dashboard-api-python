class PII(object):
    def __init__(self, session):
        super(PII, self).__init__()
        self._session = session
    
    def getNetworkPiiPiiKeys(self, networkId: str, **kwargs):
        """
        **List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.**
        https://developer.cisco.com/meraki/api/#!get-network-pii-pii-keys
        
        - networkId (string)
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['PII'],
            'operation': 'getNetworkPiiPiiKeys',
        }
        resource = f'/networks/{networkId}/pii/piiKeys'

        query_params = ['username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkPiiRequests(self, networkId: str):
        """
        **List the PII requests for this network or organization**
        https://developer.cisco.com/meraki/api/#!get-network-pii-requests
        
        - networkId (string)
        """

        metadata = {
            'tags': ['PII'],
            'operation': 'getNetworkPiiRequests',
        }
        resource = f'/networks/{networkId}/pii/requests'

        return self._session.get(metadata, resource)

    def createNetworkPiiRequest(self, networkId: str, **kwargs):
        """
        **Submit a new delete or restrict processing PII request**
        https://developer.cisco.com/meraki/api/#!create-network-pii-request
        
        - networkId (string)
        - type (string): One of "delete" or "restrict processing"
        - datasets (array): The datasets related to the provided key that should be deleted. Only applies to "delete" requests. The value "all" will be expanded to all datasets applicable to this type. The datasets by applicable to each type are: mac (usage, events, traffic), email (users, loginAttempts), username (users, loginAttempts), bluetoothMac (client, connectivity), smDeviceId (device), smUserId (user)
        - username (string): The username of a network log in. Only applies to "delete" requests.
        - email (string): The email of a network user account. Only applies to "delete" requests.
        - mac (string): The MAC of a network client device. Applies to both "restrict processing" and "delete" requests.
        - smDeviceId (string): The sm_device_id of a Systems Manager device. The only way to "restrict processing" or "delete" a Systems Manager device. Must include "device" in the dataset for a "delete" request to destroy the device.
        - smUserId (string): The sm_user_id of a Systems Manager user. The only way to "restrict processing" or "delete" a Systems Manager user. Must include "user" in the dataset for a "delete" request to destroy the user.
        """

        kwargs.update(locals())

        if 'type' in kwargs:
            options = ['delete', 'restrict processing']
            assert kwargs['type'] in options, f'''"type" cannot be "{kwargs['type']}", & must be set to one of: {options}'''

        metadata = {
            'tags': ['PII'],
            'operation': 'createNetworkPiiRequest',
        }
        resource = f'/networks/{networkId}/pii/requests'

        body_params = ['type', 'datasets', 'username', 'email', 'mac', 'smDeviceId', 'smUserId']
        payload = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in body_params}

        return self._session.post(metadata, resource, payload)

    def getNetworkPiiRequest(self, networkId: str, requestId: str):
        """
        **Return a PII request**
        https://developer.cisco.com/meraki/api/#!get-network-pii-request
        
        - networkId (string)
        - requestId (string)
        """

        metadata = {
            'tags': ['PII'],
            'operation': 'getNetworkPiiRequest',
        }
        resource = f'/networks/{networkId}/pii/requests/{requestId}'

        return self._session.get(metadata, resource)

    def deleteNetworkPiiRequest(self, networkId: str, requestId: str):
        """
        **Delete a restrict processing PII request**
        https://developer.cisco.com/meraki/api/#!delete-network-pii-request
        
        - networkId (string)
        - requestId (string)
        """

        metadata = {
            'tags': ['PII'],
            'operation': 'deleteNetworkPiiRequest',
        }
        resource = f'/networks/{networkId}/pii/requests/{requestId}'

        return self._session.delete(metadata, resource)

    def getNetworkPiiSmDevicesForKey(self, networkId: str, **kwargs):
        """
        **Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.**
        https://developer.cisco.com/meraki/api/#!get-network-pii-sm-devices-for-key
        
        - networkId (string)
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['PII'],
            'operation': 'getNetworkPiiSmDevicesForKey',
        }
        resource = f'/networks/{networkId}/pii/smDevicesForKey'

        query_params = ['username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

    def getNetworkPiiSmOwnersForKey(self, networkId: str, **kwargs):
        """
        **Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.**
        https://developer.cisco.com/meraki/api/#!get-network-pii-sm-owners-for-key
        
        - networkId (string)
        - username (string): The username of a Systems Manager user
        - email (string): The email of a network user account or a Systems Manager device
        - mac (string): The MAC of a network client device or a Systems Manager device
        - serial (string): The serial of a Systems Manager device
        - imei (string): The IMEI of a Systems Manager device
        - bluetoothMac (string): The MAC of a Bluetooth client
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['PII'],
            'operation': 'getNetworkPiiSmOwnersForKey',
        }
        resource = f'/networks/{networkId}/pii/smOwnersForKey'

        query_params = ['username', 'email', 'mac', 'serial', 'imei', 'bluetoothMac']
        params = {k.strip(): v for (k, v) in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)

