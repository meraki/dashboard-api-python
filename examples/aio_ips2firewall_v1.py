import argparse
import asyncio
import ipaddress
import sys
from typing import Dict, List

import meraki.aio

# Either input your API key below, or set an environment variable
# for example, in Terminal on macOS:  export MERAKI_DASHBOARD_API_KEY=66839003d2861bc302b292eb66d3b247709f2d0d
api_key = ""


def removeSmallAmounts(ip_counts: Dict[str, int], filter: int):
    ret = ip_counts.copy()
    for k, v in ip_counts.items():
        if v < filter:
            ret.pop(k)

    return ret


async def analyzeOrganization(aiomeraki: meraki.aio.AsyncDashboardAPI, orgId: str, days: int) -> Dict[str, int]:
    ret = {}
    timespan = days * 24 * 60 * 60
    events = await aiomeraki.appliance.getOrganizationApplianceSecurityEvents(orgId, timespan=timespan, total_pages=-1)
    for e in events:
        ip, port = e["srcIp"].rsplit(":", 1)
        ip = ip.strip("[]")  # remove brackets in case of ipv6
        if not ipaddress.ip_address(ip).is_private:  # don't block private ip addresses on the public ip of the firewall
            ret[ip] = ret.get(ip, 0) + 1

    return ret


async def updateFirewallrules(aiomeraki: meraki.aio.AsyncDashboardAPI, networkId: str, ip_list: List[str]):
    rules = await aiomeraki.appliance.getNetworkApplianceFirewallL7FirewallRules(networkId)

    rules = rules["rules"]
    # get the currently blocked ip ranges
    current_blocks = [x["value"] for x in rules if x["type"] == "ipRange"]

    new_blocks = current_blocks + list(set(ip_list) - set(current_blocks))
    new_blocks = sorted(new_blocks)

    # generate new rules based on the list of total ip ranges to block
    rules_to_add = [{"policy": "deny", "type": "ipRange", "value": x} for x in new_blocks]

    # remove all currently blocked ip ranges
    rules = [x for x in rules if x["type"] != "ipRange"]

    rules = rules + rules_to_add

    await aiomeraki.appliance.updateNetworkApplianceFirewallL7FirewallRules(networkId, rules=rules)


async def main():
    parser = argparse.ArgumentParser(description='Block IP Addresses based on security events')
    parser.add_argument('-o', '--organization', type=str, nargs='+', dest="organizations", required=True,
                        help='the name/id of the organization(s) you want to analyze/secure')
    parser.add_argument("-f", '--filter', dest='filter', type=int, default=5,
                        help='how often must an attack be listed before it gets blocked')
    parser.add_argument("-s", '--save', dest='save', action='store_true',
                        help='write the blocklist to all networks in the organization.')
    parser.add_argument("-d", '--days', dest='days', default=31, type=int,
                        help='How many days should be analyzed.')

    if len(sys.argv) < 3:
        parser.print_help()
        return

    try:
        args = parser.parse_args()
        if args.days >= 365:
            print("days must be < 365")
            parser.print_help()
            return
    except SystemExit:
        return
    except:
        print("could not parse arguments")
        parser.print_help()
        return

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
        for x in organizations:
            if x["id"] in args.organizations or x["name"] in args.organizations:
                print(f"Analyzing organization {x['name']}")
                result = await analyzeOrganization(aiomeraki, x["id"], args.days)
                result = removeSmallAmounts(result, args.filter)
                sum = 0

                for k, v in result.items():
                    print(f"{k} attacked {v} times.")
                    sum = sum + v
                print(f"Total attacks: {sum} from {len(result)} different IP adresses")

                # apply the found ip ranges to the firewall
                if args.save:
                    for n in await aiomeraki.organizations.getOrganizationNetworks(x["id"]):
                        print(f"Updating Network {n['name']}")
                        await updateFirewallrules(aiomeraki, n["id"], result.keys())

        print("Script complete!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
