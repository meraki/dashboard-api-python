from datetime import datetime
import logging
import os

from .rest_session import *
from .api.api_usage import AsyncAPIUsage
from .api.action_batches import AsyncActionBatches
from .api.admins import AsyncAdmins
from .api.alert_settings import AsyncAlertSettings
from .api.bluetooth_clients import AsyncBluetoothClients
from .api.camera_quality_retention_profiles import AsyncCameraQualityRetentionProfiles
from .api.cameras import AsyncCameras
from .api.clients import AsyncClients
from .api.config_templates import AsyncConfigTemplates
from .api.connectivity_monitoring_destinations import AsyncConnectivityMonitoringDestinations
from .api.content_filtering_categories import AsyncContentFilteringCategories
from .api.content_filtering_rules import AsyncContentFilteringRules
from .api.dashboard_branding_policies import AsyncDashboardBrandingPolicies
from .api.devices import AsyncDevices
from .api.events import AsyncEvents
from .api.firewalled_services import AsyncFirewalledServices
from .api.floorplans import AsyncFloorplans
from .api.group_policies import AsyncGroupPolicies
from .api.http_servers import AsyncHTTPServers
from .api.intrusion_settings import AsyncIntrusionSettings
from .api.licenses import AsyncLicenses
from .api.link_aggregations import AsyncLinkAggregations
from .api.mg_dhcp_settings import AsyncMGDHCPSettings
from .api.mg_lan_settings import AsyncMGLANSettings
from .api.mg_connectivity_monitoring_destinations import (
    MGConnectivityMonitoringDestinations,
)
from .api.mg_port_forwarding_rules import AsyncMGPortForwardingRules
from .api.mg_subnet_pool_settings import AsyncMGSubnetPoolSettings
from .api.mg_uplink_settings import AsyncMGUplinkSettings
from .api.mr_l3_firewall import AsyncMRL3Firewall
from .api.mv_sense import AsyncMVSense
from .api.mx_1_1_nat_rules import AsyncMX11NATRules
from .api.mx_1_many_nat_rules import AsyncMX1ManyNATRules
from .api.mx_l3_firewall import AsyncMXL3Firewall
from .api.mx_l7_application_categories import AsyncMXL7ApplicationCategories
from .api.mx_l7_firewall import AsyncMXL7Firewall
from .api.mx_vlan_ports import AsyncMXVLANPorts
from .api.mx_vpn_firewall import AsyncMXVPNFirewall
from .api.mx_cellular_firewall import AsyncMXCellularFirewall
from .api.mx_inbound_firewall import AsyncMXInboundFirewall
from .api.mx_port_forwarding_rules import AsyncMXPortForwardingRules
from .api.mx_static_routes import AsyncMXStaticRoutes
from .api.mx_warm_spare_settings import AsyncMXWarmSpareSettings
from .api.malware_settings import AsyncMalwareSettings
from .api.management_interface_settings import AsyncManagementInterfaceSettings
from .api.meraki_auth_users import AsyncMerakiAuthUsers
from .api.named_tag_scope import AsyncNamedTagScope
from .api.netflow_settings import AsyncNetFlowSettings
from .api.networks import AsyncNetworks
from .api.openapi_spec import AsyncOpenAPISpec
from .api.organizations import AsyncOrganizations
from .api.pii import AsyncPII
from .api.radio_settings import AsyncRadioSettings
from .api.saml_roles import AsyncSAMLRoles
from .api.sm import AsyncSM
from .api.snmp_settings import AsyncSNMPSettings
from .api.ssids import AsyncSSIDs
from .api.security_events import AsyncSecurityEvents
from .api.splash_login_attempts import AsyncSplashLoginAttempts
from .api.splash_settings import AsyncSplashSettings
from .api.switch_acls import AsyncSwitchACLs
from .api.switch_port_schedules import AsyncSwitchPortSchedules
from .api.switch_ports import AsyncSwitchPorts
from .api.switch_profiles import AsyncSwitchProfiles
from .api.switch_settings import AsyncSwitchSettings
from .api.switch_stacks import AsyncSwitchStacks
from .api.syslog_servers import AsyncSyslogServers
from .api.traffic_analysis_settings import AsyncTrafficAnalysisSettings
from .api.traffic_shaping import AsyncTrafficShaping
from .api.uplink_settings import AsyncUplinkSettings
from .api.vlans import AsyncVLANs
from .api.webhook_logs import AsyncWebhookLogs
from .api.wireless_health import AsyncWirelessHealth
from .api.wireless_settings import AsyncWirelessSettings

