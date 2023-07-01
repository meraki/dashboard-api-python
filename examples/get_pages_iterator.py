import argparse
import asyncio

import meraki

# Either input your API key below, or set an environment variable
# for example, in Terminal on macOS:  export MERAKI_DASHBOARD_API_KEY=66839003d2861bc302b292eb66d3b247709f2d0d
api_key = ""

ORGANIZATION_ID = ""
NETWORK_ID = ""


def getNetworksLegacy(meraki: meraki.DashboardAPI, perPage=5):
    count = 0
    for x in meraki.organizations.getOrganizationNetworks(organizationId=ORGANIZATION_ID, perPage=perPage,
                                                          total_pages=-1):
        print(f"{x['id']} - {x['name']}")
        count = count + 1
    print(f"Found {count} networks")


def getNetworksIterator(meraki: meraki.DashboardAPI, perPage=5):
    count = 0
    for x in meraki.organizations.getOrganizationNetworks(organizationId=ORGANIZATION_ID, perPage=perPage,
                                                          total_pages=-1):
        print(f"{x['id']} - {x['name']}")
        count = count + 1
    print(f"Found {count} networks")


def getNetworkEventsLegacy(meraki: meraki.DashboardAPI, perPage=5):
    count = 0
    result = meraki.networks.getNetworkEvents(networkId=NETWORK_ID, perPage=perPage, total_pages=50,
                                              productType="wireless")
    for x in result["events"]:
        print(f"{x['occurredAt']}")
        count = count + 1
    print(f"Found {count} events")


def getNetworkEventsIterator(meraki: meraki.DashboardAPI, perPage=5):
    count = 0
    for x in meraki.networks.getNetworkEvents(networkId=NETWORK_ID, perPage=perPage, total_pages=50,
                                              productType="wireless"):
        print(f"{x['occurredAt']}")
        count = count + 1
    print(f"Found {count} events")


async def main():
    parser = argparse.ArgumentParser(description='Example for demonstrating the use_iterator_for_get_pages parameter')

    # Instantiate a Meraki dashboard API session
    # NOTE: you have to use "async with" so that the session will be closed correctly at the end of the usage
    meraki_iterator = meraki.DashboardAPI(
        api_key,
        base_url="https://api.meraki.com/api/v1",
        log_file_prefix=__file__[:-3],
        print_console=True,
        use_iterator_for_get_pages=True
    )

    meraki_legacy = meraki.DashboardAPI(
        api_key,
        base_url="https://api.meraki.com/api/v1",
        log_file_prefix=__file__[:-3],
        print_console=False,
        use_iterator_for_get_pages=False
    )

    print("Test legacy")
    getNetworksLegacy(meraki_legacy)

    await asyncio.sleep(2)  # just wait two seconds between the tests

    print("Test iterator")
    getNetworksIterator(meraki_iterator)

    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")

    print("Test legacy")
    getNetworkEventsLegacy(meraki_legacy)

    await asyncio.sleep(2)  # just wait two seconds between the tests

    print("Test iterator")
    getNetworkEventsIterator(meraki_iterator)

    print("Script complete!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
