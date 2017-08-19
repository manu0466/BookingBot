from commands import TextHandler
from telegram import Update, Bot
from telegram.message import Message
import telegram
from booking import Booking


class StartCommand(TextHandler):
    """
    Class that handle the start and the help command.
    This class show to the user the help message.
    """

    # TODO: Implement an administration logic to made the first user that interact with the bot an administrator?
    def __init__(self, booking: Booking):
        super(StartCommand, self).__init__(booking, ['start', 'help'])
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
