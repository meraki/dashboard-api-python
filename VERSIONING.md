# Versioning

This document covers the SDK versioning strategy and how it relates to the upstream dashboard API.

## Which version should I use?

Use the latest stable release:

```sh
pip install --upgrade meraki
```

Only use a different release if:

- You want to test out the latest SDK features that aren't yet stable, or
- You want access to beta API operations that haven't graduated to GA yet, and you accept that those operations may change or disappear in future releases, even if you don't update or change your library version.

## How do I know which version I'm using?

If you're using v3.x+:

```python
import meraki
print(meraki.__version__)       # SDK version, e.g. "4.1.0b2"
print(meraki.__api_version__)   # API version, e.g. "1.70.0-beta.2"
```

Otherwise, please see [Releases](https://github.com/meraki/dashboard-api-python/releases).

### Why aren't the SDK version and the API version linked (as of [SDK 2.x, released April 8, 2025](https://github.com/meraki/dashboard-api-python/releases/tag/2.0.0))?

The library and the API are related but separate software. Improving the SDK sometimes requires SDK-only changes, which in turn necessitates bumping the SDK version separately from the upstream API.

## Scheme

```text
MAJOR.MINOR.PATCH[bN]
```

| Segment | Bumped when                                                                                                             |
| ------- | ----------------------------------------------------------------------------------------------------------------------- |
| MAJOR   | SDK-only breaking changes are made (new HTTP backend, generated code structure changes, Python version support changes) |
| MINOR   | New upstream API release (tracks Meraki dashboard API minor versions)                                                   |
| PATCH   | SDK bug fixes or upstream API patch releases                                                                            |
| bN      | Pre-release beta suffix for unreleased major/minor tracks, including upstream API beta operations                       |

## Objective

The repo maintainers work to streamline the adoption of new major SDK versions and minimize breaking changes. The general expectation is as follows:

- if you are exclusively using GA operations from the upstream API, and
- if you are keeping your local Python environment updated to [a contemporary Python version](https://devguide.python.org/versions/), i.e., a version that is not already nor end of life within 6 months, and
- if you are sticking to the SDK's own supported surfaces (i.e., not monkey-patching the library)

Then you should be able to update your environment to the latest stable library version without breaking changes to your application.

If you identify any unexpected breaking changes that are not a result of the upstream API changing, then please [report the issue](https://github.com/meraki/dashboard-api-python/issues).

## Beta Convention

Pre-release versions use PEP 440 beta suffixes: `4.1.0b1`, `4.1.0b2`, etc.

Beta releases are published to PyPI and installable via `pip install meraki==4.1.0b2`. They are not installed by default (`pip install meraki` gets the latest stable).

### API operation coverage

- **Stable releases** contain only GA (stable) operations from the upstream API. If an operation is marked beta in the dashboard API spec, it is excluded from stable builds.
- **Beta releases** may include beta API operations from the dashboard API in addition to all GA operations. These operations are subject to change or removal without notice by the upstream API, since beta API operations are subject to unannounced breaking changes.

This means upgrading from a beta to a stable release can _remove_ operations that were previously available, if those operations have not yet graduated to GA upstream.

## SDK-to-API Version Mapping

Each SDK minor release is generated from a specific dashboard API version:

| SDK | API          | Status      | What changed                                                                                                          |
| --- | ------------ | ----------- | --------------------------------------------------------------------------------------------------------------------- |
| 4.x | v1.70.0+     | Development | httpx migration (unified sync/async backend), supported Python version changes, all major developments moving forward |
| 3.x | v1.69.0+     | Stable      | OASv3-based, automated release pipeline, supported Python version changes                                             |
| 2.x | v1 (various) | Deprecated  | Internal overhaul (async via aiohttp, pagination, logging, supported Python version changes)                          |
| 1.x | v1 (various) | Deprecated  | Initial v1 API library, requests-based                                                                                |

Within a major, the minor version/patch versions advance with each API release. For example, 3.1.0 was generated from API v1.70.0.

Patch versions can also advance based on SDK-only fixes.

## Where Versions Live

| What            | Location                                                           |
| --------------- | ------------------------------------------------------------------ |
| SDK version     | `meraki/_version.py` (`__version__`), `pyproject.toml` (`version`) |
| API version     | `meraki/__init__.py` (`__api_version__`)                           |
| Git tags        | `4.1.0b2` (no `v` prefix for 2.x+)                                 |
| Release commits | `Auto-generated library v{SDK} for API v{API}.`                    |

## Release Triggers

- **Automated**: the generator runs when a new OpenAPI spec is detected, producing a minor bump
- **Manual**: major versions and SDK-only patches are released by maintainers
