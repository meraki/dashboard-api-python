# Changelog

All notable changes to this library are documented here.

This file is maintained with [towncrier](https://towncrier.readthedocs.io/);
add a news fragment under `changelog.d/` for every user-facing change. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the fragment format.

<!-- towncrier release notes start -->

## 4.3.0 (2026-07-09)

### Added

- On 5xx responses, the SDK now logs the Meraki `X-Request-Id` response header so it can be shared with Meraki to look up the request in server-side logs. If the header is absent, `none` is logged in its place. After retries are exhausted, the request ID is also logged at error level.


## 4.2.0b1 (2026-06-10)

### Changed

- Migrated the HTTP transport layer from `requests`/`aiohttp` to `httpx`.
