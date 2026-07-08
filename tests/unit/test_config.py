"""Verify config.py constants are sane and consumed correctly."""

from meraki import config


class TestConfigDefaults:
    def test_default_base_url_is_v1(self):
        assert "v1" in config.DEFAULT_BASE_URL
        assert config.DEFAULT_BASE_URL.startswith("https://")

    def test_alternate_urls_are_https(self):
        for url in [
            config.CANADA_BASE_URL,
            config.CHINA_BASE_URL,
            config.INDIA_BASE_URL,
            config.UNITED_STATES_FED_BASE_URL,
        ]:
            assert url.startswith("https://"), f"{url} is not HTTPS"
            assert "/api/v1" in url

    def test_timeout_is_positive(self):
        assert config.SINGLE_REQUEST_TIMEOUT > 0

    def test_maximum_retries_is_positive(self):
        assert config.MAXIMUM_RETRIES >= 1

    def test_retry_wait_times_are_positive(self):
        assert config.NGINX_429_RETRY_WAIT_TIME > 0
        assert config.ACTION_BATCH_RETRY_WAIT_TIME > 0
        assert config.NETWORK_DELETE_RETRY_WAIT_TIME > 0
        assert config.RETRY_4XX_ERROR_WAIT_TIME > 0

    def test_aio_max_concurrent_is_positive(self):
        assert config.AIO_MAXIMUM_CONCURRENT_REQUESTS >= 1

    def test_wait_on_rate_limit_defaults_true(self):
        assert config.WAIT_ON_RATE_LIMIT is True

    def test_simulate_defaults_false(self):
        assert config.SIMULATE_API_CALLS is False
