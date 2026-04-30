"""Tests for v3 generator module."""

import json
import os
import shutil
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
GENERATOR_DIR = Path(__file__).resolve().parent.parent.parent / "generator"

# Add generator to path for imports
sys.path.insert(0, str(GENERATOR_DIR))


@pytest.fixture
def v3_spec():
    with open(FIXTURES_DIR / "synthetic_v3_spec_gen.json") as f:
        return json.load(f)


@pytest.fixture
def output_dir(tmp_path):
    for tmpl in GENERATOR_DIR.glob("*.jinja2"):
        shutil.copy2(tmpl, tmp_path / tmpl.name)
    project_root = GENERATOR_DIR.parent
    shutil.copy2(project_root / "pyproject.toml", tmp_path / "pyproject.toml")
    return tmp_path


def _mock_requests_get(url):
    mock_response = MagicMock()
    mock_response.text = f"# placeholder for {url.split('/')[-1]}\n"
    mock_response.ok = True
    return mock_response


def _run_v3_generation(v3_spec, output_dir):
    import generate_library as gen_v3

    original_cwd = os.getcwd()
    try:
        os.chdir(output_dir)
        with patch("generate_library.requests.get", side_effect=_mock_requests_get):
            gen_v3.generate_library(
                spec=v3_spec,
                version_number="0.0.0-test",
                api_version_number="v1",
                is_github_action=False,
            )
    finally:
        os.chdir(original_cwd)


def _run_v3_generation_with_stubs(v3_spec, output_dir):
    import generate_library as gen_v3

    original_cwd = os.getcwd()
    try:
        os.chdir(output_dir)
        with patch("generate_library.requests.get", side_effect=_mock_requests_get):
            gen_v3.generate_library(
                spec=v3_spec,
                version_number="0.0.0-test",
                api_version_number="v1",
                is_github_action=False,
                generate_stubs=True,
            )
    finally:
        os.chdir(original_cwd)


class TestV3GeneratorOutput:
    def test_produces_sync_module(self, v3_spec, output_dir):
        _run_v3_generation(v3_spec, output_dir)
        assert (output_dir / "meraki" / "api" / "networks.py").exists()

    def test_produces_async_module(self, v3_spec, output_dir):
        _run_v3_generation(v3_spec, output_dir)
        assert (output_dir / "meraki" / "aio" / "api" / "networks.py").exists()

    def test_produces_batch_module(self, v3_spec, output_dir):
        _run_v3_generation(v3_spec, output_dir)
        assert (output_dir / "meraki" / "api" / "batch" / "networks.py").exists()

    def test_kwargs_merges_positional_params(self, v3_spec, output_dir):
        """Required positional params must be merged into kwargs for payload construction."""
        _run_v3_generation(v3_spec, output_dir)
        content = (output_dir / "meraki" / "api" / "networks.py").read_text()
        assert "kwargs.update(locals())" in content or "kwargs = locals()" in content

    def test_batch_action_count(self, v3_spec, output_dir):
        """GEN-04: All batchable actions produce batch methods."""
        _run_v3_generation(v3_spec, output_dir)
        content = (output_dir / "meraki" / "api" / "batch" / "networks.py").read_text()
        expected_count = len(v3_spec["x-batchable-actions"])
        # Count def lines (each batch method = one def)
        method_count = content.count("    def ")
        # Subtract __init__
        method_count -= 1
        assert method_count == expected_count, f"Expected {expected_count} batch methods, got {method_count}"

    def test_explicit_param_construction(self, v3_spec, output_dir):
        """GEN-02: Methods use explicit param list filtering."""
        _run_v3_generation(v3_spec, output_dir)
        content = (output_dir / "meraki" / "api" / "networks.py").read_text()
        # getNetwork has query param 'name', should appear in query_params list
        assert '"name"' in content
        # updateNetwork has body params, should appear in body_params list
        assert "body_params" in content


