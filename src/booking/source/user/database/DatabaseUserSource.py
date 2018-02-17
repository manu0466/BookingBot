from booking.utils.database import get_db
from ..UserSource import UserSource
from ..User import User
from .DatabaseUser import DatabaseUser
from typing import List


class DatabaseUserSource(UserSource):

    def __init__(self):
        db = get_db()
        db.create_table(DatabaseUser, safe=True)
        self._db = db

    def add_user(self, user: User):
        username = escape_none(user.get_username())
        name = escape_none(user.get_name())
        surname = escape_none(user.get_surname())
        DatabaseUser.get_or_create(username=username, name=name, surname=surname,
                                   identifier=user.get_identifier(), role=int(user.get_role()))

    def get_user_by_identifier(self, identifier: int) -> User:
        sql_users = DatabaseUser.select().where(DatabaseUser.identifier == identifier)
        user = None
        if len(sql_users) > 0:
            user = UserConverter(sql_user=sql_users[0])
        return user

    def get_all_users(self) -> List[User]:
        sql_users = DatabaseUser.select()
        users = []
        for sql_user in sql_users:
            users.append(UserConverter(sql_user))
        return users


def UserConverter(sql_user: DatabaseUser) -> User:
    return User(sql_user.username, sql_user.name, sql_user.surname, sql_user.identifier, User.Role(sql_user.role))


def escape_none(text: str) -> str:
    if text is None:
        return ''
    else:
        return text