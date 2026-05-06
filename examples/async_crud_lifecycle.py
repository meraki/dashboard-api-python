"""Async CRUD lifecycle demo for the Meraki Dashboard API Python SDK.

Exercises create/update/delete workflows across org-level and network-level
resources (policy objects, alerts profiles, group policies, MQTT brokers,
webhooks, SSIDs, network settings, and action batches) using the async client.

All operations run concurrently per org and each resource is fully cleaned up
before the script exits.

Usage:
    export MERAKI_DASHBOARD_API_KEY=<your-key>
    python examples/async_crud_lifecycle.py
"""

import asyncio
import hashlib
import time
from functools import wraps

import meraki.aio


KEYWORD = "TestKeyword"


def _salt():
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:6]


def timed(fn):
    @wraps(fn)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = await fn(*args, **kwargs)
        elapsed = time.perf_counter() - start
        return (*result, elapsed)

    return wrapper


@timed
async def test_policy_object(dashboard, org_id, org_name):
    """Create -> rename -> delete a policy object."""
    salt = _salt()
    print(f"[{org_name}] Creating policy object...")
    obj = await dashboard.organizations.createOrganizationPolicyObject(
        org_id,
        name=f"test-policy-object-{salt}",
        category="network",
        type="cidr",
        cidr="10.0.0.0/24",
    )
    obj_id = obj["id"]
    print(f"[{org_name}] Created policy object: {obj_id}")

    print(f"[{org_name}] Renaming policy object...")
    await dashboard.organizations.updateOrganizationPolicyObject(org_id, obj_id, name=f"test-policy-object-{salt}-r")

    print(f"[{org_name}] Deleting policy object...")
    await dashboard.organizations.deleteOrganizationPolicyObject(org_id, obj_id)
    print(f"[{org_name}] Policy object deleted.")

    return ("policy_object", obj_id)


@timed
async def test_policy_object_group(dashboard, org_id, org_name):
    """Create -> rename -> delete a policy object group."""
    salt = _salt()
    print(f"[{org_name}] Creating policy object group...")
    group = await dashboard.organizations.createOrganizationPolicyObjectsGroup(
        org_id, name=f"test-policy-group-{salt}", category="NetworkObjectGroup"
    )
    group_id = group["id"]
    print(f"[{org_name}] Created policy object group: {group_id}")

    print(f"[{org_name}] Renaming policy object group...")
    await dashboard.organizations.updateOrganizationPolicyObjectsGroup(org_id, group_id, name=f"test-policy-group-{salt}-r")

    print(f"[{org_name}] Deleting policy object group...")
    await dashboard.organizations.deleteOrganizationPolicyObjectsGroup(org_id, group_id)
    print(f"[{org_name}] Policy object group deleted.")

    return ("policy_object_group", group_id)


@timed
async def test_alerts_profile(dashboard, org_id, org_name):
    """Create -> update -> delete an org alerts profile."""
    salt = _salt()
    print(f"[{org_name}] Creating alerts profile...")
    profile = await dashboard.organizations.createOrganizationAlertsProfile(
        org_id,
        type="wanUtilization",
        alertCondition={"duration": 60, "window": 600, "bit_rate_bps": 1000000, "interface": "wan1"},
        recipients={"emails": ["test@example.com"]},
        networkTags=["__all_tags__"],
        description=f"test-alert-profile-{salt}",
    )
    profile_id = profile["id"]
    print(f"[{org_name}] Created alerts profile: {profile_id}")

    print(f"[{org_name}] Updating alerts profile description...")
    await dashboard.organizations.updateOrganizationAlertsProfile(
        org_id, profile_id, description=f"test-alert-profile-{salt}-r"
    )

    print(f"[{org_name}] Deleting alerts profile...")
    await dashboard.organizations.deleteOrganizationAlertsProfile(org_id, profile_id)
    print(f"[{org_name}] Alerts profile deleted.")

    return ("alerts_profile", profile_id)


@timed
async def test_group_policy(dashboard, net_id, org_name):
    """Create -> update -> delete a group policy."""
    salt = _salt()
    print(f"[{org_name}] Creating group policy...")
    gp = await dashboard.networks.createNetworkGroupPolicy(net_id, name=f"test-group-policy-{salt}")
    gp_id = gp["groupPolicyId"]
    print(f"[{org_name}] Created group policy: {gp_id}")

    print(f"[{org_name}] Updating group policy...")
    await dashboard.networks.updateNetworkGroupPolicy(net_id, gp_id, name=f"test-group-policy-{salt}-r")

    print(f"[{org_name}] Deleting group policy...")
    await dashboard.networks.deleteNetworkGroupPolicy(net_id, gp_id)
    print(f"[{org_name}] Group policy deleted.")

    return ("group_policy", gp_id)


