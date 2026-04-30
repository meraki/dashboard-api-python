import pytest

import meraki.aio


@pytest.mark.asyncio
async def test_async_pagination_iterator_vs_legacy_networks(api_key, org_id):
    """Prove async iterator mode yields the same networks as legacy await mode."""
    import asyncio

    async def fetch_legacy():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=False,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as dashboard:
            networks = await dashboard.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1)
            return {n["id"] for n in networks}

    async def fetch_iterator():
        async with meraki.aio.AsyncDashboardAPI(
            api_key,
            suppress_logging=True,
            maximum_retries=5,
            use_iterator_for_get_pages=True,
            caller="PythonSDKTestPaginationIterator Cisco",
        ) as dashboard:
            ids = set()
            async for network in dashboard.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1):
                ids.add(network["id"])
            return ids

    legacy_ids, iterator_ids = await asyncio.gather(fetch_legacy(), fetch_iterator())

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
