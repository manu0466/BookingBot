from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import List

from .model import Event


class EventsSource(metaclass=ABCMeta):

    """
    Class that have the responsibility to save the events and to provide access to them.
    """

    @abstractmethod
    def add_event(self, event: Event):
        """
        Adds an events to the source.
        :param event: Event that will be added.
        """
        pass

    @abstractmethod
    def get_next_event(self, classroom_identifier: str, date_time: datetime) -> Event:
        """
        Gets the next scheduled events starting from the provided time for the provided classroom.
        :param classroom_identifier: Identifier of the classroom.
        :param date_time: time used as base.
        :return: The next scheduled event, None if no events are scheduled.
        """
        pass

    @abstractmethod
    def get_current_event(self, classroom_identifier: str, date_time: datetime) -> Event:
        """
        Gets the current scheduled event in the provided class at the provided time.
        :param classroom_identifier: Identifier of the classroom of interest.
        :param date_time: The time when you want to check the presence of an event
        :return: Returns the event if is scheduled, None otherwise.
        """
        pass

    @abstractmethod
    def get_classroom_events(self, classroom_identifier: str) -> List[Event]:
        """
        Gets all the scheduled events for the provided classroom.
        :param classroom_identifier: Identifier of the classroom of interest.
        :return: Returns a list of all the events scheduled in the provided class.
        """
        pass

    @abstractmethod
    def is_classroom_free(self, classroom_identifier: str, date_time: datetime) -> bool:
        """
        Tells if the a classroom is free at the provided time.
        :param classroom_identifier: Identifier of the classroom of interest.
        :param date_time: The time when you want to check if the classroom is free.
        :return: Returns True if is free, False otherwise.
        """
        pass

    @abstractmethod
    def get_all_events(self) -> List[Event]:
        """
        Gets all the scheduled events for all the classroom.
        :return: Returns a list of all the scheduled events.
        """
        pass

    @abstractmethod
    def delete_old_events(self):
        """
        Deletes all the events that are scheduled one day before today.
        """
        pass

    @abstractmethod
    def delete_all_events(self):
        """
        Deletes all events in the source.
        """
        pass

