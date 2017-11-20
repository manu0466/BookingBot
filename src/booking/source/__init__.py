from .classroom import ClassroomSourceProvider, ClassroomSource, Classroom, Building
from .event import EventSourceProvider, EventsSource
from .user import UserSourceProvider, UserSource
import dependency_injector.containers as containers


class SourceContainer(containers.DeclarativeContainer):

    users = UserSourceProvider

    events = EventSourceProvider

    classrooms = ClassroomSourceProvider
