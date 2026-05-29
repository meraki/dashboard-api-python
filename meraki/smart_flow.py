"""Per-org token bucket rate limiter for Meraki Dashboard API (smart flow).

The Meraki API enforces rate limits per organization (default 10 req/s). This module
provides proactive rate limiting that prevents 429 errors before they happen by
tracking request rates per org and throttling when approaching the limit.

Key concepts:
- URL patterns are parsed to extract org/network/device identifiers
- A lazy cache maps network IDs and device serials to their parent org ID
- Each org gets its own token bucket, refilling at the configured rate
- Unknown identifiers route through a conservative shared bucket until resolved
"""

from __future__ import annotations

import asyncio
import re
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Coroutine, Dict, Optional, Set

import json


# URL patterns for extracting resource identifiers
_ORG_PATTERN = re.compile(r"/organizations/([^/]+)")
_NETWORK_PATTERN = re.compile(r"/networks/([^/]+)")
_DEVICE_PATTERN = re.compile(r"/devices/([^/]+)")


def _parse_saved_at(value: Any) -> Optional[float]:
    """Parse ISO 8601Z saved_at timestamp to epoch seconds."""
    if not isinstance(value, str):
        return None
    try:
        dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
        return dt.timestamp()
    except ValueError:
        return None


class TokenBucket:
    """Thread-safe token bucket for synchronous rate limiting."""

    def __init__(self, rate: float, capacity: int):
        self._rate = rate
        self._capacity = capacity
        self._tokens = float(capacity)
        self._last = time.monotonic()
        self._lock = threading.Lock()

    @property
    def rate(self) -> float:
        return self._rate

    @rate.setter
    def rate(self, value: float) -> None:
        self._rate = max(0.5, value)

    def acquire(self) -> None:
        # Reserve the token (read-modify-write) under the lock, then sleep
        # outside it so concurrent callers don't serialize behind one sleeper.
        with self._lock:
            now = time.monotonic()
            # Refill, then deduct this request unconditionally. Tokens may go
            # negative: that deficit IS the reservation, so concurrent callers
            # each compute their own wait against the accumulated deficit rather
            # than all colliding on the same instant.
            elapsed = now - self._last
            self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
            self._last = now
            self._tokens -= 1.0

            wait = -self._tokens / self._rate if self._tokens < 0 else 0.0

        if wait > 0.0:
            time.sleep(wait)


class AsyncTokenBucket:
    """Async token bucket for asynchronous rate limiting."""

    def __init__(self, rate: float, capacity: int):
        self._rate = rate
        self._capacity = capacity
        self._tokens = float(capacity)
        self._last: Optional[float] = None
        self._lock = asyncio.Lock()

    @property
    def rate(self) -> float:
        return self._rate

    @rate.setter
    def rate(self, value: float) -> None:
        self._rate = max(0.5, value)

    async def acquire(self) -> None:
        # Reserve the token under the lock, then await the sleep OUTSIDE the
        # lock so concurrent coroutines on the same bucket aren't serialized
        # behind a single sleeper (preserving burst/parallelism).
        loop = asyncio.get_event_loop()
        async with self._lock:
            now = loop.time()
            if self._last is None:
                self._last = now

            # Refill, then deduct this request unconditionally. Tokens may go
            # negative: that deficit IS the reservation, so concurrent callers
            # each compute their own wait against the accumulated deficit rather
            # than all colliding on the same instant.
            elapsed = now - self._last
            self._tokens = min(self._capacity, self._tokens + elapsed * self._rate)
            self._last = now
            self._tokens -= 1.0

            wait = -self._tokens / self._rate if self._tokens < 0 else 0.0

        if wait > 0.0:
            await asyncio.sleep(wait)


