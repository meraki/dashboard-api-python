from unittest.mock import MagicMock, patch

import httpx
import pytest

from meraki.exceptions import APIError, SessionInputError
from meraki.session.sync import RestSession


@pytest.fixture
def session():
    with patch("meraki.session.base.check_python_version"):
        with patch("httpx.Client") as mock_client:
            mock_instance = MagicMock()
            mock_instance.headers = MagicMock(spec=dict)
            mock_client.return_value = mock_instance
            s = RestSession(
                logger=None,
                api_key="fake_api_key_1234567890123456789012345678901234567890",
                base_url="https://api.meraki.com/api/v1",
                single_request_timeout=60,
                certificate_path="",
                requests_proxy="",
                wait_on_rate_limit=True,
                nginx_429_retry_wait_time=2,
                action_batch_retry_wait_time=2,
                network_delete_retry_wait_time=2,
                retry_4xx_error=False,
                retry_4xx_error_wait_time=1,
                maximum_retries=3,
                simulate=False,
                be_geo_id="",
                caller="TestApp TestVendor",
                use_iterator_for_get_pages=False,
            )
    return s


def _metadata(operation="getOrganizations", tags=None):
    return {"tags": tags or ["organizations"], "operation": operation}


def _mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=b'{"ok":true}',
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


# --- Retry logic tests ---


class TestRetryLogic:
    @patch("time.sleep", return_value=None)
    def test_retry_on_429_with_retry_after(self, mock_sleep, session):
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_429, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200
        mock_sleep.assert_called_with(1)

    @patch("time.sleep", return_value=None)
    def test_retry_on_429_without_retry_after(self, mock_sleep, session):
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={})
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_429, resp_200])

        with patch("random.randint", return_value=1):
            result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_429_raises_after_max_retries(self, mock_sleep, session):
        session._maximum_retries = 2
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        session._client.request = MagicMock(return_value=resp_429)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_429_raises_immediately_when_wait_disabled(self, mock_sleep, session):
        session._wait_on_rate_limit = False
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={})
        session._client.request = MagicMock(return_value=resp_429)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_retry_on_5xx(self, mock_sleep, session):
        resp_500 = _mock_response(500, reason_phrase="Internal Server Error")
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_500, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_5xx_raises_after_max_retries(self, mock_sleep, session):
        session._maximum_retries = 2
        resp_500 = _mock_response(500, reason_phrase="Internal Server Error")
        session._client.request = MagicMock(return_value=resp_500)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_retry_on_connection_error(self, mock_sleep, session):
        exc = httpx.ConnectError("Connection refused")
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[exc, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_connection_error_raises_after_max_retries(self, mock_sleep, session):
        session._maximum_retries = 1
        exc = httpx.ConnectError("Connection refused")
        session._client.request = MagicMock(side_effect=[exc])

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_429_retry_count_matches_maximum_retries(self, mock_sleep, session):
        """Verify exactly maximum_retries attempts occur before APIError."""
        session._maximum_retries = 3
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        session._client.request = MagicMock(return_value=resp_429)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

        assert session._client.request.call_count == 3

    @patch("time.sleep", return_value=None)
    def test_429_uses_retry_after_header_value(self, mock_sleep, session):
        """Verify sleep uses exact Retry-After header value."""
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={"Retry-After": "7"})
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_429, resp_200])

        session.request(_metadata(), "GET", "/organizations")
        mock_sleep.assert_called_with(7)

    @patch("time.sleep", return_value=None)
    def test_server_error_retries_exactly_maximum_retries(self, mock_sleep, session):
        """Verify 5xx retries exhaust exactly maximum_retries attempts."""
        session._maximum_retries = 2
        resp_500 = _mock_response(500, reason_phrase="Internal Server Error")
        session._client.request = MagicMock(return_value=resp_500)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

        assert session._client.request.call_count == 2
        assert mock_sleep.call_count == 2

    @patch("time.sleep", return_value=None)
    def test_connection_error_retries_exactly_maximum_retries(self, mock_sleep, session):
        """Verify HTTPError retries exhaust exactly maximum_retries attempts."""
        session._maximum_retries = 3
        session._client.request = MagicMock(side_effect=httpx.ConnectError("connection refused"))

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

        assert session._client.request.call_count == 3
        assert mock_sleep.call_count == 3


