from commands import TextHandler
from telegram import Update, Bot
import telegram
from booking import Booking, User


class StartCommand(TextHandler):
    """
    Class that handle the start command.
    """
    def __init__(self, booking: Booking):
        super(StartCommand, self).__init__(booking, ['start'])
        self._message = ("Hi, welcome into @BookingMathUniPd_bot\n"
                         "To know how the bot works you can use the /help command.\n"
                         "If you found some bugs or you have some tips to improve the bot feel "
                         "free to contact me at @ManuelTuretta.")

    def execute(self, chat_id,  bot: Bot, update: Update):
        bot.send_message(chat_id,
                         text=self._message)
        user_source = self.get_user_source()
        user_source.get_all_users()
        if len(user_source.get_all_users()) == 0:
            user_source.add_user(User(update.message.from_user.name, chat_id, User.Role.ADMIN.value))
            bot.send_message(chat_id, "You are now admin")
        elif user_source.get_user_by_identifier(chat_id) is None:
            user_source.add_user(User(update.message.from_user.name, chat_id, User.Role.USER.value))

        return True

