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
def policy_objects(dashboard, org_id, version_salt):
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

    _run_action_batch(dashboard, org_id, actions)

    all_objects = dashboard.organizations.getOrganizationPolicyObjects(org_id, total_pages=-1)
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
    _run_action_batch(dashboard, org_id, delete_actions)


def test_pagination_iterator_vs_legacy_policy_objects(api_key, org_id, version_salt, policy_objects):
    """Prove iterator mode yields the same policy objects as legacy mode."""
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

    legacy_objects = dashboard_legacy.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1)
    legacy_ids = {o["id"] for o in legacy_objects if o["name"].startswith(f"_test_pobj_{version_salt}")}

    iterator_ids = set()
    for obj in dashboard_iterator.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1):
        if obj["name"].startswith(f"_test_pobj_{version_salt}"):
            iterator_ids.add(obj["id"])

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) >= 100


def test_pagination_iterator_yields_dicts(api_key, org_id, version_salt, policy_objects):
    """Each yielded item from the iterator is a dict with an id field."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    for obj in dashboard.organizations.getOrganizationPolicyObjects(org_id, perPage=10, total_pages=-1):
        assert isinstance(obj, dict)
        assert "id" in obj
        break
