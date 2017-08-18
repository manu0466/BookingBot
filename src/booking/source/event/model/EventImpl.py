from datetime import datetime
from . import Event


class EventImpl(Event):

    """
    Class that implements the Event interface.
    """

    def __init__(self, name: str, description: str, classroom_identifier: str, begin_at: datetime, end_at: datetime):
        self._name = name
        self._description = description
        self._classroom_identifier = classroom_identifier
        self._beginAt = begin_at
        self._endAt = end_at

    def get_description(self) -> str:
        return self._description

    def get_name(self) -> str:
        return self._name

    def get_classroom_identifier(self) -> str:
        return self._classroom_identifier

    def get_begin(self) -> datetime:
        return self._beginAt

    def get_end(self) -> datetime:
        return self._endAt

