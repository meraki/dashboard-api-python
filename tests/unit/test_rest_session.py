from unittest.mock import MagicMock, patch

import pytest
import requests

from meraki.exceptions import APIError, SessionInputError
from meraki.rest_session import RestSession, encode_params, user_agent_extended


@pytest.fixture
def session():
    with patch("meraki.rest_session.check_python_version"):
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


@pytest.fixture
def session_with_logger():
    with patch("meraki.rest_session.check_python_version"):
        s = RestSession(
            logger=MagicMock(),
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
            maximum_retries=2,
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
    reason="OK",
    headers=None,
    content=b'{"ok":true}',
    links=None,
):
    resp = MagicMock(spec=requests.Response)
    resp.status_code = status_code
    resp.reason = reason
    resp.headers = headers or {}
    resp.content = content
    resp.links = links or {}
    resp.json.return_value = json_data if json_data is not None else {"ok": True}
    resp.close = MagicMock()
    return resp


# --- encode_params tests ---


class TestEncodeParams:
    def test_string_passthrough(self):
        assert encode_params(None, "already_encoded") == "already_encoded"

    def test_bytes_passthrough(self):
        assert encode_params(None, b"raw") == b"raw"

    def test_file_like_passthrough(self):
        class FakeFile:
            def read(self):
                pass

        f = FakeFile()
        assert encode_params(None, f) is f

    def test_simple_dict(self):
        result = encode_params(None, {"key": "value"})
        assert "key=value" in result

    def test_list_values(self):
        result = encode_params(None, {"tag": ["a", "b"]})
        assert "tag=a" in result
        assert "tag=b" in result

    def test_dict_values_appended_keys(self):
        result = encode_params(None, {"param[]": [{"key1": "val1"}, {"key2": "val2"}]})
        assert "param%5B%5Dkey1=val1" in result
        assert "param%5B%5Dkey2=val2" in result

    def test_none_passthrough(self):
        assert encode_params(None, 42) == 42


# --- user_agent_extended tests ---


class TestUserAgentExtended:
    def test_with_caller(self):
        result = user_agent_extended(None, "MyApp MyVendor")
        assert "MyApp MyVendor" in result

    def test_with_be_geo_id_fallback(self):
        result = user_agent_extended("geo123", None)
        assert "geo123" in result

    def test_unidentified_fallback(self):
        result = user_agent_extended(None, None)
        assert "unidentified" in result


# --- Retry logic tests ---


class TestRetryLogic:
    @patch("time.sleep", return_value=None)
    def test_retry_on_429_with_retry_after(self, mock_sleep, session):
        resp_429 = _mock_response(
            429, reason="Too Many Requests", headers={"Retry-After": "1"}
        )
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_429, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200
        mock_sleep.assert_called_with(1)

    @patch("time.sleep", return_value=None)
    def test_retry_on_429_without_retry_after(self, mock_sleep, session):
        resp_429 = _mock_response(429, reason="Too Many Requests", headers={})
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_429, resp_200])

        with patch("random.randint", return_value=1):
            result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_429_raises_after_max_retries(self, mock_sleep, session):
        session._maximum_retries = 2
        resp_429 = _mock_response(
            429, reason="Too Many Requests", headers={"Retry-After": "1"}
        )
        session._req_session.request = MagicMock(return_value=resp_429)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_429_raises_immediately_when_wait_disabled(self, mock_sleep, session):
        session._wait_on_rate_limit = False
        resp_429 = _mock_response(429, reason="Too Many Requests", headers={})
        session._req_session.request = MagicMock(return_value=resp_429)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_retry_on_5xx(self, mock_sleep, session):
        resp_500 = _mock_response(500, reason="Internal Server Error")
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_500, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_5xx_raises_after_max_retries(self, mock_sleep, session):
        session._maximum_retries = 2
        resp_500 = _mock_response(500, reason="Internal Server Error")
        session._req_session.request = MagicMock(return_value=resp_500)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")


# --- X-Request-Id logging on 5xx ---


