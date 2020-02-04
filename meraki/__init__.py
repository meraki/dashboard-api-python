from datetime import datetime
import logging
import os

from .legacy import *
from .rest_session import *
from .api.api_usage import APIUsage
from .api.action_batches import ActionBatches
from .api.admins import Admins
from .api.alert_settings import AlertSettings
from .api.bluetooth_clients import BluetoothClients
from .api.camera_quality_retention_profiles import CameraQualityRetentionProfiles
from .api.cameras import Cameras
from .api.clients import Clients
from .api.config_templates import ConfigTemplates
from .api.connectivity_monitoring_destinations import ConnectivityMonitoringDestinations
from .api.content_filtering_categories import ContentFilteringCategories
from .api.content_filtering_rules import ContentFilteringRules
from .api.dashboard_branding_policies import DashboardBrandingPolicies
from .api.devices import Devices
from .api.events import Events
from .api.firewalled_services import FirewalledServices
from .api.floorplans import Floorplans
from .api.group_policies import GroupPolicies
from .api.http_servers import HTTPServers
from .api.intrusion_settings import IntrusionSettings
from .api.licenses import Licenses
from .api.link_aggregations import LinkAggregations
from .api.mg_dhcp_settings import MGDHCPSettings
from .api.mg_lan_settings import MGLANSettings
from .api.mg_connectivity_monitoring_destinations import MGConnectivityMonitoringDestinations
from .api.mg_port_forwarding_rules import MGPortForwardingRules
from .api.mg_subnet_pool_settings import MGSubnetPoolSettings
from .api.mg_uplink_settings import MGUplinkSettings
from .api.mr_l3_firewall import MRL3Firewall
from .api.mv_sense import MVSense
from .api.mx_1_1_nat_rules import MX11NATRules
from .api.mx_1_many_nat_rules import MX1ManyNATRules
from .api.mx_l3_firewall import MXL3Firewall
from .api.mx_l7_application_categories import MXL7ApplicationCategories
from .api.mx_l7_firewall import MXL7Firewall
from .api.mx_vlan_ports import MXVLANPorts
from .api.mx_vpn_firewall import MXVPNFirewall
from .api.mx_cellular_firewall import MXCellularFirewall
from .api.mx_inbound_firewall import MXInboundFirewall
from .api.mx_port_forwarding_rules import MXPortForwardingRules
from .api.mx_static_routes import MXStaticRoutes
from .api.mx_warm_spare_settings import MXWarmSpareSettings
from .api.malware_settings import MalwareSettings
from .api.management_interface_settings import ManagementInterfaceSettings
from .api.meraki_auth_users import MerakiAuthUsers
from .api.monitored_media_servers import MonitoredMediaServers
from .api.named_tag_scope import NamedTagScope
from .api.netflow_settings import NetFlowSettings
from .api.networks import Networks
from .api.openapi_spec import OpenAPISpec
from .api.organizations import Organizations
from .api.pii import PII
from .api.radio_settings import RadioSettings
from .api.saml_roles import SAMLRoles
from .api.sm import SM
from .api.snmp_settings import SNMPSettings
from .api.ssids import SSIDs
from .api.security_events import SecurityEvents
from .api.splash_login_attempts import SplashLoginAttempts
from .api.splash_settings import SplashSettings
from .api.switch_acls import SwitchACLs
from .api.switch_port_schedules import SwitchPortSchedules
from .api.switch_ports import SwitchPorts
from .api.switch_profiles import SwitchProfiles
from .api.switch_settings import SwitchSettings
from .api.switch_stacks import SwitchStacks
from .api.syslog_servers import SyslogServers
from .api.traffic_analysis_settings import TrafficAnalysisSettings
from .api.traffic_shaping import TrafficShaping
from .api.uplink_settings import UplinkSettings
from .api.vlans import VLANs
from .api.webhook_logs import WebhookLogs
from .api.wireless_health import WirelessHealth
from .api.wireless_settings import WirelessSettings
from .config import (
    API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, SINGLE_REQUEST_TIMEOUT, CERTIFICATE_PATH, WAIT_ON_RATE_LIMIT,
    MAXIMUM_RETRIES, OUTPUT_LOG, LOG_PATH, LOG_FILE_PREFIX, PRINT_TO_CONSOLE, SIMULATE_API_CALLS
)


