from typing import List, Dict
from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from booking import Booking
from .. import TextHandler


class BuildingHandler(TextHandler):

    def __init__(self, booking: Booking):
        classrooms_source = booking.get_classroom_source()
        self._buildings_dict = {}  # type: Dict
        keys = []
        for building in classrooms_source.get_all_buildings():
            building_command = building.get_name().lower().replace(" ", "_")
            keys.append(building_command)
            self._buildings_dict[building_command] = building.get_identifier()
        super().__init__(booking, keys, False, exact_match=True)

    def execute(self, chat_id, bot: Bot, update: Update):
        handled = False
        if update.message.text in self._buildings_dict:
            handled = True
            building_identifier = self._buildings_dict[update.message.text]
            classrooms = self.get_classroom_source().get_classrooms_in_building(building_identifier)
            keyboard_button = []
            counter = 0
            row = -1
            for classroom in classrooms:
                if counter == 0:
                    keyboard_button.append([])
                    row += 1
                keyboard_button[row].append(KeyboardButton("/"+classroom.get_name().lower()))
                counter += 1
                if counter == 3:
                    counter = 0
            keyboard_button.append(["/buildings"])
            reply_keyboard = ReplyKeyboardMarkup(keyboard_button)
            bot.send_message(chat_id=chat_id, text="Available classrooms", reply_markup=reply_keyboard)
        return handled

