import csv
from datetime import datetime
import os
import asyncio

import meraki.aio

# Either input your API key below, or set an environment variable
# for example, in Terminal on macOS:  export MERAKI_DASHBOARD_API_KEY=093b24e85df15a3e66f1fc359f4c48493eaa1b73
api_key = ""


async def listNetworkClients(aiomeraki: meraki.aio.AsyncDashboardAPI, folder_name, network):
    print(f'Finding clients in network {network["name"]}')
    try:
        # Get list of clients on network, filtering on timespan of last 14 days
        clients = await aiomeraki.networks.getNetworkClients(
            network["id"],
            timespan=60 * 60 * 24 * 14,
            perPage=1000,
            total_pages="all",
        )
    except meraki.AsyncAPIError as e:
        print(f"Meraki API error: {e}")
    except Exception as e:
        print(f"some other error: {e}")
    else:
        if clients:
            # Write to file
            file_name = f'{network["name"]}.csv'
            output_file = open(
                f"{folder_name}/{file_name}", mode="w", newline="\n"
            )
            field_names = clients[0].keys()
            csv_writer = csv.DictWriter(
                output_file,
                field_names,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_ALL,
            )
            csv_writer.writeheader()
            csv_writer.writerows(clients)
            output_file.close()
            print(
                f"Successfully output {len(clients)} clients' data to file {file_name}"
            )
            return network["name"], field_names
    return network["name"], None


async def listOrganization(aiomeraki: meraki.aio.AsyncDashboardAPI, org):
    print(f'Analyzing organization {org["name"]}:')
    org_id = org["id"]

    # Get list of networks in organization
    try:
        networks = await aiomeraki.organizations.getOrganizationNetworks(org_id)
    except meraki.AsyncAPIError as e:
        print(f"Meraki API error: {e}")
        return org["name"]
    except Exception as e:
        print(f"some other error: {e}")
        return org["name"]

    # Create local folder
    todays_date = f"{datetime.now():%Y-%m-%d}"
    folder_name = f"Org {org_id} clients {todays_date}"
    if folder_name not in os.listdir():
        os.mkdir(folder_name)

    # Iterate through networks
    total = len(networks)
    print(f"Iterating through {total} networks in organization {org_id}")

    # create a list of all networks in the organization so we can call them all concurrently
    networkClientsTasks = [listNetworkClients(aiomeraki, folder_name, net) for net in networks]
    for task in asyncio.as_completed(networkClientsTasks):
        networkname, field_names = await task
        print(f"finished network: {networkname}")

    # Stitch together one consolidated CSV per org
    output_file = open(f"{folder_name}.csv", mode="w", newline="\n")
    field_names = ['id', 'mac', 'description', 'ip', 'ip6', 'ip6Local', 'user', 'firstSeen', 'lastSeen', 'manufacturer', 'os', 'recentDeviceSerial', 'recentDeviceName', 'recentDeviceMac', 'ssid', 'vlan', 'switchport', 'usage', 'status', 'notes', 'smInstalled', 'groupPolicy8021x']
    field_names.insert(0, "Network Name")
    field_names.insert(1, "Network ID")
    
    csv_writer = csv.DictWriter(
        output_file,
        field_names,
        delimiter=",",
        quotechar='"',
        quoting=csv.QUOTE_ALL,
    )
    csv_writer.writeheader()
    for net in networks:
        file_name = f'{net["name"]}.csv'
        if file_name in os.listdir(folder_name):
            with open(f"{folder_name}/{file_name}") as input_file:
                csv_reader = csv.DictReader(
                    input_file,
                    delimiter=",",
                    quotechar='"',
                    quoting=csv.QUOTE_ALL,
                )
                next(csv_reader)
                for row in csv_reader:
                    row["Network Name"] = net["name"]
                    row["Network ID"] = net["id"]
                    csv_writer.writerow(row)
    return org["name"]


async def main():
    # Instantiate a Meraki dashboard API session
    # NOTE: you have to use "async with" so that the session will be closed correctly at the end of the usage
    async with meraki.aio.AsyncDashboardAPI(
            api_key,
            base_url="https://api.meraki.com/api/v1",
            log_file_prefix=__file__[:-3],
            print_console=False,
    ) as aiomeraki:
        # Get list of organizations to which API key has access
        organizations = await aiomeraki.organizations.getOrganizations()

        # create a list of all organizations so we can call them all concurrently
        organizationTasks = [listOrganization(aiomeraki, org) for org in organizations]
        for task in asyncio.as_completed(organizationTasks):
            # as_completed returns an iterator, so we just have to await the iterator and not call it
            organizationName = await task
            print(f"finished organization: {organizationName}")

        print("Script complete!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
