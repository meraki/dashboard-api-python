"""Seed each test org with 10 networks so integration tests that assume
pre-existing networks (e.g. test_org_wide_workflows.py) don't fail on
an empty org. Idempotent; skips networks that already exist by name.

Usage: TEST_MERAKI_DASHBOARD_API_KEY=... python scripts/seed-networks.py
"""

import asyncio
import os
import sys

import meraki.aio


async def main():
    api_key = os.environ.get("TEST_MERAKI_DASHBOARD_API_KEY")
    if not api_key:
        print("ERROR: TEST_MERAKI_DASHBOARD_API_KEY is not set")
        sys.exit(1)

    async with meraki.aio.AsyncDashboardAPI(api_key, suppress_logging=True) as dashboard:
        orgs = await dashboard.organizations.getOrganizations()
        print(f"Found {len(orgs)} orgs")

        async def seed_org(org):
            org_id = org["id"]
            org_name = org["name"]

            networks = await dashboard.organizations.getOrganizationNetworks(org_id, total_pages="all")
            existing_names = {n["name"] for n in networks}
            print(f"\n{org_name} ({org_id}): {len(networks)} existing networks")

            tasks = []
            for i in range(10):
                name = f"Seed Network {i:02d}"
                if name in existing_names:
                    print(f"  Skipped {name} (already exists)")
                    continue
                tasks.append(create_network(dashboard, org_id, name))

            for result in await asyncio.gather(*tasks):
                print(f"  Created {result}")

        async def create_network(dashboard, org_id, name):
            await dashboard.organizations.createOrganizationNetwork(
                org_id, name=name, productTypes=["appliance", "wireless", "sensor", "cellularGateway"]
            )
            return name

        await asyncio.gather(*(seed_org(org) for org in orgs))

    print("\nDone")


if __name__ == "__main__":
    asyncio.run(main())
