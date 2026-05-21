import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import meraki.aio
from meraki.exceptions import AsyncAPIError

TOOL_VERSION = "0.1.0b"
DEFAULT_NETWORK_ID = ""
DEFAULT_ORG_ID = ""
BACKUP_DIR = Path(__file__).parent / "ssid_backups"
DEFAULTS_FILE = Path(__file__).parent / "defaults.json"

SSID_SUB_RESOURCES = {
    "main": {
        "get": "getNetworkWirelessSsid",
        "update": "updateNetworkWirelessSsid",
    },
    "bonjourForwarding": {
        "get": "getNetworkWirelessSsidBonjourForwarding",
        "update": "updateNetworkWirelessSsidBonjourForwarding",
    },
    "deviceTypeGroupPolicies": {
        "get": "getNetworkWirelessSsidDeviceTypeGroupPolicies",
        "update": "updateNetworkWirelessSsidDeviceTypeGroupPolicies",
    },
    "eapOverride": {
        "get": "getNetworkWirelessSsidEapOverride",
        "update": "updateNetworkWirelessSsidEapOverride",
    },
    "firewallL3": {
        "get": "getNetworkWirelessSsidFirewallL3FirewallRules",
        "update": "updateNetworkWirelessSsidFirewallL3FirewallRules",
    },
    "firewallL7": {
        "get": "getNetworkWirelessSsidFirewallL7FirewallRules",
        "update": "updateNetworkWirelessSsidFirewallL7FirewallRules",
    },
    "hotspot20": {
        "get": "getNetworkWirelessSsidHotspot20",
        "update": "updateNetworkWirelessSsidHotspot20",
    },
    "schedules": {
        "get": "getNetworkWirelessSsidSchedules",
        "update": "updateNetworkWirelessSsidSchedules",
    },
    "splashSettings": {
        "get": "getNetworkWirelessSsidSplashSettings",
        "update": "updateNetworkWirelessSsidSplashSettings",
    },
    "trafficShapingRules": {
        "get": "getNetworkWirelessSsidTrafficShapingRules",
        "update": "updateNetworkWirelessSsidTrafficShapingRules",
    },
    "vpn": {
        "get": "getNetworkWirelessSsidVpn",
        "update": "updateNetworkWirelessSsidVpn",
    },
}


class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    DIM = "\033[2m"


def cprint(msg: str, color: str = Color.RESET) -> None:
    print(f"{color}{msg}{Color.RESET}")


class AsyncSpinner:
    FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

    def __init__(self, message: str = "Working"):
        self.message = message
        self._task: asyncio.Task | None = None

    async def _spin(self) -> None:
        i = 0
        try:
            while True:
                frame = self.FRAMES[i % len(self.FRAMES)]
                print(
                    f"\r{Color.CYAN}{frame} {self.message}...{Color.RESET}",
                    end="",
                    flush=True,
                )
                i += 1
                await asyncio.sleep(0.1)
        except asyncio.CancelledError:
            print(f"\r{' ' * (len(self.message) + 10)}\r", end="", flush=True)

    async def __aenter__(self):
        self._task = asyncio.create_task(self._spin())
        return self

    async def __aexit__(self, *_):
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass


IDENTITY_PSK_CREATE_PARAMS = ["name", "passphrase", "groupPolicyId", "expiresAt"]

# Keys that are path parameters or read-only identifiers returned by GET
PATH_PARAMS = {"networkId", "number", "ssidNumber"}

WRITE_EXCLUDE_KEYS = {
    "splashSettings": {
        "sentryEnrollment": "References network-specific Systems Manager network ID",
        "guestSponsorship": "API returns null for durationInMinutes (expects integer)",
        "billing": "API returns null for prepaidAccessFastLoginEnabled (expects boolean)",
    },
    "hotspot20": {
        "operator": "API returns null for name (expects string)",
        "venue": "API returns null for name/type (expects strings)",
    },
    "vpn": {
        "failover": "API returns null for requestIp (expects string)",
        "concentrator": "Requires a VPN concentrator configured on the network",
        "splitTunnel": "Depends on concentrator; fails if VPN topology not present",
    },
}


