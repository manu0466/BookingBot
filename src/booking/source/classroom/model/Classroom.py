from .Building import Building


class Classroom:
    """
    Class that represents a single classroom.
    """

    def __init__(self, identifier: str, name: str, building: Building, floor: str):
        self._identifier = identifier
        self._name = name
        self._building = building
        self._floor = floor

    def get_identifier(self) -> str:
        return self._identifier

    def get_name(self) -> str:
        return self._name

    def get_building(self) -> Building:
        return self._building

    def get_floor(self) -> str:
        return self._floor
