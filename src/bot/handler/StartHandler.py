from telegram import Update, Bot
from injector import inject
from telegram.ext import Dispatcher

from booking import User
from booking.usecase import UsersUseCase

from bot.handler import FilterableHandler
from bot.handler.filter import RegexFilter


class StartHandler(FilterableHandler):
    """
    Class that handle the start command.
    """
    @inject
    def __init__(self, user_uc: UsersUseCase):
        super().__init__()
        self.add_filter(RegexFilter(['/start'], case_sensitive=True, exact_match=True))
        self._users_uc = user_uc
        self._message = ("Hi, welcome into @BookingMathUniPd_bot\n"
                         "To know how the bot works you can use the /help command.\n"
                         "If you found some bugs or you have some tips to improve the bot feel "
                         "free to contact me at @ManuelTuretta.")

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        bot = dispatcher.bot
        bot.send_message(chat_id, text=self._message)

        if self._users_uc.get_user_count() == 0:
            self._users_uc.add_user(User(update.message.from_user.name, chat_id, User.Role.ADMIN.value))
            bot.send_message(chat_id, "You are now admin")
        elif not self._users_uc.is_user_present(chat_id):
            self._users_uc.add_user(User(update.message.from_user.name, chat_id, User.Role.USER.value))
        return True

