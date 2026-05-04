"""Abstract base class for sync and async Meraki API sessions."""

from __future__ import annotations

import json
import random
import urllib.parse
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Dict, Optional

from meraki._version import __version__
from meraki.common import (
    check_python_version,
    reject_v0_base_url,
    validate_base_url,
    validate_user_agent,
)
from meraki.config import (
    ACTION_BATCH_RETRY_WAIT_TIME,
    BE_GEO_ID,
    CERTIFICATE_PATH,
    DEFAULT_BASE_URL,
    MAXIMUM_RETRIES,
    MERAKI_PYTHON_SDK_CALLER,
    NETWORK_DELETE_RETRY_WAIT_TIME,
    NGINX_429_RETRY_WAIT_TIME,
    REQUESTS_PROXY,
    RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME,
    SIMULATE_API_CALLS,
    SINGLE_REQUEST_TIMEOUT,
    USE_ITERATOR_FOR_GET_PAGES,
    WAIT_ON_RATE_LIMIT,
)
from meraki.exceptions import APIError, APIResponseError
from meraki.response_handler import handle_3xx

if TYPE_CHECKING:
    import httpx


class SessionBase(ABC):
    """Abstract base class providing config storage, URL resolution, retry loop, and status dispatch.

    Subclasses must implement:
        _send_request: perform the actual HTTP call
        _sleep: pause execution (sync or async)
        _transport_kwargs: prepare transport-specific request kwargs
    """

    def __init__(
        self,
        logger: Any,
        api_key: str,
        base_url: str = DEFAULT_BASE_URL,
        single_request_timeout: int = SINGLE_REQUEST_TIMEOUT,
        certificate_path: str = CERTIFICATE_PATH,
        requests_proxy: str = REQUESTS_PROXY,
        wait_on_rate_limit: bool = WAIT_ON_RATE_LIMIT,
        nginx_429_retry_wait_time: int = NGINX_429_RETRY_WAIT_TIME,
        action_batch_retry_wait_time: int = ACTION_BATCH_RETRY_WAIT_TIME,
        network_delete_retry_wait_time: int = NETWORK_DELETE_RETRY_WAIT_TIME,
        retry_4xx_error: bool = RETRY_4XX_ERROR,
        retry_4xx_error_wait_time: int = RETRY_4XX_ERROR_WAIT_TIME,
        maximum_retries: int = MAXIMUM_RETRIES,
        simulate: bool = SIMULATE_API_CALLS,
        be_geo_id: str = BE_GEO_ID,
        caller: str = MERAKI_PYTHON_SDK_CALLER,
        use_iterator_for_get_pages: bool = USE_ITERATOR_FOR_GET_PAGES,
        validate_kwargs: bool = False,
    ) -> None:
        super().__init__()

        # Store config attributes
        self._version = __version__
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._requests_proxy = requests_proxy
        self._wait_on_rate_limit = wait_on_rate_limit
        self._nginx_429_retry_wait_time = nginx_429_retry_wait_time
        self._action_batch_retry_wait_time = action_batch_retry_wait_time
        self._network_delete_retry_wait_time = network_delete_retry_wait_time
        self._retry_4xx_error = retry_4xx_error
        self._retry_4xx_error_wait_time = retry_4xx_error_wait_time
        self._maximum_retries = maximum_retries
        self._simulate = simulate
        self._be_geo_id = be_geo_id
        self._caller = caller
        self._use_iterator_for_get_pages = use_iterator_for_get_pages
        self._validate_kwargs = validate_kwargs

        # Check Python version
        check_python_version()

        # Reject v0 base URL
        reject_v0_base_url(self)

        # Logger and masked parameters for logging
        self._logger = logger
        self._parameters: Dict[str, Any] = {"version": self._version}
        self._parameters["api_key"] = "*" * 36 + self._api_key[-4:]
        self._parameters["base_url"] = self._base_url
        self._parameters["single_request_timeout"] = self._single_request_timeout
        self._parameters["certificate_path"] = self._certificate_path
        self._parameters["requests_proxy"] = self._requests_proxy
        self._parameters["wait_on_rate_limit"] = self._wait_on_rate_limit
        self._parameters["nginx_429_retry_wait_time"] = self._nginx_429_retry_wait_time
        self._parameters["action_batch_retry_wait_time"] = self._action_batch_retry_wait_time
        self._parameters["network_delete_retry_wait_time"] = self._network_delete_retry_wait_time
        self._parameters["retry_4xx_error"] = self._retry_4xx_error
        self._parameters["retry_4xx_error_wait_time"] = self._retry_4xx_error_wait_time
        self._parameters["maximum_retries"] = self._maximum_retries
        self._parameters["simulate"] = self._simulate
        self._parameters["be_geo_id"] = self._be_geo_id
        self._parameters["caller"] = self._caller
        self._parameters["use_iterator_for_get_pages"] = self._use_iterator_for_get_pages

        if self._logger:
            self._logger.info(
                f"Meraki dashboard API session initialized with these parameters: {self._parameters}"
            )

    # ------------------------------------------------------------------
    # Abstract methods (subclass contract)
    # ------------------------------------------------------------------

    @abstractmethod
    def _send_request(self, method: str, url: str, **kwargs: Any) -> "httpx.Response":
        """Send the HTTP request. Implemented by sync/async subclasses."""
        ...

    @abstractmethod
    def _sleep(self, seconds: float) -> None:
        """Sleep for the given duration. Sync uses time.sleep, async uses asyncio.sleep."""
        ...

    @abstractmethod
    def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Prepare transport-specific kwargs (verify, proxy, timeout, etc.)."""
        ...

    # ------------------------------------------------------------------
    # Template method: request
    # ------------------------------------------------------------------

    def request(
        self, metadata: Dict[str, Any], method: str, url: str, **kwargs: Any
    ) -> Optional["httpx.Response"]:
        """Execute an API request with retry loop and status dispatch.

        Args:
            metadata: Endpoint metadata (tags, operation, optional page counter).
            method: HTTP method (GET, POST, PUT, DELETE).
            url: Endpoint URL (relative or absolute).
            **kwargs: Additional request kwargs (json, params, etc.).

        Returns:
            httpx.Response on success, or None if simulated.
        """
        tag = metadata["tags"][0]
        operation = metadata["operation"]

        # Prepare transport-specific kwargs
        kwargs = self._transport_kwargs(kwargs)

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
                if self._logger:
                    self._logger.info(f"{method} {abs_url}")
                response = self._send_request(method, abs_url, allow_redirects=False, **kwargs)
            except Exception as e:
                if self._logger:
                    self._logger.warning(f"{tag}, {operation} - {e}, retrying in 1 second")
                self._sleep(1)
                retries -= 1
                if retries == 0:
                    raise APIError(
                        metadata,
                        APIResponseError(e.__class__.__name__, 503, str(e)),
                    )
                continue

            status = response.status_code

            # Dispatch by status code
            if 300 <= status < 400:
                abs_url = self._handle_redirect(response)
            elif 200 <= status < 300:
                result = self._handle_success(response, metadata, method, retries)
                if result is None:
                    # JSON decode failure, retry
                    retries -= 1
                    if retries == 0:
                        raise APIError(metadata, response)
                    self._sleep(1)
                    continue
                return result
            elif status == 429:
                wait = self._handle_rate_limit(response, metadata, retries)
                self._sleep(wait)
                retries -= 1
                if retries == 0:
                    raise APIError(metadata, response)
            elif status >= 500:
                self._handle_server_error(response, metadata)
                self._sleep(1)
                retries -= 1
                if retries == 0:
                    raise APIError(metadata, response)
            elif 400 <= status < 500:
                retries = self._handle_client_error(response, metadata, retries)

        return response

    # ------------------------------------------------------------------
    # Status handlers (each kept under cyclomatic complexity 10)
    # ------------------------------------------------------------------

    def _handle_success(
        self,
        response: "httpx.Response",
        metadata: Dict[str, Any],
        method: str,
        retries: int,
    ) -> Optional["httpx.Response"]:
        """Handle 2xx responses. Returns response or None if JSON validation fails."""
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason_phrase if hasattr(response, "reason_phrase") else ""
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
                self._logger.warning(
                    f"{tag}, {operation} - JSON decode error, retrying in 1 second"
                )
            return None

    def _handle_redirect(self, response: "httpx.Response") -> str:
        """Handle 3xx redirects. Returns the new absolute URL."""
        return handle_3xx(self, response)

    def _handle_rate_limit(
        self,
        response: "httpx.Response",
        metadata: Dict[str, Any],
        retries: int,
    ) -> float:
        """Handle 429 rate limiting. Returns seconds to wait.

        Raises APIError if rate limit retries disabled or retries exhausted.
        """
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason_phrase if hasattr(response, "reason_phrase") else ""
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
            self._logger.warning(
                f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds"
            )
        return wait

    def _handle_server_error(
        self, response: "httpx.Response", metadata: Dict[str, Any]
    ) -> None:
        """Handle 5xx server errors. Logs warning before retry."""
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason_phrase if hasattr(response, "reason_phrase") else ""
        status = response.status_code

        if self._logger:
            self._logger.warning(
                f"{tag}, {operation} - {status} {reason}, retrying in 1 second"
            )

    def _handle_client_error(
        self,
        response: "httpx.Response",
        metadata: Dict[str, Any],
        retries: int,
    ) -> int:
        """Handle 4xx client errors. Returns updated retry count.

        Raises APIError if error is not retryable or retries exhausted.
        """
        tag = metadata["tags"][0]
        operation = metadata["operation"]
        reason = response.reason_phrase if hasattr(response, "reason_phrase") else ""
        status = response.status_code

        # Parse response body
        try:
            message = response.json()
        except (ValueError, json.decoder.JSONDecodeError):
            message = response.content[:100]

        # Network delete concurrency error
        if self._is_network_delete_concurrency(metadata, response, message):
            wait = random.randint(30, self._network_delete_retry_wait_time)
            if self._logger:
                self._logger.warning(
                    f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds"
                )
            self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)
            return retries

        # Action batch concurrency error
        if self._is_action_batch_concurrency(message):
            wait = self._action_batch_retry_wait_time
            if self._logger:
                self._logger.warning(
                    f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds"
                )
            self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)
            return retries

        # Generic 4xx retry
        if self._retry_4xx_error and retries > 0:
            wait = random.randint(1, self._retry_4xx_error_wait_time)
            if self._logger:
                self._logger.warning(
                    f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds"
                )
            self._sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)
            return retries

        # Non-retryable client error
        if self._logger:
            self._logger.error(f"{tag}, {operation} - {status} {reason}, {message}")
        raise APIError(metadata, response)

    # ------------------------------------------------------------------
    # Helper methods
    # ------------------------------------------------------------------

    def _is_network_delete_concurrency(
        self,
        metadata: Dict[str, Any],
        response: "httpx.Response",
        message: Any,
    ) -> bool:
        """Check if error is a network delete concurrency conflict."""
        if metadata.get("operation") != "deleteNetwork":
            return False
        if response.status_code != 400:
            return False
        if isinstance(message, dict) and "errors" in message:
            return "concurrent" in str(message["errors"][0])
        return False

    def _is_action_batch_concurrency(self, message: Any) -> bool:
        """Check if error is an action batch concurrency conflict."""
        if isinstance(message, dict) and "errors" in message:
            return "executing batches" in str(message["errors"][0]).lower()
        return False

    def _build_headers(self) -> Dict[str, str]:
        """Build standard request headers."""
        return {
            "Authorization": "Bearer " + self._api_key,
            "Content-Type": "application/json",
            "User-Agent": f"python-meraki/{self._version} "
            + validate_user_agent(self._be_geo_id, self._caller),
        }
