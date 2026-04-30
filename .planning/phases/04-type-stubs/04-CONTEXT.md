# Phase 4: Type Stubs - Context

**Gathered:** 2026-04-30
**Status:** Ready for planning
**Mode:** Auto-generated (infrastructure phase, discuss skipped)

<domain>
## Phase Boundary

Generator produces .pyi type stub files via Jinja2 template for static analysis tooling. Adds --stubs flag, py.typed marker, and type annotations reflecting nullable/oneOf semantics.

</domain>

<decisions>
## Implementation Decisions

### Claude's Discretion
All implementation choices are at Claude's discretion. Key constraints from success criteria:

- .pyi files created when --stubs flag is passed to CLI
- py.typed marker file for PEP 561 compliance
- Type annotations use `str | None` for nullable params and `Union[str, dict]` (or `str | dict`) for oneOf params
- Stubs generated via Jinja2 template (new template for .pyi output)
- Must integrate with generate_library_v3.py CLI from Phase 3

</decisions>

<code_context>
## Existing Code Insights

### Reusable Assets
- `generator/generate_library_v3.py`: Phase 3 generator with CLI and template rendering
- `generator/parser_v3.py`: parse_params_v3 output includes nullable and type info
- Jinja2 templates in generator/ directory

### Established Patterns
- Generator uses Jinja2 templates for code generation
- CLI uses argparse with -h/-o/-k/-v/-a/-g flags
- Param dicts have nullable and type fields for annotation generation

### Integration Points
- --stubs flag added to existing CLI in generate_library_v3.py
- .pyi files go alongside .py files in meraki/api/, meraki/aio/api/
- py.typed marker in meraki/ package root

</code_context>

<specifics>
## Specific Ideas

No specific requirements. Standard approaches are fine.

</specifics>

<deferred>
## Deferred Ideas

None.

</deferred>
