"""Synchronous REST session for Meraki Dashboard API."""

from __future__ import annotations

import time
import urllib.parse
from datetime import datetime, timezone
from typing import Any, Dict, Optional

import httpx

from meraki.common import (
    iterator_for_get_pages_bool,
    use_iterator_for_get_pages_setter,
)
from meraki.exceptions import SessionInputError
from meraki.smart_limiter import OrgRateLimiter
from meraki.session.base import SessionBase


class RestSession(SessionBase):
    """Synchronous session using httpx.Client.

    Inherits config, retry loop, and status dispatch from SessionBase.
    Implements transport-specific sleep and request methods.
    """

    def __init__(self, logger, api_key, **kwargs: Any) -> None:
        super().__init__(logger, api_key, **kwargs)

        # Build client config from session config (per D-06: requests_proxy -> proxy kwarg)
        client_kwargs: Dict[str, Any] = {
            "timeout": self._single_request_timeout,
        }
        if self._certificate_path:
            client_kwargs["verify"] = self._certificate_path
        if self._requests_proxy:
            client_kwargs["proxy"] = self._requests_proxy

        # Persistent httpx client with connection pooling
        self._client = httpx.Client(**client_kwargs)
        self._client.headers.update(self._build_headers())

        # Per-org smart limiter (opt-in)
        if self._smart_limiting:
            self._smart_limiter = OrgRateLimiter(
                rate=self._smart_limit_requests_per_second,
                capacity=int(self._smart_limit_requests_per_second),
                cache_path=self._smart_limit_cache_path or None,
                cache_ttl=self._smart_limit_cache_ttl,
                logger=self._logger if self._smart_limit_logging else None,
            )
            self._smart_limiter.set_resolver(self._resolve_org_for_limiter)
            self._smart_limiter.set_hydrator(self._hydrate_org_for_limiter)

    def close(self):
        """Close the underlying httpx.Client and release connections."""
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    @property
    def use_iterator_for_get_pages(self):
        return iterator_for_get_pages_bool(self)

    @use_iterator_for_get_pages.setter
    def use_iterator_for_get_pages(self, value):
        use_iterator_for_get_pages_setter(self, value)

    def _send_request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        """Send HTTP request via persistent httpx.Client."""
        response = self._client.request(method, url, follow_redirects=False, **kwargs)
        return response

    def _sleep(self, seconds: float) -> None:
        """Blocking sleep for retry delays."""
        time.sleep(seconds)

    def _transport_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """No-op: httpx config handled at client initialization level."""
        return kwargs

    # ------------------------------------------------------------------
    # Smart limiter resolver
    # ------------------------------------------------------------------

    def _resolve_org_for_limiter(self, id_type: str, identifier: str) -> Optional[str]:
        """Resolve a network/device ID to its org by calling the API directly."""
        if id_type == "network":
            endpoint = f"{self._base_url}/networks/{identifier}"
        else:
            endpoint = f"{self._base_url}/devices/{identifier}"
        try:
            response = self._client.request("GET", endpoint, follow_redirects=True)
            if response.status_code == 200:
                data = response.json()
                return data.get("organizationId")
        except Exception:
            pass
        return None

    def _hydrate_org_for_limiter(self, org_id: str) -> None:
        """Fetch all networks and devices for an org and register them with the limiter."""
        networks = self._fetch_all_pages(f"{self._base_url}/organizations/{org_id}/networks?perPage=1000")
        for net in networks:
            if "id" in net:
                self._smart_limiter.register_network(net["id"], org_id)

        devices = self._fetch_all_pages(f"{self._base_url}/organizations/{org_id}/inventoryDevices?perPage=1000")
        for dev in devices:
            if "serial" in dev:
                self._smart_limiter.register_device(dev["serial"], org_id)

    def _fetch_all_pages(self, url: str) -> list:
        """Paginate through a Meraki list endpoint using Link headers."""
        results = []
        while url:
            response = self._client.request("GET", url, follow_redirects=True)
            if response.status_code != 200:
                break
            page = response.json()
            if isinstance(page, list):
                results.extend(page)
            next_link = response.links.get("next", {}).get("url")
            url = next_link if next_link else None
        return results

    # ------------------------------------------------------------------
    # Convenience HTTP methods
    # ------------------------------------------------------------------

    def get(self, metadata, url, params=None):
        metadata["method"] = "GET"
        metadata["url"] = url
        metadata["params"] = params
        response = self.request(metadata, "GET", url, params=params)
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def post(self, metadata, url, json=None):
        metadata["method"] = "POST"
        metadata["url"] = url
        metadata["json"] = json
        response = self.request(metadata, "POST", url, json=json)
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def put(self, metadata, url, json=None):
        metadata["method"] = "PUT"
        metadata["url"] = url
        metadata["json"] = json
        response = self.request(metadata, "PUT", url, json=json)
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def delete(self, metadata, url, params=None):
        metadata["method"] = "DELETE"
        metadata["url"] = url
        metadata["params"] = params
        response = self.request(metadata, "DELETE", url, params=params)
        if response:
            response.close()
        return None

    # ------------------------------------------------------------------
    # Pagination
    # ------------------------------------------------------------------

    def get_pages(self, metadata, url, params=None, total_pages=-1, direction="next", event_log_end_time=None):
        """Dispatch to iterator or legacy pagination based on config."""
        if self._use_iterator_for_get_pages:
            return self._get_pages_iterator(metadata, url, params, total_pages, direction, event_log_end_time)
        return self._get_pages_legacy(metadata, url, params, total_pages, direction, event_log_end_time)

    def _get_pages_iterator(
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

        response = self.request(metadata, "GET", url, params=params)

        # Get additional pages if more than one requested
        while total_pages != 0:
            results = response.json()
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
                    # Or if the next page is past the specified window's end time
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

            response.close()

            return_items = []
            # Just prepare the list
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

            total_pages = total_pages - 1

            if total_pages != 0:
                response = self.request(metadata, "GET", nextlink)

    def _get_pages_legacy(
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

        response = self.request(metadata, "GET", url, params=params)

        # Handle GETs that produce 204 No Content responses
        if response.status_code == 204:
            results = None
        else:
            results = response.json()

        # For event log endpoint when using 'next' direction, so results/events are sorted chronologically
        if isinstance(results, dict) and metadata["operation"] == "getNetworkEvents" and direction == "next":
            results["events"] = results["events"][::-1]

        # Get additional pages if more than one requested
        while total_pages != 1:
            links = response.links
            response.close()
            response = None

            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(links["next"]["url"].split("startingAfter=")[1])
                    delta = datetime.now(timezone.utc) - datetime.fromisoformat(starting_after)
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300:
                        break
                    # Or if next page is past the specified window's end time
                    elif event_log_end_time and starting_after > event_log_end_time:
                        break

                metadata["page"] += 1
                response = self.request(metadata, "GET", links["next"]["url"])
            elif direction == "prev" and "prev" in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(links["prev"]["url"].split("endingBefore=")[1])
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < "2014-01-01":
                        break

                metadata["page"] += 1
                response = self.request(metadata, "GET", links["prev"]["url"])
            else:
                break

            # Append that page's results, depending on the endpoint
            if isinstance(results, list):
                results.extend(response.json())
            elif isinstance(results, dict) and "items" in results:
                results["items"].extend(response.json()["items"])
                if "meta" in results:
                    results["meta"]["counts"]["items"]["remaining"] = response.json()["meta"]["counts"]["items"]["remaining"]
            # For event log endpoint
            elif isinstance(results, dict):
                try:
                    start = response.json()["pageStartAt"]
                except KeyError:
                    if self._logger:
                        self._logger.warning(f"pageStartAt missing from response: {response.headers}")
                    start = results["pageStartAt"]  # fallback: keep existing value
                end = response.json()["pageEndAt"]
                events = response.json()["events"]
                if direction == "next":
                    events = events[::-1]
                if start < results["pageStartAt"]:
                    results["pageStartAt"] = start
                if end > results["pageEndAt"]:
                    results["pageEndAt"] = end
                results["events"].extend(events)

            total_pages -= 1

        if response:
            response.close()

        return results
