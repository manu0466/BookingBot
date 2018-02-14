from injector import Module, provider, singleton

from booking.scheduler import Scheduler
from .Booking import Booking
from .source import EventsSource, ClassroomSource, UserSource
from .source.event import Event
from .source.user import User


class BookingModule(Module):

    @provider
    @singleton
    def booking(self, events_source: EventsSource, classroom_source: ClassroomSource,
                user_source: UserSource, scheduler: Scheduler) -> Booking:
        return Booking(events_source, classroom_source, user_source, scheduler)
