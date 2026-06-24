import json
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from meraki.exceptions import APIError

from tests.unit.conftest import make_metadata as _metadata, make_async_mock_response as _mock_aio_response


async def _noop_sleep(*args, **kwargs):
    pass


SLEEP_PATCH = "meraki.session.async_.asyncio.sleep"


# --- Init tests ---


class TestAsyncInit:
    def test_certificate_path_passed_to_client(self, async_session_with_cert):
        assert async_session_with_cert._certificate_path

    def test_proxy_stored(self, async_session_with_proxy):
        assert async_session_with_proxy._requests_proxy == "http://proxy:8080"

    def test_logger_logs_init(self, async_session_with_logger):
        async_session_with_logger._logger.info.assert_called_once()
        call_args = async_session_with_logger._logger.info.call_args[0][0]
        assert "initialized" in call_args

    def test_use_iterator_property_setter(self, async_session):
        async_session.use_iterator_for_get_pages = True
        assert async_session._use_iterator_for_get_pages is True
        assert async_session.get_pages == async_session._get_pages_iterator

        async_session.use_iterator_for_get_pages = False
        assert async_session._use_iterator_for_get_pages is False
        assert async_session.get_pages == async_session._get_pages_legacy


# --- Request kwargs (cert, proxy, timeout) ---


class TestAsyncRequestKwargs:
    @pytest.mark.asyncio
    async def test_follow_redirects_false(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp_200)

        await async_session.request(_metadata(), "GET", "/orgs")
        call_kwargs = async_session._client.request.call_args[1]
        assert call_kwargs.get("follow_redirects") is False


# --- URL handling ---


class TestAsyncURLHandling:
    @pytest.mark.asyncio
    async def test_relative_url_prepends_base(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp_200)

        await async_session.request(_metadata(), "GET", "/organizations")
        call_args = async_session._client.request.call_args[0]
        assert call_args[1] == "https://api.meraki.com/api/v1/organizations"

    @pytest.mark.asyncio
    async def test_absolute_meraki_url_not_prepended(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp_200)

        await async_session.request(_metadata(), "GET", "https://n123.meraki.com/api/v1/orgs")
        call_args = async_session._client.request.call_args[0]
        assert call_args[1] == "https://n123.meraki.com/api/v1/orgs"

    @pytest.mark.asyncio
    async def test_meraki_cn_domain_recognized(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp_200)

        await async_session.request(_metadata(), "GET", "https://n123.meraki.cn/api/v1/orgs")
        call_args = async_session._client.request.call_args[0]
        assert call_args[1] == "https://n123.meraki.cn/api/v1/orgs"

    @pytest.mark.asyncio
    async def test_non_string_url_converted(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp_200)

        class FakeURL:
            def __str__(self):
                return "https://n1.meraki.com/api/v1/orgs"

        await async_session.request(_metadata(), "GET", FakeURL())
        call_args = async_session._client.request.call_args[0]
        assert call_args[1] == "https://n1.meraki.com/api/v1/orgs"


# --- Retry on 429 ---


