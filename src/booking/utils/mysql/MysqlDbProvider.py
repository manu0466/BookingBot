from peewee import Database
from playhouse.sqlite_ext import SqliteExtDatabase

import configurations

SQLITE_DB = SqliteExtDatabase(configurations.SQLITE_DB,
                              pragmas=(('cache_size', -1024 * 64),  # 64MB page-cache.
                                      ('foreign_keys', 1)))  # Enforce foreign-key constraints.


def get_db() -> Database:
    if SQLITE_DB.is_closed():
        SQLITE_DB.connect()
    return SQLITE_DB
