import threading

from injector import inject
from telegram import Bot, Update

from booking import Booking
from booking.scheduler.Scheduler import SchedulerStatus
from commands import AbstractBookingHandler


class SchedulerRefreshingHandler(AbstractBookingHandler):

    @inject
    def __init__(self, booking: Booking):
        super().__init__(booking)
        self._status = SchedulerStatus.IDLE
        self._lock = threading.RLock()
        self._message = "Sorry at the moment i'm refreshing the events :("
        booking.get_scheduler().on_status_changed() \
            .subscribe(self.handle_scheduler_status)

    def check_update(self, update):
        self._lock.acquire()
        should_handle = self._status != SchedulerStatus.COMPLETED
        self._lock.release()
        return should_handle

    def execute(self, chat_id, bot: Bot, update: Update):
        bot.send_message(chat_id,
                         text=self._message)

    def handle_scheduler_status(self, new_status: SchedulerStatus):
        self._lock.acquire()
        self._status = new_status
        self._lock.release()
        print("Scheduler status: {0}\n".format(new_status))

