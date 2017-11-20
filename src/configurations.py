import os

#
# Telegram configuration
#

# Telegram bot API token
API_TOKEN = "133010209:AAGN-0LacvgfBS_7OKbS-lioISJzkfJORF0"

#
# SQL configurations
#

# SQL server url
BOT_EVENTS_SQL_SERVER = "localhost"
# SQL database name
BOT_SQL_DB = "booking"
# SQL database user
BOT_SQL_USER = "booking-bot"
# SQL database user password
BOT_SQL_PASSWORD = "botpassword"

#
#  Scheduler configuration
#

# Path where wil be stored the configurations
SCHEDULER_CONFIG_PATH = os.path.dirname(__file__)
# File that holds the log
LOG_FILENAME = os.path.dirname(__file__) + "/booking.log"
