import shelve
from datetime import datetime
from .. import SettingsSource
from .ShelveSettings import ShelveSettings
import configurations


class ShelveSettingsSource(SettingsSource):
    """
    Interface that represents a source for the scheduler settings.
    """

    def __init__(self):
        self._configuration_file = configurations.SCHEDULER_CONFIG_PATH + '/scheduler_settings'

    def get_settings(self) -> ShelveSettings:
        """
        Gets the settings for the spider scheduler.
        :return: A Settings instance.
        """
        db = shelve.open(self._configuration_file)
        time = None
        next_refresh = datetime.now()
        try:
            time = datetime.strptime(db['last_refresh'], "%Y-%m-%d %H:%M:%S")
        except KeyError:
            time = None
        try:
            next_refresh = datetime.strptime(db['next_refresh'], "%Y-%m-%d %H:%M:%S")
        except KeyError:
            next_refresh = datetime.now()

        db.close()
        return ShelveSettings(time, next_refresh)

    def update_settings(self, new_settings: ShelveSettings):
        """
        Updates the spider scheduler settings.
        :param new_settings: The settings instance that will be saved.
        """
        db = shelve.open(self._configuration_file)
        db['last_refresh'] = new_settings.get_last_refresh_date().strftime("%Y-%m-%d %H:%M:%S")
        db['next_refresh'] = new_settings.get_next_refresh_date().strftime("%Y-%m-%d %H:%M:%S")
        db.close()

