from abc import ABCMeta, abstractmethod
from datetime import datetime


class Event(metaclass=ABCMeta):

    """
    Interface that represents a generic event
    """

    @abstractmethod
    def get_classroom_identifier(self) -> str:
        """Returns the classroom identifier where will be the event."""
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Returns the name of the event
        :rtype: str representing the name of the event
        """
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Return a short description of the event"""
        pass

    @abstractmethod
    def get_begin(self) -> datetime:
        """Returns the date time representing when the event start"""
        pass

    @abstractmethod
    def get_end(self) -> datetime:
        """Returns the date time representing when is the event end"""
        pass

    def __str__(self):
        return self.get_name() + "\n" + \
               self.get_classroom_identifier() + "\n" + \
               str(self.get_begin()) + "\n" + \
               str(self.get_end()) + "\n" + \
               self.get_description()
