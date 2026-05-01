# Phase 8: Integration Baseline - Research

**Researched:** 2026-05-01
**Domain:** pytest reporting, integration test infrastructure
**Confidence:** HIGH

## Summary

Phase 8 captures a machine-readable pass/fail baseline of all integration tests before any HTTP transport changes. The test infrastructure already exists (5 files, conftest with CLI options). The work is: install pytest-json-report, fix the stale FILE_ORDER in conftest, run the suite against Meraki sandbox, and store the JSON artifact.

pytest-json-report 1.5.0 (last released 2022) resolves cleanly with pytest 9.x and provides per-test duration, outcome, and stage breakdown. Its dependency pytest-metadata is also compatible.

**Primary recommendation:** Add pytest-json-report + pytest-metadata to dev deps, fix conftest FILE_ORDER, run `pytest tests/integration/ --json-report --json-report-file=tests/integration/baseline/report.json`, commit the artifact.

<user_constraints>
## User Constraints (from CONTEXT.md)

### Locked Decisions
- D-01: Use pytest-json-report to produce machine-readable pass/fail per test
- D-02: Include timing data (test durations) for Phase 13 performance comparison
- D-03: Store report in `tests/integration/baseline/` (survives .planning/ cleanup, easy Phase 13 reference)
- D-04: Run only `tests/integration/` (5 files: CRUD lifecycle sync/async, org-wide workflows, iterators sync/async)
- D-05: Update `conftest.py` FILE_ORDER to match actual filenames on disk (currently references non-existent pagination files)
- D-06: Document current pass/fail state as-is (known failures tagged, not fixed)
- D-07: Regression gate for Phase 13 = "same or better" (no new failures allowed, new passes OK)

### Claude's Discretion
- Exact pytest-json-report flags and output filename
- Whether to add a README in the baseline directory explaining the artifact
- How to tag known failures in the report (markers vs separate list)

### Deferred Ideas (OUT OF SCOPE)
None.
</user_constraints>

<phase_requirements>
## Phase Requirements

| ID | Description | Research Support |
|----|-------------|------------------|
| TEST-01 | Integration test baseline captured before any HTTP changes | pytest-json-report produces JSON with per-test pass/fail + durations; stored in tests/integration/baseline/ |
</phase_requirements>

## Architectural Responsibility Map

| Capability | Primary Tier | Secondary Tier | Rationale |
|------------|-------------|----------------|-----------|
| Test execution | CLI / pytest runner | - | pytest collects and runs tests |
| Report generation | pytest plugin (pytest-json-report) | - | Plugin hooks into pytest session |
| Baseline storage | Filesystem (git-tracked artifact) | - | JSON file committed to repo |
| Regression comparison | Phase 13 tooling (future) | - | Consumes the baseline artifact |

## Standard Stack

### Core
| Library | Version | Purpose | Why Standard |
|---------|---------|---------|--------------|
| pytest-json-report | 1.5.0 | Machine-readable test report | User decision D-01; produces per-test JSON with durations [VERIFIED: pypi.org] |
| pytest-metadata | 3.1.1 | Required dependency of pytest-json-report | Auto-installed; provides environment metadata [VERIFIED: uv dry-run] |

### Supporting
| Library | Version | Purpose | When to Use |
|---------|---------|---------|-------------|
| pytest | 9.0.3 | Test runner (already installed) | Always [VERIFIED: uv run] |
| pytest-asyncio | installed | Async test support | Used by async CRUD and iterator tests [VERIFIED: pyproject.toml] |

**Installation:**
```bash
uv add --group dev pytest-json-report
```

**Version verification:** pytest-json-report 1.5.0 is the latest on PyPI (released 2022-03-15). It resolves cleanly with pytest 9.x per uv dry-run. [VERIFIED: uv pip install --dry-run]

## Architecture Patterns

### System Architecture Diagram

