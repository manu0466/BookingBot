from .scheduler import Scheduler
from .source import EventsSource, ClassroomSource
from .source.event import MysqlEventsSource
from .source.classroom import MysqlClassroomSource
from .spider.math import MathSpider, OfflineSpider

from .scheduler.settings import ShelveSettingsSource


class Booking:
    """
    Class used as a facade to interact with the Scheduler and the EventsSource,
    this also initiate the source and the spider scheduler.
    """
    def __init__(self):
        self._events_source = MysqlEventsSource()
        self._classroom_source = MysqlClassroomSource()
        self._scheduler_settings = ShelveSettingsSource()
        self._scheduler = Scheduler(self._events_source, self._classroom_source, self._scheduler_settings,
                                    [MathSpider()])

    def start_scheduler(self):
        """
        Start the spiders scheduler.
        """
        self._scheduler.start()

    def stop_scheduler(self):
        """
        Stops the spiders scheduler.
        """
        self._scheduler.stop()

    def get_events_source(self) -> EventsSource:
        """
        Gets the source that can be used to access the events.
        :return: Returns an instance of EventsSource.
        """
        return self._events_source

    def get_classroom_source(self) -> ClassroomSource:
        """
        Gets the source that can be used to access the classrooms.
        :return: Returns an instance of ClassroomSource.
        """
        return self._classroom_source
