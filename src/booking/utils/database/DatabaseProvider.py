from injector import Injector, Module, provider, singleton
from peewee import Database
from playhouse.sqlite_ext import SqliteExtDatabase

import configurations


class DatabaseModule(Module):

    @provider
    @singleton
    def provide_db(self) -> Database:
        return SqliteExtDatabase(configurations.SQLITE_DB,
                                 pragmas=(('cache_size', -1024 * 64),  # 64MB page-cache.
                                          ('foreign_keys', 1)))  # Enforce foreign-key constraints.

DB_INJECTOR = Injector(modules=[DatabaseModule()])


def get_db() -> Database:
    database = DB_INJECTOR.get(Database)
    if database.is_closed():
        database.connect()
    return database
