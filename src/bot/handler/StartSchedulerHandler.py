from datetime import datetime, timedelta

from injector import inject
from telegram import Update, Bot
from telegram.ext import Dispatcher

from booking.scheduler import Scheduler, SchedulerInfo, SchedulerStatus
from bot.handler.filter import RegexFilter, IsAdminHandlerFilter
from . import FilterableHandler


class StartSchedulerHandler(FilterableHandler):

    @inject
    def __init__(self, scheduler: Scheduler, is_admin_filter: IsAdminHandlerFilter):
        super().__init__()
        self._scheduler = scheduler
        self.add_filter(RegexFilter(['/start_scheduler'], case_sensitive=True))
        self.add_filter(is_admin_filter)
        self._waiting_users = []
        self._scheduler_status = SchedulerStatus.IDLE
        self._bot = None
        self._scheduler.on_new_info().subscribe(self._on_scheduler_status_changed)

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        bot = dispatcher.bot  # type: Bot
        if update.message.chat_id not in self._waiting_users:
            self._waiting_users.append(update.message.chat_id)

        if self._scheduler_status != SchedulerStatus.RUNNING:
            self._scheduler.re_schedule()
            self._bot = bot
            bot.send_message(update.message.chat_id, "Scheduler started")
        else:
            bot.send_message(update.message.chat_id, "Scheduler already running.")
        return True

    def _on_scheduler_status_changed(self, new_info: SchedulerInfo):
        if new_info.status == SchedulerStatus.COMPLETED:
            if self._bot and len(self._waiting_users) > 0:
                next_refresh = datetime.now() + timedelta(seconds=new_info.next_refresh)
                message = "Schedule completed.\nNext refresh at {0}\nTotal Events: {1}".format(
                    next_refresh.strftime("%H:%M"), new_info.total_events)
                for user in self._waiting_users:
                    self._bot.send_message(user, message)
                self._waiting_users.clear()
                self._bot = None
