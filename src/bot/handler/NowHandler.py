from datetime import datetime
import telegram
from injector import inject

from bot.handler.decorator.TypingDecorator import typing
from . import FilterableHandler
from bot.handler.filter import RegexFilter
from booking.usecase import EventsUseCase, ClassroomsUseCase


class NowHandler(FilterableHandler):

    """
    Class that represents the now, free command.
    """
    @inject
    def __init__(self, events_uc: EventsUseCase, classrooms_uc: ClassroomsUseCase):
        # Regex to validate the time format
        super().__init__()
        self._events_uc = events_uc
        self._classrooms_uc = classrooms_uc
        self.add_filter(RegexFilter(['now', 'free'], case_sensitive=False, exact_match=True, handle_command=True))

    @typing
    def handle_update(self, update, dispatcher):
        time = datetime.now()
        text = "*Requested time: " + time.strftime("%H:%M") + "*\n"
        for classroom in self._classrooms_uc.get_classrooms():
            if self._classrooms_uc.is_classroom_free(classroom.get_identifier(), time=time):
                event = self._events_uc.get_next_event(classroom.get_identifier(), time)
                text += "/" + classroom.get_name().lower()
                if event is not None:
                    text += " free until " + event.get_begin().strftime("%H:%M") + "\n"
                else:
                    text += " no events until close\n"
        dispatcher.bot.send_message(update.message.chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
        return True
