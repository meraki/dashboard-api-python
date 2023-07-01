import pytest
import meraki


@pytest.fixture(scope='session')
def api_key(pytestconfig):
    # Replace with a valid Meraki API key
    return pytestconfig.getoption("apikey")


@pytest.fixture(scope='session')
def dashboard(api_key):
    return meraki.DashboardAPI(api_key, suppress_logging=True)


@pytest.fixture(scope='session')
def org_id(pytestconfig):
    # Replace with a valid organization id
    return pytestconfig.getoption("o")


@pytest.fixture(scope='session')
def network(dashboard, org_id):
    # Replace with network details
    name = "_GitHubAction Test Network"
    producttypes = ["appliance", "switch", "wireless", "systemsManager", "sensor"]
    network_kwargs = {
        "tags": ["test_tag", "github", "shouldBeDeleted"],
        "timezone": "America/Los_Angeles"
    }

    created_network = dashboard.organizations.createOrganizationNetwork(org_id, name, producttypes, **network_kwargs)
    yield created_network


def test_get_administered_identities_me(dashboard):
    me = dashboard.administered.getAdministeredIdentitiesMe()
    assert me is not None
    assert isinstance(me["name"], str)
    assert me["authentication"]["api"]["key"]["created"]


def test_get_organizations(dashboard):
    organizations = dashboard.organizations.getOrganizations()
    assert organizations is not None
    assert len(organizations) > 0


def test_get_organization(dashboard, org_id):
    organization = dashboard.organizations.getOrganization(org_id)
    assert isinstance(organization, dict)
    assert isinstance(organization["id"], str)


def test_create_network(dashboard, org_id, network):
    assert network is not None
    assert network['name'] == "_GitHubAction Test Network"


def test_get_networks(dashboard, org_id):
    networks = dashboard.organizations.getOrganizationNetworks(org_id)
    assert networks is not None
    assert len(networks) > 0


def test_update_network(dashboard, network):
    # Replace with updated network details
    new_name = "_GitHubAction Updated Test Network"
    updated_network_data = {
        "name": new_name,
        "tags": ["updated_test_tag", "github", "shouldBeDeleted"]
    }
    updated_network = dashboard.networks.updateNetwork(network['id'], **updated_network_data)
    assert updated_network is not None
    assert updated_network['name'] == new_name


def test_create_organization_policy_objects(dashboard, org_id, network):
    policy_objects = [
        {
            "name": "Ham",
            "category": "network",
            "type": "cidr",
            "cidr": "10.51.1.253",
            "networkIds": [network["id"]]
        },
        {
            "name": "Hamlet",
            "category": "network",
            "type": "cidr",
            "cidr": "10.17.38.0/24"
        }
    ]

    for policy_object in policy_objects:
        new_object = dashboard.organizations.createOrganizationPolicyObject(org_id, **policy_object)
        assert new_object is not None
        assert isinstance(new_object["id"], str)


def test_get_organization_policy_objects(dashboard, org_id):
    policy_objects = dashboard.organizations.getOrganizationPolicyObjects(org_id)
    assert policy_objects is not None
    assert len(policy_objects) > 0


def test_get_network_appliance_l3_firewall_rules(dashboard, network):
    rules = dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(network["id"])
    assert rules is not None
    assert len(rules) > 0


def test_update_network_appliance_vlan_settings(dashboard, network):
    response = dashboard.appliance.updateNetworkApplianceVlansSettings(network["id"], vlansEnabled=True)
    assert response is not None
    assert response["vlansEnabled"]


def test_create_network_appliance_vlan(dashboard, network):
    name = "testy_vlan"
    name2 = "home_base"
    new_vlans = [{
        "id": 51,
        "name": name,
        "subnet": "10.51.1.0/24",
        "applianceIp": "10.51.1.1"
        },
        {
            "id": 1738,
            "name": name2,
            "subnet": "10.17.38.0/24",
            "applianceIp": "10.17.38.1"
        }
    ]
    for vlan in new_vlans:
        new_vlan = dashboard.appliance.createNetworkApplianceVlan(network["id"], **vlan)
        assert new_vlan is not None
        assert len(new_vlan) > 0
        assert new_vlan["name"] == vlan["name"]


def test_update_l3_firewall_rules(dashboard, org_id, network):
    policy_objects = dashboard.organizations.getOrganizationPolicyObjects(org_id)
    print(f'policy_objects length is {len(policy_objects)}')
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
                "syslogEnabled": False
            },
            {
                "comment": "Ham",
                "policy": "deny",
                "protocol": "tcp",
                "srcPort": "Any",
                "srcCidr": f"OBJ({policy_objects[1]['id']})",
                "destPort": "Any",
                "destCidr": "11.1.1.1/32",
                "syslogEnabled": False
            }
        ]
    }
    updated_rules = dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(network["id"],
                                                                                      **new_rules)["rules"]
    assert updated_rules is not None
    print(f'new_rules["rules"] length is {len(new_rules["rules"])}')
    print(f'updated_rules length is {len(updated_rules)}')
    assert len(updated_rules) == 3
    assert updated_rules[0]["comment"] == "HamByIP"
    assert updated_rules[1]["comment"] == "Ham"


def test_delete_policy_objects(dashboard, org_id):
    policy_objects = dashboard.organizations.getOrganizationPolicyObjects(org_id)
    for policy_object in policy_objects:
        response = dashboard.organizations.deleteOrganizationPolicyObject(org_id, policy_object["id"])
        assert response is None


def test_delete_network(dashboard, network):
    response = dashboard.networks.deleteNetwork(network['id'])
    assert response is None
