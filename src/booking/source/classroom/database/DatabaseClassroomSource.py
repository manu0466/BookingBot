import logging
from typing import List

from booking.utils.database import get_db
from .. import ClassroomSource, Classroom, Building
from .model import DatabaseClassroom, DatabaseBuild


class DatabaseClassroomSource(ClassroomSource):

    def __init__(self):
        db = get_db()
        db.create_tables([DatabaseClassroom, DatabaseBuild], safe=True)
        self._db = db

    def get_classroom(self, name: str) -> Classroom:
        class_room = None
        try:
            class_room = DatabaseClassroom.get(DatabaseClassroom.name == name)
        except DatabaseClassroom.DoesNotExist:
            logging.error("MysqlClassroomSource.get_classroom: No class found with name: %s" % name)
        return query_result_to_classroom(class_room)

    def get_classrooms_in_building(self, identifier: str) -> List[Classroom]:
        return query_result_to_classrooms(
            DatabaseClassroom.select().join(DatabaseBuild).where(DatabaseBuild.identifier == identifier).execute())

    def add_classroom(self, classroom: Classroom):
        build = safe_get_build(classroom)
        try:
            DatabaseClassroom.get(DatabaseClassroom.identifier == classroom.get_identifier())
        except DatabaseClassroom.DoesNotExist:
            DatabaseClassroom.create(build=build, name=classroom.get_name(), floor=classroom.get_floor(),
                                     identifier=classroom.get_identifier())
            logging.error("MysqlClassroomSource.add_classroom: No class found with name: %s" % classroom.get_name())

    def get_all_classrooms(self) -> List[Classroom]:
        return query_result_to_classrooms(DatabaseClassroom.select().order_by(DatabaseClassroom.name.asc()).execute())

    def get_all_buildings(self) -> List[Building]:
        return query_result_to_buildings(DatabaseBuild.select().order_by(DatabaseBuild.name.asc()).execute())


def safe_get_build(classroom: Classroom) -> DatabaseBuild:
    build = DatabaseBuild.get_or_create(name=classroom.get_building().get_name(),
                                        identifier=classroom.get_building().get_identifier())[0]  # type: DatabaseBuild
    return build


def query_result_to_classroom(classroom: DatabaseClassroom) -> Classroom:
    result = None
    if classroom is not None:
        building = Building(classroom.build.identifier, classroom.build.name)
        result = Classroom(name=str(classroom.name),
                           building=building,
                           floor=classroom.floor,
                           identifier=classroom.identifier)
    return result


def query_result_to_classrooms(events: List[DatabaseClassroom]) -> List[Classroom]:
    results = []
    for event in events:
        results.append(query_result_to_classroom(event))
    return results


def query_result_to_building(building: DatabaseBuild) -> Building:
    result = None
    if building is not None:
        result = Building(building.identifier, building.name)
    return result


def query_result_to_buildings(buildings: List[DatabaseBuild]) -> List[Building]:
    results = []
    for building in buildings:
        results.append(query_result_to_building(building))
    return results
