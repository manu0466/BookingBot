from peewee import *
from booking.utils.database.models.BaseModel import BaseModel
from . import DatabaseBuild


class DatabaseClassroom(BaseModel):
    class Meta:
        db_table = 'classroom'

    """
    Mysql representation of a classroom.
    """
    build = ForeignKeyField(DatabaseBuild)
    name = CharField()
    identifier = CharField()
    floor = IntegerField()
