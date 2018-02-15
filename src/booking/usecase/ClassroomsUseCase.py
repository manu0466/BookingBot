import datetime

from injector import inject
from typing import List

from booking.source import ClassroomSource, EventsSource, Classroom


class ClassroomsUseCase:

    @inject
    def __init__(self, classroom_source: ClassroomSource, events_source: EventsSource):
        self._classroom_source = classroom_source
        self._events_source = events_source

    def get_classrooms(self, building_id: str = None) -> List[Classroom]:
        result = []
        if building_id:
            result = self._classroom_source.get_classrooms_in_building(building_id)
        else:
            result = self._classroom_source.get_all_classrooms()
        return result

    def is_classroom_present(self, class_id: str) -> bool:
        return self._classroom_source.is_classroom_present(class_id)

    def is_classroom_free(self, class_id: str, time: datetime) -> bool:
        return self._events_source.is_classroom_free(class_id, time)

