from injector import inject
from telegram import Update
from telegram.ext import Dispatcher

from booking.usecase import UsersUseCase
from .FilterableHandler import FilterableHandler
from bot.handler.filter import IsAdminHandlerFilter, RegexFilter


class UsersHandler(FilterableHandler):

    @inject
    def __init__(self, is_admin_filer: IsAdminHandlerFilter, users_uc: UsersUseCase):
        super().__init__()
        self._users_uc = users_uc
        self.add_filter(is_admin_filer)
        self.add_filter(RegexFilter(['users'], handle_command=True, case_sensitive=False))

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        users = self._users_uc.get_users()
        message = "Users:\n"
        for user in users:
            message += "- {0} {1}\n".format(user.get_name(), user.get_role())
        dispatcher.bot.send_message(update.message.chat_id, message)
        return True
