from datetime import datetime
import logging
import os

from meraki_v0.legacy import *
from meraki_v0.rest_session import *
from meraki_v0.api.api_usage import APIUsage
from meraki_v0.api.action_batches import ActionBatches
from meraki_v0.api.admins import Admins
from meraki_v0.api.alert_settings import AlertSettings
from meraki_v0.api.bluetooth_clients import BluetoothClients
from meraki_v0.api.bluetooth_settings import BluetoothSettings
from meraki_v0.api.camera_quality_retention_profiles import CameraQualityRetentionProfiles
from meraki_v0.api.cameras import Cameras
from meraki_v0.api.change_log import ChangeLog
from meraki_v0.api.clients import Clients
from meraki_v0.api.config_templates import ConfigTemplates
from meraki_v0.api.connectivity_monitoring_destinations import ConnectivityMonitoringDestinations
from meraki_v0.api.content_filtering_categories import ContentFilteringCategories
from meraki_v0.api.content_filtering_rules import ContentFilteringRules
from meraki_v0.api.dashboard_branding_policies import DashboardBrandingPolicies
from meraki_v0.api.devices import Devices
from meraki_v0.api.events import Events
from meraki_v0.api.firewalled_services import FirewalledServices
from meraki_v0.api.floor_plans import FloorPlans
from meraki_v0.api.group_policies import GroupPolicies
from meraki_v0.api.http_servers import HTTPServers
from meraki_v0.api.intrusion_settings import IntrusionSettings
from meraki_v0.api.licenses import Licenses
from meraki_v0.api.link_aggregations import LinkAggregations
from meraki_v0.api.mg_dhcp_settings import MGDHCPSettings
from meraki_v0.api.mg_lan_settings import MGLANSettings
from meraki_v0.api.mg_connectivity_monitoring_destinations import MGConnectivityMonitoringDestinations
from meraki_v0.api.mg_port_forwarding_rules import MGPortForwardingRules
from meraki_v0.api.mg_subnet_pool_settings import MGSubnetPoolSettings
from meraki_v0.api.mg_uplink_settings import MGUplinkSettings
from meraki_v0.api.mr_l3_firewall import MRL3Firewall
from meraki_v0.api.mv_sense import MVSense
from meraki_v0.api.mx_1_1_nat_rules import MX11NATRules
from meraki_v0.api.mx_1_many_nat_rules import MX1ManyNATRules
from meraki_v0.api.mx_l3_firewall import MXL3Firewall
from meraki_v0.api.mx_l7_application_categories import MXL7ApplicationCategories
from meraki_v0.api.mx_l7_firewall import MXL7Firewall
from meraki_v0.api.mx_vlan_ports import MXVLANPorts
from meraki_v0.api.mx_vpn_firewall import MXVPNFirewall
from meraki_v0.api.mx_cellular_firewall import MXCellularFirewall
from meraki_v0.api.mx_inbound_firewall import MXInboundFirewall
from meraki_v0.api.mx_port_forwarding_rules import MXPortForwardingRules
from meraki_v0.api.mx_static_routes import MXStaticRoutes
from meraki_v0.api.mx_warm_spare_settings import MXWarmSpareSettings
from meraki_v0.api.malware_settings import MalwareSettings
from meraki_v0.api.management_interface_settings import ManagementInterfaceSettings
from meraki_v0.api.meraki_auth_users import MerakiAuthUsers
from meraki_v0.api.monitored_media_servers import MonitoredMediaServers
from meraki_v0.api.named_tag_scope import NamedTagScope
from meraki_v0.api.netflow_settings import NetFlowSettings
from meraki_v0.api.networks import Networks
from meraki_v0.api.openapi_spec import OpenAPISpec
from meraki_v0.api.organizations import Organizations
from meraki_v0.api.pii import PII
from meraki_v0.api.radio_settings import RadioSettings
from meraki_v0.api.saml_roles import SAMLRoles
from meraki_v0.api.sm import SM
from meraki_v0.api.snmp_settings import SNMPSettings
from meraki_v0.api.ssids import SSIDs
from meraki_v0.api.security_events import SecurityEvents
from meraki_v0.api.splash_login_attempts import SplashLoginAttempts
from meraki_v0.api.splash_settings import SplashSettings
from meraki_v0.api.switch_acls import SwitchACLs
from meraki_v0.api.switch_port_schedules import SwitchPortSchedules
from meraki_v0.api.switch_ports import SwitchPorts
from meraki_v0.api.switch_profiles import SwitchProfiles
from meraki_v0.api.switch_settings import SwitchSettings
from meraki_v0.api.switch_stacks import SwitchStacks
from meraki_v0.api.syslog_servers import SyslogServers
from meraki_v0.api.traffic_analysis_settings import TrafficAnalysisSettings
from meraki_v0.api.traffic_shaping import TrafficShaping
from meraki_v0.api.uplink_settings import UplinkSettings
from meraki_v0.api.vlans import VLANs
from meraki_v0.api.webhook_logs import WebhookLogs
from meraki_v0.api.wireless_health import WirelessHealth
from meraki_v0.api.wireless_settings import WirelessSettings
from meraki_v0.config import (
    API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, SINGLE_REQUEST_TIMEOUT, CERTIFICATE_PATH, REQUESTS_PROXY,
    WAIT_ON_RATE_LIMIT, NGINX_429_RETRY_WAIT_TIME, ACTION_BATCH_RETRY_WAIT_TIME, RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME, MAXIMUM_RETRIES, OUTPUT_LOG, LOG_PATH, LOG_FILE_PREFIX, PRINT_TO_CONSOLE,
    SUPPRESS_LOGGING, SIMULATE_API_CALLS, BE_GEO_ID, MERAKI_PYTHON_SDK_CALLER
)


