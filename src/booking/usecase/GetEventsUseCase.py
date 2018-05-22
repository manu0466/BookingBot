from datetime import datetime
from typing import List
from injector import inject

from booking import EventsSource, Event


class GetEventsUseCase:

    @inject
    def __init__(self, events_source: EventsSource):
        self._events_source = events_source

    def get_events(self, class_id: str, date: datetime) -> List[Event]:
        events = self._events_source.get_all_classroom_events(class_id)
        return list(filter(lambda event: event.get_begin() <= date <= event.get_end(), events))
