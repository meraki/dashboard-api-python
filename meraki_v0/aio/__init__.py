from datetime import datetime
import logging
import os

from meraki_v0.aio.rest_session import *
from meraki_v0.aio.api.api_usage import AsyncAPIUsage
from meraki_v0.aio.api.action_batches import AsyncActionBatches
from meraki_v0.aio.api.admins import AsyncAdmins
from meraki_v0.aio.api.alert_settings import AsyncAlertSettings
from meraki_v0.aio.api.bluetooth_clients import AsyncBluetoothClients
from meraki_v0.aio.api.bluetooth_settings import AsyncBluetoothSettings
from meraki_v0.aio.api.camera_quality_retention_profiles import AsyncCameraQualityRetentionProfiles
from meraki_v0.aio.api.cameras import AsyncCameras
from meraki_v0.aio.api.change_log import AsyncChangeLog
from meraki_v0.aio.api.clients import AsyncClients
from meraki_v0.aio.api.config_templates import AsyncConfigTemplates
from meraki_v0.aio.api.connectivity_monitoring_destinations import AsyncConnectivityMonitoringDestinations
from meraki_v0.aio.api.content_filtering_categories import AsyncContentFilteringCategories
from meraki_v0.aio.api.content_filtering_rules import AsyncContentFilteringRules
from meraki_v0.aio.api.dashboard_branding_policies import AsyncDashboardBrandingPolicies
from meraki_v0.aio.api.devices import AsyncDevices
from meraki_v0.aio.api.events import AsyncEvents
from meraki_v0.aio.api.firewalled_services import AsyncFirewalledServices
from meraki_v0.aio.api.floor_plans import AsyncFloorPlans
from meraki_v0.aio.api.group_policies import AsyncGroupPolicies
from meraki_v0.aio.api.http_servers import AsyncHTTPServers
from meraki_v0.aio.api.intrusion_settings import AsyncIntrusionSettings
from meraki_v0.aio.api.licenses import AsyncLicenses
from meraki_v0.aio.api.link_aggregations import AsyncLinkAggregations
from meraki_v0.aio.api.mg_dhcp_settings import AsyncMGDHCPSettings
from meraki_v0.aio.api.mg_lan_settings import AsyncMGLANSettings
from meraki_v0.aio.api.mg_connectivity_monitoring_destinations import AsyncMGConnectivityMonitoringDestinations
from meraki_v0.aio.api.mg_port_forwarding_rules import AsyncMGPortForwardingRules
from meraki_v0.aio.api.mg_subnet_pool_settings import AsyncMGSubnetPoolSettings
from meraki_v0.aio.api.mg_uplink_settings import AsyncMGUplinkSettings
from meraki_v0.aio.api.mr_l3_firewall import AsyncMRL3Firewall
from meraki_v0.aio.api.mv_sense import AsyncMVSense
from meraki_v0.aio.api.mx_1_1_nat_rules import AsyncMX11NATRules
from meraki_v0.aio.api.mx_1_many_nat_rules import AsyncMX1ManyNATRules
from meraki_v0.aio.api.mx_l3_firewall import AsyncMXL3Firewall
from meraki_v0.aio.api.mx_l7_application_categories import AsyncMXL7ApplicationCategories
from meraki_v0.aio.api.mx_l7_firewall import AsyncMXL7Firewall
from meraki_v0.aio.api.mx_vlan_ports import AsyncMXVLANPorts
from meraki_v0.aio.api.mx_vpn_firewall import AsyncMXVPNFirewall
from meraki_v0.aio.api.mx_cellular_firewall import AsyncMXCellularFirewall
from meraki_v0.aio.api.mx_inbound_firewall import AsyncMXInboundFirewall
from meraki_v0.aio.api.mx_port_forwarding_rules import AsyncMXPortForwardingRules
from meraki_v0.aio.api.mx_static_routes import AsyncMXStaticRoutes
from meraki_v0.aio.api.mx_warm_spare_settings import AsyncMXWarmSpareSettings
from meraki_v0.aio.api.malware_settings import AsyncMalwareSettings
from meraki_v0.aio.api.management_interface_settings import AsyncManagementInterfaceSettings
from meraki_v0.aio.api.meraki_auth_users import AsyncMerakiAuthUsers
from meraki_v0.aio.api.monitored_media_servers import AsyncMonitoredMediaServers
from meraki_v0.aio.api.named_tag_scope import AsyncNamedTagScope
from meraki_v0.aio.api.netflow_settings import AsyncNetFlowSettings
from meraki_v0.aio.api.networks import AsyncNetworks
from meraki_v0.aio.api.openapi_spec import AsyncOpenAPISpec
from meraki_v0.aio.api.organizations import AsyncOrganizations
from meraki_v0.aio.api.pii import AsyncPII
from meraki_v0.aio.api.radio_settings import AsyncRadioSettings
from meraki_v0.aio.api.saml_roles import AsyncSAMLRoles
from meraki_v0.aio.api.sm import AsyncSM
from meraki_v0.aio.api.snmp_settings import AsyncSNMPSettings
from meraki_v0.aio.api.ssids import AsyncSSIDs
from meraki_v0.aio.api.security_events import AsyncSecurityEvents
from meraki_v0.aio.api.splash_login_attempts import AsyncSplashLoginAttempts
from meraki_v0.aio.api.splash_settings import AsyncSplashSettings
from meraki_v0.aio.api.switch_acls import AsyncSwitchACLs
from meraki_v0.aio.api.switch_port_schedules import AsyncSwitchPortSchedules
from meraki_v0.aio.api.switch_ports import AsyncSwitchPorts
from meraki_v0.aio.api.switch_profiles import AsyncSwitchProfiles
from meraki_v0.aio.api.switch_settings import AsyncSwitchSettings
from meraki_v0.aio.api.switch_stacks import AsyncSwitchStacks
from meraki_v0.aio.api.syslog_servers import AsyncSyslogServers
from meraki_v0.aio.api.traffic_analysis_settings import AsyncTrafficAnalysisSettings
from meraki_v0.aio.api.traffic_shaping import AsyncTrafficShaping
from meraki_v0.aio.api.uplink_settings import AsyncUplinkSettings
from meraki_v0.aio.api.vlans import AsyncVLANs
from meraki_v0.aio.api.webhook_logs import AsyncWebhookLogs
from meraki_v0.aio.api.wireless_health import AsyncWirelessHealth
from meraki_v0.aio.api.wireless_settings import AsyncWirelessSettings
from meraki_v0.config import (
    API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, SINGLE_REQUEST_TIMEOUT, CERTIFICATE_PATH, REQUESTS_PROXY,
    WAIT_ON_RATE_LIMIT, NGINX_429_RETRY_WAIT_TIME, ACTION_BATCH_RETRY_WAIT_TIME, RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME, MAXIMUM_RETRIES, OUTPUT_LOG, LOG_PATH, LOG_FILE_PREFIX, PRINT_TO_CONSOLE,
    SUPPRESS_LOGGING, SIMULATE_API_CALLS, AIO_MAXIMUM_CONCURRENT_REQUESTS, BE_GEO_ID, MERAKI_PYTHON_SDK_CALLER
)


