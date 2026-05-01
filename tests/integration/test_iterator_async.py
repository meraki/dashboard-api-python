import asyncio
import platform
import random

import pytest

import meraki.aio
from meraki.api.batch.organizations import ActionBatchOrganizations

pytestmark = pytest.mark.asyncio(loop_scope="module")

BATCH_SIZE_MAX = 50
TOTAL_POL_OBJS = 100


async def _poll_batch(dashboard, org_id, batch_id, max_checks=10, delay=4):
    for _ in range(max_checks):
        await asyncio.sleep(delay)
        status = await dashboard.organizations.getOrganizationActionBatch(
            organizationId=org_id,
            actionBatchId=batch_id,
        )
        if status["status"]["completed"]:
            return True
        if status["status"]["failed"]:
            return False
    return False


async def test_iterator_async_full_lifecycle(api_key, org_id):
    python_version = platform.python_version()
    salt = str(random.randint(1, 17381738))
    version_salt = f"{python_version} {salt}"

    batch_orgs = ActionBatchOrganizations()

    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=1000,
        caller="PythonSDKTestIteratorAsync Cisco",
    ) as dashboard:
        # Phase 1: Clean up stale action batches
        batches = await dashboard.organizations.getOrganizationActionBatches(organizationId=org_id)
        unconfirmed = [b for b in batches if not b["confirmed"]]
        for b in unconfirmed:
            await dashboard.organizations.deleteOrganizationActionBatch(organizationId=org_id, actionBatchId=b["id"])
        remaining = await dashboard.organizations.getOrganizationActionBatches(organizationId=org_id)
        assert all(b["confirmed"] for b in remaining)

        # Phase 2: Clean up existing policy objects
        existing_objects = await dashboard.organizations.getOrganizationPolicyObjects(organizationId=org_id, total_pages=-1)
        if len(existing_objects) > 0:
            delete_actions = [
                batch_orgs.deleteOrganizationPolicyObject(organizationId=org_id, policyObjectId=obj["id"])
                for obj in existing_objects
            ]
            for i in range(0, len(delete_actions), BATCH_SIZE_MAX):
                chunk = delete_actions[i : i + BATCH_SIZE_MAX]
                batch = await dashboard.organizations.createOrganizationActionBatch(
                    organizationId=org_id, actions=chunk, synchronous=False, confirmed=True
                )
                assert await _poll_batch(dashboard, org_id, batch["id"])

        leftover = await dashboard.organizations.getOrganizationPolicyObjects(organizationId=org_id, total_pages=-1)
        assert len(leftover) == 0

        # Phase 3: Create policy objects
        create_actions = [
            batch_orgs.createOrganizationPolicyObject(
                organizationId=org_id,
                name=f"_test_iter_{version_salt}_{i:03d}",
                category="network",
                type="cidr",
                cidr=f"10.{i // 256}.{i % 256}.0/24",
            )
            for i in range(TOTAL_POL_OBJS)
        ]

        create_batch_ids = []
        for i in range(0, len(create_actions), BATCH_SIZE_MAX):
            chunk = create_actions[i : i + BATCH_SIZE_MAX]
            batch = await dashboard.organizations.createOrganizationActionBatch(
                organizationId=org_id, actions=chunk, synchronous=False, confirmed=True
            )
            assert batch["id"]
            create_batch_ids.append(batch["id"])

        # Phase 4: Poll until all create batches complete
        for batch_id in create_batch_ids:
            assert await _poll_batch(dashboard, org_id, batch_id), f"Create batch {batch_id} did not complete"

        # Phase 5: Test pagination iterator vs legacy
        async with (
            meraki.aio.AsyncDashboardAPI(
                api_key,
                suppress_logging=True,
                maximum_retries=5,
                use_iterator_for_get_pages=False,
                caller="PythonSDKTestIteratorAsync Cisco",
            ) as dashboard_legacy,
            meraki.aio.AsyncDashboardAPI(
                api_key,
                suppress_logging=True,
                maximum_retries=5,
                use_iterator_for_get_pages=True,
                caller="PythonSDKTestIteratorAsync Cisco",
            ) as dashboard_iterator,
        ):
            legacy_objects = await dashboard_legacy.organizations.getOrganizationPolicyObjects(
                org_id, perPage=10, total_pages=-1
            )
            legacy_ids = {o["id"] for o in legacy_objects if o["name"].startswith(f"_test_iter_{version_salt}")}

            iterator_ids = set()
            async for obj in dashboard_iterator.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1):
                if obj["name"].startswith(f"_test_iter_{version_salt}"):
                    iterator_ids.add(obj["id"])

        assert legacy_ids == iterator_ids
        assert len(legacy_ids) >= TOTAL_POL_OBJS

        # Phase 6: Delete policy objects
        all_objects = await dashboard.organizations.getOrganizationPolicyObjects(organizationId=org_id, total_pages=-1)
        test_objects = [o for o in all_objects if o["name"].startswith(f"_test_iter_{version_salt}")]

        delete_actions = [
            batch_orgs.deleteOrganizationPolicyObject(organizationId=org_id, policyObjectId=obj["id"]) for obj in test_objects
        ]

        delete_batch_ids = []
        for i in range(0, len(delete_actions), BATCH_SIZE_MAX):
            chunk = delete_actions[i : i + BATCH_SIZE_MAX]
            batch = await dashboard.organizations.createOrganizationActionBatch(
                organizationId=org_id, actions=chunk, synchronous=False, confirmed=True
            )
            assert batch["id"]
            delete_batch_ids.append(batch["id"])

        # Phase 7: Poll until all delete batches complete
        for batch_id in delete_batch_ids:
            assert await _poll_batch(dashboard, org_id, batch_id), f"Delete batch {batch_id} did not complete"
