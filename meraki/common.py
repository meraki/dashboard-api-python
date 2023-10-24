import platform
from meraki.exceptions import *


def check_python_version():
    # Check minimum Python version

    if not (
        int(platform.python_version_tuple()[0]) == 3
        and int(platform.python_version_tuple()[1]) >= 8
    ):
        message = (
            f"This library requires Python 3.8 at minimum. Python versions 3.7 and below "
            f"no longer receive security updates since reaching end of life and of support "
            f"per the Python maintainers. Your interpreter version is: {platform.python_version()}. "
            f"Please consult the readme at your convenience: https://github.com/meraki/dashboard-api-python "
            f"Additional details: "
            f"python_version_tuple()[0] = {platform.python_version_tuple()[0]}; "
            f"python_version_tuple()[1] = {platform.python_version_tuple()[1]} "
        )

        raise PythonVersionError(message)
