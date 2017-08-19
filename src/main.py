#!/usr/bin/env python
import logging
from telegram.ext import Updater
import configurations
from booking import Booking
from commands.start import StartCommand
from commands.now import NowCommand
from commands.at import AtCommand
from commands.decorator import CommandDecorator
from commands.events import BuildingHandler, ClassroomHandler, GetBuildingsHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():

    # Starts the bot booking
    booking = Booking()
    booking.start_scheduler()

    # Create the Updater and pass it your bot's token.
    updater = Updater(configurations.API_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # Adds the commands
    dp.add_handler(CommandDecorator(StartCommand(booking=booking)))
    dp.add_handler(NowCommand(booking=booking))
    dp.add_handler(AtCommand(booking=booking))
    dp.add_handler(CommandDecorator(BuildingHandler(booking)))
    classroom_handler = ClassroomHandler(booking)
    dp.add_handler(CommandDecorator(classroom_handler))
    dp.add_handler(classroom_handler)
    dp.add_handler(CommandDecorator(GetBuildingsHandler(booking)))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    print("Starting...")
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    print("Bot online!")
    updater.idle()


if __name__ == '__main__':
    main()
