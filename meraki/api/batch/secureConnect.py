import urllib


class ActionBatchSecureConnect(object):
    def __init__(self):
        super(ActionBatchSecureConnect, self).__init__()

    def createOrganizationSecureConnectPrivateResourceGroup(self, organizationId: str, name: str, **kwargs):
        """
        **Adds a new private resource group to an organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-private-resource-group

        - organizationId (string): Organization ID
        - name (string): Name of group. This is required and should be unique across all groups for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - description (string): Optional text description for a group.
        - resourceIds (array): List of resource ids assigned to this group.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups"

        body_params = [
            "name",
            "description",
            "resourceIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationSecureConnectPrivateResourceGroup(self, organizationId: str, id: str, name: str, **kwargs):
        """
        **Updates a specific private resource group.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-secure-connect-private-resource-group

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of group. This is required and should be unique across all groups for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - description (string): Optional text description for a group.
        - resourceIds (array): List of resource ids assigned to this group.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups/{id}"

        body_params = [
            "name",
            "description",
            "resourceIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSecureConnectPrivateResourceGroup(self, organizationId: str, id: str):
        """
        **Deletes a specific private resource group.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-private-resource-group

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResourceGroups/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationSecureConnectPrivateResource(
        self, organizationId: str, name: str, accessTypes: list, resourceAddresses: list, **kwargs
    ):
        """
        **Adds a new private resource to the organization.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-private-resource

        - organizationId (string): Organization ID
        - name (string): Name of resource. This is required and should be unique across all resources for a given organization. Name cannot have any special characters other than spaces and hyphens.
        - accessTypes (array): List of access types.
        - resourceAddresses (array): List of resource addresses Protocols must be unique in this list.
        - description (string): Optional text description for a resource.
        - resourceGroupIds (array): List of resource group ids attached to this resource.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources"

        body_params = [
            "name",
            "description",
            "accessTypes",
            "resourceAddresses",
            "resourceGroupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def updateOrganizationSecureConnectPrivateResource(
        self, organizationId: str, id: str, name: str, accessTypes: list, resourceAddresses: list, **kwargs
    ):
        """
        **Updates a specific private resource.**
        https://developer.cisco.com/meraki/api-v1/#!update-organization-secure-connect-private-resource

        - organizationId (string): Organization ID
        - id (string): ID
        - name (string): Name of resource. This is required and should be unique across all resources for a given organization.Name cannot have any special characters other than spaces and hyphens.
        - accessTypes (array): List of access types.
        - resourceAddresses (array): List of resource addresses Protocols must be unique in this list.
        - description (string): Optional text description for resource.
        - resourceGroupIds (array): List of resource group ids attached to this resource.
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources/{id}"

        body_params = [
            "name",
            "description",
            "accessTypes",
            "resourceAddresses",
            "resourceGroupIds",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "update",
            "body": payload,
        }
        return action

    def deleteOrganizationSecureConnectPrivateResource(self, organizationId: str, id: str):
        """
        **Deletes a specific private resource. If this is the last resource in a resource group you must remove it from that resource group before deleting.**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-private-resource

        - organizationId (string): Organization ID
        - id (string): ID
        """

        organizationId = urllib.parse.quote(organizationId, safe="")
        id = urllib.parse.quote(id, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/privateResources/{id}"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action

    def createOrganizationSecureConnectSite(self, organizationId: str, **kwargs):
        """
        **Enroll sites in this organization to Secure Connect. For an organization, a maximum of 4000 sites can be enrolled if they are in spoke mode or a maximum of 10 sites can be enrolled in hub mode.**
        https://developer.cisco.com/meraki/api-v1/#!create-organization-secure-connect-site

        - organizationId (string): Organization ID
        - enrollments (array): List of Meraki SD-WAN sites with the associated regions to be enrolled.
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/sites"

        body_params = [
            "enrollments",
            "callback",
        ]
        payload = {k.strip(): v for k, v in kwargs.items() if k.strip() in body_params}
        action = {
            "resource": resource,
            "operation": "create",
            "body": payload,
        }
        return action

    def deleteOrganizationSecureConnectSites(self, organizationId: str, **kwargs):
        """
        **Detach given sites from Secure Connect**
        https://developer.cisco.com/meraki/api-v1/#!delete-organization-secure-connect-sites

        - organizationId (string): Organization ID
        - sites (array): List of site IDs to detach
        - callback (object): Details for the callback. Please include either an httpServerId OR url and sharedSecret
        """

        kwargs.update(locals())

        organizationId = urllib.parse.quote(organizationId, safe="")
        resource = f"/organizations/{organizationId}/secureConnect/sites"

        action = {
            "resource": resource,
            "operation": "destroy",
        }
        return action