def strip_nulls(obj: dict) -> dict:
    def _recurse(val: object) -> object:
        if isinstance(val, dict):
            return {k: _recurse(v) for k, v in val.items() if v is not None}
        if isinstance(val, list):
            return [_recurse(item) for item in val]
        return val

    result = _recurse(obj)
    assert isinstance(result, dict)
    return result


def prepare_payload(resource_name: str, raw: dict, apply_exclusions: bool = True) -> dict:
    payload = strip_nulls({k: v for k, v in raw.items() if k not in PATH_PARAMS})
    if apply_exclusions:
        exclude = WRITE_EXCLUDE_KEYS.get(resource_name)
        if exclude:
            payload = {k: v for k, v in payload.items() if k not in exclude}
    if resource_name == "firewallL3" and "rules" in payload:
        payload["rules"] = [r for r in payload["rules"] if r.get("destCidr") not in ("Local LAN", "local_lan")]
    return payload


async def fetch_identity_psks(api: meraki.aio.AsyncDashboardAPI, network_id: str, ssid_number: int) -> list[dict]:
    try:
        return await api.wireless.getNetworkWirelessSsidIdentityPsks(network_id, str(ssid_number))
    except AsyncAPIError as e:
        if e.status in (400, 404):
            return []
        raise


async def swap_identity_psks(
    api: meraki.aio.AsyncDashboardAPI,
    network_id: str,
    slot_a: int,
    slot_b: int,
    psks_a: list[dict],
    psks_b: list[dict],
) -> tuple[list[str], list[str]]:
    success = []
    failed = []

    async def _delete(slot, psk):
        try:
            await api.wireless.deleteNetworkWirelessSsidIdentityPsk(network_id, str(slot), psk["id"])
            return None
        except AsyncAPIError as e:
            return f"identityPsks: delete {psk['name']} from slot {slot} ({e.status})"

    delete_tasks = [_delete(slot_a, p) for p in psks_a] + [_delete(slot_b, p) for p in psks_b]
    if delete_tasks:
        delete_results = await asyncio.gather(*delete_tasks)
        failed.extend(r for r in delete_results if r)

    async def _create(slot, psk):
        payload = {k: v for k, v in psk.items() if k in IDENTITY_PSK_CREATE_PARAMS and v is not None}
        if "name" not in payload or "groupPolicyId" not in payload:
            return None
        try:
            await api.wireless.createNetworkWirelessSsidIdentityPsk(network_id, str(slot), **payload)
            return ("success", f"identityPsks: {psk['name']} -> slot {slot}")
        except AsyncAPIError as e:
            return ("failed", f"identityPsks: create {psk['name']} on slot {slot} ({e.status})")

    create_tasks = [_create(slot_b, p) for p in psks_a] + [_create(slot_a, p) for p in psks_b]
    if create_tasks:
        create_results = await asyncio.gather(*create_tasks)
        for r in create_results:
            if r:
                (success if r[0] == "success" else failed).append(r[1])

    return success, failed


async def fetch_ssid_sub_resources(api: meraki.aio.AsyncDashboardAPI, network_id: str, ssid_number: int) -> tuple[dict, list]:
    """Fetch all sub-resources for a single SSID slot (excludes main config)."""
    config = {}
    errors = []

    async def _fetch_one(resource_name: str, resource_info: dict):
        getter = getattr(api.wireless, resource_info["get"])
        try:
            return resource_name, await getter(network_id, str(ssid_number)), None
        except AsyncAPIError as e:
            if e.status in (400, 404):
                return resource_name, None, str(e)
            raise

    tasks = [_fetch_one(name, info) for name, info in SSID_SUB_RESOURCES.items() if name != "main"]
    tasks.append(_fetch_psk_wrapper(api, network_id, ssid_number))

    results = await asyncio.gather(*tasks)

    for result in results:
        name, data, err = result
        config[name] = data
        if err:
            errors.append((name, err))

    return config, errors


