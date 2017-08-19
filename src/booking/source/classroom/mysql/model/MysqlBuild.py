from peewee import *
from booking.utils.mysql.models.BaseModel import BaseModel


class MysqlBuild(BaseModel):
    class Meta:
        db_table = 'building'
    """
    Mysql representation of a build.
    """
    identifier = CharField()
    name = CharField()
