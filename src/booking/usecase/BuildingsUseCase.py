from injector import inject

from booking.source import ClassroomSource


class BuildingsUseCase:

    @inject
    def __init__(self, classroom_source: ClassroomSource):
        self._classroom_source = classroom_source

    def get_buildings(self):
        return self._classroom_source.get_all_buildings()

    def is_building_present(self, name: str) -> bool:
        result = False
        for building in self._classroom_source.get_all_buildings():
            if building.get_name().lower() == name.lower():
                result = True
                break
        return result
