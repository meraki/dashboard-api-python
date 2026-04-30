import logging
import os
from unittest.mock import patch

import pytest

import meraki
from meraki.exceptions import APIKeyError


class TestDashboardAPIInit:
    @patch("meraki.rest_session.check_python_version")
    def test_api_key_from_param(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert (
            d._session._api_key == "test_key_1234567890123456789012345678901234567890"
        )

    @patch("meraki.rest_session.check_python_version")
    def test_api_key_from_env(self, mock_check):
        with patch.dict(
            os.environ,
            {
                "MERAKI_DASHBOARD_API_KEY": "env_key_12345678901234567890123456789012345678"
            },
        ):
            d = meraki.DashboardAPI(
                suppress_logging=True,
                caller="TestApp TestVendor",
            )
        assert d._session._api_key == "env_key_12345678901234567890123456789012345678"

    def test_missing_api_key_raises(self):
        with patch.dict(os.environ, {}, clear=True):
            os.environ.pop("MERAKI_DASHBOARD_API_KEY", None)
            with pytest.raises(APIKeyError):
                meraki.DashboardAPI(suppress_logging=True, caller="TestApp TestVendor")

    @patch("meraki.rest_session.check_python_version")
    def test_suppress_logging_sets_none(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is None

    @patch("meraki.rest_session.check_python_version")
    def test_simulate_mode_propagates(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            simulate=True,
            caller="TestApp TestVendor",
        )
        assert d._session._simulate is True

    @patch("meraki.rest_session.check_python_version")
    def test_custom_base_url(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            base_url="https://api.meraki.cn/api/v1",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d._session._base_url == "https://api.meraki.cn/api/v1"

    @patch("meraki.rest_session.check_python_version")
    def test_maximum_retries_propagates(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            maximum_retries=10,
            caller="TestApp TestVendor",
        )
        assert d._session._maximum_retries == 10

    @patch("meraki.rest_session.check_python_version")
    def test_use_iterator_propagates(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            use_iterator_for_get_pages=True,
            caller="TestApp TestVendor",
        )
        assert d._session.use_iterator_for_get_pages is True

    @patch("meraki.rest_session.check_python_version")
    def test_caller_from_env(self, mock_check):
        with patch.dict(os.environ, {"MERAKI_PYTHON_SDK_CALLER": "EnvApp EnvVendor"}):
            d = meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )
        assert "EnvApp EnvVendor" in d._session._req_session.headers["User-Agent"]

    @patch("meraki.rest_session.check_python_version")
    def test_all_api_sections_initialized(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d.organizations is not None
        assert d.networks is not None
        assert d.devices is not None
        assert d.appliance is not None
        assert d.wireless is not None


class TestDashboardAPILogging:
    @patch("meraki.rest_session.check_python_version")
    def test_inherit_logging_config(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is not None
        assert d._logger.name == "meraki"

    @patch("meraki.rest_session.check_python_version")
    def test_output_log_with_print_console(self, mock_check, tmp_path):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=False,
            output_log=True,
            log_path=str(tmp_path),
            log_file_prefix="test",
            print_console=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is not None
        assert d._logger.level == logging.DEBUG
        assert hasattr(d, "_log_file")
        assert "test_log__" in d._log_file
        # Clean up handlers to avoid pollution
        d._logger.handlers.clear()

    @patch("meraki.rest_session.check_python_version")
    def test_output_log_path_without_trailing_slash(self, mock_check, tmp_path):
        log_path = str(tmp_path).rstrip("/").rstrip("\\")
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=False,
            output_log=True,
            log_path=log_path,
            log_file_prefix="pfx",
            print_console=False,
            caller="TestApp TestVendor",
        )
        assert "/" in d._log_file or "\\" in d._log_file
        assert "pfx_log__" in d._log_file
        d._logger.handlers.clear()

    @patch("meraki.rest_session.check_python_version")
    def test_output_log_path_with_trailing_slash(self, mock_check, tmp_path):
        log_path = str(tmp_path) + "/"
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=False,
            output_log=True,
            log_path=log_path,
            log_file_prefix="pfx",
            print_console=False,
            caller="TestApp TestVendor",
        )
        assert "//" not in d._log_file.replace("\\", "/").replace("//", "/", 1)
        d._logger.handlers.clear()

    @patch("meraki.rest_session.check_python_version")
    def test_no_output_log_with_print_console(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=False,
            output_log=False,
            print_console=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is not None
        assert d._logger.level == logging.DEBUG
        d._logger.handlers.clear()

    @patch("meraki.rest_session.check_python_version")
    def test_no_output_log_no_print_console(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=False,
            output_log=False,
            print_console=False,
            caller="TestApp TestVendor",
        )
        assert d._logger is not None
        d._logger.handlers.clear()
