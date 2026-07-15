from pathlib import Path


# =============================================================================
# CONNECTION & AUTH
# =============================================================================

# --- API Key ---
# Meraki dashboard API key, set either at instantiation or as an environment variable
API_KEY_ENVIRONMENT_VARIABLE = "MERAKI_DASHBOARD_API_KEY"

# --- Custom Headers ---
# Extra HTTP headers appended to every request, e.g. {"X-MyApp": "id", "X-Trace": "abc"}.
# Additive only: SDK-managed headers (Authorization, Content-Type, User-Agent) always win on collision.
CUSTOM_HEADERS = {}

# --- Base URL ---
# Base URL preceding all endpoint resources
DEFAULT_BASE_URL = "https://api.meraki.com/api/v1"

# Regional base URLs
CANADA_BASE_URL = "https://api.meraki.ca/api/v1"
CHINA_BASE_URL = "https://api.meraki.cn/api/v1"
INDIA_BASE_URL = "https://api.meraki.in/api/v1"
UNITED_STATES_FED_BASE_URL = "https://api.gov-meraki.com/api/v1"

# --- Transport ---
# Maximum number of seconds for each API call
SINGLE_REQUEST_TIMEOUT = 60

# Path for TLS/SSL certificate verification if behind local proxy
CERTIFICATE_PATH = ""

# Proxy server and port, if needed, for HTTPS
REQUESTS_PROXY = ""


# =============================================================================
# IDENTITY & ATTESTATION
# =============================================================================

# --- SDK Caller ---
# Optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER
# It's good practice to use this to identify your application using the format:
# CamelCasedApplicationName/OptionalVersionNumber CamelCasedVendorName
# Please note:
# 1. Application name precedes vendor name in all cases.
# 2. If your application or vendor name normally contains spaces or special casing, you should omit them in favor of
#    normal CamelCasing here.
# 3. The slash and version number are optional. Leave both out if you like.
# 4. The slash is a forward slash, '/' -- not a backslash.
# 5. Don't use the 'Meraki' or 'Cisco' names in your application name here. Maybe in general? I'm a config file, not a
#    lawyer.
# Example 1: if your application is named 'Mambo', version number is 5.0, and your vendor/company name is Vega, then
# you would use, at minimum: 'Mambo Vega'. Optionally: 'Mambo/5.0 Vega'.
# Example 2: if your application is named 'Sunshine Rainbows', and company name is 'hunter2 for Life', and if you
# don't want to report version number, then you would use, at minimum: 'SunshineRainbows hunter2ForLife'
# The choice is yours as long as you follow the format. You should **not** include other information in this string.
# If you are an official ecosystem partner, this is required.
# For more guidance, please refer to https://developer.cisco.com/meraki/api-v1/user-agents-overview/
MERAKI_PYTHON_SDK_CALLER = ""

# --- Legacy ---
# Legacy partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID
# This is no longer used. Please use MERAKI_PYTHON_SDK_CALLER instead.
BE_GEO_ID = ""


# =============================================================================
# REQUEST HANDLING
# =============================================================================

# --- Concurrency ---
# Maximum concurrent connections for the async HTTP client (httpx.Limits(max_connections=N)).
# This is a local resource constraint (open sockets), NOT a rate limit. It controls how many
# requests can be in-flight simultaneously. For rate limiting, see Smart Limiting below.
AIO_MAXIMUM_CONCURRENT_REQUESTS = 90

# --- Smart Limiting ---
# Proactive per-org rate limiting via token buckets. Unlike AIO_MAXIMUM_CONCURRENT_REQUESTS
# (which caps how many requests are in-flight at once), smart limiting caps how many requests
# per second are sent to each organization, preventing 429s before they happen.
# The SDK parses request URLs to determine which org a request targets, using a cache of
# network -> org and device serial -> org mappings gathered via getOrganizationInventoryDevices()
# and getOrganizationNetworks().

# Enable per-org rate limiting? When False, the SDK relies solely on 429 retry logic.
# If you disable this feature, you will produce more 429 errors, which in turn wastes API budget
# and unnecessarily interferes with other applications interacting with your organization(s).
SMART_FLOW_ENABLED = True