```
[User runs pytest CLI with --apikey and --o]
         |
         v
[pytest collects tests/integration/ (5 files)]
         |
         v
[conftest.py: FILE_ORDER sorts execution, fixtures provide api_key/org_id]
         |
         v
[Tests call Meraki Dashboard API (real sandbox)]
         |
         v
[pytest-json-report hooks capture outcome + duration per test]
         |
         v
[JSON report written to tests/integration/baseline/report.json]
         |
         v
[Phase 13 reads baseline for regression comparison]
```

### Recommended Project Structure
```
tests/
  integration/
    conftest.py              # FILE_ORDER, fixtures, CLI options
    test_client_crud_lifecycle_sync.py
    test_client_crud_lifecycle_async.py
    test_org_wide_workflows.py
    test_iterator_sync.py
    test_iterator_async.py
    baseline/
      report.json            # pytest-json-report output (committed)
      README.md              # Explains the artifact (optional)
```

### Pattern 1: pytest-json-report invocation
**What:** Generate JSON report with timing data
**When to use:** Capturing baseline
**Example:**
```bash
# Source: https://github.com/numirias/pytest-json-report README
pytest tests/integration/ \
  --apikey=$MERAKI_API_KEY \
  --o=$MERAKI_ORG_ID \
  --json-report \
  --json-report-file=tests/integration/baseline/report.json \
  --json-report-indent=2 \
  --json-report-omit=collectors,log,streams
```
[VERIFIED: pytest-json-report README on GitHub]

### Pattern 2: JSON report structure
**What:** The output schema
**When to use:** Understanding what Phase 13 will consume
**Example:**
```json
{
  "created": 1714567890.123,
  "duration": 145.67,
  "exitcode": 0,
  "root": "/path/to/project",
  "environment": { "Python": "3.11.x", "Platform": "..." },
  "summary": { "passed": 25, "failed": 2, "total": 27 },
  "tests": [
    {
      "nodeid": "tests/integration/test_client_crud_lifecycle_sync.py::test_get_organizations",
      "outcome": "passed",
      "setup": { "duration": 0.001, "outcome": "passed" },
      "call": { "duration": 1.234, "outcome": "passed" },
      "teardown": { "duration": 0.0, "outcome": "passed" }
    }
  ]
}
```
[VERIFIED: pytest-json-report README on GitHub]

### Pattern 3: conftest FILE_ORDER fix
**What:** Update stale references to match actual filenames
**When to use:** Before running baseline (ensures correct execution order)
**Example:**
```python
FILE_ORDER = [
    "test_client_crud_lifecycle_sync.py",
    "test_client_crud_lifecycle_async.py",
    "test_org_wide_workflows.py",
    "test_iterator_sync.py",       # was: test_pagination_iterator_policy_objects_sync.py
    "test_iterator_async.py",      # was: test_pagination_iterator_policy_objects_async.py
]
```
[VERIFIED: ls tests/integration/test_*.py vs conftest.py contents]

### Anti-Patterns to Avoid
- **Running baseline with --exitfirst/-x:** Would stop at first failure, missing the full picture
- **Fixing failures in this phase:** D-06 says document as-is, don't fix
- **Omitting duration data from report:** D-02 requires it for Phase 13 perf comparison

## Don't Hand-Roll

| Problem | Don't Build | Use Instead | Why |
|---------|-------------|-------------|-----|
| JSON test output | Custom pytest plugin / conftest hook | pytest-json-report | Already handles all stages, durations, metadata; D-01 locks this |
| Test ordering | Manual test naming conventions | conftest FILE_ORDER | Already exists, just needs filename fix |

## Common Pitfalls

### Pitfall 1: Stale FILE_ORDER causes test_iterator files to sort last randomly
**What goes wrong:** Tests not in FILE_ORDER fall to index `len(FILE_ORDER)` and sort arbitrarily
**Why it happens:** Files were renamed but conftest wasn't updated
**How to avoid:** Fix FILE_ORDER before running baseline (D-05)
**Warning signs:** Iterator tests run in wrong order; batch cleanup from one test interferes with another

