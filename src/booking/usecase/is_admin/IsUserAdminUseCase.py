from injector import inject

from booking.usecase import UseCase
from booking.source.user import UserSource


class IsUserAdminUseCase(UseCase):

    @inject
    def __init__(self, users_source: UserSource):
        self._users_source = users_source
        self._result_value = False
        self._user_identifier = -1

    def set_request_value(self, identifier: int):
        """
        Sets the user identifier.
        :param identifier: The id of the user that will ve checked if is admin.
        """
        self._user_identifier = identifier

    def get_result_value(self) -> bool:
        return self._result_value

    def execute(self):
        if self._user_identifier > 0:
            user = self._users_source.get_user_by_identifier(self._user_identifier)
            if user is not None and user.get_role() == user.Role.ADMIN:
                self._result_value = True


