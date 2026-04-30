import json
import pytest
from pathlib import Path

from parser_v3 import resolve_ref, clear_cache, _ref_cache, parse_request_body

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def v3_spec():
    with open(FIXTURES / "synthetic_v3_spec.json") as f:
        return json.load(f)


@pytest.fixture(autouse=True)
def reset_cache():
    """Clear cache before each test to prevent cross-test pollution."""
    clear_cache()
    yield
    clear_cache()


class TestResolveRef:
    def test_basic_resolution(self, v3_spec):
        result = resolve_ref(v3_spec, "#/components/schemas/Network")
        assert result["type"] == "object"
        assert "id" in result["properties"]
        assert result["properties"]["id"]["type"] == "string"

    def test_caching(self, v3_spec):
        resolve_ref(v3_spec, "#/components/schemas/Network")
        assert "#/components/schemas/Network" in _ref_cache

    def test_cache_returns_same_object(self, v3_spec):
        first = resolve_ref(v3_spec, "#/components/schemas/Network")
        second = resolve_ref(v3_spec, "#/components/schemas/Network")
        assert first is second

    def test_cycle_detection_returns_sentinel(self, v3_spec):
        # Circular: $ref points to itself
        result = resolve_ref(v3_spec, "#/components/schemas/Circular")
        assert result == {}

    def test_unresolvable_raises_key_error(self, v3_spec):
        with pytest.raises(KeyError, match="Unresolvable"):
            resolve_ref(v3_spec, "#/components/schemas/DoesNotExist")

    def test_rejects_external_ref(self, v3_spec):
        with pytest.raises(ValueError, match="Only internal refs"):
            resolve_ref(v3_spec, "external.json#/schemas/Foo")

    def test_json_pointer_escaping(self, v3_spec):
        # Add a key with slash to test RFC 6901 escaping
        v3_spec["components"]["schemas"]["has/slash"] = {"type": "string"}
        result = resolve_ref(v3_spec, "#/components/schemas/has~1slash")
        assert result == {"type": "string"}

    def test_tilde_escaping(self, v3_spec):
        v3_spec["components"]["schemas"]["has~tilde"] = {"type": "integer"}
        result = resolve_ref(v3_spec, "#/components/schemas/has~0tilde")
        assert result == {"type": "integer"}


class TestClearCache:
    def test_clears_populated_cache(self, v3_spec):
        resolve_ref(v3_spec, "#/components/schemas/Network")
        assert len(_ref_cache) > 0
        clear_cache()
        assert len(_ref_cache) == 0

    def test_clear_empty_cache_no_error(self):
        clear_cache()  # Should not raise
        assert _ref_cache == {}


class TestParseRequestBody:
    """Tests for parse_request_body per PARSE-02."""

    def test_json_body_extracts_properties(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, content_type = parse_request_body(operation, v3_spec)
        assert "name" in params
        assert "tags" in params
        assert "timeZone" in params
        assert "notes" in params
        assert params["name"]["in"] == "body"
        assert params["name"]["type"] == "string"
        assert params["name"]["description"] == "Network name"

    def test_required_tracking(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, _ = parse_request_body(operation, v3_spec)
        assert params["name"]["required"] is True
        assert params["tags"]["required"] is False
        assert params["notes"]["required"] is False

    def test_nullable_field(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, _ = parse_request_body(operation, v3_spec)
        assert params["timeZone"]["nullable"] is True
        assert params["name"]["nullable"] is False

    def test_content_type_json(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        _, content_type = parse_request_body(operation, v3_spec)
        assert content_type == "application/json"

    def test_no_request_body(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["get"]
        params, content_type = parse_request_body(operation, v3_spec)
        assert params == {}
        assert content_type is None

    def test_ref_in_schema(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}/firmware"]["post"]
        params, content_type = parse_request_body(operation, v3_spec)
        # Schema $ref resolves to Network which has id and name properties
        assert "id" in params
        assert "name" in params
        assert params["id"]["type"] == "string"
        assert content_type == "application/json"

    def test_octet_stream(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}/upload"]["post"]
        params, content_type = parse_request_body(operation, v3_spec)
        assert content_type == "application/octet-stream"
        assert "file" in params
        assert params["file"]["required"] is True
        assert params["file"]["in"] == "body"
        assert params["file"]["type"] == "file"
        assert params["file"]["description"] == "Binary file content"

    def test_multipart_form_data(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}/floorPlans"]["post"]
        params, content_type = parse_request_body(operation, v3_spec)
        assert content_type == "multipart/form-data"
        assert "name" in params
        assert "imageContents" in params
        assert params["name"]["required"] is True
        assert params["imageContents"]["required"] is True
        assert params["name"]["in"] == "body"

    def test_array_type_includes_items(self, v3_spec):
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, _ = parse_request_body(operation, v3_spec)
        assert params["tags"]["type"] == "array"
        assert params["tags"]["items"] == {"type": "string"}

    def test_v2_format_keys_present(self, v3_spec):
        """Every param entry has required v2 keys: required, in, type, description."""
        operation = v3_spec["paths"]["/networks/{networkId}"]["put"]
        params, _ = parse_request_body(operation, v3_spec)
        for name, entry in params.items():
            assert "required" in entry, f"{name} missing 'required'"
            assert "in" in entry, f"{name} missing 'in'"
            assert "type" in entry, f"{name} missing 'type'"
            assert "description" in entry, f"{name} missing 'description'"
            assert "nullable" in entry, f"{name} missing 'nullable'"
