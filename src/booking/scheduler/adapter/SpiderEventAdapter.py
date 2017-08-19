from datetime import datetime

from booking.spider import SpiderEvent
from booking.source.event import Event


class SpiderEventAdapter(Event):

    """
    Adapter class to convert the SpiderEvent object into an Event object.
    This class have the responsibility to convert the objects returned from the spider
    to the objects that the EventSource manage.
    """

    def __init__(self, spider_event: SpiderEvent):
        self._adapted = spider_event
        scheduled_date = spider_event.get_scheduled_date()

        begin_time = spider_event.get_begin()
        self._begin = datetime(scheduled_date.year, scheduled_date.month, scheduled_date.day,
                               begin_time.hour, begin_time.minute)

        end_time = spider_event.get_end()
        self._end = datetime(scheduled_date.year, scheduled_date.month, scheduled_date.day,
                             end_time.hour, end_time.minute)

    def get_description(self) -> str:
        return self._adapted.get_description()

    def get_name(self) -> str:
        return self._adapted.get_name()

    def get_classroom_identifier(self) -> str:
        return self._adapted.get_classroom_key()

    def get_begin(self) -> datetime:
        return self._begin

    def get_end(self) -> datetime:
        return self._end

