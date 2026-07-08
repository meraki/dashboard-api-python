# httpx → main Final Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Merge the httpx-based transport rewrite (branch `origin/httpx`) into `main`, making main's tree exactly httpx while preserving both branches' commit history, then regenerate the API surface to GA.

**Architecture:** A no-fast-forward merge records httpx as a second parent (preserving both histories in the DAG), then `git read-tree --reset` forces the working tree to be byte-identical to httpx (no 155-file conflict resolution). The one genuinely main-only feature not already on httpx (X-Request-Id-on-5xx) is replayed via cherry-pick. The generated `meraki/api` code and version strings arrive as beta throwaway and are regenerated to GA by the maintainer.

**Tech Stack:** git (merge, read-tree, cherry-pick), Python 3, uv, pytest, ruff.

## Global Constraints

- Base branch for the PR: `main`. Work branch: `migrate/httpx`.
- httpx tip = `origin/httpx` (`6b20c2a`). main tip = `ec91975`. Merge base = `6d3dd19`.
- Tree after merge MUST equal `origin/httpx` byte-for-byte (verified via `git diff --stat origin/httpx` = empty).
- Both parent histories MUST remain reachable (merge commit has exactly 2 parents).
- Do NOT hand-port app-id/bearer or delete()-params — both already exist on httpx tip.
- Do NOT cherry-pick dangling `6c8bf68` — it is a duplicate of httpx tip's app-id/bearer feature.
- The maintainer regenerates `meraki/api`, `meraki/aio/api`, and version strings AFTER the merge — the plan does not touch generated code or versions.
- Pre-existing stashes `stash@{0}` / `stash@{1}` on main are the maintainer's — do not pop or drop them.

---

### Task 1: Create migration branch and history-preserving merge

**Files:**
- No file edits; git plumbing only. Result: `migrate/httpx` branch with a 2-parent merge commit whose tree == `origin/httpx`.

**Interfaces:**
- Consumes: `main` (current), `origin/httpx` (fetched).
- Produces: branch `migrate/httpx` at a merge commit `M` with parents `[main_tip, origin/httpx_tip]` and tree identical to `origin/httpx`.

- [ ] **Step 1: Fetch and confirm clean starting state**

```bash
cd "c:/Users/jkuchta/Work/_Repos/meraki/dashboard-api-python"
git fetch origin
git checkout main
git status --short          # expect: empty (stashes are fine, not shown here)
git rev-parse --short main origin/httpx
```
Expected: working tree clean; `main` = `ec91975...`, `origin/httpx` = `6b20c2a...`.

- [ ] **Step 2: Create the migration branch**

```bash
git checkout -b migrate/httpx main
```
Expected: `Switched to a new branch 'migrate/httpx'`.

- [ ] **Step 3: Start the merge without committing**

```bash
git merge --no-commit --no-ff origin/httpx
```
Expected: reports conflicts (155 files). This is expected and ignored — the next step overwrites the tree wholesale. Do NOT resolve conflicts by hand.

- [ ] **Step 4: Force index + working tree to exactly httpx**

```bash
git read-tree -u --reset origin/httpx
```
Expected: no output. Index and working tree now match `origin/httpx` byte-for-byte; merge is still in progress (MERGE_HEAD set).

- [ ] **Step 5: Verify tree equals httpx before committing**

```bash
git diff --stat origin/httpx        # expect: EMPTY (identical trees)
git diff --stat --cached origin/httpx   # expect: EMPTY
```
Expected: both empty. If not empty, STOP — do not commit; investigate.

- [ ] **Step 6: Commit the merge**

```bash
git commit --no-edit
```
Expected: a merge commit is created.

- [ ] **Step 7: Verify 2-parent merge and history preservation**

```bash
git log -1 --format='%h parents: %p'                 # expect 2 parent hashes
git rev-parse --short 'HEAD^1' 'HEAD^2'               # expect ec91975 (main), 6b20c2a (httpx)
git merge-base --is-ancestor ec91975 HEAD && echo "MAIN HISTORY PRESERVED"
git merge-base --is-ancestor 6b20c2a HEAD && echo "HTTPX HISTORY PRESERVED"
git rev-list --count origin/httpx..HEAD^1            # expect 83 (main-only commits reachable)
```
Expected: 2 parents (main tip + httpx tip), both "PRESERVED" lines print, count = 83.

- [ ] **Step 8: No commit here** — the merge commit from Step 6 is the deliverable. Proceed to Task 2.

---

### Task 2: Replay X-Request-Id-on-5xx (the one missing feature)

**Files:**
- Modify (via cherry-pick `18e47b1`): `meraki/session/base.py`, `meraki/session/async_.py`
- Test (via cherry-pick): `tests/unit/test_rest_session.py`, `tests/unit/test_aio_rest_session.py`, `tests/unit/conftest.py`
- Add (via cherry-pick): `changelog.d/+log-x-request-id-on-5xx.added.md`

**Interfaces:**
- Consumes: merge commit from Task 1 (httpx `session/` layout).
- Produces: X-Request-Id logging on 5xx responses in both sync and async sessions, with unit tests. `18e47b1` was built on an older base (`5da8e29`), so a conflict in `base.py`/`async_.py` is possible.

- [ ] **Step 1: Confirm the feature is genuinely absent at the merge tip**

```bash
git show HEAD:meraki/session/base.py | grep -niE "x-request-id|request_id|requestId" || echo "ABSENT — cherry-pick needed"
```
Expected: "ABSENT — cherry-pick needed".

- [ ] **Step 2: Cherry-pick the feature commit**

```bash
git cherry-pick 18e47b1
```
Expected: either clean success, OR a conflict in `meraki/session/base.py` / `meraki/session/async_.py`.