# --- Pagination tests ---


class TestPaginationLegacy:
    @patch("time.sleep", return_value=None)
    def test_single_page(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._client.request = MagicMock(return_value=resp)

        result = session._get_pages_legacy(_metadata(), "/organizations")
        assert result == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_multiple_pages(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "1"}],
            links={"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"}},
        )
        resp2 = _mock_response(200, json_data=[{"id": "2"}], links={})
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(_metadata(), "/organizations", total_pages=-1)
        assert result == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_limit(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "1"}],
            links={"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"}},
        )
        resp2 = _mock_response(
            200,
            json_data=[{"id": "2"}],
            links={"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=2"}},
        )
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(_metadata(), "/organizations", total_pages=2)
        assert result == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_string_all(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._client.request = MagicMock(return_value=resp)

        result = session._get_pages_legacy(_metadata(), "/organizations", total_pages="all")
        assert result == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_invalid_raises(self, mock_sleep, session):
        with pytest.raises(SessionInputError):
            session._get_pages_legacy(_metadata(), "/organizations", total_pages="invalid")

    @patch("time.sleep", return_value=None)
    def test_204_no_content(self, mock_sleep, session):
        resp = _mock_response(204, json_data=None, reason_phrase="No Content", links={})
        session._client.request = MagicMock(return_value=resp)

        result = session._get_pages_legacy(_metadata(), "/organizations")
        assert result is None

    @patch("time.sleep", return_value=None)
    def test_items_dict_pagination(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data={
                "items": [{"id": "1"}],
                "meta": {"counts": {"items": {"remaining": 1}}},
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/things?startingAfter=1"}},
        )
        resp2 = _mock_response(
            200,
            json_data={
                "items": [{"id": "2"}],
                "meta": {"counts": {"items": {"remaining": 0}}},
            },
            links={},
        )
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(_metadata(), "/things", total_pages=-1)
        assert result["items"] == [{"id": "1"}, {"id": "2"}]
        assert result["meta"]["counts"]["items"]["remaining"] == 0


class TestPaginationIterator:
    @patch("time.sleep", return_value=None)
    def test_single_page_yields_items(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}, {"id": "2"}], links={})
        session._client.request = MagicMock(return_value=resp)

        results = list(session._get_pages_iterator(_metadata(), "/organizations"))
        assert results == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_multiple_pages_yields_all(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "1"}],
            links={"next": {"url": "https://api.meraki.com/api/v1/orgs?startingAfter=1"}},
        )
        resp2 = _mock_response(200, json_data=[{"id": "2"}], links={})
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        results = list(session._get_pages_iterator(_metadata(), "/organizations", total_pages=-1))
        assert results == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_items_dict_yields_items(self, mock_sleep, session):
        resp = _mock_response(200, json_data={"items": [{"id": "a"}, {"id": "b"}]}, links={})
        session._client.request = MagicMock(return_value=resp)

        results = list(session._get_pages_iterator(_metadata(), "/things"))
        assert results == [{"id": "a"}, {"id": "b"}]


# --- 4xx error handling tests ---


class TestHandle4xxErrors:
    @patch("time.sleep", return_value=None)
    def test_generic_4xx_raises_immediately(self, mock_sleep, session):
        resp_400 = _mock_response(400, json_data={"errors": ["bad request"]}, reason_phrase="Bad Request")
        session._client.request = MagicMock(return_value=resp_400)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_network_delete_concurrency_retries(self, mock_sleep, session):
        resp_400 = _mock_response(
            400,
            json_data={"errors": ["concurrent requests detected"]},
            reason_phrase="Bad Request",
        )
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_400, resp_200])

        with patch("random.randint", return_value=1):
            result = session.request(_metadata(operation="deleteNetwork"), "DELETE", "/networks/123")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_action_batch_concurrency_retries(self, mock_sleep, session):
        resp_400 = _mock_response(
            400,
            json_data={"errors": ["Too many concurrently executing batches"]},
            reason_phrase="Bad Request",
        )
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_400, resp_200])

        result = session.request(_metadata(operation="createBatch"), "POST", "/batches")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_retry_4xx_when_enabled(self, mock_sleep, session):
        session._retry_4xx_error = True
        resp_400 = _mock_response(400, json_data={"errors": ["something"]}, reason_phrase="Bad Request")
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_400, resp_200])

        with patch("random.randint", return_value=1):
            result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200


