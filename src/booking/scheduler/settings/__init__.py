from injector import Module, provider, singleton

from .Settings import Settings
from .SettingsSource import SettingsSource
from .shelve.ShelveSettings import ShelveSettings
from .shelve.ShelveSettingsSource import ShelveSettingsSource


class SettingSourceModule(Module):

    @provider
    @singleton
    def setting_source(self) -> SettingsSource:
        return ShelveSettingsSource()

