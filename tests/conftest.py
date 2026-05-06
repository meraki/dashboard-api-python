"""Root test configuration: shared fixtures for all test modules."""

from unittest.mock import MagicMock

import httpx
import pytest


@pytest.fixture
def mock_response_factory():
    """Factory for creating mock httpx.Response objects."""

    def _make(
        status_code=200,
        json_data=None,
        headers=None,
        content=b'{"ok":true}',
        reason_phrase="OK",
        links=None,
    ):
        resp = MagicMock(spec=httpx.Response)
        resp.status_code = status_code
        resp.reason_phrase = reason_phrase
        resp.headers = headers or {}
        resp.content = content
        resp.links = links or {}
        resp.json.return_value = json_data if json_data is not None else {"ok": True}
        resp.close = MagicMock()
        return resp

    return _make


@pytest.fixture
def fake_api_key():
    return "fake_api_key_1234567890123456789012345678901234567890"


@pytest.fixture(autouse=True)
def _clean_env(monkeypatch):
    """Remove Meraki env vars so tests don't leak state."""
    monkeypatch.delenv("MERAKI_DASHBOARD_API_KEY", raising=False)
    monkeypatch.delenv("BE_GEO_ID", raising=False)
    monkeypatch.delenv("MERAKI_PYTHON_SDK_CALLER", raising=False)


@pytest.fixture
def metadata_factory():
    """Factory for endpoint metadata dicts."""

    def _make(operation="getOrganizations", tags=None):
        return {"tags": tags or ["organizations"], "operation": operation}

    return _make
