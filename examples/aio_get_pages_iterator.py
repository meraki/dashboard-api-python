import csv
from datetime import datetime, timedelta
import os
import asyncio
import argparse
import ipaddress
from typing import Dict,List
import sys
import time

import meraki.aio

# Either input your API key below, or set an environment variable
# for example, in Terminal on macOS:  export MERAKI_DASHBOARD_API_KEY=66839003d2861bc302b292eb66d3b247709f2d0d
api_key = ""

ORGANIZATION_ID = ""
NETWORK_ID = ""


def timeit(func):
    async def process(func, *args, **params):
        if asyncio.iscoroutinefunction(func):
            print('this function is a coroutine: {}'.format(func.__name__))
            return await func(*args, **params)
        else:
            print('this is not a coroutine')
            return func(*args, **params)

    async def helper(*args, **params):
        print('{}.time'.format(func.__name__))
        start = time.time()
        result = await process(func, *args, **params)

        # Test normal function route...
        # result = await process(lambda *a, **p: print(*a, **p), *args, **params)

        print('>>>', time.time() - start)
        return result

    return helper


@timeit
async def getNetworksLegacy(aiomeraki: meraki.aio.AsyncDashboardAPI, perPage=5):
    count = 0
    for x in await aiomeraki.organizations.getOrganizationNetworks(organizationId=ORGANIZATION_ID, perPage=perPage, total_pages=-1):
        print(f"{x['id']} - {x['name']}")
        count = count + 1
    print(f"Found {count} networks")


@timeit
async def getNetworksIterator(aiomeraki: meraki.aio.AsyncDashboardAPI, perPage=5):
    count = 0
    async for x in aiomeraki.organizations.getOrganizationNetworks(organizationId=ORGANIZATION_ID, perPage=perPage,total_pages=-1):
        print(f"{x['id']} - {x['name']}")
        count = count + 1
    print(f"Found {count} networks")


@timeit
async def getNetworkEventsLegacy(aiomeraki: meraki.aio.AsyncDashboardAPI, perPage=5):
    count = 0
    result = await aiomeraki.networks.getNetworkEvents(networkId=NETWORK_ID, perPage=perPage,total_pages=50,productType="wireless")
    for x in result["events"]:
        print(f"{x['occurredAt']}")
        count = count + 1
    print(f"Found {count} events")


@timeit
async def getNetworkEventsIterator(aiomeraki: meraki.aio.AsyncDashboardAPI, perPage=5):
    count = 0
    async for x in aiomeraki.networks.getNetworkEvents(networkId=NETWORK_ID, perPage=perPage,total_pages=50,productType="wireless"):
        print(f"{x['occurredAt']}")
        count = count + 1
    print(f"Found {count} events")


async def main():

    parser = argparse.ArgumentParser(description='Example for demonstrating the use_iterator_for_get_pages parameter')

    # Instantiate a Meraki dashboard API session
    # NOTE: you have to use "async with" so that the session will be closed correctly at the end of the usage
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        base_url="https://api.meraki.com/api/v1",
        log_file_prefix=__file__[:-3],
        print_console=True,
        use_iterator_for_get_pages = True
    ) as aiomeraki_iterator:
        async with meraki.aio.AsyncDashboardAPI(
        api_key,
        base_url="https://api.meraki.com/api/v1",
        log_file_prefix=__file__[:-3],
        print_console=False,
        use_iterator_for_get_pages = False
        ) as aiomeraki_legacy:
            pass

            
            print("Test legacy")
            await getNetworksLegacy(aiomeraki_legacy)

            await asyncio.sleep(2) #just wait two seconds between the tests

            print("Test iterator")
            await getNetworksIterator(aiomeraki_iterator)
            
            print("-----------------------------------------------------------------------")
            print("-----------------------------------------------------------------------")
            print("-----------------------------------------------------------------------")
            print("-----------------------------------------------------------------------")

            print("Test legacy")
            await getNetworkEventsLegacy(aiomeraki_legacy)

            await asyncio.sleep(2) #just wait two seconds between the tests

            print("Test iterator")
            await getNetworkEventsIterator(aiomeraki_iterator)

        print("Script complete!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

