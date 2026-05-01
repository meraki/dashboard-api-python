import platform
import random
import time

import pytest

import meraki
from meraki.api.batch.organizations import ActionBatchOrganizations


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
        maximum_retries=1000,
        caller="PythonSDKTestPaginationIterator Cisco",
    )


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
def firewall_rulesets(dashboard, org_id, version_salt):
    """Create 100 firewall rulesets via action batch, yield ruleset IDs, then delete."""
    batch_orgs = ActionBatchOrganizations()

    actions = [
        batch_orgs.createOrganizationPoliciesGlobalFirewallRuleset(
            organizationId=org_id,
            name=f"_test_ruleset_{version_salt}_{i:03d}",
        )
        for i in range(100)
    ]

    _run_action_batch(dashboard, org_id, actions)

    rulesets = dashboard.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
        org_id, name=f"_test_ruleset_{version_salt}", total_pages=-1
    )
    ruleset_ids = [r["rulesetId"] for r in rulesets]
    assert len(ruleset_ids) >= 100

    yield ruleset_ids

    delete_actions = [
        batch_orgs.deleteOrganizationPoliciesGlobalFirewallRuleset(
            organizationId=org_id,
            rulesetId=ruleset_id,
        )
        for ruleset_id in ruleset_ids
    ]
    _run_action_batch(dashboard, org_id, delete_actions)


def test_pagination_iterator_vs_legacy_firewall_rulesets(api_key, org_id, version_salt, firewall_rulesets):
    """Prove iterator mode yields the same firewall rulesets as legacy mode."""
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

    legacy_rulesets = dashboard_legacy.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
        org_id, name=f"_test_ruleset_{version_salt}", perPage=3, total_pages=-1
    )
    legacy_ids = {r["rulesetId"] for r in legacy_rulesets}

    iterator_ids = set()
    for ruleset in dashboard_iterator.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
        org_id, name=f"_test_ruleset_{version_salt}", perPage=3, total_pages=-1
    ):
        iterator_ids.add(ruleset["rulesetId"])

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) >= 100


def test_pagination_iterator_yields_dicts(api_key, org_id, version_salt, firewall_rulesets):
    """Each yielded item from the iterator is a dict with rulesetId."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    for ruleset in dashboard.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
        org_id, name=f"_test_ruleset_{version_salt}", perPage=3, total_pages=-1
    ):
        assert isinstance(ruleset, dict)
        assert "rulesetId" in ruleset
        break
