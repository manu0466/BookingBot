from bot.handler import FilterableHandler
from bot.handler.filter import RegexFilter


class EventsHandler(FilterableHandler):

    def __int__(self):
        self.add_filter(RegexFilter(['/events', 'events'], case_sensitive=False, exact_match=True))

    def handle_update(self, update, dispatcher):
        pass

