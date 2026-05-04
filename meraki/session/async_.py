"""Asynchronous REST session for Meraki Dashboard API."""

from __future__ import annotations

import asyncio
import json
import random
import ssl
import urllib.parse
from datetime import datetime
from typing import TYPE_CHECKING, Any, Dict, Optional

import aiohttp

from meraki.common import validate_base_url, validate_user_agent
from meraki.config import AIO_MAXIMUM_CONCURRENT_REQUESTS
from meraki.exceptions import APIError, AsyncAPIError
from meraki.session.base import SessionBase

if TYPE_CHECKING:
    import httpx


class AsyncRestSession(SessionBase):
    """Asynchronous session using aiohttp library.

    Inherits config storage from SessionBase.
    Overrides request() as async with await on _send_request/_sleep.
    Adds concurrency semaphore per D-08.
    """

    def __init__(
        self,
        logger,
        api_key,
        maximum_concurrent_requests: int = AIO_MAXIMUM_CONCURRENT_REQUESTS,
        **kwargs: Any,
    ) -> None:
        super().__init__(logger, api_key, **kwargs)
        self._concurrent_requests_semaphore = asyncio.Semaphore(maximum_concurrent_requests)

        # Build headers dict (aiohttp uses dict, not session.headers)
        self._headers = self._build_headers()
        # Async user-agent prefix
        self._headers["User-Agent"] = f"python-meraki/aio-{self._version} " + validate_user_agent(
            self._be_geo_id, self._caller
        )

        # SSL context for certificate_path
        if self._certificate_path:
            self._sslcontext: Optional[ssl.SSLContext] = ssl.create_default_context()
            self._sslcontext.load_verify_locations(self._certificate_path)
        else:
            self._sslcontext = None

        # Initialize aiohttp session
        self._req_session = aiohttp.ClientSession(
            headers=self._headers,
            timeout=aiohttp.ClientTimeout(total=self._single_request_timeout),
        )

        # Trigger the property setter to bind the correct get_pages implementation
        self.use_iterator_for_get_pages = self._use_iterator_for_get_pages

    @property
    def use_iterator_for_get_pages(self):
        return self._use_iterator_for_get_pages

    @use_iterator_for_get_pages.setter
    def use_iterator_for_get_pages(self, value):
        if value:
            self.get_pages = self._get_pages_iterator
        else:
            self.get_pages = self._get_pages_legacy
        self._use_iterator_for_get_pages = value

    # ------------------------------------------------------------------
    # Abstract method implementations
    # ------------------------------------------------------------------

    async def _send_request(self, method: str, url: str, **kwargs: Any) -> "httpx.Response":
        """Send HTTP request via aiohttp with semaphore gating (D-08)."""
        async with self._concurrent_requests_semaphore:
            response = await self._req_session.request(method, url, **kwargs)
            return response  # type: ignore[return-value]

    async def _sleep(self, seconds: float) -> None:
        """Async sleep for retry delays."""
        await asyncio.sleep(seconds)

    def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Map config to aiohttp-specific kwargs (ssl, proxy, timeout)."""
        if self._sslcontext:
            kwargs.setdefault("ssl", self._sslcontext)
        if self._requests_proxy:
            kwargs.setdefault("proxy", self._requests_proxy)
        kwargs.setdefault("timeout", self._single_request_timeout)
        return kwargs

    # ------------------------------------------------------------------
    # Async request override (awaits abstract methods)
    # ------------------------------------------------------------------

    async def request(self, metadata: Dict[str, Any], method: str, url: str, **kwargs: Any) -> Optional["httpx.Response"]:
        """Execute an API request with retry loop and status dispatch (async version).

        Mirrors SessionBase.request() but awaits _send_request and _sleep.
        """
        tag = metadata["tags"][0]
        operation = metadata["operation"]

        # Prepare transport-specific kwargs
        kwargs = self._transport_kwargs(kwargs)

        # aiohttp manipulates URLs as instances of yarl.URL
        if not isinstance(url, str):
            url = str(url)

        # Resolve absolute URL
        abs_url = validate_base_url(self, url)

        # Simulate non-GET calls
        if self._logger:
            self._logger.debug(metadata)
        if self._simulate and method != "GET":
            if self._logger:
                self._logger.info(f"{tag}, {operation} - SIMULATED")
            return None

        retries = self._maximum_retries
        response: Optional["httpx.Response"] = None

        while retries > 0:
            # Attempt the request
            try:
                if response:
                    response.release()
                if self._logger:
                    self._logger.info(f"{method} {abs_url}")
                response = await self._send_request(method, abs_url, **kwargs)
            except Exception as e:
                if self._logger:
                    self._logger.warning(f"{tag}, {operation} - {e}, retrying in 1 second")
                await self._sleep(1)
                retries -= 1
                if retries == 0:
                    raise APIError(
                        metadata,
                        type(
                            "FakeResponse",
                            (),
                            {"status_code": 503, "reason_phrase": str(e), "json": lambda: {}, "content": b""},
                        )(),
                    )
                continue

            status = response.status
            reason = response.reason if response.reason else ""

            # Dispatch by status code
            if 300 <= status < 400:
                abs_url = self._handle_redirect_async(response)
            elif 200 <= status < 300:
                result = await self._handle_success_async(response, metadata, method)
                if result is None:
                    # JSON decode failure, retry
                    retries -= 1
                    if retries == 0:
                        raise AsyncAPIError(metadata, response, "JSON decode error after retries")
                    await self._sleep(1)
                    continue
                return result
            elif status == 429:
                wait = self._handle_rate_limit_async(response, metadata, retries)
                await self._sleep(wait)
                retries -= 1
                if retries == 0:
                    raise AsyncAPIError(metadata, response, "Rate limit retries exhausted")
            elif status >= 500:
                if self._logger:
                    self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in 1 second")
                await self._sleep(1)
                retries -= 1
                if retries == 0:
                    raise AsyncAPIError(metadata, response, "Server error retries exhausted")
            elif 400 <= status < 500:
                retries = await self._handle_client_error_async(response, metadata, retries)

        return response

    # ------------------------------------------------------------------
    # Async status handlers
    # ------------------------------------------------------------------

    async def _handle_success_async(
        self,
        response: Any,
        metadata: Dict[str, Any],
        method: str,
    ) -> Optional[Any]:
        """Handle 2xx responses (async). Returns response or None if JSON validation fails."""
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason if response.reason else ""
        status = response.status

        if "page" in metadata:
            counter = metadata["page"]
            if self._logger:
                self._logger.info(f"{tag}, {operation}; page {counter} - {status} {reason}")
        else:
            if self._logger:
                self._logger.info(f"{tag}, {operation} - {status} {reason}")

        # For non-empty GET responses, validate JSON
        try:
            if method == "GET":
                await response.json(content_type=None)
            return response
        except (json.decoder.JSONDecodeError, aiohttp.client_exceptions.ContentTypeError):
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - JSON decode error, retrying in 1 second")
            return None

    def _handle_redirect_async(self, response: Any) -> str:
        """Handle 3xx redirects for aiohttp responses."""
        abs_url = str(response.headers["Location"])
        substring = "meraki.com/api/v"
        if substring not in abs_url:
            substring = "meraki.cn/api/v"
        if substring in abs_url:
            self._base_url = abs_url[: abs_url.find(substring) + len(substring) + 1]
        return abs_url

    def _handle_rate_limit_async(
        self,
        response: Any,
        metadata: Dict[str, Any],
        retries: int,
    ) -> float:
        """Handle 429 rate limiting (async). Returns seconds to wait."""
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason if response.reason else ""
        status = response.status

        if not self._wait_on_rate_limit or retries <= 0:
            raise AsyncAPIError(metadata, response, "Rate limited")

        if "Retry-After" in response.headers:
            wait = int(response.headers["Retry-After"])
        else:
            attempt = self._maximum_retries - retries
            wait = min(
                (2**attempt) * (1 + random.random()),
                self._nginx_429_retry_wait_time,
            )

        if self._logger:
            self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
        return wait

    async def _handle_client_error_async(
        self,
        response: Any,
        metadata: Dict[str, Any],
        retries: int,
    ) -> int:
        """Handle 4xx client errors (async). Returns updated retry count."""
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason if response.reason else ""
        status = response.status

        # Parse response body
        try:
            message = await response.json(content_type=None)
            message_is_dict = isinstance(message, dict)
        except (json.decoder.JSONDecodeError, aiohttp.client_exceptions.ContentTypeError):
            message_is_dict = False
            try:
                message = (await response.text())[:100]
            except Exception:
                message = None

        # Network delete concurrency error
        if (
            metadata.get("operation") == "deleteNetwork"
            and status == 400
            and message_is_dict
            and "errors" in message
            and "concurrent" in str(message["errors"][0])
        ):
            wait = random.randint(30, self._network_delete_retry_wait_time)
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
            await self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise AsyncAPIError(metadata, response, message)
            return retries

        # Action batch concurrency error
        if message_is_dict and "errors" in message and "executing batches" in str(message["errors"][0]).lower():
            wait = self._action_batch_retry_wait_time
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
            await self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise AsyncAPIError(metadata, response, message)
            return retries

        # Retry other 4xx if configured
        if self._retry_4xx_error:
            wait = random.randint(1, self._retry_4xx_error_wait_time)
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
            await self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise AsyncAPIError(metadata, response, message)
            return retries

        # Non-retryable client error
        if self._logger:
            self._logger.error(f"{tag}, {operation} - {status} {reason}, {message}")
        raise AsyncAPIError(metadata, response, message)

    # ------------------------------------------------------------------
    # Convenience HTTP methods
    # ------------------------------------------------------------------

    async def get(self, metadata, url, params=None):
        metadata["method"] = "GET"
        metadata["url"] = url
        metadata["params"] = params
        async with await self.request(metadata, "GET", url, params=params) as response:
            return await response.json(content_type=None)

    async def get_pages(self, metadata, url, params=None, total_pages=-1, direction="next", event_log_end_time=None):
        pass

    async def _download_page(self, request):
        response = await request
        result = await response.json(content_type=None)
        return response, result

    async def _get_pages_iterator(
        self,
        metadata,
        url,
        params=None,
        total_pages=-1,
        direction="next",
        event_log_end_time=None,
    ):
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        metadata["page"] = 1

        request_task = asyncio.create_task(self._download_page(self.request(metadata, "GET", url, params=params)))

        # Get additional pages if more than one requested
        while total_pages != 0:
            response, results = await request_task
            links = response.links

            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(str(links["next"]["url"]).split("startingAfter=")[1])
                    delta = datetime.utcnow() - datetime.fromisoformat(starting_after[:-1])
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300:
                        break
                    # Or if next page is past the specified window's end time
                    elif event_log_end_time and starting_after > event_log_end_time:
                        break

                metadata["page"] += 1
                nextlink = links["next"]["url"]
            elif direction == "prev" and "prev" in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(str(links["prev"]["url"]).split("endingBefore=")[1])
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < "2014-01-01":
                        break

                metadata["page"] += 1
                nextlink = links["prev"]["url"]
            else:
                total_pages = 1

            response.release()

            total_pages = total_pages - 1

            if total_pages != 0:
                request_task = asyncio.create_task(self._download_page(self.request(metadata, "GET", nextlink)))

            return_items = []
            # just prepare the list
            if isinstance(results, list):
                return_items = results
            elif isinstance(results, dict) and "items" in results:
                return_items = results["items"]
            # For event log endpoint
            elif isinstance(results, dict):
                if direction == "next":
                    return_items = results["events"][::-1]
                else:
                    return_items = results["events"]

            for item in return_items:
                yield item

    async def _get_pages_legacy(
        self,
        metadata,
        url,
        params=None,
        total_pages=-1,
        direction="next",
        event_log_end_time=None,
    ):
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        metadata["page"] = 1

        async with await self.request(metadata, "GET", url, params=params) as response:
            results = await response.json(content_type=None)

            # For event log endpoint when using 'next' direction
            if isinstance(results, dict) and metadata["operation"] == "getNetworkEvents" and direction == "next":
                results["events"] = results["events"][::-1]

            links = response.links

        # Get additional pages if more than one requested
        while total_pages != 1:
            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(str(links["next"]["url"]).split("startingAfter=")[1])
                    delta = datetime.utcnow() - datetime.fromisoformat(starting_after[:-1])
                    if delta.total_seconds() < 300:
                        break
                    elif event_log_end_time and starting_after > event_log_end_time:
                        break

                metadata["page"] += 1
                nextlink = links["next"]["url"]
            elif direction == "prev" and "prev" in links:
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(str(links["prev"]["url"]).split("endingBefore=")[1])
                    if ending_before < "2014-01-01":
                        break

                metadata["page"] += 1
                nextlink = links["prev"]["url"]
            else:
                break

            async with await self.request(metadata, "GET", nextlink) as response:
                links = response.links
                if isinstance(results, list):
                    results.extend(await response.json(content_type=None))
                elif isinstance(results, dict) and "items" in results:
                    json_response = await response.json(content_type=None)
                    results["items"].extend(json_response["items"])
                    if "meta" in results:
                        results["meta"]["counts"]["items"]["remaining"] = json_response["meta"]["counts"]["items"]["remaining"]
                # For event log endpoint
                elif isinstance(results, dict):
                    json_response = await response.json(content_type=None)
                    start = json_response["pageStartAt"]
                    end = json_response["pageEndAt"]
                    events = json_response["events"]
                    if direction == "next":
                        events = events[::-1]
                    if start < results["pageStartAt"]:
                        results["pageStartAt"] = start
                    if end > results["pageEndAt"]:
                        results["pageEndAt"] = end
                    results["events"].extend(events)

            total_pages = total_pages - 1

        return results

    async def post(self, metadata, url, json=None):
        metadata["method"] = "POST"
        metadata["url"] = url
        metadata["json"] = json
        async with await self.request(metadata, "POST", url, json=json) as response:
            return await response.json(content_type=None)

    async def put(self, metadata, url, json=None):
        metadata["method"] = "PUT"
        metadata["url"] = url
        metadata["json"] = json
        async with await self.request(metadata, "PUT", url, json=json) as response:
            return await response.json(content_type=None)

    async def delete(self, metadata, url):
        metadata["method"] = "DELETE"
        metadata["url"] = url
        async with await self.request(metadata, "DELETE", url):
            return None

    async def close(self):
        await self._req_session.close()
