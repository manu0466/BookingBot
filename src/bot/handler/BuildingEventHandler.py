import telegram
from injector import inject
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Dispatcher

from bot.handler.decorator.TypingDecorator import typing
from .FilterableHandler import FilterableHandler
from bot.handler.filter import RegexFilter
from booking.usecase import EventsUseCase, BuildingsUseCase, ClassroomsUseCase
from booking.scheduler import Scheduler, SchedulerStatus


class BuildingEventHandler(FilterableHandler):

    @inject
    def __init__(self, events_uc: EventsUseCase,
                 buildings_uc: BuildingsUseCase,
                 classrooms_uc: ClassroomsUseCase,
                 scheduler: Scheduler):
        super().__init__()
        self._events_uc = events_uc
        self._buildings_uc = buildings_uc
        self._classrooms_uc = classrooms_uc
        self._buildings_map = {}
        scheduler.on_status_changed().subscribe(self.on_scheduler_status_changed)

    @typing
    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        building_name = update.message.text  # type: str
        if building_name.startswith('/'):
            building_name = building_name[1:]
        building_name = building_name.lower()

        handled = False
        if building_name in self._buildings_map:
            handled = True
            building_identifier = self._buildings_map[building_name]
            classrooms = self._classrooms_uc.get_classrooms(building_identifier)
            keyboard_button = []
            counter = 0
            row = -1
            for classroom in classrooms:
                if counter == 0:
                    keyboard_button.append([])
                    row += 1
                keyboard_button[row].append(KeyboardButton("/"+classroom.get_name().lower()))
                counter += 1
                if counter == 3:
                    counter = 0
            keyboard_button.append(["/buildings"])
            reply_keyboard = ReplyKeyboardMarkup(keyboard_button)
            dispatcher.bot.send_message(chat_id=chat_id, text="Available classrooms", reply_markup=reply_keyboard)
        return handled

    def on_scheduler_status_changed(self, new_status: SchedulerStatus):
        if new_status != SchedulerStatus.COMPLETED:
            self.clear_filters()
            self._buildings_map.clear()
        else:
            buildings = []
            for building in self._buildings_uc.get_buildings():
                building_name = building.get_name().lower().replace(" ", "_")
                self._buildings_map[building_name] = building.get_identifier()
                buildings.append(building_name)
            self.add_filter(RegexFilter(buildings, case_sensitive=False, handle_command=True))
