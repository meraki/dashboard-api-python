import json

import meraki

"""
2023-11-13
Author: John M. Kuchta ( TKIPisalegacycipher // https://github.com/TKIPisalegacycipher )
Requrires: Meraki library v1.39.0 or later.

This script gathers all your appliances' local subnets from your organizations' networks and dumps them to a JSON file.
You might find this handy for certain IPAM exercises. Subnets from appliances in "single LAN" mode will have VLAN 0.

EXTRA CREDIT
If you are feeling adventurous, or just want an opportunity to flex your Python skills, consider re-writing this script
to work asynchronously, which can substantially improve the speed for large environments. You might start by gathering
all the relevant information asynchronously, then doing the list comprehensions after the API calls are complete.
"""

# You can exclude specific organization or networks here. This is optional but recommended if you have a large
# deployment including lots of irrelevant networks.
excluded_org_ids = []
excluded_network_ids = []

# init session
d = meraki.DashboardAPI()

# gather orgs
my_orgs = d.organizations.getOrganizations()
my_orgs = [org for org in my_orgs if org["id"] not in excluded_org_ids]

print(f"done gathering organizations")

# gather networks
my_networks = [
    d.organizations.getOrganizationNetworks(
        organization["id"], total_pages=all
    )
    for organization in my_orgs
]

print(f"done gathering networks")

my_appliance_networks = [
    network
    for netlist in my_networks
    for network in netlist
    if network["id"] not in excluded_network_ids
    and "appliance" in network["productTypes"]
]

print(f"done gathering appliance networks")

# gather routed networks -- appliances in passthrough mode don't have local subnets
my_appliance_routed_networks = [
    network
    for network in my_appliance_networks
    if d.appliance.getNetworkApplianceSettings(network["id"])["deploymentMode"]
    == "routed"
]

print(f"done gathering routed appliance networks")

my_appliance_networks_with_vlans = [
    network
    for network in my_appliance_routed_networks
    if d.appliance.getNetworkApplianceVlansSettings(network["id"])["vlansEnabled"]
]

print(f"done gathering appliance network vlan settings")

my_appliance_networks_without_vlans = [
    network
    for network in my_appliance_routed_networks
    if network not in my_appliance_networks_with_vlans
]

my_vlan_lists = [
    {
        "organizationId": network["organizationId"],
        "networkId": network["id"],
        "vlans": d.appliance.getNetworkApplianceVlans(network["id"]),
    }
    for network in my_appliance_networks_with_vlans
]

print(f"done gathering appliance network vlans")

my_lans = [
    {
        "organizationId": network["organizationId"],
        "networkId": network["id"],
        "lan": d.appliance.getNetworkApplianceSingleLan(network["id"]),
    }
    for network in my_appliance_networks_without_vlans
]

print(f"done gathering appliance network lans")

# unpack the subnets
vlan_subnets = list()

for item in my_vlan_lists:
    for vlan in item["vlans"]:
        this_subnet = dict()
        this_subnet["organizationId"] = item["organizationId"]
        this_subnet["networkId"] = vlan["networkId"]
        this_subnet["subnet"] = vlan["subnet"]
        this_subnet["vlanId"] = vlan["id"]
        this_subnet["applianceIp"] = vlan["applianceIp"]
        vlan_subnets.append(this_subnet)

lan_subnets = list()

for item in my_lans:
    this_subnet = dict()
    this_subnet["organizationId"] = item["organizationId"]
    this_subnet["networkId"] = item["networkId"]
    this_subnet["subnet"] = item["lan"]["subnet"]
    this_subnet["vlanId"] = 0
    this_subnet["applianceIp"] = item["lan"]["applianceIp"]
    lan_subnets.append(this_subnet)

all_subnets = vlan_subnets + lan_subnets

print("done assembling subnets")

# dump the subnets to a JSON file
json_object = json.dumps(all_subnets, indent=4)

with open(
    "subnets.json",
    "w",
) as outfile:
    outfile.write(json_object)

print("subnets dumped to subnets.json")
