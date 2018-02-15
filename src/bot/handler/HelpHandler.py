from telegram import Update
import telegram
from injector import inject
from telegram.ext import Dispatcher

from bot.handler import FilterableHandler
from bot.handler.filter import RegexFilter


class HelpHandler(FilterableHandler):
    """
    Class that handle the help command.
    """

    @inject
    def __init__(self):
        super().__init__()
        self._message = ("*Currently available commands:*\n\n"
                         "- *Now* shows the classrooms that are not currently booked, and so they are free;\n\n"
                         "- *At* shows the classrooms that are not booked for today at the XX:YY hour;\n\n"
                         "*Note* that the time format must be 24 hours, so 1pm = 13:00, and you can separate hours "
                         "from minutes using the colon (:) or dot (.).\n\n"
                         "Ex.Searching for free classrooms at 3pm will result in the command either At 15:00, At 15.00 or At 15")
        self.add_filter(RegexFilter(['help', "/help"], exact_match=True, case_sensitive=False))

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        dispatcher.bot.send_message(chat_id,
                                    text=self._message,
                                    parse_mode=telegram.ParseMode.MARKDOWN)
        return True
