# Package Constants

# Meraki dashboard API key, set either at instantiation or as an environment variable
API_KEY_ENVIRONMENT_VARIABLE = 'MERAKI_DASHBOARD_API_KEY'

# Base URL preceding all endpoint resources
DEFAULT_BASE_URL = 'https://api.meraki.com/api/v0'

# Maximum number of seconds for each API call
SINGLE_REQUEST_TIMEOUT = 60

# Path for TLS/SSL certificate verification if behind local proxy
CERTIFICATE_PATH = ''

# Retry if 429 rate limit error encountered?
WAIT_ON_RATE_LIMIT = True

# Retry up to this many times when encountering 429s or other server-side errors
MAXIMUM_RETRIES = 2

# Create an output log file?
OUTPUT_LOG = True

# Path to output log; by default, working directory of script if not specified
LOG_PATH = ''

# Log file name appended with date and timestamp
LOG_FILE_PREFIX = 'meraki_api_'

# If output log used, output to console too?
PRINT_TO_CONSOLE = True

# Simulate POST/PUT/DELETE calls to prevent changes?
SIMULATE_API_CALLS = False