class OrgRateLimiter:
    """Per-org rate limiter with URL-based routing and org resolution cache.

    Maintains a token bucket per organization and a shared "unknown" bucket for
    requests whose org cannot yet be determined. The cache maps network IDs and
    device serials to org IDs, populated eagerly at init or lazily from responses.
    """

    def __init__(
        self,
        rate: float = 10.0,
        capacity: int = 10,
        global_rate: float = 100.0,
        cache_path: Optional[str] = None,
        cache_ttl: Optional[float] = 604800.0,
        logger: Any = None,
    ):
        self._rate = rate
        self._capacity = capacity
        self._global_rate = global_rate
        self._logger = logger
        self._cache_path = Path(cache_path) if cache_path else None
        self._cache_ttl = cache_ttl

        # org_id -> bucket
        self._org_buckets: Dict[str, TokenBucket] = {}
        # network_id -> org_id, serial -> org_id
        self._network_to_org: Dict[str, str] = {}
        self._serial_to_org: Dict[str, str] = {}
        # Global bucket: source IP limit shared by all requests
        self._global_bucket = TokenBucket(rate=global_rate, capacity=int(global_rate))

        self._cache_fresh = False
        self._dirty = 0
        self._pending_lookups: Set[str] = set()
        self._hydrated_orgs: Set[str] = set()
        self._resolver: Optional[Callable[[str, str], Optional[str]]] = None
        self._hydrator: Optional[Callable[[str], None]] = None
        self._load_cache()

    def set_resolver(self, resolver: Callable[[str, str], Optional[str]]) -> None:
        """Set a callback to resolve unknown network/device IDs to org IDs.

        The callback receives (id_type, identifier) where id_type is "network" or "device",
        and should return the org_id or None.
        """
        self._resolver = resolver

    def set_hydrator(self, hydrator: Callable[[str], None]) -> None:
        """Set a callback to bulk-populate all networks/devices for an org.

        Called once per org after first resolution. The callback should call
        register_network/register_device for each mapping discovered.
        """
        self._hydrator = hydrator

    @property
    def cache_fresh(self) -> bool:
        return self._cache_fresh

    def _log(self, msg: str) -> None:
        if self._logger:
            self._logger.debug(f"smart_flow, {msg}")

    def _maybe_flush(self) -> None:
        if self._dirty >= 50:
            self.save_cache()
            self._dirty = 0

    def _get_or_create_bucket(self, org_id: str) -> TokenBucket:
        if org_id not in self._org_buckets:
            self._org_buckets[org_id] = TokenBucket(self._rate, self._capacity)
            self._log(f"new bucket for org {org_id} at {self._rate} req/s")
        return self._org_buckets[org_id]

    def resolve_org(self, url: str) -> Optional[str]:
        """Extract org ID from URL, using cache for network/device lookups."""
        m = _ORG_PATTERN.search(url)
        if m:
            return m.group(1)

        m = _NETWORK_PATTERN.search(url)
        if m:
            return self._network_to_org.get(m.group(1))

        m = _DEVICE_PATTERN.search(url)
        if m:
            return self._serial_to_org.get(m.group(1))

        return None

    def acquire(self, url: str) -> None:
        """Block until tokens are available from both global and per-org buckets."""
        self._global_bucket.acquire()

        org_id = self.resolve_org(url)
        if org_id:
            self._get_or_create_bucket(org_id).acquire()
        else:
            self._resolve_inline(url)
            org_id = self.resolve_org(url)
            if org_id:
                self._get_or_create_bucket(org_id).acquire()

    def _resolve_inline(self, url: str) -> None:
        """Attempt a synchronous lookup for an unresolved network/device ID."""
        if not self._resolver:
            return

        m = _NETWORK_PATTERN.search(url)
        if m:
            identifier, id_type = m.group(1), "network"
        else:
            m = _DEVICE_PATTERN.search(url)
            if m:
                identifier, id_type = m.group(1), "device"
            else:
                return

        if identifier in self._pending_lookups:
            return
        self._pending_lookups.add(identifier)
        try:
            org_id = self._resolver(id_type, identifier)
            if org_id:
                if id_type == "network":
                    self._network_to_org[identifier] = org_id
                else:
                    self._serial_to_org[identifier] = org_id
                self._get_or_create_bucket(org_id)
                self._dirty += 1
                self._log(f"resolved {id_type} {identifier} -> org {org_id}")
                if self._hydrator and org_id not in self._hydrated_orgs:
                    self._hydrated_orgs.add(org_id)
                    self._log(f"hydrating org {org_id}")
                    self._hydrator(org_id)
                    self._log(
                        f"hydrated org {org_id} "
                        f"({len(self._network_to_org)} networks, {len(self._serial_to_org)} devices total)"
                    )
                self._maybe_flush()
        except Exception:
            pass
        finally:
            self._pending_lookups.discard(identifier)

    def on_rate_limited(self, url: str) -> None:
        """Tighten the appropriate bucket (multiplicative decrease)."""
        org_id = self.resolve_org(url)
        if org_id and org_id in self._org_buckets:
            bucket = self._org_buckets[org_id]
            bucket.rate = bucket.rate * 0.7
            self._log(f"rate limited org {org_id}, decreased to {bucket.rate:.1f} req/s")
        elif self._is_unresolved_scoped_url(url):
            # URL targets a specific network/device whose org isn't resolved
            # yet. Penalizing the global bucket would punish every other org for
            # one org's 429, so skip and let background resolution catch up.
            self._log("rate limited on unresolved network/device url, skipping global penalty")
        else:
            self._global_bucket.rate = self._global_bucket.rate * 0.7
            self._log(f"rate limited (global), decreased to {self._global_bucket.rate:.1f} req/s")

    @staticmethod
    def _is_unresolved_scoped_url(url: str) -> bool:
        """True if the URL has a network/device component but no explicit org.

        These are the URLs whose org we can't yet attribute the 429 to; the
        offending org is specific (just unknown), so the global bucket must not
        be punished on its behalf. An explicit /organizations/<id> URL is NOT
        considered unresolved (it names its org directly).
        """
        if OrgRateLimiter._org_id_from_url(url):
            return False
        return bool(OrgRateLimiter._network_id_from_url(url) or OrgRateLimiter._serial_from_url(url))

    def on_success(self, url: str) -> None:
        """Slowly widen buckets back toward configured rates (additive increase)."""
        org_id = self.resolve_org(url)
        if org_id and org_id in self._org_buckets:
            bucket = self._org_buckets[org_id]
            if bucket.rate < self._rate:
                bucket.rate = min(self._rate, bucket.rate + 0.2)
        if self._global_bucket.rate < self._global_rate:
            self._global_bucket.rate = min(self._global_rate, self._global_bucket.rate + 0.5)

    def register_org(self, org_id: str) -> None:
        """Ensure a bucket exists for this org."""
        self._get_or_create_bucket(org_id)

    def register_network(self, network_id: str, org_id: str) -> None:
        """Cache a network -> org mapping."""
        self._network_to_org[network_id] = org_id

    def register_device(self, serial: str, org_id: str) -> None:
        """Cache a serial -> org mapping."""
        self._serial_to_org[serial] = org_id

    def learn_from_response(self, url: str, body: Any) -> None:
        """Extract org/network/device mappings from a URL and response body."""
        org_id = self._org_id_from_url(url)
        if not org_id:
            org_id = self._org_id_from_body(body)
        if not org_id:
            return

        self._get_or_create_bucket(org_id)
        changed_networks = 0
        changed_devices = 0

        network_id = self._network_id_from_url(url)
        if network_id and self._network_to_org.get(network_id) != org_id:
            self._network_to_org[network_id] = org_id
            changed_networks += 1

        serial = self._serial_from_url(url)
        if serial and self._serial_to_org.get(serial) != org_id:
            self._serial_to_org[serial] = org_id
            changed_devices += 1

        if isinstance(body, dict):
            n, d = self._learn_from_body(body, org_id)
            changed_networks += n
            changed_devices += d

        total = changed_networks + changed_devices
        if total:
            self._dirty += total
            if self._logger:
                self._log(
                    f"learned {total} new mapping{'s' if total != 1 else ''} "
                    f"({changed_networks} network{'s' if changed_networks != 1 else ''}, "
                    f"{changed_devices} device{'s' if changed_devices != 1 else ''}) "
                    f"from {url}"
                )
            self._maybe_flush()

    def _learn_from_body(self, body: dict, org_id: str) -> tuple:
        """Returns (changed_networks, changed_devices) counts."""
        changed_networks = 0
        changed_devices = 0
        if "networkId" in body and self._network_to_org.get(body["networkId"]) != org_id:
            self._network_to_org[body["networkId"]] = org_id
            changed_networks += 1
        if "serial" in body and self._serial_to_org.get(body["serial"]) != org_id:
            self._serial_to_org[body["serial"]] = org_id
            changed_devices += 1
        net = body.get("network")
        if isinstance(net, dict) and "id" in net:
            if self._network_to_org.get(net["id"]) != org_id:
                self._network_to_org[net["id"]] = org_id
                changed_networks += 1
        return changed_networks, changed_devices

    @staticmethod
    def _org_id_from_url(url: str) -> Optional[str]:
        m = _ORG_PATTERN.search(url)
        return m.group(1) if m else None

    @staticmethod
    def _network_id_from_url(url: str) -> Optional[str]:
        m = _NETWORK_PATTERN.search(url)
        return m.group(1) if m else None

    @staticmethod
    def _serial_from_url(url: str) -> Optional[str]:
        m = _DEVICE_PATTERN.search(url)
        return m.group(1) if m else None

    @staticmethod
    def _org_id_from_body(body: Any) -> Optional[str]:
        if not isinstance(body, dict):
            return None
        if "organizationId" in body:
            return body["organizationId"]
        org = body.get("organization")
        if isinstance(org, dict) and "id" in org:
            return org["id"]
        return None

    def save_cache(self) -> None:
        """Persist the mapping cache to disk with a timestamp."""
        if not self._cache_path:
            return
        self._cache_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "saved_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "networks": [{"id": net_id, "organization": {"id": org_id}} for net_id, org_id in self._network_to_org.items()],
            "devices": [{"serial": serial, "organization": {"id": org_id}} for serial, org_id in self._serial_to_org.items()],
        }
        self._cache_path.write_text(json.dumps(data), encoding="utf-8")
        n = len(self._network_to_org) + len(self._serial_to_org)
        self._log(f"saved cache ({n} mappings) to {self._cache_path}")

    def _load_cache(self) -> None:
        """Load mapping cache from disk if it exists and hasn't expired."""
        if not self._cache_path or not self._cache_path.exists():
            return
        try:
            data = json.loads(self._cache_path.read_text(encoding="utf-8"))
            if self._cache_ttl is not None:
                saved_at = data.get("saved_at")
                if saved_at is None:
                    self._log("cache expired, will rebuild")
                    return
                saved_ts = _parse_saved_at(saved_at)
                if saved_ts is None or (time.time() - saved_ts) > self._cache_ttl:
                    self._log("cache expired, will rebuild")
                    return
            for net in data.get("networks", []):
                self._network_to_org[net["id"]] = net["organization"]["id"]
            for dev in data.get("devices", []):
                self._serial_to_org[dev["serial"]] = dev["organization"]["id"]
            self._cache_fresh = True
            n = len(self._network_to_org) + len(self._serial_to_org)
            self._log(f"loaded cache ({n} mappings) from {self._cache_path}")
        except (json.JSONDecodeError, OSError, KeyError):
            pass


