from .Settings import Settings
from .SettingsSource import SettingsSource
from .shelve.ShelveSettings import ShelveSettings
from .shelve.ShelveSettingsSource import ShelveSettingsSource
import dependency_injector.providers as providers

SettingsSourceProvider = providers.Singleton(ShelveSettingsSource)