### Pitfall 2: pytest-json-report report.json not committed
**What goes wrong:** Baseline lost, Phase 13 has nothing to compare against
**Why it happens:** .gitignore or developer forgetting to commit
**How to avoid:** Explicitly `git add tests/integration/baseline/report.json`
**Warning signs:** File exists locally but not in repo

### Pitfall 3: Tests require API key but none provided
**What goes wrong:** All tests skip or error with empty string API key
**Why it happens:** --apikey not passed on CLI
**How to avoid:** Document exact command with env var substitution
**Warning signs:** Zero actual assertions, all tests "passed" trivially (they don't; they'll error on API call)

### Pitfall 4: Iterator tests are slow (create 100 policy objects)
**What goes wrong:** User thinks tests are hung
**Why it happens:** Each iterator test creates 100 objects via action batches, polls for completion
**How to avoid:** Expect ~5-10 min runtime for iterator tests; use -v for progress visibility
**Warning signs:** No output for extended period during iterator tests

### Pitfall 5: pytest-json-report omits keyword field needed later
**What goes wrong:** Report too large or missing needed fields
**Why it happens:** Default includes everything (collectors, logs, streams add bulk)
**How to avoid:** Use `--json-report-omit=collectors,log,streams` to keep report lean while preserving keywords/markers
**Warning signs:** Report file is megabytes instead of kilobytes

## Code Examples

### Running the baseline capture
```bash
# Source: project integration test conventions + pytest-json-report docs
pytest tests/integration/ \
  --apikey="$MERAKI_DASHBOARD_API_KEY" \
  --o="$MERAKI_ORG_ID" \
  -v \
  --json-report \
  --json-report-file=tests/integration/baseline/report.json \
  --json-report-indent=2 \
  --json-report-omit=collectors,log,streams,keywords
```

### Tagging known failures (post-run analysis)
```python
# Script or manual: read report.json, extract failures as known_failures list
import json

with open("tests/integration/baseline/report.json") as f:
    report = json.load(f)

known_failures = [
    t["nodeid"] for t in report["tests"] if t["outcome"] == "failed"
]
# Write to separate file or embed as metadata
```

## Endpoints Exercised by Integration Tests

| Endpoint | Test File | Method |
|----------|-----------|--------|
| getAdministeredIdentitiesMe | crud_sync, crud_async | GET |
| getOrganizations | crud_sync, crud_async | GET |
| getOrganization | crud_sync, crud_async | GET |
| createOrganizationNetwork | crud_sync, crud_async | POST |
| getOrganizationNetworks | crud_sync, crud_async, org_wide | GET |
| updateNetwork | crud_sync, crud_async | PUT |
| createOrganizationPolicyObject | crud_sync, crud_async, iter_sync, iter_async | POST |
| getOrganizationPolicyObjects | crud_sync, crud_async, iter_sync, iter_async | GET (paginated) |
| deleteOrganizationPolicyObject | crud_sync, crud_async, iter_sync, iter_async | DELETE |
| getNetworkApplianceFirewallL3FirewallRules | crud_sync, crud_async | GET |
| updateNetworkApplianceFirewallL3FirewallRules | crud_sync, crud_async | PUT |
| updateNetworkApplianceVlansSettings | crud_sync, crud_async | PUT |
| createNetworkApplianceVlan | crud_sync, crud_async | POST |
| createOrganizationActionBatch | crud_sync, crud_async, iter_sync, iter_async | POST |
| updateOrganizationActionBatch | crud_sync, crud_async | PUT |
| getOrganizationActionBatch | crud_sync, crud_async, iter_sync, iter_async | GET |
| getOrganizationActionBatches | iter_sync, iter_async | GET |
| deleteOrganizationActionBatch | iter_sync, iter_async | DELETE |
| getNetworkClients | org_wide | GET (paginated) |

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
|--------------|------------------|--------------|--------|
| pytest --junitxml | pytest-json-report | 2020+ | JSON is easier to parse programmatically than XML |
| Manual test logs | Structured JSON with durations | - | Enables automated regression gate in Phase 13 |

**Note on pytest-json-report maintenance:** Last release 2022-03-15. Not actively maintained, but the hook interface it uses (pytest_runtest_makereport) is stable across pytest versions. It resolved cleanly with pytest 9.x in this project. [VERIFIED: uv dry-run resolution]

