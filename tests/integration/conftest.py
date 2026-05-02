import pytest

FILE_ORDER = [
    "test_client_crud_lifecycle_sync.py",
    "test_client_crud_lifecycle_async.py",
    "test_org_wide_workflows.py",
    "test_iterator_sync.py",
    "test_iterator_async.py",
]


def pytest_collection_modifyitems(items):
    def sort_key(item):
        filename = item.fspath.basename
        try:
            return FILE_ORDER.index(filename)
        except ValueError:
            return len(FILE_ORDER)

    items.sort(key=sort_key)


def pytest_addoption(parser):
    parser.addoption("--apikey", action="store", default="")
    parser.addoption("--o", action="store", default="")


@pytest.fixture(scope="session")
def api_key(pytestconfig):
    return pytestconfig.getoption("apikey")


@pytest.fixture(scope="session")
def org_id(pytestconfig):
    return pytestconfig.getoption("o")
