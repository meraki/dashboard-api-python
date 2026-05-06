"""Opt in to all available early access features for a Meraki organization.

Reads BETA_ORG_1_ID from the environment, fetches the feature list,
creates org-wide opt-ins for any features not already enabled, and
prints a summary report.

WARNING: This will subject the organization to unannounced breaking API
changes.
"""

import asyncio
import os
import sys

import meraki.aio

ORG_ID: str = os.environ.get("BETA_ORG_1_ID", "")
if not ORG_ID:
    sys.exit("BETA_ORG_1_ID environment variable is not set")


async def main():
    async with meraki.aio.AsyncDashboardAPI(suppress_logging=True) as dashboard:
        features = await dashboard.organizations.getOrganizationEarlyAccessFeatures(ORG_ID)
        opt_ins = await dashboard.organizations.getOrganizationEarlyAccessFeaturesOptIns(ORG_ID)

        opted_in_short_names = {oi["shortName"] for oi in opt_ins}

        tasks = []
        for feature in features:
            if feature["shortName"] not in opted_in_short_names:
                tasks.append(dashboard.organizations.createOrganizationEarlyAccessFeaturesOptIn(ORG_ID, feature["shortName"]))

        new_opt_ins = await asyncio.gather(*tasks) if tasks else []

        all_opt_ins = opt_ins + list(new_opt_ins)
        print(f"Enabled {len(new_opt_ins)} new features ({len(opt_ins)} already opted in)")
        print(f"\nAll early access features ({len(all_opt_ins)} total):")
        for oi in all_opt_ins:
            print(f"  - {oi['shortName']}")

        return all_opt_ins


if __name__ == "__main__":
    asyncio.run(main())
