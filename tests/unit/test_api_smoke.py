"""Smoke tests: all generated API modules import and instantiate."""

from unittest.mock import MagicMock, patch

import pytest


SYNC_API_CLASSES = [
    ("meraki.api.administered", "Administered"),
    ("meraki.api.appliance", "Appliance"),
    ("meraki.api.camera", "Camera"),
    ("meraki.api.campusGateway", "CampusGateway"),
    ("meraki.api.cellularGateway", "CellularGateway"),
    ("meraki.api.devices", "Devices"),
    ("meraki.api.insight", "Insight"),
    ("meraki.api.licensing", "Licensing"),
    ("meraki.api.networks", "Networks"),
    ("meraki.api.organizations", "Organizations"),
    ("meraki.api.sensor", "Sensor"),
    ("meraki.api.sm", "Sm"),
    ("meraki.api.spaces", "Spaces"),
    ("meraki.api.switch", "Switch"),
    ("meraki.api.wireless", "Wireless"),
    ("meraki.api.wirelessController", "WirelessController"),
]

ASYNC_API_CLASSES = [
    ("meraki.aio.api.administered", "AsyncAdministered"),
    ("meraki.aio.api.appliance", "AsyncAppliance"),
    ("meraki.aio.api.camera", "AsyncCamera"),
    ("meraki.aio.api.campusGateway", "AsyncCampusGateway"),
    ("meraki.aio.api.cellularGateway", "AsyncCellularGateway"),
    ("meraki.aio.api.devices", "AsyncDevices"),
    ("meraki.aio.api.insight", "AsyncInsight"),
    ("meraki.aio.api.licensing", "AsyncLicensing"),
    ("meraki.aio.api.networks", "AsyncNetworks"),
    ("meraki.aio.api.organizations", "AsyncOrganizations"),
    ("meraki.aio.api.sensor", "AsyncSensor"),
    ("meraki.aio.api.sm", "AsyncSm"),
    ("meraki.aio.api.spaces", "AsyncSpaces"),
    ("meraki.aio.api.switch", "AsyncSwitch"),
    ("meraki.aio.api.wireless", "AsyncWireless"),
    ("meraki.aio.api.wirelessController", "AsyncWirelessController"),
]


class TestSyncAPIModuleSmoke:
    @pytest.mark.parametrize("module_path,class_name", SYNC_API_CLASSES)
    def test_import_and_instantiate(self, module_path, class_name):
        """Each sync API class imports and instantiates with a mock session."""
        import importlib

        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        instance = cls(session=MagicMock())
        assert instance is not None


class TestAsyncAPIModuleSmoke:
    @pytest.mark.parametrize("module_path,class_name", ASYNC_API_CLASSES)
    def test_import_and_instantiate(self, module_path, class_name):
        """Each async API class imports and instantiates with a mock session."""
        import importlib

        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        instance = cls(session=MagicMock())
        assert instance is not None


class TestDashboardAPISectionsSmoke:
    def test_all_sync_sections_accessible(self):
        """DashboardAPI exposes all API sections after init."""
        with patch("meraki.session.base.check_python_version"):
            import meraki

            api = meraki.DashboardAPI(
                api_key="fake_key_1234567890123456789012345678901234567890",
                suppress_logging=True,
            )

        expected_sections = [
            "administered",
            "appliance",
            "camera",
            "campusGateway",
            "cellularGateway",
            "devices",
            "insight",
            "licensing",
            "networks",
            "organizations",
            "sensor",
            "sm",
            "spaces",
            "switch",
            "wireless",
            "wirelessController",
            "batch",
        ]
        for section in expected_sections:
            attr = getattr(api, section, None)
            assert attr is not None, f"DashboardAPI missing section: {section}"
