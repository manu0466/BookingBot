from injector import inject
from typing import List

from booking.source import UserSource
from booking import User


class UsersUseCase:

    @inject
    def __init__(self, user_source: UserSource):
        self._user_source = user_source

    def add_user(self, user: User):
        self._user_source.add_user(user)

    def is_user_present(self, identifier: int) -> bool:
        return self._user_source.get_user_by_identifier(identifier) is not None

    def get_user_count(self) -> int:
        return len(self._user_source.get_all_users())

    def get_users(self) -> List[User]:
        return self._user_source.get_all_users()

    def get_admins(self) -> List[User]:
        users = []
        for user in self._user_source.get_all_users():
            if user.get_role() == User.Role.ADMIN:
                users.append(user)
        return users