async def _fetch_psk_wrapper(api: meraki.aio.AsyncDashboardAPI, network_id: str, ssid_number: int):
    data = await fetch_identity_psks(api, network_id, ssid_number)
    return "identityPsks", data, None


async def fetch_ssid_full_config(api: meraki.aio.AsyncDashboardAPI, network_id: str, ssid_number: int) -> tuple[dict, list]:
    """Fetch main config + all sub-resources for a single SSID slot."""

    async def _fetch_main():
        try:
            return await api.wireless.getNetworkWirelessSsid(network_id, str(ssid_number))
        except AsyncAPIError as e:
            if e.status in (400, 404):
                return None
            raise

    main, (sub, errors) = await asyncio.gather(
        _fetch_main(),
        fetch_ssid_sub_resources(api, network_id, ssid_number),
    )
    sub["main"] = main
    return sub, errors


async def backup_all_ssids(api: meraki.aio.AsyncDashboardAPI, network_id: str) -> tuple[Path, list]:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"{timestamp}-{network_id}-ssids.jsonc"
    filepath = BACKUP_DIR / filename
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    all_ssids = {}
    all_errors = []

    async with AsyncSpinner("Backing up SSIDs"):
        ssids = await api.wireless.getNetworkWirelessSsids(network_id)

        async def _backup_slot(ssid: dict):
            slot = ssid["number"]
            sub, errors = await fetch_ssid_sub_resources(api, network_id, slot)
            sub["main"] = ssid
            return slot, sub, errors

        results = await asyncio.gather(*[_backup_slot(s) for s in ssids])
        for slot, sub, errors in results:
            all_ssids[str(slot)] = sub
            all_errors.extend(errors)

    header = f"// SSID Backup - ssid_tool v{TOOL_VERSION}\n// {datetime.now().isoformat()}\n// Network: {network_id}\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header)
        json.dump(all_ssids, f, indent=2, ensure_ascii=False)

    return filepath, all_errors


async def swap_ssid_slots(
    api: meraki.aio.AsyncDashboardAPI,
    network_id: str,
    slot_a: int,
    slot_b: int,
) -> dict:
    async with AsyncSpinner(f"Reading slots {slot_a} and {slot_b}"):
        (config_a, _), (config_b, _) = await asyncio.gather(
            fetch_ssid_full_config(api, network_id, slot_a),
            fetch_ssid_full_config(api, network_id, slot_b),
        )

    results = {"success": [], "failed": []}

    # Free up SSID names to avoid uniqueness constraint during swap
    async with AsyncSpinner("Preparing swap"):
        await asyncio.gather(
            api.wireless.updateNetworkWirelessSsid(network_id, str(slot_a), name=f"_swap_tmp_{slot_a}"),
            api.wireless.updateNetworkWirelessSsid(network_id, str(slot_b), name=f"_swap_tmp_{slot_b}"),
        )

    async with AsyncSpinner("Swapping configurations"):

        async def _apply(resource_name, src_slot, dst_slot, config):
            updater = getattr(api.wireless, SSID_SUB_RESOURCES[resource_name]["update"])
            payload = prepare_payload(resource_name, config.get(resource_name) or {}, apply_exclusions=False)
            if not payload:
                return None
            try:
                await updater(network_id, str(dst_slot), **payload)
                return ("success", f"{resource_name}: slot {src_slot} -> slot {dst_slot}")
            except AsyncAPIError as e:
                return ("failed", f"{resource_name}: slot {src_slot} -> slot {dst_slot} ({e.status})")

        swap_tasks = []
        for resource_name in SSID_SUB_RESOURCES:
            if resource_name in ("vpn", "hotspot20"):
                continue
            swap_tasks.append(_apply(resource_name, slot_a, slot_b, config_a))
            swap_tasks.append(_apply(resource_name, slot_b, slot_a, config_b))

        swap_results = await asyncio.gather(*swap_tasks)
        for r in swap_results:
            if r:
                results[r[0]].append(r[1])

        psks_a = config_a.get("identityPsks", [])
        psks_b = config_b.get("identityPsks", [])
        if psks_a or psks_b:
            psk_success, psk_failed = await swap_identity_psks(api, network_id, slot_a, slot_b, psks_a, psks_b)
            results["success"].extend(psk_success)
            results["failed"].extend(psk_failed)

    return results