# --- Simulate mode ---


class TestSimulateMode:
    def test_simulate_skips_non_get(self, session):
        session._simulate = True
        result = session.request(_metadata(), "POST", "/organizations")
        assert result is None

    def test_simulate_allows_get(self, session):
        session._simulate = True
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(return_value=resp_200)
        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200


# --- 3xx redirect ---


class TestRedirect:
    @patch("time.sleep", return_value=None)
    def test_follows_redirect(self, mock_sleep, session):
        resp_301 = _mock_response(
            301,
            reason_phrase="Moved",
            headers={"Location": "https://n123.meraki.com/api/v1/organizations"},
        )
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(side_effect=[resp_301, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200


# --- _transport_kwargs ---


class TestTransportKwargs:
    def test_returns_kwargs_unchanged(self, session):
        kwargs = {"params": {"foo": "bar"}}
        result = session._transport_kwargs(kwargs)
        assert result == {"params": {"foo": "bar"}}

    def test_does_not_inject_timeout(self, session):
        kwargs = {}
        result = session._transport_kwargs(kwargs)
        assert "timeout" not in result

    def test_does_not_inject_verify(self, session):
        session._certificate_path = "/path/to/cert.pem"
        kwargs = {}
        result = session._transport_kwargs(kwargs)
        assert "verify" not in result


# --- HTTP verb methods ---


class TestHTTPVerbs:
    def test_get_returns_json(self, session):
        resp = _mock_response(200, json_data={"id": "1"}, content=b'{"id":"1"}')
        session._client.request = MagicMock(return_value=resp)
        result = session.get(_metadata(), "/organizations")
        assert result == {"id": "1"}

    def test_get_returns_none_on_empty_content(self, session):
        resp = _mock_response(200, json_data=None, content=b"   ")
        session._client.request = MagicMock(return_value=resp)
        result = session.get(_metadata(), "/organizations")
        assert result is None

    def test_get_returns_none_when_simulated(self, session):
        session._simulate = True
        resp = _mock_response(200, json_data={"id": "1"}, content=b'{"id":"1"}')
        session._client.request = MagicMock(return_value=resp)
        # GET still goes through in simulate mode
        result = session.get(_metadata(), "/organizations")
        assert result == {"id": "1"}

    def test_post_returns_json(self, session):
        resp = _mock_response(201, json_data={"id": "new"}, content=b'{"id":"new"}')
        session._client.request = MagicMock(return_value=resp)
        result = session.post(_metadata(), "/organizations", json={"name": "Test"})
        assert result == {"id": "new"}

    def test_post_returns_none_on_empty_content(self, session):
        resp = _mock_response(204, json_data=None, content=b"")
        session._client.request = MagicMock(return_value=resp)
        result = session.post(_metadata(), "/organizations", json={"name": "Test"})
        assert result is None

    def test_put_returns_json(self, session):
        resp = _mock_response(200, json_data={"id": "updated"}, content=b'{"id":"updated"}')
        session._client.request = MagicMock(return_value=resp)
        result = session.put(_metadata(), "/organizations/1", json={"name": "New"})
        assert result == {"id": "updated"}

    def test_put_returns_none_on_empty_content(self, session):
        resp = _mock_response(200, json_data=None, content=b"  ")
        session._client.request = MagicMock(return_value=resp)
        result = session.put(_metadata(), "/organizations/1", json={"name": "New"})
        assert result is None

    def test_delete_returns_none(self, session):
        resp = _mock_response(204, reason_phrase="No Content", content=b"")
        session._client.request = MagicMock(return_value=resp)
        result = session.delete(_metadata(), "/organizations/1")
        assert result is None

    def test_delete_passes_query_params(self, session):
        resp = _mock_response(204, reason_phrase="No Content", content=b"")
        session._client.request = MagicMock(return_value=resp)
        params = {"force": "true"}
        session.delete(_metadata(), "/networks/1/groupPolicies/1", params)
        call_kwargs = session._client.request.call_args
        assert call_kwargs.kwargs.get("params") == params


# --- Connection error with response object ---


class TestConnectionErrorWithResponse:
    @patch("time.sleep", return_value=None)
    def test_connection_error_with_response_status(self, mock_sleep, session):
        session._maximum_retries = 1
        exc = httpx.ConnectError("refused")
        session._client.request = MagicMock(side_effect=[exc])

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")


# --- JSON decode retry exhaustion ---


class TestJSONDecodeRetryExhaustion:
    @patch("time.sleep", return_value=None)
    def test_bad_json_raises_after_max_retries(self, mock_sleep, session):
        import json as json_mod

        session._maximum_retries = 2
        resp = _mock_response(200, content=b'{"ok":true}')
        resp.json.side_effect = json_mod.decoder.JSONDecodeError("", "", 0)
        session._client.request = MagicMock(return_value=resp)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")


# --- Pagination legacy: prev direction and event log ---


class TestPaginationLegacyExtended:
    @patch("time.sleep", return_value=None)
    def test_prev_direction(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "2"}],
            links={"prev": {"url": "https://api.meraki.com/api/v1/orgs?endingBefore=2"}},
        )
        resp2 = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(_metadata(), "/orgs", direction="prev")
        assert result == [{"id": "2"}, {"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_next_reverses_events(self, mock_sleep, session):
        resp = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}, {"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
            links={},
        )
        session._client.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        result = session._get_pages_legacy(metadata, "/events", direction="next")
        assert result["events"] == [{"ts": "a"}, {"ts": "b"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_breaks_on_recent_starting_after(self, mock_sleep, session):
        from datetime import datetime, timezone

        resp = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-01-01T00:00:00+00:00"}},
        )
        session._client.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        with patch("meraki.session.sync.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2024, 1, 1, 0, 2, 0, tzinfo=timezone.utc)
            mock_dt.fromisoformat.return_value = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            result = session._get_pages_legacy(metadata, "/events", direction="next")
        assert result["events"] == [{"ts": "a"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_breaks_on_end_time(self, mock_sleep, session):
        from datetime import datetime, timezone

        resp = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-06-01T00:00:00+00:00"}},
        )
        session._client.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        with patch("meraki.session.sync.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            mock_dt.fromisoformat.return_value = datetime(2024, 6, 1, 0, 0, 0, tzinfo=timezone.utc)
            result = session._get_pages_legacy(
                metadata,
                "/events",
                direction="next",
                event_log_end_time="2024-05-01T00:00:00Z",
            )
        assert result["events"] == [{"ts": "a"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_prev_breaks_before_2014(self, mock_sleep, session):
        resp = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2014-01-01T00:00:00Z",
                "pageEndAt": "2014-01-02T00:00:00Z",
            },
            links={"prev": {"url": "https://api.meraki.com/api/v1/events?endingBefore=2013-12-31T00:00:00Z"}},
        )
        session._client.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        result = session._get_pages_legacy(metadata, "/events", direction="prev")
        assert result["events"] == [{"ts": "a"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_numeric_string(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._client.request = MagicMock(return_value=resp)

        result = session._get_pages_legacy(_metadata(), "/orgs", total_pages="3")
        assert result == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_multi_page_extends_events(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}, {"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2014-06-01T00:00:00+00:00"}},
        )
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "d"}, {"ts": "c"}],
                "pageStartAt": "2024-01-01T01:00:00Z",
                "pageEndAt": "2024-01-01T02:00:00Z",
            },
            links={},
        )
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        from datetime import datetime, timezone

        with patch("meraki.session.sync.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            mock_dt.fromisoformat.return_value = datetime(2014, 6, 1, 0, 0, 0, tzinfo=timezone.utc)
            result = session._get_pages_legacy(metadata, "/events", direction="next")

        # First page reversed, second page reversed and appended
        assert result["events"] == [{"ts": "a"}, {"ts": "b"}, {"ts": "c"}, {"ts": "d"}]
        assert result["pageStartAt"] == "2024-01-01T00:00:00Z"
        assert result["pageEndAt"] == "2024-01-01T02:00:00Z"


# --- Pagination iterator: extended coverage ---


class TestBackoffStrategy:
    @patch("time.sleep", return_value=None)
    @patch("random.random", return_value=0.5)
    def test_429_exponential_backoff_without_retry_after(self, mock_random, mock_sleep, session):
        """Without Retry-After, backoff is 2^attempt * (1 + random), capped."""
        session._maximum_retries = 4
        session._nginx_429_retry_wait_time = 60
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={})
        resp_200 = _mock_response(200)

        session._client.request = MagicMock(side_effect=[resp_429, resp_429, resp_429, resp_200])

        session.request(_metadata(), "GET", "/organizations")

        sleep_calls = [call.args[0] for call in mock_sleep.call_args_list]
        assert len(sleep_calls) == 3
        # attempt 0: 2^0 * 1.5 = 1.5
        # attempt 1: 2^1 * 1.5 = 3.0
        # attempt 2: 2^2 * 1.5 = 6.0
        assert sleep_calls[0] == pytest.approx(1.5)
        assert sleep_calls[1] == pytest.approx(3.0)
        assert sleep_calls[2] == pytest.approx(6.0)

    @patch("time.sleep", return_value=None)
    @patch("random.random", return_value=0.0)
    def test_429_backoff_capped_at_nginx_wait_time(self, mock_random, mock_sleep, session):
        """Backoff never exceeds nginx_429_retry_wait_time."""
        session._maximum_retries = 10
        session._nginx_429_retry_wait_time = 5
        resp_429 = _mock_response(429, reason_phrase="Too Many Requests", headers={})
        resp_200 = _mock_response(200)

        session._client.request = MagicMock(side_effect=[resp_429] * 8 + [resp_200])

        session.request(_metadata(), "GET", "/organizations")

        sleep_calls = [call.args[0] for call in mock_sleep.call_args_list]
        for wait in sleep_calls:
            assert wait <= 5, f"Wait {wait} exceeds cap of 5"


class TestEdgeCases:
    @patch("time.sleep", return_value=None)
    def test_json_decode_failure_retries(self, mock_sleep, session):
        """Invalid JSON on GET triggers retry, eventual success returns response."""
        bad_resp = _mock_response(200, content=b"not json")
        bad_resp.json.side_effect = ValueError("No JSON")
        good_resp = _mock_response(200, json_data={"id": "123"})

        session._client.request = MagicMock(side_effect=[bad_resp, good_resp])
        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200
        assert session._client.request.call_count == 2

    @patch("time.sleep", return_value=None)
    def test_json_decode_failure_exhausts_retries(self, mock_sleep, session):
        """Persistent invalid JSON exhausts retries and raises APIError."""
        session._maximum_retries = 2
        bad_resp = _mock_response(200, content=b"not json")
        bad_resp.json.side_effect = ValueError("No JSON")

        session._client.request = MagicMock(return_value=bad_resp)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

        assert session._client.request.call_count == 2

    def test_simulate_mode_skips_post(self, session):
        """Simulate mode returns None for POST without making HTTP call."""
        session._simulate = True
        session._client.request = MagicMock()

        result = session.request(_metadata(), "POST", "/organizations")
        assert result is None
        session._client.request.assert_not_called()

    def test_simulate_mode_allows_get(self, session):
        """Simulate mode still executes GET requests."""
        session._simulate = True
        resp_200 = _mock_response(200)
        session._client.request = MagicMock(return_value=resp_200)

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200
        session._client.request.assert_called_once()

    def test_204_no_content_returns_response(self, session):
        """204 No Content returns the response object (not None)."""
        resp_204 = _mock_response(204, content=b"", reason_phrase="No Content")
        resp_204.json.side_effect = ValueError("No JSON")
        session._client.request = MagicMock(return_value=resp_204)

        result = session.request(_metadata(), "DELETE", "/organizations/123")
        assert result.status_code == 204


class TestPaginationIteratorExtended:
    @patch("time.sleep", return_value=None)
    def test_total_pages_numeric_string(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._client.request = MagicMock(return_value=resp)

        results = list(session._get_pages_iterator(_metadata(), "/orgs", total_pages="3"))
        assert results == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_invalid_raises(self, mock_sleep, session):
        with pytest.raises(SessionInputError):
            list(session._get_pages_iterator(_metadata(), "/orgs", total_pages="invalid"))

    @patch("time.sleep", return_value=None)
    def test_prev_direction(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "2"}],
            links={"prev": {"url": "https://api.meraki.com/api/v1/orgs?endingBefore=2"}},
        )
        resp2 = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        results = list(session._get_pages_iterator(_metadata(), "/orgs", direction="prev"))
        assert results == [{"id": "2"}, {"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_next_reverses(self, mock_sleep, session):
        resp = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}, {"ts": "a"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
            links={},
        )
        session._client.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        results = list(session._get_pages_iterator(metadata, "/events", direction="next"))
        assert results == [{"ts": "a"}, {"ts": "b"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_prev_normal_order(self, mock_sleep, session):
        resp = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}, {"ts": "b"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
            links={},
        )
        session._client.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="someOp")
        results = list(session._get_pages_iterator(metadata, "/events", direction="prev"))
        assert results == [{"ts": "a"}, {"ts": "b"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_breaks_on_recent_starting_after(self, mock_sleep, session):
        from datetime import datetime, timezone

        # Page 1: far enough in past, passes check, yields items
        resp1 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2014-06-01T00:00:00+00:00"}},
        )
        # Page 2: too recent, triggers break before yielding
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2025-01-01",
                "pageEndAt": "2025-01-02",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2025-01-01T23:58:00+00:00"}},
        )
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        call_count = [0]

        def fake_fromisoformat(s):
            call_count[0] += 1
            if call_count[0] == 1:
                return datetime(2014, 6, 1, 0, 0, 0, tzinfo=timezone.utc)
            return datetime(2025, 1, 1, 23, 58, 0, tzinfo=timezone.utc)

        with patch("meraki.session.sync.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 1, 2, 0, 0, 0, tzinfo=timezone.utc)
            mock_dt.fromisoformat = fake_fromisoformat
            results = list(session._get_pages_iterator(metadata, "/events", direction="next"))
        # Only page 1 yielded (reversed)
        assert results == [{"ts": "a"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_breaks_on_end_time(self, mock_sleep, session):
        from datetime import datetime, timezone

        # Page 1: passes check
        resp1 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-03-01T00:00:00+00:00"}},
        )
        # Page 2: past end_time, triggers break
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2024-06-01",
                "pageEndAt": "2024-06-02",
            },
            links={"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-07-01T00:00:00+00:00"}},
        )
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        call_count = [0]

        def fake_fromisoformat(s):
            call_count[0] += 1
            if call_count[0] == 1:
                return datetime(2024, 3, 1, 0, 0, 0, tzinfo=timezone.utc)
            return datetime(2024, 7, 1, 0, 0, 0, tzinfo=timezone.utc)

        with patch("meraki.session.sync.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
            mock_dt.fromisoformat = fake_fromisoformat
            results = list(
                session._get_pages_iterator(
                    metadata,
                    "/events",
                    direction="next",
                    event_log_end_time="2024-05-01T00:00:00Z",
                )
            )
        assert results == [{"ts": "a"}]

    @patch("time.sleep", return_value=None)
    def test_event_log_prev_breaks_before_2014(self, mock_sleep, session):
        # Page 1: endingBefore is after 2014, passes
        resp1 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2014-06-01",
                "pageEndAt": "2014-06-02",
            },
            links={"prev": {"url": "https://api.meraki.com/api/v1/events?endingBefore=2014-06-01T00:00:00Z"}},
        )
        # Page 2: endingBefore is before 2014, triggers break
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2014-01-01",
                "pageEndAt": "2014-01-02",
            },
            links={"prev": {"url": "https://api.meraki.com/api/v1/events?endingBefore=2013-12-31T00:00:00Z"}},
        )
        session._client.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        results = list(session._get_pages_iterator(metadata, "/events", direction="prev"))
        # Only page 1 yielded
        assert results == [{"ts": "a"}]
