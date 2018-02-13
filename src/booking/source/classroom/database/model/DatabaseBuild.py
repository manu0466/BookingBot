from peewee import *
from booking.utils.database.models.BaseModel import BaseModel


class DatabaseBuild(BaseModel):
    class Meta:
        db_table = 'building'
    """
    Mysql representation of a build.
    """
    identifier = CharField()
    name = CharField()
