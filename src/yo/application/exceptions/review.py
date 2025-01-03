from .application import ApplicationError


class ReviewAlreadyExistsError(ApplicationError):
    def __init__(self, message, *args) -> None:
        super().__init__(message, *args)


class ReviewNotFoundError(ApplicationError):
    def __init__(self, message, *args) -> None:
        super().__init__(message, *args)
