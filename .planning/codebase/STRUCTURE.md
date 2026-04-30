# Codebase Structure

**Analysis Date:** 2026-04-29

## Directory Layout

```
meraki/
├── __init__.py                 # DashboardAPI entry point (sync)
├── _version.py                 # Version string
├── config.py                   # Configuration constants and defaults
├── exceptions.py               # Exception classes (APIError, APIKeyError, etc.)
├── common.py                   # Utility functions (validation, version checks)
├── rest_session.py             # RestSession HTTP layer (sync)
├── response_handler.py         # Response processing utilities
├── aio/
│   ├── __init__.py             # AsyncDashboardAPI entry point (async)
│   ├── rest_session.py         # AsyncRestSession HTTP layer (async)
│   └── api/
│       ├── administered.py     # AsyncAdministered scope
│       ├── organizations.py    # AsyncOrganizations scope
│       ├── networks.py         # AsyncNetworks scope
│       ├── devices.py          # AsyncDevices scope
│       ├── [+ 13 more scope files]
│       └── ...
└── api/
    ├── __init__.py             # API module init
    ├── administered.py         # Administered scope
    ├── organizations.py        # Organizations scope
    ├── networks.py             # Networks scope
    ├── devices.py              # Devices scope
    ├── appliance.py            # Appliance scope
    ├── camera.py               # Camera scope
    ├── cellularGateway.py      # CellularGateway scope
    ├── campusGateway.py        # CampusGateway scope
    ├── insight.py              # Insight scope
    ├── licensing.py            # Licensing scope
    ├── sensor.py               # Sensor scope
    ├── sm.py                   # Systems Manager scope
    ├── spaces.py               # Spaces scope
    ├── switch.py               # Switch scope
    ├── wireless.py             # Wireless scope
    ├── wirelessController.py   # WirelessController scope
    └── batch/
        ├── __init__.py         # Batch class aggregator
        ├── organizations.py    # ActionBatchOrganizations
        ├── networks.py         # ActionBatchNetworks
        ├── devices.py          # ActionBatchDevices
        ├── [+ more batch scopes]
        └── ...

tests/
├── unit/
│   ├── test_dashboard_api_init.py              # DashboardAPI initialization tests
│   ├── test_aio_rest_session.py                # AsyncRestSession tests
│   ├── test_common.py                          # common.py utility tests
│   ├── test_mock_integration.py                # Mock integration tests
│   └── test_exceptions.py                      # Exception tests
├── integration/
│   ├── test_dashboard_api_python_library.py    # Live API tests (requires key)
│   ├── test_async_dashboard_api.py             # Async integration tests
│   └── conftest.py                             # Integration test fixtures
└── generator/
    ├── test_generate_library_golden.py         # Golden file comparison tests
    ├── test_pure_functions.py                  # Generator utility tests
    ├── conftest.py                             # Generator test fixtures
    └── golden/
        ├── meraki/api/networks.py              # Expected generated output (sync)
        ├── meraki/aio/api/networks.py          # Expected generated output (async)
        └── meraki/api/batch/networks.py        # Expected generated output (batch)

generator/
├── generate_library.py                         # Main OpenAPI v2 library generator
├── generate_library_oasv3.py                   # OpenAPI v3 library generator
├── generate_snippets.py                        # Code snippet generator
├── function_template.jinja2                    # Template for sync operation methods
├── async_function_template.jinja2              # Template for async operation methods
├── batch_function_template.jinja2              # Template for batch operation methods
├── class_template.jinja2                       # Template for scope class wrapper
├── async_class_template.jinja2                 # Template for async scope class wrapper
├── batch_class_template.jinja2                 # Template for batch scope class wrapper
├── common.py                                   # Generator utility functions
└── README.md                                   # Generator documentation

examples/
├── org_wide_clients.py                         # Example: list all clients in org
├── aio_org_wide_clients.py                     # Example: async client listing
├── aio_ips2firewall.py                         # Example: async L7 firewall automation
└── merakiApplianceVlanToL3SwitchInterfaceMigrator/
    └── ...                                     # Example: network migration tool

notebooks/
└── Uplink preference backup and restore/
    └── ...                                     # Jupyter notebook examples
```

## Directory Purposes

**meraki/:**
- Purpose: Main package containing synchronous SDK
- Contains: Entry points, HTTP session, configuration, exceptions, utility functions
- Key files: `__init__.py` (DashboardAPI), `rest_session.py` (HTTP layer), `config.py` (defaults)

**meraki/api/:**
- Purpose: Scope classes for synchronous API operations
- Contains: 17 resource type classes (Organizations, Networks, Devices, etc.) each exposing operations from OpenAPI spec
- Key files: `organizations.py`, `networks.py`, `devices.py` (primary scopes)