def load_defaults() -> dict:
    with open(DEFAULTS_FILE, encoding="utf-8") as f:
        return json.load(f)


def display_ssid_summary(ssids: list[dict]) -> None:
    cprint(f"\n  {'Slot':<5} {'Name':<34} {'Auth':<22} {'Status'}", Color.DIM)
    cprint(f"  {'─' * 72}", Color.DIM)
    for ssid in sorted(ssids, key=lambda s: s["number"]):
        status = f"{Color.GREEN}ON{Color.RESET}" if ssid["enabled"] else f"{Color.DIM}OFF{Color.RESET}"
        name = ssid.get("name", "?")
        auth = ssid.get("authMode", "?")
        cprint(f"  {ssid['number']:<5} {name:<34} {auth:<22} {status}", Color.RESET)
    print()


async def reset_ssid_slot(api: meraki.aio.AsyncDashboardAPI, network_id: str, slot: int) -> dict:
    defaults = load_defaults()
    default_config = defaults.get(str(slot))
    if not default_config:
        return {"success": [], "failed": [f"No default config for slot {slot}"]}

    cprint("  Creating safety backup...", Color.YELLOW)
    backup_path, _ = await backup_all_ssids(api, network_id)
    cprint(f"  Saved: {backup_path.name}", Color.GREEN)

    results = {"success": [], "failed": []}

    async with AsyncSpinner(f"Resetting slot {slot} to defaults"):

        async def _reset_resource(resource_name, resource_info):
            updater = getattr(api.wireless, resource_info["update"])
            payload = prepare_payload(resource_name, default_config.get(resource_name) or {})
            if not payload:
                return None
            try:
                await updater(network_id, str(slot), **payload)
                return ("success", f"{resource_name}: reset to default")
            except AsyncAPIError as e:
                return ("failed", f"{resource_name}: ({e.status})")

        reset_results = await asyncio.gather(*[_reset_resource(name, info) for name, info in SSID_SUB_RESOURCES.items()])
        for r in reset_results:
            if r:
                results[r[0]].append(r[1])

        current_psks = await fetch_identity_psks(api, network_id, slot)

        async def _delete_psk(psk):
            try:
                await api.wireless.deleteNetworkWirelessSsidIdentityPsk(network_id, str(slot), psk["id"])
                return ("success", f"identityPsks: deleted {psk['name']}")
            except AsyncAPIError as e:
                return ("failed", f"identityPsks: delete {psk['name']} ({e.status})")

        if current_psks:
            psk_results = await asyncio.gather(*[_delete_psk(p) for p in current_psks])
            for r in psk_results:
                results[r[0]].append(r[1])

    return results


def display_caveats() -> None:
    cprint("\n  Write Exclusions (not restored during swap/reset):", Color.YELLOW)
    cprint(f"  {'─' * 70}", Color.DIM)
    for resource, keys in WRITE_EXCLUDE_KEYS.items():
        for key, reason in keys.items():
            cprint(f"    {resource}.{key}", Color.RESET)
            cprint(f"      {reason}", Color.DIM)
    cprint(f"  {'─' * 70}\n", Color.DIM)


def display_menu() -> None:
    cprint("\n╔══════════════════════════════════════╗", Color.CYAN)
    cprint("║     Meraki SSID Management Tool      ║", Color.CYAN)
    cprint("╠══════════════════════════════════════╣", Color.CYAN)
    cprint("║  1. Backup SSIDs                     ║", Color.CYAN)
    cprint("║  2. Swap SSID Slots                  ║", Color.CYAN)
    cprint("║  3. Reset Slot to Default            ║", Color.CYAN)
    cprint("║  4. See Caveats                      ║", Color.CYAN)
    cprint("║  0. Exit                             ║", Color.CYAN)
    cprint("╚══════════════════════════════════════╝", Color.CYAN)


