import logging
import os
from unittest.mock import MagicMock, patch

import pytest

import meraki
from meraki.exceptions import APIKeyError


class TestDashboardAPIInit:
    @patch("meraki.session.base.check_python_version")
    def test_api_key_from_param(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d._session._api_key == "test_key_1234567890123456789012345678901234567890"

    @patch("meraki.session.base.check_python_version")
    def test_api_key_from_env(self, mock_check):
        with patch.dict(
            os.environ,
            {"MERAKI_DASHBOARD_API_KEY": "env_key_12345678901234567890123456789012345678"},
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

    @patch("meraki.session.base.check_python_version")
    def test_suppress_logging_sets_none(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is None

    @patch("meraki.session.base.check_python_version")
    def test_simulate_mode_propagates(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            simulate=True,
            caller="TestApp TestVendor",
        )
        assert d._session._simulate is True

    @patch("meraki.session.base.check_python_version")
    def test_custom_base_url(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            base_url="https://api.meraki.cn/api/v1",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d._session._base_url == "https://api.meraki.cn/api/v1"

    @patch("meraki.session.base.check_python_version")
    def test_maximum_retries_propagates(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            maximum_retries=10,
            caller="TestApp TestVendor",
        )
        assert d._session._maximum_retries == 10

    @patch("meraki.session.base.check_python_version")
    def test_use_iterator_propagates(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            use_iterator_for_get_pages=True,
            caller="TestApp TestVendor",
        )
        assert d._session.use_iterator_for_get_pages is True

    @patch("meraki.session.base.check_python_version")
    def test_use_iterator_default_false_propagates(self, mock_check):
        # Regression for removed dead self-assignment
        # `use_iterator_for_get_pages = use_iterator_for_get_pages`: param
        # must still reach the session unchanged.
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            use_iterator_for_get_pages=False,
            caller="TestApp TestVendor",
        )
        assert d._session.use_iterator_for_get_pages is False

    @patch("meraki.session.base.check_python_version")
    def test_inherit_logging_config_param_takes_effect(self, mock_check):
        # Regression for removed dead self-assignment
        # `inherit_logging_config = inherit_logging_config`: passing True must
        # leave the logger at its inherited (non-DEBUG-forced) level.
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is not None
        d._logger.handlers.clear()

    @patch("meraki.session.base.check_python_version")
    def test_caller_from_env(self, mock_check):
        with patch.dict(os.environ, {"MERAKI_PYTHON_SDK_CALLER": "EnvApp EnvVendor"}):
            d = meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )
        assert "EnvApp EnvVendor" in d._session._client.headers["User-Agent"]

    @patch("meraki.session.base.check_python_version")
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

    @patch("meraki.session.base.check_python_version")
    def test_be_geo_id_from_env(self, mock_check):
        with patch.dict(os.environ, {"BE_GEO_ID": "GeoApp V1"}):
            d = meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )
        assert "GeoApp V1" in d._session._client.headers["User-Agent"]

    @patch("meraki.session.base.check_python_version")
    def test_batch_initialized(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d.batch is not None

    @patch("meraki.session.base.check_python_version")
    def test_all_additional_sections(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d.administered is not None
        assert d.camera is not None
        assert d.cellularGateway is not None
        assert d.insight is not None
        assert d.licensing is not None
        assert d.sensor is not None
        assert d.sm is not None
        assert d.switch is not None
        assert d.spaces is not None
        assert d.wirelessController is not None
        assert d.campusGateway is not None


class TestDashboardAPILogging:
    @patch("meraki.session.base.check_python_version")
    def test_inherit_logging_config(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=False,
            inherit_logging_config=True,
            caller="TestApp TestVendor",
        )
        assert d._logger is not None
        assert d._logger.name == "meraki"

    @patch("meraki.session.base.check_python_version")
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
        d._logger.handlers.clear()

    @patch("meraki.session.base.check_python_version")
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

    @patch("meraki.session.base.check_python_version")
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

    @patch("meraki.session.base.check_python_version")
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

    @patch("meraki.session.base.check_python_version")
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


class TestDashboardAPILoggingHandlers:
    @patch("meraki.session.base.check_python_version")
    def test_handlers_added_when_no_existing_handlers(self, mock_check, tmp_path):
        with patch("meraki.__init__.logging.getLogger") as mock_get_logger:
            mock_logger = MagicMock()
            mock_logger.hasHandlers.return_value = False
            mock_get_logger.return_value = mock_logger
            meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=False,
                inherit_logging_config=False,
                output_log=True,
                log_path=str(tmp_path),
                log_file_prefix="t",
                print_console=True,
                caller="TestApp TestVendor",
            )
        assert mock_logger.addHandler.call_count == 2

    @patch("meraki.session.base.check_python_version")
    def test_no_handlers_added_when_already_has_handlers(self, mock_check, tmp_path):
        with patch("meraki.__init__.logging.getLogger") as mock_get_logger:
            mock_logger = MagicMock()
            mock_logger.hasHandlers.return_value = True
            mock_get_logger.return_value = mock_logger
            meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=False,
                inherit_logging_config=False,
                output_log=True,
                log_path=str(tmp_path),
                log_file_prefix="t",
                print_console=True,
                caller="TestApp TestVendor",
            )
        assert mock_logger.addHandler.call_count == 0

    @patch("meraki.session.base.check_python_version")
    def test_console_only_handler_when_no_output_log(self, mock_check):
        with patch("meraki.__init__.logging.getLogger") as mock_get_logger:
            mock_logger = MagicMock()
            mock_logger.hasHandlers.return_value = False
            mock_get_logger.return_value = mock_logger
            meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=False,
                inherit_logging_config=False,
                output_log=False,
                print_console=True,
                caller="TestApp TestVendor",
            )
        assert mock_logger.addHandler.call_count == 1


