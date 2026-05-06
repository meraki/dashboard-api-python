"""Asynchronous REST session for Meraki Dashboard API."""

from __future__ import annotations

import asyncio
import json
import random
import urllib.parse
from datetime import datetime, timezone
from typing import Any, Dict, Optional

import httpx

from meraki.common import validate_base_url, validate_user_agent
from meraki.config import AIO_MAXIMUM_CONCURRENT_REQUESTS
from meraki.exceptions import APIError, SessionInputError
from meraki.session.base import SessionBase


class AsyncRestSession(SessionBase):
    """Asynchronous session using httpx.AsyncClient.

    Inherits config storage from SessionBase.
    Overrides request() as async with await on _send_request/_sleep.
    Uses httpx.Limits for concurrency control (replaces asyncio.Semaphore per D-02).
    """

    def __init__(
        self,
        logger,
        api_key,
        maximum_concurrent_requests: int = AIO_MAXIMUM_CONCURRENT_REQUESTS,
        **kwargs: Any,
    ) -> None:
        super().__init__(logger, api_key, **kwargs)

        # Build headers dict
        headers = self._build_headers()
        # Async user-agent prefix
        headers["User-Agent"] = f"python-meraki/aio-{self._version} " + validate_user_agent(self._be_geo_id, self._caller)

        # Build client config (per D-02: Limits replaces Semaphore, per D-06: proxy passthrough)
        client_kwargs: Dict[str, Any] = {
            "timeout": self._single_request_timeout,
            "limits": httpx.Limits(max_connections=maximum_concurrent_requests),
            "headers": headers,
        }
        if self._certificate_path:
            client_kwargs["verify"] = self._certificate_path
        if self._requests_proxy:
            client_kwargs["proxy"] = self._requests_proxy

        # Persistent async client with connection pooling
        self._client = httpx.AsyncClient(**client_kwargs)

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

    async def _send_request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        """Send HTTP request via httpx.AsyncClient (pool limits enforce concurrency per D-02)."""
        response = await self._client.request(method, url, follow_redirects=False, **kwargs)
        return response

    async def _sleep(self, seconds: float) -> None:
        """Async sleep for retry delays."""
        await asyncio.sleep(seconds)

    def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """No-op: httpx config handled at client initialization level."""
        return kwargs

    # ------------------------------------------------------------------
    # Async request override (awaits abstract methods)
    # ------------------------------------------------------------------

    async def request(self, metadata: Dict[str, Any], method: str, url: str, **kwargs: Any) -> Optional[httpx.Response]:
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
        response: Optional[httpx.Response] = None

        while retries > 0:
            # Attempt the request
            try:
                if response:
                    await response.aclose()
                if self._logger:
                    self._logger.info(f"{method} {abs_url}")
                response = await self._send_request(method, abs_url, **kwargs)
            except httpx.HTTPError as e:
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
                            {"status_code": 503, "reason_phrase": str(e), "json": lambda self: {}, "content": b""},
                        )(),
                    )
                continue

            status = response.status_code
            reason = response.reason_phrase if response.reason_phrase else ""

            # Dispatch by status code
            if 300 <= status < 400:
                abs_url = self._handle_redirect_async(response)
            elif 200 <= status < 300:
                result = await self._handle_success_async(response, metadata, method)
                if result is None:
                    # JSON decode failure, retry
                    retries -= 1
                    if retries == 0:
                        raise APIError(metadata, response)
                    await self._sleep(1)
                    continue
                return result
            elif status == 429:
                wait = self._handle_rate_limit_async(response, metadata, retries)
                await self._sleep(wait)
                retries -= 1
                if retries == 0:
                    raise APIError(metadata, response)
            elif status >= 500:
                if self._logger:
                    self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in 1 second")
                await self._sleep(1)
                retries -= 1
                if retries == 0:
                    raise APIError(metadata, response)
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
        reason = response.reason_phrase if response.reason_phrase else ""
        status = response.status_code

        if "page" in metadata:
            counter = metadata["page"]
            if self._logger:
                self._logger.info(f"{tag}, {operation}; page {counter} - {status} {reason}")
        else:
            if self._logger:
                self._logger.info(f"{tag}, {operation} - {status} {reason}")

        # For non-empty GET responses, validate JSON
        try:
            if method == "GET" and response.content.strip():
                response.json()
            return response
        except (json.decoder.JSONDecodeError, ValueError):
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
        reason = response.reason_phrase if response.reason_phrase else ""
        status = response.status_code

        if not self._wait_on_rate_limit or retries <= 0:
            raise APIError(metadata, response)

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
        reason = response.reason_phrase if response.reason_phrase else ""
        status = response.status_code

        # Parse response body
        try:
            message = response.json()
            message_is_dict = isinstance(message, dict)
        except (json.decoder.JSONDecodeError, ValueError):
            message_is_dict = False
            try:
                message = response.text[:100]
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
                raise APIError(metadata, response)
            return retries

        # Action batch concurrency error
        if message_is_dict and "errors" in message and "executing batches" in str(message["errors"][0]).lower():
            wait = self._action_batch_retry_wait_time
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
            await self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)
            return retries

        # Retry other 4xx if configured
        if self._retry_4xx_error:
            wait = random.randint(1, self._retry_4xx_error_wait_time)
            if self._logger:
                self._logger.warning(f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds")
            await self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)
            return retries

        # Non-retryable client error
        if self._logger:
            self._logger.error(f"{tag}, {operation} - {status} {reason}, {message}")
        raise APIError(metadata, response)

    # ------------------------------------------------------------------
    # Convenience HTTP methods
    # ------------------------------------------------------------------

    async def get(self, metadata, url, params=None):
        metadata["method"] = "GET"
        metadata["url"] = url
        metadata["params"] = params
        response = await self.request(metadata, "GET", url, params=params)
        if response:
            if response.content.strip():
                return response.json()
        return None

    async def get_pages(self, metadata, url, params=None, total_pages=-1, direction="next", event_log_end_time=None):
        pass

    async def _download_page(self, request):
        response = await request
        result = response.json()
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
        elif not isinstance(total_pages, int):
            raise SessionInputError(
                "total_pages",
                total_pages,
                "total_pages must be either an integer or 'all' as a string (remember to add the quotation marks).",
                None,
            )
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
                    delta = datetime.now(timezone.utc) - datetime.fromisoformat(starting_after)
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

            await response.aclose()

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
        elif not isinstance(total_pages, int):
            raise SessionInputError(
                "total_pages",
                total_pages,
                "total_pages must be either an integer or 'all' as a string (remember to add the quotation marks).",
                None,
            )
        metadata["page"] = 1

        response = await self.request(metadata, "GET", url, params=params)

        if response.status_code == 204:
            results = None
        else:
            results = response.json()

        # For event log endpoint when using 'next' direction
        if isinstance(results, dict) and metadata["operation"] == "getNetworkEvents" and direction == "next":
            results["events"] = results["events"][::-1]

        links = response.links
        await response.aclose()

        # Get additional pages if more than one requested
        while total_pages != 1:
            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(str(links["next"]["url"]).split("startingAfter=")[1])
                    delta = datetime.now(timezone.utc) - datetime.fromisoformat(starting_after)
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

            response = await self.request(metadata, "GET", nextlink)
            links = response.links
            if isinstance(results, list):
                results.extend(response.json())
            elif isinstance(results, dict) and "items" in results:
                json_response = response.json()
                results["items"].extend(json_response["items"])
                if "meta" in results:
                    results["meta"]["counts"]["items"]["remaining"] = json_response["meta"]["counts"]["items"]["remaining"]
            # For event log endpoint
            elif isinstance(results, dict):
                json_response = response.json()
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

            await response.aclose()
            total_pages = total_pages - 1

        return results

    async def post(self, metadata, url, json=None):
        metadata["method"] = "POST"
        metadata["url"] = url
        metadata["json"] = json
        response = await self.request(metadata, "POST", url, json=json)
        if response:
            if response.content.strip():
                return response.json()
        return None

    async def put(self, metadata, url, json=None):
        metadata["method"] = "PUT"
        metadata["url"] = url
        metadata["json"] = json
        response = await self.request(metadata, "PUT", url, json=json)
        if response:
            if response.content.strip():
                return response.json()
        return None

    async def delete(self, metadata, url, params=None):
        metadata["method"] = "DELETE"
        metadata["url"] = url
        metadata["params"] = params
        await self.request(metadata, "DELETE", url, params=params)
        return None

    async def close(self):
        """Close the underlying httpx.AsyncClient and release connections."""
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
