"""Test AsyncDashboardAPI context manager and session lifecycle."""

import asyncio
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

    @pytest.mark.asyncio
    async def test_aexit_shuts_down_smart_flow_before_closing_client(self):
        # Regression for #7: __aexit__ must drain/cancel in-flight background
        # smart-flow tasks (via shutdown()) and persist the cache BEFORE the
        # httpx client is closed, otherwise those tasks fail with
        # "client has been closed" and resolution is lost.
        with patch("meraki.session.base.check_python_version"):
            api = AsyncDashboardAPI(
                api_key="fake_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )

        order = []
        bg_task_done = asyncio.Event()

        async def slow_background():
            # Simulate an in-flight resolve/hydrate task touching the client.
            await asyncio.sleep(0.05)
            bg_task_done.set()

        bg = asyncio.create_task(slow_background())

        smart_flow = MagicMock()
        save_calls = {"n": 0}

        async def fake_shutdown():
            order.append("shutdown")
            # Drain the in-flight background task before the client closes.
            await bg
            save_calls["n"] += 1  # shutdown performs the final save itself

        smart_flow.shutdown = AsyncMock(side_effect=fake_shutdown)
        api._session._smart_flow = smart_flow

        async def fake_close():
            order.append("close")

        api._session.close = AsyncMock(side_effect=fake_close)

        async with api:
            pass

        # shutdown ran exactly once, before the client/session close
        smart_flow.shutdown.assert_awaited_once()
        assert order == ["shutdown", "close"]
        # background task was awaited to completion (no lingering task)
        assert bg.done()
        assert bg_task_done.is_set()
        # cache persisted exactly once (shutdown does the save, not save_cache)
        assert save_calls["n"] == 1

    @pytest.mark.asyncio
    async def test_aexit_skips_shutdown_when_smart_flow_disabled(self):
        # When smart flow is disabled the limiter is None; __aexit__ must not
        # attempt to call shutdown() and must still close the client.
        with patch("meraki.session.base.check_python_version"):
            api = AsyncDashboardAPI(
                api_key="fake_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
                smart_flow_enabled=False,
            )

        assert api._session._smart_flow is None
        api._session.close = AsyncMock()

        async with api:
            pass

        api._session.close.assert_awaited_once()

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
