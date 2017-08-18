from datetime import time
from datetime import date


class SpiderEvent:

    """
    Class that represents a single event extract from a spider.
    """

    def __init__(self, classroom: str, build: str, event_name: str, event_description: str,
                 begin_at: time, end_at: time, scheduled_date: date):
        """
        Default constructor.
        :param classroom: Name of the classroom where the events is scheduled.
        :param build: Name of the build where the events is scheduled.
        :param event_name: Event name.
        :param event_description: Event description.
        :param begin_at: the time that represents when the event begin.
        :param end_at: the time that represents when the event end.
        :param scheduled_date: The day of when the event is scheduled.
        """
        self._classroom = classroom
        self._build = build
        self._event_name = event_name
        self._event_description = event_description
        self._begin_at = begin_at
        self._end_at = end_at
        self._scheduled_date = scheduled_date
        self._classroom_key = build + "_" + classroom.lower()

    def get_classroom(self) -> str:
        return self._classroom

    def get_build(self) -> str:
        return self._build

    def get_name(self) -> str:
        return self._event_name

    def get_description(self) -> str:
        return self._event_description

    def get_begin(self) -> time:
        return self._begin_at

    def get_end(self) -> time:
        return self._end_at

    def get_scheduled_date(self):
        return self._scheduled_date

    def get_classroom_key(self) -> str:
        return self._classroom_key