@timed
async def test_mqtt_broker(dashboard, net_id, org_name):
    """Create -> update -> delete an MQTT broker."""
    salt = _salt()
    print(f"[{org_name}] Creating MQTT broker...")
    broker = await dashboard.networks.createNetworkMqttBroker(
        net_id, name=f"test-mqtt-broker-{salt}", host="mqtt.example.com", port=1883
    )
    broker_id = broker["id"]
    print(f"[{org_name}] Created MQTT broker: {broker_id}")

    print(f"[{org_name}] Updating MQTT broker...")
    await dashboard.networks.updateNetworkMqttBroker(net_id, broker_id, name=f"test-mqtt-broker-{salt}-r")

    print(f"[{org_name}] Deleting MQTT broker...")
    await dashboard.networks.deleteNetworkMqttBroker(net_id, broker_id)
    print(f"[{org_name}] MQTT broker deleted.")

    return ("mqtt_broker", broker_id)


@timed
async def test_webhook_http_server(dashboard, net_id, org_name):
    """Create -> update -> delete a webhook HTTP server."""
    salt = _salt()
    print(f"[{org_name}] Creating webhook HTTP server...")
    server = await dashboard.networks.createNetworkWebhooksHttpServer(
        net_id, name=f"test-webhook-server-{salt}", url="https://example.com/webhook"
    )
    server_id = server["id"]
    print(f"[{org_name}] Created webhook HTTP server: {server_id}")

    print(f"[{org_name}] Updating webhook HTTP server...")
    await dashboard.networks.updateNetworkWebhooksHttpServer(net_id, server_id, name=f"test-webhook-server-{salt}-r")

    print(f"[{org_name}] Deleting webhook HTTP server...")
    await dashboard.networks.deleteNetworkWebhooksHttpServer(net_id, server_id)
    print(f"[{org_name}] Webhook HTTP server deleted.")

    return ("webhook_http_server", server_id)


@timed
async def test_webhook_payload_template(dashboard, net_id, org_name):
    """Create -> delete a webhook payload template."""
    salt = _salt()
    print(f"[{org_name}] Creating webhook payload template...")
    template = await dashboard.networks.createNetworkWebhooksPayloadTemplate(
        net_id,
        name=f"test-payload-template-{salt}",
        body='{"event": "{{alertType}}", "network": "{{networkName}}"}',
    )
    template_id = template["payloadTemplateId"]
    print(f"[{org_name}] Created payload template: {template_id}")
    print(f"[{org_name}]   body: {template.get('body', '')[:80]}")

    print(f"[{org_name}] Deleting payload template...")
    await dashboard.networks.deleteNetworkWebhooksPayloadTemplate(net_id, template_id)
    print(f"[{org_name}] Payload template deleted.")

    return ("webhook_payload_template", template_id)


@timed
async def test_ssid(dashboard, net_id, org_name):
    """Read -> update -> restore SSID 0."""
    print(f"[{org_name}] Reading SSID 0...")
    ssid = await dashboard.wireless.getNetworkWirelessSsid(net_id, "0")
    original_name = ssid["name"]
    print(f"[{org_name}] SSID 0 name: {original_name}")

    new_name = "test-ssid-renamed"
    print(f"[{org_name}] Updating SSID 0 name to '{new_name}'...")
    await dashboard.wireless.updateNetworkWirelessSsid(net_id, "0", name=new_name)

    print(f"[{org_name}] Restoring SSID 0 name to '{original_name}'...")
    await dashboard.wireless.updateNetworkWirelessSsid(net_id, "0", name=original_name)
    print(f"[{org_name}] SSID 0 restored.")

    return ("ssid_0", net_id)


