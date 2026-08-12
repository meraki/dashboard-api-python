import urllib


class ActionBatchNac:
    def __init__(self):
        super().__init__()

    def createOrganizationNacCertificatesAuthoritiesCrl(self, organizationId: str, **kwargs):
        """
        **Upload a CRL through Certificate Validation**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-authorities-crl

        - organizationId (string): Organization ID
        - trustedCertificateId (string): ID of the CRL issuer
        - crlBody (string): CRL content in PEM format or base64-encoded DER. Required when the access-manager-crl-ui flag is enabled.
        - fileName (string): Original filename supplied by the browser
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls"

        body_params = [
            "trustedCertificateId",
            "crlBody",
            "fileName",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "action",
            "body": payload,
        }
        return action

    def retrieveOrganizationNacCertificatesAuthoritiesCrls(self, organizationId: str, trustedCertificateId: str, **kwargs):
        """
        **Retrieve a CRL for an existing CA through Certificate Validation**
        https://developer.cisco.com/meraki/api-v1/#!retrieve-organization-nac-certificates-authorities-crls

        - organizationId (string): Organization ID
        - trustedCertificateId (string): ID of the CRL issuer
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls/retrieve"

        body_params = [
            "trustedCertificateId",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "action",
            "body": payload,
        }
        return action

    def deleteOrganizationNacCertificatesAuthoritiesCrl(self, organizationId: str, crlId: str):
        """
        **Deletes a CRL. Deleting a base CRL also deletes deltas associated with that base CRL.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-nac-certificates-authorities-crl

        - organizationId (string): Organization ID
        - crlId (string): Crl ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        crlId = urllib.parse.quote(crlId, safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/authorities/crls/{crlId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationNacCertificatesImport(self, organizationId: str, contents: str, **kwargs):
        """
        **Import certificate for this organization or validate without persisting**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-certificates-import

        - organizationId (string): Organization ID
        - contents (string): Certificate content in valid PEM format
        - dryRun (boolean): If true, validates the certificate without persisting it
        - profile (object): Profile object containing certificate config fields
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/import"

        body_params = [
            "contents",
            "dryRun",
            "profile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationNacCertificate(self, organizationId: str, certificateId: str, profile: dict, **kwargs):
        """
        **Update certificate configuration by certificateId for this organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-certificate

        - organizationId (string): Organization ID
        - certificateId (string): Certificate ID
        - profile (object): Profile object containing certificate config fields
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        certificateId = urllib.parse.quote(certificateId, safe="")
        resource = f"/organizations/{organizationId}/nac/certificates/{certificateId}"

        body_params = [
            "profile",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "action",
            "body": payload,
        }
        return action

    def bulkOrganizationNacClientsDelete(self, organizationId: str, clientIds: list, **kwargs):
        """
        **Delete existing client(s) for the organization**
        https://developer.cisco.com/meraki/api-v1/#!bulk-organization-nac-clients-delete

        - organizationId (string): Organization ID
        - clientIds (array): List of ids for specific client retrieval
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/bulkDelete"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationNacClientsBulkEdit(self, organizationId: str, clientIds: list, **kwargs):
        """
        **Bulk Update of existing clients for the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-clients-bulk-edit

        - organizationId (string): Organization ID
        - clientIds (array): List of clients ids to apply the bulk edit operation on.
        - description (string): User provided description to be applied on the list of clients provided
        - ipsk (string): Per-client Identity Pre-Shared Key (iPSK) passphrase to apply to all selected clients (8-63 printable ASCII characters). Only accepted when the access-manager-ipsk-per-client feature flag is enabled; omit when the flag is disabled. Send an empty string to clear the passphrase. Omit the field to leave existing passphrases unchanged.
        - groups (object): Client group information to be applied on the list of clients provided
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/bulkEdit"

        body_params = [
            "clientIds",
            "description",
            "ipsk",
            "groups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "edit",
            "body": payload,
        }
        return action

    def createOrganizationNacClientsBulkUpload(
        self, organizationId: str, contents: str, updateClients: bool, createClientGroups: bool, **kwargs
    ):
        """
        **Bulk upload of clients, client groups and their associations for the organization. CSV columns: MAC Address, Endpoint device group, Description, and an optional IPSK column for per-client Identity Pre-Shared Key (iPSK) passphrases. The IPSK column is only accepted when the access-manager-ipsk-per-client feature flag is enabled; omit the column when the flag is disabled. When the IPSK column is present, provide a valid passphrase (8-63 printable ASCII characters) per row to set or update it; leave the cell blank to skip setting a passphrase for that row. The response echoes errored rows in Base64 CSV format for troubleshooting; IPSK column values are never returned in the response.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-clients-bulk-upload

        - organizationId (string): Organization ID
        - contents (string): CSV file content in Base64 encoded string format. Example CSV includes headers MAC Address, Endpoint device group, Description, IPSK.
        - updateClients (boolean): The updateClients indicates whether existing clients must be updated with new data from the CSV
        - createClientGroups (boolean): The createClientGroups indicates whether new client groups must be created or not
        """

        kwargs = locals()

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/bulkUpload"

        body_params = [
            "contents",
            "updateClients",
            "createClientGroups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def createOrganizationNacClientsGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Create a client group for the organization**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-nac-clients-group

        - organizationId (string): Organization ID
        - name (string): The name of the group for access control model
        - description (string): User provided description of the group
        - members (array): List of client members associated with the group
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups"

        body_params = [
            "name",
            "description",
            "members",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationNacClientsGroup(self, organizationId: str, groupId: str, **kwargs):
        """
        **Update an existing client group for the organization with bulk member operations**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-clients-group

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        - name (string): The name of the group for access control model
        - description (string): User provided description of the group
        - members (object): Bulk member operations with addList/removeList arrays
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        groupId = urllib.parse.quote(groupId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups/{groupId}"

        body_params = [
            "name",
            "description",
            "members",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationNacClientsGroup(self, organizationId: str, groupId: str):
        """
        **Delete an existing client group for the organization**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-nac-clients-group

        - organizationId (string): Organization ID
        - groupId (string): Group ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        groupId = urllib.parse.quote(groupId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/groups/{groupId}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def updateOrganizationNacClient(self, organizationId: str, clientId: str, mac: str, **kwargs):
        """
        **Update an existing client for the organization**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-nac-client

        - organizationId (string): Organization ID
        - clientId (string): Client ID
        - mac (string): The MAC address of the client
        - type (string): Type describes if the network client belongs to an individual user or corporate
        - owner (string): The username of the owner of the client
        - description (string): User provided description for the client
        - uuid (string): Universally unique identifier of the client
        - userDetails (array): List of users of this network client
        - oui (object): Organizationally unique identifier assigned to a vendor of the client
        - ipsk (string): Per-client Identity Pre-Shared Key (iPSK) passphrase (8-63 printable ASCII characters). Only accepted when the access-manager-ipsk-per-client feature flag is enabled; omit when the flag is disabled. Send an empty string to clear the passphrase. Omit the field to leave any existing passphrase unchanged.
        - groups (object): Client group membership changes
        """

        kwargs.update(locals())

        if "type" in kwargs:
            options = ["BYOD", "corporate"]
            assert kwargs["type"] in options, f'''"type" cannot be "{kwargs["type"]}", & must be set to one of: {options}'''

        organizationId = urllib.parse.quote(organizationId, safe="")
        clientId = urllib.parse.quote(clientId, safe="")
        resource = f"/organizations/{organizationId}/nac/clients/{clientId}"

        body_params = [
            "type",
            "owner",
            "mac",
            "description",
            "uuid",
            "userDetails",
            "oui",
            "ipsk",
            "groups",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action
