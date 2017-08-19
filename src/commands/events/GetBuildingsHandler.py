from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from booking import Booking
from .. import TextHandler


class GetBuildingsHandler(TextHandler):

    def __init__(self, booking: Booking):
        classrooms_source = booking.get_classroom_source()
        keys = []
        self._keyboard = None
        for building in classrooms_source.get_all_buildings():
            building_command = "/" + building.get_name().lower().replace(" ", "_")
            keys.append([KeyboardButton(building_command)])
        if len(keys) > 0:
            self._keyboard = ReplyKeyboardMarkup(keys)
        super().__init__(booking, ["buildings"], False, exact_match=True)

    def execute(self, chat_id, bot: Bot, update: Update):
        if self._keyboard:
            bot.send_message(chat_id=chat_id, text="Available buildings", reply_markup=self._keyboard)
        else:
            bot.send_message(chat_id=chat_id, text="Sorry, no buildings available")
