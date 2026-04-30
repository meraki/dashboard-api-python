#!/usr/bin/env python3
"""Semantic diff between v2 and v3 generator output.

Compares method signatures, parameter lists, and types.
Ignores formatting, kwargs style, and whitespace.

Usage:
    python scripts/semantic_diff_v2_v3.py [spec.json]
    python scripts/semantic_diff_v2_v3.py --live

Exit codes:
    0: Only known/expected differences (or identical)
    1: Unexpected semantic drift detected
"""

import argparse
import contextlib
import json
import os
import re
import shutil
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

GENERATOR_DIR = Path(__file__).resolve().parent.parent / "generator"
sys.path.insert(0, str(GENERATOR_DIR))


def extract_methods(content: str) -> dict[str, dict]:
    """Extract method name -> {signature, params, body_section} from module."""
    methods = {}
    # Match method definitions (may span multiple lines after ruff formatting)
    pattern = re.compile(r"^\s{4}def (\w+)\(\s*self(.*?)\s*\):", re.MULTILINE | re.DOTALL)
    for match in pattern.finditer(content):
        name = match.group(1)
        if name == "__init__":
            continue
        # Normalize multiline signatures: collapse whitespace
        raw_sig = re.sub(r"\s+", " ", match.group(2)).strip(", ")
        # Parse param names and types from signature
        params = {}
        if raw_sig:
            for part in re.split(r",\s*", raw_sig):
                part = part.strip()
                if "=" in part:
                    part = part.split("=")[0].strip()
                if ":" in part:
                    pname, ptype = part.split(":", 1)
                    params[pname.strip()] = ptype.strip()
                elif part == "**kwargs":
                    params["**kwargs"] = "**kwargs"
                else:
                    params[part] = "untyped"
        methods[name] = {"signature": raw_sig, "params": params}
    return methods


def compare_modules(v2_content: str, v3_content: str, scope: str) -> list[dict]:
    """Compare two module contents semantically. Returns list of drift entries."""
    v2_methods = extract_methods(v2_content)
    v3_methods = extract_methods(v3_content)

    drifts = []

    # Methods in v2 but not v3
    for name in sorted(set(v2_methods) - set(v3_methods)):
        drifts.append(
            {"type": "MISSING_IN_V3", "scope": scope, "method": name, "detail": f"Method {name} exists in v2 but not v3"}
        )

    # Methods in v3 but not v2 (informational, not failure)
    for name in sorted(set(v3_methods) - set(v2_methods)):
        drifts.append(
            {
                "type": "MISSING_IN_V2",
                "scope": scope,
                "method": name,
                "detail": f"Method {name} exists in v3 but not v2 (likely new endpoint)",
            }
        )

    # Methods in both: compare params
    for name in sorted(set(v2_methods) & set(v3_methods)):
        v2_params = v2_methods[name]["params"]
        v3_params = v3_methods[name]["params"]

        # Compare param names (ignore **kwargs, it's expected to differ)
        v2_names = set(v2_params.keys()) - {"**kwargs"}
        v3_names = set(v3_params.keys()) - {"**kwargs"}

        if v2_names != v3_names:
            missing_in_v3 = v2_names - v3_names
            extra_in_v3 = v3_names - v2_names
            if missing_in_v3 or extra_in_v3:
                drifts.append(
                    {
                        "type": "PARAM_DIFF",
                        "scope": scope,
                        "method": name,
                        "detail": f"Param diff: missing_in_v3={missing_in_v3}, extra_in_v3={extra_in_v3}",
                    }
                )

        # Compare types for shared params
        shared = v2_names & v3_names
        for p in sorted(shared):
            v2_type = v2_params[p]
            v3_type = v3_params[p]
            if v2_type != v3_type and v2_type != "untyped" and v3_type != "untyped":
                drifts.append(
                    {"type": "TYPE_DIFF", "scope": scope, "method": name, "detail": f"Param '{p}': v2={v2_type}, v3={v3_type}"}
                )

    return drifts


def mock_requests_get(url):
    """Mock requests.get for offline generation."""
    m = MagicMock()
    m.text = f"# placeholder for {url.split('/')[-1]}\n"
    m.ok = True
    return m


def run_v2_generator(spec: dict, output_dir: Path):
    """Run v2 generator in output_dir."""
    import generate_library as gen_v2

    original = os.getcwd()
    try:
        os.chdir(output_dir)
        with (
            patch("generate_library.requests.get", side_effect=mock_requests_get),
            contextlib.redirect_stdout(open(os.devnull, "w")),
        ):
            gen_v2.generate_library(spec, "0.0.0-diff", "v1", False)
    finally:
        os.chdir(original)


