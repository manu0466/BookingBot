from booking import Booking, EventsSource, ClassroomSource, UserSource
from abc import abstractmethod
from telegram.ext import Handler
from telegram import Bot, Update
import telegram


class AbstractBookingHandler(Handler):

    """"
    Base class that represents a simple command that interact with the Booking instance.
    """

    def __init__(self, backend: Booking):
        super(AbstractBookingHandler, self).__init__(None)
        self.backend = backend

    @abstractmethod
    def check_update(self, update):
        pass

    def handle_update(self, update, dispatcher):
        bot = dispatcher.bot
        chat_id = update.message.chat_id
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        return self.execute(chat_id, dispatcher.bot, update)

    def get_event_source(self) -> EventsSource:
        return self.backend.get_events_source()

    def get_classroom_source(self) -> ClassroomSource:
        return self.backend.get_classroom_source()

    def get_user_source(self) -> UserSource:
        return self.backend.get_user_source()

    @abstractmethod
    def execute(self, chat_id,  bot: Bot, update: Update):
        """
        Method called when one of the command passed in the constructor is received.
        :param chat_id: Unique identifier of a conversation.
        :param bot: Object that represents the Telegram Bot.
        :param update: Object that represents a Telegram Update.
        """
        pass
