import asyncio
from datetime import datetime
import json
import platform
import random
import ssl
import sys
import urllib.parse

import aiohttp

from ..config import *
from ..exceptions import *
from ..__init__ import __version__
from ..rest_session import user_agent_extended

# Main module interface
class AsyncRestSession:
    def __init__(
        self,
        logger,
        api_key,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=SINGLE_REQUEST_TIMEOUT,
        certificate_path=CERTIFICATE_PATH,
        requests_proxy=REQUESTS_PROXY,
        wait_on_rate_limit=WAIT_ON_RATE_LIMIT,
        nginx_429_retry_wait_time=NGINX_429_RETRY_WAIT_TIME,
        action_batch_retry_wait_time=ACTION_BATCH_RETRY_WAIT_TIME,
        retry_4xx_error=RETRY_4XX_ERROR,
        retry_4xx_error_wait_time=RETRY_4XX_ERROR_WAIT_TIME,
        maximum_retries=MAXIMUM_RETRIES,
        simulate=SIMULATE_API_CALLS,
        maximum_concurrent_requests=AIO_MAXIMUM_CONCURRENT_REQUESTS,
        be_geo_id=BE_GEO_ID,
        caller=MERAKI_PYTHON_SDK_CALLER,
    ):
        super().__init__()

        # Initialize attributes and properties
        self._version = __version__
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._requests_proxy = requests_proxy
        self._wait_on_rate_limit = wait_on_rate_limit
        self._nginx_429_retry_wait_time = nginx_429_retry_wait_time
        self._action_batch_retry_wait_time = action_batch_retry_wait_time
        self._retry_4xx_error = retry_4xx_error
        self._retry_4xx_error_wait_time = retry_4xx_error_wait_time
        self._maximum_retries = maximum_retries
        self._simulate = simulate
        self._concurrent_requests_semaphore = asyncio.Semaphore(maximum_concurrent_requests)
        self._be_geo_id = be_geo_id
        self._caller = caller

        # Check base URL
        if 'v0' in self._base_url:
            sys.exit(f'If you want to use the Python library with v0 paths ({self._base_url} was configured as the base'
                     f' URL), then install the v0 library. See the "Setup" section @ https://github.com/meraki/dashboard-api-python/')
        elif self._base_url[-1] == '/':
            self._base_url = self._base_url[:-1]

        # Update the headers for the session
        self._headers = {
            "Authorization": "Bearer " + self._api_key,
            "Content-Type": "application/json",
            "User-Agent": f"python-meraki/aio-{self._version} " + user_agent_extended(self._be_geo_id, self._caller),
        }
        if self._certificate_path:
            self._sslcontext = ssl.create_default_context()
            self._sslcontext.load_verify_locations(certificate_path)

        # Initialize a new `aiohttp` session
        self._req_session = aiohttp.ClientSession(
            headers=self._headers,
            timeout=aiohttp.ClientTimeout(total=single_request_timeout),
        )

        # Log API calls
        self._logger = logger
        self._parameters = {"version": self._version}
        self._parameters.update(locals())
        self._parameters.pop("self")
        self._parameters.pop("logger")
        self._parameters.pop("__class__")
        self._parameters["api_key"] = "*" * 36 + self._api_key[-4:]
        if self._logger:
            self._logger.info(f"Meraki dashboard API session initialized with these parameters: {self._parameters}")

    async def request(self, metadata, method, url, **kwargs):
        async with self._concurrent_requests_semaphore:
            return await self._request(metadata, method, url, allow_redirects=False, **kwargs)

    async def _request(self, metadata, method, url, **kwargs):
        # Metadata on endpoint
        tag = metadata["tags"][0]
        operation = metadata["operation"]

        # Update request kwargs with session defaults
        if self._certificate_path:
            kwargs.setdefault("ssl", self._sslcontext)
        if self._requests_proxy:
            kwargs.setdefault("proxy", self._requests_proxy)
        kwargs.setdefault("timeout", self._single_request_timeout)

        # Ensure proper base URL
        url = str(url)
        if "meraki.com" in url or "meraki.cn" in url:
            abs_url = url
        else:
            abs_url = self._base_url + url

        # Set maximum number of retries
        retries = self._maximum_retries

        # Option to simulate non-safe API calls without actually sending them
        if self._logger:
            self._logger.debug(metadata)
        if self._simulate and method != "GET":
            if self._logger:
                self._logger.info(f"{tag}, {operation} > {abs_url} - SIMULATED")
            return None
        else:
            response = None
            message = None
            for _ in range(retries):
                # Make the HTTP request to the API endpoint
                try:
                    if self._logger:
                        self._logger.info(f'{method} {abs_url}')
                    response = await self._req_session.request(method, abs_url, **kwargs)
                    reason = response.reason if response.reason else None
                    status = response.status
                except Exception as e:
                    if self._logger:
                        self._logger.warning(f"{tag}, {operation} > {abs_url} - {e}, retrying in 1 second")
                    await asyncio.sleep(1)
                    continue

                if status == 200:
                    if "page" in metadata:
                        counter = metadata["page"]
                        if self._logger:
                            self._logger.info(f"{tag}, {operation}; page {counter} > {abs_url} - {status} {reason}")
                    else:
                        if self._logger:
                            self._logger.info(f"{tag}, {operation} > {abs_url} - {status} {reason}")
                    # For non-empty response to GET, ensure valid JSON
                    try:
                        if method == "GET":
                            await response.json()
                        return response
                    except (
                        json.decoder.JSONDecodeError,
                        aiohttp.client_exceptions.ContentTypeError,
                    ) as e:
                        if self._logger:
                            self._logger.warning(f"{tag}, {operation} > {abs_url} - {e}, retrying in 1 second")
                        await asyncio.sleep(1)
                # Handle 3XX redirects automatically
                elif 300 <= status < 400:
                    abs_url = response.headers["Location"]
                    substring = "meraki.com/api/v"
                    if substring not in abs_url:
                        substring = "meraki.cn/api/v"
                    self._base_url = abs_url[
                        : abs_url.find(substring) + len(substring) + 1
                    ]
                # Rate limit 429 errors
                elif status == 429:
                    wait = 0
                    if "Retry-After" in response.headers:
                        wait = int(response.headers["Retry-After"])
                    else:
                        wait = random.randint(1, self._nginx_429_retry_wait_time)
                    if self._logger:
                        self._logger.warning(f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in {wait} seconds")
                    await asyncio.sleep(wait)
                # 5XX errors
                elif status >= 500:
                    if self._logger:
                        self._logger.warning(f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in 1 second")
                    await asyncio.sleep(1)
                # 4XX errors
                else:
                    try:
                        message = await response.json()
                    except aiohttp.client_exceptions.ContentTypeError:
                        try:
                            message = (await response.text())[:100]
                        except:
                            message = None

                    # Check specifically for action batch concurrency error
                    action_batch_concurrency_error = {
                        "errors": [
                            "Too many concurrently executing batches. Maximum is 5 confirmed but not yet executed batches."
                        ]
                    }
                    if message == action_batch_concurrency_error:
                        wait = self._action_batch_retry_wait_time
                        if self._logger:
                            self._logger.warning(f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in {wait} seconds")
                        await asyncio.sleep(wait)
                    
                    elif self._retry_4xx_error:
                        wait = random.randint(1, self._retry_4xx_error_wait_time)
                        if self._logger:
                            self._logger.warning(f"{tag}, {operation} > {abs_url} - {status} {reason}, retrying in {wait} seconds")
                        await asyncio.sleep(wait)

                    # All other client-side errors
                    else:
                        if self._logger:
                            self._logger.error(f"{tag}, {operation} > {abs_url} - {status} {reason}, {message}")
                        raise AsyncAPIError(metadata, response, message)
            raise AsyncAPIError(metadata, response, "Reached retry limit: " + str(message))

    async def get(self, metadata, url, params=None):
        metadata["method"] = "GET"
        metadata["url"] = url
        metadata["params"] = params
        response = await self.request(metadata, "GET", url, params=params)
        return await response.json()

    async def get_pages(
        self, metadata, url, params=None, total_pages=-1, direction="next", event_log_end_time=None
    ):
        if type(total_pages) == str and total_pages.lower() == "all":
            total_pages = -1
        elif type(total_pages) == str and total_pages.isnumeric():
            total_pages = int(total_pages)
        metadata["page"] = 1

        response = await self.request(metadata, "GET", url, params=params)
        results = await response.json()

        # For event log endpoint when using 'next' direction, so results/events are sorted chronologically
        if type(results) == dict and metadata["operation"] == "getNetworkEvents" and direction == "next":
            results["events"] = results["events"][::-1]

        # Get additional pages if more than one requested
        while total_pages != 1:
            links = response.links

            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(links["next"]["url"].split("startingAfter=")[1])
                    delta = datetime.utcnow() - datetime.fromisoformat(starting_after[:-1])
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300:
                        break
                    # Or if next page is past the specified window's end time
                    elif event_log_end_time and starting_after > event_log_end_time:
                        break
                
                metadata["page"] += 1
                response = await self.request(metadata, "GET", links["next"]["url"])
            elif direction == "prev" and "prev" in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(links["prev"]["url"].split("endingBefore=")[1])
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < "2014-01-01":
                        break
                
                metadata["page"] += 1
                response = await self.request(metadata, "GET", links["prev"]["url"])
            else:
                break

            # Append that page's results, depending on the endpoint
            if type(results) == list:
                results.extend(await response.json())
            # For event log endpoint
            elif type(results) == dict:
                json_response = await response.json()
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

            total_pages -= 1

        return results

    async def post(self, metadata, url, json=None):
        metadata["method"] = "POST"
        metadata["url"] = url
        metadata["json"] = json
        response = await self.request(metadata, "POST", url, json=json)
        return await response.json()

    async def put(self, metadata, url, json=None):
        metadata["method"] = "PUT"
        metadata["url"] = url
        metadata["json"] = json
        response = await self.request(metadata, "PUT", url, json=json)
        return await response.json()

    async def delete(self, metadata, url):
        metadata["method"] = "DELETE"
        metadata["url"] = url
        await self.request(metadata, "DELETE", url)
        return None

    async def close(self):
        await self._req_session.close()
