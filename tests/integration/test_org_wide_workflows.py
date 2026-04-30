import asyncio

import pytest

import meraki
import meraki.aio


def test_sync_org_wide_clients_workflow(api_key, org_id):
    """Multi-endpoint chain: orgs -> networks -> clients."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        caller="PythonSDKTestOrgWideWorkflows Cisco",
    )

    networks = dashboard.organizations.getOrganizationNetworks(org_id, total_pages="all", perPage=1000)
    assert isinstance(networks, list)
    assert len(networks) > 0

    # Take first network and fetch its clients
    network_id = networks[0]["id"]
    clients = dashboard.networks.getNetworkClients(network_id, timespan=86400, perPage=1000, total_pages="all")
    assert isinstance(clients, list)

    if len(clients) > 0:
        assert isinstance(clients[0], dict)
        assert "mac" in clients[0]


@pytest.mark.asyncio
async def test_async_org_wide_clients_workflow(api_key, org_id):
    """Concurrent async fetching via asyncio.as_completed."""
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        caller="PythonSDKTestOrgWideWorkflows Cisco",
    ) as dashboard:
        networks = await dashboard.organizations.getOrganizationNetworks(org_id)
        assert len(networks) > 0

        # Take up to first 3 networks
        target_networks = networks[:3]

        async def fetch_clients(net_id):
            return await dashboard.networks.getNetworkClients(net_id, timespan=86400, perPage=1000, total_pages="all")

        tasks = [asyncio.create_task(fetch_clients(n["id"])) for n in target_networks]

        results = []
        for coro in asyncio.as_completed(tasks):
            result = await coro
            results.append(result)

        # All results should be lists
        assert len(results) == len(target_networks)
        for result in results:
            assert isinstance(result, list)
