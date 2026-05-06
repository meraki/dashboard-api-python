"""Shared fixtures and helpers for unit tests."""

import json
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from meraki.session.sync import RestSession


FAKE_API_KEY = "fake_api_key_1234567890123456789012345678901234567890"

DEFAULT_SESSION_KWARGS = {
    "base_url": "https://api.meraki.com/api/v1",
    "single_request_timeout": 60,
    "certificate_path": "",
    "requests_proxy": "",
    "wait_on_rate_limit": True,
    "nginx_429_retry_wait_time": 2,
    "action_batch_retry_wait_time": 2,
    "network_delete_retry_wait_time": 2,
    "retry_4xx_error": False,
    "retry_4xx_error_wait_time": 1,
    "maximum_retries": 3,
    "simulate": False,
    "be_geo_id": "",
    "caller": "TestApp TestVendor",
    "use_iterator_for_get_pages": False,
}


def make_metadata(operation="getOrganizations", tags=None, **extra):
    meta = {"tags": tags or ["organizations"], "operation": operation}
    meta.update(extra)
    return meta


def make_mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=None,
    links=None,
):
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.reason_phrase = reason_phrase
    resp.headers = headers or {}
    resp.links = links or {}
    if content is not None:
        resp.content = content
    else:
        resp.content = json.dumps(json_data if json_data is not None else {"ok": True}).encode()
    resp.json.return_value = json_data if json_data is not None else {"ok": True}
    resp.text = json.dumps(json_data if json_data is not None else {"ok": True})
    resp.close = MagicMock()
    return resp


def make_async_mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=None,
    links=None,
):
    resp = make_mock_response(
        status_code=status_code,
        json_data=json_data,
        reason_phrase=reason_phrase,
        headers=headers,
        content=content,
        links=links,
    )
    resp.close = MagicMock(side_effect=RuntimeError("Attempted to call sync close on an async stream."))
    resp.aclose = AsyncMock()
    return resp


def make_sync_session(logger=None, **overrides):
    kwargs = {**DEFAULT_SESSION_KWARGS, **overrides}
    with patch("meraki.session.base.check_python_version"):
        with patch("httpx.Client") as mock_client:
            mock_instance = MagicMock()
            mock_instance.headers = MagicMock(spec=dict)
            mock_client.return_value = mock_instance
            s = RestSession(logger=logger, api_key=FAKE_API_KEY, **kwargs)
    return s


def make_async_session(logger=None, **overrides):
    kwargs = {"maximum_concurrent_requests": 8, **DEFAULT_SESSION_KWARGS, **overrides}
    with (
        patch("meraki.session.base.check_python_version"),
        patch("httpx.AsyncClient") as mock_client,
    ):
        mock_instance = MagicMock()
        mock_instance.headers = {}
        mock_instance.request = AsyncMock()
        mock_client.return_value = mock_instance
        from meraki.session.async_ import AsyncRestSession

        s = AsyncRestSession(logger=logger, api_key=FAKE_API_KEY, **kwargs)
    return s


# --- Pytest fixtures wrapping the factories ---


@pytest.fixture
def session():
    return make_sync_session()


@pytest.fixture
def async_session():
    return make_async_session()


@pytest.fixture
def async_session_with_logger():
    return make_async_session(logger=MagicMock())


@pytest.fixture
def async_session_with_cert(tmp_path):
    cert_file = tmp_path / "cert.pem"
    cert_file.write_text("FAKE CERT")
    return make_async_session(certificate_path=str(cert_file))


@pytest.fixture
def async_session_with_proxy():
    return make_async_session(requests_proxy="http://proxy:8080")
