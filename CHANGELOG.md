# Changelog

All notable changes to this library are documented here.

This file is maintained with [towncrier](https://towncrier.readthedocs.io/);
add a news fragment under `changelog.d/` for every user-facing change. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the fragment format.

<!-- towncrier release notes start -->

## 4.5.0b4 (2026-09-30)

### Fixed

- `DashboardAPI` and `AsyncDashboardAPI` now expose the `nac`, `secureConnect`, `support`, `users`, and `assistant` categories. They were generated but never registered, so accessing them raised `AttributeError` even though the underlying API methods worked. ([#472](https://github.com/meraki/dashboard-api-python/issues/472))
