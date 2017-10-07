from peewee import *
from booking.utils.mysql.models.BaseModel import BaseModel


class MysqlUser(BaseModel):
    class Meta:
        db_table = 'user'

    """
    Mysql representation of a User
    """
    name = CharField(256)
    identifier = IntegerField()
    role = IntegerField()
