from datetime import datetime
import logging
import os

from .rest_session import *
from .api.organizations import Organizations
from .api.networks import Networks
from .api.devices import Devices
from .api.appliance import Appliance
from .api.camera import Camera
from .api.cellularGateway import CellularGateway
from .api.insight import Insight
from .api.sm import Sm
from .api.switch import Switch
from .api.wireless import Wireless

# Batch class imports
from .api.batch.organizations import ActionBatchOrganizations
from .api.batch.networks import ActionBatchNetworks
from .api.batch.devices import ActionBatchDevices
from .api.batch.appliance import ActionBatchAppliance
from .api.batch.camera import ActionBatchCamera
from .api.batch.cellularGateway import ActionBatchCellularGateway
from .api.batch.insight import ActionBatchInsight
from .api.batch.sm import ActionBatchSm
from .api.batch.switch import ActionBatchSwitch
from .api.batch.wireless import ActionBatchWireless

# Config import
from .config import (
    API_KEY_ENVIRONMENT_VARIABLE, DEFAULT_BASE_URL, SINGLE_REQUEST_TIMEOUT, CERTIFICATE_PATH, REQUESTS_PROXY,
    WAIT_ON_RATE_LIMIT, NGINX_429_RETRY_WAIT_TIME, ACTION_BATCH_RETRY_WAIT_TIME, RETRY_4XX_ERROR,
    RETRY_4XX_ERROR_WAIT_TIME, MAXIMUM_RETRIES, OUTPUT_LOG, LOG_PATH, LOG_FILE_PREFIX, PRINT_TO_CONSOLE,
    SUPPRESS_LOGGING, SIMULATE_API_CALLS, BE_GEO_ID, MERAKI_PYTHON_SDK_CALLER
)

__version__ = '1.7.1'


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
    - use_iterator_for_get_pages (boolean): list* methods will return an iterator with each object instead of a complete list with all items
    """

    def __init__(self, api_key=None, base_url=DEFAULT_BASE_URL, single_request_timeout=SINGLE_REQUEST_TIMEOUT,
                 certificate_path=CERTIFICATE_PATH, requests_proxy=REQUESTS_PROXY,
                 wait_on_rate_limit=WAIT_ON_RATE_LIMIT, nginx_429_retry_wait_time=NGINX_429_RETRY_WAIT_TIME,
                 action_batch_retry_wait_time=ACTION_BATCH_RETRY_WAIT_TIME, retry_4xx_error=RETRY_4XX_ERROR,
                 retry_4xx_error_wait_time=RETRY_4XX_ERROR_WAIT_TIME, maximum_retries=MAXIMUM_RETRIES,
                 output_log=OUTPUT_LOG, log_path=LOG_PATH, log_file_prefix=LOG_FILE_PREFIX,
                 print_console=PRINT_TO_CONSOLE, suppress_logging=SUPPRESS_LOGGING, simulate=SIMULATE_API_CALLS,
                 be_geo_id=BE_GEO_ID, caller=MERAKI_PYTHON_SDK_CALLER, use_iterator_for_get_pages=False):
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
                fmt='%(asctime)s %(name)12s: %(levelname)8s > %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            handler_console = logging.StreamHandler()
            handler_console.setFormatter(formatter)

            if output_log:
                if log_path and log_path[-1] != '/':
                    log_path += '/'
                self._log_file = f'{log_path}{log_file_prefix}_log__{datetime.now():%Y-%m-%d_%H-%M-%S}.log'
                handler_log = logging.FileHandler(
                    filename=self._log_file
                )
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
            use_iterator_for_get_pages=use_iterator_for_get_pages,
        )

        # API endpoints by section
        self.organizations = Organizations(self._session)
        self.networks = Networks(self._session)
        self.devices = Devices(self._session)
        self.appliance = Appliance(self._session)
        self.camera = Camera(self._session)
        self.cellularGateway = CellularGateway(self._session)
        self.insight = Insight(self._session)
        self.sm = Sm(self._session)
        self.switch = Switch(self._session)
        self.wireless = Wireless(self._session)

        # Batch class
        class Batch:
            def __init__(self):
                pass

        # Batch definitions
        self.batch = Batch()

        # Action Batch API endpoints by section
        self.batch.organizations = ActionBatchOrganizations()
        self.batch.networks = ActionBatchNetworks()
        self.batch.devices = ActionBatchDevices()
        self.batch.appliance = ActionBatchAppliance()
        self.batch.camera = ActionBatchCamera()
        self.batch.cellularGateway = ActionBatchCellularGateway()
        self.batch.insight = ActionBatchInsight()
        self.batch.sm = ActionBatchSm()
        self.batch.switch = ActionBatchSwitch()
        self.batch.wireless = ActionBatchWireless()