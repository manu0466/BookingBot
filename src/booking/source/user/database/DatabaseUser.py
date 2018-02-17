from peewee import *
from booking.utils.database.models.BaseModel import BaseModel


class DatabaseUser(BaseModel):
    class Meta:
        db_table = 'user'

    """
    Database representation of a User
    """
    username = CharField(64, default='')
    name = CharField(64, default='')
    surname = CharField(64, default='')
    identifier = IntegerField()
    role = IntegerField()
