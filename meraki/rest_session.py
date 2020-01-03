import json
import time

import requests

from .config import *
from .exceptions import *


# Main module interface
class RestSession(object):
    def __init__(self, logger, api_key, base_url=DEFAULT_BASE_URL, single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                 wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT, maximum_retries=MAXIMUM_RETRIES, simulate=SIMULATE_API_CALLS):
        super(RestSession, self).__init__()

        # Initialize attributes and properties
        self._api_key = str(api_key)
        self._base_url = str(base_url)
        self._single_request_timeout = single_request_timeout
        self._wait_on_rate_limit = wait_on_rate_limit
        self._maximum_retries = maximum_retries
        self._simulate = simulate

        # Initialize a new `requests` session
        self._req_session = requests.session()

        # Remove unneeded trailing slash in base URL if present
        if self._base_url[-1] == '/':
            self._base_url = self._base_url[:-1]

        # Update the headers of the `requests` session
        if 'v0' in self._base_url:
            self._req_session.headers = {'X-Cisco-Meraki-API-Key': self._api_key, 'Content-Type': 'application/json'}
        elif 'v1' in self._base_url:
            self._req_session.headers = {'Authorization': 'Bearer ' + self._api_key, 'Content-Type': 'application/json'}

        # Log API calls
        self._logger = logger
        self._parameters = locals()
        self._parameters['api_key'] = '*' * 36 + self._api_key[-4:]
        self._logger.info(f'Meraki dashboard API session initialized with these parameters: {self._parameters}')

    def request(self, metadata, method, url, **kwargs):
        # Metadata on endpoint
        tag = metadata['tags'][0]
        operation = metadata['operation']

        # Update request kwargs with session defaults
        kwargs.setdefault('timeout', self._single_request_timeout)
        if 'meraki.com' in url:
            abs_url = url
        else:
            abs_url = self._base_url + url
        retries = self._maximum_retries

        # Option to simulate non-safe API calls without actually sending them
        self._logger.debug(metadata)
        if self._simulate and method != 'GET':
            self._logger.info(f'{tag}, {operation} - SIMULATED')
            return None
        else:
            while retries > 0:
                # Make the HTTP request to the API endpoint
                try:
                    response = self._req_session.request(method, abs_url, allow_redirects=False, **kwargs)
                    reason = response.reason if response.reason else ''
                    status = response.status_code
                except requests.exceptions.RequestException as e:
                    self._logger.warning(f'{tag}, {operation} - {e}, retrying in 1 second')
                    time.sleep(1)
                    retries -= 1
                    if retries == 0:
                        raise APIError(metadata, response)
                    else:
                        continue

                # Handle 3XX redirects automatically
                if str(status)[0] == '3':
                    abs_url = response.headers['Location']
                    substring = 'meraki.com/api/v'
                    self._base_url = abs_url[:abs_url.find(substring) + len(substring) + 1]

                # 2XX success
                elif response.ok:
                    if 'page' in metadata:
                        counter = metadata['page']
                        self._logger.info(f'{tag}, {operation}; page {counter} - {status} {reason}')
                    else:
                        self._logger.info(f'{tag}, {operation} - {status} {reason}')
                    try:
                        response.json()
                        return response
                    except json.decoder.JSONDecodeError as e:
                        self._logger.warning(f'{tag}, {operation} - {e}, retrying in 1 second')
                        time.sleep(1)
                        retries -= 1
                        if retries == 0:
                            raise APIError(metadata, response)
                        else:
                            continue

                # Rate limit 429 errors
                elif status == 429:
                    wait = int(response.headers['Retry-After'])
                    self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in {wait} seconds')
                    time.sleep(wait)
                    retries -= 1
                    if retries == 0:
                        raise APIError(metadata, response)

                # 5XX errors
                elif status >= 500:
                    self._logger.warning(f'{tag}, {operation} - {status} {reason}, retrying in 1 second')
                    time.sleep(1)
                    retries -= 1
                    if retries == 0:
                        raise APIError(metadata, response)

                # 4XX errors
                else:
                    try:
                        message = response.json()
                    except ValueError:
                        message = response.text[:100]
                    self._logger.error(f'{tag}, {operation} - {status} {reason}, {message}')
                    raise APIError(metadata, response)

    def get(self, metadata, url, params=None):
        metadata['method'] = 'GET'
        metadata['url'] = url
        metadata['params'] = params
        response = self.request(metadata, 'GET', url, params=params)
        text = response.text.strip()
        return response.json() if response and text else None

    def get_pages(self, metadata, url, params=None, total_pages=-1, direction='next'):
        if type(total_pages) == str and total_pages.lower() == 'all':
            total_pages = -1
        elif type(total_pages) == str and total_pages.isnumeric():
            total_pages = int(total_pages)
        metadata['page'] = 1

        response = self.request(metadata, 'GET', url, params=params)
        results = response.json()

        # Get additional pages if more than one requested
        while total_pages != 1:
            # Parse Link from headers
            links = response.headers['Link'].split(',')
            first = prev = next = last = None
            for l in links:
                if 'rel=first' in l:
                    first = l[l.find('<')+1:l.find('>')]
                elif 'rel=prev' in l:
                    prev = l[l.find('<')+1:l.find('>')]
                elif 'rel=next' in l:
                    next = l[l.find('<')+1:l.find('>')]
                elif 'rel=last' in l:
                    last = l[l.find('<')+1:l.find('>')]

            # GET the subsequent page
            if direction == 'next' and next:
                metadata['page'] += 1
                response = self.request(metadata, 'GET', next)
            elif direction == 'prev' and prev:
                metadata['page'] += 1
                response = self.request(metadata, 'GET', prev)
            else:
                break

            # Append that page's results, depending on the endpoint
            if type(results) == list:
                results.extend(response.json())
            # For event log endpoint
            elif type(results) == dict:
                start = response.json()['pageStartAt']
                end = response.json()['pageEndAt']
                events = response.json()['events']
                if start < results['pageStartAt']:
                    results['pageStartAt'] = start
                if end > results['pageEndAt']:
                    results['pageEndAt'] = end
                results['events'].extend(events)

            total_pages -= 1

        return results

    def post(self, metadata, url, json=None):
        metadata['method'] = 'POST'
        metadata['url'] = url
        metadata['json'] = json
        response = self.request(metadata, 'POST', url, json=json)
        text = response.text.strip()
        return response.json() if response and text else None

    def put(self, metadata, url, json=None):
        metadata['method'] = 'PUT'
        metadata['url'] = url
        metadata['json'] = json
        response = self.request(metadata, 'PUT', url, json=json)
        text = response.text.strip()
        return response.json() if response and text else None

    def delete(self, metadata, url):
        metadata['method'] = 'DELETE'
        metadata['url'] = url
        self.request(metadata, 'DELETE', url)
        return None
