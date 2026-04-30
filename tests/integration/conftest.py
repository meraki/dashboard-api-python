import pytest


def pytest_addoption(parser):
    parser.addoption("--apikey", action="store", default="")
    parser.addoption("--o", action="store", default="")


@pytest.fixture(scope="session")
def api_key(pytestconfig):
    return pytestconfig.getoption("apikey")


@pytest.fixture(scope="session")
def org_id(pytestconfig):
    return pytestconfig.getoption("o")
