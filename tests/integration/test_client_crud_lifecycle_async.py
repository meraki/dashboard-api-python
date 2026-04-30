import platform
import random

import pytest
import pytest_asyncio

import meraki.aio

pytestmark = pytest.mark.asyncio(loop_scope="session")


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
    name = f"_GitHubAction Test Network {version_salt}"
    product_types = ["appliance", "switch", "wireless", "systemsManager", "sensor"]
    network_kwargs = {
        "tags": ["test_tag", "github", "shouldBeDeleted"],
        "timezone": "America/Los_Angeles",
    }

    created_network = await dashboard.organizations.createOrganizationNetwork(org_id, name, product_types, **network_kwargs)
    yield created_network


async def test_get_administered_identities_me(dashboard):
    me = await dashboard.administered.getAdministeredIdentitiesMe()
    assert me is not None
    assert isinstance(me["name"], str)
    assert me["authentication"]["api"]["key"]["created"]


async def test_get_organizations(dashboard):
    organizations = await dashboard.organizations.getOrganizations()
    assert organizations is not None
    assert len(organizations) > 0


async def test_get_organization(dashboard, org_id):
    organization = await dashboard.organizations.getOrganization(org_id)
    assert isinstance(organization, dict)
    assert isinstance(organization["id"], str)


async def test_create_network(dashboard, org_id, network, version_salt):
    assert network is not None
    assert network["name"] == f"_GitHubAction Test Network {version_salt}"


async def test_get_networks(dashboard, org_id):
    networks = await dashboard.organizations.getOrganizationNetworks(org_id)
    assert networks is not None
    assert len(networks) > 0


async def test_update_network(dashboard, network):
    new_name = f"{network['name']} new"
    updated_network_data = {
        "name": new_name,
        "tags": ["updated_test_tag", "github", "shouldBeDeleted"],
    }
    updated_network = await dashboard.networks.updateNetwork(network["id"], **updated_network_data)
    assert updated_network is not None
    assert updated_network["name"] == new_name


async def test_create_organization_policy_objects(dashboard, org_id, network, version_salt):
    policy_objects = [
        {
            "name": f"Ham {version_salt}".replace(".", "-"),
            "category": "network",
            "type": "cidr",
            "cidr": "10.51.1.253",
            "networkIds": [network["id"]],
        },
        {
            "name": f"Hamlet {version_salt}".replace(".", "-"),
            "category": "network",
            "type": "cidr",
            "cidr": "10.17.38.0/24",
        },
    ]

    for policy_object in policy_objects:
        new_object = await dashboard.organizations.createOrganizationPolicyObject(org_id, **policy_object)
        assert new_object is not None
        assert isinstance(new_object["id"], str)


async def test_get_organization_policy_objects(dashboard, org_id):
    policy_objects = await dashboard.organizations.getOrganizationPolicyObjects(org_id)
    assert policy_objects is not None
    assert len(policy_objects) > 0


async def test_get_network_appliance_l3_firewall_rules(dashboard, network):
    rules = await dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network["id"])
    assert rules is not None
    assert len(rules) > 0


async def test_update_network_appliance_vlan_settings(dashboard, network):
    response = await dashboard.appliance.updateNetworkApplianceVlansSettings(network["id"], vlansEnabled=True)
    assert response is not None
    assert response["vlansEnabled"]


async def test_create_network_appliance_vlan(dashboard, network):
    name = "testy_vlan"
    name2 = "home_base"
    new_vlans = [
        {"id": 51, "name": name, "subnet": "10.51.1.0/24", "applianceIp": "10.51.1.1"},
        {
            "id": 1738,
            "name": name2,
            "subnet": "10.17.38.0/24",
            "applianceIp": "10.17.38.1",
        },
    ]
    for vlan in new_vlans:
        new_vlan = await dashboard.appliance.createNetworkApplianceVlan(network["id"], **vlan)
        assert new_vlan is not None
        assert len(new_vlan) > 0
        assert new_vlan["name"] == vlan["name"]


async def test_update_l3_firewall_rules(dashboard, org_id, network, version_salt):
    all_policy_objects = await dashboard.organizations.getOrganizationPolicyObjects(org_id)

    policy_objects = [
        policy_object for policy_object in all_policy_objects if f"{version_salt}".replace(".", "-") in policy_object["name"]
    ]
    new_rules = {
        "rules": [
            {
                "comment": "HamByIP",
                "policy": "deny",
                "protocol": "tcp",
                "srcPort": "1738",
                "srcCidr": "VLAN(1738).*",
                "destPort": "1928",
                "destCidr": f"OBJ({policy_objects[0]['id']})",
                "syslogEnabled": False,
            },
            {
                "comment": "Ham",
                "policy": "deny",
                "protocol": "tcp",
                "srcPort": "Any",
                "srcCidr": f"OBJ({policy_objects[1]['id']})",
                "destPort": "Any",
                "destCidr": "11.1.1.1/32",
                "syslogEnabled": False,
            },
        ]
    }
    updated_rules = (await dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network["id"], **new_rules))[
        "rules"
    ]
    assert updated_rules is not None
    assert len(updated_rules) == 3
    assert updated_rules[0]["comment"] == "HamByIP"
    assert updated_rules[1]["comment"] == "Ham"


async def test_delete_policy_objects(dashboard, org_id, version_salt):
    all_policy_objects = await dashboard.organizations.getOrganizationPolicyObjects(org_id)

    for policy_object in all_policy_objects:
        if f"{version_salt}".replace(".", "-") in policy_object["name"]:
            response = await dashboard.organizations.deleteOrganizationPolicyObject(org_id, policy_object["id"])
            assert response is None

    remaining_policy_objects = await dashboard.organizations.getOrganizationPolicyObjects(org_id)
    missed_policy_objects = [
        policy_object
        for policy_object in remaining_policy_objects
        if f"{version_salt}".replace(".", "-") in policy_object["name"]
    ]
    assert len(missed_policy_objects) == 0


async def test_delete_network(dashboard, org_id, network):
    from meraki.api.batch.networks import ActionBatchNetworks

    action = ActionBatchNetworks().deleteNetwork(network["id"])

    batch = await dashboard.organizations.createOrganizationActionBatch(
        organizationId=org_id,
        actions=[action],
        confirmed=False,
        synchronous=False,
    )
    assert batch is not None
    assert batch["id"]

    response = await dashboard.organizations.updateOrganizationActionBatch(
        organizationId=org_id,
        actionBatchId=batch["id"],
        confirmed=True,
    )
    assert response is not None
