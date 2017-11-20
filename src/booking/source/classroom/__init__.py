from .ClassroomSource import ClassroomSource
from .model import *
from .mysql import MysqlClassroomSource
import dependency_injector.providers as providers

ClassroomSourceProvider = providers.Singleton(MysqlClassroomSource)
