import dependency_injector.providers as providers
from .Scheduler import Scheduler
from .settings import SettingsSourceProvider
from booking.source import SourceContainer
from booking.spider import SpiderFactoryProvider


SchedulerProvider = providers.Singleton(Scheduler,
                                        events_source=SourceContainer.events,
                                        classroom_source=SourceContainer.classrooms,
                                        settings_source=SettingsSourceProvider,
                                        spiders_provider=SpiderFactoryProvider)
