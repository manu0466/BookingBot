from typing import List, Dict
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
import telegram
from booking import Booking
from .. import TextHandler


class ClassroomHandler(TextHandler):

    def __init__(self, booking: Booking):
        classrooms_source = booking.get_classroom_source()
        self._classrooms_dict = {}  # type: Dict
        keys = []
        for classroom in classrooms_source.get_all_classrooms():
            classroom_command = classroom.get_name().lower().replace(" ", "_")
            keys.append(classroom_command)
            self._classrooms_dict[classroom_command] = classroom.get_identifier()
        super().__init__(booking, keys, case_sensitive=False, exact_match=True)

    def execute(self, chat_id, bot: Bot, update: Update):
        classroom_identifier = self._classrooms_dict[update.message.text.lower()]
        event_source = self.get_event_source()
        events = event_source.get_today_classroom_events(classroom_identifier)
        message = ""
        if len(events) > 0:
            for event in events:
                message += "*{0}*\nBegin at: {1}\nEnd at: {2}\n\n".format(event.get_name(),
                                                                          event.get_begin().strftime("%H:%M"),
                                                                          event.get_end().strftime("%H:%M"))
        else:
            message = "No scheduled events"
        bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        return True

