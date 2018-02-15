import datetime

from injector import inject
from typing import List

from booking import Event
from booking.source import EventsSource


class EventsUseCase:

    @inject
    def __init__(self, events_source: EventsSource):
        self._events_source = events_source

    def get_next_event(self, class_id: str, time: datetime) -> Event:
        return self._events_source.get_next_event(class_id, time)

    def get_today_events(self, class_id: str) -> List[Event]:
        return self._events_source.get_today_classroom_events(class_id)
