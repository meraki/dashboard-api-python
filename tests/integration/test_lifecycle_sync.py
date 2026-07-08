import hashlib
import platform
import random
import time

import pytest

import meraki
from meraki.api.batch.networks import ActionBatchNetworks


def _salt():
    return hashlib.md5(str(time.time()).encode()).hexdigest()[:6]


@pytest.fixture(scope="session")
def version_salt():
    python_version = platform.python_version()
    salt = str(random.randint(1, 17381738))
    return f"{python_version} {salt}"


@pytest.fixture(scope="session")
def dashboard(api_key):
    return meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        network_delete_retry_wait_time=1000,
        maximum_retries=1000,
        caller="PythonSDKTest Cisco",
    )


@pytest.fixture(scope="session")
def network(dashboard, org_id, version_salt):
    name = f"_GitHubAction Test Lifecycle Network {version_salt}"
    product_types = ["wireless", "appliance"]
    network_kwargs = {
        "tags": ["test_tag", "github", "shouldBeDeleted"],
        "timezone": "America/Los_Angeles",
    }

    created_network = dashboard.organizations.createOrganizationNetwork(org_id, name, product_types, **network_kwargs)
    yield created_network

    action = ActionBatchNetworks().deleteNetwork(created_network["id"])
    for attempt in range(1, 6):
        delay = 2**attempt
        time.sleep(delay)
        batch = dashboard.organizations.createOrganizationActionBatch(
            organizationId=org_id, actions=[action], confirmed=True, synchronous=False
        )
        for _ in range(10):
            time.sleep(delay)
            status = dashboard.organizations.getOrganizationActionBatch(org_id, batch["id"])
            if status["status"]["completed"]:
                return
            if status["status"]["failed"]:
                break
        if attempt == 5:
            pytest.fail("Network cleanup action batch failed after 5 attempts")


def test_policy_object(dashboard, org_id):
    salt = _salt()
    obj = dashboard.organizations.createOrganizationPolicyObject(
        org_id, name=f"test-policy-object-{salt}", category="network", type="cidr", cidr="10.0.0.0/24"
    )
    assert isinstance(obj["id"], str)

    dashboard.organizations.updateOrganizationPolicyObject(org_id, obj["id"], name=f"test-policy-object-{salt}-r")
    dashboard.organizations.deleteOrganizationPolicyObject(org_id, obj["id"])


def test_policy_object_group(dashboard, org_id):
    salt = _salt()
    group = dashboard.organizations.createOrganizationPolicyObjectsGroup(
        org_id, name=f"test-policy-group-{salt}", category="NetworkObjectGroup"
    )
    assert isinstance(group["id"], str)

    dashboard.organizations.updateOrganizationPolicyObjectsGroup(org_id, group["id"], name=f"test-policy-group-{salt}-r")
    dashboard.organizations.deleteOrganizationPolicyObjectsGroup(org_id, group["id"])


def test_alerts_profile(dashboard, org_id):
    salt = _salt()
    profile = dashboard.organizations.createOrganizationAlertsProfile(
        org_id,
        type="wanUtilization",
        alertCondition={"duration": 60, "window": 600, "bit_rate_bps": 1000000, "interface": "wan1"},
        recipients={"emails": ["test@example.com"]},
        networkTags=["__all_tags__"],
        description=f"test-alert-profile-{salt}",
    )
    assert isinstance(profile["id"], str)

    dashboard.organizations.updateOrganizationAlertsProfile(org_id, profile["id"], description=f"test-alert-profile-{salt}-r")
    dashboard.organizations.deleteOrganizationAlertsProfile(org_id, profile["id"])


def test_group_policy(dashboard, network):
    salt = _salt()
    gp = dashboard.networks.createNetworkGroupPolicy(network["id"], name=f"test-group-policy-{salt}")
    assert "groupPolicyId" in gp

    dashboard.networks.updateNetworkGroupPolicy(network["id"], gp["groupPolicyId"], name=f"test-group-policy-{salt}-r")
    dashboard.networks.deleteNetworkGroupPolicy(network["id"], gp["groupPolicyId"])


def test_mqtt_broker(dashboard, network):
    salt = _salt()
    broker = dashboard.networks.createNetworkMqttBroker(
        network["id"], name=f"test-mqtt-broker-{salt}", host="mqtt.example.com", port=1883
    )
    assert isinstance(broker["id"], str)

    dashboard.networks.updateNetworkMqttBroker(network["id"], broker["id"], name=f"test-mqtt-broker-{salt}-r")
    dashboard.networks.deleteNetworkMqttBroker(network["id"], broker["id"])


def test_webhook_http_server(dashboard, network):
    salt = _salt()
    server = dashboard.networks.createNetworkWebhooksHttpServer(
        network["id"], name=f"test-webhook-server-{salt}", url="https://example.com/webhook"
    )
    assert isinstance(server["id"], str)

    dashboard.networks.updateNetworkWebhooksHttpServer(network["id"], server["id"], name=f"test-webhook-server-{salt}-r")
    dashboard.networks.deleteNetworkWebhooksHttpServer(network["id"], server["id"])


def test_webhook_payload_template(dashboard, network):
    salt = _salt()
    template = dashboard.networks.createNetworkWebhooksPayloadTemplate(
        network["id"],
        name=f"test-payload-template-{salt}",
        body='{"event": "{{alertType}}", "network": "{{networkName}}"}',
    )
    assert "payloadTemplateId" in template

    dashboard.networks.deleteNetworkWebhooksPayloadTemplate(network["id"], template["payloadTemplateId"])


def test_ssid(dashboard, network):
    ssid = dashboard.wireless.getNetworkWirelessSsid(network["id"], "0")
    original_name = ssid["name"]

    dashboard.wireless.updateNetworkWirelessSsid(network["id"], "0", name="test-ssid-renamed")
    dashboard.wireless.updateNetworkWirelessSsid(network["id"], "0", name=original_name)


def test_network_settings(dashboard, network):
    settings = dashboard.networks.getNetworkSettings(network["id"])
    original = settings.get("localStatusPageEnabled", True)

    dashboard.networks.updateNetworkSettings(network["id"], localStatusPageEnabled=not original)
    dashboard.networks.updateNetworkSettings(network["id"], localStatusPageEnabled=original)


def test_action_batch(dashboard, org_id, network):
    actions = [
        {
            "resource": f"/networks/{network['id']}/wireless/airMarshal/rules",
            "operation": "create",
            "body": {"type": "block", "match": {"string": f"test-rule-{i}", "type": "bssid"}},
        }
        for i in range(1, 4)
    ]

    batch = dashboard.organizations.createOrganizationActionBatch(org_id, actions, confirmed=True, synchronous=False)
    assert isinstance(batch["id"], str)

    for _ in range(30):
        time.sleep(2)
        status = dashboard.organizations.getOrganizationActionBatch(org_id, batch["id"])
        if status["status"]["completed"]:
            assert len(status["actions"]) == 3
            return
        if status["status"]["failed"]:
            pytest.fail(f"Action batch {batch['id']} failed")

    pytest.fail("Action batch did not complete within timeout")
