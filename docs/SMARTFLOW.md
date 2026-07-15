# Smart Flow — Rate Limiter Specification

Language-agnostic spec for the Meraki proactive rate limiter. The Python
reference implementation is `meraki/smart_flow.py`; this document defines the
*behavior* so any implementation (Python, PowerShell, .NET, …) can be verified
against the same conformance vectors in `smartflow-vectors.json`.

Goal: prevent 429s before they happen by throttling per-organization request
rates locally, plus a global per-source-IP ceiling, learning which org each
network/device belongs to as traffic flows.

---

## 1. Token bucket

The primitive. One bucket = one rate limit.

**State:** `rate` (tokens/sec), `capacity` (max tokens), `tokens` (current, float),
`last` (monotonic timestamp of last refill).

**Init:** `tokens = capacity`, `last =` monotonic now at creation.
(The async reference lazily sets `last` on the first `acquire`; equivalent to
setting it at creation when no time passes before the first call.)

**`acquire()`** — the whole algorithm, executed atomically per bucket:

```
now      = monotonic()
elapsed  = now - last
tokens   = min(capacity, tokens + elapsed * rate)   # refill
last     = now
tokens   = tokens - 1                                # deduct unconditionally
wait     = (-tokens / rate) if tokens < 0 else 0     # deficit -> sleep
if wait > 0: sleep(wait)
```

Critical properties, all load-bearing for parity:

- **Deduct unconditionally; tokens may go negative.** The negative value *is* the
  reservation. Concurrent callers each compute their own `wait` against the
  accumulated deficit instead of colliding on the same instant. Do **not** clamp
  tokens at zero.
- **Reserve under lock, sleep outside it.** Compute `wait` while holding the
  per-bucket lock, release, then sleep. Serializing the sleeps destroys burst
  parallelism.
- **`rate` has a floor of 0.5.** Setting `rate` to anything lower clamps to `0.5`
  (prevents AIMD decrease from stalling a bucket to zero throughput).

---

## 2. Rate defaults

| Bucket | rate | capacity |
| --- | --- | --- |
| Per-org | `10.0` (SDK config default surfaces `9`) | `10` |
| Global (per source IP) | `100.0` | `100` (`int(global_rate)`) |

Meraki enforces ~10 req/s per org and ~100 req/s per source IP. Per-org default
is set below the ceiling to reserve headroom for other apps.

---

## 3. URL → identifier extraction

Three regexes, searched (not full-match) against the request URL:

| Identifier | Pattern | Capture |
| --- | --- | --- |
| org | `/organizations/([^/]+)` | org id |
| network | `/networks/([^/]+)` | network id |
| device | `/devices/([^/]+)` | serial |

**`resolve_org(url)`** returns the first that resolves:

1. org id directly from URL → return it
2. else network id from URL → look up `network_to_org[net]` (may be `None`)
3. else serial from URL → look up `serial_to_org[serial]` (may be `None`)
4. else `None`

---

## 4. acquire(url)

```
global_bucket.acquire()            # always, first
org = resolve_org(url)
if org:
    bucket(org).acquire()          # get-or-create org bucket
else:
    resolve_inline(url)            # sync ref; async fires a background task
    org = resolve_org(url)
    if org: bucket(org).acquire()
```

Global bucket is charged on **every** request regardless of org resolution.
An unresolved request pays only the global cost until its org is learned.

**Sync vs async divergence (the one intentional difference):**
- Sync `resolve_inline` calls the resolver **inline and blocks**, so a freshly
  resolved org's bucket is acquired *in the same call*.
- Async `_trigger_background_resolve` fires a one-shot background task and does
  **not** block; the org bucket is acquired on *subsequent* calls once learned.

An implementation without async (e.g. PowerShell sync) follows the sync path.

---

## 5. AIMD rate adaptation

Additive-increase / multiplicative-decrease on top of the static limits.

**`on_rate_limited(url)`** (called on a 429):

```
org = resolve_org(url)
if org has a bucket:
    bucket.rate *= 0.7                       # multiplicative decrease
elif url is an "unresolved scoped url":
    skip                                     # do NOT penalize global
else:
    global_bucket.rate *= 0.7
```

**Unresolved scoped URL** = URL has a network or device component but **no**
explicit `/organizations/<id>`. The offending org is specific but unknown;
penalizing the global bucket would punish every other org for one org's 429, so
skip and let resolution catch up.

**`on_success(url)`** (called on a 2xx):

```
org = resolve_org(url)
if org has a bucket and bucket.rate < configured_org_rate:
    bucket.rate = min(configured_org_rate, bucket.rate + 0.2)   # additive increase
if global_bucket.rate < configured_global_rate:
    global_bucket.rate = min(configured_global_rate, global_bucket.rate + 0.5)
```

Increments: **+0.2** per-org, **+0.5** global. Decrease factor: **×0.7** both.
Remember the `0.5` rate floor from §1 bounds the decrease.

---

## 6. Learning org mappings

**`learn_from_response(url, body)`** — called on successful GET responses to
populate the net→org / serial→org caches.

Resolve the governing org first:
1. org id from URL (`/organizations/<id>`), else
2. org id from body: `body.organizationId`, else `body.organization.id`
3. if neither → return (nothing learned)

Then record mappings (only counting ones that *change* an existing value):

- network id from **URL** → `network_to_org`
- serial from **URL** → `serial_to_org`
- from **body**: `body.networkId`, `body.serial`, `body.network.id`

Each changed mapping increments a `dirty` counter (see §7).

Explicit registration API (used by eager hydration / resolver callbacks):
`register_org(org)`, `register_network(net, org)`, `register_device(serial, org)`.

---

## 7. Disk cache

Persists learned mappings across sessions so warm runs skip re-learning.

**Format** (`rate_limit_cache.json`, default `~/.meraki/.cache/`):

```json
{
  "saved_at": "2026-07-08T12:00:00Z",
  "networks": [{ "id": "N_1", "organization": { "id": "O_1" } }],
  "devices":  [{ "serial": "Q2XX-XXXX-XXXX", "organization": { "id": "O_1" } }]
}
```

**`saved_at`** is UTC, format `%Y-%m-%dT%H:%M:%SZ` (trailing `Z`, no offset).

**Load / freshness:**
- No file → start empty.
- TTL default `604800` s (7 days). `None` = never expire.
- Expired if `saved_at` missing, unparseable, or `now - saved_at > ttl` →
  ignore file, rebuild. `cache_fresh` stays false.
- On fresh load, populate both maps; set `cache_fresh = true`.
- Malformed JSON / missing keys / IO error → swallow, start empty.

**Flush cadence:** when `dirty >= 50`, save and reset the counter. Async saves on
a background thread and only subtracts the flushed count on success (unsaved
mappings are retained, not lost, if the write fails). Async `shutdown()` drains
in-flight resolves + pending flush, then does a final save.

---

## 8. Resolver & hydrator callbacks

Hooks the SDK wires in so the limiter can fill its cache without knowing about
HTTP:

- **resolver** `(id_type, identifier) -> org_id | None`, `id_type ∈ {"network","device"}`.
  Called for an unresolved id. Guarded by a `pending_lookups` set so the same id
  isn't resolved twice concurrently.
- **hydrator** `(org_id) -> void`. Called **once per org** (tracked in
  `hydrated_orgs`) after first resolution, to bulk-register all of that org's
  networks/devices via the register APIs.

---

## Conformance

`smartflow-vectors.json` encodes deterministic cases for each section above
(bucket math with injected timestamps, URL resolution, AIMD, learning, cache
freshness). An implementation is conformant if it reproduces every vector's
expected output. See that file's `notes` field per case.
