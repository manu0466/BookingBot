import telegram
from injector import inject
from telegram import Update
from telegram.ext import Dispatcher

from .FilterableHandler import FilterableHandler
from bot.handler.filter import RegexFilter
from booking.usecase import EventsUseCase, ClassroomsUseCase
from booking.scheduler import Scheduler, SchedulerStatus


class ClassRoomEventHandler(FilterableHandler):

    @inject
    def __init__(self, events_uc: EventsUseCase, classrooms_uc: ClassroomsUseCase, scheduler: Scheduler):
        super().__init__()
        self._events_uc = events_uc
        self._classrooms_uc = classrooms_uc
        self._classrooms_map = {}
        scheduler.on_status_changed().subscribe(self.on_scheduler_status_changed)

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        class_name = update.message.text  # type: str
        if class_name.startswith('/'):
            class_name = class_name[1:]
        class_name = class_name.lower()
        events = self._events_uc.get_today_events(self._classrooms_map[class_name])
        message = ""
        if len(events) > 0:
            for event in events:
                event_name = event.get_name().replace('*', '')
                message += "*{0}*\nBegin at: {1}\nEnd at: {2}\n\n".format(event_name,
                                                                          event.get_begin().strftime("%H:%M"),
                                                                          event.get_end().strftime("%H:%M"))
        else:
            message = "No scheduled events"
        dispatcher.bot.send_message(chat_id=chat_id, text=message, parse_mode=telegram.ParseMode.MARKDOWN)
        return True

    def on_scheduler_status_changed(self, new_status: SchedulerStatus):
        if new_status != SchedulerStatus.COMPLETED:
            self.clear_filters()
            self._classrooms_map.clear()
        else:
            classrooms = []
            for classroom in self._classrooms_uc.get_classrooms():
                classroom_name = classroom.get_name().lower()
                self._classrooms_map[classroom_name] = classroom.get_identifier()
                classrooms.append(classroom_name)
            self.add_filter(RegexFilter(classrooms, case_sensitive=False, handle_command=True))
