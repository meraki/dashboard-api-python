"""
Golden-file integration test for the full generate_library pipeline.

To regenerate golden files after intentional changes:
    pytest --update-golden tests/generator/test_generate_library_golden.py
"""

import json
import os
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

import generate_library as gen

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
GOLDEN_DIR = Path(__file__).resolve().parent / "golden"
GENERATOR_DIR = Path(__file__).resolve().parent.parent.parent / "generator"

GOLDEN_FILES = [
    "meraki/api/networks.py",
    "meraki/aio/api/networks.py",
    "meraki/api/batch/networks.py",
]


@pytest.fixture
def update_golden(request):
    return request.config.getoption("--update-golden")


@pytest.fixture
def synthetic_spec():
    with open(FIXTURES_DIR / "synthetic_spec.json") as f:
        return json.load(f)


@pytest.fixture
def output_dir(tmp_path):
    for tmpl in GENERATOR_DIR.glob("*.jinja2"):
        shutil.copy2(tmpl, tmp_path / tmpl.name)
    return tmp_path


def _mock_requests_get(url):
    mock_response = MagicMock()
    mock_response.text = f"# placeholder for {url.split('/')[-1]}\n"
    mock_response.ok = True
    return mock_response


def _run_generation(synthetic_spec, output_dir):
    original_cwd = os.getcwd()
    try:
        os.chdir(output_dir)
        with patch("generate_library.requests.get", side_effect=_mock_requests_get):
            gen.generate_library(
                spec=synthetic_spec,
                version_number="0.0.0-test",
                api_version_number="v1-test",
                is_github_action=False,
            )
    finally:
        os.chdir(original_cwd)


class TestGoldenFiles:
    def test_generate_and_compare(self, synthetic_spec, output_dir, update_golden):
        _run_generation(synthetic_spec, output_dir)

        for rel_path in GOLDEN_FILES:
            generated_file = output_dir / rel_path
            golden_file = GOLDEN_DIR / rel_path

            assert generated_file.exists(), (
                f"Expected generated file not found: {rel_path}"
            )

            generated_content = generated_file.read_text(encoding="utf-8")

            if update_golden:
                golden_file.parent.mkdir(parents=True, exist_ok=True)
                golden_file.write_text(generated_content, encoding="utf-8")
            else:
                assert golden_file.exists(), (
                    f"Golden file missing: {golden_file}\n"
                    f"Run with --update-golden to generate."
                )
                expected_content = golden_file.read_text(encoding="utf-8")
                assert generated_content == expected_content, (
                    f"Generated output differs from golden file: {rel_path}\n"
                    f"Run with --update-golden to update."
                )

    def test_no_real_http_calls(self, synthetic_spec, output_dir):
        original_cwd = os.getcwd()
        try:
            os.chdir(output_dir)
            with patch(
                "generate_library.requests.get", side_effect=_mock_requests_get
            ) as mocked:
                gen.generate_library(
                    spec=synthetic_spec,
                    version_number="0.0.0-test",
                    api_version_number="v1-test",
                    is_github_action=False,
                )
            assert mocked.call_count > 0
            for call in mocked.call_args_list:
                url = call[0][0]
                assert "raw.githubusercontent.com" in url
        finally:
            os.chdir(original_cwd)
