import pytest

import generate_library as gen


class TestDocsUrl:
    def test_simple(self):
        assert gen.docs_url("getOrganizations") == (
            "https://developer.cisco.com/meraki/api-v1/#!get-organizations"
        )

    def test_multi_camel_case(self):
        assert gen.docs_url("getNetworkApplianceFirewallL3FirewallRules") == (
            "https://developer.cisco.com/meraki/api-v1/#!"
            "get-network-appliance-firewall-l-3-firewall-rules"
        )

    def test_all_lowercase(self):
        assert gen.docs_url("lowercase") == (
            "https://developer.cisco.com/meraki/api-v1/#!lowercase"
        )


class TestGeneratePaginationParameters:
    def test_standard_operation(self):
        result = gen.generate_pagination_parameters("getOrganizationNetworks")
        assert "total_pages" in result
        assert "direction" in result
        assert "next" in result["direction"]["description"]
        assert "event_log_end_time" not in result

    def test_reverse_pagination_events(self):
        result = gen.generate_pagination_parameters("getNetworkEvents")
        assert "prev" in result["direction"]["description"]
        assert "event_log_end_time" in result

    def test_reverse_pagination_config_changes(self):
        result = gen.generate_pagination_parameters(
            "getOrganizationConfigurationChanges"
        )
        assert "prev" in result["direction"]["description"]
        assert "event_log_end_time" not in result


class TestReturnParams:
    @pytest.fixture
    def sample_params(self):
        return {
            "networkId": {
                "required": True,
                "in": "path",
                "type": "string",
                "description": "Network ID",
            },
            "perPage": {
                "required": False,
                "in": "query",
                "type": "integer",
                "description": "Per page",
            },
            "name": {
                "required": False,
                "in": "body",
                "type": "string",
                "description": "Name",
            },
            "tags": {
                "required": False,
                "in": "body",
                "type": "array",
                "description": "Tags",
            },
            "status": {
                "required": False,
                "in": "query",
                "type": "string",
                "description": "Status",
                "enum": ["online", "offline"],
            },
        }

    def test_no_filters_returns_all(self, sample_params):
        result = gen.return_params("someOp", sample_params, None)
        assert result == sample_params

    def test_required_filter(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["required"])
        assert "networkId" in result
        assert "perPage" not in result

    def test_path_filter(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["path"])
        assert list(result.keys()) == ["networkId"]

    def test_query_filter(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["query"])
        assert "perPage" in result
        assert "status" in result
        assert "name" not in result

    def test_body_filter(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["body"])
        assert "name" in result
        assert "tags" in result
        assert "networkId" not in result

    def test_array_filter(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["array"])
        assert list(result.keys()) == ["tags"]

    def test_enum_filter(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["enum"])
        assert list(result.keys()) == ["status"]

    def test_pagination_filter_with_perPage(self, sample_params):
        result = gen.return_params("someOp", sample_params, ["pagination"])
        assert "total_pages" in result
        assert "direction" in result


class TestUnpackParamWithSchema:
    def test_basic_schema(self):
        this_param = {
            "in": "body",
            "schema": {
                "properties": {
                    "name": {"type": "string", "description": "The name"},
                    "enabled": {"type": "boolean", "description": "Enable flag"},
                },
                "required": ["name"],
                "example": {"name": "test"},
            },
        }
        result = gen.unpack_param_with_schema({}, this_param)
        assert result["name"]["required"] is True
        assert result["name"]["in"] == "body"
        assert result["name"]["type"] == "string"
        assert result["name"]["example"] == "test"
        assert result["enabled"]["required"] is False

    def test_schema_with_enum(self):
        this_param = {
            "in": "body",
            "schema": {
                "properties": {
                    "mode": {
                        "type": "string",
                        "description": "Mode",
                        "enum": ["a", "b"],
                    },
                },
            },
        }
        result = gen.unpack_param_with_schema({}, this_param)
        assert result["mode"]["enum"] == ["a", "b"]