class TestRequestIdLoggingOn5xx:
    @patch("time.sleep", return_value=None)
    def test_request_id_logged_in_warning(self, mock_sleep, session_with_logger):
        session = session_with_logger
        resp_500 = _mock_response(
            500,
            reason="Internal Server Error",
            headers={"X-Request-Id": "abc123def456"},
        )
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_500, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")

        assert result.status_code == 200
        warning_messages = [c.args[0] for c in session._logger.warning.call_args_list]
        assert any("X-Request-Id: abc123def456" in m for m in warning_messages)

    @patch("time.sleep", return_value=None)
    def test_request_id_logged_as_error_after_exhausting_retries(self, mock_sleep, session_with_logger):
        session = session_with_logger
        session._maximum_retries = 2
        resp_500 = _mock_response(
            500,
            reason="Internal Server Error",
            headers={"X-Request-Id": "deadbeef00112233"},
        )
        session._req_session.request = MagicMock(return_value=resp_500)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

        error_messages = [c.args[0] for c in session._logger.error.call_args_list]
        assert any("deadbeef00112233" in m for m in error_messages)
        assert any("Provide this X-Request-Id to Meraki" in m for m in error_messages)

    @patch("time.sleep", return_value=None)
    def test_no_request_id_logs_none(self, mock_sleep, session_with_logger):
        session = session_with_logger
        session._maximum_retries = 2
        resp_500 = _mock_response(500, reason="Internal Server Error", headers={})
        session._req_session.request = MagicMock(return_value=resp_500)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

        warning_messages = [c.args[0] for c in session._logger.warning.call_args_list]
        assert any("X-Request-Id: none" in m for m in warning_messages)
        error_messages = [c.args[0] for c in session._logger.error.call_args_list]
        assert any("log lookup: none" in m for m in error_messages)

    @patch("time.sleep", return_value=None)
    def test_retry_on_connection_error(self, mock_sleep, session):
        exc = requests.exceptions.ConnectionError("Connection refused")
        exc.response = None
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[exc, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_connection_error_raises_after_max_retries(self, mock_sleep, session):
        session._maximum_retries = 1
        exc = requests.exceptions.ConnectionError("Connection refused")
        exc.response = None
        session._req_session.request = MagicMock(side_effect=[exc])

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")


# --- Pagination tests ---


class TestPaginationLegacy:
    @patch("time.sleep", return_value=None)
    def test_single_page(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._req_session.request = MagicMock(return_value=resp)

        result = session._get_pages_legacy(_metadata(), "/organizations")
        assert result == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_multiple_pages(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "1"}],
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"
                }
            },
        )
        resp2 = _mock_response(200, json_data=[{"id": "2"}], links={})
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(
            _metadata(), "/organizations", total_pages=-1
        )
        assert result == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_limit(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "1"}],
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"
                }
            },
        )
        resp2 = _mock_response(
            200,
            json_data=[{"id": "2"}],
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/organizations?startingAfter=2"
                }
            },
        )
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(_metadata(), "/organizations", total_pages=2)
        assert result == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_string_all(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._req_session.request = MagicMock(return_value=resp)

        result = session._get_pages_legacy(
            _metadata(), "/organizations", total_pages="all"
        )
        assert result == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_invalid_raises(self, mock_sleep, session):
        with pytest.raises(SessionInputError):
            session._get_pages_legacy(
                _metadata(), "/organizations", total_pages="invalid"
            )

    @patch("time.sleep", return_value=None)
    def test_204_no_content(self, mock_sleep, session):
        resp = _mock_response(204, json_data=None, reason="No Content", links={})
        session._req_session.request = MagicMock(return_value=resp)

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
            links={
                "next": {"url": "https://api.meraki.com/api/v1/things?startingAfter=1"}
            },
        )
        resp2 = _mock_response(
            200,
            json_data={
                "items": [{"id": "2"}],
                "meta": {"counts": {"items": {"remaining": 0}}},
            },
            links={},
        )
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        result = session._get_pages_legacy(_metadata(), "/things", total_pages=-1)
        assert result["items"] == [{"id": "1"}, {"id": "2"}]
        assert result["meta"]["counts"]["items"]["remaining"] == 0


