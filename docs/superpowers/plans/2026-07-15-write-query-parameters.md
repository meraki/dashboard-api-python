# Write-operation Query Parameters Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Preserve OpenAPI query parameters on generated POST, PUT, and PATCH methods, including action-batch methods.

**Architecture:** The generator will collect query parameters independently of the HTTP method. Standard and asynchronous methods will pass them through trailing-compatible session helper arguments; batch methods will encode them into the action resource with the already-installed `httpx` dependency.

**Tech Stack:** Python 3.11+, Jinja2, httpx, pytest

## Global Constraints

- Add exactly one regression test.
- Cover standard, asynchronous, and action-batch generation.
- Do not add endpoint-specific exceptions or regenerate generated API modules.
- Do not add a dependency or perform unrelated refactoring.

---

### Task 1: Generate and transport query parameters on write operations

**Files:**
- Modify: `tests/generator/test_generator_audit.py`
- Modify: `generator/generate_library.py`
- Modify: `generator/batch_function_template.jinja2`
- Modify: `generator/batch_class_template.jinja2`
- Modify: `meraki/session/sync.py`
- Modify: `meraki/session/async_.py`

**Interfaces:**
- Consumes: OpenAPI parameters where `in == "query"`, existing Jinja templates, and existing `SessionBase.request(..., **kwargs)` support for `params`.
- Produces: `RestSession.post/put/patch(metadata, url, json=None, params=None)`, matching async signatures, generated write calls using `params=params`, and batch action resources containing the encoded query string.

- [ ] **Step 1: Add the single failing regression test**

Append this synthetic spec and test before the module's `if __name__ == "__main__"` block in `tests/generator/test_generator_audit.py`:

```python
def _write_query_spec():
    return {
        "paths": {
            "/things": {
                "post": {
                    "operationId": "claimThings",
                    "tags": ["organizations"],
                    "summary": "Claim things",
                    "parameters": [
                        {
                            "name": "validate",
                            "in": "query",
                            "required": False,
                            "schema": {"type": "boolean"},
                        }
                    ],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "required": ["name"],
                                    "properties": {
                                        "name": {"type": "string", "description": "Thing name"}
                                    },
                                }
                            }
                        }
                    },
                }
            }
        }
    }


def test_write_operations_generate_query_params_for_all_clients():
    clear_cache()
    spec = _write_query_spec()
    section = {"/things": {"post": spec["paths"]["/things"]["post"]}}
    output = io.StringIO()
    async_output = io.StringIO()
    batch_output = io.StringIO()

    generate_library.generate_standard_and_async_functions(
        _jinja_env(), TEMPLATE_DIR, section, output, async_output, spec
    )
    generate_library.generate_action_batch_functions(
        _jinja_env(),
        TEMPLATE_DIR,
        section,
        batch_output,
        [{"summary": "Claim things", "operation": "create"}],
        spec,
    )

    for rendered in (output.getvalue(), async_output.getvalue()):
        assert 'query_params = ["validate", ]' in rendered
        assert "self._session.post(metadata, resource, payload, params=params)" in rendered

    batch_rendered = batch_output.getvalue()
    assert 'query_params = ["validate", ]' in batch_rendered
    assert 'resource += f"?{httpx.QueryParams(params)}"' in batch_rendered
```

- [ ] **Step 2: Run the regression test and verify RED**

Run:

```powershell
uv run pytest tests/generator/test_generator_audit.py::test_write_operations_generate_query_params_for_all_clients -q
```

Expected: FAIL because generated POST methods do not define query parameters or pass `params`, and batch resources do not contain a query string.

- [ ] **Step 3: Collect query parameters for all generated methods**

In `generate_standard_and_async_functions`, initialize query parameters before method dispatch and restrict array handling to query arrays:

```python
query_params = return_params(operation, all_params, ["query"])
array_params = {k: v for k, v in query_params.items() if v["type"] == "array"}
body_params = path_params = {}
```

Leave each method branch responsible only for `body_params` and `path_params`. For POST, PUT, and PATCH, build the call without changing body-only output:

```python
args = "metadata, resource"
if body_params:
    args += ", payload"
if query_params:
    args += ", params=params"
call_line = f"return self._session.{method}({args})"
```

Apply the same query and query-array initialization in `generate_action_batch_functions` before its method-specific body handling.

- [ ] **Step 4: Encode batch query parameters in the resource**

Add the existing runtime dependency to `generator/batch_class_template.jinja2`:

```python
import urllib

import httpx
```

After query-array normalization in `generator/batch_function_template.jinja2`, append query parameters to the batch resource:

```jinja2
{% if query_params|length > 0 %}
resource += f"?{httpx.QueryParams(params)}"

{% endif %}
```

- [ ] **Step 5: Pass query parameters through synchronous session helpers**

Change POST, PUT, and PATCH in `meraki/session/sync.py` without breaking existing positional JSON callers:

```python
def post(self, metadata, url, json=None, params=None):
    metadata["method"] = "POST"
    metadata["url"] = url
    metadata["params"] = params
    metadata["json"] = json
    response = self.request(metadata, "POST", url, params=params, json=json)
```

Apply the same trailing `params=None`, metadata assignment, and request keyword to `put` and `patch`.

- [ ] **Step 6: Pass query parameters through asynchronous session helpers**

Make the equivalent changes in `meraki/session/async_.py`:

```python
async def post(self, metadata, url, json=None, params=None):
    metadata["method"] = "POST"
    metadata["url"] = url
    metadata["params"] = params
    metadata["json"] = json
    response = await self.request(metadata, "POST", url, params=params, json=json)
```

Apply the same trailing argument and propagation to async `put` and `patch`.

- [ ] **Step 7: Run focused tests and verify GREEN**

Run:

```powershell
uv run pytest tests/generator/test_generator_audit.py tests/unit/test_rest_session.py tests/unit/test_aio_rest_session.py -q
```

Expected: all tests pass.

- [ ] **Step 8: Run formatting and the full test suite**

Run:

```powershell
uv run ruff format --check generator meraki tests
uv run ruff check generator meraki tests
uv run pytest -q
```

Expected: all commands exit 0 with no formatting, lint, or test failures.

- [ ] **Step 9: Review and commit**

Run:

```powershell
git diff --check
git diff --stat
git add generator/generate_library.py generator/batch_function_template.jinja2 generator/batch_class_template.jinja2 meraki/session/sync.py meraki/session/async_.py tests/generator/test_generator_audit.py docs/superpowers/plans/2026-07-15-write-query-parameters.md
git commit -m "fix: preserve query params on write operations"
```

Expected: one implementation commit containing the generator, runtime transport, regression test, and plan.
