"""Tests for .pyi stub generation."""
import json
import os
import shutil
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
GENERATOR_DIR = Path(__file__).resolve().parent.parent.parent / "generator"
sys.path.insert(0, str(GENERATOR_DIR))


@pytest.fixture
def v3_spec():
    with open(FIXTURES_DIR / "synthetic_v3_spec_gen.json") as f:
        return json.load(f)


@pytest.fixture
def output_dir(tmp_path):
    for tmpl in GENERATOR_DIR.glob("*.jinja2"):
        shutil.copy2(tmpl, tmp_path / tmpl.name)
    return tmp_path


class TestStubGeneration:
    def test_produces_pyi_file(self, v3_spec, output_dir):
        """Test 1: generate_stub_modules produces meraki/api/networks.pyi file."""
        import jinja2
        from generate_stubs import generate_stub_modules

        tags = v3_spec["tags"]
        scopes = {tag["name"]: {} for tag in tags}

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            assert (output_dir / "meraki" / "api" / "networks.pyi").exists()
        finally:
            os.chdir(original_cwd)

    def test_contains_typed_class(self, v3_spec, output_dir):
        """Test 2: .pyi file contains class Networks with typed method signatures."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            assert "class Networks:" in content
            assert "def getNetwork(" in content
        finally:
            os.chdir(original_cwd)

    def test_required_string_param_no_default(self, v3_spec, output_dir):
        """Test 3: Required string param renders as 'networkId: str' (no default)."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            assert "networkId: str" in content
            # Verify no default on required param
            assert "networkId: str = None" not in content
        finally:
            os.chdir(original_cwd)

    def test_optional_string_param_with_default(self, v3_spec, output_dir):
        """Test 4: Optional string param renders as 'name: str | None = None'."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            # getNetwork has optional 'name' query param
            assert "str | None" in content
        finally:
            os.chdir(original_cwd)

    def test_nullable_required_param_renders_nullable(self, v3_spec, output_dir):
        """Test 5: Nullable required param renders as 'deviceName: str | None' (no default, but nullable)."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            # provisionNetworkClients has required deviceName with nullable: true
            assert "deviceName: str | None" in content
        finally:
            os.chdir(original_cwd)

    def test_oneof_param_renders_union(self, v3_spec, output_dir):
        """Test 6: OneOf param (type 'string or object') renders as 'filter: dict | str | None = None'."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            # getNetworkClients has oneOf filter param (types sorted alphabetically)
            assert "dict | str" in content
        finally:
            os.chdir(original_cwd)

    def test_required_int_param(self, v3_spec, output_dir):
        """Test 7: Required int param renders as 'count: int'."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            # getNetworkClients has required count param
            assert "count: int" in content
        finally:
            os.chdir(original_cwd)

    def test_stub_body_is_ellipsis(self, v3_spec, output_dir):
        """Test 8: .pyi contains no function bodies (only '...' after signature)."""
        import jinja2
        from generate_stubs import generate_stub_modules
        import common

        tags = v3_spec["tags"]
        paths = v3_spec["paths"]
        scopes = {tag["name"]: {} for tag in tags}

        filtered_paths = {}
        for path, path_item in paths.items():
            filtered_paths[path] = {k: v for k, v in path_item.items() if k in ["get", "post", "put", "delete", "patch"]}

        operations, scopes = common.organize_spec(filtered_paths, scopes)

        jinja_env = jinja2.Environment(trim_blocks=True, lstrip_blocks=True, keep_trailing_newline=True)

        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            os.makedirs("meraki/api", exist_ok=True)

            generate_stub_modules(v3_spec, scopes, jinja_env, "")

            content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
            # Methods should end with ': ...'
            assert "def getNetwork(" in content
            assert ": ..." in content
            # No implementation bodies
            assert "return" not in content
        finally:
            os.chdir(original_cwd)
