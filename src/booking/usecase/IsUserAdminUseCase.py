from injector import inject

from booking.source.user import UserSource


class IsUserAdminUseCase:

    @inject
    def __init__(self, users_source: UserSource):
        self._users_source = users_source

    def is_admin(self, user_identifier):
        result = False
        if user_identifier > 0:
            user = self._users_source.get_user_by_identifier(user_identifier)
            result = user is not None and user.get_role() == user.Role.ADMIN
        return result


