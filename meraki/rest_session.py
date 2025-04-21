import random
import urllib.parse
from datetime import datetime, timezone
import json
import time

import requests
from requests.utils import to_key_val_list
from requests.compat import basestring, urlencode

from meraki.__init__ import __version__
from meraki.common import *
from meraki.response_handler import *
from meraki.config import *


def encode_params(_, data):
    """Encode parameters in a piece of data.

    Will successfully encode parameters when passed as a dict or a list of
    2-tuples. Order is retained if data is a list of 2-tuples but arbitrary
    if parameters are supplied as a dict.

    MERAKI OVERRIDE:
    By default, when parameters are supplied as a dict, only the object keys
    are encoded.

    Ex. {"param": [{"key_1":"value_1"}, {"key_2":"value_2"}]} => ?param[]=key_1&param[]=key_2

    Now when parameters are supplied as a dict, dict keys will be appended to
    parameter names. This adds support for the "array of objects" query parameter type.

    Ex. {"param": [{"key_1":"value_1"}, {"key_2":"value_2"}]} => ?param[]key_1=value_1&param[]key_2=value_2
    """
    if isinstance(data, (str, bytes)):
        return data
    elif hasattr(data, "read"):
        return data
    elif hasattr(data, "__iter__"):
        result = []
        # Get each query parameter key value pair
        for k, vs in to_key_val_list(data):
            """
            Turn value into list/iterable if it is not already. 
            Ex. {"param": "value"} => {"param": ["value"]}
            """
            if isinstance(vs, basestring) or not hasattr(vs, "__iter__"):
                vs = [vs]
            for v in vs:
                # List params
                if v is not None and not isinstance(v, dict):
                    """
                    Add a query parameter key-value pair for each value to the list of results. 
                    Ex. {"param": ["value_1", "value_2"]} => [(param, value_1), (param, value_2)]
                    """
                    result.append(
                        (
                            k.encode("utf-8") if isinstance(k, str) else k,
                            v.encode("utf-8") if isinstance(v, str) else v,
                        )
                    )
                # Dict params
                else:
                    """
                    Append each dict key to the parameter name. 
                    Add a query parameter key-value pair for each value to the list of results. 
                    {"param": [{"key_1": "value_1"}, {"key_2": "value_2"}]} => [(param + key_1, value1), (param + key_2, value2)]
                    """
                    for k_1, v_1 in v.items():
                        result.append(
                            (
                                (k + k_1).encode("utf-8") if isinstance(k, str) else k_1,
                                (v + v_1).encode("utf-8") if isinstance(v, str) else v_1,
                            )
                        )
        # Return URL encoded string
        return urlencode(result, doseq=True)
    else:
        return data


# Monkey patch the _encode_params from the requests library with the encode_params function above
requests.models.RequestEncodingMixin._encode_params = encode_params


def user_agent_extended(be_geo_id, caller):
    # Generate the extended portion of the User-Agent
    user_agent = dict()

    if caller:
        user_agent["caller"] = caller
    elif be_geo_id:
        user_agent["caller"] = be_geo_id
    else:
        user_agent["caller"] = "unidentified"

    caller_string = f'Caller/({user_agent["caller"]})'

    return caller_string

  