class TestPaginationIterator:
    @patch("time.sleep", return_value=None)
    def test_single_page_yields_items(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}, {"id": "2"}], links={})
        session._req_session.request = MagicMock(return_value=resp)

        results = list(session._get_pages_iterator(_metadata(), "/organizations"))
        assert results == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_multiple_pages_yields_all(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "1"}],
            links={
                "next": {"url": "https://api.meraki.com/api/v1/orgs?startingAfter=1"}
            },
        )
        resp2 = _mock_response(200, json_data=[{"id": "2"}], links={})
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        results = list(
            session._get_pages_iterator(_metadata(), "/organizations", total_pages=-1)
        )
        assert results == [{"id": "1"}, {"id": "2"}]

    @patch("time.sleep", return_value=None)
    def test_items_dict_yields_items(self, mock_sleep, session):
        resp = _mock_response(
            200, json_data={"items": [{"id": "a"}, {"id": "b"}]}, links={}
        )
        session._req_session.request = MagicMock(return_value=resp)

        results = list(session._get_pages_iterator(_metadata(), "/things"))
        assert results == [{"id": "a"}, {"id": "b"}]


# --- 4xx error handling tests ---


class TestHandle4xxErrors:
    @patch("time.sleep", return_value=None)
    def test_generic_4xx_raises_immediately(self, mock_sleep, session):
        resp_400 = _mock_response(
            400, json_data={"errors": ["bad request"]}, reason="Bad Request"
        )
        session._req_session.request = MagicMock(return_value=resp_400)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")

    @patch("time.sleep", return_value=None)
    def test_network_delete_concurrency_retries(self, mock_sleep, session):
        resp_400 = _mock_response(
            400,
            json_data={"errors": ["concurrent requests detected"]},
            reason="Bad Request",
        )
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_400, resp_200])

        with patch("random.randint", return_value=1):
            result = session.request(
                _metadata(operation="deleteNetwork"), "DELETE", "/networks/123"
            )
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_action_batch_concurrency_retries(self, mock_sleep, session):
        resp_400 = _mock_response(
            400,
            json_data={"errors": ["Too many concurrently executing batches"]},
            reason="Bad Request",
        )
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_400, resp_200])

        result = session.request(_metadata(operation="createBatch"), "POST", "/batches")
        assert result.status_code == 200

    @patch("time.sleep", return_value=None)
    def test_retry_4xx_when_enabled(self, mock_sleep, session):
        session._retry_4xx_error = True
        resp_400 = _mock_response(
            400, json_data={"errors": ["something"]}, reason="Bad Request"
        )
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_400, resp_200])

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
        session._req_session.request = MagicMock(return_value=resp_200)
        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200


# --- 3xx redirect ---


class TestRedirect:
    @patch("time.sleep", return_value=None)
    def test_follows_redirect(self, mock_sleep, session):
        resp_301 = _mock_response(
            301,
            reason="Moved",
            headers={"Location": "https://n123.meraki.com/api/v1/organizations"},
        )
        resp_200 = _mock_response(200)
        session._req_session.request = MagicMock(side_effect=[resp_301, resp_200])

        result = session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200


# --- prepare_request ---


class TestPrepareRequest:
    def test_sets_timeout(self, session):
        kwargs = {}
        session.prepare_request(kwargs)
        assert kwargs["timeout"] == 60

    def test_sets_certificate(self, session):
        session._certificate_path = "/path/to/cert.pem"
        kwargs = {}
        session.prepare_request(kwargs)
        assert kwargs["verify"] == "/path/to/cert.pem"

    def test_sets_proxy(self, session):
        session._requests_proxy = "https://proxy:8080"
        kwargs = {}
        session.prepare_request(kwargs)
        assert kwargs["proxies"] == {"https": "https://proxy:8080"}

    def test_does_not_override_existing(self, session):
        kwargs = {"timeout": 30}
        session.prepare_request(kwargs)
        assert kwargs["timeout"] == 30


# --- HTTP verb methods ---


