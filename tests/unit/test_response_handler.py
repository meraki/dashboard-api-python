from unittest.mock import MagicMock

from meraki.response_handler import handle_3xx


class TestHandle3xx:
    def test_extracts_location_and_updates_base_url(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.com/api/v1"
        response = MagicMock()
        response.headers = {"Location": "https://n123.meraki.com/api/v1/organizations"}

        result = handle_3xx(session, response)

        assert result == "https://n123.meraki.com/api/v1/organizations"
        assert session._base_url == "https://n123.meraki.com/api/v1"

    def test_handles_china_domain(self):
        session = MagicMock()
        session._base_url = "https://api.meraki.cn/api/v1"
        response = MagicMock()
        response.headers = {"Location": "https://n456.meraki.cn/api/v1/networks"}

        result = handle_3xx(session, response)

        assert result == "https://n456.meraki.cn/api/v1/networks"
        assert session._base_url == "https://n456.meraki.cn/api/v1"
