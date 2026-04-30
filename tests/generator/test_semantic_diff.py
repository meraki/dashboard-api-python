"""Unit tests for semantic_diff_v2_v3.py core functions."""
import sys
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parent.parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from semantic_diff_v2_v3 import extract_methods, compare_modules


class TestExtractMethods:
    def test_extracts_simple_method(self):
        content = "    def getNetwork(self, networkId: str):\n        pass\n"
        methods = extract_methods(content)
        assert "getNetwork" in methods
        assert methods["getNetwork"]["params"] == {"networkId": "str"}

    def test_extracts_multiple_params(self):
        content = "    def updateNetwork(self, networkId: str, name: str, **kwargs):\n        pass\n"
        methods = extract_methods(content)
        assert "updateNetwork" in methods
        assert "networkId" in methods["updateNetwork"]["params"]
        assert "name" in methods["updateNetwork"]["params"]
        assert "**kwargs" in methods["updateNetwork"]["params"]

    def test_ignores_init(self):
        content = "    def __init__(self, session):\n        pass\n    def getNetwork(self, id: str):\n        pass\n"
        methods = extract_methods(content)
        assert "__init__" not in methods
        assert "getNetwork" in methods

    def test_handles_default_values(self):
        content = "    def listDevices(self, total_pages=1, direction='next'):\n        pass\n"
        methods = extract_methods(content)
        assert "listDevices" in methods
        assert "total_pages" in methods["listDevices"]["params"]
        assert "direction" in methods["listDevices"]["params"]

    def test_empty_content(self):
        methods = extract_methods("")
        assert methods == {}


class TestCompareModules:
    def test_identical_modules(self):
        content = "    def getNetwork(self, networkId: str):\n        pass\n"
        drifts = compare_modules(content, content, "networks")
        assert len(drifts) == 0

    def test_missing_in_v3(self):
        v2 = "    def getNetwork(self, id: str):\n        pass\n    def deleteNetwork(self, id: str):\n        pass\n"
        v3 = "    def getNetwork(self, id: str):\n        pass\n"
        drifts = compare_modules(v2, v3, "networks")
        missing = [d for d in drifts if d["type"] == "MISSING_IN_V3"]
        assert len(missing) == 1
        assert missing[0]["method"] == "deleteNetwork"

    def test_extra_in_v3(self):
        v2 = "    def getNetwork(self, id: str):\n        pass\n"
        v3 = "    def getNetwork(self, id: str):\n        pass\n    def newMethod(self, id: str):\n        pass\n"
        drifts = compare_modules(v2, v3, "networks")
        extra = [d for d in drifts if d["type"] == "MISSING_IN_V2"]
        assert len(extra) == 1
        assert extra[0]["method"] == "newMethod"

    def test_param_diff(self):
        v2 = "    def getNetwork(self, networkId: str, orgId: str):\n        pass\n"
        v3 = "    def getNetwork(self, networkId: str):\n        pass\n"
        drifts = compare_modules(v2, v3, "networks")
        param_diffs = [d for d in drifts if d["type"] == "PARAM_DIFF"]
        assert len(param_diffs) == 1

    def test_type_diff(self):
        v2 = "    def getNetwork(self, count: str):\n        pass\n"
        v3 = "    def getNetwork(self, count: int):\n        pass\n"
        drifts = compare_modules(v2, v3, "networks")
        type_diffs = [d for d in drifts if d["type"] == "TYPE_DIFF"]
        assert len(type_diffs) == 1
        assert "count" in type_diffs[0]["detail"]

    def test_kwargs_ignored(self):
        v2 = "    def getNetwork(self, id: str, **kwargs):\n        pass\n"
        v3 = "    def getNetwork(self, id: str):\n        pass\n"
        drifts = compare_modules(v2, v3, "networks")
        # **kwargs difference should not trigger PARAM_DIFF
        param_diffs = [d for d in drifts if d["type"] == "PARAM_DIFF"]
        assert len(param_diffs) == 0
