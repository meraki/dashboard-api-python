# Package Constants

# Meraki dashboard API key, set either at instantiation or as an environment variable
API_KEY_ENVIRONMENT_VARIABLE = 'MERAKI_DASHBOARD_API_KEY'

# Base URL preceding all endpoint resources
DEFAULT_BASE_URL = 'https://api.meraki.com/api/v1'

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

# You might integrate the library in an application with a predefined logging scheme. If so, you may not need the
# library's default logging handlers, formatters etc.--instead, you can inherit an external logger instance.
INHERIT_LOGGING_CONFIG = False

# Use iterator for pages. May offer improved performance in some instances. Off by default for backwards compatibility.
USE_ITERATOR_FOR_GET_PAGES = False

# Simulate POST/PUT/DELETE calls to prevent changes?
SIMULATE_API_CALLS = False

# Number of concurrent API requests for asynchronous class
AIO_MAXIMUM_CONCURRENT_REQUESTS = 8

# Legacy partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID
BE_GEO_ID = ''

# Optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER
# It's good practice to use this to identify your application using the format:
# CamelCasedApplicationName/OptionalVersionNumber CamelCasedVendorName
# Please note:
# 1. Application name precedes vendor name in all cases.
# 2. If your application or vendor name normally contains spaces or special casing, you should omit them in favor of
#    normal CamelCasing here.
# 3. The optional slash and version number are optional. Leave both out if you like.
# 4. The slash is a forward slash, '/' -- not a backslash.
# 5. Don't use the 'Meraki' name in your application name here. Maybe in general? I'm a config file, not a lawyer.
# Example 1: if your application is named 'Mambo', version number is 5.0, and your vendor/company name is Vega, then
# you would use, at minimum: 'Mambo Vega'. Optionally: 'Mambo/5.0 Vega'.
# Example 2: if your application is named 'Sunshine Rainbows', and company name is 'hunter2 for Life', and if you
# don't want to report version number, then you would use, at minimum: 'SunshineRainbows hunter2ForLife'
# The choice is yours as long as you follow the format. You should **not** include other information in this string.
# If you are an official ecosystem partner, this is required.
MERAKI_PYTHON_SDK_CALLER = ''
