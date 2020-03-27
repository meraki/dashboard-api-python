"""
SPECIAL THANKS to Heimo Stieg (https://github.com/coreGreenberet) for implementing the "aio_" examples as well as this
script, which generates the contents of the "aio" directory for running asynchronously.
"""


import csv
from datetime import datetime
import os
import logging
import re
import io

_logger = logging.Logger("")


def create_logger(log_file_prefix, print_console) -> logging.Logger:
    logger = logging.getLogger(__name__)
    log_file = f"{log_file_prefix}_log__{datetime.now():%Y-%m-%d_%H-%M-%S}.log"
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s %(name)12s: %(levelname)8s > %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    if print_console:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter("%(name)12s: %(levelname)8s > %(message)s")
        console.setFormatter(formatter)
        logging.getLogger("").addHandler(console)

    return logger


def get_aio_path(path, filename) -> str:
    """helper function to return the correct for a converted file based on the original file path"""

    if not os.path.isfile(os.path.join(path, filename)):
        raise ValueError(f"{os.path.join(path,filename)} is not a file")

    if "api" in path:
        path, _ = os.path.split(path)
        return os.path.join(path, "aio", "api", filename)
    else:
        return os.path.join(path, "aio", filename)


def read_file(filepath):
    """reads the file into memory and returns it contents"""

    _logger.info(f"Reading {filepath}")
    # read file into memory
    contents = None
    with open(filepath, "r") as f:
        contents = f.read()
    return contents


def compile_regex():
    """this function will compile all needed regex patterns for the conversion
    returns a tuple of dictionaries for the meraki/__init__.py file and all files under the api directory
    """
    patternInitFile = {}
    patternAPIFile = {}

    # all patterns for meraki/__init__.py
    patternInitFile[re.compile("from \.legacy import \*\n")] = ""
    patternInitFile[re.compile("from \.config import")] = "from ..config import"
    patternInitFile[
        re.compile("class DashboardAPI\(object\):")
    ] = "class AsyncDashboardAPI:"
    patternInitFile[re.compile("(from \.api\..*import )(.*)")] = r"\1Async\2"

    patternInitFile[re.compile("(, SIMULATE_API_CALLS)")] = r"\1, AIO_MAXIMUM_CONCURRENT_REQUESTS"
    patternInitFile[re.compile("(, simulate=SIMULATE_API_CALLS)")] = ("\\1,\n"+" "*17)+"maximum_concurrent_requests=AIO_MAXIMUM_CONCURRENT_REQUESTS"
    patternInitFile[re.compile("(    - simulate \(boolean\): .*)")] = "\\1\n    - maximum_concurrent_requests (integer): How many requests should be handled at the same time? Additional requests will be queued"
    patternInitFile[re.compile("( {12}simulate=simulate,)")] = ("\\1\n"+" "*12)+"maximum_concurrent_requests=maximum_concurrent_requests"

    patternInitFile[
        re.compile("self\._session = RestSession\(")
    ] = "self._session = AsyncRestSession("
    patternInitFile[re.compile("(self\..*) = (.*\(self\._session\))")] = r"\1 = Async\2"
    patternInitFile[
        re.compile("\n$")
    ] = """

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._session.close()
"""

    # patterns for meraki/api/*.py files
    patternAPIFile[
        re.compile("super\([a-zA-Z0-9_]+, self\)\.__init__\(\)")
    ] = "super().__init__()"
    patternAPIFile[re.compile("class ([a-zA-Z0-9]+)\(object\):")] = r"class Async\1:"
    patternAPIFile[re.compile("def ([^_].*)")] = r"async def \1"
    patternAPIFile[
        re.compile("return self\._session\.")
    ] = "return await self._session."

    return patternInitFile, patternAPIFile


def convert_file(path, filename, patternDict):
    content = read_file(os.path.join(path, filename))

    _logger.info("Starting Conversion")

    for p, v in patternDict.items():
        content, count = p.subn(v, content)
        _logger.debug(f"Applied pattern {p.pattern} {count} times")

    _logger.info("Finished Conversion")

    aioFile = get_aio_path(path, filename)
    with open(aioFile, "w") as f:
        f.write(content)
    _logger.info(f"File {aioFile} saved")


def main():
    # make sure that the aio/api directory does exist
    if not os.path.exists("meraki/aio"):
        os.makedirs("meraki/aio")
    if not os.path.exists("meraki/aio/api"):
        os.makedirs("meraki/aio/api")

    patternInitFile, patternAPIFile = compile_regex()
    convert_file("meraki", "__init__.py", patternInitFile)
    apifolder = "meraki/api"

    for file in os.listdir("meraki/api"):
        if os.path.isfile(os.path.join(apifolder, file)) and file[-3:] == ".py":
            convert_file(apifolder, file, patternAPIFile)


if __name__ == "__main__":
    start_time = datetime.now()
    _logger = create_logger(log_file_prefix=__file__[:-3], print_console=True)
    main()
    end_time = datetime.now()
    _logger.info(f"\nScript complete, total runtime {end_time - start_time}")
