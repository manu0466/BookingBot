#!/usr/bin/env python
import logging
from telegram.ext import Updater
from injector import Injector
import configurations

# DI imports
from booking.source import ClassRoomSourceModule, EventsSourceModule, UsersSourceModule
from booking.scheduler.settings import SettingSourceModule

from booking import Booking, BookingModule
from booking.scheduler import SchedulerModule
from bot.handler import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler(configurations.LOG_FILENAME),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():

    injector = Injector(modules=[ClassRoomSourceModule(),
                                 EventsSourceModule(),
                                 UsersSourceModule(),
                                 SettingSourceModule(),
                                 SchedulerModule(),
                                 BookingModule()])

    # Starts the bot booking
    booking = injector.get(Booking)  # type: Booking
    booking.start_scheduler()

    # Create the Updater and pass it your bot's token.
    updater = Updater(configurations.API_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    dp.add_handler(injector.get(LogHandler))
    dp.add_handler(injector.get(SchedulerRefreshingHandler))
    dp.add_handler(injector.get(StartSchedulerHandler))

    # Adds the commands
    dp.add_handler(injector.get(StartHandler))
    dp.add_handler(injector.get(HelpHandler))
    dp.add_handler(injector.get(NowHandler))
    dp.add_handler(injector.get(AtHandler))

    dp.add_handler(injector.get(BuildingsKeyboardHandler))
    dp.add_handler(injector.get(ClassRoomEventHandler))
    dp.add_handler(injector.get(BuildingEventHandler))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    logging.info("Starting...")
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    logging.info("Bot online!")
    updater.idle()


if __name__ == '__main__':
    main()