class TestAsyncRetry429:
    @pytest.mark.asyncio
    async def test_retry_on_429_with_retry_after(self, async_session):
        resp_429 = _mock_aio_response(status_code=429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_429, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_retry_on_429_without_retry_after(self, async_session):
        resp_429 = _mock_aio_response(status_code=429, reason_phrase="Too Many Requests")
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_429, resp_200])

        with (
            patch(SLEEP_PATCH, side_effect=_noop_sleep),
            patch("random.randint", return_value=1),
        ):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_429_raises_after_max_retries(self, async_session):
        async_session._maximum_retries = 2
        resp_429 = _mock_aio_response(status_code=429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        async_session._client.request = AsyncMock(return_value=resp_429)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")

    @pytest.mark.asyncio
    async def test_429_retry_count_matches_maximum_retries(self, async_session):
        async_session._maximum_retries = 3
        resp_429 = _mock_aio_response(status_code=429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        async_session._client.request = AsyncMock(return_value=resp_429)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")

        assert async_session._client.request.call_count == 3

    @pytest.mark.asyncio
    async def test_429_uses_retry_after_header_value(self, async_session):
        resp_429 = _mock_aio_response(status_code=429, reason_phrase="Too Many Requests", headers={"Retry-After": "42"})
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_429, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep) as mock_sleep:
            await async_session.request(_metadata(), "GET", "/organizations")

        mock_sleep.assert_called_once_with(42)


# --- Retry on 5xx ---


class TestAsyncRetry5xx:
    @pytest.mark.asyncio
    async def test_retry_on_500(self, async_session):
        resp_500 = _mock_aio_response(status_code=500, reason_phrase="Internal Server Error")
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_500, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_5xx_raises_after_max_retries(self, async_session):
        async_session._maximum_retries = 2
        resp_500 = _mock_aio_response(status_code=500, reason_phrase="Internal Server Error")
        async_session._client.request = AsyncMock(return_value=resp_500)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")

    @pytest.mark.asyncio
    async def test_request_id_logged_in_warning(self, async_session_with_logger):
        session = async_session_with_logger
        resp_500 = _mock_aio_response(
            status_code=500,
            reason_phrase="Internal Server Error",
            headers={"X-Request-Id": "abc123def456"},
        )
        resp_200 = _mock_aio_response(status_code=200)
        session._client.request = AsyncMock(side_effect=[resp_500, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await session.request(_metadata(), "GET", "/organizations")

        assert result.status_code == 200
        warning_messages = [c.args[0] for c in session._logger.warning.call_args_list]
        assert any("X-Request-Id: abc123def456" in m for m in warning_messages)

    @pytest.mark.asyncio
    async def test_request_id_logged_as_error_after_exhausting_retries(self, async_session_with_logger):
        session = async_session_with_logger
        session._maximum_retries = 2
        resp_500 = _mock_aio_response(
            status_code=500,
            reason_phrase="Internal Server Error",
            headers={"X-Request-Id": "deadbeef00112233"},
        )
        session._client.request = AsyncMock(return_value=resp_500)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await session.request(_metadata(), "GET", "/organizations")

        error_messages = [c.args[0] for c in session._logger.error.call_args_list]
        assert any("deadbeef00112233" in m for m in error_messages)
        assert any("Provide this X-Request-Id to Meraki" in m for m in error_messages)

    @pytest.mark.asyncio
    async def test_no_request_id_logs_none(self, async_session_with_logger):
        session = async_session_with_logger
        session._maximum_retries = 2
        resp_500 = _mock_aio_response(status_code=500, reason_phrase="Internal Server Error", headers={})
        session._client.request = AsyncMock(return_value=resp_500)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await session.request(_metadata(), "GET", "/organizations")

        warning_messages = [c.args[0] for c in session._logger.warning.call_args_list]
        assert any("X-Request-Id: none" in m for m in warning_messages)
        error_messages = [c.args[0] for c in session._logger.error.call_args_list]
        assert any("log lookup: none" in m for m in error_messages)


# --- Connection errors ---


class TestAsyncConnectionErrors:
    @pytest.mark.asyncio
    async def test_retry_on_exception(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[httpx.ConnectError("Connection refused"), resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_exception_raises_after_max_retries(self, async_session):
        async_session._maximum_retries = 2
        async_session._client.request = AsyncMock(side_effect=httpx.ConnectError("Connection refused"))

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")


# --- 4xx errors ---


class TestAsync4xx:
    @pytest.mark.asyncio
    async def test_generic_4xx_raises(self, async_session):
        resp_400 = _mock_aio_response(status_code=400, json_data={"errors": ["bad"]}, reason_phrase="Bad Request")
        async_session._client.request = AsyncMock(return_value=resp_400)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")

    @pytest.mark.asyncio
    async def test_retry_4xx_when_enabled(self, async_session):
        async_session._retry_4xx_error = True
        resp_400 = _mock_aio_response(status_code=400, json_data={"errors": ["something"]}, reason_phrase="Bad Request")
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_400, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with patch("random.randint", return_value=1):
                result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_network_delete_concurrency_retries(self, async_session):
        async_session._maximum_retries = 3
        error_msg = {"errors": ["This may be due to concurrent requests to delete networks. Please retry."]}
        resp_400 = _mock_aio_response(status_code=400, json_data=error_msg, reason_phrase="Bad Request")
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_400, resp_200])

        with (
            patch(SLEEP_PATCH, side_effect=_noop_sleep),
            patch("random.randint", return_value=1),
        ):
            result = await async_session.request(_metadata(operation="deleteNetwork"), "GET", "/networks")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_network_delete_concurrency_exhausts_retries(self, async_session):
        async_session._maximum_retries = 2
        error_msg = {"errors": ["This may be due to concurrent requests to delete networks. Please retry."]}
        resp_400 = _mock_aio_response(status_code=400, json_data=error_msg, reason_phrase="Bad Request")
        async_session._client.request = AsyncMock(return_value=resp_400)

        with (
            patch(SLEEP_PATCH, side_effect=_noop_sleep),
            patch("random.randint", return_value=1),
        ):
            with pytest.raises(APIError):
                await async_session.request(_metadata(operation="deleteNetwork"), "GET", "/networks")

    @pytest.mark.asyncio
    async def test_action_batch_concurrency_retries(self, async_session):
        error_msg = {
            "errors": ["Too many concurrently executing batches. Maximum is 5 confirmed but not yet executed batches."]
        }
        resp_400 = _mock_aio_response(status_code=400, json_data=error_msg, reason_phrase="Bad Request")
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_400, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/batches")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_4xx_non_json_response(self, async_session):
        resp_400 = MagicMock()
        resp_400.status_code = 400
        resp_400.reason_phrase = "Bad Request"
        resp_400.headers = {}
        resp_400.links = {}
        resp_400.json = MagicMock(side_effect=json.decoder.JSONDecodeError("", "", 0))
        resp_400.text = "Some HTML error page content"
        resp_400.close = MagicMock()

        async_session._client.request = AsyncMock(return_value=resp_400)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")

    @pytest.mark.asyncio
    async def test_4xx_non_json_text_fails_too(self, async_session):
        resp_400 = MagicMock()
        resp_400.status_code = 400
        resp_400.reason_phrase = "Bad Request"
        resp_400.headers = {}
        resp_400.links = {}
        resp_400.json = MagicMock(side_effect=ValueError("Invalid JSON"))
        resp_400.text = MagicMock(side_effect=Exception("read error"))
        resp_400.close = MagicMock()

        async_session._client.request = AsyncMock(return_value=resp_400)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")

    @pytest.mark.asyncio
    async def test_4xx_non_dict_json_response(self, async_session):
        resp_400 = _mock_aio_response(status_code=400, json_data="just a string", reason_phrase="Bad Request")
        async_session._client.request = AsyncMock(return_value=resp_400)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session.request(_metadata(), "GET", "/organizations")


# --- 3xx redirect ---


class TestAsyncRedirect:
    @pytest.mark.asyncio
    async def test_follows_redirect(self, async_session):
        resp_301 = _mock_aio_response(
            status_code=301,
            reason_phrase="Moved",
            headers={"Location": "https://n123.meraki.com/api/v1/organizations"},
        )
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_301, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200
        assert async_session._base_url == "https://n123.meraki.com/api/v1"

    @pytest.mark.asyncio
    async def test_redirect_to_cn_domain(self, async_session):
        resp_301 = _mock_aio_response(
            status_code=301,
            reason_phrase="Moved",
            headers={"Location": "https://n123.meraki.cn/api/v1/organizations"},
        )
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(side_effect=[resp_301, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200
        assert "meraki.cn" in async_session._base_url


# --- Simulate mode ---


class TestAsyncSimulate:
    @pytest.mark.asyncio
    async def test_simulate_skips_non_get(self, async_session):
        async_session._simulate = True
        result = await async_session.request(_metadata(), "POST", "/organizations")
        assert result is None

    @pytest.mark.asyncio
    async def test_simulate_allows_get(self, async_session):
        async_session._simulate = True
        resp_200 = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp_200)

        result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_simulate_with_logger(self, async_session_with_logger):
        async_session_with_logger._simulate = True
        result = await async_session_with_logger.request(_metadata(), "POST", "/organizations")
        assert result is None
        assert async_session_with_logger._logger.info.call_count >= 1


# --- 2xx response handling ---


class TestAsync2xxResponse:
    @pytest.mark.asyncio
    async def test_success_with_page_metadata(self, async_session_with_logger):
        resp_200 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        async_session_with_logger._client.request = AsyncMock(return_value=resp_200)

        metadata = _metadata()
        metadata["page"] = 3
        result = await async_session_with_logger.request(metadata, "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_success_without_page_metadata(self, async_session_with_logger):
        resp_200 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        async_session_with_logger._client.request = AsyncMock(return_value=resp_200)

        result = await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_get_retries_on_invalid_json(self, async_session):
        resp_bad_json = MagicMock()
        resp_bad_json.status_code = 200
        resp_bad_json.reason_phrase = "OK"
        resp_bad_json.headers = {}
        resp_bad_json.links = {}
        resp_bad_json.json = MagicMock(side_effect=json.decoder.JSONDecodeError("", "", 0))
        resp_bad_json.close = MagicMock(side_effect=RuntimeError("Attempted to call an sync close on an async stream."))
        resp_bad_json.aclose = AsyncMock()

        resp_200 = _mock_aio_response(status_code=200, json_data={"ok": True})

        async_session._client.request = AsyncMock(side_effect=[resp_bad_json, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200

    @pytest.mark.asyncio
    async def test_non_get_returns_without_json_validation(self, async_session):
        resp_200 = _mock_aio_response(status_code=200, json_data={"id": "abc"})
        async_session._client.request = AsyncMock(return_value=resp_200)

        result = await async_session.request(_metadata(), "POST", "/organizations")
        assert result.status_code == 200
        resp_200.json.assert_not_called()

    @pytest.mark.asyncio
    async def test_response_with_no_reason(self, async_session):
        resp_200 = _mock_aio_response(status_code=200)
        resp_200.reason = None
        async_session._client.request = AsyncMock(return_value=resp_200)

        result = await async_session.request(_metadata(), "GET", "/organizations")
        assert result.status_code == 200


# --- Logger coverage in request flow ---


class TestAsyncRequestLogging:
    @pytest.mark.asyncio
    async def test_logs_debug_metadata(self, async_session_with_logger):
        resp_200 = _mock_aio_response(status_code=200)
        async_session_with_logger._client.request = AsyncMock(return_value=resp_200)

        await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        async_session_with_logger._logger.debug.assert_called()

    @pytest.mark.asyncio
    async def test_logs_request_url(self, async_session_with_logger):
        resp_200 = _mock_aio_response(status_code=200)
        async_session_with_logger._client.request = AsyncMock(return_value=resp_200)

        await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        info_calls = [str(c) for c in async_session_with_logger._logger.info.call_args_list]
        assert any("GET" in c for c in info_calls)

    @pytest.mark.asyncio
    async def test_logs_warning_on_connection_error(self, async_session_with_logger):
        resp_200 = _mock_aio_response(status_code=200)
        async_session_with_logger._client.request = AsyncMock(side_effect=[httpx.ConnectError("timeout"), resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        async_session_with_logger._logger.warning.assert_called()

    @pytest.mark.asyncio
    async def test_logs_warning_on_429(self, async_session_with_logger):
        resp_429 = _mock_aio_response(status_code=429, reason_phrase="Too Many Requests", headers={"Retry-After": "1"})
        resp_200 = _mock_aio_response(status_code=200)
        async_session_with_logger._client.request = AsyncMock(side_effect=[resp_429, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        async_session_with_logger._logger.warning.assert_called()

    @pytest.mark.asyncio
    async def test_logs_warning_on_5xx(self, async_session_with_logger):
        resp_500 = _mock_aio_response(status_code=500, reason_phrase="Server Error")
        resp_200 = _mock_aio_response(status_code=200)
        async_session_with_logger._client.request = AsyncMock(side_effect=[resp_500, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        async_session_with_logger._logger.warning.assert_called()

    @pytest.mark.asyncio
    async def test_logs_error_on_4xx(self, async_session_with_logger):
        resp_400 = _mock_aio_response(status_code=400, json_data={"errors": ["bad"]}, reason_phrase="Bad Request")
        async_session_with_logger._client.request = AsyncMock(return_value=resp_400)

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            with pytest.raises(APIError):
                await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        async_session_with_logger._logger.error.assert_called()

    @pytest.mark.asyncio
    async def test_logs_warning_on_bad_json_200(self, async_session_with_logger):
        resp_bad = MagicMock()
        resp_bad.status_code = 200
        resp_bad.reason_phrase = "OK"
        resp_bad.headers = {}
        resp_bad.links = {}
        resp_bad.json = MagicMock(side_effect=ValueError("Invalid JSON"))
        resp_bad.close = MagicMock(side_effect=RuntimeError("Attempted to call an sync close on an async stream."))
        resp_bad.aclose = AsyncMock()

        resp_200 = _mock_aio_response(status_code=200)

        async_session_with_logger._client.request = AsyncMock(side_effect=[resp_bad, resp_200])

        with patch(SLEEP_PATCH, side_effect=_noop_sleep):
            await async_session_with_logger.request(_metadata(), "GET", "/organizations")
        async_session_with_logger._logger.warning.assert_called()


# --- HTTP verb methods (get, post, put, delete, close) ---


class TestAsyncHTTPVerbs:
    @pytest.mark.asyncio
    async def test_get(self, async_session):
        resp_200 = _mock_aio_response(status_code=200, json_data={"data": [1, 2, 3]})
        async_session._client.request = AsyncMock(return_value=resp_200)

        result = await async_session.get(_metadata(), "/organizations")
        assert result == {"data": [1, 2, 3]}

    @pytest.mark.asyncio
    async def test_get_with_params(self, async_session):
        resp_200 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        async_session._client.request = AsyncMock(return_value=resp_200)

        result = await async_session.get(_metadata(), "/organizations", params={"perPage": 10})
        assert result == [{"id": 1}]

    @pytest.mark.asyncio
    async def test_post(self, async_session):
        resp_201 = _mock_aio_response(status_code=201, json_data={"id": "new"})
        async_session._client.request = AsyncMock(return_value=resp_201)

        result = await async_session.post(_metadata(), "/organizations", json={"name": "Test"})
        assert result == {"id": "new"}

    @pytest.mark.asyncio
    async def test_put(self, async_session):
        resp_200 = _mock_aio_response(status_code=200, json_data={"id": "updated"})
        async_session._client.request = AsyncMock(return_value=resp_200)

        result = await async_session.put(_metadata(), "/organizations/1", json={"name": "New"})
        assert result == {"id": "updated"}

    @pytest.mark.asyncio
    async def test_delete(self, async_session):
        resp_204 = _mock_aio_response(status_code=204, json_data=None, reason_phrase="No Content")
        async_session._client.request = AsyncMock(return_value=resp_204)

        result = await async_session.delete(_metadata(), "/organizations/1")
        assert result is None

    @pytest.mark.asyncio
    async def test_delete_passes_query_params(self, async_session):
        resp_204 = _mock_aio_response(status_code=204, json_data=None, reason_phrase="No Content")
        async_session._client.request = AsyncMock(return_value=resp_204)

        params = {"force": "true"}
        result = await async_session.delete(_metadata(), "/networks/1/groupPolicies/1", params)
        assert result is None
        call_kwargs = async_session._client.request.call_args
        assert call_kwargs.kwargs.get("params") == params

    @pytest.mark.asyncio
    async def test_close(self, async_session):
        async_session._client.aclose = AsyncMock()
        await async_session.close()
        async_session._client.aclose.assert_called_once()


# --- Pagination: _get_pages_legacy ---


class TestAsyncPaginationLegacy:
    @pytest.mark.asyncio
    async def test_single_page_no_links(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}, {"id": 2}])
        async_session._client.request = AsyncMock(return_value=resp)

        result = await async_session._get_pages_legacy(_metadata(), "/organizations")
        assert result == [{"id": 1}, {"id": 2}]

    @pytest.mark.asyncio
    async def test_multiple_pages_list(self, async_session):
        resp1 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"}}
        resp2 = _mock_aio_response(status_code=200, json_data=[{"id": 2}])
        resp2.links = {}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        result = await async_session._get_pages_legacy(_metadata(), "/organizations")
        assert result == [{"id": 1}, {"id": 2}]

    @pytest.mark.asyncio
    async def test_total_pages_string_all(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        result = await async_session._get_pages_legacy(_metadata(), "/organizations", total_pages="all")
        assert result == [{"id": 1}]

    @pytest.mark.asyncio
    async def test_total_pages_numeric_string(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        result = await async_session._get_pages_legacy(_metadata(), "/organizations", total_pages="1")
        assert result == [{"id": 1}]

    @pytest.mark.asyncio
    async def test_total_pages_limit(self, async_session):
        resp1 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"}}
        resp2 = _mock_aio_response(status_code=200, json_data=[{"id": 2}])
        resp2.links = {"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=2"}}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        result = await async_session._get_pages_legacy(_metadata(), "/organizations", total_pages=2)
        assert result == [{"id": 1}, {"id": 2}]

    @pytest.mark.asyncio
    async def test_prev_direction(self, async_session):
        resp1 = _mock_aio_response(status_code=200, json_data=[{"id": 2}])
        resp1.links = {"prev": {"url": "https://api.meraki.com/api/v1/organizations?endingBefore=2"}}
        resp2 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp2.links = {}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        result = await async_session._get_pages_legacy(_metadata(), "/organizations", direction="prev")
        assert result == [{"id": 2}, {"id": 1}]

    @pytest.mark.asyncio
    async def test_items_dict_pagination(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "items": [{"id": 1}],
                "meta": {"counts": {"items": {"remaining": 1}}},
            },
        )
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/items?startingAfter=1"}}
        resp2 = _mock_aio_response(
            200,
            json_data={
                "items": [{"id": 2}],
                "meta": {"counts": {"items": {"remaining": 0}}},
            },
        )
        resp2.links = {}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        result = await async_session._get_pages_legacy(_metadata(), "/items")
        assert result == {
            "items": [{"id": 1}, {"id": 2}],
            "meta": {"counts": {"items": {"remaining": 0}}},
        }

    @pytest.mark.asyncio
    async def test_event_log_pagination_next(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "b"}, {"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
        )
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2014-06-01T00:00:00Z"}}
        resp2 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "d"}, {"ts": "c"}],
                "pageStartAt": "2024-01-01T01:00:00Z",
                "pageEndAt": "2024-01-01T02:00:00Z",
            },
        )
        resp2.links = {}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        with patch("meraki.session.async_.datetime") as mock_dt:
            mock_dt.now.return_value = type(
                "FakeDT",
                (),
                {"__sub__": lambda self, other: type("TD", (), {"total_seconds": lambda s: 86400})()},
            )()
            mock_dt.fromisoformat = lambda s: s
            result = await async_session._get_pages_legacy(metadata, "/events", direction="next")

        assert result["events"][0] == {"ts": "a"}
        assert result["events"][1] == {"ts": "b"}

    @pytest.mark.asyncio
    async def test_event_log_breaks_on_recent_starting_after(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "b"}, {"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
        )
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-01-01T00:00:00Z"}}
        async_session._client.request = AsyncMock(return_value=resp1)

        metadata = _metadata(operation="getNetworkEvents")
        from datetime import datetime

        with patch("meraki.session.async_.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2024, 1, 1, 0, 2, 0)
            mock_dt.fromisoformat.return_value = datetime(2024, 1, 1, 0, 0, 0)
            result = await async_session._get_pages_legacy(metadata, "/events", direction="next")

        assert result["events"] == [{"ts": "a"}, {"ts": "b"}]

    @pytest.mark.asyncio
    async def test_event_log_breaks_on_end_time(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01T00:00:00Z",
                "pageEndAt": "2024-01-01T01:00:00Z",
            },
        )
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-06-01T00:00:00Z"}}
        async_session._client.request = AsyncMock(return_value=resp1)

        metadata = _metadata(operation="getNetworkEvents")
        from datetime import datetime

        with patch("meraki.session.async_.datetime") as mock_dt:
            mock_dt.now.return_value = datetime(2025, 1, 1, 0, 0, 0)
            mock_dt.fromisoformat.return_value = datetime(2024, 6, 1, 0, 0, 0)
            result = await async_session._get_pages_legacy(
                metadata,
                "/events",
                direction="next",
                event_log_end_time="2024-05-01T00:00:00Z",
            )
        assert result["events"] == [{"ts": "a"}]

    @pytest.mark.asyncio
    async def test_event_log_prev_direction_breaks_before_2014(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2014-01-01T00:00:00Z",
                "pageEndAt": "2014-01-02T00:00:00Z",
            },
        )
        resp1.links = {"prev": {"url": "https://api.meraki.com/api/v1/events?endingBefore=2013-12-31T00:00:00Z"}}
        async_session._client.request = AsyncMock(return_value=resp1)

        metadata = _metadata(operation="getNetworkEvents")
        result = await async_session._get_pages_legacy(metadata, "/events", direction="prev")
        assert result["events"] == [{"ts": "a"}]


# --- Pagination: _get_pages_iterator ---


class TestAsyncPaginationIterator:
    @pytest.mark.asyncio
    async def test_single_page_yields_items(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}, {"id": 2}])
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/organizations"):
            items.append(item)
        assert items == [{"id": 1}, {"id": 2}]

    @pytest.mark.asyncio
    async def test_multiple_pages_yields_all(self, async_session):
        resp1 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/organizations?startingAfter=1"}}
        resp2 = _mock_aio_response(status_code=200, json_data=[{"id": 2}])
        resp2.links = {}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/organizations"):
            items.append(item)
        assert items == [{"id": 1}, {"id": 2}]

    @pytest.mark.asyncio
    async def test_total_pages_string_all(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/organizations", total_pages="all"):
            items.append(item)
        assert items == [{"id": 1}]

    @pytest.mark.asyncio
    async def test_total_pages_numeric_string(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/organizations", total_pages="2"):
            items.append(item)
        assert items == [{"id": 1}]

    @pytest.mark.asyncio
    async def test_items_dict_yields_items(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data={"items": [{"id": 1}, {"id": 2}]})
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/items"):
            items.append(item)
        assert items == [{"id": 1}, {"id": 2}]

    @pytest.mark.asyncio
    async def test_event_log_next_yields_reversed(self, async_session):
        resp = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "b"}, {"ts": "a"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
        )
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        metadata = _metadata(operation="getNetworkEvents")
        items = []
        async for item in async_session._get_pages_iterator(metadata, "/events", direction="next"):
            items.append(item)
        assert items == [{"ts": "a"}, {"ts": "b"}]

    @pytest.mark.asyncio
    async def test_event_log_prev_yields_normal(self, async_session):
        resp = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "a"}, {"ts": "b"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
        )
        resp.links = {}
        async_session._client.request = AsyncMock(return_value=resp)

        metadata = _metadata(operation="someOtherOp")
        items = []
        async for item in async_session._get_pages_iterator(metadata, "/events", direction="prev"):
            items.append(item)
        assert items == [{"ts": "a"}, {"ts": "b"}]

    @pytest.mark.asyncio
    async def test_prev_direction_pagination(self, async_session):
        resp1 = _mock_aio_response(status_code=200, json_data=[{"id": 2}])
        resp1.links = {"prev": {"url": "https://api.meraki.com/api/v1/orgs?endingBefore=2"}}
        resp2 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp2.links = {}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/orgs", direction="prev"):
            items.append(item)
        assert items == [{"id": 2}, {"id": 1}]

    @pytest.mark.asyncio
    async def test_iterator_event_log_breaks_on_recent(self, async_session):
        # First page yields normally (far enough in past), second page triggers break
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
        )
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-01-01T00:00:00Z"}}
        resp2 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2024-01-02",
                "pageEndAt": "2024-01-03",
            },
        )
        resp2.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-01-02T23:58:00Z"}}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        from datetime import datetime

        call_count = [0]

        def fake_now(tz=None):
            return datetime(2025, 1, 1, 0, 0, 0)

        def fake_fromisoformat(s):
            call_count[0] += 1
            if call_count[0] == 1:
                return datetime(2024, 1, 1, 0, 0, 0)
            return datetime(2025, 1, 1, 0, 0, 0)

        with patch("meraki.session.async_.datetime") as mock_dt:
            mock_dt.now = fake_now
            mock_dt.fromisoformat = fake_fromisoformat
            items = []
            async for item in async_session._get_pages_iterator(metadata, "/events", direction="next"):
                items.append(item)
        # First page yielded, second page triggered break (data lost)
        assert items == [{"ts": "a"}]

    @pytest.mark.asyncio
    async def test_iterator_event_log_breaks_on_end_time(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2024-01-01",
                "pageEndAt": "2024-01-02",
            },
        )
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-04-01T00:00:00Z"}}
        resp2 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2024-04-01",
                "pageEndAt": "2024-05-01",
            },
        )
        resp2.links = {"next": {"url": "https://api.meraki.com/api/v1/events?startingAfter=2024-06-01T00:00:00Z"}}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        from datetime import datetime

        call_count = [0]

        def fake_now(tz=None):
            return datetime(2025, 1, 1, 0, 0, 0)

        def fake_fromisoformat(s):
            call_count[0] += 1
            if call_count[0] == 1:
                return datetime(2024, 4, 1, 0, 0, 0)
            return datetime(2024, 6, 1, 0, 0, 0)

        with patch("meraki.session.async_.datetime") as mock_dt:
            mock_dt.now = fake_now
            mock_dt.fromisoformat = fake_fromisoformat
            items = []
            async for item in async_session._get_pages_iterator(
                metadata,
                "/events",
                direction="next",
                event_log_end_time="2024-05-01T00:00:00Z",
            ):
                items.append(item)
        assert items == [{"ts": "a"}]

    @pytest.mark.asyncio
    async def test_iterator_event_log_prev_breaks_before_2014(self, async_session):
        resp1 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "a"}],
                "pageStartAt": "2014-06-01",
                "pageEndAt": "2014-06-02",
            },
        )
        resp1.links = {"prev": {"url": "https://api.meraki.com/api/v1/events?endingBefore=2014-06-01T00:00:00Z"}}
        resp2 = _mock_aio_response(
            200,
            json_data={
                "events": [{"ts": "b"}],
                "pageStartAt": "2013-01-01",
                "pageEndAt": "2013-12-31",
            },
        )
        resp2.links = {"prev": {"url": "https://api.meraki.com/api/v1/events?endingBefore=2013-06-01T00:00:00Z"}}
        async_session._client.request = AsyncMock(side_effect=[resp1, resp2])

        metadata = _metadata(operation="getNetworkEvents")
        items = []
        async for item in async_session._get_pages_iterator(metadata, "/events", direction="prev"):
            items.append(item)
        # First page yielded, second triggers break
        assert items == [{"ts": "a"}]


