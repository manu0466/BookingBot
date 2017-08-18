from abc import ABCMeta, abstractmethod
from datetime import datetime


class Settings(metaclass=ABCMeta):

    """
    Interface that represents the settings for the spider scheduler.
    """

    def need_refresh(self) -> bool:
        """
        Tels if the scheduler should start the spiders.
        :return: True if should run the spiders false otherwise.
        """
        return datetime.now() >= self.get_next_refresh_date()

    @abstractmethod
    def get_last_refresh_date(self) -> datetime:
        """
        Gets the datetime of the last scheduler refresh.
        :return: datetime value that represents the last scheduler refresh.
        """
        pass

    @abstractmethod
    def update_refresh_date(self, date_time: datetime):
        """
        Sets the datetime of the last scheduler refresh.
        """
        pass

    @abstractmethod
    def get_next_refresh_date(self) -> datetime:
        pass
