# Releasing

## Automated releases

A GitHub Action polls [meraki/openapi releases](https://github.com/meraki/openapi/releases) daily at 14:00 UTC. When a new release is detected, it triggers library regeneration, runs tests, and publishes automatically.

## Versioning rules

1. **Source of truth is the target branch.** The current library minor version is read from `pyproject.toml` on `main` (GA), `beta` (pre-releases), or `httpx` (dev pre-releases).

2. **GA releases go to `main`.** Bump library minor, reset patch: `X.Y.Z` becomes `X.(Y+1).0`.

3. **Beta releases go to `beta`.** Library patch and beta number mirror the API release:
   - Library patch = API patch (e.g. API `1.81.2-beta.0` → library patch `2`)
   - Library beta number = API beta number (e.g. API `1.81.2-beta.3` → `bN` where N=3)
   - New API minor bumps library minor (e.g. API minor 80 → 81 bumps library minor)

4. **Dev releases go to `httpx`.** Same versioning logic as beta (mirrors API patch and beta number). Triggered by the same prerelease tags. The generator runs with the `-b httpx` flag and a test org ID for beta endpoint access.

5. **API version is the OpenAPI tag with `v` stripped.** `v1.71.0-beta.2` becomes `1.71.0-beta.2`.

6. **Manual releases can happen independently.** Patches, features, or fixes can be released at any time. They update `pyproject.toml` on their target branch, and the next automated release uses that as its baseline.

7. **GA always bumps minor, never patch.** Even after manual patches (e.g. `3.1.1` becomes `3.2.0`, not `3.1.2`).

8. **No version slot is reused.** If a manual release occupies the next expected version, the automated release takes the one after it.

## Examples

Starting from `main` at `3.1.0`, `beta` at `3.1.0`, `httpx` at `4.0.0`:

| Event | API Version | Library Version | Branch |
| --- | --- | --- | --- |
| `v1.71.0-beta.0` detected | `1.71.0-beta.0` | `3.2.0b0` | `beta` |
| (same trigger) | `1.71.0-beta.0` | `4.1.0b0` | `httpx` |
| `v1.71.0-beta.1` detected | `1.71.0-beta.1` | `3.2.0b1` | `beta` |
| (same trigger) | `1.71.0-beta.1` | `4.1.0b1` | `httpx` |
| `v1.71.1-beta.0` detected | `1.71.1-beta.0` | `3.2.1b0` | `beta` |
| (same trigger) | `1.71.1-beta.0` | `4.1.1b0` | `httpx` |
| Manual bugfix (no API change) | `1.70.0` | `3.1.1` | `main` |
| `v1.71.0` detected (GA) | `1.71.0` | `3.2.0` | `main` |
| `v1.72.0-beta.0` detected | `1.72.0-beta.0` | `3.3.0b0` | `beta` |
| (same trigger) | `1.72.0-beta.0` | `4.2.0b0` | `httpx` |

## Beta/dev release additional step

When a new prerelease is detected, the `enable-early-access.yml` workflow runs first (waited on synchronously). This enables early access features on the test organizations so the generated beta and dev SDKs can be tested against them.

## Release branches and PRs

| Stage | Source branch | Release branch | PR target |
| --- | --- | --- | --- |
| GA | `main` | `release` | `main` |
| Beta | `beta` | `beta-release` | `beta` |
| Dev | `httpx` | `httpx-release` | `httpx` |

All release PRs are set to auto-merge (squash). Once merged and tests pass, the `create-release.yml` workflow creates a GitHub release, which triggers `publish-release.yml` to publish to PyPI.
