"""Property-based tests for meraki.encoding using hypothesis."""

from hypothesis import given, settings
from hypothesis import strategies as st

from meraki.encoding import encode_meraki_params


simple_params = st.dictionaries(
    keys=st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=("L", "N"))),
    values=st.one_of(st.text(max_size=50), st.integers(), st.floats(allow_nan=False, allow_infinity=False)),
    min_size=1,
    max_size=10,
)


class TestEncodeRoundtripProperties:
    @given(data=simple_params)
    @settings(max_examples=200)
    def test_always_returns_string(self, data):
        """encode_meraki_params always returns a string for dict input."""
        result = encode_meraki_params(data)
        assert isinstance(result, str)

    @given(data=simple_params)
    @settings(max_examples=200)
    def test_all_keys_present_in_output(self, data):
        """Every key from input dict appears (URL-encoded) in output."""
        from urllib.parse import quote_plus

        result = encode_meraki_params(data)
        for key in data:
            encoded_key = quote_plus(key)
            assert encoded_key in result, f"Key '{key}' (encoded: '{encoded_key}') missing from output"

    @given(text=st.text(max_size=100))
    def test_string_passthrough(self, text):
        """String input passes through unchanged."""
        assert encode_meraki_params(text) is text

    @given(data=st.binary(max_size=100))
    def test_bytes_passthrough(self, data):
        """Bytes input passes through unchanged."""
        assert encode_meraki_params(data) is data

    def test_none_values_excluded(self):
        """None values are excluded from encoding."""
        data = {"key1": "value1", "key2": None}
        result = encode_meraki_params(data)
        assert "key1" in result
        assert "key2" not in result

    def test_empty_dict_returns_empty_string(self):
        """Empty dict produces empty string."""
        result = encode_meraki_params({})
        assert result == ""

    def test_file_like_object_passthrough(self):
        """Objects with .read() attribute pass through."""
        import io

        f = io.BytesIO(b"file content")
        assert encode_meraki_params(f) is f

    def test_array_of_objects_encoding(self):
        """Array-of-objects uses Meraki bracket concatenation."""
        data = {"rules[]": [{"policy": "allow", "destPort": "80"}]}
        result = encode_meraki_params(data)
        assert "rules" in result
        assert "policy" in result
        assert "allow" in result
