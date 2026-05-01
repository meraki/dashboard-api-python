import asyncio
import platform
import random

import pytest
import pytest_asyncio

import meraki.aio
from meraki.api.batch.organizations import ActionBatchOrganizations

pytestmark = pytest.mark.asyncio(loop_scope="module")


@pytest.fixture(scope="module")
def version_salt():
    python_version = platform.python_version()
    salt = str(random.randint(1, 17381738))
    return f"{python_version} {salt}"


@pytest_asyncio.fixture(scope="module", loop_scope="module")
async def dashboard(api_key):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=1000,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as d:
        yield d


async def _run_action_batch_async(dashboard, org_id, actions, max_attempts=5):
    for attempt in range(1, max_attempts + 1):
        delay = 2**attempt
        await asyncio.sleep(delay)

        batch = await dashboard.organizations.createOrganizationActionBatch(
            organizationId=org_id,
            actions=actions,
            confirmed=False,
            synchronous=False,
        )
        assert batch["id"]

        await asyncio.sleep(delay)
        await dashboard.organizations.updateOrganizationActionBatch(
            organizationId=org_id,
            actionBatchId=batch["id"],
            confirmed=True,
        )

        for _ in range(10):
            await asyncio.sleep(delay)
            status = await dashboard.organizations.getOrganizationActionBatch(
                organizationId=org_id,
                actionBatchId=batch["id"],
            )
            if status["status"]["completed"]:
                return
            if status["status"]["failed"]:
                break

        if attempt == max_attempts:
            pytest.fail(f"Action batch failed after {max_attempts} attempts")


@pytest_asyncio.fixture(scope="module", loop_scope="module")
async def firewall_rulesets(dashboard, org_id, version_salt):
    """Create 100 firewall rulesets via action batch, yield ruleset IDs, then delete."""
    batch_orgs = ActionBatchOrganizations()

    actions = [
        batch_orgs.createOrganizationPoliciesGlobalFirewallRuleset(
            organizationId=org_id,
            name=f"_test_ruleset_{version_salt}_{i:03d}",
        )
        for i in range(100)
    ]

    await _run_action_batch_async(dashboard, org_id, actions)

    rulesets = await dashboard.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
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
    await _run_action_batch_async(dashboard, org_id, delete_actions)


async def test_async_pagination_iterator_vs_legacy_firewall_rulesets(api_key, org_id, version_salt, firewall_rulesets):
    """Prove async iterator mode yields the same firewall rulesets as legacy await mode."""

    async def fetch_legacy():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=False,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as d:
            rulesets = await d.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
                org_id, name=f"_test_ruleset_{version_salt}", perPage=3, total_pages=-1
            )
            return {r["rulesetId"] for r in rulesets}

    async def fetch_iterator():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=True,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as d:
            ids = set()
            async for ruleset in d.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
                org_id, name=f"_test_ruleset_{version_salt}", perPage=3, total_pages=-1
            ):
                ids.add(ruleset["rulesetId"])
            return ids

    legacy_ids, iterator_ids = await asyncio.gather(fetch_legacy(), fetch_iterator())

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) >= 100


async def test_async_iterator_yields_dicts(api_key, org_id, version_salt, firewall_rulesets):
    """Each item from async iterator is a dict with rulesetId."""
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as d:
        async for ruleset in d.organizations.getOrganizationPoliciesGlobalFirewallRulesets(
            org_id, name=f"_test_ruleset_{version_salt}", perPage=3, total_pages=-1
        ):
            assert isinstance(ruleset, dict)
            assert "rulesetId" in ruleset
            break
