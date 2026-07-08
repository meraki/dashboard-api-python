import asyncio
import hashlib
import platform
import random
import time

import pytest
import pytest_asyncio

import meraki.aio
from meraki.api.batch.networks import ActionBatchNetworks

pytestmark = pytest.mark.asyncio(loop_scope="session")


def _salt():
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:6]


@pytest.fixture(scope="session")
def version_salt():
    python_version = platform.python_version()
    salt = str(random.randint(1, 17381738))
    return f"{python_version} {salt}"


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def dashboard(api_key):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        network_delete_retry_wait_time=1000,
        maximum_retries=1000,
        caller="PythonSDKTest Cisco",
    ) as dashboard:
        yield dashboard


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def network(dashboard, org_id, version_salt):
    name = f"_GitHubAction Test Lifecycle Network {version_salt}"
    product_types = ["wireless", "appliance"]
    network_kwargs = {
        "tags": ["test_tag", "github", "shouldBeDeleted"],
        "timezone": "America/Los_Angeles",
    }

    created_network = await dashboard.organizations.createOrganizationNetwork(org_id, name, product_types, **network_kwargs)
    yield created_network

    action = ActionBatchNetworks().deleteNetwork(created_network["id"])
    for attempt in range(1, 6):
        delay = 2**attempt
        await asyncio.sleep(delay)
        batch = await dashboard.organizations.createOrganizationActionBatch(
            organizationId=org_id, actions=[action], confirmed=True, synchronous=False
        )
        for _ in range(10):
            await asyncio.sleep(delay)
            status = await dashboard.organizations.getOrganizationActionBatch(org_id, batch["id"])
            if status["status"]["completed"]:
                return
            if status["status"]["failed"]:
                break
        if attempt == 5:
            pytest.fail("Network cleanup action batch failed after 5 attempts")


async def test_policy_object(dashboard, org_id):
    salt = _salt()
    obj = await dashboard.organizations.createOrganizationPolicyObject(
        org_id, name=f"test-policy-object-{salt}", category="network", type="cidr", cidr="10.0.0.0/24"
    )
    assert isinstance(obj["id"], str)

    await dashboard.organizations.updateOrganizationPolicyObject(org_id, obj["id"], name=f"test-policy-object-{salt}-r")
    await dashboard.organizations.deleteOrganizationPolicyObject(org_id, obj["id"])


async def test_policy_object_group(dashboard, org_id):
    salt = _salt()
    group = await dashboard.organizations.createOrganizationPolicyObjectsGroup(
        org_id, name=f"test-policy-group-{salt}", category="NetworkObjectGroup"
    )
    assert isinstance(group["id"], str)

    await dashboard.organizations.updateOrganizationPolicyObjectsGroup(org_id, group["id"], name=f"test-policy-group-{salt}-r")
    await dashboard.organizations.deleteOrganizationPolicyObjectsGroup(org_id, group["id"])


async def test_alerts_profile(dashboard, org_id):
    salt = _salt()
    profile = await dashboard.organizations.createOrganizationAlertsProfile(
        org_id,
        type="wanUtilization",
        alertCondition={"duration": 60, "window": 600, "bit_rate_bps": 1000000, "interface": "wan1"},
        recipients={"emails": ["test@example.com"]},
        networkTags=["__all_tags__"],
        description=f"test-alert-profile-{salt}",
    )
    assert isinstance(profile["id"], str)

    await dashboard.organizations.updateOrganizationAlertsProfile(
        org_id, profile["id"], description=f"test-alert-profile-{salt}-r"
    )
    await dashboard.organizations.deleteOrganizationAlertsProfile(org_id, profile["id"])


async def test_group_policy(dashboard, network):
    salt = _salt()
    gp = await dashboard.networks.createNetworkGroupPolicy(network["id"], name=f"test-group-policy-{salt}")
    assert "groupPolicyId" in gp

    await dashboard.networks.updateNetworkGroupPolicy(network["id"], gp["groupPolicyId"], name=f"test-group-policy-{salt}-r")
    await dashboard.networks.deleteNetworkGroupPolicy(network["id"], gp["groupPolicyId"])


async def test_mqtt_broker(dashboard, network):
    salt = _salt()
    broker = await dashboard.networks.createNetworkMqttBroker(
        network["id"], name=f"test-mqtt-broker-{salt}", host="mqtt.example.com", port=1883
    )
    assert isinstance(broker["id"], str)

    await dashboard.networks.updateNetworkMqttBroker(network["id"], broker["id"], name=f"test-mqtt-broker-{salt}-r")
    await dashboard.networks.deleteNetworkMqttBroker(network["id"], broker["id"])


async def test_webhook_http_server(dashboard, network):
    salt = _salt()
    server = await dashboard.networks.createNetworkWebhooksHttpServer(
        network["id"], name=f"test-webhook-server-{salt}", url="https://example.com/webhook"
    )
    assert isinstance(server["id"], str)

    await dashboard.networks.updateNetworkWebhooksHttpServer(network["id"], server["id"], name=f"test-webhook-server-{salt}-r")
    await dashboard.networks.deleteNetworkWebhooksHttpServer(network["id"], server["id"])


async def test_webhook_payload_template(dashboard, network):
    salt = _salt()
    template = await dashboard.networks.createNetworkWebhooksPayloadTemplate(
        network["id"],
        name=f"test-payload-template-{salt}",
        body='{"event": "{{alertType}}", "network": "{{networkName}}"}',
    )
    assert "payloadTemplateId" in template

    await dashboard.networks.deleteNetworkWebhooksPayloadTemplate(network["id"], template["payloadTemplateId"])


async def test_ssid(dashboard, network):
    ssid = await dashboard.wireless.getNetworkWirelessSsid(network["id"], "0")
    original_name = ssid["name"]

    await dashboard.wireless.updateNetworkWirelessSsid(network["id"], "0", name="test-ssid-renamed")
    await dashboard.wireless.updateNetworkWirelessSsid(network["id"], "0", name=original_name)


async def test_network_settings(dashboard, network):
    settings = await dashboard.networks.getNetworkSettings(network["id"])
    original = settings.get("localStatusPageEnabled", True)

    await dashboard.networks.updateNetworkSettings(network["id"], localStatusPageEnabled=not original)
    await dashboard.networks.updateNetworkSettings(network["id"], localStatusPageEnabled=original)


async def test_action_batch(dashboard, org_id, network):
    actions = [
        {
            "resource": f"/networks/{network['id']}/wireless/airMarshal/rules",
            "operation": "create",
            "body": {"type": "block", "match": {"string": f"test-rule-{i}", "type": "bssid"}},
        }
        for i in range(1, 4)
    ]

    batch = await dashboard.organizations.createOrganizationActionBatch(org_id, actions, confirmed=True, synchronous=False)
    assert isinstance(batch["id"], str)

    for _ in range(30):
        await asyncio.sleep(2)
        status = await dashboard.organizations.getOrganizationActionBatch(org_id, batch["id"])
        if status["status"]["completed"]:
            assert len(status["actions"]) == 3
            return
        if status["status"]["failed"]:
            pytest.fail(f"Action batch {batch['id']} failed")

    pytest.fail("Action batch did not complete within timeout")
