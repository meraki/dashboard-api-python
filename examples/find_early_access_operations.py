import meraki

# The organization you supply here should be enrolled in early access to use this script.
# If your organization is not enrolled in early access, you will not see early access operations
# in the OAS.
ORGANIZATION_ID = "YOUR_ORG_ID_HERE"

d = meraki.DashboardAPI(suppress_logging=True)

oas = d.organizations.getOrganizationOpenapiSpec(ORGANIZATION_ID, version=3)

paths = oas["paths"]

operations = list()

# parse paths, e.g. '/path/to/operation'
for path in paths:
    # parse operation in each path, e.g. 'get'
    for key in paths[path].keys():
        if "x-release-stage" in paths[path][key].keys():
            operations.append(
                {
                    "id": paths[path][key]["operationId"],
                    "description": paths[path][key]["description"],
                    "x-release-stage": paths[path][key]["x-release-stage"],
                }
            )

print(f"Total number of non-GA operations is {len(operations)}.")

# Find the channels. We only want the distinct values.
channels = list(set([operation["x-release-stage"] for operation in operations]))

# Sort the channels.
channels.sort()

# How many channels?
print(f"{len(channels)} channels found. The channels are {channels}.")

# How many operations in each channel?
for channel in channels:
    print(
        f'There are {len([operation for operation in operations if operation["x-release-stage"] == channel])}'
        f" operations in the {channel} channel."
    )

if input(f"Would you like to see the operations? y/N") == 'y':
    print(operations)
else:
    print(f"Goodbye.")