class TestHTTPVerbs:
    def test_get_returns_json(self, session):
        resp = _mock_response(200, json_data={"id": "1"}, content=b'{"id":"1"}')
        session._req_session.request = MagicMock(return_value=resp)
        result = session.get(_metadata(), "/organizations")
        assert result == {"id": "1"}

    def test_get_returns_none_on_empty_content(self, session):
        resp = _mock_response(200, json_data=None, content=b"   ")
        session._req_session.request = MagicMock(return_value=resp)
        result = session.get(_metadata(), "/organizations")
        assert result is None

    def test_get_returns_none_when_simulated(self, session):
        session._simulate = True
        resp = _mock_response(200, json_data={"id": "1"}, content=b'{"id":"1"}')
        session._req_session.request = MagicMock(return_value=resp)
        # GET still goes through in simulate mode
        result = session.get(_metadata(), "/organizations")
        assert result == {"id": "1"}

    def test_post_returns_json(self, session):
        resp = _mock_response(201, json_data={"id": "new"}, content=b'{"id":"new"}')
        session._req_session.request = MagicMock(return_value=resp)
        result = session.post(_metadata(), "/organizations", json={"name": "Test"})
        assert result == {"id": "new"}

    def test_post_returns_none_on_empty_content(self, session):
        resp = _mock_response(204, json_data=None, content=b"")
        session._req_session.request = MagicMock(return_value=resp)
        result = session.post(_metadata(), "/organizations", json={"name": "Test"})
        assert result is None

    def test_put_returns_json(self, session):
        resp = _mock_response(
            200, json_data={"id": "updated"}, content=b'{"id":"updated"}'
        )
        session._req_session.request = MagicMock(return_value=resp)
        result = session.put(_metadata(), "/organizations/1", json={"name": "New"})
        assert result == {"id": "updated"}

    def test_put_returns_none_on_empty_content(self, session):
        resp = _mock_response(200, json_data=None, content=b"  ")
        session._req_session.request = MagicMock(return_value=resp)
        result = session.put(_metadata(), "/organizations/1", json={"name": "New"})
        assert result is None

    def test_delete_returns_none(self, session):
        resp = _mock_response(204, reason="No Content", content=b"")
        session._req_session.request = MagicMock(return_value=resp)
        result = session.delete(_metadata(), "/organizations/1")
        assert result is None


# --- Connection error with response object ---


class TestConnectionErrorWithResponse:
    @patch("time.sleep", return_value=None)
    def test_connection_error_with_response_status(self, mock_sleep, session):
        session._maximum_retries = 1
        exc = requests.exceptions.ConnectionError("refused")
        exc.response = MagicMock()
        exc.response.status_code = 502
        session._req_session.request = MagicMock(side_effect=[exc])

        with pytest.raises(APIError) as exc_info:
            session.request(_metadata(), "GET", "/organizations")
        assert exc_info.value.status == 502


# --- JSON decode retry exhaustion ---


class TestJSONDecodeRetryExhaustion:
    @patch("time.sleep", return_value=None)
    def test_bad_json_raises_after_max_retries(self, mock_sleep, session):
        import json as json_mod

        session._maximum_retries = 2
        resp = _mock_response(200, content=b'{"ok":true}')
        resp.json.side_effect = json_mod.decoder.JSONDecodeError("", "", 0)
        session._req_session.request = MagicMock(return_value=resp)

        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/organizations")


# --- Pagination legacy: prev direction and event log ---