# Main module interface
class RestSession(object):
    def __init__(
        self,
        logger,
        api_key,
        base_url=DEFAULT_BASE_URL,
        single_request_timeout=SINGLE_REQUEST_TIMEOUT,
        certificate_path=CERTIFICATE_PATH,
        requests_proxy=REQUESTS_PROXY,
        wait_on_rate_limit=WAIT_ON_RATE_LIMIT,
        nginx_429_retry_wait_time=NGINX_429_RETRY_WAIT_TIME,
        action_batch_retry_wait_time=ACTION_BATCH_RETRY_WAIT_TIME,
        network_delete_retry_wait_time=NETWORK_DELETE_RETRY_WAIT_TIME,
        retry_4xx_error=RETRY_4XX_ERROR,
        retry_4xx_error_wait_time=RETRY_4XX_ERROR_WAIT_TIME,
        maximum_retries=MAXIMUM_RETRIES,
        simulate=SIMULATE_API_CALLS,
        be_geo_id=BE_GEO_ID,
        caller=MERAKI_PYTHON_SDK_CALLER,
        use_iterator_for_get_pages=USE_ITERATOR_FOR_GET_PAGES,
    ):
        super(RestSession, self).__init__()

        # Initialize attributes and properties
        self._version = __version__
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._certificate_path = certificate_path
        self._requests_proxy = requests_proxy
        self._wait_on_rate_limit = wait_on_rate_limit
        self._nginx_429_retry_wait_time = nginx_429_retry_wait_time
        self._action_batch_retry_wait_time = action_batch_retry_wait_time
        self._network_delete_retry_wait_time = network_delete_retry_wait_time
        self._retry_4xx_error = retry_4xx_error
        self._retry_4xx_error_wait_time = retry_4xx_error_wait_time
        self._maximum_retries = maximum_retries
        self._simulate = simulate
        self._be_geo_id = be_geo_id
        self._caller = caller
        self.use_iterator_for_get_pages = use_iterator_for_get_pages

        # Initialize a new `requests` session
        self._req_session = requests.session()
        self._req_session.encoding = 'utf-8'

        # Check the Python version
        check_python_version()

        # Check base URL
        reject_v0_base_url(self)

        # Update the headers for the session
        self._req_session.headers = {
            'Authorization': 'Bearer ' + self._api_key,
            'Content-Type': 'application/json',
            'User-Agent': f'python-meraki/{self._version} ' + validate_user_agent(self._be_geo_id, self._caller),
        }

        # Log API calls
        self._logger = logger
        self._parameters = {'version': self._version}
        self._parameters.update(locals())
        self._parameters.pop('self')
        self._parameters.pop('logger')
        self._parameters.pop('__class__')
        self._parameters['api_key'] = '*' * 36 + self._api_key[-4:]
        if self._logger:
            self._logger.info(f'Meraki dashboard API session initialized with these parameters: {self._parameters}')

    @property
    def use_iterator_for_get_pages(self):
        return iterator_for_get_pages_bool(self)

    @use_iterator_for_get_pages.setter
    def use_iterator_for_get_pages(self, value):
        use_iterator_for_get_pages_setter(self, value)

    def request(self, metadata, method, url, **kwargs):
        # Metadata on endpoint
        tag = metadata['tags'][0]
        operation = metadata['operation']

        # Update request kwargs with session defaults
        self.prepare_request(kwargs)

        # Ensure proper base URL
        abs_url = validate_base_url(self, url)

        # Set the maximum number of retries
        retries = self._maximum_retries

        # Option to simulate non-safe API calls without actually sending them
        if self._logger:
            self._logger.debug(metadata)
        if self._simulate and method != 'GET':
            if self._logger:
                self._logger.info(f'{tag}, {operation} - SIMULATED')
            return None
        else:
            response = None
            while retries > 0:
                # Make the HTTP request to the API endpoint
                try:
                    if response:
                        response.close()
                    if self._logger:
                        self._logger.info(f'{method} {abs_url}')
                    response = self._req_session.request(method, abs_url, allow_redirects=False,
                                                         **kwargs)
                    reason = response.reason if response.reason else ''
                    status = response.status_code
                except requests.exceptions.RequestException as e:
                    if self._logger:
                        self._logger.warning(f'{tag}, {operation} - {e}, retrying in 1 second')
                    time.sleep(1)
                    retries -= 1
                    if retries == 0:
                        if e.response and e.response.status_code:
                            raise APIError(metadata, APIResponseError(e.__class__.__name__,
                                                                      e.response.status_code, str(e)))
                        else:
                            raise APIError(metadata, APIResponseError(e.__class__.__name__, 503, str(e)))
                    else:
                        continue

                match status:
                    # Handle 3xx redirects automatically
                    case status if 300 <= status < 400:
                        abs_url = handle_3xx(self, response)
                    # Handle 2xx success
                    case status if 200 <= status < 300:
                        if 'page' in metadata:
                            counter = metadata['page']
                            if self._logger:
                                self._logger.info(f'{tag}, {operation}; page {counter} - {status} {reason}')
                        else:
                            if self._logger:
                                self._logger.info(f'{tag}, {operation} - {status} {reason}')
                        # For non-empty response to GET, ensure valid JSON
                        try:
                            if method == 'GET' and response.content.strip():
                                response.json()
                            return response
                        except json.decoder.JSONDecodeError as e:
                            if self._logger:
                                self._logger.warning(f'{tag}, {operation} - {e}, retrying in 1 second')
                            time.sleep(1)
                            retries -= 1
                            if retries == 0:
                                raise APIError(metadata, response)
                            else:
                                continue
                    # Handle rate limiting
                    case 429:
                        # Retry if 429 retries are enabled and there are retries left
                        if self._wait_on_rate_limit and retries > 0:
                            if 'Retry-After' in response.headers:
                                wait = int(response.headers['Retry-After'])
                            else:
                                wait = random.randint(1, self._nginx_429_retry_wait_time)
                            if self._logger:
                                self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in {wait} seconds')
                            time.sleep(wait)
                            retries -= 1
                        # We're either out of retries or the client told us not to retry
                        else:
                            raise APIError(metadata, response)
                    # Handle 5xx errors
                    case status if 500 <= status:
                        if self._logger:
                            self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in 1 second')
                        time.sleep(1)
                        retries -= 1
                        if retries == 0:
                            raise APIError(metadata, response)
                    # Handle other 4xx errors
                    case status if status != 429 and 400 <= status < 500:
                        retries = self.handle_4xx_errors(metadata, operation, reason, response, retries, status, tag)

        return response

    def prepare_request(self, kwargs):
        if self._certificate_path:
            kwargs.setdefault('verify', self._certificate_path)
        if self._requests_proxy:
            kwargs.setdefault('proxies', {'https': self._requests_proxy})
        kwargs.setdefault('timeout', self._single_request_timeout)


    def handle_4xx_errors(self, metadata, operation, reason, response, retries, status, tag):
        try:
            message = response.json()
            message_is_dict = True
        except ValueError:
            message = response.content[:100]
            message_is_dict = False

        # Check specifically for concurrency errors
        network_delete_concurrency_error_text = 'concurrent'
        action_batch_concurrency_error_text = 'executing batches'

        # First, we check for network deletion concurrency errors
        if operation == 'deleteNetwork' and response.status_code == 400:
            # message['errors'][0] is the first error, and it contains helpful text
            # here we use it to confirm that the 400 error is related to concurrent requests
            if network_delete_concurrency_error_text in message['errors'][0]:
                wait = random.randint(30, self._network_delete_retry_wait_time)
                if self._logger:
                    self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in {wait} seconds')
                time.sleep(wait)
                retries -= 1
                if retries == 0:
                    raise APIError(metadata, response)

        # Next, we check for action batch concurrency errors
        # message['errors'][0] is the first error, and it contains helpful text
        # here we use it to confirm that the 400 error is related to concurrent requests
        elif (message_is_dict and 'errors' in message.keys() and action_batch_concurrency_error_text
              in message['errors'][0]):
            wait = self._action_batch_retry_wait_time
            if self._logger:
                self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in {wait} seconds')
            time.sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)

        # Then we check if the user asked to retry other 4xx errors, based on their session config
        elif self._retry_4xx_error:
            wait = random.randint(1, self._retry_4xx_error_wait_time)
            if self._logger:
                self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in {wait} seconds')
            time.sleep(wait)
            retries -= 1
            if retries == 0:
                raise APIError(metadata, response)

        # All other client-side errors will raise an error
        else:
            if self._logger:
                self._logger.error(f'{tag}, {operation} - {status} {reason}, {message}')
            raise APIError(metadata, response)
        return retries

    def get(self, metadata, url, params=None):
        metadata['method'] = 'GET'
        metadata['url'] = url
        metadata['params'] = params
        response = self.request(metadata, 'GET', url, params=params)
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def get_pages(self, metadata, url, params=None, total_pages=-1, direction='next', event_log_end_time=None):
        pass

    def _get_pages_iterator(
        self,
        metadata,
        url,
        params=None,
        total_pages=-1,
        direction="next",
        event_log_end_time=None,
    ):
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        elif not isinstance(total_pages, int):
            raise SessionInputError("total_pages",  total_pages, "total_pages must be either an"
                                                                 " integer or 'all' as a string (remember to add the"
                                                                 " quotation marks).", None)
        metadata["page"] = 1

        response = self.request(metadata, 'GET', url, params=params)

        # Get additional pages if more than one requested
        while total_pages != 0:
            results = response.json()
            links = response.links

            # GET the subsequent page
            if direction == "next" and "next" in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata["operation"] == "getNetworkEvents":
                    starting_after = urllib.parse.unquote(
                        str(links["next"]["url"]).split("startingAfter=")[1]
                    )
                    delta = datetime.now(timezone.utc) - datetime.fromisoformat(
                        starting_after
                    )
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300:
                        break
                    # Or if the next page is past the specified window's end time
                    elif event_log_end_time and starting_after > event_log_end_time:
                        break

                metadata["page"] += 1
                nextlink = links["next"]["url"]
            elif direction == "prev" and "prev" in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata["operation"] == "getNetworkEvents":
                    ending_before = urllib.parse.unquote(
                        str(links["prev"]["url"]).split("endingBefore=")[1]
                    )
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < "2014-01-01":
                        break

                metadata["page"] += 1
                nextlink = links["prev"]["url"]
            else:
                break

            response.close()

            return_items = []
            # Just prepare the list
            if isinstance(results, list):
                return_items = results
            elif isinstance(results, dict) and "items" in results:
                return_items = results["items"]
            # For event log endpoint
            elif isinstance(results, dict):
                if direction == "next":
                    return_items = results["events"][::-1]
                else:
                    return_items = results["events"]

            for item in return_items:
                yield item

            total_pages = total_pages - 1

            if total_pages != 0:
                response = self.request(metadata, 'GET', nextlink)

    def _get_pages_legacy(self, metadata, url, params=None, total_pages=-1, direction='next', event_log_end_time=None):
        if isinstance(total_pages, str) and total_pages.lower() == "all":
            total_pages = -1
        elif isinstance(total_pages, str) and total_pages.isnumeric():
            total_pages = int(total_pages)
        elif not isinstance(total_pages, int):
            raise SessionInputError("total_pages",  total_pages, "total_pages must be either an"
                                                                 " integer or 'all' as a string (remember to add the"
                                                                 " quotation marks).", None)

        metadata['page'] = 1

        response = self.request(metadata, 'GET', url, params=params)

        # Handle GETs that produce 204 No Content responses, e.g. getOrganizationClientSearch
        if response.status_code == 204:
            results = None
        else:
            results = response.json()

        # For event log endpoint when using 'next' direction, so results/events are sorted chronologically
        if isinstance(results, dict) and metadata['operation'] == 'getNetworkEvents' and direction == 'next':
            results['events'] = results['events'][::-1]

        # Get additional pages if more than one requested
        while total_pages != 1:
            links = response.links
            response.close()
            response = None

            # GET the subsequent page
            if direction == 'next' and 'next' in links:
                # Prevent getNetworkEvents from infinite loop as time goes forward
                if metadata['operation'] == 'getNetworkEvents':
                    starting_after = urllib.parse.unquote(links['next']['url'].split('startingAfter=')[1])
                    delta = datetime.now(timezone.utc) - datetime.fromisoformat(starting_after)
                    # Break out of loop if startingAfter returned from next link is within 5 minutes of current time
                    if delta.total_seconds() < 300:
                        break
                    # Or if next page is past the specified window's end time
                    elif event_log_end_time and starting_after > event_log_end_time:
                        break

                metadata['page'] += 1
                response = self.request(metadata, 'GET', links['next']['url'])
            elif direction == 'prev' and 'prev' in links:
                # Prevent getNetworkEvents from infinite loop as time goes backward (to epoch 0)
                if metadata['operation'] == 'getNetworkEvents':
                    ending_before = urllib.parse.unquote(links['prev']['url'].split('endingBefore=')[1])
                    # Break out of loop if endingBefore returned from prev link is before 2014
                    if ending_before < '2014-01-01':
                        break

                metadata['page'] += 1
                response = self.request(metadata, 'GET', links['prev']['url'])
            else:
                break

            # Append that page's results, depending on the endpoint
            if isinstance(results, list):
                results.extend(response.json())
            elif isinstance(results, dict) and "items" in results:
                results["items"].extend(response.json()["items"])
                if "meta" in results:
                    results["meta"]["counts"]["items"]["remaining"] = response.json()["meta"]["counts"]["items"]["remaining"]
            # For event log endpoint
            elif isinstance(results, dict):
                try:
                    start = response.json()['pageStartAt']
                except KeyError:
                    print(response.headers)
                end = response.json()['pageEndAt']
                events = response.json()['events']
                if direction == 'next':
                    events = events[::-1]
                if start < results['pageStartAt']:
                    results['pageStartAt'] = start
                if end > results['pageEndAt']:
                    results['pageEndAt'] = end
                results['events'].extend(events)

            total_pages -= 1

        if response:
            response.close()

        return results

    def post(self, metadata, url, json=None):
        metadata['method'] = 'POST'
        metadata['url'] = url
        metadata['json'] = json
        response = self.request(metadata, 'POST', url, json=json)
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def put(self, metadata, url, json=None):
        metadata['method'] = 'PUT'
        metadata['url'] = url
        metadata['json'] = json
        response = self.request(metadata, 'PUT', url, json=json)
        ret = None
        if response:
            if response.content.strip():
                ret = response.json()
            response.close()
        return ret

    def delete(self, metadata, url, json=None):
        metadata['method'] = 'DELETE'
        metadata['url'] = url
        metadata['json'] = json
        response = self.request(metadata, 'DELETE', url, json=json)
        if response:
            response.close()
        return None
