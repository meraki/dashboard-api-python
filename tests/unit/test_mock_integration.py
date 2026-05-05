"""
Mock-server version of the integration test suite.
Exercises the same DashboardAPI CRUD flows as the live integration tests
but against canned HTTP responses, so it can run in CI without API keys.
"""

import httpx
import pytest
import respx

import meraki

BASE = "https://api.meraki.com/api/v1"
ORG_ID = "123456"
NETWORK_ID = "N_123456"
POLICY_OBJ_1_ID = "PO_1"
POLICY_OBJ_2_ID = "PO_2"


@pytest.fixture
def mock_api():
    with respx.mock(assert_all_mocked=False) as rsps:
        yield rsps


@pytest.fixture
def dashboard(mock_api):
    return meraki.DashboardAPI(
        "fake_key_1234567890123456789012345678901234567890",
        suppress_logging=True,
        caller="MockTest MockVendor",
        maximum_retries=1,
    )


# --- /administered/identities/me ---


class TestGetAdministeredIdentitiesMe:
    def test_returns_identity(self, mock_api, dashboard):
        mock_api.get(f"{BASE}/administered/identities/me").mock(
            return_value=httpx.Response(
                200,
                json={
                    "name": "Test User",
                    "email": "test@example.com",
                    "authentication": {"api": {"key": {"created": True}}},
                },
            )
        )
        me = dashboard.administered.getAdministeredIdentitiesMe()
        assert me is not None
        assert isinstance(me["name"], str)
        assert me["authentication"]["api"]["key"]["created"]


# --- /organizations ---


class TestOrganizations:
    def test_get_organizations(self, mock_api, dashboard):
        mock_api.get(f"{BASE}/organizations").mock(
            return_value=httpx.Response(
                200, json=[{"id": ORG_ID, "name": "Test Org"}]
            )
        )
        orgs = dashboard.organizations.getOrganizations()
        assert orgs is not None
        assert len(orgs) > 0

    def test_get_organization(self, mock_api, dashboard):
        mock_api.get(f"{BASE}/organizations/{ORG_ID}").mock(
            return_value=httpx.Response(
                200, json={"id": ORG_ID, "name": "Test Org"}
            )
        )
        org = dashboard.organizations.getOrganization(ORG_ID)
        assert isinstance(org, dict)
        assert isinstance(org["id"], str)


# --- /organizations/{orgId}/networks ---


class TestNetworks:
    def test_create_network(self, mock_api, dashboard):
        mock_api.post(f"{BASE}/organizations/{ORG_ID}/networks").mock(
            return_value=httpx.Response(
                201,
                json={
                    "id": NETWORK_ID,
                    "name": "_Test Network",
                    "productTypes": ["appliance", "switch", "wireless"],
                    "tags": ["test_tag"],
                    "timeZone": "America/Los_Angeles",
                },
            )
        )
        network = dashboard.organizations.createOrganizationNetwork(
            ORG_ID,
            "_Test Network",
            ["appliance", "switch", "wireless"],
            tags=["test_tag"],
            timezone="America/Los_Angeles",
        )
        assert network is not None
        assert network["name"] == "_Test Network"

    def test_get_organization_networks(self, mock_api, dashboard):
        mock_api.get(f"{BASE}/organizations/{ORG_ID}/networks").mock(
            return_value=httpx.Response(
                200, json=[{"id": NETWORK_ID, "name": "_Test Network"}]
            )
        )
        networks = dashboard.organizations.getOrganizationNetworks(ORG_ID)
        assert networks is not None
        assert len(networks) > 0

    def test_update_network(self, mock_api, dashboard):
        mock_api.put(f"{BASE}/networks/{NETWORK_ID}").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": NETWORK_ID,
                    "name": "_Test Network new",
                    "tags": ["updated_test_tag"],
                },
            )
        )
        updated = dashboard.networks.updateNetwork(
            NETWORK_ID, name="_Test Network new", tags=["updated_test_tag"]
        )
        assert updated is not None
        assert updated["name"] == "_Test Network new"

    def test_delete_network(self, mock_api, dashboard):
        mock_api.delete(f"{BASE}/networks/{NETWORK_ID}").mock(
            return_value=httpx.Response(204)
        )
        result = dashboard.networks.deleteNetwork(NETWORK_ID)
        assert result is None


# --- /organizations/{orgId}/policyObjects ---


