import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path

import meraki.aio
from meraki.exceptions import AsyncAPIError

TOOL_VERSION = "1.0.0"
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

# Keys to strip from sub-resource payloads before PUT (not predictable across networks)
WRITE_EXCLUDE_KEYS = {
    "splashSettings": ["sentryEnrollment"],
}


def prepare_payload(resource_name: str, raw: dict) -> dict:
    payload = {k: v for k, v in raw.items() if k not in PATH_PARAMS and v is not None}
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

    for slot, psks_to_delete in [(slot_a, psks_a), (slot_b, psks_b)]:
        for psk in psks_to_delete:
            try:
                await api.wireless.deleteNetworkWirelessSsidIdentityPsk(network_id, str(slot), psk["id"])
            except AsyncAPIError as e:
                failed.append(f"identityPsks: delete {psk['name']} from slot {slot} ({e.status})")

    for slot, psks_to_create in [(slot_b, psks_a), (slot_a, psks_b)]:
        for psk in psks_to_create:
            payload = {k: v for k, v in psk.items() if k in IDENTITY_PSK_CREATE_PARAMS and v is not None}
            if "name" not in payload or "groupPolicyId" not in payload:
                continue
            try:
                await api.wireless.createNetworkWirelessSsidIdentityPsk(network_id, str(slot), **payload)
                success.append(f"identityPsks: {psk['name']} -> slot {slot}")
            except AsyncAPIError as e:
                failed.append(f"identityPsks: create {psk['name']} on slot {slot} ({e.status})")

    return success, failed


async def fetch_ssid_sub_resources(api: meraki.aio.AsyncDashboardAPI, network_id: str, ssid_number: int) -> tuple[dict, list]:
    """Fetch all sub-resources for a single SSID slot (excludes main config)."""
    config = {}
    errors = []

    for resource_name, resource_info in SSID_SUB_RESOURCES.items():
        if resource_name == "main":
            continue
        getter = getattr(api.wireless, resource_info["get"])
        try:
            data = await getter(network_id, str(ssid_number))
            config[resource_name] = data
        except AsyncAPIError as e:
            if e.status in (400, 404):
                config[resource_name] = None
                errors.append((resource_name, str(e)))
            else:
                raise

    config["identityPsks"] = await fetch_identity_psks(api, network_id, ssid_number)

    return config, errors


async def fetch_ssid_full_config(api: meraki.aio.AsyncDashboardAPI, network_id: str, ssid_number: int) -> tuple[dict, list]:
    """Fetch main config + all sub-resources for a single SSID slot."""
    try:
        main = await api.wireless.getNetworkWirelessSsid(network_id, str(ssid_number))
    except AsyncAPIError as e:
        if e.status in (400, 404):
            main = None
        else:
            raise

    sub, errors = await fetch_ssid_sub_resources(api, network_id, ssid_number)
    sub["main"] = main
    return sub, errors


async def backup_all_ssids(api: meraki.aio.AsyncDashboardAPI, network_id: str) -> tuple[Path, list]:
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"{today}-{network_id}-ssids.jsonc"
    filepath = BACKUP_DIR / filename
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    all_ssids = {}
    all_errors = []

    async with AsyncSpinner("Backing up SSIDs"):
        ssids = await api.wireless.getNetworkWirelessSsids(network_id)
        for ssid in ssids:
            slot = ssid["number"]
            sub, errors = await fetch_ssid_sub_resources(api, network_id, slot)
            sub["main"] = ssid
            all_ssids[str(slot)] = sub
            all_errors.extend(errors)

    header = f"// SSID Backup - ssid_tool v{TOOL_VERSION}\n// {datetime.now().isoformat()}\n// Network: {network_id}\n"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header)
        json.dump(all_ssids, f, indent=2)

    return filepath, all_errors


async def swap_ssid_slots(
    api: meraki.aio.AsyncDashboardAPI,
    network_id: str,
    slot_a: int,
    slot_b: int,
) -> dict:
    cprint("  Creating safety backup...", Color.YELLOW)
    backup_path, _ = await backup_all_ssids(api, network_id)
    cprint(f"  Saved: {backup_path.name}", Color.GREEN)

    async with AsyncSpinner(f"Reading slots {slot_a} and {slot_b}"):
        config_a, _ = await fetch_ssid_full_config(api, network_id, slot_a)
        config_b, _ = await fetch_ssid_full_config(api, network_id, slot_b)

    results = {"success": [], "failed": []}

    async with AsyncSpinner("Swapping configurations"):
        for resource_name, resource_info in SSID_SUB_RESOURCES.items():
            updater = getattr(api.wireless, resource_info["update"])

            payload_a = prepare_payload(resource_name, config_a.get(resource_name) or {})
            payload_b = prepare_payload(resource_name, config_b.get(resource_name) or {})

            if payload_a:
                try:
                    await updater(network_id, str(slot_b), **payload_a)
                    results["success"].append(f"{resource_name}: slot {slot_a} -> slot {slot_b}")
                except AsyncAPIError as e:
                    results["failed"].append(f"{resource_name}: slot {slot_a} -> slot {slot_b} ({e.status})")

            if payload_b:
                try:
                    await updater(network_id, str(slot_a), **payload_b)
                    results["success"].append(f"{resource_name}: slot {slot_b} -> slot {slot_a}")
                except AsyncAPIError as e:
                    results["failed"].append(f"{resource_name}: slot {slot_b} -> slot {slot_a} ({e.status})")

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
        for resource_name, resource_info in SSID_SUB_RESOURCES.items():
            updater = getattr(api.wireless, resource_info["update"])
            payload = prepare_payload(resource_name, default_config.get(resource_name) or {})
            if payload:
                try:
                    await updater(network_id, str(slot), **payload)
                    results["success"].append(f"{resource_name}: reset to default")
                except AsyncAPIError as e:
                    results["failed"].append(f"{resource_name}: ({e.status})")

        current_psks = await fetch_identity_psks(api, network_id, slot)
        for psk in current_psks:
            try:
                await api.wireless.deleteNetworkWirelessSsidIdentityPsk(network_id, str(slot), psk["id"])
                results["success"].append(f"identityPsks: deleted {psk['name']}")
            except AsyncAPIError as e:
                results["failed"].append(f"identityPsks: delete {psk['name']} ({e.status})")

    return results


def display_caveats() -> None:
    cprint("\n  Write Exclusions (not restored during swap/reset):", Color.YELLOW)
    cprint(f"  {'─' * 50}", Color.DIM)
    for resource, keys in WRITE_EXCLUDE_KEYS.items():
        for key in keys:
            cprint(f"    {resource}.{key}", Color.RESET)
    cprint(f"\n  {'Reason:':<10} These attributes reference network-specific IDs", Color.DIM)
    cprint(f"  {'':>10} that are not portable across networks or slots.", Color.DIM)
    cprint(f"  {'─' * 50}\n", Color.DIM)


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
        output_log=False,
        print_console=False,
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
                try:
                    slot_a = int(input(f"{Color.YELLOW}  First SSID slot (0-14): {Color.RESET}"))
                    slot_b = int(input(f"{Color.YELLOW}  Second SSID slot (0-14): {Color.RESET}"))
                except ValueError:
                    cprint("  Invalid input.", Color.RED)
                    continue
                if not (0 <= slot_a <= 14 and 0 <= slot_b <= 14 and slot_a != slot_b):
                    cprint("  Slots must be 0-14 and different.", Color.RED)
                    continue
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
