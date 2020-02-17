class CellularUplinkConfigurations(object):
    def __init__(self, session):
        super(CellularUplinkConfigurations, self).__init__()
        self._session = session

    def getCellularUplinkConfigurations(self, networkId: str, serial: str):
        """
        **Return the cellular uplink configurations for a device.**
        https://api.meraki.com/api_docs

        - networkId (string)
        - serial (string)
        """

        metadata = {
            'tags': ['Cellular Uplink Configurations'],
            'operation': 'getCellularUplinkConfigurations',
        }
        resource = f'/networks/{networkId}/devices/{serial}/uplink/cellular'

        return self._session.get(metadata, resource)

    def createCellularUplinkConfigurations(self, networkId: str, serial: str, **kwargs):
        """
        **Create an uplink configuration for a device**
        https://api.meraki.com/api_docs

        - networkId (string)
        - serial (string)
        - apn (string): Access Point Name (APN) to send to carrier (optional)
        - enabled (boolean): Whether this uplink is enabled (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Cellular Uplink Configurations'],
            'operation': 'createCellularUplinkConfigurations',
        }
        resource = f'/networks/{networkId}/devices/{serial}/uplink/cellular'

        body_params = ['apn', 'enabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.post(metadata, resource, payload)

    def getCellularUplinkConfiguration(self, networkId: str, serial: str, id: str):
        """
        **Return the cellular uplink configuration.**
        https://api.meraki.com/api_docs

        - networkId (string)
        - serial (string)
        - id (string): id for the cellular uplink configuration
        """

        metadata = {
            'tags': ['Cellular Uplink Configurations'],
            'operation': 'getCellularUplinkConfiguration',
        }
        resource = f'/networks/{networkId}/devices/{serial}/uplink/cellular/{id}'

        return self._session.get(metadata, resource)

    def updateCellularUplinkConfiguration(self, networkId: str, serial: str, id: str, **kwargs):
        """
        **Update cellular uplink configuration**
        https://api.meraki.com/api_docs

        - networkId (string)
        - serial (string)
        - id (string): id for the cellular uplink configuration
        - apn (string): Access Point Name (APN) to send to carrier (optional)
        - enabled (boolean): Whether this uplink is enabled (optional)
        """

        kwargs.update(locals())

        metadata = {
            'tags': ['Cellular Uplink Configurations'],
            'operation': 'updateCellularUplinkConfiguration',
        }
        resource = f'/networks/{networkId}/devices/{serial}/uplink/cellular/{id}'

        body_params = ['apn', 'enabled']
        payload = {k: v for (k, v) in kwargs.items() if k in body_params}

        return self._session.put(metadata, resource, payload)
