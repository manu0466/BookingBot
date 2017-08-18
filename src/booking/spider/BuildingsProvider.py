class BuildingsProvider:

    """
    Class that expose the classrooms and buildings handled from a spider.
    """

    class Building:

        """
        Class that represents a building.
        """

        def __init__(self, identifier: str, name: str):
            self.identifier = identifier
            self.name = name

        def get_name(self) -> str:
            return self.name

        def get_identifier(self) -> str:
            return self.identifier

    class Classroom:

        """
        Class that represents a classroom.
        """

        def __init__(self, building, name: str, floor: int):
            self.building = building
            self.name = name
            self.floor = floor
            self.identifier = building.get_identifier() + "_" + name.lower()

        def get_building(self):
            return self.building

        def get_name(self) -> str:
            return self.name

        def get_floor(self) -> int:
            return self.floor

        def get_identifier(self) -> str:
            return self.identifier

    class Builder:

        """
        Builder class to create instances of BuildingsProvider.
        """

        def __init__(self):
            self.building_provider = BuildingsProvider()

        def add_building(self, identifier: str, name: str):
            """
            Adds a building
            :param identifier: Unique key that identify a building, this can be equal to the key of a building
                                handled from an another spider in case this spider provides events associated to that building.
            :param name: Name of the building.
            :return: Returns self in order to provide a fluent api.
            """
            self.building_provider._buildings.append(BuildingsProvider.Building(identifier, name))
            return self

        def add_classroom(self, name: str, floor: int):
            """
            Adds a classroom to the last created building
            :param name: Name of the classroom.
            :param floor: Floor of the classroom.
            :return: Returns self in order to provide a fluent api.
            """
            current_building = self.building_provider._buildings[-1]
            classroom = BuildingsProvider.Classroom(current_building, name, floor)
            self.building_provider._classrooms.append(classroom)
            return self

        def build(self):
            """
            Creates the BuildingsProvider instance.
            :return: Returns the initialized BuildingsProvider instance.
            """
            return self.building_provider

    def __init__(self):
        self._buildings = []
        self._classrooms = []

    def get_classrooms(self):
        """
        Gets all the classrooms.
        :return: Return a list of Classroom.
        """
        return self._classrooms

    def get_buildings(self):
        """
        Gets all the building
        :return: Return a list of Building.
        """
        return self._buildings


def builder() -> BuildingsProvider.Builder:
    return BuildingsProvider.Builder()
