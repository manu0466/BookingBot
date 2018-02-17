from enum import Enum


class User:

    class Role(Enum):
        USER = 0
        ADMIN = 1

        def __new__(cls, value):
            member = object.__new__(cls)
            member._value = value
            return member

        def __int__(self):
            return self._value

    def __init__(self, username: str, name: str, surname: str, identifier: int, role: Role = Role.USER):
        self._username = escape_none(username)
        self._name = escape_none(name)
        self._surname = escape_none(surname)
        self._identifier = identifier
        self._role = role

    def get_username(self) -> str:
        return self._username

    def get_name(self) -> str:
        return self._name

    def get_surname(self) -> str:
        return self._surname

    def get_identifier(self) -> int:
        return self._identifier

    def get_role(self) -> Role:
        return self._role

    def set_role(self, role: Role):
        self._role = role


def escape_none(text: str) -> str:
    if text is None:
        return ''
    else:
        return text
