import json
import pytest
from pathlib import Path

from parser_v3 import resolve_ref, clear_cache, _ref_cache

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
