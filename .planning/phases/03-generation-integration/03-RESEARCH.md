# Phase 03: Generation Integration - Research

**Researched:** 2026-04-30
**Domain:** Code generation (Jinja2 templating, OpenAPI traversal, CLI orchestration)
**Confidence:** HIGH

## Summary

Phase 03 integrates the Phase 1+2 parsing functions into a new v3 generator that produces sync, async, and batch modules matching v2 output structure. The v2 generator provides complete architecture reference: entry point (main()), spec organization (common.organize_spec()), module generation loops, and Jinja2 templates.

The kwargs.update(locals()) antipattern captures all local variables including `self`, causing the runtime SDK to send unnecessary params in HTTP requests. The v3 generator must build explicit param dicts from parse_params_v3() output (already filtered by param_filters=['query', 'body', 'path']).

**Primary recommendation:** Clone v2 generator structure (generate_library.py lines 207-355), replace parse_params() calls with parse_params_v3(), and remove kwarg_line logic from templates. Batch actions are driven by x-batchable-actions array (298 entries: summary, resource, operation).

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| GEN-01 | Generator produces sync/async/batch modules matching v2 output structure | v2 generator creates meraki/api/, meraki/aio/api/, meraki/api/batch/ via generate_modules() (lines 310-355); templates in generator/*.jinja2 |
| GEN-02 | Generated methods use explicit param construction instead of kwargs.update(locals()) | v2 antipattern at lines 437, 439, 501, 665, 706; fix requires omitting kwarg_line and building params from parse_params_v3 output |
| GEN-04 | Generator handles x-batchable-actions for batch class generation | v3 spec has x-batchable-actions array (298 items: summary, resource, operation); v2 batch logic at lines 557-710 matches summaries |
| GEN-05 | CLI accepts same args as v2 and fetches v3 spec with ?version=3 param | v2 CLI: -h, -o, -k, -v, -a, -g (lines 736-796); v3 spec URL: https://api.meraki.com/api/v1/openapiSpec?version=3 |
</phase_requirements>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| OpenAPI spec traversal | Generator script | — | Generator iterates paths, groups by tag/scope (common.organize_spec) |
| Parameter parsing | parser_v3.py | — | parse_params_v3() normalizes v3 params to v2 format |
| Code generation | Jinja2 templates | — | Templates receive operation metadata and emit Python methods |
| CLI orchestration | generate_library.py | — | Entry point fetches spec, calls generate_library(), formats with ruff |
| Module structure | File system | — | Generator creates directories (meraki/api/, meraki/aio/api/, meraki/api/batch/) |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| Jinja2 | 3.1.6 | Template engine | Pinned in pyproject.toml [generator] group; v2 generator uses it for all code emission |
| requests | ≥2.33.1,<3 | HTTP client | For fetching OpenAPI spec at generator runtime (not SDK runtime) |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| ruff | ≥0.15.12 | Formatter/linter | Post-generation formatting (line 306-307 in v2 generator) |
| pytest | ≥8.3.5,<10 | Test runner | Validation architecture (existing tests in tests/generator/) |

### Alternatives Considered
| Instead of | Could Use | Tradeoff |
|------------|-----------|----------|
| Jinja2 | String formatting | Jinja2 handles escaping, indentation, control flow; string formatting is brittle |
| ruff | black + flake8 | Project already uses ruff; switching adds dependency churn |

**Installation:**
```bash
# Already in pyproject.toml [dependency-groups]
uv sync --group generator
```

**Version verification:** Verified via pyproject.toml (read during research).

## Architecture Patterns

### System Architecture Diagram

```
[CLI Entry Point (main)]
        |
        v
[Fetch OpenAPI Spec] --version=3--> [Meraki API]
        |
        v
[organize_spec()] --> Groups paths by tag/scope
        |
        v
[generate_modules() loop] --> For each scope:
        |
        +----> [Render class_template.jinja2] --> meraki/api/{scope}.py
        |
        +----> [Render async_class_template.jinja2] --> meraki/aio/api/{scope}.py
        |
        +----> [Render batch_class_template.jinja2] --> meraki/api/batch/{scope}.py
        |
        v
[generate_standard_and_async_functions()] --> For each operation:
        |
        +----> [parse_params_v3()] --> Normalized param dict
        |
        +----> [Render function_template.jinja2] --> Append to sync+async modules
        |
        v
[generate_action_batch_functions()] --> For each batchable operation:
        |
        +----> [Match against x-batchable-actions]
        |
        +----> [Render batch_function_template.jinja2] --> Append to batch module
        |
        v
[ruff format meraki/] --> Post-process generated code
```

### Component Responsibilities

| Component | File | Responsibility |
|-----------|------|----------------|
| CLI parser | generate_library.py:736-796 (main()) | Parse -h/-o/-k/-v/-a/-g, fetch spec, call generate_library() |
| Spec organizer | common.py:1-36 (organize_spec()) | Group paths by tag/scope, return operations list + scopes dict |
| Module generator | generate_library.py:310-355 (generate_modules()) | Iterate scopes, render class templates, call function generators |
| Function generator | generate_library.py:357-514 (generate_standard_and_async_functions()) | Iterate operations, call parser, render function templates |
| Batch generator | generate_library.py:557-710 (generate_action_batch_functions()) | Match summaries against x-batchable-actions, render batch templates |
| Parameter parser | parser_v3.py:226-284 (parse_params_v3()) | Normalize v3 params to v2 format for templates |

### Recommended Project Structure
```
generator/
├── generate_library_v3.py        # New v3 generator (clone of v2 structure)
├── parser_v3.py                  # Exists: resolve_ref, parse_params_v3
├── common.py                     # Reuse: organize_spec()
├── class_template.jinja2         # Reuse: sync class header
├── async_class_template.jinja2   # Reuse: async class header
├── batch_class_template.jinja2   # Reuse: batch class header
├── function_template.jinja2      # Modify: remove kwarg_line logic
├── batch_function_template.jinja2 # Modify: remove kwarg_line logic
└── async_function_template.jinja2 # Create: if needed (v2 reuses function_template)
```

### Pattern 1: Explicit Parameter Construction
**What:** Build query/body/path dicts from parse_params_v3() filtered output, avoiding locals() capture
**When to use:** All generated methods (sync, async, batch)
**Example:**
```python
# Current v2 antipattern (generate_library.py:437, 439)
kwarg_line = ""
if parse_params(operation, parameters, ["optional"]):
    kwarg_line = "kwargs.update(locals())"  # Captures self, networkId, etc.
elif parse_params(operation, parameters, ["query", "array", "body"]):
    kwarg_line = "kwargs = locals()"

# function_template.jinja2:11-13 renders:
kwargs.update(locals())

# v3 fix: remove kwarg_line entirely, templates build explicit dicts
query_params = parse_params_v3(operation, path_item, spec, ["query"])
body_params = parse_params_v3(operation, path_item, spec, ["body"])
path_params = parse_params_v3(operation, path_item, spec, ["path"])

# Template receives filtered param dicts, builds:
params = {k: kwargs[k] for k in ["networkId", "tags"] if k in kwargs}
payload = {k: kwargs[k] for k in ["name", "notes"] if k in kwargs}
```

### Pattern 2: Batch Action Matching
**What:** Match operation summary/description against x-batchable-actions array to determine batch eligibility
**When to use:** During batch function generation loop
**Example:**
```python
# Source: generate_library.py:566-576
batchable_actions = spec["x-batchable-actions"]
batchable_action_summaries = [action["summary"] for action in batchable_actions]

for path, methods in section.items():
    for method, endpoint in methods.items():
        if endpoint["description"] in batchable_action_summaries:
            this_action = [a for a in batchable_actions if a["summary"] == endpoint["description"]][0]
            batch_operation = this_action["operation"]
            # render batch_function_template.jinja2 with batch_operation
```

### Pattern 3: Pagination Injection
**What:** Detect perPage param and inject total_pages/direction params via generate_pagination_parameters()
**When to use:** Already handled by parse_params_v3() at line 277 (reuses v2 logic via import)
**Example:**
```python
# parser_v3.py:276-277
if "perPage" in params:
    params.update(generate_pagination_parameters(operation_id))

# generate_pagination_parameters() from v2 (lines 32-51):
# - Adds total_pages, direction params
# - Special-cases getNetworkEvents with event_log_end_time
```

### Anti-Patterns to Avoid
- **kwargs.update(locals()):** Captures all local vars including self, causes runtime SDK to send unnecessary params; use explicit dict comprehensions filtered by param_filters output
- **Inline $ref resolution in templates:** Templates should receive resolved schemas; parser_v3.py already resolves via resolve_ref()
- **Hardcoded batch operation names:** Derive from x-batchable-actions["operation"] field, don't infer from HTTP method

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| Template engine | String concatenation with manual escaping | Jinja2 | Handles indentation, control flow, auto-escaping; v2 generator already uses it |
| Spec traversal | Custom tree walker | OpenAPI spec dict + organize_spec() | v2 pattern works for v3; paths/operations are structurally identical |
| Code formatting | Manual indentation logic | ruff format | Handles line length, quote normalization; project already uses ruff |
| Param filtering | Custom filter logic | return_params() from v2 | Supports 'required', 'optional', 'query', 'body', 'path', 'array', 'enum' filters; reuse via import |

**Key insight:** v2 generator architecture (lines 207-710) is 90% compatible with v3. Only parsing layer (lines 378-432) needs replacement with parse_params_v3() calls. Templates need minor surgery to remove kwarg_line injection.

## Common Pitfalls

### Pitfall 1: Forgetting to Clear $ref Cache Between Generator Runs
**What goes wrong:** Stale cache entries from previous spec version leak into new generation, causing incorrect resolution
**Why it happens:** resolve_ref() uses module-level _ref_cache; multiple runs in same process accumulate cache entries
**How to avoid:** Call clear_cache() at generator entry point (main()), as documented in parser_v3.py:17-19
**Warning signs:** Generated code has params from previous spec version; test failures after spec update

### Pitfall 2: Matching Batch Actions by Description vs. Summary
**What goes wrong:** v2 generator checks both `endpoint["description"]` and `endpoint["summary"]` (lines 567-576); v3 spec may differ
**Why it happens:** Spec inconsistency; some operations have description=summary, others differ
**How to avoid:** Match against both fields (v2 line 575), or verify v3 spec structure first
**Warning signs:** 298 batchable actions in spec, but <298 batch methods generated

### Pitfall 3: Not Handling Path-Level Parameters
**What goes wrong:** v3 spec uses path-level parameters for shared params across operations (e.g., organizationId); omitting path_item causes missing params
**Why it happens:** v2 generator only checks operation.parameters (line 372); v3 needs operation + path_item
**How to avoid:** parse_params_v3() requires both operation and path_item args (parser_v3.py:226); always pass both
**Warning signs:** Path params missing from generated method signatures; URL construction fails at runtime

### Pitfall 4: Template kwarg_line Logic Assumes locals() is Safe
**What goes wrong:** v2 templates inject `kwargs.update(locals())` which captures self, metadata, resource; runtime SDK sends these as HTTP params
**Why it happens:** v2 generator assumes locals() only contains user-provided params; it doesn't filter
**How to avoid:** Remove kwarg_line from template context, build explicit param dicts from parse_params_v3() output
**Warning signs:** HTTP requests have extra params; API returns 400 for unrecognized fields

### Pitfall 5: Forgetting to Add ?version=3 to Spec URL
**What goes wrong:** Generator fetches OASv2 spec instead of OASv3, parse_params_v3() fails on v2 structure
**Why it happens:** Default endpoint returns v2 spec; v3 requires query param
**How to avoid:** Add params={"version": 3} to requests.get() call (see generate_library_oasv3.py:820)
**Warning signs:** Parser sees parameters with in="body" (v2) instead of requestBody (v3); resolve_ref() fails on missing components/schemas

## Code Examples

Verified patterns from existing codebase:

### CLI Entry Point with v3 Spec Fetch
```python
# Source: generate_library_oasv3.py:775-828
def main(inputs):
    api_key = os.environ.get("MERAKI_DASHBOARD_API_KEY")
    org_id = None
    version_number = "custom"
    is_github_action = False

    try:
        opts, args = getopt.getopt(inputs, "ho:k:v:g:")
    except getopt.GetoptError:
        print_help()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print_help()
            sys.exit(2)
        elif opt == "-o":
            org_id = arg
        elif opt == "-k" and api_key is None:
            api_key = arg
        elif opt == "-v":
            version_number = arg
        elif opt == "-g":
            if arg.lower() == "true":
                is_github_action = True

    # Retrieve latest OpenAPI specification with version=3
    if org_id:
        if not api_key:
            print_help()
            sys.exit(2)
        else:
            response = requests.get(
                f"https://api.meraki.com/api/v1/organizations/{org_id}/openapiSpec",
                headers={"Authorization": f"Bearer {api_key}"},
                params={"version": 3},
            )
            if response.ok:
                spec = response.json()
            else:
                print_help()
                sys.exit(f"API key provided does not have access to org {org_id}")
    else:
        response = requests.get(
            "https://api.meraki.com/api/v1/openapiSpec", params={"version": 3}
        )
        if response.ok:
            spec = response.json()
        else:
            print_help()
            sys.exit("Failed to retrieve OpenAPI v3 specification. Please try again.")

    generate_library(spec, version_number, is_github_action)
```

### Module Generation Loop Structure
```python
# Source: generate_library.py:310-355 (v2 reference, adapt for v3)
def generate_modules(batchable_actions, jinja_env, scopes, template_dir):
    for scope in scopes:
        print(f"...generating {scope}")
        section = scopes[scope]

        # Generate the standard module
        with open(f"meraki/api/{scope}.py", "w", encoding="utf-8", newline=None) as output:
            # Open module file for Asyncio API libraries
            async_output = open(f"meraki/aio/api/{scope}.py", "w", encoding="utf-8", newline=None)
            # Open module file for Action Batch API libraries
            batch_output = open(f"meraki/api/batch/{scope}.py", "w", encoding="utf-8", newline=None)

            modules = [
                {"template_name": "class_template.jinja2", "module_output": output},
                {"template_name": "async_class_template.jinja2", "module_output": async_output},
                {"template_name": "batch_class_template.jinja2", "module_output": batch_output},
            ]

            # Generate modules
            for module in modules:
                render_class_template(
                    jinja_env,
                    template_dir,
                    module["template_name"],
                    module["module_output"],
                    scope,
                )

            # Generate API & Asyncio API functions
            generate_standard_and_async_functions(jinja_env, template_dir, section, output, async_output)

            # Generate API action batch functions
            generate_action_batch_functions(
                jinja_env,
                template_dir,
                section,
                batch_output,
                batchable_actions,
            )
```

### Explicit Parameter Construction (v3 Fix)
```python
# v2 antipattern (generate_library.py:436-440)
kwarg_line = ""
if parse_params(operation, parameters, ["optional"]):
    kwarg_line = "kwargs.update(locals())"
elif parse_params(operation, parameters, ["query", "array", "body"]):
    kwarg_line = "kwargs = locals()"

# v3 fix (pseudo-code for new generator):
# Don't pass kwarg_line to template at all
# Template builds explicit dicts:

# In template (function_template.jinja2 modified):
{% if query_params|length > 0 %}
query_params_list = [{% for param in query_params %}"{{ param }}", {% endfor %}]
params = {k: kwargs[k] for k in query_params_list if k in kwargs}
{% endif %}

{% if body_params|length > 0 %}
body_params_list = [{% for param in body_params %}"{{ param }}", {% endfor %}]
payload = {k: kwargs[k] for k in body_params_list if k in kwargs}
{% endif %}
```

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| kwargs.update(locals()) | Explicit param dicts from parser output | Phase 3 (this phase) | Removes self/metadata from HTTP requests; fixes unnecessary param warnings |
| Inline $ref resolution in generator loop | resolve_ref() with caching at parse time | Phase 1 (2026-04-29) | Templates receive normalized dicts; no $ref handling needed in generation logic |
| parameters only | parameters + requestBody | OASv3 (spec change) | Body params no longer have in="body" in parameters array; separate requestBody object |
| Single kwargs dict | Separate query_params/body_params/path_params dicts | Phase 3 (this phase) | Templates can validate/filter by param location; clearer template logic |

**Deprecated/outdated:**
- generate_library_oasv3.py: Abandoned monolithic attempt (lines 262-765 inline everything); v3 generator should reuse common.py and parser_v3.py modular functions
- v2 parse_params() function (generate_library.py:198-204): Doesn't handle requestBody or path-level params; use parse_params_v3() instead

## Open Questions

1. **Should async functions reuse function_template.jinja2 or need separate template?**
   - What we know: v2 generator reuses function_template.jinja2 for both sync and async (lines 474-513)
   - What's unclear: Whether async-specific patterns (e.g., await) need template changes
   - Recommendation: Start with reuse (v2 pattern works); create async_function_template.jinja2 only if differences emerge

2. **How to verify 298 batch actions generated correctly?**
   - What we know: x-batchable-actions has 298 entries; v2 matches by summary/description
   - What's unclear: Whether v3 spec summary/description fields align with action entries
   - Recommendation: Add assertion in generator: generated_count == len(x-batchable-actions), fail if mismatch

3. **Should generator accept -a (api_version_number) for v3?**
   - What we know: v2 generator uses -a to set __api_version__ in __init__.py (lines 759, 282-286)
   - What's unclear: Whether v3 spec version should be separate from v2 API version
   - Recommendation: Keep -a flag for backward compatibility; default to "3" if not provided

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| Python | Generator runtime | ✓ | 3.11+ | — |
| pytest | Validation | ✓ | 9.0.3 | — |
| Jinja2 | Template rendering | ✓ (via pyproject.toml) | 3.1.6 | — |
| ruff | Code formatting | ✓ (via pyproject.toml) | ≥0.15.12 | — |
| requests | Spec fetching | ✓ (via pyproject.toml) | ≥2.33.1 | — |

**Missing dependencies with no fallback:** None

**Missing dependencies with fallback:** None

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | pytest 9.0.3 |
| Config file | pyproject.toml [tool.pytest.ini_options] |
| Quick run command | `pytest tests/generator/test_parser_v3.py -x` |
| Full suite command | `pytest tests/generator/ -x` |

### Phase Requirements → Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| GEN-01 | Generator produces sync/async/batch modules matching v2 structure | golden-file | `pytest tests/generator/test_generate_library_golden.py -x` | ✅ (structure exists, needs v3 variant) |
| GEN-02 | Generated methods use explicit param construction | golden-file | `pytest tests/generator/test_generate_library_golden.py::test_no_kwargs_update_locals -x` | ❌ Wave 0 |
| GEN-04 | Generator handles x-batchable-actions for batch class generation | unit | `pytest tests/generator/test_generate_library_v3.py::test_batch_action_count -x` | ❌ Wave 0 |
| GEN-05 | CLI accepts same args and fetches v3 spec | integration | `python generator/generate_library_v3.py -h` (manual check) | ❌ Wave 0 |

### Sampling Rate
- **Per task commit:** `pytest tests/generator/test_generate_library_v3.py -x` (new v3-specific tests)
- **Per wave merge:** `pytest tests/generator/ -x` (full generator test suite)
- **Phase gate:** Full suite green + manual spot-check of generated code structure before `/gsd-verify-work`

### Wave 0 Gaps
- [ ] `tests/generator/test_generate_library_v3.py` — covers GEN-02 (no locals()), GEN-04 (298 batch actions)
- [ ] `tests/generator/fixtures/v3_spec_minimal.json` — minimal v3 spec for fast unit tests
- [ ] Framework already installed (pytest 9.0.3)

## Sources

### Primary (HIGH confidence)
- generate_library.py (v2 generator architecture, lines 207-710, 736-796)
- generate_library_oasv3.py (abandoned v3 attempt, reference for spec fetch pattern line 820)
- parser_v3.py (parse_params_v3(), resolve_ref(), parse_request_body())
- common.py (organize_spec())
- function_template.jinja2, batch_function_template.jinja2, class_template.jinja2 (existing templates)
- pyproject.toml (test framework config, dependency versions)
- Meraki API live spec (x-batchable-actions structure verified via curl)

### Secondary (MEDIUM confidence)
- tests/generator/test_parser_v3.py (validation patterns for parse_params_v3 output)
- synthetic_v3_spec.json (test fixture structure for v3-specific features)

### Tertiary (LOW confidence)
- None (all findings verified against existing codebase or live API spec)

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH - Jinja2 version pinned in pyproject.toml, v2 generator imports verified
- Architecture: HIGH - Full v2 generator code read, structure maps directly to v3 needs
- Pitfalls: HIGH - Antipatterns identified in v2 code (kwargs.update(locals()) lines 437, 439, 501, 665), confirmed in generated code grep
- Batch actions: HIGH - Live v3 spec curl confirmed 298 entries with summary/resource/operation structure

**Research date:** 2026-04-30
**Valid until:** 2026-05-30 (stable domain; Jinja2/pytest APIs unlikely to change; v3 spec structure locked by Meraki)
