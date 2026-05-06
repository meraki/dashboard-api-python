from unittest.mock import MagicMock

import pytest

from meraki.exceptions import (
    APIKeyError,
    APIResponseError,
    APIError,
    AsyncAPIError,
    PythonVersionError,
    SessionInputError,
)


class TestAPIKeyError:
    def test_message(self):
        err = APIKeyError()
        assert "API key" in err.message

    def test_repr(self):
        err = APIKeyError()
        assert repr(err) == err.message

    def test_raises(self):
        with pytest.raises(APIKeyError):
            raise APIKeyError()


class TestAPIResponseError:
    def test_init(self):
        err = APIResponseError("RestSession", 503, "Connection timeout")
        assert err.obj_name == "RestSession"
        assert err.status_code == 503
        assert err.reason == "Connection timeout"

    def test_exc_message(self):
        err = APIResponseError("RestSession", 503, "timeout")
        msg = err.exc_message()
        assert "RestSession" in msg
        assert "503" in msg
        assert "timeout" in msg

    def test_json(self):
        err = APIResponseError("RestSession", 503, "timeout")
        j = err.json()
        assert j == {"error": "timeout", "status_code": 503}

    def test_str(self):
        err = APIResponseError("RestSession", 503, "timeout")
        assert str(err) == err.exc_message()


class TestAPIError:
    def _make_response(self, status_code=400, reason_phrase="Bad Request", json_data=None, content=b""):
        resp = MagicMock()
        resp.status_code = status_code
        resp.reason_phrase = reason_phrase
        resp.json.return_value = json_data or {"errors": ["something"]}
        resp.content = content
        return resp

    def test_basic_init(self):
        metadata = {"tags": ["networks"], "operation": "getNetworks"}
        resp = self._make_response()
        err = APIError(metadata, resp)
        assert err.tag == "networks"
        assert err.operation == "getNetworks"
        assert err.status == 400
        assert err.reason == "Bad Request"
        assert err.message == {"errors": ["something"]}

    def test_repr(self):
        metadata = {"tags": ["networks"], "operation": "getNetworks"}
        resp = self._make_response()
        err = APIError(metadata, resp)
        r = repr(err)
        assert "networks" in r
        assert "getNetworks" in r
        assert "400" in r

    def test_none_response_fields(self):
        metadata = {"tags": ["orgs"], "operation": "getOrgs"}
        resp = MagicMock()
        resp.status_code = None
        resp.reason_phrase = None
        resp.json.return_value = None
        err = APIError(metadata, resp)
        assert err.status is None
        assert err.reason is None
        assert err.message is None

    def test_json_decode_error_falls_back_to_content(self):
        metadata = {"tags": ["orgs"], "operation": "getOrgs"}
        resp = MagicMock()
        resp.status_code = 500
        resp.reason_phrase = "Server Error"
        resp.json.side_effect = ValueError("No JSON")
        resp.content = b"<html>Internal Server Error</html>"
        err = APIError(metadata, resp)
        assert "Internal Server Error" in err.message

    def test_404_appends_wait_message(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        resp = MagicMock()
        resp.status_code = 404
        resp.reason_phrase = "Not Found"
        resp.json.side_effect = ValueError("No JSON")
        resp.content = b"Not found here"
        err = APIError(metadata, resp)
        assert "please wait" in err.message

    def test_non_404_does_not_append_wait_message(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        resp = MagicMock()
        resp.status_code = 500
        resp.reason_phrase = "Server Error"
        resp.json.side_effect = ValueError("No JSON")
        resp.content = b"error text"
        err = APIError(metadata, resp)
        assert "please wait" not in err.message


class TestAsyncAPIError:
    def _make_response(self, status_code=400, reason_phrase="Bad Request"):
        resp = MagicMock()
        resp.status_code = status_code
        resp.reason_phrase = reason_phrase
        return resp

    def test_basic_init(self):
        metadata = {"tags": ["devices"], "operation": "getDevices"}
        resp = self._make_response()
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp, {"errors": ["fail"]})
        assert err.tag == "devices"
        assert err.operation == "getDevices"
        assert err.status == 400
        assert err.reason == "Bad Request"
        assert err.message == {"errors": ["fail"]}

    def test_repr(self):
        metadata = {"tags": ["devices"], "operation": "getDevices"}
        resp = self._make_response()
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp, "some error")
        r = repr(err)
        assert "devices" in r
        assert "400" in r

    def test_string_message_stripped(self):
        metadata = {"tags": ["orgs"], "operation": "getOrgs"}
        resp = self._make_response()
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp, "  spaces around  ")
        assert err.message == "spaces around"

    def test_404_appends_wait_message(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        resp = self._make_response(status_code=404, reason_phrase="Not Found")
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp, "resource missing")
        assert "please wait" in err.message

    def test_non_404_does_not_append_wait_message(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        resp = self._make_response(status_code=500, reason_phrase="Server Error")
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp, "server broke")
        assert "please wait" not in err.message

    def test_none_response(self):
        metadata = {"tags": ["orgs"], "operation": "getOrg"}
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, None, "no response")
        assert err.status is None
        assert err.reason is None

    def test_is_subclass_of_api_error(self):
        metadata = {"tags": ["devices"], "operation": "getDevices"}
        resp = self._make_response()
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp, "msg")
        assert isinstance(err, APIError)

    def test_emits_deprecation_warning(self):
        metadata = {"tags": ["devices"], "operation": "getDevices"}
        resp = self._make_response()
        with pytest.warns(DeprecationWarning, match="AsyncAPIError is deprecated"):
            AsyncAPIError(metadata, resp, {"errors": ["fail"]})

    def test_2arg_signature_delegates_to_parent(self):
        metadata = {"tags": ["networks"], "operation": "getNetworks"}
        resp = self._make_response()
        resp.json.return_value = {"errors": ["server failed"]}
        with pytest.warns(DeprecationWarning):
            err = AsyncAPIError(metadata, resp)
        assert err.message == {"errors": ["server failed"]}


class TestPythonVersionError:
    def test_message_preserved(self):
        err = PythonVersionError("Python too old")
        assert err.message == "Python too old"
        assert str(err) == "Python too old"


class TestSessionInputError:
    def test_fields(self):
        err = SessionInputError("CALLER", "bad!!!", "Format wrong", "https://docs.example.com")
        assert err.argument == "CALLER"
        assert err.value == "bad!!!"
        assert err.message == "Format wrong"
        assert err.doc_link == "https://docs.example.com"
        assert "Format wrong" in str(err)
        assert "https://docs.example.com" in str(err)

    def test_none_doc_link(self):
        err = SessionInputError("total_pages", "invalid", "must be int or 'all'", None)
        assert "None" in str(err)
