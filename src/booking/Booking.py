from .scheduler import Scheduler
from .source import EventsSource, ClassroomSource, UserSource


class Booking:
    """
    Class used as a facade to interact with the Scheduler and the EventsSource,
    this also initiate the source and the spider scheduler.
    """
    def __init__(self, events_source: EventsSource, classroom_source: ClassroomSource,
                 user_source: UserSource, scheduler: Scheduler):
        self._events_source = events_source
        self._classroom_source = classroom_source
        self._users_source = user_source
        self._scheduler = scheduler

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

    def get_user_source(self) -> UserSource:
        """
        Gets the source that can be used to access the users.
        :return: Returns an instance of UserSource.
        """
        return self._users_source
