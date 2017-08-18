from peewee import *

import configurations

MYSQL_DB = MySQLDatabase(configurations.BOT_SQL_DB,
                         user=configurations.BOT_SQL_USER,
                         passwd=configurations.BOT_SQL_PASSWORD)


def get_db() -> MySQLDatabase:
    if MYSQL_DB.is_closed():
        MYSQL_DB.connect()
    return MYSQL_DB