def display_report(title: str, results: dict) -> None:
    cprint(f"\n{'─' * 40}", Color.DIM)
    cprint(f"  {title}", Color.BOLD)
    cprint(f"{'─' * 40}", Color.DIM)
    for item in results.get("success", []):
        cprint(f"  ✓ {item}", Color.GREEN)
    for item in results.get("failed", []):
        cprint(f"  ✗ {item}", Color.RED)
    total = len(results.get("success", [])) + len(results.get("failed", []))
    passed = len(results.get("success", []))
    cprint(f"  {passed}/{total} operations succeeded", Color.DIM)
    cprint(f"{'─' * 40}\n", Color.DIM)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Meraki SSID Management Tool")
    parser.add_argument("-n", "--network-id", default=None, help="Network ID")
    parser.add_argument("-o", "--org-id", default=None, help="Organization ID")
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    network_id = args.network_id or os.environ.get("MERAKI_NETWORK_ID") or DEFAULT_NETWORK_ID
    if not network_id:
        cprint("Error: Network ID required (--network-id or MERAKI_NETWORK_ID)", Color.RED)
        sys.exit(1)

    async with meraki.aio.AsyncDashboardAPI(
        output_log=True, print_console=False, maximum_retries=10, smart_limiting=True, smart_limit_logging=True
    ) as api:
        while True:
            display_menu()
            choice = input(f"{Color.YELLOW}  Select option: {Color.RESET}").strip()

            if choice == "1":
                filepath, errors = await backup_all_ssids(api, network_id)
                results = {"success": [f"Saved to {filepath.name}"], "failed": []}
                if errors:
                    for name, msg in errors:
                        results["failed"].append(f"{name}: {msg}")
                display_report("Backup Complete", results)

            elif choice == "2":
                async with AsyncSpinner("Fetching current SSIDs"):
                    ssids = await api.wireless.getNetworkWirelessSsids(network_id)
                display_ssid_summary(ssids)

                backup_task = asyncio.create_task(backup_all_ssids(api, network_id))

                try:
                    slot_a = int(input(f"{Color.YELLOW}  First SSID slot (0-14): {Color.RESET}"))
                    slot_b = int(input(f"{Color.YELLOW}  Second SSID slot (0-14): {Color.RESET}"))
                except ValueError:
                    cprint("  Invalid input.", Color.RED)
                    backup_task.cancel()
                    continue
                if not (0 <= slot_a <= 14 and 0 <= slot_b <= 14 and slot_a != slot_b):
                    cprint("  Slots must be 0-14 and different.", Color.RED)
                    backup_task.cancel()
                    continue

                cprint("  Waiting for backup to complete...", Color.DIM)
                backup_path, _ = await backup_task
                cprint(f"  Saved: {backup_path.name}", Color.GREEN)

                results = await swap_ssid_slots(api, network_id, slot_a, slot_b)
                display_report(f"Swap: Slot {slot_a} <-> Slot {slot_b}", results)

            elif choice == "3":
                async with AsyncSpinner("Fetching current SSIDs"):
                    ssids = await api.wireless.getNetworkWirelessSsids(network_id)
                display_ssid_summary(ssids)
                try:
                    slot = int(input(f"{Color.YELLOW}  Slot to reset (0-14): {Color.RESET}"))
                except ValueError:
                    cprint("  Invalid input.", Color.RED)
                    continue
                if not 0 <= slot <= 14:
                    cprint("  Slot must be 0-14.", Color.RED)
                    continue
                results = await reset_ssid_slot(api, network_id, slot)
                display_report(f"Reset: Slot {slot}", results)

            elif choice == "4":
                display_caveats()

            elif choice == "0":
                cprint("Done.", Color.GREEN)
                break

            else:
                cprint("  Invalid choice.", Color.RED)


if __name__ == "__main__":
    asyncio.run(main())
