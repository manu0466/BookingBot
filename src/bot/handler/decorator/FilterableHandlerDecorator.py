from telegram import Update
from telegram.ext import Handler
from typing import List

from bot.handler.filter import HandlerFilter
from bot import Message


class FilterableHandlerDecorator(Handler):

    def __init__(self, handler: Handler):
        self._filters = []  # type: List[HandlerFilter]
        super().__init__(None)
        self._handler = handler

    def add_filter(self, handler_filter: HandlerFilter):
        self._filters.append(handler_filter)
        return self

    def add_filters(self, handler_filters: List[HandlerFilter]):
        for f in handler_filters:
            self.add_filter(f)
        return self

    def clear_filters(self):
        self._filters.clear()
        return self

    def check_update(self, update: Update):
        result = len(self._filters) <= 0
        if len(self._filters) > 0 and isinstance(update, Update) and (update.message or update.edited_message):
            text = update.message or update.edited_message
            user_id = update.message.chat_id
            message = Message(text, user_id)
            result = True
            i = 0
            while result and i < len(self._filters):
                result = self._filters[i].filter(message)
                i = i + 1

        return result and self._handler.check_update(update)

    def handle_update(self, update, dispatcher):
        self._handler.handle_update(update, dispatcher)

    def collect_optional_args(self, dispatcher, update=None):
        return self._handler.collect_optional_args(dispatcher, update)
