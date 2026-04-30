"""TEST-01: Validate synthetic_v3_spec_full.json exercises all v3-specific features."""
import json
import pytest
from pathlib import Path

from parser_v3 import resolve_ref, parse_request_body, parse_params_v3, clear_cache

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def full_spec():
    with open(FIXTURES / "synthetic_v3_spec_full.json") as f:
        return json.load(f)


@pytest.fixture(autouse=True)
def reset_cache():
    clear_cache()
    yield
    clear_cache()


class TestFixtureCoverage:
    """Assert the comprehensive fixture exercises every v3-specific feature."""

    def test_ref_with_cycle(self, full_spec):
        """Circular $ref returns empty dict sentinel without stack overflow."""
        result = resolve_ref(full_spec, "#/components/schemas/Circular")
        assert result == {}

    def test_ref_chain_cycle(self, full_spec):
        """Multi-hop cycle (ChainA -> ChainB -> ChainA) detected."""
        result = resolve_ref(full_spec, "#/components/schemas/ChainA")
        assert "properties" in result
        # ChainB refs back to ChainA
        chain_b = resolve_ref(full_spec, "#/components/schemas/ChainB")
        assert "properties" in chain_b

    def test_ref_normal_resolution(self, full_spec):
        """Normal $ref resolves to schema dict."""
        result = resolve_ref(full_spec, "#/components/schemas/Network")
        assert result["type"] == "object"
        assert "properties" in result

    def test_request_body_json(self, full_spec):
        """Fixture has endpoint with application/json requestBody."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("put", "post"):
                if method in path_item:
                    op = path_item[method]
                    params, ct = parse_request_body(op, full_spec)
                    if ct == "application/json" and params:
                        found = True
                        break
            if found:
                break
        assert found, "No endpoint with application/json requestBody found"

    def test_request_body_multipart(self, full_spec):
        """Fixture has endpoint with multipart/form-data requestBody."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("put", "post"):
                if method in path_item:
                    op = path_item[method]
                    _, ct = parse_request_body(op, full_spec)
                    if ct == "multipart/form-data":
                        found = True
                        break
            if found:
                break
        assert found, "No endpoint with multipart/form-data requestBody found"

    def test_request_body_octet_stream(self, full_spec):
        """Fixture has endpoint with application/octet-stream requestBody."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("put", "post"):
                if method in path_item:
                    op = path_item[method]
                    _, ct = parse_request_body(op, full_spec)
                    if ct == "application/octet-stream":
                        found = True
                        break
            if found:
                break
        assert found, "No endpoint with application/octet-stream requestBody found"

    def test_oneof_query_param(self, full_spec):
        """Fixture has query param with oneOf schema."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("get", "post", "put", "delete"):
                if method in path_item:
                    op = path_item[method]
                    params, _ = parse_params_v3(op, path_item, full_spec)
                    for name, entry in params.items():
                        if " or " in entry.get("type", ""):
                            found = True
                            break
                if found:
                    break
            if found:
                break
        assert found, "No oneOf query param found"

    def test_nullable_param(self, full_spec):
        """Fixture has at least one param with nullable: true."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("get", "post", "put", "delete"):
                if method in path_item:
                    op = path_item[method]
                    params, _ = parse_params_v3(op, path_item, full_spec)
                    for name, entry in params.items():
                        if entry.get("nullable") is True:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        assert found, "No nullable param found"

    def test_path_level_params(self, full_spec):
        """Fixture has path-level parameters key on at least one path."""
        found = any(
            "parameters" in path_item
            for path_item in full_spec["paths"].values()
        )
        assert found, "No path-level parameters found"

    def test_array_param_with_style(self, full_spec):
        """Fixture has array query param that gets style/explode defaults."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("get", "post", "put", "delete"):
                if method in path_item:
                    op = path_item[method]
                    params, _ = parse_params_v3(op, path_item, full_spec)
                    for name, entry in params.items():
                        if entry.get("type") == "array" and "style" in entry:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        assert found, "No array param with style/explode found"

    def test_pagination_injection(self, full_spec):
        """Fixture has perPage param triggering pagination params injection."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("get",):
                if method in path_item:
                    op = path_item[method]
                    params, _ = parse_params_v3(op, path_item, full_spec)
                    if "total_pages" in params and "direction" in params:
                        found = True
                        break
            if found:
                break
        assert found, "No pagination injection found"

    def test_batchable_actions(self, full_spec):
        """Fixture has x-batchable-actions with >= 3 entries."""
        actions = full_spec.get("x-batchable-actions", [])
        assert len(actions) >= 3

    def test_multiple_scopes(self, full_spec):
        """Fixture has tags for both networks and organizations."""
        tag_names = [t["name"] for t in full_spec["tags"]]
        assert "networks" in tag_names
        assert "organizations" in tag_names

    def test_enum_param(self, full_spec):
        """Fixture has at least one param with enum values."""
        found = False
        for path, path_item in full_spec["paths"].items():
            for method in ("get", "post", "put", "delete"):
                if method in path_item:
                    op = path_item[method]
                    params, _ = parse_params_v3(op, path_item, full_spec)
                    for name, entry in params.items():
                        if "enum" in entry:
                            found = True
                            break
                if found:
                    break
            if found:
                break
        assert found, "No enum param found"
