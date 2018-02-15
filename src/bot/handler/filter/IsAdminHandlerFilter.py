from injector import inject

from bot import Message
from bot.handler.filter import HandlerFilter
from booking.usecase import IsUserAdminUseCase


class IsAdminHandlerFilter(HandlerFilter):

    @inject
    def __init__(self, is_user_admin_uc: IsUserAdminUseCase):
        self._is_user_admin_uc = is_user_admin_uc

    def filter(self, message: Message) -> bool:
        return self._is_user_admin_uc.is_admin(message.get_sender_id())