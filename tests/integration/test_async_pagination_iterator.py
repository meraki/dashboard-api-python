import pytest

import meraki.aio


@pytest.fixture(scope="session")
def api_key(pytestconfig):
    return pytestconfig.getoption("apikey")


@pytest.fixture(scope="session")
def org_id(pytestconfig):
    return pytestconfig.getoption("o")


@pytest.mark.asyncio
async def test_async_pagination_iterator_vs_legacy_networks(api_key, org_id):
    """Prove async iterator mode yields the same networks as legacy await mode."""
    # Legacy: await returns a list, iterate with for
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=False,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as dashboard_legacy:
        legacy_networks = await dashboard_legacy.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1)
        legacy_ids = {n["id"] for n in legacy_networks}

    # Iterator: async for yields items one by one
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as dashboard_iterator:
        iterator_ids = set()
        async for network in dashboard_iterator.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1):
            iterator_ids.add(network["id"])

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) > 0


@pytest.mark.asyncio
async def test_async_iterator_yields_dicts(api_key, org_id):
    """Each item from async iterator is a dict with id and name keys."""
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    ) as dashboard:
        async for network in dashboard.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1):
            assert isinstance(network, dict)
            assert "id" in network
            assert "name" in network
            break  # Only need to verify the first item
