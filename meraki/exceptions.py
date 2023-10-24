# API key error
class APIKeyError(Exception):
    def __init__(self):
        self.message = "Meraki API key needs to be defined"
        super(APIKeyError, self).__init__(self.message)

    def __repr__(self):
        return self.message


class APIResponseError(Exception):
    """
    Exception class raised from HTTP class methods. Used as a single catch-all error for any possible
    requests exception error that might happen during communication with Meraki API to simplify caller coding.
    """

    def __init__(self, obj_name, status_code, error_msg):
        self.obj_name = obj_name
        self.status_code = status_code
        self.reason = error_msg

    def exc_message(self):
        return (
            f'HTTP call within object "{self.obj_name}" failed. Status code is "{self.status_code}". '
            f'Error message is: "{self.reason}".'
        )

    def json(self):
        return dict(error=self.reason, status_code=self.status_code)

    def __str__(self):
        return self.exc_message()


# To catch exceptions while making API calls
class APIError(Exception):
    def __init__(self, metadata, response):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = (
            self.response.status_code
            if self.response is not None and self.response.status_code
            else None
        )
        self.reason = (
            self.response.reason
            if self.response is not None and self.response.reason
            else None
        )
        try:
            self.message = (
                self.response.json()
                if self.response is not None and self.response.json()
                else None
            )
        except ValueError:
            self.message = self.response.content[:100].decode("UTF-8").strip()
            if (
                type(self.message) == str
                and self.status == 404
                and self.reason == "Not Found"
            ):
                self.message += (
                    "please wait a minute if the key or org was just newly created."
                )
        super(APIError, self).__init__(
            f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
        )

    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"


# To catch exceptions while making AIO API calls
class AsyncAPIError(Exception):
    def __init__(self, metadata, response, message):
        self.response = response
        self.tag = metadata["tags"][0]
        self.operation = metadata["operation"]
        self.status = (
            response.status if response is not None and response.status else None
        )
        self.reason = (
            response.reason if response is not None and response.reason else None
        )
        self.message = message
        if type(self.message) == str:
            self.message = self.message.strip()
            if self.status == 404 and self.reason == "Not Found":
                self.message += (
                    "please wait a minute if the key or org was just newly created."
                )

        super().__init__(
            f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"
        )

    def __repr__(self):
        return f"{self.tag}, {self.operation} - {self.status} {self.reason}, {self.message}"


class PythonVersionError(Exception):
    """Exception raised for unsupported Python versions."""

    def __init__(self, message):
        self.message = message

        super().__init__(self.message)
