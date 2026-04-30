# Contributing

Meraki welcomes constructive pull requests that maintain backwards compatibility with prior versions.

## Setup

```bash
# Clone and install dev dependencies
git clone https://github.com/meraki/dashboard-api-python.git
cd dashboard-api-python
uv sync
```

## Development Workflow

1. Create a feature branch from `main`
2. Make your changes
3. Run tests: `uv run pytest tests/unit`
4. Run linting: `uv run ruff check . && uv run ruff format --check .`
5. Open a pull request against `main`

## Code Standards

- Line length: 127 characters
- Formatter: ruff format
- Linter: ruff + flake8
- Test coverage floor: 90% (core, non-generated code)
- Python versions: 3.11+

## What to Contribute

- Bug fixes with regression tests
- Documentation improvements
- Test coverage improvements for non-generated code
- Performance improvements with benchmarks

## What Not to Modify

- Generated API scope files (`meraki/api/`, `meraki/aio/api/`) are auto-generated from the OpenAPI spec. Changes here will be overwritten. Fix the generator instead.
- Do not vendor or bundle dependencies.

## Running the Generator

```bash
uv sync --group generator
uv run python generator/generate_library.py
```

## Questions

- GitHub Issues: bug reports and feature requests
- [Meraki Community](https://community.meraki.com/): general discussion
- [api-feedback@meraki.net](mailto:api-feedback@meraki.net): direct contact
