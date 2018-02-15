import threading
from injector import inject
from telegram import Bot, Update
from telegram.ext import Handler, Dispatcher

from booking.scheduler.Scheduler import SchedulerStatus, Scheduler


class SchedulerRefreshingHandler(Handler):

    @inject
    def __init__(self, scheduler: Scheduler):
        super().__init__(None)
        self._status = SchedulerStatus.IDLE
        self._lock = threading.RLock()
        self._message = "Sorry at the moment i'm refreshing the events :("
        scheduler.on_status_changed() \
            .subscribe(self.handle_scheduler_status)

    def check_update(self, update):
        self._lock.acquire()
        should_handle = self._status != SchedulerStatus.COMPLETED
        self._lock.release()
        return should_handle

    def handle_update(self, update: Update, dispatcher: Dispatcher):
        chat_id = update.message.chat_id
        dispatcher.bot.send_message(chat_id, text=self._message)
        return True

    def handle_scheduler_status(self, new_status: SchedulerStatus):
        self._lock.acquire()
        self._status = new_status
        self._lock.release()
        print("Scheduler status: {0}\n".format(new_status))

