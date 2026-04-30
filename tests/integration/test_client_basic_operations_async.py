import pytest

import meraki.aio


@pytest.fixture(scope="session")
def api_key(pytestconfig):
    return pytestconfig.getoption("apikey")


@pytest.fixture(scope="session")
def org_id(pytestconfig):
    return pytestconfig.getoption("o")


@pytest.mark.asyncio
async def test_get_organizations(api_key):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=1000,
        caller="PythonSDKTest Cisco",
    ) as dashboard:
        organizations = await dashboard.organizations.getOrganizations()
        assert organizations is not None
        assert len(organizations) > 0


@pytest.mark.asyncio
async def test_get_organization(api_key, org_id):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=1000,
        caller="PPythonSDKTest Cisco",
    ) as dashboard:
        organization = await dashboard.organizations.getOrganization(org_id)
        assert isinstance(organization, dict)
        assert isinstance(organization["id"], str)


@pytest.mark.asyncio
async def test_get_organization_networks(api_key, org_id):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=1000,
        caller="PythonSDKTest Cisco",
    ) as dashboard:
        networks = await dashboard.organizations.getOrganizationNetworks(org_id)
        assert networks is not None
        assert len(networks) > 0
