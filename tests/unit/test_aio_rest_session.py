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
