class TaskManagerError(Exception):
    pass


class UserAlreadyExistsError(TaskManagerError):
    pass


class UserNotFoundError(TaskManagerError):
    pass


class InvalidPasswordError(TaskManagerError):
    pass


class TaskNotFoundError(TaskManagerError):
    pass


class InvalidInputError(TaskManagerError):
    pass