- [ ] **Step 3: If conflict — resolve**

Open each conflicted file. The intent: on a 5xx response, read the `X-Request-Id` response header and include it in the error log line. Keep httpx's surrounding code (its `session/base.py` structure), inserting only the request-id logging from the incoming patch. After resolving:

```bash
git add meraki/session/base.py meraki/session/async_.py
git cherry-pick --continue
```
Expected: cherry-pick completes. If the changelog/test files also conflict, take the incoming (`--theirs`) version for the new changelog fragment and merge test additions.

- [ ] **Step 4: Run the cherry-picked tests to verify they pass**

```bash
uv run pytest tests/unit/test_rest_session.py tests/unit/test_aio_rest_session.py -v -k "request_id or requestId or 5xx or request_id_log" 2>&1 | tail -30
```
Expected: the X-Request-Id tests from `18e47b1` PASS. If the `-k` filter matches nothing, run the two files in full and confirm the request-id tests are present and green.

- [ ] **Step 5: No separate commit** — `git cherry-pick` already created the commit. Proceed to Task 3.

---

### Task 3: Full verification before handoff

**Files:**
- No edits. Verification only.

**Interfaces:**
- Consumes: `migrate/httpx` after Tasks 1-2.
- Produces: evidence the merged tree imports and the httpx test suite passes on top of the merge. (Generated `meraki/api` is still beta here — regeneration is the maintainer's step, done after this plan.)

- [ ] **Step 1: Sync dependencies to the merged lockfile**

```bash
uv sync
```
Expected: environment resolves against httpx's `uv.lock` (httpx, not requests). No errors.

- [ ] **Step 2: Import smoke test (transport swap sanity)**

```bash
uv run python -c "import meraki; d = meraki.DashboardAPI.__init__; print('sync import OK'); import meraki.aio; print('async import OK')"
```
Expected: both "OK" lines print, no ImportError/ModuleNotFoundError referencing `rest_session`.

- [ ] **Step 3: Run the unit + session test suite**

```bash
uv run pytest tests/unit -q 2>&1 | tail -30
```
Expected: all pass. These are httpx's own tests plus the cherry-picked request-id tests.

- [ ] **Step 4: Run generator tests**

```bash
uv run pytest tests/generator -q 2>&1 | tail -20
```
Expected: pass (validates the httpx generator/scaffolding landed intact).

- [ ] **Step 5: Lint**

```bash
uv run ruff check meraki tests 2>&1 | tail -20
```
Expected: clean, or only pre-existing httpx-branch findings (compare against `git show origin/httpx` if unsure).

- [ ] **Step 6: Record verification result**

If any step fails, STOP and report which — do not open the PR. If all pass, the branch is ready for the maintainer's regeneration step and PR.

---

### Task 4: Handoff for regeneration + PR (maintainer-owned)

**Files:**
- Maintainer regenerates: `meraki/api/**`, `meraki/aio/api/**`, `meraki/_version.py`, `meraki/__init__.py` (`__api_version__`).

**Interfaces:**
- Consumes: verified `migrate/httpx` branch.
- Produces: GA-versioned generated code, then a PR into `main`.

- [ ] **Step 1: Regenerate API surface to GA (maintainer runs the generator)**

The generated code and version strings on the branch are currently httpx's beta values (`4.3.0b1`, `1.72.0-beta.1`). Maintainer runs the generator against the GA spec and sets the GA version. This plan does not prescribe the generator command — it is the maintainer's existing workflow.

- [ ] **Step 2: Re-run verification after regeneration**

```bash
uv run pytest tests/unit tests/generator -q 2>&1 | tail -20
uv run python -c "import meraki, meraki.aio; print('import OK')"
```
Expected: pass. Confirms regenerated code matches httpx session call signatures.

- [ ] **Step 3: Push and open the PR**

```bash
git push -u origin migrate/httpx
```
Then open a PR `migrate/httpx -> main`. PR body should note: transport rewrite (requests → httpx), both histories preserved, X-Request-Id-on-5xx replayed, API regenerated to GA.

- [ ] **Step 4: Do NOT delete branch `httpx`** until the PR is merged and the team confirms the dev track's next steps.

---

## Appendix: PyPI publish outage (root-caused during this migration)

**Symptom:** Every beta/dev release after 2026-06-10 (`3.2.0b3`, `3.3.0b0`, `4.2.0b1/b2/b3`, `4.3.0b0/b1`) created a GitHub Release but never published to PyPI. GA releases (`3.2.0`, `3.3.0`) published fine.

**Root cause:** `release`-triggered workflows run the workflow file from the **tagged commit's tree**, not the default branch. PRs #407 (`db0ddfe`, beta) and #408 (`1f84868`, httpx) deleted `publish-release.yml` from beta+httpx on 2026-06-10 as "unreachable orchestration." The first beta cut 7 minutes later (`4.2.0b1`) had no publish workflow in its tree, so the `release: created` event had nothing to run. GA survived because GA tags come off `main`, which kept the file. Truth table (publish-release.yml in tag tree ⟺ on PyPI) held with zero exceptions.

**Forward fix (applied 2026-07-08):** restored `publish-release.yml` to `httpx` (`acbfd6a`), `beta` (`7fd69d5`), and `migrate/httpx` (`c7800d2`, part of this migration). `create-release`/`watch-openapi-release`/`regenerate-library`/`enable-early-access` correctly stay single-sourced on `main` (their `workflow_run`/`schedule`/`workflow_dispatch` triggers use main's copy; only `release`-triggered workflows must live on every release-cutting branch).

**Backfill:** decided NOT to backfill the 8 orphaned PyPI versions — superseded quickly, and PyPI uploads are permanent/non-reusable. Gaps remain by choice.
