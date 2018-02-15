from injector import inject
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Dispatcher

from booking.scheduler import Scheduler, SchedulerStatus
from booking.usecase import BuildingsUseCase
from bot.handler import FilterableHandler
from bot.handler.filter import RegexFilter


class BuildingsKeyboardHandler(FilterableHandler):

    @inject
    def __init__(self, scheduler: Scheduler, buildings_uc: BuildingsUseCase):
        super().__init__()
        self.add_filter(RegexFilter(['/buildings']))
        self._buildings_uc = buildings_uc
        self._keyboard = None
        scheduler.on_status_changed().subscribe(self.on_scheduler_status_changed)

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        if self._keyboard:
            dispatcher.bot.send_message(chat_id=chat_id, text="Available buildings", reply_markup=self._keyboard)
        else:
            dispatcher.bot.send_message(chat_id=chat_id, text="Sorry, no buildings available")

        return True

    def on_scheduler_status_changed(self, new_status: SchedulerStatus):
        if new_status == SchedulerStatus.COMPLETED:
            self._keyboard = None
            buildings = [['/' + building.get_name().lower().replace(' ', '_')] for building in self._buildings_uc.get_buildings()]
            self._keyboard = ReplyKeyboardMarkup(buildings)
