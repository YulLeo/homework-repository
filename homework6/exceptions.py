class CustomException(Exception):
    pass


class DeadlineError(CustomException):
    """
    Raises when homework is expired.
    """
    pass