**meraki/api/batch/:**
- Purpose: Batch operation helper classes for Action Batch support
- Contains: Specialized classes for staging batch requests without immediate execution
- Key files: `__init__.py` (Batch aggregator), scope files mirror api/ structure

**meraki/aio/:**
- Purpose: Asynchronous SDK using asyncio/aiohttp
- Contains: Async entry point and HTTP session, mirrors api/ structure
- Key files: `__init__.py` (AsyncDashboardAPI), `rest_session.py` (async HTTP layer)

**meraki/aio/api/:**
- Purpose: Scope classes for asynchronous API operations
- Contains: 17 async scope classes (AsyncOrganizations, AsyncNetworks, etc.)
- Key files: Mirror meraki/api/ structure with Async prefix and await keywords

**tests/unit/:**
- Purpose: Unit tests for SDK internals, runnable without API key
- Contains: DashboardAPI initialization, RestSession behavior, utilities, exceptions
- Key files: `test_dashboard_api_init.py` (initialization tests), `test_common.py` (utility tests)

**tests/integration/:**
- Purpose: Integration tests against live Meraki API
- Contains: Full workflows requiring valid API key and test organization
- Key files: `test_dashboard_api_python_library.py` (sync tests), `test_async_dashboard_api.py` (async tests)

**tests/generator/:**
- Purpose: Validation of code generation from OpenAPI spec
- Contains: Golden file comparison tests ensuring generated code matches expected output
- Key files: `test_generate_library_golden.py` (output validation), `golden/` (expected files)

**generator/:**
- Purpose: OpenAPI spec to Python SDK code generation
- Contains: Jinja2 templates for method/class generation, parser for OpenAPI spec
- Key files: `generate_library.py` (OpenAPI v2), `generate_library_oasv3.py` (OpenAPI v3), `*_template.jinja2` (templates)

**examples/:**
- Purpose: Runnable example scripts demonstrating SDK usage
- Contains: Real-world use cases like client listing, firewall automation
- Key files: `org_wide_clients.py` (basic example), `aio_ips2firewall.py` (async example)

**notebooks/:**
- Purpose: Jupyter notebook examples for exploratory usage
- Contains: Interactive workflows for specific tasks
- Key files: Uplink preference backup/restore notebook

## Key File Locations

**Entry Points:**
- `meraki/__init__.py`: DashboardAPI class - instantiate with api_key, exposes scope properties
- `meraki/aio/__init__.py`: AsyncDashboardAPI class - async context manager, exposes async scope properties
- `meraki/__main__.py`: Module runnable (if present) or package import for scripts

**Configuration:**
- `meraki/config.py`: All default constants (timeouts, retry counts, log settings, etc.)
- `meraki/_version.py`: __version__ string (auto-generated)
- No .env file in repository; env vars read from MERAKI_DASHBOARD_API_KEY, BE_GEO_ID, MERAKI_PYTHON_SDK_CALLER

**Core Logic:**
- `meraki/rest_session.py`: RestSession with request(), get(), post(), put(), delete(), get_pages()
- `meraki/aio/rest_session.py`: AsyncRestSession with identical interface using aiohttp
- `meraki/api/{scope}.py`: Scope classes (17 total) with operation methods
- `meraki/aio/api/{scope}.py`: Async scope classes (17 total) mirroring sync structure

**Request Handling:**
- `meraki/rest_session.py`: HTTP client implementation, retry logic, rate limiting, pagination
- `meraki/aio/rest_session.py`: Async HTTP client implementation
- `meraki/response_handler.py`: Response processing (3xx redirect handling)
- `meraki/common.py`: Validation functions called during initialization

**Error Handling:**
- `meraki/exceptions.py`: APIKeyError, APIError, AsyncAPIError, PythonVersionError, SessionInputError

**Testing:**
- `tests/unit/`: Mock-based tests, no API key required
- `tests/integration/`: Live API tests, requires MERAKI_DASHBOARD_API_KEY
- `tests/generator/`: Code generation validation against golden files
- Golden files at `tests/generator/golden/meraki/api/networks.py`, `meraki/aio/api/networks.py`, `meraki/api/batch/networks.py`

## Naming Conventions

**Files:**
- Scope resource names: camelCase with first letter lowercase (organizations.py, networkDevices.py, cellularGateway.py)
- Test files: test_{module_under_test}.py or test_{feature}.py
- Generated code: Classes have generated names matching OpenAPI operationId, methods match API paths
- Templates: {context}_template.jinja2 (function_template.jinja2, async_function_template.jinja2, batch_function_template.jinja2)

**Directories:**
- Scope directories: lowercase (api/, aio/, batch/)
- Test groupings: unit/, integration/, generator/
- Generator artifacts: golden/ for expected outputs

