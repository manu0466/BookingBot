from booking.utils.mysql import get_db
from peewee import *
from ..UserSource import UserSource
from ..User import User
from .MysqlUser import MysqlUser
from typing import List


def init_mysql_db() -> MySQLDatabase:
    db = get_db()
    db.create_tables([MysqlUser], safe=True)
    return db


class MysqlUserSource(UserSource):

    def __init__(self):
        self._db = init_mysql_db()

    def add_user(self, user: User):
        MysqlUser.get_or_create(name=user.get_name(), identifier=user.get_identifier(), role=int(user.get_role()))

    def get_user_by_identifier(self, identifier: int) -> User:
        sql_users = MysqlUser.select().where(MysqlUser.identifier == identifier)
        user = None
        if len(sql_users) > 0:
            user = UserConverter(sql_user=sql_users[0])
        return user

    def get_all_users(self) -> List[User]:
        sql_users = MysqlUser.select()
        users = []
        for sql_user in sql_users:
            users.append(UserConverter(sql_user))
        return users


def UserConverter(sql_user: MysqlUser) -> User:
    return User(sql_user.name, sql_user.identifier, User.Role(sql_user.role))