## Assumptions Log

| # | Claim | Section | Risk if Wrong |
|---|-------|---------|---------------|
| A1 | pytest-json-report 1.5.0 works correctly at runtime with pytest 9.x (only dry-run verified, not actually executed) | Standard Stack | Low; could fall back to junitxml + custom JSON converter |
| A2 | Iterator tests take 5-10 min due to 100 object creation/deletion | Common Pitfalls | Low; just affects user expectations, not correctness |

## Open Questions

1. **Meraki sandbox API key availability**
   - What we know: Tests require `--apikey` and `--o` CLI options
   - What's unclear: Whether the user has valid sandbox credentials ready
   - Recommendation: Plan should document the exact env vars expected; execution is manual (user provides key)

2. **Known failure count**
   - What we know: D-06 says document failures as-is
   - What's unclear: Whether any tests currently fail (can't know until run against sandbox)
   - Recommendation: Plan should include a post-run step to extract and document known failures

## Environment Availability

| Dependency | Required By | Available | Version | Fallback |
|------------|------------|-----------|---------|----------|
| pytest | Test runner | Yes | 9.0.3 | - |
| pytest-asyncio | Async tests | Yes | installed | - |
| pytest-json-report | Report generation (D-01) | No (not installed) | 1.5.0 target | Install via uv add |
| Meraki sandbox API key | All integration tests | Unknown | - | User must provide |
| Network connectivity | API calls | Required | - | Cannot run offline |

**Missing dependencies with no fallback:**
- Meraki sandbox API key (user must provide at runtime)

**Missing dependencies with fallback:**
- pytest-json-report (install step required; trivial)

## Validation Architecture

### Test Framework
| Property | Value |
|----------|-------|
| Framework | pytest 9.0.3 |
| Config file | pyproject.toml `[tool.pytest.ini_options]` |
| Quick run command | `pytest tests/integration/ --apikey=KEY --o=ORG -x` |
| Full suite command | `pytest tests/integration/ --apikey=KEY --o=ORG --json-report --json-report-file=tests/integration/baseline/report.json` |

### Phase Requirements to Test Map
| Req ID | Behavior | Test Type | Automated Command | File Exists? |
|--------|----------|-----------|-------------------|-------------|
| TEST-01 | Baseline captured with pass/fail + timing | manual-only | User runs full suite against sandbox | N/A (this phase IS the test run) |

### Sampling Rate
- **Per task commit:** Verify report.json is valid JSON with expected structure
- **Per wave merge:** N/A (single execution phase)
- **Phase gate:** report.json exists, contains `tests` array, contains `duration` fields

### Wave 0 Gaps
- [ ] `pytest-json-report` package not installed (add to dev deps)
- [ ] `tests/integration/baseline/` directory does not exist (create it)
- [ ] conftest.py FILE_ORDER references wrong filenames (fix before run)

## Sources

### Primary (HIGH confidence)
- pytest-json-report PyPI page: version 1.5.0, deps [VERIFIED: pypi.org/pypi/pytest-json-report/json]
- pytest-json-report GitHub README: CLI flags, output schema [VERIFIED: raw.githubusercontent.com]
- Project source: conftest.py, all 5 integration test files [VERIFIED: local filesystem]
- uv dry-run: package resolves with pytest 9.x [VERIFIED: uv pip install --dry-run]

### Secondary (MEDIUM confidence)
- pytest-json-report maintenance status (15 open issues, last release 2022) [VERIFIED: GitHub repo page]

## Metadata

**Confidence breakdown:**
- Standard stack: HIGH (user decision locks pytest-json-report; verified it resolves)
- Architecture: HIGH (test files exist, structure is clear, pattern is straightforward)
- Pitfalls: HIGH (verified FILE_ORDER mismatch; common pytest usage patterns)

**Research date:** 2026-05-01
**Valid until:** 2026-06-01 (stable domain; pytest plugin ecosystem moves slowly)
