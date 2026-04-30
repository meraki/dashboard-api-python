import pytest

import meraki


@pytest.fixture(scope="session")
def api_key(pytestconfig):
    return pytestconfig.getoption("apikey")


@pytest.fixture(scope="session")
def org_id(pytestconfig):
    return pytestconfig.getoption("o")


def test_pagination_iterator_vs_legacy_networks(api_key, org_id):
    """Prove iterator mode yields the same networks as legacy mode."""
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

    # Legacy returns a flat list
    legacy_networks = dashboard_legacy.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1)
    legacy_ids = {n["id"] for n in legacy_networks}

    # Iterator yields items one by one
    iterator_ids = set()
    for network in dashboard_iterator.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1):
        iterator_ids.add(network["id"])

    assert legacy_ids == iterator_ids
    assert len(legacy_ids) > 0


def test_pagination_iterator_yields_dicts(api_key, org_id):
    """Each yielded item from the iterator is a dict with id and name."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        use_iterator_for_get_pages=True,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    for network in dashboard.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1):
        assert isinstance(network, dict)
        assert "id" in network
        assert "name" in network
        break  # Only need to verify the first item


def test_get_organization_api_requests(api_key, org_id):
    """getOrganizationApiRequests returns records with expected fields."""
    dashboard = meraki.DashboardAPI(
        api_key,
        suppress_logging=True,
        maximum_retries=5,
        caller="PythonSDKTestPaginationIterator Cisco",
    )

    requests_log = dashboard.organizations.getOrganizationApiRequests(org_id, timespan=900, total_pages=-1)
    assert isinstance(requests_log, list)

    if len(requests_log) > 0:
        record = requests_log[0]
        expected_keys = [
            "method",
            "host",
            "path",
            "ts",
            "responseCode",
            "sourceIp",
            "userAgent",
        ]
        for key in expected_keys:
            assert key in record, f"Expected key '{key}' missing from API request record"
