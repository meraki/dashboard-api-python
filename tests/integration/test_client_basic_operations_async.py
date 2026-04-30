import pytest
import pytest_asyncio

import meraki.aio

pytestmark = pytest.mark.asyncio(loop_scope="session")


@pytest_asyncio.fixture(scope="session", loop_scope="session")
async def dashboard(api_key):
    async with meraki.aio.AsyncDashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=10,
        caller="PythonSDKTest Cisco",
    ) as dashboard:
        yield dashboard


async def test_get_organizations(dashboard):
    organizations = await dashboard.organizations.getOrganizations()
    assert organizations is not None
    assert len(organizations) > 0


async def test_get_organization(dashboard, org_id):
    organization = await dashboard.organizations.getOrganization(org_id)
    assert isinstance(organization, dict)
    assert isinstance(organization["id"], str)


async def test_get_organization_networks(dashboard, org_id):
    networks = await dashboard.organizations.getOrganizationNetworks(org_id)
    assert networks is not None
    assert len(networks) > 0
