import logging
from typing import List
from peewee import *
from booking.utils.mysql import get_db
from .. import ClassroomSource, Classroom, Building
from .model import MysqlClassroom, MysqlBuild


def init_mysql_db() -> MySQLDatabase:
    db = get_db()
    db.create_tables([MysqlClassroom, MysqlBuild], safe=True)
    return db


class MysqlClassroomSource(ClassroomSource):
    def __init__(self):
        self._db = init_mysql_db()

    def get_classroom(self, name: str) -> Classroom:
        class_room = None
        try:
            class_room = MysqlClassroom.get(MysqlClassroom.name == name)
        except MysqlClassroom.DoesNotExist:
            logging.error("MysqlClassroomSource.get_classroom: No class found with name: %s" % name)
        return query_result_to_classroom(class_room)

    def get_classrooms_in_building(self, identifier: str) -> List[Classroom]:
        return query_result_to_classrooms(
            MysqlClassroom.select().join(MysqlBuild).where(MysqlBuild.identifier == identifier).execute())

    def add_classroom(self, classroom: Classroom):
        build = safe_get_build(classroom)
        try:
            MysqlClassroom.get(MysqlClassroom.identifier == classroom.get_identifier())
        except MysqlClassroom.DoesNotExist:
            MysqlClassroom.create(build=build, name=classroom.get_name(), floor=classroom.get_floor(),
                                  identifier=classroom.get_identifier())
            logging.error("MysqlClassroomSource.add_classroom: No class found with name: %s" % classroom.get_name())

    def get_all_classrooms(self) -> List[Classroom]:
        return query_result_to_classrooms(MysqlClassroom.select().order_by(MysqlClassroom.name.asc()).execute())

    def get_all_buildings(self) -> List[Building]:
        return query_result_to_buildings(MysqlBuild.select().order_by(MysqlBuild.name.asc()).execute())


def safe_get_build(classroom: Classroom) -> MysqlBuild:
    build = MysqlBuild.get_or_create(name=classroom.get_building().get_name(),
                                     identifier=classroom.get_building().get_identifier())[0]  # type: MysqlBuild
    return build


def query_result_to_classroom(classroom: MysqlClassroom) -> Classroom:
    result = None
    if classroom is not None:
        building = Building(classroom.build.identifier, classroom.build.name)
        result = Classroom(name=str(classroom.name),
                           building=building,
                           floor=classroom.floor,
                           identifier=classroom.identifier)
    return result


def query_result_to_classrooms(events: List[MysqlClassroom]) -> List[Classroom]:
    results = []
    for event in events:
        results.append(query_result_to_classroom(event))
    return results


def query_result_to_building(building: MysqlBuild) -> Building:
    result = None
    if building is not None:
        result = Building(building.identifier, building.name)
    return result


def query_result_to_buildings(buildings: List[MysqlBuild]) -> List[Building]:
    results = []
    for building in buildings:
        results.append(query_result_to_building(building))
    return results
