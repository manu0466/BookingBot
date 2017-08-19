from booking import Booking, EventsSource, ClassroomSource
from abc import abstractmethod
from telegram.ext import Handler
from telegram import Bot, Update


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
        self.execute(dispatcher.bot, update)
        return True

    def get_event_source(self) -> EventsSource:
        return self.backend.get_events_source()

    def get_classroom_source(self) -> ClassroomSource:
        return self.backend.get_classroom_source()

    @abstractmethod
    def execute(self, bot: Bot, update: Update):
        """
        Method called when one of the command passed in the constructor is received.
        :param bot: Object that represents the Telegram Bot.
        :param update: Object that represents a Telegram Update.
        """
        pass