# --- download_page helper ---


class TestAsyncDownloadPage:
    @pytest.mark.asyncio
    async def test_download_page(self, async_session):
        resp = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        request_coro = AsyncMock(return_value=resp)()
        response, result = await async_session._download_page(request_coro)
        assert result == [{"id": 1}]
        assert response.status_code == 200

    @pytest.mark.asyncio
    async def test_download_page_204_no_json(self, async_session):
        """A 204 page yields result=None without calling .json()."""
        resp = _mock_aio_response(status_code=204, reason_phrase="No Content", content=b"")
        resp.json = MagicMock(side_effect=json.decoder.JSONDecodeError("", "", 0))
        request_coro = AsyncMock(return_value=resp)()
        response, result = await async_session._download_page(request_coro)
        assert result is None
        resp.json.assert_not_called()


# --- Fix #4: async iterator 204 guard ---


class TestAsyncIterator204Guard:
    @pytest.mark.asyncio
    async def test_204_page_terminates_iterator_cleanly(self, async_session):
        """A 204 page terminates the async iterator without JSONDecodeError."""
        resp_204 = _mock_aio_response(status_code=204, reason_phrase="No Content", content=b"")
        resp_204.links = {}
        resp_204.json = MagicMock(side_effect=json.decoder.JSONDecodeError("", "", 0))
        async_session._client.request = AsyncMock(return_value=resp_204)

        items = []
        async for item in async_session._get_pages_iterator(_metadata(), "/organizations"):
            items.append(item)
        assert items == []
        resp_204.json.assert_not_called()