# Maximum requests per second per organization. Meraki's default org-level limit is 10 req/s.
# The default setting is 9, which helps reserve a minimum budget for other applications. You
# can further reduce this if you are working in an organization with lots of other applications.
SMART_FLOW_ORG_RATE = 9

# Maximum requests per second across all organizations (source IP limit).
# Meraki enforces a global 100 req/s limit per source IP, independent of per-org limits.
# All requests deduct from this budget; per-org buckets provide additional throttling.
SMART_FLOW_GLOBAL_RATE = 100

# Path to the rate limit mapping cache file. The cache persists network -> org and
# serial -> org mappings across sessions so subsequent runs skip the eager load API calls
# if the cache is fresh. Set to empty string to disable persistence.
# Default: ~/.meraki/.cache/rate_limit_cache.json (platform-agnostic)
SMART_FLOW_CACHE_PATH = str(Path.home() / ".meraki" / ".cache" / "rate_limit_cache.json")

# How long (in seconds) before the disk cache is considered stale and re-fetched.
# Default is 604800 (7 days). Set to None to never expire.
# Organizations with frequent cross-org device or network movement may consider
# reducing this value to better match their real-world use and improve the effectiveness.
SMART_FLOW_CACHE_TTL = 604800.0

# How org/network/device mappings are loaded. Options: "lazy", "eager".
# "lazy" (default): mappings are collected passively as API calls are made.
# "eager": all mappings are fetched at session init via getOrganizations().
#   Costs more API calls at startup for large deployments, but reduces cache misses during operation.
#   You may notice a brief delay as the cache is created, which indicates either
#   that your environment did not previously have a cache, or the previous cache had expired.
SMART_FLOW_CACHE_MODE = "lazy"

# Log smart flow activity (bucket creation, rate adjustments, learned mappings, cache events)
# to the standard session log. Disable this if you don't want to see smart_flow log messages
# in your logs.
SMART_FLOW_LOGGING = True


# --- Retry Behavior ---
# Retry if 429 rate limit error encountered?
# Please note, setting to False means your application will not retry upon a 429. Not intended for production apps.
WAIT_ON_RATE_LIMIT = True

# Retry up to this many times when encountering 429s or other server-side errors
MAXIMUM_RETRIES = 5

# Nginx 429 retry wait time
NGINX_429_RETRY_WAIT_TIME = 60

# Action batch concurrency error retry wait time
ACTION_BATCH_RETRY_WAIT_TIME = 60

# Network deletion concurrency error retry wait time
NETWORK_DELETE_RETRY_WAIT_TIME = 240

# Retry if encountering other 4XX error (besides 429)?
RETRY_4XX_ERROR = False

# Other 4XX error retry wait time
RETRY_4XX_ERROR_WAIT_TIME = 60

# --- Pagination ---
# Use iterator for pages. May offer improved performance in some instances.
USE_ITERATOR_FOR_GET_PAGES = False


# =============================================================================
# LOGGING & OBSERVABILITY
# =============================================================================

# --- File Logging ---
# Create an output log file?
OUTPUT_LOG = True

# Path to output log; by default, working directory of script if not specified
LOG_PATH = ""

# Log file name appended with date and timestamp
LOG_FILE_PREFIX = "meraki_api_"

# --- Console ---
# Print output logging to console?
PRINT_TO_CONSOLE = True

# --- Control ---
# Disable all logging? You're on your own then!
SUPPRESS_LOGGING = False

# You might integrate the library in an application with a predefined logging scheme. If so, you may not need the
# library's default logging handlers, formatters etc.--instead, you can inherit an external logger instance.
INHERIT_LOGGING_CONFIG = False


# =============================================================================
# DEVELOPMENT
# =============================================================================

# --- Simulation ---
# Simulate POST/PUT/DELETE calls to prevent changes?
SIMULATE_API_CALLS = False

# --- Validation ---
# Log a warning when unrecognized kwargs are passed to API methods?
VALIDATE_KWARGS = False