__version__ = '0.110.6'


class DashboardAPI(object):
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
                 be_geo_id=BE_GEO_ID, caller=MERAKI_PYTHON_SDK_CALLER):
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
        self._session = RestSession(
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
            be_geo_id=be_geo_id,
            caller=caller,
        )

        # API endpoints by section
        self.api_usage = APIUsage(self._session)
        self.action_batches = ActionBatches(self._session)
        self.admins = Admins(self._session)
        self.alert_settings = AlertSettings(self._session)
        self.bluetooth_clients = BluetoothClients(self._session)
        self.bluetooth_settings = BluetoothSettings(self._session)
        self.camera_quality_retention_profiles = CameraQualityRetentionProfiles(self._session)
        self.cameras = Cameras(self._session)
        self.change_log = ChangeLog(self._session)
        self.clients = Clients(self._session)
        self.config_templates = ConfigTemplates(self._session)
        self.connectivity_monitoring_destinations = ConnectivityMonitoringDestinations(self._session)
        self.content_filtering_categories = ContentFilteringCategories(self._session)
        self.content_filtering_rules = ContentFilteringRules(self._session)
        self.dashboard_branding_policies = DashboardBrandingPolicies(self._session)
        self.devices = Devices(self._session)
        self.events = Events(self._session)
        self.firewalled_services = FirewalledServices(self._session)
        self.floor_plans = FloorPlans(self._session)
        self.group_policies = GroupPolicies(self._session)
        self.http_servers = HTTPServers(self._session)
        self.intrusion_settings = IntrusionSettings(self._session)
        self.licenses = Licenses(self._session)
        self.link_aggregations = LinkAggregations(self._session)
        self.mg_dhcp_settings = MGDHCPSettings(self._session)
        self.mg_lan_settings = MGLANSettings(self._session)
        self.mg_connectivity_monitoring_destinations = MGConnectivityMonitoringDestinations(self._session)
        self.mg_port_forwarding_rules = MGPortForwardingRules(self._session)
        self.mg_subnet_pool_settings = MGSubnetPoolSettings(self._session)
        self.mg_uplink_settings = MGUplinkSettings(self._session)
        self.mr_l3_firewall = MRL3Firewall(self._session)
        self.mv_sense = MVSense(self._session)
        self.mx_1_1_nat_rules = MX11NATRules(self._session)
        self.mx_1_many_nat_rules = MX1ManyNATRules(self._session)
        self.mx_l3_firewall = MXL3Firewall(self._session)
        self.mx_l7_application_categories = MXL7ApplicationCategories(self._session)
        self.mx_l7_firewall = MXL7Firewall(self._session)
        self.mx_vlan_ports = MXVLANPorts(self._session)
        self.mx_vpn_firewall = MXVPNFirewall(self._session)
        self.mx_cellular_firewall = MXCellularFirewall(self._session)
        self.mx_inbound_firewall = MXInboundFirewall(self._session)
        self.mx_port_forwarding_rules = MXPortForwardingRules(self._session)
        self.mx_static_routes = MXStaticRoutes(self._session)
        self.mx_warm_spare_settings = MXWarmSpareSettings(self._session)
        self.malware_settings = MalwareSettings(self._session)
        self.management_interface_settings = ManagementInterfaceSettings(self._session)
        self.meraki_auth_users = MerakiAuthUsers(self._session)
        self.monitored_media_servers = MonitoredMediaServers(self._session)
        self.named_tag_scope = NamedTagScope(self._session)
        self.netflow_settings = NetFlowSettings(self._session)
        self.networks = Networks(self._session)
        self.openapi_spec = OpenAPISpec(self._session)
        self.organizations = Organizations(self._session)
        self.pii = PII(self._session)
        self.radio_settings = RadioSettings(self._session)
        self.saml_roles = SAMLRoles(self._session)
        self.sm = SM(self._session)
        self.snmp_settings = SNMPSettings(self._session)
        self.ssids = SSIDs(self._session)
        self.security_events = SecurityEvents(self._session)
        self.splash_login_attempts = SplashLoginAttempts(self._session)
        self.splash_settings = SplashSettings(self._session)
        self.switch_acls = SwitchACLs(self._session)
        self.switch_port_schedules = SwitchPortSchedules(self._session)
        self.switch_ports = SwitchPorts(self._session)
        self.switch_profiles = SwitchProfiles(self._session)
        self.switch_settings = SwitchSettings(self._session)
        self.switch_stacks = SwitchStacks(self._session)
        self.syslog_servers = SyslogServers(self._session)
        self.traffic_analysis_settings = TrafficAnalysisSettings(self._session)
        self.traffic_shaping = TrafficShaping(self._session)
        self.uplink_settings = UplinkSettings(self._session)
        self.vlans = VLANs(self._session)
        self.webhook_logs = WebhookLogs(self._session)
        self.wireless_health = WirelessHealth(self._session)
        self.wireless_settings = WirelessSettings(self._session)
