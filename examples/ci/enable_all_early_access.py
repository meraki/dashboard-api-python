"""Opt in to all available early access features for Meraki organizations.

Reads EA_ORG_0 through EA_ORG_7 from the environment, and for each org
fetches the feature list, creates org-wide opt-ins for any features not
already enabled, and prints a summary report.

WARNING: This will subject the organizations to unannounced breaking API
changes.
"""

import asyncio
import os
import sys

import meraki.aio

ORG_IDS: list[str] = [v for i in range(8) if (v := os.environ.get(f"EA_ORG_{i}", ""))]
if not ORG_IDS:
    sys.exit("No EA_ORG_* environment variables are set")


async def enable_early_access(dashboard, org_id: str):
    features = await dashboard.organizations.getOrganizationEarlyAccessFeatures(org_id)
    opt_ins = await dashboard.organizations.getOrganizationEarlyAccessFeaturesOptIns(org_id)

    opted_in_short_names = {oi["shortName"] for oi in opt_ins}

    tasks = []
    for feature in features:
        if feature["shortName"] not in opted_in_short_names:
            tasks.append(dashboard.organizations.createOrganizationEarlyAccessFeaturesOptIn(org_id, feature["shortName"]))

    new_opt_ins = await asyncio.gather(*tasks) if tasks else []

    all_opt_ins = opt_ins + list(new_opt_ins)
    print(f"\nOrg {org_id}: enabled {len(new_opt_ins)} new features ({len(opt_ins)} already opted in)")
    print(f"  All early access features ({len(all_opt_ins)} total):")
    for oi in all_opt_ins:
        print(f"    - {oi['shortName']}")

    return all_opt_ins


async def main():
    async with meraki.aio.AsyncDashboardAPI(suppress_logging=True) as dashboard:
        results = await asyncio.gather(*(enable_early_access(dashboard, org_id) for org_id in ORG_IDS))
    return results


if __name__ == "__main__":
    asyncio.run(main())
