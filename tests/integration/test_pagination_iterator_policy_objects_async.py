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
async def policy_objects(dashboard, org_id, version_salt):
    """Create 100 policy objects via action batch, yield object IDs, then delete."""
    batch_orgs = ActionBatchOrganizations()

    actions = [
        batch_orgs.createOrganizationPolicyObject(
            organizationId=org_id,
            name=f"_test_pobj_{version_salt}_{i:03d}",
            category="network",
            type="cidr",
            cidr=f"10.{i // 256}.{i % 256}.0/24",
        )
        for i in range(100)
    ]

    await _run_action_batch_async(dashboard, org_id, actions)

    all_objects = await dashboard.organizations.getOrganizationPolicyObjects(org_id, total_pages=-1)
    obj_ids = [o["id"] for o in all_objects if o["name"].startswith(f"_test_pobj_{version_salt}")]
    assert len(obj_ids) >= 100

    yield obj_ids

    delete_actions = [
        batch_orgs.deleteOrganizationPolicyObject(
            organizationId=org_id,
            policyObjectId=obj_id,
        )
        for obj_id in obj_ids
    ]
    await _run_action_batch_async(dashboard, org_id, delete_actions)


async def test_async_pagination_iterator_vs_legacy_policy_objects(api_key, org_id, version_salt, policy_objects):
    """Prove async iterator mode yields the same policy objects as legacy await mode."""

    async def fetch_legacy():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=False,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as d:
            objects = await d.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1)
            return {o["id"] for o in objects if o["name"].startswith(f"_test_pobj_{version_salt}")}

    async def fetch_iterator():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=True,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as d:
            ids = set()
            async for obj in d.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1):
                if obj["name"].startswith(f"_test_pobj_{version_salt}"):
                    ids.add(obj["id"])
            return ids

    legacy_ids, iterator_ids = await asyncio.gather(fetch_legacy(), fetch_iterator())

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) >= 100


async def test_async_iterator_yields_dicts(api_key, org_id, version_salt, policy_objects):
    """Each item from async iterator is a dict with an id field."""
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as d:
        async for obj in d.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1):
            assert isinstance(obj, dict)
            assert "id" in obj
            break
