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
        if not self._users_uc.is_user_present(message.from_user.id):
            self._users_uc.add_user(User(message.from_user.username, message.from_user.id))
            logger.info("Added user: {}".format(message.from_user.username))
        return False

    def handle_update(self, update, dispatcher):
        return False
