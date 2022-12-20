class Error(Exception):
    """Base class for exceptions"""

    def __init__(self, message: str=None, error_code: str=None, data: dict=None) -> None:
        self.message = message
        self.error_code = error_code
        self.data = data


class AuthenticationError(Error):
    """Exception raised when authentication credentials are not valid"""


class AuthorizationError(Error):
    """Exception raised when user has no authorization to perform the requested action"""


class ResourceNotFound(Error):
    """Exception raised when a resource is not found in the database"""


class UnprocessablePayload(Error):
    """Exception raised when a payload has the right format but wrong data"""


class ServiceProviderError(Error):
    """Exception raised when an error occurs on the provider's side"""


class UnprocessableRequest(Error):
    """Exeption raised when the request cannot be fulfilled"""


class PreconditionNotMet(Error):
    """Exeption raised when a precondition is not met"""