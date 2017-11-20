import dependency_injector.providers as providers
from .Booking import Booking
from .source import EventsSource, ClassroomSource, UserSource
from .source import SourceContainer
from .source.event import Event
from .source.user import User
from .scheduler import SchedulerProvider

BookingProvider = providers.Singleton(Booking, events_source=SourceContainer.events,
                                      classroom_source=SourceContainer.classrooms,
                                      user_source=SourceContainer.users,
                                      scheduler=SchedulerProvider)

