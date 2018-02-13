from peewee import *
from booking.utils.database.models.BaseModel import BaseModel


class DatabaseUser(BaseModel):
    class Meta:
        db_table = 'user'

    """
    Database representation of a User
    """
    name = CharField(256)
    identifier = IntegerField()
    role = IntegerField()
