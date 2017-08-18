from abc import ABCMeta, abstractmethod
from . import Settings


class SettingsSource(metaclass=ABCMeta):
    """
    Interface that represents a source for the scheduler settings.
    """

    @abstractmethod
    def get_settings(self) -> Settings:
        """
        Gets the settings for the spider scheduler.
        :return: A Settings instance.
        """
        pass

    @abstractmethod
    def update_settings(self, new_settings: Settings):
        """
        Updates the spider scheduler settings.
        :param new_settings: The settings instance that will be saved.
        """
        pass
