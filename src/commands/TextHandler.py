from typing import List
from telegram import Update, Bot
from . import AbstractBookingHandler
from booking import Booking
import re
from abc import abstractmethod


class TextHandler(AbstractBookingHandler):

    """
    Class that represents a command that will be executed when the user send a text message.
    """

    def __init__(self, booking: Booking, hot_keys: List[str],
                 case_sensitive: bool = False, exact_match: bool = False):
        """
        Default constructor
        :param booking: The booking instance.
        :param hot_keys: The keys that will cause the command execution.
        :param case_sensitive: Tells if the match with the user message is case sensitive.
        :param exact_match: Tells if the message must have the same chars of a hot_key.
        """
        super(TextHandler, self).__init__(booking)
        regex = ""
        for i in range(len(hot_keys)):
            regex += ("(^" + hot_keys[i] + (".*$)" if not exact_match else "$)"))
            if i < len(hot_keys) - 1:
                regex += "|"
        self._text_regex = re.compile(regex, re.IGNORECASE if not case_sensitive else None)

    def check_update(self, update: Update):
        result = False
        if isinstance(update, Update) and (update.message or update.edited_message):
            message = update.message or update.edited_message

            match = self._text_regex.search(message.text)
            result = match is not None
        return result

    @abstractmethod
    def execute(self, chat_id, bot: Bot, update: Update):
        pass
