# Package Constants

# Meraki dashboard API key, set either at instantiation or as an environment variable
API_KEY_ENVIRONMENT_VARIABLE = 'MERAKI_DASHBOARD_API_KEY'

# Base URL preceding all endpoint resources
DEFAULT_BASE_URL = 'https://api.meraki.com/api/v0'

# Maximum number of seconds for each API call
SINGLE_REQUEST_TIMEOUT = 60

# Path for TLS/SSL certificate verification if behind local proxy
CERTIFICATE_PATH = ''

# Proxy server and port, if needed, for HTTPS
REQUESTS_PROXY = ''

# Retry if 429 rate limit error encountered?
WAIT_ON_RATE_LIMIT = True

# Nginx 429 retry wait time
NGINX_429_RETRY_WAIT_TIME = 60

# Action batch concurrency error retry wait time
ACTION_BATCH_RETRY_WAIT_TIME = 60

# Retry if encountering other 4XX error (besides 429)?
RETRY_4XX_ERROR = False

# Other 4XX error retry wait time
RETRY_4XX_ERROR_WAIT_TIME = 60

# Retry up to this many times when encountering 429s or other server-side errors
MAXIMUM_RETRIES = 2

# Create an output log file?
OUTPUT_LOG = True

# Path to output log; by default, working directory of script if not specified
LOG_PATH = ''

# Log file name appended with date and timestamp
LOG_FILE_PREFIX = 'meraki_api_'

# Print output logging to console?
PRINT_TO_CONSOLE = True

# Disable all logging? You're on your own then!
SUPPRESS_LOGGING = False

# Simulate POST/PUT/DELETE calls to prevent changes?
SIMULATE_API_CALLS = False

# Number of concurrent API requests for asynchronous class
AIO_MAXIMUM_CONCURRENT_REQUESTS = 3

# Optional partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID
BE_GEO_ID = ''

# Optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER
MERAKI_PYTHON_SDK_CALLER = ''