class DashboardAPI(object):
    """
    **Creates a persistent Meraki dashboard API session**

    - api_key (string): API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY
    - base_url (string): preceding all endpoint resources
    - single_request_timeout (integer): maximum number of seconds for each API call
    - certificate_path (string): path for TLS/SSL certificate verification if behind local proxy
    - wait_on_rate_limit (boolean): retry if 429 rate limit error encountered?
    - maximum_retries (integer): retry up to this many times when encountering 429s or other server-side errors
    - output_log (boolean): create an output log file?
    - log_path (string): path to output log; by default, working directory of script if not specified
    - log_file_prefix (string): log file name appended with date and timestamp
    - print_console (boolean): if output log used, output to console too?
    - simulate (boolean): simulate POST/PUT/DELETE calls to prevent changes?
    """

    def __init__(self, api_key=None, base_url=DEFAULT_BASE_URL, single_request_timeout=SINGLE_REQUEST_TIMEOUT,
                 certificate_path=CERTIFICATE_PATH, wait_on_rate_limit=WAIT_ON_RATE_LIMIT,
                 maximum_retries=MAXIMUM_RETRIES, output_log=OUTPUT_LOG, log_path=LOG_PATH,
                 log_file_prefix=LOG_FILE_PREFIX, print_console=PRINT_TO_CONSOLE, simulate=SIMULATE_API_CALLS):
        # Check API key
        api_key = api_key or os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
        if not api_key:
            raise APIKeyError()

        # Configure logging
        self._logger = logging.getLogger(__name__)
        if log_path and log_path[-1] != '/':
            log_path += '/'
        self._log_file = f'{log_path}{log_file_prefix}_log__{datetime.now():%Y-%m-%d_%H-%M-%S}.log'
        if output_log:
            logging.basicConfig(
                filename=self._log_file,
                level=logging.DEBUG,
                format='%(asctime)s %(name)12s: %(levelname)8s > %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S')

            if print_console:
                console = logging.StreamHandler()
                console.setLevel(logging.INFO)
                formatter = logging.Formatter('%(name)12s: %(levelname)8s > %(message)s')
                console.setFormatter(formatter)
                logging.getLogger('').addHandler(console)

        # Creates the API session
        self._session = RestSession(
            logger=self._logger,
            api_key=api_key,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            certificate_path=certificate_path,
            wait_on_rate_limit=wait_on_rate_limit,
            maximum_retries=maximum_retries,
            simulate=simulate,
        )

        # API endpoints by section
        self.api_usage = APIUsage(self._session)
        self.action_batches = ActionBatches(self._session)
        self.admins = Admins(self._session)
        self.alert_settings = AlertSettings(self._session)
        self.bluetooth_clients = BluetoothClients(self._session)
        self.camera_quality_retention_profiles = CameraQualityRetentionProfiles(self._session)
        self.cameras = Cameras(self._session)
        self.clients = Clients(self._session)
        self.config_templates = ConfigTemplates(self._session)
        self.connectivity_monitoring_destinations = ConnectivityMonitoringDestinations(self._session)
        self.content_filtering_categories = ContentFilteringCategories(self._session)
        self.content_filtering_rules = ContentFilteringRules(self._session)
        self.dashboard_branding_policies = DashboardBrandingPolicies(self._session)
        self.devices = Devices(self._session)
        self.events = Events(self._session)
        self.firewalled_services = FirewalledServices(self._session)
        self.floorplans = Floorplans(self._session)
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
