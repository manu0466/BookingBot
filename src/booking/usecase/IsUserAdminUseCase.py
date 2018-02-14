from injector import inject

from booking.source.user import UserSource


class IsUserAdminUseCase:

    @inject
    def __init__(self, users_source: UserSource):
        self._users_source = users_source
        self._result_value = False

    def get_result_value(self) -> bool:
        return self._result_value

    def execute(self, user_identifier):
        if user_identifier > 0:
            user = self._users_source.get_user_by_identifier(user_identifier)
            if user is not None and user.get_role() == user.Role.ADMIN:
                self._result_value = True

        return self._result_value


