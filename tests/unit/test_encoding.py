"""Tests for meraki.encoding module (HTTP-04, QUAL-03)."""
import inspect

import pytest
from hypothesis import given, strategies as st
from urllib.parse import parse_qs

from meraki.encoding import encode_meraki_params


class TestEncodeMerakiParams:
    """Unit tests replicating behavioral spec from test_rest_session.py."""

    def test_string_passthrough(self):
        assert encode_meraki_params("already_encoded") == "already_encoded"

    def test_bytes_passthrough(self):
        assert encode_meraki_params(b"raw") == b"raw"

    def test_file_like_passthrough(self):
        class FakeFile:
            def read(self):
                pass

        f = FakeFile()
        assert encode_meraki_params(f) is f

    def test_non_iterable_passthrough(self):
        assert encode_meraki_params(42) == 42

    def test_simple_dict(self):
        result = encode_meraki_params({"key": "value"})
        assert "key=value" in result

    def test_list_values(self):
        result = encode_meraki_params({"tag": ["a", "b"]})
        assert "tag=a" in result
        assert "tag=b" in result

    def test_array_of_objects(self):
        result = encode_meraki_params({"param[]": [{"key1": "val1"}, {"key2": "val2"}]})
        assert "param%5B%5Dkey1=val1" in result
        assert "param%5B%5Dkey2=val2" in result

    def test_list_of_tuples(self):
        result = encode_meraki_params([("k", "v")])
        assert "k=v" in result


class TestNoRequestsDependency:
    """Verify HTTP-04: no requests import in encoding module."""

    def test_no_requests_import(self):
        import meraki.encoding
        source = inspect.getsource(meraki.encoding)
        assert "import requests" not in source
        assert "from requests" not in source


# --- Property-based tests (QUAL-03, per D-04: roundtrip fidelity) ---

# Strategy: printable text keys (no surrogates, no empty)
_key_strategy = st.text(
    alphabet=st.characters(whitelist_categories=("L", "N", "P"), blacklist_characters="=&#"),
    min_size=1,
    max_size=20,
)

_value_strategy = st.text(
    alphabet=st.characters(whitelist_categories=("L", "N", "P"), blacklist_characters="=&#"),
    min_size=1,
    max_size=50,
)


@given(st.dictionaries(
    keys=_key_strategy,
    values=st.lists(_value_strategy, min_size=1, max_size=5),
))
def test_roundtrip_simple(data):
    """(D-04) Encoded output parsed back with parse_qs reconstructs keys and values."""
    encoded = encode_meraki_params(data)
    if not data:
        assert encoded == ""
        return
    decoded = parse_qs(encoded)
    assert set(decoded.keys()) == set(data.keys())
    for k in data:
        assert decoded[k] == data[k]


@given(st.dictionaries(
    keys=_key_strategy,
    values=st.lists(
        st.dictionaries(
            keys=_key_strategy,
            values=_value_strategy,
            min_size=1,
            max_size=3,
        ),
        min_size=1,
        max_size=3,
    ),
))
def test_roundtrip_array_of_objects(data):
    """(D-04, D-05) Array-of-objects encoding roundtrips: param+inner_key maps to value."""
    encoded = encode_meraki_params(data)
    if not data:
        assert encoded == ""
        return
    decoded = parse_qs(encoded)
    # Verify all expected keys exist
    for param, obj_list in data.items():
        for obj in obj_list:
            for inner_key, inner_val in obj.items():
                composite_key = param + inner_key
                assert composite_key in decoded
                assert inner_val in decoded[composite_key]