class TestPolicyObjects:
    def test_create_policy_object(self, mock_api, dashboard):
        mock_api.post(f"{BASE}/organizations/{ORG_ID}/policyObjects").mock(
            return_value=httpx.Response(
                201,
                json={
                    "id": POLICY_OBJ_1_ID,
                    "name": "Ham",
                    "category": "network",
                    "type": "cidr",
                    "cidr": "10.51.1.253",
                },
            )
        )
        obj = dashboard.organizations.createOrganizationPolicyObject(
            ORG_ID, name="Ham", category="network", type="cidr", cidr="10.51.1.253"
        )
        assert obj is not None
        assert isinstance(obj["id"], str)

    def test_get_policy_objects(self, mock_api, dashboard):
        mock_api.get(f"{BASE}/organizations/{ORG_ID}/policyObjects").mock(
            return_value=httpx.Response(
                200,
                json=[
                    {"id": POLICY_OBJ_1_ID, "name": "Ham"},
                    {"id": POLICY_OBJ_2_ID, "name": "Hamlet"},
                ],
            )
        )
        objs = dashboard.organizations.getOrganizationPolicyObjects(ORG_ID)
        assert objs is not None
        assert len(objs) > 0

    def test_delete_policy_object(self, mock_api, dashboard):
        mock_api.delete(
            f"{BASE}/organizations/{ORG_ID}/policyObjects/{POLICY_OBJ_1_ID}"
        ).mock(return_value=httpx.Response(204))
        result = dashboard.organizations.deleteOrganizationPolicyObject(
            ORG_ID, POLICY_OBJ_1_ID
        )
        assert result is None


# --- /networks/{networkId}/appliance ---


class TestAppliance:
    def test_get_l3_firewall_rules(self, mock_api, dashboard):
        mock_api.get(
            f"{BASE}/networks/{NETWORK_ID}/appliance/firewall/l3FirewallRules"
        ).mock(
            return_value=httpx.Response(
                200,
                json={
                    "rules": [
                        {
                            "comment": "Default rule",
                            "policy": "allow",
                            "protocol": "Any",
                        }
                    ]
                },
            )
        )
        rules = dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(
            NETWORK_ID
        )
        assert rules is not None
        assert len(rules) > 0

    def test_update_vlan_settings(self, mock_api, dashboard):
        mock_api.put(
            f"{BASE}/networks/{NETWORK_ID}/appliance/vlans/settings"
        ).mock(return_value=httpx.Response(200, json={"vlansEnabled": True}))
        resp = dashboard.appliance.updateNetworkApplianceVlansSettings(
            NETWORK_ID, vlansEnabled=True
        )
        assert resp is not None
        assert resp["vlansEnabled"]

    def test_create_vlan(self, mock_api, dashboard):
        mock_api.post(f"{BASE}/networks/{NETWORK_ID}/appliance/vlans").mock(
            return_value=httpx.Response(
                201,
                json={
                    "id": "51",
                    "name": "testy_vlan",
                    "subnet": "10.51.1.0/24",
                    "applianceIp": "10.51.1.1",
                },
            )
        )
        vlan = dashboard.appliance.createNetworkApplianceVlan(
            NETWORK_ID,
            id="51",
            name="testy_vlan",
            subnet="10.51.1.0/24",
            applianceIp="10.51.1.1",
        )
        assert vlan is not None
        assert vlan["name"] == "testy_vlan"

    def test_update_l3_firewall_rules(self, mock_api, dashboard):
        mock_api.put(
            f"{BASE}/networks/{NETWORK_ID}/appliance/firewall/l3FirewallRules"
        ).mock(
            return_value=httpx.Response(
                200,
                json={
                    "rules": [
                        {
                            "comment": "HamByIP",
                            "policy": "deny",
                            "protocol": "tcp",
                        },
                        {"comment": "Ham", "policy": "deny", "protocol": "tcp"},
                        {
                            "comment": "Default rule",
                            "policy": "allow",
                            "protocol": "Any",
                        },
                    ]
                },
            )
        )
        updated = dashboard.appliance.updateNetworkApplianceFirewallL3FirewallRules(
            NETWORK_ID,
            rules=[
                {
                    "comment": "HamByIP",
                    "policy": "deny",
                    "protocol": "tcp",
                    "srcPort": "1738",
                    "srcCidr": "VLAN(1738).*",
                    "destPort": "1928",
                    "destCidr": "OBJ(PO_1)",
                    "syslogEnabled": False,
                },
                {
                    "comment": "Ham",
                    "policy": "deny",
                    "protocol": "tcp",
                    "srcPort": "Any",
                    "srcCidr": "OBJ(PO_2)",
                    "destPort": "Any",
                    "destCidr": "11.1.1.1/32",
                    "syslogEnabled": False,
                },
            ],
        )
        assert updated["rules"] is not None
        assert len(updated["rules"]) == 3
        assert updated["rules"][0]["comment"] == "HamByIP"
        assert updated["rules"][1]["comment"] == "Ham"