# --- Fix #5: smart-flow GET parses JSON only once ---


class TestAsyncSuccessSingleParse:
    @pytest.mark.asyncio
    async def test_smart_flow_get_parses_json_once(self, async_session):
        """With smart flow on, a successful GET must call response.json() exactly once."""
        async_session._smart_flow = MagicMock()
        async_session._smart_flow.acquire = AsyncMock()

        body = {"organizationId": "42", "id": "N_1"}
        resp = _mock_aio_response(status_code=200, json_data=body)
        async_session._client.request = AsyncMock(return_value=resp)

        await async_session.request(_metadata(), "GET", "/networks/N_1")

        assert resp.json.call_count == 1
        # learn_from_response receives the already-decoded body (same object)
        async_session._smart_flow.learn_from_response.assert_called_once()
        passed_body = async_session._smart_flow.learn_from_response.call_args.args[1]
        assert passed_body == body

    @pytest.mark.asyncio
    async def test_handle_success_async_returns_response_and_body(self, async_session):
        body = [{"id": 1}]
        resp = _mock_aio_response(status_code=200, json_data=body)
        result, parsed = await async_session._handle_success_async(resp, _metadata(), "GET")
        assert result is resp
        assert parsed == body
        assert resp.json.call_count == 1

    @pytest.mark.asyncio
    async def test_handle_success_async_non_get_no_body(self, async_session):
        resp = _mock_aio_response(status_code=201, json_data={"id": "x"})
        result, parsed = await async_session._handle_success_async(resp, _metadata(), "POST")
        assert result is resp
        assert parsed is None
        resp.json.assert_not_called()


