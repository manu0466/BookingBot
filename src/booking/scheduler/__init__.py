from injector import Module, singleton, provider

from booking.source import EventsSource, ClassroomSource
from booking.scheduler.settings import SettingsSource
from booking.spider import SpiderFactory
from .Scheduler import Scheduler, SchedulerStatus


class SchedulerModule(Module):

    @provider
    @singleton
    def scheduler(self, events_source: EventsSource, classroom_source: ClassroomSource,
                  settings_source: SettingsSource, spiders_provider: SpiderFactory) -> Scheduler:
        return Scheduler(events_source, classroom_source, settings_source, spiders_provider)
