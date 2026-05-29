"""Tests for SessionBase ABC contract and behavior."""

import ast
import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from meraki.exceptions import APIError
from meraki.session.base import SessionBase
from tests.unit.conftest import make_metadata as _metadata


# ---------------------------------------------------------------------------
# Test helper: concrete subclass
# ---------------------------------------------------------------------------


class ConcreteSession(SessionBase):
    """Minimal concrete implementation for testing."""

    def __init__(self, **kwargs):
        self.sleeps: list[float] = []
        self._mock_response = kwargs.pop("mock_response", None)
        with patch("meraki.session.base.check_python_version"):
            super().__init__(**kwargs)

    def _send_request(self, method: str, url: str, **kwargs):
        return self._mock_response

    def _sleep(self, seconds: float) -> None:
        self.sleeps.append(seconds)

    def _transport_kwargs(self, kwargs):
        return kwargs


def _make_session(**overrides):
    """Factory with sensible defaults."""
    from tests.unit.conftest import DEFAULT_SESSION_KWARGS, FAKE_API_KEY

    defaults = {"logger": None, "api_key": FAKE_API_KEY, **DEFAULT_SESSION_KWARGS}
    defaults.update(overrides)
    return ConcreteSession(**defaults)


def _mock_response(
    status_code=200,
    json_data=None,
    reason_phrase="OK",
    headers=None,
    content=b'{"ok":true}',
):
    """Create a mock httpx-like response."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.reason_phrase = reason_phrase
    resp.headers = headers or {}
    resp.content = content
    if json_data is not None:
        resp.json.return_value = json_data
    else:
        try:
            resp.json.return_value = json.loads(content) if content.strip() else None
        except (json.JSONDecodeError, ValueError):
            resp.json.side_effect = ValueError("No JSON")
    return resp


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestABCEnforcement:
    def test_abc_enforcement(self):
        """SessionBase cannot be instantiated directly."""
        with pytest.raises(TypeError):
            SessionBase(
                logger=None,
                api_key="test_key_00000000000000000000000000000000000test",
                caller="TestApp TestVendor",
            )


class TestConfigStorage:
    def test_config_storage(self):
        """Constructor stores all config attributes."""
        session = _make_session()
        assert session._api_key == "fake_api_key_1234567890123456789012345678901234567890"
        assert session._base_url == "https://api.meraki.com/api/v1"
        assert session._maximum_retries == 3
        assert session._wait_on_rate_limit is True
        assert session._single_request_timeout == 60
        assert session._simulate is False
        assert session._retry_4xx_error is False


class TestBuildHeaders:
    def test_build_headers(self):
        """_build_headers produces correct Authorization, Content-Type, User-Agent."""
        session = _make_session()
        headers = session._build_headers()
        assert headers["Authorization"] == "Bearer fake_api_key_1234567890123456789012345678901234567890"
        assert headers["Content-Type"] == "application/json"
        assert "python-meraki/" in headers["User-Agent"]


class TestRequestSuccess:
    def test_request_success_dispatch(self):
        """200 response dispatches to _handle_success and returns response."""
        resp = _mock_response(status_code=200, content=b'{"data": 1}')
        session = _make_session(mock_response=resp)
        result = session.request(_metadata(), "GET", "/test")
        assert result is resp

    def test_request_success_with_page(self):
        """200 response with page metadata logs page counter."""
        logger = MagicMock()
        resp = _mock_response(status_code=200, content=b"[1,2,3]")
        session = _make_session(mock_response=resp, logger=logger)
        result = session.request(_metadata(page=2), "GET", "/test")
        assert result is resp


class TestRequestRateLimit:
    def test_request_rate_limit(self):
        """429 response triggers _handle_rate_limit with Retry-After."""
        resp_429 = _mock_response(
            status_code=429,
            reason_phrase="Too Many Requests",
            headers={"Retry-After": "3"},
            content=b"rate limited",
        )
        resp_200 = _mock_response(status_code=200, content=b'{"ok":true}')

        call_count = [0]
        original_429 = resp_429
        original_200 = resp_200

        def side_effect(method, url, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return original_429
            return original_200

        session = _make_session()
        session._send_request = side_effect
        result = session.request(_metadata(), "GET", "/test")
        assert result.status_code == 200
        assert 3 in session.sleeps


class TestRequestServerError:
    def test_request_server_error(self):
        """500 response triggers retry with 1s sleep."""
        resp_500 = _mock_response(status_code=500, reason_phrase="Internal Server Error", content=b"error")
        resp_200 = _mock_response(status_code=200, content=b'{"ok":true}')

        call_count = [0]

        def side_effect(method, url, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return resp_500
            return resp_200

        session = _make_session()
        session._send_request = side_effect
        result = session.request(_metadata(), "GET", "/test")
        assert result.status_code == 200
        assert 1 in session.sleeps


class TestRequestRedirect:
    def test_request_redirect(self):
        """301 response updates URL via _handle_redirect."""
        resp_301 = _mock_response(
            status_code=301,
            reason_phrase="Moved Permanently",
            headers={"Location": "https://n123.meraki.com/api/v1/test"},
            content=b"",
        )
        resp_200 = _mock_response(status_code=200, content=b'{"redirected":true}')

        call_count = [0]

        def side_effect(method, url, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return resp_301
            return resp_200

        session = _make_session()
        session._send_request = side_effect
        result = session.request(_metadata(), "GET", "/test")
        assert result.status_code == 200


class TestRetriesExhausted:
    def test_request_raises_apierror_when_retries_exhausted(self):
        """APIError raised after max retries on 500."""
        resp_500 = _mock_response(status_code=500, reason_phrase="ISE", content=b"err")
        session = _make_session(maximum_retries=1, mock_response=resp_500)
        with pytest.raises(APIError):
            session.request(_metadata(), "GET", "/test")


class TestClientErrorNetworkDelete:
    def test_handle_client_error_network_delete_concurrency(self):
        """Network delete concurrency error triggers retry with random wait."""
        resp_400 = _mock_response(
            status_code=400,
            reason_phrase="Bad Request",
            content=b'{"errors":["concurrent network deletion in progress"]}',
            json_data={"errors": ["concurrent network deletion in progress"]},
        )
        resp_200 = _mock_response(status_code=200, content=b'{"ok":true}')

        call_count = [0]

        def side_effect(method, url, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return resp_400
            return resp_200

        session = _make_session(network_delete_retry_wait_time=60)
        session._send_request = side_effect
        result = session.request(_metadata(operation="deleteNetwork"), "DELETE", "/test")
        assert result.status_code == 200
        assert len(session.sleeps) == 1
        assert 30 <= session.sleeps[0] <= 60


class TestClientErrorActionBatch:
    def test_handle_client_error_action_batch_concurrency(self):
        """Action batch concurrency error triggers retry."""
        resp_400 = _mock_response(
            status_code=400,
            reason_phrase="Bad Request",
            content=b'{"errors":["Currently executing batches. Try again later."]}',
            json_data={"errors": ["Currently executing batches. Try again later."]},
        )
        resp_200 = _mock_response(status_code=200, content=b'{"ok":true}')

        call_count = [0]

        def side_effect(method, url, **kwargs):
            call_count[0] += 1
            if call_count[0] == 1:
                return resp_400
            return resp_200

        session = _make_session(action_batch_retry_wait_time=5)
        session._send_request = side_effect
        result = session.request(_metadata(), "POST", "/test")
        assert result.status_code == 200
        assert 5 in session.sleeps


class TestSimulateMode:
    def test_simulate_mode_returns_none_for_non_get(self):
        """Simulate mode returns None for POST without calling _send_request."""
        session = _make_session(simulate=True)
        call_tracker = []
        session._send_request = lambda *a, **kw: call_tracker.append(1)
        result = session.request(_metadata(), "POST", "/test")
        assert result is None
        assert len(call_tracker) == 0

    def test_simulate_mode_allows_get(self):
        """Simulate mode still performs GET requests."""
        resp = _mock_response(status_code=200, content=b'{"data":1}')
        session = _make_session(simulate=True, mock_response=resp)
        result = session.request(_metadata(), "GET", "/test")
        assert result is resp


class TestComplexityAudit:
    def test_complexity_audit(self):
        """All handler methods have cyclomatic complexity under 10."""
        base_path = Path(__file__).resolve().parent.parent.parent / "meraki" / "session" / "base.py"
        source = base_path.read_text()
        tree = ast.parse(source)

        handler_methods = [
            "_handle_success",
            "_handle_redirect",
            "_handle_rate_limit",
            "_handle_server_error",
            "_handle_client_error",
        ]

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in handler_methods:
                complexity = _compute_complexity(node)
                assert complexity < 10, f"{node.name} has complexity {complexity} (must be < 10)"


class TestMerakiParamEncodingHelpers:
    """Fix #15: shared param-encoding helpers in base.py."""

    def test_detects_list_of_dict(self):
        from meraki.session.base import params_need_meraki_encoding

        assert params_need_meraki_encoding({"variables[]": [{"name": "n"}]}) is True

    def test_ignores_scalar_list(self):
        from meraki.session.base import params_need_meraki_encoding

        assert params_need_meraki_encoding({"networkIds[]": ["a", "b"]}) is False

    def test_ignores_scalars_and_non_dict(self):
        from meraki.session.base import params_need_meraki_encoding

        assert params_need_meraki_encoding({"perPage": 10}) is False
        assert params_need_meraki_encoding(None) is False
        assert params_need_meraki_encoding("a=b") is False

    def test_apply_folds_query_and_drops_params(self):
        from meraki.session.base import apply_meraki_param_encoding

        kwargs = {"params": {"variables[]": [{"name": "n1", "value": "v1"}]}}
        url = apply_meraki_param_encoding("https://x/api/v1/things", kwargs)
        assert "variables%5B%5Dname=n1" in url
        assert "variables%5B%5Dvalue=v1" in url
        assert url.count("?") == 1
        assert kwargs["params"] is None

    def test_apply_appends_with_ampersand_when_query_exists(self):
        from meraki.session.base import apply_meraki_param_encoding

        kwargs = {"params": {"variables[]": [{"name": "n1"}]}}
        url = apply_meraki_param_encoding("https://x/api/v1/things?foo=bar", kwargs)
        assert "?foo=bar&variables%5B%5Dname=n1" in url
        assert kwargs["params"] is None

    def test_apply_leaves_scalar_params_untouched(self):
        from meraki.session.base import apply_meraki_param_encoding

        kwargs = {"params": {"perPage": 10}}
        url = apply_meraki_param_encoding("https://x/api/v1/things", kwargs)
        assert url == "https://x/api/v1/things"
        assert kwargs["params"] == {"perPage": 10}


def _compute_complexity(func_node: ast.FunctionDef) -> int:
    """Approximate McCabe cyclomatic complexity: count decision points + 1."""
    complexity = 1
    for node in ast.walk(func_node):
        if isinstance(node, (ast.If, ast.IfExp)):
            complexity += 1
        elif isinstance(node, ast.For):
            complexity += 1
        elif isinstance(node, ast.While):
            complexity += 1
        elif isinstance(node, ast.ExceptHandler):
            complexity += 1
        elif isinstance(node, ast.BoolOp):
            # Each and/or adds a branch
            complexity += len(node.values) - 1
    return complexity