# --- Fix #9: early consumer break cancels the prefetch task ---


class TestAsyncIteratorPrefetchCancel:
    @pytest.mark.asyncio
    async def test_early_break_cancels_prefetch(self, async_session):
        """Breaking out of the iterator early cancels the in-flight prefetch task."""
        import asyncio

        resp1 = _mock_aio_response(status_code=200, json_data=[{"id": 1}])
        resp1.links = {"next": {"url": "https://api.meraki.com/api/v1/orgs?startingAfter=1"}}

        # Second request hangs forever so the prefetch task is genuinely pending at break.
        never = asyncio.Event()

        call_count = [0]

        async def fake_request(*args, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return resp1
            await never.wait()  # never resolves
            return _mock_aio_response(status_code=200, json_data=[{"id": 2}])

        async_session._client.request = AsyncMock(side_effect=fake_request)

        captured = {}
        orig_create_task = asyncio.create_task

        def capture_create_task(coro):
            task = orig_create_task(coro)
            captured.setdefault("tasks", []).append(task)
            return task

        agen = async_session._get_pages_iterator(_metadata(), "/orgs", total_pages=-1)
        with patch("meraki.session.async_.asyncio.create_task", side_effect=capture_create_task):
            first = await agen.__anext__()
            assert first == {"id": 1}
            # Break early: close the generator, triggering finally -> cancel prefetch.
            await agen.aclose()

        # The second (prefetch) task should have been cancelled.
        prefetch_tasks = captured["tasks"]
        assert len(prefetch_tasks) >= 2
        assert prefetch_tasks[-1].cancelled()


# --- Fix #12: internal resolver/hydrator GETs drain the global bucket ---


def _make_async_smart_flow_session():
    from tests.unit.conftest import DEFAULT_SESSION_KWARGS, FAKE_API_KEY

    kwargs = {"maximum_concurrent_requests": 8, **DEFAULT_SESSION_KWARGS, "smart_flow_enabled": True}
    with (
        patch("meraki.session.base.check_python_version"),
        patch("httpx.AsyncClient") as mock_client,
    ):
        mock_instance = MagicMock()
        mock_instance.headers = {}
        mock_instance.request = AsyncMock()
        mock_client.return_value = mock_instance
        from meraki.session.async_ import AsyncRestSession

        return AsyncRestSession(logger=None, api_key=FAKE_API_KEY, **kwargs)


class TestAsyncGlobalBucketAccounting:
    @pytest.mark.asyncio
    async def test_resolver_acquires_global_bucket(self):
        s = _make_async_smart_flow_session()
        s._smart_flow._global_bucket = MagicMock()
        s._smart_flow._global_bucket.acquire = AsyncMock()
        resp = _mock_aio_response(status_code=200, json_data={"organizationId": "999"})
        s._client.request = AsyncMock(return_value=resp)

        org = await s._resolve_org_for_limiter("network", "N_1")
        assert org == "999"
        s._smart_flow._global_bucket.acquire.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_hydrator_acquires_global_bucket_per_page(self):
        s = _make_async_smart_flow_session()
        s._smart_flow._global_bucket = MagicMock()
        s._smart_flow._global_bucket.acquire = AsyncMock()

        page1 = _mock_aio_response(status_code=200, json_data=[{"id": "N_1"}])
        page1.links = {"next": {"url": "https://api.meraki.com/api/v1/organizations/9/networks?page=2"}}
        page2 = _mock_aio_response(status_code=200, json_data=[{"id": "N_2"}])
        page2.links = {}
        empty = _mock_aio_response(status_code=200, json_data=[])
        empty.links = {}
        s._client.request = AsyncMock(side_effect=[page1, page2, empty])

        await s._hydrate_org_for_limiter("9")
        assert s._smart_flow._global_bucket.acquire.await_count == 3

    @pytest.mark.asyncio
    async def test_acquire_global_bucket_defensive(self, async_session):
        async_session._smart_flow = None
        await async_session._acquire_global_bucket()  # must not raise


# --- Fix #15: Meraki array-of-objects param encoding on the wire (async) ---


class TestMerakiParamEncodingAsync:
    @pytest.mark.asyncio
    async def test_list_of_dict_params_use_meraki_encoding(self, async_session):
        resp = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp)

        params = {"variables[]": [{"name": "n1", "value": "v1"}]}
        await async_session.request(_metadata(), "GET", "/things", params=params)

        call = async_session._client.request.call_args
        sent_url = call.args[1]
        assert "variables%5B%5Dname=n1" in sent_url
        assert "variables%5B%5Dvalue=v1" in sent_url
        assert call.kwargs.get("params") is None

    @pytest.mark.asyncio
    async def test_scalar_list_params_unchanged(self, async_session):
        resp = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp)

        params = {"networkIds[]": ["a", "b"]}
        await async_session.request(_metadata(), "GET", "/things", params=params)

        call = async_session._client.request.call_args
        assert call.kwargs.get("params") == params
        assert "networkIds" not in call.args[1]

    @pytest.mark.asyncio
    async def test_scalar_params_unchanged(self, async_session):
        resp = _mock_aio_response(status_code=200)
        async_session._client.request = AsyncMock(return_value=resp)

        params = {"perPage": 10}
        await async_session.request(_metadata(), "GET", "/things", params=params)

        call = async_session._client.request.call_args
        assert call.kwargs.get("params") == params
