from injector import Module, provider, singleton
from .classroom import ClassroomSource, Classroom, Building
from .event import EventsSource
from .user import UserSource


class ClassRoomSourceModule(Module):

    @provider
    @singleton
    def class_room_source(self) -> ClassroomSource:
        from .classroom.database import DatabaseClassroomSource
        return DatabaseClassroomSource()


class EventsSourceModule(Module):

    @provider
    @singleton
    def class_room_source(self) -> EventsSource:
        from .event.database import DatabaseEventsSource
        return DatabaseEventsSource()


class UsersSourceModule(Module):

    @provider
    @singleton
    def class_room_source(self) -> UserSource:
        from .user.database import DatabaseUserSource
        return DatabaseUserSource()
