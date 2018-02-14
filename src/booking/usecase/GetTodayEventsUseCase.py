from typing import List
from injector import inject

from booking import EventsSource, Event


class GetTodayEventsUseCase:

    @inject
    def __init__(self, events_source: EventsSource):
        self._events_source = events_source

    def get_today_events(self, class_id) -> List[Event]:
        return self._events_source.get_today_classroom_events(class_id)
