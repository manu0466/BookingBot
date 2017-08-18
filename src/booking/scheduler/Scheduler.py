from datetime import datetime
from threading import Thread, Event
from time import sleep
from typing import List

from .adapter import SpiderEventAdapter
from ..spider import BaseSpider
from ..source import EventsSource, ClassroomSource, Classroom, Building
from .settings import SettingsSource


class Scheduler:

    """
    Class that schedule the spiders to update the events inside the events source.
    """

    def __init__(self, collection: EventsSource, classroom_source: ClassroomSource,
                 settings_source: SettingsSource, spiders: List[BaseSpider]):
        self._collection = collection  # type: EventsSource
        self._classroom_source = classroom_source  # type: ClassroomSource
        self._spiders = spiders  # type: List[BaseSpider]
        self._settings_source = settings_source  # type: SettingsSource
        self._stop_event = Event()
        self._thread = Thread(target=_scheduler_loop,
                              args=(collection, classroom_source, spiders,
                                    settings_source, self._stop_event))  # type: Thread
        self._thread.setName("BookingBot Scheduler")
        self._thread.daemon = True

    def start(self):
        self._thread.start()

    def stop(self):
        self._stop_event.set()


def _scheduler_loop(events_source: EventsSource, classroom_source: ClassroomSource,
                    spiders: List[BaseSpider],
                    settings_source: SettingsSource, stop_event: Event):
    while not stop_event.is_set():
        settings = settings_source.get_settings()
        if settings.need_refresh():
            print("Starting scheduler")
            events_source.delete_old_events()
            # Calls the spider and update the source
            for spider in spiders:
                buildings_provider = spider.get_buildings_provider()
                classrooms_dict = {}
                # Adds the classrooms inside the classroom source
                for classroom in buildings_provider.get_classrooms():
                    # Create the Building instance
                    temp_building = Building(classroom.get_building().get_name())
                    # Create the classroom building
                    temp_classroom = Classroom(classroom.get_identifier(), classroom.get_name(),
                                               temp_building, classroom.get_floor())
                    # If the classroom is not present in the source will be added
                    if not classroom_source.is_classroom_present(classroom.get_name()):
                        classroom_source.add_classroom(classroom)
                    # Adds the classroom to the dict
                    classrooms_dict[classroom.get_identifier()] = temp_classroom

                for event in spider.get_events():
                    # Checks if the classroom provided from the spider is present in the dict.
                    if event.get_classroom_key() not in classrooms_dict:
                        print("WARN no classroom found for: " + event.get_classroom_key())
                    else:
                        # Adds the event to the source.
                        events_source.add_event(SpiderEventAdapter(event))

            # Save the last refresh
            settings.update_refresh_date(date_time=datetime.now())
            # Updates the settings
            settings_source.update_settings(settings)
        else:
            print("Scheduler skipped")

        now = datetime.now()
        next_refresh = settings.get_next_refresh_date()
        next_refresh_time = (next_refresh - now).seconds
        print("Next scheduler refresh in %d seconds" % next_refresh_time)
        print("Total number of events: %d" % len(events_source.get_all_events()))
        # Wait until is time to run the spiders again.
        sleep(next_refresh_time)

