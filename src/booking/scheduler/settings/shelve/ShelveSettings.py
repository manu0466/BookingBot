from .. import Settings
from datetime import datetime, timedelta


class ShelveSettings(Settings):

    """
    Implementation of the Settings interface.
    """
    def __init__(self, last_refresh: datetime, next_refresh: datetime):
        self._last_refresh = last_refresh
        self._next_refresh = next_refresh

    def get_last_refresh_date(self) -> datetime:
        return self._last_refresh

    def update_refresh_date(self, date_time: datetime):
        self._last_refresh = date_time
        now = datetime.now()
        self._next_refresh = datetime(year=now.year, month=now.month, day=now.day) + timedelta(days=1)

    def get_next_refresh_date(self) -> datetime:
        return self._next_refresh




