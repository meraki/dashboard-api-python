# Meraki Dashboard API Python Library

A Python client for the Cisco Meraki [dashboard API](https://developer.cisco.com/meraki/api-v1/), covering every
current operation. It's generated from the API's OpenAPI spec, so it tracks the latest releases automatically. The full
source, including the generator, is here for Early Access participants and contributors; pull requests that maintain
backwards compatibility are welcome. Requires Python 3.10+, community-supported, installable via
[PyPI](https://pypi.org/project/meraki/):

    pip install --upgrade meraki

Or with [uv](https://docs.astral.sh/uv/):

    uv pip install --upgrade meraki

If you participate
in [our Early Access program](https://community.meraki.com/t5/Developers-APIs/UPDATED-Beta-testing-with-the-Meraki-Developer-Early-Access/m-p/145344#M5808)
and would like to use early access features via the library, you have two options: install a published
[beta release](#releases) from PyPI (`pip install meraki==<version>bN`), or, if you need a library matched to your own
org's spec, [generate one yourself](https://github.com/meraki/dashboard-api-python/tree/main/generator#readme).

### [Features](#features) · [Releases](#releases) · [Usage](#usage) · [Smart flow](#smart-flow-rate-limiting) · [AsyncIO](#asyncio) · [Versioning](VERSIONING.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

## Features

You could hit the dashboard API with raw HTTP in any language. But then you own the rate-limit math, the retry loops,
the pagination bookkeeping, the auth headers, and the error handling, for every one of the hundreds of operations, and
you re-own it every time the API changes. This library does all of that for you, and stays current automatically because
it's generated from the API's own OpenAPI spec.

What you get out of the box:

- **Complete, always-current operation coverage** — every dashboard API operation, generated straight from the
  [OpenAPI specification](https://api.meraki.com/api/v1/openapiSpec), so new operations land as the API ships them
- **Proactive rate limiting ("smart flow")** — per-org token buckets keep you under Meraki's 10 req/s org limit and
  100 req/s source-IP limit _before_ you get throttled, turning 429-and-retry churn into steady throughput. On by
  default, zero config. [Details below.](#smart-flow-rate-limiting)
- **Automatic retries** — 429s honor the [`Retry-After`](https://developer.cisco.com/meraki/api-v1/#!rate-limit)
  header; transient 5xx and select 4xx (network-delete/action-batch concurrency) back off and retry so your script
  doesn't fall over on a blip
- **Built-in pagination** — pull all pages, or a specific number, with one call; no manual Link-header walking
- **Sync and async** — a synchronous client and a fully `async`/`await` client
  ([AsyncIO](#asyncio)) sharing the same interface, so you scale up concurrency without rewriting your logic
- **Modern HTTP stack** — built on [httpx](https://www.python-httpx.org/) (not `requests`/`aiohttp`), a unified,
  type-annotated, HTTP/2-capable backend powering both the sync and async clients
- **Early access via beta releases** — opt into beta builds to use API operations before they reach GA, in step with
  Meraki's [Early Access program](https://community.meraki.com/t5/Developers-APIs/UPDATED-Beta-testing-with-the-Meraki-Developer-Early-Access/m-p/145344#M5808). [Details below.](#releases)
- **Dry-run mode** — simulate POST/PUT/DELETE calls to preview changes without touching your network configuration
- **Logging you can trust** — every request logged to file and console, with X-Request-Id captured on failures for
  fast support escalation to Meraki
- **Kwarg validation** — optional typo protection that warns when an unrecognized keyword argument would otherwise be
  silently ignored, catching bugs before they ship
- **Tunable everything** — retries, timeouts, certificate path, proxy, logging verbosity, and more, all configurable
  per client or via environment

## Setup

1. Enable API access in your Meraki dashboard organization and obtain an API
   key ([instructions](https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API))

2. Keep your API key safe and secure, as it is similar to a password for your dashboard. If publishing your Python code
   to a wider audience, please research secure handling of API keys.

3. Install [Python 3.10 or later](https://wiki.python.org/moin/BeginnersGuide/NonProgrammers)

4. Use _pip_ to install the library from the
   Python [Package Index](https://pypi.org/project/meraki/):
   - `pip install meraki`
   - If _meraki_ was previously installed, you can upgrade to the latest non-beta release
     with `pip install --upgrade meraki`

5. The library supports Meraki dashboard API v1. To install or check a specific version:
   - `pip install meraki==4.3.0` installs that version (see the full [release history](https://pypi.org/project/meraki/#history))
   - `pip show meraki` reports the version currently installed
   - Picking between stable and beta releases is covered under [Releases](#releases) below

## Releases

`pip install --upgrade meraki` gets the latest **stable (GA)** release, which contains only GA operations from the
upstream dashboard API. Stable releases track upstream API minor versions and are published automatically when a new
OpenAPI spec ships.

**Beta releases** (PEP 440 suffix, e.g. `4.3.0b1`) may also include beta API operations that haven't graduated to GA.
They are published to PyPI but never installed by default; opt in explicitly:

```shell
pip install meraki==4.3.0b1
```

Both the beta API operations they expose and the SDK surfaces themselves may change in breaking ways between beta releases, without notice. Beta API operations are subject to unannounced change or removal upstream, so upgrading from a beta to a stable release can _remove_ operations that never reached GA. Use a beta release only if you need early-access API operations or unreleased SDK features and accept that trade-off.

For the full versioning scheme, cadence, and SDK-to-API version mapping, see [VERSIONING.md](VERSIONING.md).

## Usage

1. Export your API key as
   an [environment variable](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html), for example:

   ```shell
   export MERAKI_DASHBOARD_API_KEY=YOUR_KEY_HERE
   ```

2. Alternatively, define it as a variable in your source code (not recommended: it's insecure).

3. Import the library at the top of your script:

   ```python
   import meraki
   ```

4. Instantiate the client (API consumer class), optionally specifying any of the parameters available to set:

   ```python
   dashboard = meraki.DashboardAPI()
   ```

5. Make dashboard API calls in your source code, using the format _client.scope.operation_, where _client_ is the name
   you defined in the previous step (**dashboard** above), _scope_ is the corresponding scope that represents the first
   tag from the OpenAPI spec, and _operation_ is the operation ID from the OpenAPI spec. For example, to make a call to
   get the list of organizations accessible by the API key defined in step 1, use this function call:

   ```python
   my_orgs = dashboard.organizations.getOrganizations()
   ```

### Examples

You can find fully working example scripts in the **examples** folder.

| Script                  | Purpose                                                                                                                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **org_wide_clients.py** | That code collects the clients of all networks, in all orgs to which the key has access. No changes are made, since only GET operations are called, and the data is written to local CSV output files. |

### Keyword argument validation

All optional parameters are passed as keyword arguments (`**kwargs`). By default, if you pass a misspelled or
unsupported kwarg, it is silently ignored. Enable `validate_kwargs` to log a warning when this happens:

```python
dashboard = meraki.DashboardAPI(validate_kwargs=True)

# This will log a warning: "updateNetwork: ignoring unrecognized kwargs: ['nme']"
dashboard.networks.updateNetwork(networkId, nme="HQ")
```

This is off by default for backwards compatibility and zero performance overhead in production.

## Smart flow rate limiting

The Meraki API enforces two rate limits: **10 requests/second per organization** and **100 requests/second per source
IP**. Exceed either and you get `429` responses. The traditional approach is reactive: send too fast, get a 429, wait
for `Retry-After`, retry. That wastes round-trips, and every 429 you generate also eats into the budget shared by other
applications hitting the same org.

Smart flow is **proactive**. Each org gets its own token bucket, so the SDK paces requests to stay under the limit
_before_ sending, turning 429-and-retry churn into steady throughput. It's **enabled by default** with no code changes
required.

Benefits:

- **Fewer 429s** — requests are throttled client-side instead of bouncing off the server
- **Faster overall** — no `Retry-After` wait cycles wasted on avoidable rate-limit errors
- **Fairer** — reserves headroom (default 9 of 10 req/s per org) so you don't starve other apps on the same org
- **Zero-config** — org membership is learned automatically from the URLs you already call, and cached to disk
  (`~/.meraki/.cache/`) so subsequent runs skip the lookup

Tune it via kwargs on the client (all optional):

```python
dashboard = meraki.DashboardAPI(
    smart_flow_enabled=True,      # default; set False to fall back to 429-retry only
    smart_flow_org_rate=9,        # max req/s per org (leaves 1 for other apps)
    smart_flow_global_rate=100,   # max req/s across all orgs (source-IP limit)
    smart_flow_cache_mode="lazy", # "lazy" learns as you go; "eager" pre-fetches at init
)
```

See [config.py](https://github.com/meraki/dashboard-api-python/blob/main/meraki/config.py) for the full set of smart
flow options and their defaults.

## AsyncIO

The library ships a fully async client (`meraki.aio.AsyncDashboardAPI`) using **async/await**, alongside the
synchronous client. Original async port by Heimo Stieg ([@coreGreenberet](https://github.com/coreGreenberet)).

### Usage

Same as the synchronous client, with four differences: import `meraki.aio`, instantiate inside `async with`, `await`
each call, and run it all in an event loop.

```python
import asyncio
import meraki.aio


async def main():
    # `async with` ensures the client's sessions are closed on exit
    async with meraki.aio.AsyncDashboardAPI() as aiomeraki:
        my_orgs = await aiomeraki.organizations.getOrganizations()


if __name__ == "__main__":
    asyncio.run(main())
```

### Examples

You can find fully working example scripts in the **examples** folder.
| Script                      | Purpose                                                                                                                                                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **aio_org_wide_clients.py** | An asyncio port of org_wide_clients.py: collects the clients of all networks, in all orgs to which the key has access. No changes are made, since only GET operations are called, and data is written to local CSVs. |
| **aio_ips2firewall.py**     | Collects the source IP of security events and creates L7 firewall rules to block them. `usage: aio_ips2firewall.py [-h] -o ORGANIZATIONS [ORGANIZATIONS ...] [-f FILTER] [-s] [-d DAYS]`                            |

## Note for application developers and ecosystem partners

Identify your application with every API request by following the format defined
in [config.py](https://github.com/meraki/dashboard-api-python/blob/main/meraki/config.py) and passing the session
kwarg:

```Python
MERAKI_PYTHON_SDK_CALLER
```

Unless you are an ecosystem partner, this identifier is optional.

1. If you are an ecosystem partner and you have questions about this requirement, please reach out to your ecosystem
   rep.
2. If you have any questions about the formatting, please ask your question by opening an issue in this repo.

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and builds with
[Hatchling](https://hatch.pypa.io/).

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already.

2. Install dev dependencies:

   uv sync

3. Run tests:

   uv run pytest

4. If you're working with the generator, install its additional dependencies:

   uv sync --group generator

## Further documentation

| Doc                                        | Covers                                            |
| ------------------------------------------ | ------------------------------------------------- |
| [CHANGELOG.md](CHANGELOG.md)               | Release notes per version                         |
| [VERSIONING.md](VERSIONING.md)             | Versioning scheme, GA vs beta, SDK-to-API mapping |
| [CONTRIBUTING.md](CONTRIBUTING.md)         | How to contribute and add changelog fragments     |
| [SECURITY.md](SECURITY.md)                 | Reporting security issues                         |
| [generator/README.md](generator/README.md) | Regenerating the library and Early Access usage   |
