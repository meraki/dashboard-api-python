import platform
from meraki.exceptions import *
import re
import sys
import urllib.parse


def check_python_version():
    # Check minimum Python version

    if not (
        int(platform.python_version_tuple()[0]) == 3
        and int(platform.python_version_tuple()[1]) >= 10
    ):
        message = (
            f"This library requires Python 3.10 at minimum. Python versions 3.8 and below are EOL as of October 2024"
            f" or earlier. End of life Python versions no longer receive security updates since reaching end of life"
            f" and of support per the Python maintainers. Your interpreter version is: {platform.python_version()}. "
            f"Please consult the readme at your convenience: https://github.com/meraki/dashboard-api-python "
            f"Additional details: "
            f"python_version_tuple()[0] = {platform.python_version_tuple()[0]}; "
            f"python_version_tuple()[1] = {platform.python_version_tuple()[1]} "
        )

        raise PythonVersionError(message)


def validate_user_agent(be_geo_id, caller):
    # Generate extended portion of the User Agent
    # Validate that it follows the expected format
    user_agent = dict()

    allowed_format_in_regex = r'^[A-Za-z0-9]+(?:/[0-9A-Za-z]+(?:\.[0-9A-Za-z]+)*(-[a-z]+)?)? [A-Za-z-0-9]+$'

    if caller and re.match(allowed_format_in_regex, caller):
        user_agent["caller"] = caller
    elif be_geo_id and re.match(allowed_format_in_regex, be_geo_id):
        user_agent["caller"] = be_geo_id
    else:
        if caller:
            message = "Please follow the user agent format prescribed in our User Agents guide, available here:"
            doc_link = "https://developer.cisco.com/meraki/api-v1/user-agents-overview/"
            raise SessionInputError("MERAKI_PTYHON_SDK_CALLER", caller, message, doc_link)
        elif be_geo_id:
            message = "Use of be_geo_id is deprecated. Please use the argument MERAKI_PTYHON_SDK_CALLER instead."
            doc_link = "https://developer.cisco.com/meraki/api-v1/user-agents-overview/"
            raise SessionInputError("BE_GEO_ID", caller, message, doc_link)
        else:
            user_agent["caller"] = "unidentified"

    caller_string = f'Caller/({user_agent["caller"]})'

    return caller_string


def reject_v0_base_url(self):
    if 'v0' in self._base_url:
        sys.exit(f'This library does not support dashboard API v0 ({self._base_url} was configured as the base'
                 f' URL).  API v0 has been end of life since 2020 August 5.')
    elif self._base_url[-1] == '/':
        self._base_url = self._base_url[:-1]


def iterator_for_get_pages_bool(self):
    return self._use_iterator_for_get_pages


def use_iterator_for_get_pages_setter(self, value):
    if value:
        self.get_pages = self._get_pages_iterator
    else:
        self.get_pages = self._get_pages_legacy

    self._use_iterator_for_get_pages = value


def validate_base_url(self, url):
    allowed_domains = ['meraki.com', 'meraki.ca', 'meraki.cn', 'meraki.in', 'gov-meraki.com']
    parsed_url = urllib.parse.urlparse(url)
    if any(domain in parsed_url.netloc for domain in allowed_domains):
        abs_url = url
    else:
        abs_url = self._base_url + url
    return abs_url

