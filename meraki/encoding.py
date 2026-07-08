"""Meraki-specific parameter encoding using only stdlib.

This module provides encode_meraki_params(), a pure function replacement for
the monkey-patched requests._encode_params in rest_session.py. Uses only
urllib.parse (no requests dependency). See HTTP-04.
"""

from urllib.parse import urlencode


def encode_meraki_params(data):
    """Encode parameters for Meraki API requests.

    Supports:
    - str/bytes: passthrough
    - file-like (has .read): passthrough
    - dict: URL encode with array-of-objects support
    - list of 2-tuples: URL encode with array-of-objects support
    - other: passthrough

    Array-of-objects encoding (Meraki-specific):
        {"param[]": [{"key1": "val1"}]} -> "param%5B%5Dkey1=val1"

    Args:
        data: Parameters to encode. Dict, list of tuples, str, bytes,
              file-like object, or any other type (passthrough).

    Returns:
        URL-encoded string for dict/list inputs, original value for passthrough types.
    """
    if isinstance(data, (str, bytes)):
        return data
    elif hasattr(data, "read"):
        return data
    elif hasattr(data, "__iter__"):
        result = []

        # Convert to key-val list (stdlib replacement for requests.utils.to_key_val_list)
        if hasattr(data, "items"):
            items = list(data.items())
        else:
            items = list(data)

        for k, vs in items:
            # Normalize scalar to list
            if isinstance(vs, str) or not hasattr(vs, "__iter__"):
                vs = [vs]

            for v in vs:
                if v is not None and not isinstance(v, dict):
                    # Simple key-value pair
                    result.append(
                        (
                            k.encode("utf-8") if isinstance(k, str) else k,
                            v.encode("utf-8") if isinstance(v, str) else v,
                        )
                    )
                elif v is not None:
                    # Array-of-objects: concatenate dict keys to param name
                    for k_inner, v_inner in v.items():
                        result.append(
                            (
                                (k + k_inner).encode("utf-8") if isinstance(k, str) else k_inner,
                                v_inner.encode("utf-8") if isinstance(v_inner, str) else v_inner,
                            )
                        )

        return urlencode(result, doseq=True)
    else:
        return data
