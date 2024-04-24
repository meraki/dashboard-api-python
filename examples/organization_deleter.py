# organization_deleter.py
# A script to clean up and delete obsolete organizations, especially for lab testing scenarios.
# Deletes all networks, config templates, extra admins, and releases from inventory all devices
# in the organizations being deleted.
###############################
# WARNING
# This script is highly destructive. It should not be used in production environments.
###############################

import sys

import meraki

# This should be a list of string organization IDs you want to delete
# E.g., ["1","2","3"]
LIST_OF_ORGANIZATIONS_TO_DELETE = []

# This should be the single email address of the owner of the API key you're using to run this script.
# E.g., "tam@shan.ter"
EMAIL_ADDRESS_OF_API_KEY_OWNER = ""

print(
    f"This script will delete all orgs in this list: {LIST_OF_ORGANIZATIONS_TO_DELETE}"
)
confirmed = input(f"Are you sure you'd like to proceed? (yes/N)")

# User will need to type yes to continue
if confirmed != "yes":
    print("Aborting")
    sys.exit()

# Init dashboard session
d = meraki.DashboardAPI(suppress_logging=True)

for organization in LIST_OF_ORGANIZATIONS_TO_DELETE:
    print(f"Deleting networks in organization (id: {organization})...")

    # get networks
    org_networks = d.organizations.getOrganizationNetworks(organization)
    count_networks = len(org_networks)
    print(f"There are {count_networks} networks to delete.")
    for network in org_networks:
        print(f"Deleting network (id: {network['id']})...")
        delete_network = d.networks.deleteNetwork(network["id"])
        count_networks -= 1
        print(f"{count_networks} remaining.")
    print(f"Done deleting networks.")

    # get config templates
    org_templates = d.organizations.getOrganizationConfigTemplates(organization)
    count_templates = len(org_templates)
    for template in org_templates:
        print(f"Deleting config template (id: {template['id']})...")
        delete_network = d.organizations.deleteOrganizationConfigTemplate(
            organization, template["id"]
        )
        count_templates -= 1
        print(f"{count_templates} remaining.")
    print(f"Done deleting config templates.")

    # get org inventory devices
    org_devices = d.organizations.getOrganizationInventoryDevices(organization)
    count_devices = len(org_devices)
    print(f"There are {count_devices} devices to release from inventory.")
    device_serials = [device["serial"] for device in org_devices]
    if len(device_serials) > 0:
        release_devices = d.organizations.releaseFromOrganizationInventory(
            organization, serials=device_serials
        )
        print(f"Released {count_devices} devices from inventory.")
    print(f"Done releasing devices.")

    # get org admins
    org_admins = d.organizations.getOrganizationAdmins(organization)
    for admin in org_admins:
        if admin["email"] != EMAIL_ADDRESS_OF_API_KEY_OWNER:
            delete_admin = d.organizations.deleteOrganizationAdmin(
                organization, admin["id"]
            )

    print(f"Done deleting networks and admins in organization (id: {organization}).")

confirmed = input(f"Would you like to proceed with deleting the organizations? (yes/N)")

if confirmed != "yes":
    print("Aborting")
    sys.exit()

for organization in LIST_OF_ORGANIZATIONS_TO_DELETE:
    delete_organization = d.organizations.deleteOrganization(organization)
    print(f"Deleted organization (id: {organization}).")

print(f"Done deleting organizations.")
