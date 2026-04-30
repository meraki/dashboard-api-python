---
phase: quick
plan: 01
type: execute
wave: 1
depends_on: []
files_modified:
  - tests/integration/test_pagination_iterator.py
  - tests/integration/test_async_pagination_iterator.py
  - tests/integration/test_org_wide_workflows.py
autonomous: true
must_haves:
  truths:
    - "Sync pagination iterator yields same networks as legacy mode"
    - "Async pagination iterator yields same networks as legacy mode"
    - "Multi-endpoint org-wide workflow completes (orgs -> networks -> clients)"
    - "Async concurrent client fetching works via asyncio.as_completed"
    - "getOrganizationApiRequests returns records with expected fields"
  artifacts:
    - path: "tests/integration/test_pagination_iterator.py"
      provides: "Sync pagination + API requests log tests"
    - path: "tests/integration/test_async_pagination_iterator.py"
      provides: "Async pagination iterator tests"
    - path: "tests/integration/test_org_wide_workflows.py"
      provides: "Sync and async org-wide client workflow tests"
---

<objective>
Create integration tests covering the SDK's pagination iterator (sync+async), org-wide multi-endpoint workflows (sync+async), and API requests log endpoint.

Purpose: Validate SDK machinery (pagination modes, async iteration, concurrent fetching) against live API.
Output: Three new test files in tests/integration/
</objective>

<context>
@tests/integration/conftest.py
@tests/integration/test_async_dashboard_api.py
@tests/integration/test_dashboard_api_python_library.py
@examples/get_pages_iterator.py
@examples/aio_get_pages_iterator.py
@examples/org_wide_clients_v1.py
@examples/aio_org_wide_clients_v1.py
@examples/apiData2CSV_v1.py
</context>

<tasks>

<task type="auto">
  <name>Task 1: Sync pagination iterator + API requests log tests</name>
  <files>tests/integration/test_pagination_iterator.py</files>
  <action>
Create `tests/integration/test_pagination_iterator.py` with session-scoped fixtures `api_key` and `org_id` (from pytestconfig, same pattern as existing tests).

Tests to implement:

1. `test_pagination_iterator_vs_legacy_networks` - Create two DashboardAPI instances: one with `use_iterator_for_get_pages=True`, one with `False`. Both call `getOrganizationNetworks(org_id, perPage=5, total_pages=-1)`. Collect results from both (iterator yields items via `for x in ...`; legacy returns list directly). Assert both produce the same set of network IDs. Use `suppress_logging=True`, `caller="PytestIntegration"`.

2. `test_pagination_iterator_yields_dicts` - With iterator mode, verify each yielded item is a dict with keys `id` and `name`.

3. `test_get_organization_api_requests` - Call `dashboard.organizations.getOrganizationApiRequests(org_id, timespan=900, total_pages=-1)`. Assert result is a list. If non-empty, assert first record has keys: `method`, `host`, `path`, `ts`, `responseCode`, `sourceIp`, `userAgent`. (List may be empty if no recent API activity besides this test itself, so only check fields if len > 0.)

Use `meraki.DashboardAPI` directly (no async). Keep `suppress_logging=True` and `maximum_retries=5` on all clients.
  </action>
  <verify>
    <automated>uv run pytest tests/integration/test_pagination_iterator.py --apikey $TEST_ORG_API_KEY --o $TEST_ORG_ID -v --timeout=120</automated>
  </verify>
  <done>All sync pagination and API requests log tests pass against live API</done>
</task>

<task type="auto">
  <name>Task 2: Async pagination iterator tests</name>
  <files>tests/integration/test_async_pagination_iterator.py</files>
  <action>
Create `tests/integration/test_async_pagination_iterator.py` with session-scoped fixtures `api_key` and `org_id`.

Tests to implement (all marked `@pytest.mark.asyncio`):

1. `test_async_pagination_iterator_vs_legacy_networks` - Create two `AsyncDashboardAPI` instances via `async with`: one with `use_iterator_for_get_pages=True`, one with `False`. Legacy mode: `for x in await dashboard.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1)`. Iterator mode: `async for x in dashboard.organizations.getOrganizationNetworks(org_id, perPage=5, total_pages=-1)`. Assert both produce the same set of network IDs.

2. `test_async_iterator_yields_dicts` - With async iterator mode, verify each item is a dict with `id` and `name` keys.

Use `suppress_logging=True`, `maximum_retries=5`, `caller="PytestIntegration"`.
  </action>
  <verify>
    <automated>uv run pytest tests/integration/test_async_pagination_iterator.py --apikey $TEST_ORG_API_KEY --o $TEST_ORG_ID -v --timeout=120</automated>
  </verify>
  <done>Async pagination iterator tests pass, confirming `async for` yields same data as `await` + list iteration</done>
</task>

<task type="auto">
  <name>Task 3: Org-wide workflow tests (sync + async)</name>
  <files>tests/integration/test_org_wide_workflows.py</files>
  <action>
Create `tests/integration/test_org_wide_workflows.py` with session-scoped fixtures `api_key` and `org_id`.

Tests to implement:

1. `test_sync_org_wide_clients_workflow` - Using `meraki.DashboardAPI`: call `getOrganizationNetworks(org_id, total_pages="all", perPage=1000)`, assert returns non-empty list. Take first network, call `dashboard.networks.getNetworkClients(network_id, timespan=86400, perPage=1000, total_pages="all")`. Assert result is a list (may be empty for some networks, that's OK). If non-empty, assert first item is a dict with key `mac`.

2. `test_async_org_wide_clients_workflow` - Using `meraki.aio.AsyncDashboardAPI` via `async with`: await `getOrganizationNetworks(org_id)`, take up to first 3 networks. Create tasks for `getNetworkClients` on each. Use `asyncio.as_completed` to collect results. Assert all results are lists. Verifies concurrent async fetching works.

Mark async test with `@pytest.mark.asyncio`. Use `suppress_logging=True`, `maximum_retries=5`, `caller="PytestIntegration"`.
  </action>
  <verify>
    <automated>uv run pytest tests/integration/test_org_wide_workflows.py --apikey $TEST_ORG_API_KEY --o $TEST_ORG_ID -v --timeout=180</automated>
  </verify>
  <done>Both sync and async org-wide multi-endpoint workflows complete without error</done>
</task>

</tasks>

<verification>
Run all new integration tests together:
```
uv run pytest tests/integration/test_pagination_iterator.py tests/integration/test_async_pagination_iterator.py tests/integration/test_org_wide_workflows.py --apikey $TEST_ORG_API_KEY --o $TEST_ORG_ID -v
```
All tests pass.
</verification>

<success_criteria>
- 7 new integration tests across 3 files
- Pagination iterator (sync): proves iterator mode == legacy mode
- Pagination iterator (async): proves `async for` == `await` + iterate
- Org-wide workflow (sync): multi-endpoint chain works
- Org-wide workflow (async): concurrent fetching via as_completed works
- API requests log: endpoint returns expected record schema
- All tests are read-only (no creates/deletes)
- Tests follow existing conftest.py patterns (--apikey, --o options)
</success_criteria>
