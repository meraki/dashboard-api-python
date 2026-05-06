# Releasing

## Automated releases

A GitHub Action polls [meraki/openapi releases](https://github.com/meraki/openapi/releases) daily at 14:00 UTC. When a new release is detected, it triggers library regeneration, runs tests, and publishes automatically.

## Versioning rules

1. **Source of truth is the target branch.** The current library minor version is read from `pyproject.toml` on `main` (GA) or `beta` (pre-releases).

2. **GA releases go to `main`.** Bump library minor, reset patch: `X.Y.Z` becomes `X.(Y+1).0`.

3. **Beta releases go to `beta`.** Library patch and beta number mirror the API release:
   - Library patch = API patch (e.g. API `1.81.2-beta.0` → library patch `2`)
   - Library beta number = API beta number (e.g. API `1.81.2-beta.3` → `bN` where N=3)
   - New API minor bumps library minor (e.g. API minor 80 → 81 bumps library minor)

4. **API version is the OpenAPI tag with `v` stripped.** `v1.71.0-beta.2` becomes `1.71.0-beta.2`.

5. **Manual releases can happen independently.** Patches, features, or fixes can be released at any time. They update `pyproject.toml` on their target branch, and the next automated release uses that as its baseline.

6. **GA always bumps minor, never patch.** Even after manual patches (e.g. `3.1.1` becomes `3.2.0`, not `3.1.2`).

7. **No version slot is reused.** If a manual release occupies the next expected version, the automated release takes the one after it.

## Examples

Starting from `main` at `3.1.0`, `beta` at `3.1.0`:

| Event | API Version | Library Version | Branch |
| --- | --- | --- | --- |
| `v1.71.0-beta.0` detected | `1.71.0-beta.0` | `3.2.0b0` | `beta` |
| `v1.71.0-beta.1` detected | `1.71.0-beta.1` | `3.2.0b1` | `beta` |
| `v1.71.1-beta.0` detected | `1.71.1-beta.0` | `3.2.1b0` | `beta` |
| Manual bugfix (no API change) | `1.70.0` | `3.1.1` | `main` |
| `v1.71.0` detected | `1.71.0` | `3.2.0` | `main` |
| `v1.72.0-beta.0` detected | `1.72.0-beta.0` | `3.3.0b0` | `beta` |

## Beta release additional step

When a new beta release is detected, the `enable-early-access.yml` workflow runs first. This enables early access features on the test organization so the generated beta SDK can be tested against them.
