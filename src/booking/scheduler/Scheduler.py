import logging
from datetime import datetime
from enum import Enum
from threading import Thread, Event
from typing import List

from .adapter import SpiderEventAdapter
from ..spider import BaseSpider, SpiderFactory
from ..source import EventsSource, ClassroomSource, Classroom, Building
from .settings import SettingsSource
from rx.subjects import BehaviorSubject
from rx import Observable


class SchedulerStatus(Enum):
    IDLE = 0,
    RUNNING = 1,
    COMPLETED = 2


class SchedulerInfo:

    def __init__(self, status: SchedulerStatus, total_events: int = 0, next_refresh = 0):
        self.status = status
        self.total_events = total_events
        self.next_refresh = next_refresh


class Scheduler(Thread):

    """
    Class that schedule the spiders to update the events inside the events source.
    """

    def __init__(self, events_source: EventsSource, classroom_source: ClassroomSource,
                 settings_source: SettingsSource, spiders_provider: SpiderFactory):
        super().__init__()
        self._status_subject = BehaviorSubject(SchedulerStatus.IDLE)
        self._info_subject = BehaviorSubject(SchedulerInfo(SchedulerStatus.IDLE))
        self._events_source = events_source  # type: EventsSource
        self._classroom_source = classroom_source  # type: ClassroomSource
        self._spiders = spiders_provider.get_spiders()  # type: List[BaseSpider]
        self._settings_source = settings_source  # type: SettingsSource
        self._stop_event = Event()
        self._refresh_event = Event()
        self.setName("BookingBot Scheduler")
        self.daemon = True

    def stop(self):
        self._stop_event.set()

    def re_schedule(self):
        self._refresh_event.set()
        logging.info("Restarting the scheduler")

    def on_status_changed(self) -> Observable:
        return self._status_subject

    def on_new_info(self) -> Observable:
        return self._info_subject

    def run(self):
        while not self._stop_event.is_set():
            settings = self._settings_source.get_settings()
            if settings.need_refresh() or self._refresh_event.is_set():
                logging.info("Starting scheduler")

                self._status_subject.on_next(SchedulerStatus.RUNNING)
                self._info_subject.on_next(SchedulerInfo(SchedulerStatus.RUNNING))

                self._events_source.delete_old_events()
                # Calls the spider and update the source
                for spider in self._spiders:
                    buildings_provider = spider.get_buildings_provider()
                    classrooms_dict = {}
                    # Adds the classrooms inside the classroom source
                    for classroom in buildings_provider.get_classrooms():
                        # Create the Building instance
                        temp_building = Building(classroom.get_building().get_identifier(),
                                                 classroom.get_building().get_name())
                        # Create the classroom building
                        temp_classroom = Classroom(classroom.get_identifier(), classroom.get_name(),
                                                   temp_building, classroom.get_floor())
                        # If the classroom is not present in the source will be added
                        if not self._classroom_source.is_classroom_present(classroom.get_name()):
                            self._classroom_source.add_classroom(classroom)
                        # Adds the classroom to the dict
                        classrooms_dict[classroom.get_identifier()] = temp_classroom

                    for event in spider.get_events():
                        # Checks if the classroom provided from the spider is present in the dict.
                        if event.get_classroom_key() not in classrooms_dict:
                            logging.warning("No classroom found for: " + event.get_classroom_key())
                        else:
                            # Adds the event to the source.
                            self._events_source.add_event(SpiderEventAdapter(event))

                # Save the last refresh
                settings.update_refresh_date(date_time=datetime.now())
                # Updates the settings
                self._settings_source.update_settings(settings)
            else:
                logging.info("Scheduler skipped")

            now = datetime.now()
            next_refresh = settings.get_next_refresh_date()
            next_refresh_time = (next_refresh - now).seconds
            total_events = len(self._events_source.get_all_events())
            logging.info("Next scheduler refresh in %d seconds" % next_refresh_time)
            logging.info("Total number of events: %d" % total_events)

            self._status_subject.on_next(SchedulerStatus.COMPLETED)
            self._info_subject.on_next(SchedulerInfo(SchedulerStatus.COMPLETED, total_events, next_refresh_time))

            # Wait until is time to run the spiders again.
            self._refresh_event.clear()
            self._refresh_event.wait(next_refresh_time)

        self._status_subject.on_completed()

