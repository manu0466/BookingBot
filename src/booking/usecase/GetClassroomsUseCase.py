from injector import inject

from booking.source import ClassroomSource


class GetClassroomsUseCase:

    @inject
    def __init__(self, classroom_source: ClassroomSource):
        self._classroom_source = classroom_source

    def get_classrooms(self, building_id: str = None):
        result = []
        if building_id:
            result = self._classroom_source.get_classrooms_in_building(building_id)
        else:
            result = self._classroom_source.get_all_classrooms()
        return result
