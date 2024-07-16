import meraki

print(
    f"To use this tool, you must supply your organization ID. Your organization ID should be an integer."
)
organization_id = "102908"
# organization_id = input(f"Enter your organization ID:")

all_rf_profiles = list()

d = meraki.DashboardAPI(suppress_logging=True)

# fetch RF profiles assignments by device
print(f"Fetching RF profile assignments for the organization")
rf_profiles_assignments = (
    d.wireless.getOrganizationWirelessRfProfilesAssignmentsByDevice(
        organization_id, total_pages=all
    )["items"]
)

# Find the top five profiles by how many devices are assigned to them
counts = list()
profiles = list()
profiles_and_counts = list()

profile_ids = list()
for assignment in rf_profiles_assignments:
    if assignment["rfProfile"]["id"] not in profile_ids:
        profile_ids.append(assignment["rfProfile"]["id"])
        assignment["rfProfile"]["count"] = 0
        profiles.append(assignment["rfProfile"])

# assemble the profiles
for assignment in rf_profiles_assignments:
    # build the list of relevant profiles
    if assignment["rfProfile"]["id"] not in profiles:
        profiles.append(assignment["rfProfile"])

# create a count for each profile
for profile in profiles:
    profile["count"] = 0

# count up the number of times something's assigned
# for assignment in rf_profiles_assignments:


# fetch wireless networks
print(f"Fetching wireless networks")
networks = d.organizations.getOrganizationNetworks(
    organization_id, productTypes=["wireless"], total_pages=all
)
wireless_networks = [
    network for network in networks if "wireless" in network["productTypes"]
]

print(f"Fetching RF profiles per network")
rf_profiles_by_network = [
    d.wireless.getNetworkWirelessRfProfiles(network["id"])
    for network in wireless_networks
]

# flatten the list
for network in rf_profiles_by_network:
    for profile in network:
        all_rf_profiles.append(profile)

print(f"Fetching RF profiles per network")
print(f"Fetching RF profiles per network")

print(1)