class TestUnpackParamWithoutSchema:
    def test_required_param(self):
        result = gen.unpack_param_without_schema(
            {},
            {"in": "path", "type": "string", "description": "The ID"},
            "networkId",
            True,
        )
        assert result["networkId"]["required"] is True
        assert result["networkId"]["in"] == "path"
        assert result["networkId"]["description"] == "The ID"

    def test_required_param_without_description(self):
        result = gen.unpack_param_without_schema(
            {},
            {"in": "query", "type": "integer"},
            "perPage",
            True,
        )
        assert result["perPage"]["description"] == "(required)"

    def test_enum_captured(self):
        result = gen.unpack_param_without_schema(
            {},
            {
                "in": "query",
                "type": "string",
                "description": "Sort order",
                "enum": ["asc", "desc"],
            },
            "sortOrder",
            False,
        )
        assert result["sortOrder"]["enum"] == ["asc", "desc"]


class TestParseParams:
    def test_none_parameters(self):
        assert gen.parse_params("someOp", None) == {}

    def test_empty_list(self):
        assert gen.parse_params("someOp", []) == {}

    def test_path_param(self):
        params = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            }
        ]
        result = gen.parse_params("someOp", params)
        assert "networkId" in result
        assert result["networkId"]["required"] is True


class TestParseGetParams:
    def test_with_pagination(self):
        parameters = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            },
            {
                "name": "perPage",
                "in": "query",
                "type": "integer",
                "required": False,
                "description": "Per page",
            },
            {
                "name": "startingAfter",
                "in": "query",
                "type": "string",
                "required": False,
                "description": "Starting after",
            },
        ]
        array_params, call_line, path_params, query_params = gen.parse_get_params(
            "getNetworkClients", parameters
        )
        assert "get_pages" in call_line
        assert "networkId" in path_params
        assert "perPage" in query_params

    def test_without_query_params(self):
        parameters = [
            {
                "name": "serial",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Serial",
            },
        ]
        array_params, call_line, path_params, query_params = gen.parse_get_params(
            "getDevice", parameters
        )
        assert call_line == "return self._session.get(metadata, resource)"

    def test_network_events_pagination(self):
        parameters = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            },
            {
                "name": "perPage",
                "in": "query",
                "type": "integer",
                "required": False,
                "description": "Per page",
            },
        ]
        _, call_line, _, _ = gen.parse_get_params("getNetworkEvents", parameters)
        assert "event_log_end_time" in call_line


class TestParsePostAndPutParams:
    def test_post_with_body(self):
        parameters = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            },
            {
                "name": "createBody",
                "in": "body",
                "schema": {
                    "properties": {"name": {"type": "string", "description": "Name"}},
                },
            },
        ]
        body_params, call_line, path_params = gen.parse_post_and_put_params(
            "post", "createNetwork", parameters
        )
        assert "post" in call_line
        assert "payload" in call_line
        assert "name" in body_params

    def test_put_without_body(self):
        parameters = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            },
        ]
        body_params, call_line, path_params = gen.parse_post_and_put_params(
            "put", "updateThing", parameters
        )
        assert "payload" not in call_line


class TestParseDeleteParams:
    def test_simple_delete(self):
        parameters = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            },
        ]
        call_line, path_params, query_params = gen.parse_delete_params(
            "deleteNetwork", parameters
        )
        assert call_line == "return self._session.delete(metadata, resource)"
        assert "networkId" in path_params

    def test_delete_with_query_params(self):
        parameters = [
            {
                "name": "networkId",
                "in": "path",
                "type": "string",
                "required": True,
                "description": "Network ID",
            },
            {
                "name": "force",
                "in": "query",
                "type": "boolean",
                "required": False,
                "description": "Force delete",
            },
        ]
        call_line, path_params, query_params = gen.parse_delete_params(
            "deleteNetwork", parameters
        )
        assert "params" in call_line
        assert "force" in query_params