from .config import (
    API_KEY_ENVIRONMENT_VARIABLE,
    DEFAULT_BASE_URL,
    SINGLE_REQUEST_TIMEOUT,
    CERTIFICATE_PATH,
    WAIT_ON_RATE_LIMIT,
    MAXIMUM_RETRIES,
    OUTPUT_LOG,
    LOG_FILE_PREFIX,
    PRINT_TO_CONSOLE,
    SIMULATE_API_CALLS,
)


class AsyncDashboardAPI(object):
    """
    **Creates a persistent Meraki dashboard API session**

    - api_key (string): API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY
    - base_url (string): preceding all endpoint resources
    - single_request_timeout (integer): maximum number of seconds for each API call
    - certificate_path (string): path for TLS/SSL certificate verification if behind local proxy
    - wait_on_rate_limit (boolean): retry if 429 rate limit error encountered?
    - maximum_retries_on_rate_limit (integer): retry up to this many times when encountering 429s or other server-side errors
    - output_log (boolean): create an output log file?
    - log_file_prefix (string): log file name appended with date and timestamp
    - print_console (boolean): if output log used, output to console too?
    - simulate (boolean): simulate POST/PUT/DELETE calls to prevent changes?
    """

    def __init__(
        self,
        api_key=None,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=SINGLE_REQUEST_TIMEOUT,
        certificate_path=CERTIFICATE_PATH,
        wait_on_rate_limit=WAIT_ON_RATE_LIMIT,
        maximum_retries=MAXIMUM_RETRIES,
        output_log=OUTPUT_LOG,
        log_file_prefix=LOG_FILE_PREFIX,
        print_console=PRINT_TO_CONSOLE,
        simulate=SIMULATE_API_CALLS,
    ):
        api_key = api_key or os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
        if not api_key:
            raise APIKeyError()

        # Configure logging
        self._logger = logging.getLogger(__name__)
        self._log_file = (
            f"{log_file_prefix}_log__{datetime.now():%Y-%m-%d_%H-%M-%S}.log"
        )
        if output_log:
            logging.basicConfig(
                filename=self._log_file,
                level=logging.DEBUG,
                format="%(asctime)s %(name)12s: %(levelname)8s > %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )

            if print_console:
                console = logging.StreamHandler()
                console.setLevel(logging.INFO)
                formatter = logging.Formatter(
                    "%(name)12s: %(levelname)8s > %(message)s"
                )
                console.setFormatter(formatter)
                logging.getLogger("").addHandler(console)

        # Creates the API session
        self._session = AsyncRestSession(
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
        self.api_usage = AsyncAPIUsage(self._session)
        self.action_batches = AsyncActionBatches(self._session)
        self.admins = AsyncAdmins(self._session)
        self.alert_settings = AsyncAlertSettings(self._session)
        self.bluetooth_clients = AsyncBluetoothClients(self._session)
        self.camera_quality_retention_profiles = CameraQualityRetentionProfiles(
            self._session
        )
        self.cameras = AsyncCameras(self._session)
        self.clients = AsyncClients(self._session)
        self.config_templates = AsyncConfigTemplates(self._session)
        self.connectivity_monitoring_destinations = ConnectivityMonitoringDestinations(
            self._session
        )
        self.content_filtering_categories = AsyncContentFilteringCategories(self._session)
        self.content_filtering_rules = AsyncContentFilteringRules(self._session)
        self.dashboard_branding_policies = AsyncDashboardBrandingPolicies(self._session)
        self.devices = AsyncDevices(self._session)
        self.events = AsyncEvents(self._session)
        self.firewalled_services = AsyncFirewalledServices(self._session)
        self.floorplans = AsyncFloorplans(self._session)
        self.group_policies = AsyncGroupPolicies(self._session)
        self.http_servers = AsyncHTTPServers(self._session)
        self.intrusion_settings = AsyncIntrusionSettings(self._session)
        self.licenses = AsyncLicenses(self._session)
        self.link_aggregations = AsyncLinkAggregations(self._session)
        self.mg_dhcp_settings = AsyncMGDHCPSettings(self._session)
        self.mg_lan_settings = AsyncMGLANSettings(self._session)
        self.mg_connectivity_monitoring_destinations = MGConnectivityMonitoringDestinations(
            self._session
        )
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