"""
Regression tests for GROUP A (generator) audit fixes.

Covers:
  #1  generate_snippets.py: sys.exit must use a single f-string message
  #3  batch_function_template.jinja2: path-param quoting wraps str()
  #16 generate_library.py: PATCH endpoints generate without NameError
  #18 generate_library.py + templates: keyword-named params (e.g. 'from')
      are remapped from their safe signature name back to the original.

Hermetic: no network. The generator package uses bare `import common`, so the
generator directory is placed on sys.path. parse logic is exercised with small
in-memory spec dicts.
"""

import io
import os
import sys

import jinja2
import pytest

# Repo layout: <root>/generator/*.py and <root>/tests/unit/this_file
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GENERATOR_DIR = os.path.join(REPO_ROOT, "generator")

if GENERATOR_DIR not in sys.path:
    sys.path.insert(0, GENERATOR_DIR)

import generate_library  # noqa: E402
from parser_v3 import clear_cache  # noqa: E402


TEMPLATE_DIR = GENERATOR_DIR + os.sep  # trailing sep so f"{template_dir}name" resolves


def _jinja_env():
    import json

    env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)
    env.filters["to_double_quote_list"] = lambda lst: json.dumps(lst)
    return env


# ---------------------------------------------------------------------------
# #1 generate_snippets.py: sys.exit f-string diagnostic
# ---------------------------------------------------------------------------
def test_snippets_sys_exit_uses_fstring_message():
    src_path = os.path.join(GENERATOR_DIR, "generate_snippets.py")
    with open(src_path, encoding="utf-8") as fp:
        src = fp.read()

    # The buggy form passed two positional args to sys.exit (TypeError).
    assert "sys.exit(p, values)" not in src
    # The fixed form is a single f-string argument.
    assert 'sys.exit(f"Unhandled param type for {p}: {values}")' in src


# ---------------------------------------------------------------------------
# #3 batch_function_template.jinja2: str() around path param before quote
# ---------------------------------------------------------------------------
def test_batch_template_path_param_wraps_str():
    env = _jinja_env()
    with open(os.path.join(GENERATOR_DIR, "batch_function_template.jinja2"), encoding="utf-8") as fp:
        template = env.from_string(fp.read())

    rendered = template.render(
        operation="createDeviceThing",
        function_definition=", serial: str",
        description="desc",
        doc_url="http://example",
        descriptions=[],
        kwarg_line="",
        all_params=[],
        assert_blocks=[],
        tags=["devices"],
        resource="/devices/{serial}/things",
        query_params={},
        array_params={},
        body_params={},
        path_params={"serial": {"type": "string", "in": "path"}},
        call_line="return action",
        batch_operation="create",
        renamed_params={},
    )

    # A non-string (int) path param would TypeError without str() wrapping.
    assert 'urllib.parse.quote(str(serial), safe="")' in rendered
    assert 'urllib.parse.quote(serial, safe="")' not in rendered


# ---------------------------------------------------------------------------
# #16 generate_library.py: PATCH endpoint generates a patch call_line
# ---------------------------------------------------------------------------
def _patch_spec():
    return {
        "paths": {
            "/things/{thingId}": {
                "patch": {
                    "operationId": "updateThing",
                    "tags": ["organizations"],
                    "summary": "Update a thing",
                    "parameters": [
                        {
                            "name": "thingId",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                        }
                    ],
                    "requestBody": {
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {"name": {"type": "string", "description": "n"}},
                                }
                            }
                        }
                    },
                }
            }
        }
    }


def test_patch_endpoint_generates_without_nameerror():
    clear_cache()
    spec = _patch_spec()
    section = {"/things/{thingId}": {"patch": spec["paths"]["/things/{thingId}"]["patch"]}}

    output = io.StringIO()
    async_output = io.StringIO()

    # Would raise NameError (unbound call_line) before fix #16.
    generate_library.generate_standard_and_async_functions(_jinja_env(), TEMPLATE_DIR, section, output, async_output, spec)

    rendered = output.getvalue()
    assert "def updateThing(self" in rendered
    # patch mirrors put/post: dispatches to self._session.patch with the payload.
    assert "self._session.patch(metadata, resource, payload)" in rendered


# ---------------------------------------------------------------------------
# #18 keyword param 'from' is remapped from safe name 'from_' back to 'from'
# ---------------------------------------------------------------------------
def _keyword_param_spec():
    return {
        "paths": {
            "/networks/{networkId}/events": {
                "get": {
                    "operationId": "getNetworkThings",
                    "tags": ["networks"],
                    "summary": "Get things",
                    "parameters": [
                        {
                            "name": "networkId",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"},
                        },
                        {
                            "name": "from",
                            "in": "query",
                            "required": True,
                            "schema": {"type": "string", "description": "start"},
                        },
                    ],
                }
            }
        }
    }


def test_keyword_param_remapped_in_generated_function():
    clear_cache()
    spec = _keyword_param_spec()
    path = "/networks/{networkId}/events"
    section = {path: {"get": spec["paths"][path]["get"]}}

    output = io.StringIO()
    async_output = io.StringIO()

    generate_library.generate_standard_and_async_functions(_jinja_env(), TEMPLATE_DIR, section, output, async_output, spec)

    rendered = output.getvalue()
    # 'from' is a Python keyword -> signature uses 'from_'
    assert "from_: str" in rendered
    # remap loop restores the original key so the value reaches the request
    assert 'kwargs["from"] = kwargs.pop("from_")' in rendered
    # 'from' must still be the query param key used to build params
    assert '"from"' in rendered


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-q"]))
