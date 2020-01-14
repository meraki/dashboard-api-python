import json
import time

import ssl
import aiohttp
import asyncio

from meraki.config import *
from meraki.exceptions import *


# Main module interface
class AsyncRestSession(object):
    def __init__(
        self,
        logger,
        api_key,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=SINGLE_REQUEST_TIMEOUT,
        certificate_path=CERTIFICATE_PATH,
        wait_on_rate_limit=WAIT_ON_RATE_LIMIT,
        maximum_retries=MAXIMUM_RETRIES,
        simulate=SIMULATE_API_CALLS,
    ):
        super().__init__()

        # Initialize attributes and properties
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._wait_on_rate_limit = wait_on_rate_limit
        self._maximum_retries = maximum_retries
        self._simulate = simulate

        # Update the headers of the `requests` session
        headers = None
        if "v0" in self._base_url:
            headers = {
                "X-Cisco-Meraki-API-Key": self._api_key,
                "Content-Type": "application/json",
            }
        elif "v1" in self._base_url:
            headers = {
                "Authorization": "Bearer " + self._api_key,
                "Content-Type": "application/json",
            }
        if self._certificate_path:
            self._sslcontext = ssl.create_default_context()
            self._sslcontext.load_verify_locations(certificate_path)
        
        # Initialize a new `aiohttp` session
        self._req_session = aiohttp.ClientSession(
            headers=headers, timeout=aiohttp.ClientTimeout(total=single_request_timeout),
        )

        # Log API calls
        self._logger = logger
        self._parameters = locals()
        self._parameters["api_key"] = "*" * 36 + self._api_key[-4:]
        self._logger.info(
            f"Meraki dashboard API session initialized with these parameters: {self._parameters}"
        )

    async def request(self, metadata, method, url, **kwargs):
        # Metadata on endpoint
        tag = metadata["tags"][0]
        operation = metadata["operation"]

        # Update request kwargs with session defaults
        if self._certificate_path:
            kwargs.setdefault("ssl", self._sslcontext)
        kwargs.setdefault("timeout", self._single_request_timeout)

        # Ensure proper base URL
        if "meraki.com" in url:
            abs_url = url
        else:
            abs_url = self._base_url + url

        # Set maximum number of retries
        retries = self._maximum_retries

        # Option to simulate non-safe API calls without actually sending them
        self._logger.debug(metadata)
        if self._simulate and method != "GET":
            self._logger.info(f"{tag}, {operation} - SIMULATED")
            return None
        else:
            response = None
            for _ in range(retries):
                # Make the HTTP request to the API endpoint
                try:
                    response = await self._req_session.request(
                        method, abs_url, **kwargs
                    )
                    reason = response.reason if response.reason else None
                    status = response.status
                except Exception as e:
                    self._logger.warning(
                        f"{tag}, {operation} - {e}, retrying in 1 second"
                    )
                    await asyncio.sleep(1)

                if status == 200:
                    if "page" in metadata:
                        counter = metadata["page"]
                        self._logger.info(
                            f"{tag}, {operation}; page {counter} - {status} {reason}"
                        )
                    else:
                        self._logger.info(f"{tag}, {operation} - {status} {reason}")
                    # For non-empty response to GET, ensure valid JSON
                    try:
                        if method == "GET":
                            await response.json()
                        return response
                    except (
                        json.decoder.JSONDecodeError,
                        aiohttp.client_exceptions.ContentTypeError,
                    ) as e:
                        self._logger.warning(
                            f"{tag}, {operation} - {e}, retrying in 1 second"
                        )
                        await asyncio.sleep(1)
                # Handle 3XX redirects automatically
                elif 300 <= status < 400:
                    abs_url = response.headers["Location"]
                    substring = "meraki.com/api/v"
                    self._base_url = abs_url[
                        : abs_url.find(substring) + len(substring) + 1
                    ]
                # Rate limit 429 errors
                elif status == 429:
                    wait = int(response.headers["Retry-After"])
                    self._logger.warning(
                        f"{tag}, {operation} - {status} {reason}, retrying in {wait} seconds"
                    )
                    await asyncio.sleep(wait)
                # 5XX errors
                elif status >= 500:
                    self._logger.warning(
                        f"{tag}, {operation} - {status} {reason}, retrying in 1 second"
                    )
                    await asyncio.sleep(1)
                # 4XX errors
                else:
                    try:
                        message = await response.json()
                    except aiohttp.client_exceptions.ContentTypeError:
                        message = (await response.text())[:100]
                    self._logger.error(
                        f"{tag}, {operation} - {status} {reason}, {message}"
                    )
            raise AsyncAPIError(metadata, response, await response.text())

    async def get(self, metadata, url, params=None):
        metadata["method"] = "GET"
        metadata["url"] = url
        metadata["params"] = params
        response = await self.request(metadata, "GET", url, params=params)
        return await response.json()

    async def get_pages(
        self, metadata, url, params=None, total_pages=-1, direction="next"
    ):
        if type(total_pages) == str and total_pages.lower() == "all":
            total_pages = -1
        metadata["page"] = 1

        response = await self.request(metadata, "GET", url, params=params)
        results = await response.json()

        # Get additional pages if more than one requested
        while total_pages != 1:
            # Parse Link from headers
            links = response.headers["Link"].split(",")
            first = prev = next = last = None
            for l in links:
                if "rel=first" in l:
                    first = l[l.find("<") + 1 : l.find(">")]
                elif "rel=prev" in l:
                    prev = l[l.find("<") + 1 : l.find(">")]
                elif "rel=next" in l:
                    next = l[l.find("<") + 1 : l.find(">")]
                elif "rel=last" in l:
                    last = l[l.find("<") + 1 : l.find(">")]

            # GET the subsequent page
            if direction == "next" and next:
                metadata["page"] += 1
                response = await self.request(metadata, "GET", next)
            elif direction == "prev" and prev:
                metadata["page"] += 1
                response = await self.request(metadata, "GET", prev)
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