class TestPaginationLegacyExtended:
    @patch("time.sleep", return_value=None)
    def test_prev_direction(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "2"}],
            links={
                "prev": {"url": "https://api.meraki.com/api/v1/orgs?endingBefore=2"}
            },
        )
        resp2 = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

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
        session._req_session.request = MagicMock(return_value=resp)

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
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2024-01-01T00:00:00+00:00"
                }
            },
        )
        session._req_session.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        with patch("meraki.rest_session.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(
                2024, 1, 1, 0, 2, 0, tzinfo=timezone.utc
            )
            mock_dt.fromisoformat.return_value = datetime(
                2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            )
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
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2024-06-01T00:00:00+00:00"
                }
            },
        )
        session._req_session.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        with patch("meraki.rest_session.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(
                2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            )
            mock_dt.fromisoformat.return_value = datetime(
                2024, 6, 1, 0, 0, 0, tzinfo=timezone.utc
            )
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
            links={
                "prev": {
                    "url": "https://api.meraki.com/api/v1/events?endingBefore=2013-12-31T00:00:00Z"
                }
            },
        )
        session._req_session.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        result = session._get_pages_legacy(metadata, "/events", direction="prev")
        assert result["events"] == [{"ts": "a"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_numeric_string(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._req_session.request = MagicMock(return_value=resp)

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
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2014-06-01T00:00:00+00:00"
                }
            },
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
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        from datetime import datetime, timezone

        with patch("meraki.rest_session.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(
                2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            )
            mock_dt.fromisoformat.return_value = datetime(
                2014, 6, 1, 0, 0, 0, tzinfo=timezone.utc
            )
            result = session._get_pages_legacy(metadata, "/events", direction="next")

        # First page reversed, second page reversed and appended
        assert result["events"] == [{"ts": "a"}, {"ts": "b"}, {"ts": "c"}, {"ts": "d"}]
        assert result["pageStartAt"] == "2024-01-01T00:00:00Z"
        assert result["pageEndAt"] == "2024-01-01T02:00:00Z"


# --- Pagination iterator: extended coverage ---


class TestPaginationIteratorExtended:
    @patch("time.sleep", return_value=None)
    def test_total_pages_numeric_string(self, mock_sleep, session):
        resp = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._req_session.request = MagicMock(return_value=resp)

        results = list(
            session._get_pages_iterator(_metadata(), "/orgs", total_pages="3")
        )
        assert results == [{"id": "1"}]

    @patch("time.sleep", return_value=None)
    def test_total_pages_invalid_raises(self, mock_sleep, session):
        with pytest.raises(SessionInputError):
            list(
                session._get_pages_iterator(_metadata(), "/orgs", total_pages="invalid")
            )

    @patch("time.sleep", return_value=None)
    def test_prev_direction(self, mock_sleep, session):
        resp1 = _mock_response(
            200,
            json_data=[{"id": "2"}],
            links={
                "prev": {"url": "https://api.meraki.com/api/v1/orgs?endingBefore=2"}
            },
        )
        resp2 = _mock_response(200, json_data=[{"id": "1"}], links={})
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        results = list(
            session._get_pages_iterator(_metadata(), "/orgs", direction="prev")
        )
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
        session._req_session.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        results = list(
            session._get_pages_iterator(metadata, "/events", direction="next")
        )
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
        session._req_session.request = MagicMock(return_value=resp)

        metadata = _metadata(operation="someOp")
        results = list(
            session._get_pages_iterator(metadata, "/events", direction="prev")
        )
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
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2014-06-01T00:00:00+00:00"
                }
            },
        )
        # Page 2: too recent, triggers break before yielding
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2025-01-01",
                "pageEndAt": "2025-01-02",
            },
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2025-01-01T23:58:00+00:00"
                }
            },
        )
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        call_count = [0]

        def fake_fromisoformat(s):
            call_count[0] += 1
            if call_count[0] == 1:
                return datetime(2014, 6, 1, 0, 0, 0, tzinfo=timezone.utc)
            return datetime(2025, 1, 1, 23, 58, 0, tzinfo=timezone.utc)

        with patch("meraki.rest_session.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(
                2025, 1, 2, 0, 0, 0, tzinfo=timezone.utc
            )
            mock_dt.fromisoformat = fake_fromisoformat
            results = list(
                session._get_pages_iterator(metadata, "/events", direction="next")
            )
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
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2024-03-01T00:00:00+00:00"
                }
            },
        )
        # Page 2: past end_time, triggers break
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2024-06-01",
                "pageEndAt": "2024-06-02",
            },
            links={
                "next": {
                    "url": "https://api.meraki.com/api/v1/events?startingAfter=2024-07-01T00:00:00+00:00"
                }
            },
        )
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        call_count = [0]

        def fake_fromisoformat(s):
            call_count[0] += 1
            if call_count[0] == 1:
                return datetime(2024, 3, 1, 0, 0, 0, tzinfo=timezone.utc)
            return datetime(2024, 7, 1, 0, 0, 0, tzinfo=timezone.utc)

        with patch("meraki.rest_session.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(
                2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc
            )
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
            links={
                "prev": {
                    "url": "https://api.meraki.com/api/v1/events?endingBefore=2014-06-01T00:00:00Z"
                }
            },
        )
        # Page 2: endingBefore is before 2014, triggers break
        resp2 = _mock_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2014-01-01",
                "pageEndAt": "2014-01-02",
            },
            links={
                "prev": {
                    "url": "https://api.meraki.com/api/v1/events?endingBefore=2013-12-31T00:00:00Z"
                }
            },
        )
        session._req_session.request = MagicMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        results = list(
            session._get_pages_iterator(metadata, "/events", direction="prev")
        )
        # Only page 1 yielded
        assert results == [{"ts": "a"}]
