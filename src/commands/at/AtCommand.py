from datetime import datetime
from commands import TextHandler
from telegram import Update, Bot, Message
import telegram
from booking import Booking, Event
import emoji
import re


class AtCommand(TextHandler):

    """
    Class that represents the At command.
    """

    def __init__(self, booking: Booking):
        super(AtCommand, self).__init__(booking, ['at'])
        # Regex to validate the time format
        self._re = re.compile("(^[0-9]{1,2}\.[0-9]{1,2}$)|(^[0-9]{1,2}:[0-9]{1,2}$)|(^[0-9]{1,2}$)")

    def execute(self, chat_id, bot: Bot, update: Update):
        events_source = self.get_event_source()
        classroom_source = self.get_classroom_source()
        # Extract the requested time from the message
        requested_time = update.message.text.replace(" ", "")[2:]
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
                for classroom in classroom_source.get_all_classrooms():
                    if events_source.is_classroom_free(classroom.get_identifier(), date_time=time):
                        event = events_source.get_next_event(classroom.get_identifier(), time)
                        text += "*"
                        if event is not None:
                            text += classroom.get_name() + "* free untill " + event.get_begin().strftime("%H:%M") + "\n"
                        else:
                            text += classroom.get_name() + "* no events untill close\n"
                bot.send_message(chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
            else:
                bot.send_message(chat_id, text="The hour value should be >= 0 and < 24\n"
                                               "The minute value should be >= 0 and < 60")
        else:
            bot.send_message(chat_id, text="Invalid format")
        return True

    def parse_values(self, text_value: str, separator: str):
        values = text_value.split(separator)
        return int(values[0]), int(values[1])
