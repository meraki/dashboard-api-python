import platform
import inspect
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


def validate_kwargs(supported_params: list[str]):
    """
    Validate if the kwargs in the calling function are among the supported parameters.

    This function uses introspection to check the kwargs of the function that calls it.
    It raises an exception if any unsupported parameters are found.

    Args:
        supported_params (List[str]): A list of supported parameter names.

    Raises:
        ValueError: If an unsupported parameter is found in the calling function's kwargs.
    """
    # Retrieve the calling function's frame
    frame = inspect.currentframe()
    # Get one frame back to access the calling function's frame
    caller_frame = frame.f_back if frame else None

    if caller_frame and 'kwargs' in caller_frame.f_locals:
        # Extract kwargs from the calling function
        kwargs = caller_frame.f_locals['kwargs']

        # Check each kwarg against the list of supported parameters
        for key in kwargs:
            if key not in supported_params:
                raise ValueError(f"Unsupported parameter: '{key}'")
