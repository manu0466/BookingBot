from .HandlerDecorator import HandlerDecorator
from telegram import Update, Message


class AdminCommand(HandlerDecorator):

    """
    Decorator class to create a telegram handler that will be executed only if the user is admin.
    """

    def check_update(self, update: Update):
        result = False
        if isinstance(update, Update) and (update.message or update.edited_message):
            new_update = self.copy_update(update)
            message = new_update.message or new_update.edited_message  # type: Message
            if self.get_user_source().get_user_by_identifier(message.chat_id) is None:
                result = False
            else:
                result = True
        return result

