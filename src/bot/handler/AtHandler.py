import re
from datetime import datetime

import telegram
from injector import inject

from . import FilterableHandler
from bot.handler.filter import RegexFilter
from booking.usecase import EventsUseCase, ClassroomsUseCase


class AtHandler(FilterableHandler):

    """
    Class that represents the At command.
    """
    @inject
    def __init__(self, events_uc: EventsUseCase, classrooms_uc: ClassroomsUseCase):
        # Regex to validate the time format
        super().__init__()
        self._re = re.compile("(^[0-9]{1,2}\.[0-9]{1,2}$)|(^[0-9]{1,2}:[0-9]{1,2}$)|(^[0-9]{1,2}$)")
        self._events_uc = events_uc
        self._classrooms_uc = classrooms_uc
        self.add_filter(RegexFilter(['/at ', 'at '], case_sensitive=False, exact_match=False))

    def handle_update(self, update, dispatcher):
        # Extract the requested time from the message
        requested_time = update.message.text.replace(" ", "")  # type: str
        if requested_time.startswith("/"):
            requested_time = requested_time[1:]
        requested_time = requested_time[2:]
        match = self._re.search(requested_time)

        if match:
            matched_string = match.string
            hour = None
            minute = None
            if "." in matched_string:
                hour, minute = self.parse_values(matched_string, ".")
            elif ":" in matched_string:
                hour, minute = self.parse_values(matched_string, ":")
            else:
                hour = int(matched_string)
                minute = 0
            if 24 > hour >= 0 and 60 > minute >= 0:
                now = datetime.now()
                time = datetime(year=now.year, month=now.month, day=now.day, hour=hour, minute=minute)
                text = "*Requested time: " + time.strftime("%H:%M") + "*\n"
                for classroom in self._classrooms_uc.get_classrooms():
                    if self._classrooms_uc.is_classroom_free(classroom.get_identifier(), time=time):
                        event = self._events_uc.get_next_event(classroom.get_identifier(), time)
                        text += "/" + classroom.get_name().lower()
                        if event is not None:
                            text += " free until " + event.get_begin().strftime("%H:%M") + "\n"
                        else:
                            text += " no events until close\n"
                dispatcher.bot.send_message(update.message.chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
            else:
                dispatcher.bot.send_message(update.message.chat_id, text="The hour value should be >= 0 and < 24\n"
                                               "The minute value should be >= 0 and < 60")
        else:
            dispatcher.bot.send_message(update.message.chat_id, text="Invalid format")
        return True

    def parse_values(self, text_value: str, separator: str):
        values = text_value.split(separator)
        return int(values[0]), int(values[1])
