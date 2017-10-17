from peewee import *
from playhouse.shortcuts import RetryOperationalError

"""
Class to automatically reconnect to the database if an OperationalError exception
was raised when a query fails.

Source: http://docs.peewee-orm.com/en/latest/peewee/database.html#automatic-reconnect
"""

class MyRetryDB(RetryOperationalError, MySQLDatabase):
    pass

