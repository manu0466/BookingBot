from datetime import datetime
import telegram
from telegram import Update, Bot
from injector import inject

from booking.usecase import EventsUseCase, ClassroomsUseCase
from . import FilterableHandler
from .filter import RegexFilter


class NowHandler(FilterableHandler):

    """
    Class that represents the now command.
    This command will show to the user the currently free classroom.
    """
    @inject
    def __init__(self, events_uc: EventsUseCase, classrooms_uc: ClassroomsUseCase):
        super().__init__()
        self._events_uc = events_uc
        self._classrooms_uc = classrooms_uc
        self.add_filter(RegexFilter(['now', '/now'], case_sensitive=False, exact_match=True))

    def handle_update(self, update, dispatcher):
        pass

    def execute(self, chat_id, bot: Bot, update: Update):
        time = datetime.now()
        text = "*Current time: " + time.strftime("%H:%M") + "*\n"
        for classroom in self._classrooms_uc.get_classrooms():
            if self._classrooms_uc.is_classroom_free(classroom.get_identifier(), time=time):
                text += "/" + classroom.get_name().lower()
                event = self._events_uc.get_next_event(classroom.get_identifier(), time)
                if event is not None:
                    text += " free until " + event.get_begin().strftime("%H:%M") + "\n"
                else:
                    text += " no events until close\n"
        bot.send_message(chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
        return True
