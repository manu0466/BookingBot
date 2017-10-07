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

    def __init__(self, name: str, identifier: int, role):
        self._name = name
        self._identifier = identifier
        self._role = role

    def get_name(self) -> str:
        return self._name

    def get_identifier(self) -> int:
        return self._identifier

    def get_role(self) -> Role:
        return self._role
