from typing import List
from telegram import Update, Bot
from . import AbstractBookingHandler
from booking import Booking
import re


class TextHandler(AbstractBookingHandler):

    def __init__(self, booking: Booking, text: List[str], case_sensitive: bool = False):
        super(TextHandler, self).__init__(booking)
        regex = ""
        for i in range(len(text)):
            regex += ("(^" + text[i] + ".*$)")
            if i < len(text) - 1:
                regex += "|"
        self._text_regex = re.compile(regex, re.IGNORECASE if not case_sensitive else None)

    def check_update(self, update: Update):
        result = False
        if isinstance(update, Update) and (update.message or update.edited_message):
            message = update.message or update.edited_message

            match = self._text_regex.search(message.text)
            result = match is not None
        return result
