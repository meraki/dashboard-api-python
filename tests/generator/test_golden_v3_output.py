"""TEST-02: Golden-file tests for v3 generator output."""

import json
import os
import re
import shutil
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
GENERATOR_DIR = Path(__file__).resolve().parent.parent.parent / "generator"
sys.path.insert(0, str(GENERATOR_DIR))


def _extract_methods(content: str) -> dict[str, str]:
    """Extract method name -> signature from generated module."""
    methods = {}
    pattern = re.compile(r"^\s{4}def (\w+)\(([^)]*)\):", re.MULTILINE)
    for match in pattern.finditer(content):
        name = match.group(1)
        signature = match.group(2)
        methods[name] = signature
    return methods


def _extract_class_name(content: str) -> str | None:
    """Extract class name from module."""
    match = re.search(r"^class (\w+)", content, re.MULTILINE)
    return match.group(1) if match else None


def _generate_fresh_output(spec, output_dir):
    """Run v3 generator and return generated file contents."""
    import generate_library as gen_v3

    original_cwd = os.getcwd()
    try:
        os.chdir(output_dir)

        def mock_get(url):
            m = MagicMock()
            m.text = f"# placeholder for {url.split('/')[-1]}\n"
            m.ok = True
            return m

        with patch("generate_library.requests.get", side_effect=mock_get):
            gen_v3.generate_library(spec, "0.0.0-golden", "v1", False)

        sync = (output_dir / "meraki/api/networks.py").read_text()
        async_ = (output_dir / "meraki/aio/api/networks.py").read_text()
        batch = (output_dir / "meraki/api/batch/networks.py").read_text()
        return sync, async_, batch
    finally:
        os.chdir(original_cwd)


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


@pytest.fixture
def fresh_output(v3_spec, output_dir):
    return _generate_fresh_output(v3_spec, output_dir)


class TestGoldenSync:
    def test_class_name_matches(self, fresh_output):
        sync, _, _ = fresh_output
        golden = (FIXTURES_DIR / "golden_sync_networks.py").read_text()
        assert _extract_class_name(sync) == _extract_class_name(golden)

    def test_method_names_match(self, fresh_output):
        sync, _, _ = fresh_output
        golden = (FIXTURES_DIR / "golden_sync_networks.py").read_text()
        assert set(_extract_methods(sync).keys()) == set(_extract_methods(golden).keys())

    def test_method_signatures_match(self, fresh_output):
        sync, _, _ = fresh_output
        golden = (FIXTURES_DIR / "golden_sync_networks.py").read_text()
        fresh_methods = _extract_methods(sync)
        golden_methods = _extract_methods(golden)
        for name in golden_methods:
            assert name in fresh_methods, f"Missing method: {name}"
            # Compare param names (ignore whitespace)
            fresh_params = sorted(re.findall(r"\w+", fresh_methods[name]))
            golden_params = sorted(re.findall(r"\w+", golden_methods[name]))
            assert fresh_params == golden_params, f"Signature mismatch for {name}"

    def test_kwargs_update_locals_present(self, fresh_output):
        sync, _, _ = fresh_output
        assert "kwargs.update(locals())" in sync or "kwargs = locals()" in sync


class TestGoldenAsync:
    def test_class_name_matches(self, fresh_output):
        _, async_, _ = fresh_output
        golden = (FIXTURES_DIR / "golden_async_networks.py").read_text()
        assert _extract_class_name(async_) == _extract_class_name(golden)

    def test_method_names_match(self, fresh_output):
        _, async_, _ = fresh_output
        golden = (FIXTURES_DIR / "golden_async_networks.py").read_text()
        assert set(_extract_methods(async_).keys()) == set(_extract_methods(golden).keys())

    def test_method_signatures_match(self, fresh_output):
        _, async_, _ = fresh_output
        golden = (FIXTURES_DIR / "golden_async_networks.py").read_text()
        fresh_methods = _extract_methods(async_)
        golden_methods = _extract_methods(golden)
        for name in golden_methods:
            assert name in fresh_methods, f"Missing method: {name}"
            fresh_params = sorted(re.findall(r"\w+", fresh_methods[name]))
            golden_params = sorted(re.findall(r"\w+", golden_methods[name]))
            assert fresh_params == golden_params, f"Signature mismatch for {name}"


class TestGoldenBatch:
    def test_class_name_matches(self, fresh_output):
        _, _, batch = fresh_output
        golden = (FIXTURES_DIR / "golden_batch_networks.py").read_text()
        assert _extract_class_name(batch) == _extract_class_name(golden)

    def test_method_names_match(self, fresh_output):
        _, _, batch = fresh_output
        golden = (FIXTURES_DIR / "golden_batch_networks.py").read_text()
        assert set(_extract_methods(batch).keys()) == set(_extract_methods(golden).keys())

    def test_batch_method_count(self, fresh_output, v3_spec):
        _, _, batch = fresh_output
        methods = _extract_methods(batch)
        # Subtract __init__
        non_init = {k: v for k, v in methods.items() if k != "__init__"}
        expected = len(v3_spec["x-batchable-actions"])
        assert len(non_init) == expected


class TestGoldenRegeneration:
    def test_update_golden_flag(self, fresh_output, request):
        """When --update-golden is passed, overwrite golden files."""
        if not request.config.getoption("--update-golden", default=False):
            pytest.skip("--update-golden not passed")
        sync, async_, batch = fresh_output
        (FIXTURES_DIR / "golden_sync_networks.py").write_text(sync)
        (FIXTURES_DIR / "golden_async_networks.py").write_text(async_)
        (FIXTURES_DIR / "golden_batch_networks.py").write_text(batch)
