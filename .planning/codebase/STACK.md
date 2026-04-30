# Technology Stack

**Analysis Date:** 2026-04-29

## Languages

**Primary:**
- Python 3.11+ - Main language for SDK and all client implementations

**Supporting:**
- Jinja2 (templating) - Used in code generator for API endpoint generation

## Runtime

**Environment:**
- CPython 3.11+ required per `pyproject.toml`

**Package Manager:**
- uv (modern Python package manager)
- Lockfile: `uv.lock` present
- Build system: Hatchling via `hatchling` backend

## Frameworks

**Core HTTP:**
- requests 2.33.1-2.99.x - Synchronous HTTP client for REST API calls (`meraki/rest_session.py`)
- aiohttp 3.13.5-3.99.x - Asynchronous HTTP client for concurrent API calls (`meraki/aio/rest_session.py`)

**Testing:**
- pytest 8.3.5-9.x - Test runner
- pytest-asyncio 1.0-1.x - AsyncIO support for tests
- pytest-cov 7.1.0-7.x - Code coverage tracking

**Code Quality:**
- flake8 7.0-7.x - Linting
- ruff 0.15.12+ - Fast linter and formatter

**Development:**
- pre-commit 4.6.0+ - Git hook framework
- responses 0.25-0.x - HTTP mocking for tests

**Generator:**
- Jinja2 3.1.6 - Template rendering for code generation

## Key Dependencies

**Critical:**
- requests - Handles all synchronous HTTP communication with Meraki Dashboard API (`https://api.meraki.com/api/v1`)
- aiohttp - Enables concurrent API requests via AsyncIO for performance-critical applications

**Build/Runtime:**
- hatchling - Build backend for wheel and sdist generation

**Testing/Development:**
- responses - Mocks HTTP responses in unit tests without hitting real API
- pytest-asyncio - Manages async test execution and event loop lifecycle

## Configuration

**Environment:**
- API key: `MERAKI_DASHBOARD_API_KEY` environment variable (fallback to constructor parameter)
- Optional partner ID: `BE_GEO_ID` environment variable (deprecated but supported)
- Optional caller identifier: `MERAKI_PYTHON_SDK_CALLER` environment variable for API usage tracking
- Configuration file: `meraki/config.py` contains default values for all session parameters

**Build:**
- `pyproject.toml` - Project metadata, dependencies, tool configuration
- `[tool.ruff]` - Line length set to 127
- `[tool.pytest.ini_options]` - Test paths: `tests/unit`, test mode: `auto` for asyncio
- `[tool.coverage.run]` - Coverage source: `meraki/` module, excludes auto-generated API endpoints

**Dependency Groups:**
- `dev` - Testing and linting tools (pytest, flake8, ruff, pre-commit, responses)
- `generator` - Code generation dependencies (jinja2)

## Platform Requirements

**Development:**
- Python 3.11+
- uv package manager installed
- Pre-commit hooks configured via `.pre-commit-config.yaml`

**Production:**
- Python 3.11+
- requests library installed
- aiohttp library installed (only if using AsyncIO API)
- Network connectivity to `https://api.meraki.com/api/v1` (default endpoint)
- Alternate regional endpoints supported:
  - Canada: `https://api.meraki.ca/api/v1`
  - China: `https://api.meraki.cn/api/v1`
  - India: `https://api.meraki.in/api/v1`
  - US Federal: `https://api.gov-meraki.com/api/v1`

## Version

**Current:** 3.0.0 (aligns with Dashboard API v1.69.0)

---

*Stack analysis: 2026-04-29*