**Classes:**
- Sync scopes: PascalCase (Organizations, Networks, Devices)
- Async scopes: Async{SyncName} (AsyncOrganizations, AsyncNetworks, AsyncDevices)
- Batch scopes: ActionBatch{SyncName} (ActionBatchOrganizations, ActionBatchNetworks)
- Main classes: DashboardAPI (sync), AsyncDashboardAPI (async)
- Exceptions: {Context}Error (APIKeyError, APIError, AsyncAPIError)
- Sessions: RestSession (sync), AsyncRestSession (async)

**Methods:**
- API operations: camelCase matching OpenAPI operationId (getOrganizations, createNetwork, updateDevice)
- Private methods: underscore prefix (_get_pages_iterator, _get_pages_legacy, _session)
- Properties: snake_case (use_iterator_for_get_pages property)
- Dunder methods: __init__, __repr__, __str__, __async_enter__, __async_exit__

**Variables:**
- Module-level constants: SCREAMING_SNAKE_CASE (API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL)
- Instance attributes: underscore prefix + snake_case (self._api_key, self._base_url, self._session)
- Local variables: snake_case (params, resource, metadata, total_pages)
- Generator context: camelCase matching OpenAPI (perPage, startingAfter, endingBefore, organizationId)

## Where to Add New Code

**New API Scope (when OpenAPI spec adds resource):**
- Sync implementation: `meraki/api/{scope_name}.py` with class {ScopeName} inheriting from object, methods call self._session.{verb}()
- Async implementation: `meraki/aio/api/{scope_name}.py` with class Async{ScopeName}, methods call await self._session.{verb}()
- Batch helper: `meraki/api/batch/{scope_name}.py` with class ActionBatch{ScopeName} (stateless helper)
- Register in: `meraki/__init__.py` (add import and self.{scope_name} property), `meraki/aio/__init__.py` (async equivalent)
- Pattern: Follow existing scope file structure (getResource, createResource, updateResource, deleteResource methods)

**New Operation (when OpenAPI spec adds endpoint):**
- Add method to existing scope class in `meraki/api/{scope}.py` and `meraki/aio/api/{scope}.py`
- Cannot manually add; operations are auto-generated from OpenAPI spec using generator/
- If manually modifying for testing: follow kwargs.update(locals()), metadata dict, resource path, params extraction pattern
- Register operation in batch scope if applicable: `meraki/api/batch/{scope}.py`

**New Utility Function:**
- Shared helpers: `meraki/common.py` (Python checks, validation)
- Response processing: `meraki/response_handler.py` (HTTP response handling)
- Exception handling: Add new exception class to `meraki/exceptions.py`

**New Tests:**
- Unit tests: `tests/unit/test_{feature}.py` with mocked RestSession
- Integration tests: `tests/integration/test_{feature}.py` with live API calls
- Generator tests: `tests/generator/test_{aspect}.py` with golden file comparisons
- Test fixtures: Add to `tests/{category}/conftest.py` (pytest fixtures)

**New Examples:**
- Example scripts: `examples/{use_case}.py` as runnable Python scripts
- Jupyter notebooks: `notebooks/{use_case}/` directory with .ipynb file
- README: Document in examples/README.md and top-level README.md

## Special Directories

**meraki/api/batch/:**
- Purpose: Batch operation helpers
- Generated: Partially (method stubs auto-generated)
- Committed: Yes, checked in to version control
- Special: Classes are stateless, only build request dicts, do not execute HTTP calls

**tests/generator/golden/:**
- Purpose: Expected output from code generation
- Generated: Auto-generated by running generator
- Committed: Yes, checked in for golden file comparison
- Special: Used as test fixtures; when generator output matches golden files, tests pass

stitute:
- Purpose: Cache files
- Generated: Yes
- Committed: No (.gitignore excludes)
- Special: Safe to delete; will be regenerated on next build/test

**.venv/:**
- Purpose: Python virtual environment
- Generated: Created by `uv sync`
- Committed: No (.gitignore excludes)
- Special: Development only; production uses different installation method

## Generated vs Manual Code

**Generated (from OpenAPI spec):**
- All scope operation methods: Organizations.getOrganizations(), Networks.createNetwork(), etc.
- Scope class definitions and parameters
- Batch operation stubs
- Generated via `python generator/generate_library_oasv3.py`

**Manual (hand-written):**
- RestSession HTTP layer: `meraki/rest_session.py`, `meraki/aio/rest_session.py`
- DashboardAPI initialization: `meraki/__init__.py`, `meraki/aio/__init__.py`
- Exception classes: `meraki/exceptions.py`
- Configuration constants: `meraki/config.py`
- Utility functions: `meraki/common.py`
- Tests: All test files
- Generator itself: `generator/*.py`