class TestDashboardAPISmartLimiting:
    @patch("meraki.session.base.check_python_version")
    def test_smart_flow_enabled_by_default(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            caller="TestApp TestVendor",
        )
        assert d._session._smart_flow is not None

    @patch("meraki.session.base.check_python_version")
    def test_smart_flow_disabled_explicitly(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=False,
            caller="TestApp TestVendor",
        )
        assert d._session._smart_flow is None

    @patch("meraki.session.base.check_python_version")
    def test_smart_flow_creates_limiter(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            caller="TestApp TestVendor",
        )
        assert d._session._smart_flow is not None

    @patch("meraki.session.base.check_python_version")
    def test_smart_flow_with_cache_path(self, mock_check, tmp_path):
        cache_file = str(tmp_path / "test_cache.json")
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            smart_flow_cache_path=cache_file,
            caller="TestApp TestVendor",
        )
        assert d._session._smart_flow is not None


class TestDashboardAPIEagerLoad:
    @patch("meraki.session.base.check_python_version")
    def test_eager_load_populates_cache(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            caller="TestApp TestVendor",
        )
        mock_orgs = [{"id": "org_1"}, {"id": "org_2"}]
        mock_networks = [{"id": "N_1"}, {"id": "N_2"}]
        mock_devices = [{"serial": "QABC-1234-5678"}, {"serial": "QDEF-5678-9012"}]

        with patch.object(d.organizations, "getOrganizations", return_value=mock_orgs):
            with patch.object(d.organizations, "getOrganizationNetworks", return_value=mock_networks):
                with patch.object(d.organizations, "getOrganizationInventoryDevices", return_value=mock_devices):
                    d._eager_load_rate_limit_cache()

        limiter = d._session._smart_flow
        assert limiter.resolve_org("/organizations/org_1/x") == "org_1"
        assert limiter.resolve_org("/networks/N_1/x") is not None
        assert limiter.resolve_org("/devices/QABC-1234-5678/x") is not None

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_handles_org_failure(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            caller="TestApp TestVendor",
        )
        with patch.object(d.organizations, "getOrganizations", side_effect=Exception("API error")):
            d._eager_load_rate_limit_cache()

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_handles_network_failure(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            caller="TestApp TestVendor",
        )
        mock_orgs = [{"id": "org_1"}]
        with patch.object(d.organizations, "getOrganizations", return_value=mock_orgs):
            with patch.object(d.organizations, "getOrganizationNetworks", side_effect=Exception("net fail")):
                with patch.object(d.organizations, "getOrganizationInventoryDevices", return_value=[]):
                    d._eager_load_rate_limit_cache()
        assert d._session._smart_flow.resolve_org("/organizations/org_1/x") == "org_1"

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_handles_device_failure(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            caller="TestApp TestVendor",
        )
        mock_orgs = [{"id": "org_1"}]
        mock_networks = [{"id": "N_1"}]
        with patch.object(d.organizations, "getOrganizations", return_value=mock_orgs):
            with patch.object(d.organizations, "getOrganizationNetworks", return_value=mock_networks):
                with patch.object(d.organizations, "getOrganizationInventoryDevices", side_effect=Exception("dev fail")):
                    d._eager_load_rate_limit_cache()
        assert d._session._smart_flow.resolve_org("/networks/N_1/x") == "org_1"

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_skips_devices_without_serial(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="lazy",
            caller="TestApp TestVendor",
        )
        mock_orgs = [{"id": "org_1"}]
        mock_devices = [{"serial": "QABC-1234-5678"}, {"name": "no-serial-device"}]
        with patch.object(d.organizations, "getOrganizations", return_value=mock_orgs):
            with patch.object(d.organizations, "getOrganizationNetworks", return_value=[]):
                with patch.object(d.organizations, "getOrganizationInventoryDevices", return_value=mock_devices):
                    d._eager_load_rate_limit_cache()
        limiter = d._session._smart_flow
        assert limiter.resolve_org("/devices/QABC-1234-5678/x") == "org_1"

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_noop_without_limiter(self, mock_check):
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=False,
            caller="TestApp TestVendor",
        )
        d._eager_load_rate_limit_cache()

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_runs_during_init_when_cache_not_fresh(self, mock_check, tmp_path):
        cache_file = str(tmp_path / "nonexistent_cache.json")
        with patch("meraki.api.organizations.Organizations.getOrganizations", return_value=[]):
            meraki.DashboardAPI(
                "test_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
                smart_flow_enabled=True,
                smart_flow_cache_mode="eager",
                smart_flow_cache_path=cache_file,
                caller="TestApp TestVendor",
            )

    @patch("meraki.session.base.check_python_version")
    def test_eager_load_skipped_when_cache_fresh(self, mock_check, tmp_path):
        import json
        from datetime import datetime, timezone

        cache_file = tmp_path / "cache.json"
        cache_file.write_text(
            json.dumps(
                {
                    "saved_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "networks": [{"id": "N_cached", "organization": {"id": "org_cached"}}],
                    "devices": [],
                }
            )
        )
        d = meraki.DashboardAPI(
            "test_key_1234567890123456789012345678901234567890",
            suppress_logging=True,
            smart_flow_enabled=True,
            smart_flow_cache_mode="eager",
            smart_flow_cache_path=str(cache_file),
            caller="TestApp TestVendor",
        )
        assert d._session._smart_flow.resolve_org("/networks/N_cached/x") == "org_cached"