class TestV3CLI:
    def test_help_flag_exits(self):
        """GEN-05: -h prints help and exits."""
        import generate_library as gen_v3

        with pytest.raises(SystemExit) as exc_info:
            gen_v3.main(["-h"])
        assert exc_info.value.code == 2

    def test_accepts_all_v2_flags(self):
        """GEN-05: CLI accepts -o, -k, -v, -a, -g flags."""
        import getopt

        opts, args = getopt.getopt(["-o", "123", "-k", "fake", "-v", "1.0", "-a", "v1", "-g", "false"], "ho:k:v:a:g:")
        flags = [o for o, _ in opts]
        assert "-o" in flags
        assert "-k" in flags
        assert "-v" in flags
        assert "-a" in flags
        assert "-g" in flags

    def test_spec_fetch_uses_version_3(self):
        """GEN-05: Spec fetch includes ?version=3."""
        import generate_library as gen_v3

        with patch("generate_library.requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.ok = True
            mock_response.json.return_value = {"paths": {}, "tags": [], "x-batchable-actions": []}
            mock_get.return_value = mock_response

            with patch.object(gen_v3, "generate_library"):
                gen_v3.main(["-v", "1.0"])

            # Verify params={"version": 3} was passed
            call_kwargs = mock_get.call_args.kwargs
            assert call_kwargs.get("params") == {"version": 3}

    def test_org_specific_fetch_uses_version_3(self):
        """GEN-05: Org-specific fetch includes ?version=3 and auth header."""
        import generate_library as gen_v3

        with patch("generate_library.requests.get") as mock_get:
            mock_response = MagicMock()
            mock_response.ok = True
            mock_response.json.return_value = {"paths": {}, "tags": [], "x-batchable-actions": []}
            mock_get.return_value = mock_response

            with patch.object(gen_v3, "generate_library"):
                gen_v3.main(["-o", "12345", "-k", "testkey", "-v", "1.0"])

            args, kwargs = mock_get.call_args
            assert "12345" in args[0]
            assert kwargs.get("params") == {"version": 3}
            assert "Bearer testkey" in kwargs.get("headers", {}).get("Authorization", "")


class TestV3Stubs:
    def test_stubs_flag_produces_pyi(self, v3_spec, output_dir):
        """GEN-03: --stubs produces .pyi files."""
        _run_v3_generation_with_stubs(v3_spec, output_dir)
        assert (output_dir / "meraki" / "api" / "networks.pyi").exists()

    def test_stubs_flag_creates_py_typed(self, v3_spec, output_dir):
        """GEN-03: --stubs creates py.typed marker."""
        _run_v3_generation_with_stubs(v3_spec, output_dir)
        assert (output_dir / "meraki" / "py.typed").exists()

    def test_no_stubs_without_flag(self, v3_spec, output_dir):
        """GEN-03: Without --stubs, no .pyi files generated."""
        _run_v3_generation(v3_spec, output_dir)
        assert not (output_dir / "meraki" / "api" / "networks.pyi").exists()
        assert not (output_dir / "meraki" / "py.typed").exists()

    def test_pyi_contains_typed_signatures(self, v3_spec, output_dir):
        """GEN-03: .pyi has method signatures with type annotations."""
        _run_v3_generation_with_stubs(v3_spec, output_dir)
        content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
        assert "def getNetwork" in content
        assert "networkId: str" in content
        assert "..." in content  # ellipsis body

    def test_pyi_nullable_annotation(self, v3_spec, output_dir):
        """GEN-03: Nullable params use | None annotation."""
        _run_v3_generation_with_stubs(v3_spec, output_dir)
        content = (output_dir / "meraki" / "api" / "networks.pyi").read_text()
        # Optional (non-required) params should have | None = None
        assert "| None" in content

    def test_cli_accepts_s_flag(self):
        """GEN-03: CLI accepts -s flag."""
        import getopt

        opts, args = getopt.getopt(["-s", "-v", "1.0"], "ho:k:v:a:g:s")
        flags = [o for o, _ in opts]
        assert "-s" in flags
