import telegram
from telegram import Update, Bot, Message
from telegram.ext import Dispatcher


def typing(func):
    def func_wrapper(self, update: Update, dispatcher: Dispatcher):
        # type
        bot = dispatcher.bot  # type: Bot
        message = update.message  # type: Message
        bot.send_chat_action(chat_id=message.chat_id, action=telegram.ChatAction.TYPING)
        result = func(self, update, dispatcher)
        # stop
        return result
    return func_wrapper