@timed
async def test_network_settings(dashboard, net_id, org_name):
    """Read -> toggle -> restore network settings."""
    print(f"[{org_name}] Reading network settings...")
    settings = await dashboard.networks.getNetworkSettings(net_id)
    original = settings.get("localStatusPageEnabled", True)
    print(f"[{org_name}] localStatusPageEnabled = {original}")

    toggled = not original
    print(f"[{org_name}] Toggling localStatusPageEnabled to {toggled}...")
    await dashboard.networks.updateNetworkSettings(net_id, localStatusPageEnabled=toggled)

    print(f"[{org_name}] Restoring localStatusPageEnabled to {original}...")
    await dashboard.networks.updateNetworkSettings(net_id, localStatusPageEnabled=original)
    print(f"[{org_name}] Network settings restored.")

    return ("network_settings", net_id)


@timed
async def test_action_batch(dashboard, org_id, net_id, org_name):
    """Submit async action batch with 3 air marshal rules, poll to completion."""
    actions = [
        {
            "resource": f"/networks/{net_id}/wireless/airMarshal/rules",
            "operation": "create",
            "body": {
                "type": "block",
                "match": {"string": f"test-rule-{i}", "type": "bssid"},
            },
        }
        for i in range(1, 4)
    ]

    print(f"[{org_name}] Submitting action batch with 3 air marshal rules...")
    batch = await dashboard.organizations.createOrganizationActionBatch(org_id, actions, confirmed=True, synchronous=False)
    batch_id = batch["id"]
    print(f"[{org_name}] Action batch submitted: {batch_id}")

    while True:
        status = await dashboard.organizations.getOrganizationActionBatch(org_id, batch_id)
        if status["status"]["completed"]:
            break
        if status["status"]["failed"]:
            raise RuntimeError(f"Action batch {batch_id} failed in org {org_id}")
        await asyncio.sleep(1)

    print(f"[{org_name}] Action batch completed. Rules created:")
    for action in status["actions"]:
        rule = action.get("body", {})
        print(f"  - type={rule.get('type')}, match={rule.get('match')}")

    return ("action_batch", batch_id)


async def process_org(dashboard, org):
    org_id = org["id"]
    org_name = org["name"]

    # Create network (needed for network-level tests)
    print(f"[{org_name}] Creating wireless network...")
    network = await dashboard.organizations.createOrganizationNetwork(
        org_id,
        name=f"test-airmarshal-network-{_salt()}",
        productTypes=["wireless"],
    )
    net_id = network["id"]
    print(f"[{org_name}] Created network: {net_id}")

    # Run all tests concurrently
    results = await asyncio.gather(
        # Org-level (no network dependency)
        test_policy_object(dashboard, org_id, org_name),
        test_policy_object_group(dashboard, org_id, org_name),
        test_alerts_profile(dashboard, org_id, org_name),
        # Network-level
        test_group_policy(dashboard, net_id, org_name),
        test_mqtt_broker(dashboard, net_id, org_name),
        test_webhook_http_server(dashboard, net_id, org_name),
        test_webhook_payload_template(dashboard, net_id, org_name),
        test_ssid(dashboard, net_id, org_name),
        test_network_settings(dashboard, net_id, org_name),
        test_action_batch(dashboard, org_id, net_id, org_name),
    )

    # Delete the network
    print(f"[{org_name}] Deleting network {net_id}...")
    await dashboard.networks.deleteNetwork(net_id)
    print(f"[{org_name}] Network deleted.")

    return {
        "org_id": org_id,
        "network_id": net_id,
        "resources": list(results),
    }


async def main():
    total_start = time.perf_counter()

    async with meraki.aio.AsyncDashboardAPI(suppress_logging=True) as dashboard:
        orgs = await dashboard.organizations.getOrganizations()
        targets = [o for o in orgs if KEYWORD in o["name"]]

        results = await asyncio.gather(*(process_org(dashboard, org) for org in targets))

    total_elapsed = time.perf_counter() - total_start

    print("\n" + "=" * 60)
    print("Resources touched:")
    print("=" * 60)
    for r in results:
        print(f"\nOrg: {r['org_id']}")
        print(f"  Network: {r['network_id']}")
        for resource_type, resource_id, elapsed in r["resources"]:
            print(f"  {resource_type}: {resource_id} ({elapsed:.2f}s)")

    print("\n" + "=" * 60)
    print("Timing summary:")
    print("=" * 60)
    for r in results:
        print(f"\nOrg: {r['org_id']}")
        for resource_type, _, elapsed in r["resources"]:
            print(f"  {resource_type:30s} {elapsed:6.2f}s")
    print(f"\nTotal elapsed: {total_elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
