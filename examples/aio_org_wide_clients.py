import csv
from datetime import datetime
import os
import asyncio

import meraki.aio

# Either input your API key below, or set an environment variable
# for example, in Terminal on macOS:  export MERAKI_DASHBOARD_API_KEY=66839003d2861bc302b292eb66d3b247709f2d0d
api_key = ""


async def main():
    # Instantiate a Meraki dashboard API session
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        base_url="https://api.meraki.com/api/v0",
        log_file_prefix=__file__[:-3],
        print_console=False,
    ) as m:

        # Get list of organizations to which API key has access
        organizations = await m.organizations.getOrganizations()

        # Iterate through list of orgs
        for org in organizations:
            print(f'Analyzing organization {org["name"]}:')
            org_id = org["id"]

            # Get list of networks in organization
            try:
                networks = await m.networks.getOrganizationNetworks(org_id)
            except meraki.APIError as e:
                print(f"Meraki API error: {e}")
                continue
            except Exception as e:
                print(f"some other error: {e}")
                continue

            # Create local folder
            todays_date = f"{datetime.now():%Y-%m-%d}"
            folder_name = f"Org {org_id} clients {todays_date}"
            if folder_name not in os.listdir():
                os.mkdir(folder_name)

            # Iterate through networks
            total = len(networks)
            counter = 1
            print(f"Iterating through {total} networks in organization {org_id}")
            for net in networks:
                print(
                    f'Finding clients in network {net["name"]} ({counter} of {total})'
                )
                try:
                    # Get list of clients on network, filtering on timespan of last 14 days
                    clients = await m.clients.getNetworkClients(
                        net["id"],
                        timespan=60 * 60 * 24 * 14,
                        perPage=1000,
                        total_pages="all",
                    )
                except meraki.APIError as e:
                    print(f"Meraki API error: {e}")
                except Exception as e:
                    print(f"some other error: {e}")
                else:
                    if clients:
                        # Write to file
                        file_name = f'{net["name"]}.csv'
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

                counter += 1

            # Stitch together one consolidated CSV per org
            output_file = open(f"{folder_name}.csv", mode="w", newline="\n")
            field_names = list(field_names)
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

        print("Script complete!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
