from datetime import datetime
import telegram
from telegram import Update, Bot
from booking import Booking
from commands import TextHandler


class NowCommand(TextHandler):

    def __init__(self, booking: Booking):
        super(NowCommand, self).__init__(booking, ['now'])

    def execute(self, bot: Bot, update: Update):
        chat_id = update.message.chat_id
        bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
        events_source = self.get_event_source()
        classroom_source = self.get_classroom_source()
        time = datetime.now()
        text = "*Current time: " + time.strftime("%H:%M") + "*\n"
        for classroom in classroom_source.get_all_classrooms():
            if events_source.is_classroom_free(classroom.get_identifier(), date_time=time):
                event = events_source.get_next_event(classroom.get_identifier(), time)
                if event is not None:
                    text += "*" + classroom.get_name() + "* free untill " + event.get_begin().strftime("%H:%M") + "\n"
                else:
                    text += "*" + classroom.get_name() + "* no events untill close\n"
        bot.send_message(chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)
