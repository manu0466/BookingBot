from injector import inject

from booking.usecase import ClassroomsUseCase
from bot import Message
from bot.handler.filter import HandlerFilter


class ClassNameFilter(HandlerFilter):

    @inject
    def __init__(self, classrooms_uc: ClassroomsUseCase):
        self.classrooms_uc = classrooms_uc
        self._classrooms = None

    def filter(self, message: Message) -> bool:
        return self.classrooms_uc.is_classroom_present(message.get_escaped_text())
