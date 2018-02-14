from injector import inject

from booking.source import ClassroomSource


class GetBuildingsUseCase:

    @inject
    def __init__(self, classroom_source: ClassroomSource):
        self._classroom_source = classroom_source

    def get_buildings(self):
        return self._classroom_source.get_all_buildings()

