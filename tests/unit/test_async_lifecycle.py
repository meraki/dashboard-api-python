"""Test AsyncDashboardAPI context manager and session lifecycle."""

from unittest.mock import patch, AsyncMock, MagicMock

import pytest

from meraki.aio import AsyncDashboardAPI
from meraki.exceptions import APIKeyError


class TestAsyncDashboardAPILifecycle:
    def test_missing_api_key_raises(self, monkeypatch):
        monkeypatch.delenv("MERAKI_DASHBOARD_API_KEY", raising=False)
        with pytest.raises(APIKeyError):
            AsyncDashboardAPI(api_key=None, suppress_logging=True)

    def test_instantiation_with_valid_key(self):
        with patch("meraki.session.base.check_python_version"):
            api = AsyncDashboardAPI(
                api_key="fake_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )
        assert api._session is not None

    @pytest.mark.asyncio
    async def test_context_manager_enters_and_exits(self):
        with patch("meraki.session.base.check_python_version"):
            api = AsyncDashboardAPI(
                api_key="fake_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )

        api._session._client = MagicMock()
        api._session._client.aclose = AsyncMock()

        async with api as dashboard:
            assert dashboard is api

        api._session._client.aclose.assert_called_once()

    def test_all_api_sections_assigned(self):
        with patch("meraki.session.base.check_python_version"):
            api = AsyncDashboardAPI(
                api_key="fake_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )

        sections = [
            "administered",
            "appliance",
            "camera",
            "campusGateway",
            "cellularGateway",
            "devices",
            "insight",
            "licensing",
            "networks",
            "organizations",
            "sensor",
            "sm",
            "spaces",
            "switch",
            "wireless",
            "wirelessController",
        ]
        for section in sections:
            assert hasattr(api, section), f"Missing API section: {section}"
            assert getattr(api, section) is not None
