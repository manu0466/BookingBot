from peewee import *
from booking.utils.mysql.models.BaseModel import BaseModel
from . import MysqlBuild


class MysqlClassroom(BaseModel):
    class Meta:
        db_table = 'classroom'

    """
    Mysql representation of a classroom.
    """
    build = ForeignKeyField(MysqlBuild)
    name = CharField()
    identifier = CharField()
    floor = IntegerField()
