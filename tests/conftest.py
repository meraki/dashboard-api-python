"""Root test configuration: shared fixtures for all test modules."""

import pytest

from tests.unit.conftest import FAKE_API_KEY, make_metadata, make_mock_response


@pytest.fixture
def mock_response_factory():
    """Factory for creating mock httpx.Response objects."""
    return make_mock_response


@pytest.fixture
def fake_api_key():
    return FAKE_API_KEY


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    """Remove Meraki env vars so tests don't leak state."""
    monkeypatch.delenv("MERAKI_DASHBOARD_API_KEY", raising=False)
    monkeypatch.delenv("BE_GEO_ID", raising=False)
    monkeypatch.delenv("MERAKI_PYTHON_SDK_CALLER", raising=False)


@pytest.fixture
def metadata_factory():
    """Factory for endpoint metadata dicts."""
    return make_metadata