class AsyncDashboardAPI:
    """
    **Creates a persistent Meraki dashboard API session**

    - api_key (string): API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY
    - base_url (string): preceding all endpoint resources
    - single_request_timeout (integer): maximum number of seconds for each API call
    - certificate_path (string): path for TLS/SSL certificate verification if behind local proxy
    - requests_proxy (string): proxy server and port, if needed, for HTTPS
    - wait_on_rate_limit (boolean): retry if 429 rate limit error encountered?
    - nginx_429_retry_wait_time (integer): Nginx 429 retry wait time
    - action_batch_retry_wait_time (integer): action batch concurrency error retry wait time
    - retry_4xx_error (boolean): retry if encountering other 4XX error (besides 429)?
    - retry_4xx_error_wait_time (integer): other 4XX error retry wait time
    - maximum_retries (integer): retry up to this many times when encountering 429s or other server-side errors
    - output_log (boolean): create an output log file?
    - log_path (string): path to output log; by default, working directory of script if not specified
    - log_file_prefix (string): log file name appended with date and timestamp
    - print_console (boolean): print logging output to console?
    - suppress_logging (boolean): disable all logging? you're on your own then!
    - simulate (boolean): simulate POST/PUT/DELETE calls to prevent changes?
    - maximum_concurrent_requests (integer): number of concurrent API requests for asynchronous class
    - be_geo_id (string): optional partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID
    - caller (string): optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER
    """

    def __init__(self, api_key=None, base_url=DEFAULT_BASE_URL, single_request_timeout=SINGLE_REQUEST_TIMEOUT,
                 certificate_path=CERTIFICATE_PATH, requests_proxy=REQUESTS_PROXY,
                 wait_on_rate_limit=WAIT_ON_RATE_LIMIT, nginx_429_retry_wait_time=NGINX_429_RETRY_WAIT_TIME,
                 action_batch_retry_wait_time=ACTION_BATCH_RETRY_WAIT_TIME, retry_4xx_error=RETRY_4XX_ERROR,
                 retry_4xx_error_wait_time=RETRY_4XX_ERROR_WAIT_TIME, maximum_retries=MAXIMUM_RETRIES,
                 output_log=OUTPUT_LOG, log_path=LOG_PATH, log_file_prefix=LOG_FILE_PREFIX,
                 print_console=PRINT_TO_CONSOLE, suppress_logging=SUPPRESS_LOGGING, simulate=SIMULATE_API_CALLS,
                 maximum_concurrent_requests=AIO_MAXIMUM_CONCURRENT_REQUESTS, be_geo_id=BE_GEO_ID, caller=MERAKI_PYTHON_SDK_CALLER):
        # Check API key
        api_key = api_key or os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
        if not api_key:
            raise APIKeyError()

        # Pull the BE GEO ID from an environment variable if present
        be_geo_id = be_geo_id or os.environ.get('BE_GEO_ID')

        # Pull the caller from an environment variable if present
        caller = caller or os.environ.get('MERAKI_PYTHON_SDK_CALLER')

        # Configure logging
        if not suppress_logging:
            self._logger = logging.getLogger(__name__)
            self._logger.setLevel(logging.DEBUG)

            formatter = logging.Formatter(
                fmt='%(name)12s: %(levelname)8s > %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            if log_path and log_path[-1] != '/':
                log_path += '/'
            self._log_file = f'{log_path}{log_file_prefix}_log__{datetime.now():%Y-%m-%d_%H-%M-%S}.log'

            handler_console = logging.StreamHandler()
            handler_log = logging.FileHandler(
                filename=self._log_file
            )

            handler_console.setFormatter(formatter)
            handler_log.setFormatter(formatter)

            if output_log and not self._logger.hasHandlers():
                self._logger.addHandler(handler_log)
                if print_console:
                    handler_console.setLevel(logging.INFO)
                    self._logger.addHandler(handler_console)
            elif print_console and not self._logger.hasHandlers():
                self._logger.addHandler(handler_console)
        else:
            self._logger = None

        # Creates the API session
        self._session = AsyncRestSession(
            logger=self._logger,
            api_key=api_key,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            certificate_path=certificate_path,
            requests_proxy=requests_proxy,
            wait_on_rate_limit=wait_on_rate_limit,
            nginx_429_retry_wait_time=nginx_429_retry_wait_time,
            action_batch_retry_wait_time=action_batch_retry_wait_time,
            retry_4xx_error=retry_4xx_error,
            retry_4xx_error_wait_time=retry_4xx_error_wait_time,
            maximum_retries=maximum_retries,
            simulate=simulate,
            maximum_concurrent_requests=maximum_concurrent_requests,
            be_geo_id=be_geo_id,
            caller=caller,
        )

        # API endpoints by section
        self.api_usage = AsyncAPIUsage(self._session)
        self.action_batches = AsyncActionBatches(self._session)
        self.admins = AsyncAdmins(self._session)
        self.alert_settings = AsyncAlertSettings(self._session)
        self.bluetooth_clients = AsyncBluetoothClients(self._session)
        self.bluetooth_settings = AsyncBluetoothSettings(self._session)
        self.camera_quality_retention_profiles = AsyncCameraQualityRetentionProfiles(self._session)
        self.cameras = AsyncCameras(self._session)
        self.change_log = AsyncChangeLog(self._session)
        self.clients = AsyncClients(self._session)
        self.config_templates = AsyncConfigTemplates(self._session)
        self.connectivity_monitoring_destinations = AsyncConnectivityMonitoringDestinations(self._session)
        self.content_filtering_categories = AsyncContentFilteringCategories(self._session)
        self.content_filtering_rules = AsyncContentFilteringRules(self._session)
        self.dashboard_branding_policies = AsyncDashboardBrandingPolicies(self._session)
        self.devices = AsyncDevices(self._session)
        self.events = AsyncEvents(self._session)
        self.firewalled_services = AsyncFirewalledServices(self._session)
        self.floor_plans = AsyncFloorPlans(self._session)
        self.group_policies = AsyncGroupPolicies(self._session)
        self.http_servers = AsyncHTTPServers(self._session)
        self.intrusion_settings = AsyncIntrusionSettings(self._session)
        self.licenses = AsyncLicenses(self._session)
        self.link_aggregations = AsyncLinkAggregations(self._session)
        self.mg_dhcp_settings = AsyncMGDHCPSettings(self._session)
        self.mg_lan_settings = AsyncMGLANSettings(self._session)
        self.mg_connectivity_monitoring_destinations = AsyncMGConnectivityMonitoringDestinations(self._session)
        self.mg_port_forwarding_rules = AsyncMGPortForwardingRules(self._session)
        self.mg_subnet_pool_settings = AsyncMGSubnetPoolSettings(self._session)
        self.mg_uplink_settings = AsyncMGUplinkSettings(self._session)
        self.mr_l3_firewall = AsyncMRL3Firewall(self._session)
        self.mv_sense = AsyncMVSense(self._session)
        self.mx_1_1_nat_rules = AsyncMX11NATRules(self._session)
        self.mx_1_many_nat_rules = AsyncMX1ManyNATRules(self._session)
        self.mx_l3_firewall = AsyncMXL3Firewall(self._session)
        self.mx_l7_application_categories = AsyncMXL7ApplicationCategories(self._session)
        self.mx_l7_firewall = AsyncMXL7Firewall(self._session)
        self.mx_vlan_ports = AsyncMXVLANPorts(self._session)
        self.mx_vpn_firewall = AsyncMXVPNFirewall(self._session)
        self.mx_cellular_firewall = AsyncMXCellularFirewall(self._session)
        self.mx_inbound_firewall = AsyncMXInboundFirewall(self._session)
        self.mx_port_forwarding_rules = AsyncMXPortForwardingRules(self._session)
        self.mx_static_routes = AsyncMXStaticRoutes(self._session)
        self.mx_warm_spare_settings = AsyncMXWarmSpareSettings(self._session)
        self.malware_settings = AsyncMalwareSettings(self._session)
        self.management_interface_settings = AsyncManagementInterfaceSettings(self._session)
        self.meraki_auth_users = AsyncMerakiAuthUsers(self._session)
        self.monitored_media_servers = AsyncMonitoredMediaServers(self._session)
        self.named_tag_scope = AsyncNamedTagScope(self._session)
        self.netflow_settings = AsyncNetFlowSettings(self._session)
        self.networks = AsyncNetworks(self._session)
        self.openapi_spec = AsyncOpenAPISpec(self._session)
        self.organizations = AsyncOrganizations(self._session)
        self.pii = AsyncPII(self._session)
        self.radio_settings = AsyncRadioSettings(self._session)
        self.saml_roles = AsyncSAMLRoles(self._session)
        self.sm = AsyncSM(self._session)
        self.snmp_settings = AsyncSNMPSettings(self._session)
        self.ssids = AsyncSSIDs(self._session)
        self.security_events = AsyncSecurityEvents(self._session)
        self.splash_login_attempts = AsyncSplashLoginAttempts(self._session)
        self.splash_settings = AsyncSplashSettings(self._session)
        self.switch_acls = AsyncSwitchACLs(self._session)
        self.switch_port_schedules = AsyncSwitchPortSchedules(self._session)
        self.switch_ports = AsyncSwitchPorts(self._session)
        self.switch_profiles = AsyncSwitchProfiles(self._session)
        self.switch_settings = AsyncSwitchSettings(self._session)
        self.switch_stacks = AsyncSwitchStacks(self._session)
        self.syslog_servers = AsyncSyslogServers(self._session)
        self.traffic_analysis_settings = AsyncTrafficAnalysisSettings(self._session)
        self.traffic_shaping = AsyncTrafficShaping(self._session)
        self.uplink_settings = AsyncUplinkSettings(self._session)
        self.vlans = AsyncVLANs(self._session)
        self.webhook_logs = AsyncWebhookLogs(self._session)
        self.wireless_health = AsyncWirelessHealth(self._session)
        self.wireless_settings = AsyncWirelessSettings(self._session)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._session.close()
