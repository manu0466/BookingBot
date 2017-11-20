from .UserSource import UserSource
from .User import User
from .mysql import MysqlUserSource
import dependency_injector.providers as providers

UserSourceProvider = providers.Singleton(MysqlUserSource)