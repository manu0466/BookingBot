from injector import inject
from telegram import Update, Bot
from telegram.ext import Dispatcher

from booking.scheduler import Scheduler
from bot.handler.filter import RegexFilter, IsAdminHandlerFilter
from . import FilterableHandler


class StartSchedulerHandler(FilterableHandler):

    @inject
    def __init__(self, scheduler: Scheduler, is_admin_filter: IsAdminHandlerFilter):
        super().__init__()
        self._scheduler = scheduler
        self.add_filter(RegexFilter(['\start_scheduler'], case_sensitive=True))
        self.add_filter(is_admin_filter)

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        # self._scheduler.start()
        bot = dispatcher.bot  # type: Bot
        bot.send_message(update.message.chat_id, "Scheduler started")
