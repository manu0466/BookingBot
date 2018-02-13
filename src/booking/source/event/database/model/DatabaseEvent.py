from peewee import *
from booking.utils.database.models.BaseModel import BaseModel


class DatabaseEvent(BaseModel):
    class Meta:
        db_table = 'event'

    """
    Mysql representation of a Event
    """
    name = CharField(256)
    start = DateTimeField()
    end = DateTimeField()
    desc = CharField(256)
    classroom_identifier = CharField(32)
