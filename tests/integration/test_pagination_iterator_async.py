import asyncio

import pytest
import pytest_asyncio

import meraki.aio
from meraki.api.batch.wireless import ActionBatchWireless

pytestmark = pytest.mark.asyncio(loop_scope="module")


@pytest_asyncio.fixture(scope="module", loop_scope="module")
async def dashboard(api_key):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as d:
        yield d


@pytest_asyncio.fixture(scope="module", loop_scope="module")
async def network(dashboard, org_id):
    created = await dashboard.organizations.createOrganizationNetwork(
        org_id,
        "_PaginationIteratorTest Async Network",
        ["wireless"],
        tags=["test_tag", "pagination", "shouldBeDeleted"],
        timezone="America/Los_Angeles",
    )
    yield created
    from meraki.api.batch.networks import ActionBatchNetworks

    action = ActionBatchNetworks().deleteNetwork(created["id"])
    await _run_action_batch_async(dashboard, org_id, [action])


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
async def air_marshal_rules(dashboard, org_id, network):
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

    await _run_action_batch_async(dashboard, org_id, actions)

    rules = await dashboard.wireless.getOrganizationWirelessAirMarshalRules(org_id, networkIds=[network_id], total_pages=-1)
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
    await _run_action_batch_async(dashboard, org_id, delete_actions)


async def test_async_pagination_iterator_vs_legacy_air_marshal_rules(api_key, org_id, network, air_marshal_rules):
    """Prove async iterator mode yields the same air marshal rules as legacy await mode."""
    network_id = network["id"]

    async def fetch_legacy():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=False,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as dashboard:
            rules = await dashboard.wireless.getOrganizationWirelessAirMarshalRules(
                org_id, networkIds=[network_id], perPage=3, total_pages=-1
            )
            return {r["ruleId"] for r in rules}

    async def fetch_iterator():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=True,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as dashboard:
            ids = set()
            async for rule in dashboard.wireless.getOrganizationWirelessAirMarshalRules(
                org_id, networkIds=[network_id], perPage=3, total_pages=-1
            ):
                ids.add(rule["ruleId"])
            return ids

    legacy_ids, iterator_ids = await asyncio.gather(fetch_legacy(), fetch_iterator())

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) >= 100


async def test_async_iterator_yields_dicts(api_key, org_id, network, air_marshal_rules):
    """Each item from async iterator is a dict with ruleId."""
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as dashboard:
        async for rule in dashboard.wireless.getOrganizationWirelessAirMarshalRules(
            org_id, networkIds=[network["id"]], perPage=3, total_pages=-1
        ):
            assert isinstance(rule, dict)
            assert "ruleId" in rule
            break
