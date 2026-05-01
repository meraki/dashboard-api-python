import platform
import random
import time

import pytest

import meraki
from meraki.api.batch.wireless import ActionBatchWireless


@pytest.fixture(scope="module")
def version_salt():
    python_version = platform.python_version()
    salt = str(random.randint(1, 17381738))
    return f"{python_version} {salt}"


@pytest.fixture(scope="module")
def dashboard(api_key):
    return meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        caller="PythonSDKTestPaginationIterator Cisco",
    )


@pytest.fixture(scope="module")
def network(dashboard, org_id, version_salt):
    created = dashboard.organizations.createOrganizationNetwork(
        org_id,
        f"_GitHubAction PaginationIteratorTest {version_salt}",
        ["wireless"],
        tags=["test_tag", "pagination", "shouldBeDeleted"],
        timezone="America/Los_Angeles",
    )
    yield created
    _delete_network_with_retry(dashboard, org_id, created["id"])


def _delete_network_with_retry(dashboard, org_id, network_id):
    from meraki.api.batch.networks import ActionBatchNetworks

    action = ActionBatchNetworks().deleteNetwork(network_id)
    _run_action_batch(dashboard, org_id, [action])


def _run_action_batch(dashboard, org_id, actions, max_attempts=5):
    for attempt in range(1, max_attempts + 1):
        delay = 2**attempt
        time.sleep(delay)

        batch = dashboard.organizations.createOrganizationActionBatch(
            organizationId=org_id,
            actions=actions,
            confirmed=False,
            synchronous=False,
        )
        assert batch["id"]

        time.sleep(delay)
        dashboard.organizations.updateOrganizationActionBatch(
            organizationId=org_id,
            actionBatchId=batch["id"],
            confirmed=True,
        )

        for _ in range(10):
            time.sleep(delay)
            status = dashboard.organizations.getOrganizationActionBatch(
                organizationId=org_id,
                actionBatchId=batch["id"],
            )
            if status["status"]["completed"]:
                return
            if status["status"]["failed"]:
                break

        if attempt == max_attempts:
            pytest.fail(f"Action batch failed after {max_attempts} attempts")


@pytest.fixture(scope="module")
def air_marshal_rules(dashboard, org_id, network):
    """Create 100 air marshal rules via action batch, yield rule IDs, then delete."""
    network_id = network["id"]
    batch_wireless = ActionBatchWireless()

    actions = [
        batch_wireless.createNetworkWirelessAirMarshalRule(
            networkId=network_id,
            type="allow",
            match={"type": "bssid", "string": f"aa:bb:cc:dd:{i // 256:02x}:{i % 256:02x}"},
        )
        for i in range(100)
    ]

    _run_action_batch(dashboard, org_id, actions)

    rules = dashboard.wireless.getOrganizationWirelessAirMarshalRules(org_id, networkIds=[network_id], total_pages=-1)
    rule_ids = [r["ruleId"] for r in rules]
    assert len(rule_ids) >= 100

    yield rule_ids

    delete_actions = [
        batch_wireless.deleteNetworkWirelessAirMarshalRule(
            networkId=network_id,
            ruleId=rule_id,
        )
        for rule_id in rule_ids
    ]
    _run_action_batch(dashboard, org_id, delete_actions)


def test_pagination_iterator_vs_legacy_air_marshal_rules(api_key, org_id, network, air_marshal_rules):
    """Prove iterator mode yields the same air marshal rules as legacy mode."""
    network_id = network["id"]

    dashboard_iterator = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    )
    dashboard_legacy = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=False,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    legacy_rules = dashboard_legacy.wireless.getOrganizationWirelessAirMarshalRules(
        org_id, networkIds=[network_id], perPage=3, total_pages=-1
    )
    legacy_ids = {r["ruleId"] for r in legacy_rules}

    iterator_ids = set()
    for rule in dashboard_iterator.wireless.getOrganizationWirelessAirMarshalRules(
        org_id, networkIds=[network_id], perPage=3, total_pages=-1
    ):
        iterator_ids.add(rule["ruleId"])

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) >= 100


def test_pagination_iterator_yields_dicts(api_key, org_id, network, air_marshal_rules):
    """Each yielded item from the iterator is a dict with ruleId."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    for rule in dashboard.wireless.getOrganizationWirelessAirMarshalRules(
        org_id, networkIds=[network["id"]], perPage=3, total_pages=-1
    ):
        assert isinstance(rule, dict)
        assert "ruleId" in rule
        break


def test_get_organization_api_requests(api_key, org_id):
    """getOrganizationApiRequests returns records with expected fields."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    requests_log = dashboard.organizations.getOrganizationApiRequests(org_id, timespan=900, total_pages=-1)
    assert isinstance(requests_log, list)

    if len(requests_log) > 0:
        record = requests_log[0]
        expected_keys = [
            "method",
            "host",
            "path",
            "ts",
            "responseCode",
            "sourceIp",
            "userAgent",
        ]
        for key in expected_keys:
            assert key in record, f"Expected key '{key}' missing from API request record"
