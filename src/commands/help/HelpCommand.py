from commands import TextHandler
from telegram import Update, Bot
import telegram
from booking import Booking


class HelpCommand(TextHandler):
    """
    Class that handle the help command.
    """
    def __init__(self, booking: Booking):
        super(HelpCommand, self).__init__(booking, ['help'])
        self._message = ("*Currently available commands:*\n\n"
                         "- *Now* shows the classrooms that are not currently booked, and so they are free;\n\n"
                         "- *At* shows the classrooms that are not booked for today at the XX:YY hour;\n\n"
                         "*Note* that the time format must be 24 hours, so 1pm = 13:00, and you can separate hours "
                         "from minutes using the colon (:) or dot (.).\n\n"
                         "Ex.Searching for free classrooms at 3pm will result in the command either At 15:00, At 15.00 or At 15")

    def execute(self, chat_id,  bot: Bot, update: Update):
        bot.send_message(chat_id,
                         text=self._message,
                         parse_mode=telegram.ParseMode.MARKDOWN)
        return True

