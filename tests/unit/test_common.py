from unittest.mock import MagicMock, patch

import pytest

from meraki.common import (
    check_python_version,
    validate_user_agent,
    reject_v0_base_url,
    validate_base_url,
    iterator_for_get_pages_bool,
    use_iterator_for_get_pages_setter,
)
from meraki.exceptions import PythonVersionError, SessionInputError


class TestCheckPythonVersion:
    @patch("platform.python_version_tuple", return_value=("3", "11", "0"))
    def test_valid_version(self, mock_ver):
        check_python_version()

    @patch("platform.python_version_tuple", return_value=("3", "9", "0"))
    def test_too_old_raises(self, mock_ver):
        with pytest.raises(PythonVersionError):
            check_python_version()

    @patch("platform.python_version_tuple", return_value=("2", "7", "0"))
    def test_python2_raises(self, mock_ver):
        with pytest.raises(PythonVersionError):
            check_python_version()

    def test_check_python_version_valid_does_not_raise(self):
        """check_python_version should not raise on current interpreter (>=3.10)."""
        check_python_version()

    def test_check_python_version_rejects_39(self):
        """check_python_version raises PythonVersionError for 3.9."""
        with patch("platform.python_version_tuple", return_value=("3", "9", "0")):
            with pytest.raises(PythonVersionError):
                check_python_version()

    def test_check_python_version_accepts_310(self):
        """check_python_version accepts exactly 3.10.0 (minimum)."""
        with patch("platform.python_version_tuple", return_value=("3", "10", "0")):
            check_python_version()


class TestValidateUserAgent:
    def test_valid_caller(self):
        result = validate_user_agent("", "TestApp TestVendor")
        assert "TestApp TestVendor" in result
        assert result.startswith("Caller/(")

    def test_valid_caller_with_version(self):
        result = validate_user_agent("", "MyApp/1.0 MyVendor")
        assert "MyApp/1.0 MyVendor" in result

    def test_invalid_caller_raises(self):
        with pytest.raises(SessionInputError):
            validate_user_agent("", "invalid format!!!")

    def test_be_geo_id_fallback(self):
        result = validate_user_agent("GeoApp GeoVendor", "")
        assert "GeoApp GeoVendor" in result

    def test_invalid_be_geo_id_raises(self):
        with pytest.raises(SessionInputError):
            validate_user_agent("bad format!!!", "")

    def test_unidentified_when_both_empty(self):
        result = validate_user_agent("", "")
        assert "unidentified" in result


class TestRejectV0BaseUrl:
    def test_v0_exits(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.com/api/v0"
        with pytest.raises(SystemExit):
            reject_v0_base_url(session)

    def test_v1_ok(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.com/api/v1"
        reject_v0_base_url(session)

    def test_trailing_slash_stripped(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.com/api/v1/"
        reject_v0_base_url(session)
        assert session._base_url == "https://api.meraki.com/api/v1"

    def test_reject_v0_strips_trailing_slash(self):
        """reject_v0_base_url strips trailing slash from valid URLs."""
        obj = MagicMock()
        obj._base_url = "https://api.meraki.com/api/v1/"
        reject_v0_base_url(obj)
        assert obj._base_url == "https://api.meraki.com/api/v1"

    def test_reject_v0_leaves_valid_url_unchanged(self):
        """reject_v0_base_url leaves clean v1 URL untouched."""
        obj = MagicMock()
        obj._base_url = "https://api.meraki.com/api/v1"
        reject_v0_base_url(obj)
        assert obj._base_url == "https://api.meraki.com/api/v1"


class TestValidateBaseUrl:
    def test_absolute_meraki_url_passthrough(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.com/api/v1"
        result = validate_base_url(session, "https://n123.meraki.com/api/v1/orgs")
        assert result == "https://n123.meraki.com/api/v1/orgs"

    def test_relative_path_prepends_base(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.com/api/v1"
        result = validate_base_url(session, "/organizations")
        assert result == "https://api.meraki.com/api/v1/organizations"

    def test_china_domain(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.cn/api/v1"
        result = validate_base_url(session, "https://n1.meraki.cn/api/v1/x")
        assert result == "https://n1.meraki.cn/api/v1/x"

    def test_canada_domain(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.ca/api/v1"
        result = validate_base_url(session, "https://n1.meraki.ca/api/v1/x")
        assert result == "https://n1.meraki.ca/api/v1/x"

    def test_india_domain(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.in/api/v1"
        result = validate_base_url(session, "https://n1.meraki.in/api/v1/x")
        assert result == "https://n1.meraki.in/api/v1/x"

    def test_gov_domain(self):
        session = MagicMock()
        session._base_url = "https://api.gov-meraki.com/api/v1"
        result = validate_base_url(session, "https://n1.gov-meraki.com/api/v1/x")
        assert result == "https://n1.gov-meraki.com/api/v1/x"


class TestIteratorForGetPages:
    def test_getter(self):
        session = MagicMock()
        session._use_iterator_for_get_pages = True
        assert iterator_for_get_pages_bool(session) is True

    def test_setter_true_assigns_iterator(self):
        session = MagicMock()
        use_iterator_for_get_pages_setter(session, True)
        assert session.get_pages == session._get_pages_iterator
        assert session._use_iterator_for_get_pages is True

    def test_setter_false_assigns_legacy(self):
        session = MagicMock()
        use_iterator_for_get_pages_setter(session, False)
        assert session.get_pages == session._get_pages_legacy
        assert session._use_iterator_for_get_pages is False