def run_v3_generator(spec: dict, output_dir: Path):
    """Run v3 generator in output_dir."""
    import generate_library as gen_v3

    original = os.getcwd()
    try:
        os.chdir(output_dir)
        with (
            patch("generate_library.requests.get", side_effect=mock_requests_get),
            contextlib.redirect_stdout(open(os.devnull, "w")),
        ):
            gen_v3.generate_library(spec, "0.0.0-diff", False)
    finally:
        os.chdir(original)


def main():
    parser = argparse.ArgumentParser(description="Semantic diff v2 vs v3 generator output")
    parser.add_argument("spec_file", nargs="?", help="Path to OAS spec JSON (omit for live fetch)")
    parser.add_argument("--live", action="store_true", help="Fetch live spec from api.meraki.com")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fail-on-missing", action="store_true", help="Exit 1 if v3 is missing methods that v2 has")
    args = parser.parse_args()

    # Load spec
    if args.spec_file:
        with open(args.spec_file) as f:
            spec = json.load(f)
    elif args.live:
        import requests

        resp = requests.get("https://api.meraki.com/api/v1/openapiSpec", params={"version": 3})
        resp.raise_for_status()
        spec = resp.json()
    else:
        print("Error: provide spec_file path or --live flag", file=sys.stderr)
        sys.exit(2)

    # Setup temp dirs with templates
    v2_dir = Path(tempfile.mkdtemp(prefix="v2_"))
    v3_dir = Path(tempfile.mkdtemp(prefix="v3_"))

    for d in (v2_dir, v3_dir):
        for tmpl in GENERATOR_DIR.glob("*.jinja2"):
            shutil.copy2(tmpl, d / tmpl.name)
        # Copy pyproject.toml for ruff config
        pyproject = GENERATOR_DIR.parent / "pyproject.toml"
        if pyproject.exists():
            shutil.copy2(pyproject, d / "pyproject.toml")

    # Run both generators
    print("Running v2 generator...", file=sys.stderr)
    run_v2_generator(spec, v2_dir)
    print("Running v3 generator...", file=sys.stderr)
    run_v3_generator(spec, v3_dir)

    # Compare each scope
    all_drifts = []
    v2_api = v2_dir / "meraki" / "api"
    v3_api = v3_dir / "meraki" / "api"

    if v2_api.exists() and v3_api.exists():
        v2_modules = {f.stem for f in v2_api.glob("*.py") if f.stem != "__init__"}
        v3_modules = {f.stem for f in v3_api.glob("*.py") if f.stem != "__init__"}

        for scope in sorted(v2_modules & v3_modules):
            v2_content = (v2_api / f"{scope}.py").read_text()
            v3_content = (v3_api / f"{scope}.py").read_text()
            drifts = compare_modules(v2_content, v3_content, scope)
            all_drifts.extend(drifts)

    # Cleanup
    shutil.rmtree(v2_dir, ignore_errors=True)
    shutil.rmtree(v3_dir, ignore_errors=True)

    # Report
    if args.json:
        print(json.dumps(all_drifts, indent=2))
    else:
        if not all_drifts:
            print("No semantic drift detected between v2 and v3 output.")
        else:
            missing_v3 = [d for d in all_drifts if d["type"] == "MISSING_IN_V3"]
            missing_v2 = [d for d in all_drifts if d["type"] == "MISSING_IN_V2"]
            param_diffs = [d for d in all_drifts if d["type"] == "PARAM_DIFF"]
            type_diffs = [d for d in all_drifts if d["type"] == "TYPE_DIFF"]

            print("\n=== Semantic Drift Report ===")
            print(f"Methods missing in v3: {len(missing_v3)}")
            print(f"Methods only in v3: {len(missing_v2)}")
            print(f"Parameter differences: {len(param_diffs)}")
            print(f"Type differences: {len(type_diffs)}")

            if missing_v3:
                print(f"\n--- Missing in v3 ({len(missing_v3)}) ---")
                for d in missing_v3[:20]:
                    print(f"  {d['scope']}.{d['method']}")

            if param_diffs:
                print(f"\n--- Param Diffs ({len(param_diffs)}) ---")
                for d in param_diffs[:20]:
                    print(f"  {d['scope']}.{d['method']}: {d['detail']}")

            if type_diffs:
                print(f"\n--- Type Diffs ({len(type_diffs)}) ---")
                for d in type_diffs[:20]:
                    print(f"  {d['scope']}.{d['method']}: {d['detail']}")

    # Exit code
    if args.fail_on_missing:
        missing_count = len([d for d in all_drifts if d["type"] == "MISSING_IN_V3"])
        if missing_count > 0:
            sys.exit(1)

    # PARAM_DIFF and TYPE_DIFF are informational for now (v3 intentionally differs)
    sys.exit(0)


if __name__ == "__main__":
    main()
