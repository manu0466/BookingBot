import telegram
from injector import inject
from telegram import Update, Message
from telegram.ext import Handler
import logging

from booking import User
from booking.usecase import UsersUseCase

logger = logging.getLogger(__name__)


class LogHandler(Handler):

    @inject
    def __init__(self, user_uc: UsersUseCase):
        super().__init__(None)
        self._users_uc = user_uc

    def check_update(self, update: Update):
        message = update.message  # type: Message
        logger.info("Incomming message {0}, from: {1}".format(message.text, message.from_user))
        tg_user = message.from_user  # type: telegram.User
        if not self._users_uc.is_user_present(tg_user.id):
            user = User(tg_user.username, tg_user.first_name, tg_user.last_name, tg_user.id)
            if self._users_uc.get_user_count() == 0:
                user.set_role(User.Role.ADMIN)
            self._users_uc.add_user(user)
            logger.info("Added user: {0} {1} {2}".format(tg_user.username, tg_user.first_name, tg_user.last_name))
        return False

    def handle_update(self, update, dispatcher):
        return False
