from telegram import Update
from injector import inject
from telegram.ext import Dispatcher

from bot.handler import FilterableHandler
from bot.handler.decorator.TypingDecorator import typing
from bot.handler.filter import RegexFilter


class StartHandler(FilterableHandler):
    """
    Class that handle the start command.
    """
    @inject
    def __init__(self):
        super().__init__()
        self.add_filter(RegexFilter(['/start'], case_sensitive=True, exact_match=True))
        self._message = ("Hi, welcome into @BookingMathUniPd_bot\n"
                         "To know how the bot works you can use the /help command.\n"
                         "If you found some bugs or you have some tips to improve the bot feel "
                         "free to contact me at @ManuelTuretta.")

    @typing
    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        bot = dispatcher.bot
        bot.send_message(chat_id, text=self._message)
        return True