class AsyncOrgRateLimiter:
    """Async per-org rate limiter with URL-based routing and org resolution cache.

    Same strategy as OrgRateLimiter but uses AsyncTokenBucket for non-blocking waits.
    """

    def __init__(
        self,
        rate: float = 10.0,
        capacity: int = 10,
        global_rate: float = 100.0,
        cache_path: Optional[str] = None,
        cache_ttl: Optional[float] = 604800.0,
        logger: Any = None,
    ):
        self._rate = rate
        self._capacity = capacity
        self._global_rate = global_rate
        self._logger = logger
        self._cache_path = Path(cache_path) if cache_path else None
        self._cache_ttl = cache_ttl

        self._org_buckets: Dict[str, AsyncTokenBucket] = {}
        self._network_to_org: Dict[str, str] = {}
        self._serial_to_org: Dict[str, str] = {}
        self._global_bucket = AsyncTokenBucket(rate=global_rate, capacity=int(global_rate))

        self._cache_fresh = False
        self._dirty = 0
        self._flush_task: Optional[asyncio.Task] = None
        # Hold strong refs to in-flight background tasks; the event loop only
        # keeps weak refs, so without this they can be GC'd mid-flight.
        self._bg_tasks: Set[asyncio.Task] = set()
        self._pending_lookups: Set[str] = set()
        self._hydrated_orgs: Set[str] = set()
        self._resolver: Optional[Callable[[str, str], Coroutine[Any, Any, Optional[str]]]] = None
        self._hydrator: Optional[Callable[[str], Coroutine[Any, Any, None]]] = None
        self._load_cache()

    def set_resolver(self, resolver: Callable[[str, str], Coroutine[Any, Any, Optional[str]]]) -> None:
        """Set a callback to resolve unknown network/device IDs to org IDs.

        The callback receives (id_type, identifier) where id_type is "network" or "device",
        and should return the org_id or None.
        """
        self._resolver = resolver

    def set_hydrator(self, hydrator: Callable[[str], Coroutine[Any, Any, None]]) -> None:
        """Set a callback to bulk-populate all networks/devices for an org.

        Called once per org after first resolution. The callback should call
        register_network/register_device for each mapping discovered.
        """
        self._hydrator = hydrator

    @property
    def cache_fresh(self) -> bool:
        return self._cache_fresh

    def _log(self, msg: str) -> None:
        if self._logger:
            self._logger.debug(f"smart_flow, {msg}")

    def _maybe_flush(self) -> None:
        if self._dirty >= 50 and (self._flush_task is None or self._flush_task.done()):
            pending = self._dirty
            self._flush_task = asyncio.ensure_future(self.save_cache())
            self._flush_task.add_done_callback(lambda t: self._on_flush_done(t, pending))

    def _on_flush_done(self, task: asyncio.Task, pending: int) -> None:
        # Only zero the dirty counter if the save actually succeeded; otherwise
        # the unsaved mappings would be silently lost.
        exc = task.exception()
        if exc is not None:
            self._log(f"cache flush failed, retaining {pending} dirty mappings: {exc!r}")
            return
        # Subtract what we flushed rather than hard-zeroing, in case more
        # mappings were learned while the save was in flight.
        self._dirty = max(0, self._dirty - pending)

    def _get_or_create_bucket(self, org_id: str) -> AsyncTokenBucket:
        if org_id not in self._org_buckets:
            self._org_buckets[org_id] = AsyncTokenBucket(self._rate, self._capacity)
            self._log(f"new bucket for org {org_id} at {self._rate} req/s")
        return self._org_buckets[org_id]

    def resolve_org(self, url: str) -> Optional[str]:
        """Extract org ID from URL, using cache for network/device lookups."""
        m = _ORG_PATTERN.search(url)
        if m:
            return m.group(1)

        m = _NETWORK_PATTERN.search(url)
        if m:
            return self._network_to_org.get(m.group(1))

        m = _DEVICE_PATTERN.search(url)
        if m:
            return self._serial_to_org.get(m.group(1))

        return None

    async def acquire(self, url: str) -> None:
        """Await until tokens from both global and per-org buckets are available."""
        await self._global_bucket.acquire()

        org_id = self.resolve_org(url)
        if org_id:
            await self._get_or_create_bucket(org_id).acquire()
        else:
            self._trigger_background_resolve(url)

    def _trigger_background_resolve(self, url: str) -> None:
        """Fire a one-shot background lookup for an unresolved network/device ID."""
        if not self._resolver:
            return

        m = _NETWORK_PATTERN.search(url)
        if m:
            identifier, id_type = m.group(1), "network"
        else:
            m = _DEVICE_PATTERN.search(url)
            if m:
                identifier, id_type = m.group(1), "device"
            else:
                return

        if identifier in self._pending_lookups:
            return
        self._pending_lookups.add(identifier)
        t = asyncio.ensure_future(self._resolve_and_cache(id_type, identifier))
        self._bg_tasks.add(t)
        t.add_done_callback(self._bg_tasks.discard)

    async def _resolve_and_cache(self, id_type: str, identifier: str) -> None:
        """Background task: call resolver, cache result, then hydrate the full org."""
        try:
            org_id = await self._resolver(id_type, identifier)
            if not org_id:
                return
            if id_type == "network":
                self._network_to_org[identifier] = org_id
            else:
                self._serial_to_org[identifier] = org_id
            self._get_or_create_bucket(org_id)
            self._dirty += 1
            self._log(f"resolved {id_type} {identifier} -> org {org_id}")
            if self._hydrator and org_id not in self._hydrated_orgs:
                self._hydrated_orgs.add(org_id)
                self._log(f"hydrating org {org_id}")
                await self._hydrator(org_id)
                self._log(
                    f"hydrated org {org_id} ({len(self._network_to_org)} networks, {len(self._serial_to_org)} devices total)"
                )
            self._maybe_flush()
        except Exception as e:
            self._log(f"background resolve of {id_type} {identifier} failed: {e!r}")
        finally:
            self._pending_lookups.discard(identifier)

    def on_rate_limited(self, url: str) -> None:
        """Tighten the appropriate bucket (multiplicative decrease)."""
        org_id = self.resolve_org(url)
        if org_id and org_id in self._org_buckets:
            bucket = self._org_buckets[org_id]
            bucket.rate = bucket.rate * 0.7
            self._log(f"rate limited org {org_id}, decreased to {bucket.rate:.1f} req/s")
        elif OrgRateLimiter._is_unresolved_scoped_url(url):
            # URL targets a specific network/device whose org isn't resolved
            # yet. Penalizing the global bucket would punish every other org for
            # one org's 429, so skip and let background resolution catch up.
            self._log("rate limited on unresolved network/device url, skipping global penalty")
        else:
            self._global_bucket.rate = self._global_bucket.rate * 0.7
            self._log(f"rate limited (global), decreased to {self._global_bucket.rate:.1f} req/s")

    def on_success(self, url: str) -> None:
        """Slowly widen buckets back toward configured rates (additive increase)."""
        org_id = self.resolve_org(url)
        if org_id and org_id in self._org_buckets:
            bucket = self._org_buckets[org_id]
            if bucket.rate < self._rate:
                bucket.rate = min(self._rate, bucket.rate + 0.2)
        if self._global_bucket.rate < self._global_rate:
            self._global_bucket.rate = min(self._global_rate, self._global_bucket.rate + 0.5)

    async def shutdown(self) -> None:
        """Gracefully drain background work and persist the cache.

        Awaits/cancels all in-flight resolve tasks, awaits any pending flush,
        then does a final save. Idempotent and safe to call when there is no
        outstanding work (e.g. from an __aexit__ handler).
        """
        if self._bg_tasks:
            await asyncio.gather(*list(self._bg_tasks), return_exceptions=True)
        if self._flush_task is not None and not self._flush_task.done():
            try:
                await self._flush_task
            except Exception as e:
                self._log(f"flush task errored during shutdown: {e!r}")
        await self.save_cache()

    def register_org(self, org_id: str) -> None:
        """Ensure a bucket exists for this org."""
        self._get_or_create_bucket(org_id)

    def register_network(self, network_id: str, org_id: str) -> None:
        """Cache a network -> org mapping."""
        self._network_to_org[network_id] = org_id

    def register_device(self, serial: str, org_id: str) -> None:
        """Cache a serial -> org mapping."""
        self._serial_to_org[serial] = org_id

    def learn_from_response(self, url: str, body: Any) -> None:
        """Extract org/network/device mappings from a URL and response body."""
        org_id = OrgRateLimiter._org_id_from_url(url)
        if not org_id:
            org_id = OrgRateLimiter._org_id_from_body(body)
        if not org_id:
            return

        self._get_or_create_bucket(org_id)
        changed_networks = 0
        changed_devices = 0

        network_id = OrgRateLimiter._network_id_from_url(url)
        if network_id and self._network_to_org.get(network_id) != org_id:
            self._network_to_org[network_id] = org_id
            changed_networks += 1

        serial = OrgRateLimiter._serial_from_url(url)
        if serial and self._serial_to_org.get(serial) != org_id:
            self._serial_to_org[serial] = org_id
            changed_devices += 1

        if isinstance(body, dict):
            if "networkId" in body and self._network_to_org.get(body["networkId"]) != org_id:
                self._network_to_org[body["networkId"]] = org_id
                changed_networks += 1
            if "serial" in body and self._serial_to_org.get(body["serial"]) != org_id:
                self._serial_to_org[body["serial"]] = org_id
                changed_devices += 1
            net = body.get("network")
            if isinstance(net, dict) and "id" in net:
                if self._network_to_org.get(net["id"]) != org_id:
                    self._network_to_org[net["id"]] = org_id
                    changed_networks += 1

        total = changed_networks + changed_devices
        if total:
            self._dirty += total
            if self._logger:
                self._log(
                    f"learned {total} new mapping{'s' if total != 1 else ''} "
                    f"({changed_networks} network{'s' if changed_networks != 1 else ''}, "
                    f"{changed_devices} device{'s' if changed_devices != 1 else ''}) "
                    f"from {url}"
                )
            self._maybe_flush()

    async def save_cache(self) -> None:
        """Persist the mapping cache to disk in a background thread."""
        if not self._cache_path:
            return
        path = self._cache_path
        data = json.dumps(
            {
                "saved_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "networks": [
                    {"id": net_id, "organization": {"id": org_id}} for net_id, org_id in self._network_to_org.items()
                ],
                "devices": [
                    {"serial": serial, "organization": {"id": org_id}} for serial, org_id in self._serial_to_org.items()
                ],
            }
        )
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, self._write_cache, path, data)
        n = len(self._network_to_org) + len(self._serial_to_org)
        self._log(f"saved cache ({n} mappings) to {path}")

    @staticmethod
    def _write_cache(path: Path, data: str) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(data, encoding="utf-8")

    def _load_cache(self) -> None:
        """Load mapping cache from disk if it exists and hasn't expired."""
        if not self._cache_path or not self._cache_path.exists():
            return
        try:
            data = json.loads(self._cache_path.read_text(encoding="utf-8"))
            if self._cache_ttl is not None:
                saved_at = data.get("saved_at")
                if saved_at is None:
                    self._log("cache expired, will rebuild")
                    return
                saved_ts = _parse_saved_at(saved_at)
                if saved_ts is None or (time.time() - saved_ts) > self._cache_ttl:
                    self._log("cache expired, will rebuild")
                    return
            for net in data.get("networks", []):
                self._network_to_org[net["id"]] = net["organization"]["id"]
            for dev in data.get("devices", []):
                self._serial_to_org[dev["serial"]] = dev["organization"]["id"]
            self._cache_fresh = True
            n = len(self._network_to_org) + len(self._serial_to_org)
            self._log(f"loaded cache ({n} mappings) from {self._cache_path}")
        except (json.JSONDecodeError, OSError, KeyError):
            pass
