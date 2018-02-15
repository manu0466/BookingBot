from telegram import Update
from telegram.ext import Handler
from typing import List

from bot.handler.filter import HandlerFilter
from bot import Message


class FilterableHandler(Handler):

    def __init__(self):
        self._filters = []  # type: List[HandlerFilter]
        self._keys_map = {}
        super().__init__(None)

    def add_filter(self, handler_filter: HandlerFilter, key: str = None):
        self._filters.append(handler_filter)
        if key:
            index = len(self._filters) - 1
            self._keys_map[key] = index
        return self

    def add_filters(self, handler_filters: List[HandlerFilter]):
        for f in handler_filters:
            self.add_filter(f)
        return self

    def remove_filter(self, key: str):
        if key in self._keys_map:
            self._filters.pop(self._keys_map[key])
        else:
            raise RuntimeError('No filter with key: {0} founded.')

    def clear_filters(self):
        self._filters.clear()
        self._keys_map.clear()
        return self

    def check_update(self, update: Update):
        result = False
        if len(self._filters) > 0 and isinstance(update, Update) and (update.message or update.edited_message):
            tg_message = update.message or update.edited_message
            user_id = update.message.chat_id
            message = Message(tg_message.text, user_id)
            i = 0
            result = True
            while result and i < len(self._filters):
                result = self._filters[i].filter(message)
                i = i + 1

        return result

