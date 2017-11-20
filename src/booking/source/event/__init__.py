from .EventsSource import EventsSource
from .model import Event
from .mysql import MysqlEventsSource
import dependency_injector.providers as providers

EventSourceProvider = providers.Singleton(MysqlEventsSource)
