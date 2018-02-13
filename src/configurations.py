import os

#
# Telegram configuration
#

# Telegram bot API token
API_TOKEN = "API_TOKEN"

# Path where wil be stored the configurations
SCHEDULER_CONFIG_PATH = os.path.dirname(__file__)

# File that holds the log
LOG_FILENAME = os.path.dirname(__file__) + "/booking.log"

# Database file where will be stored all the events
SQLITE_DB = os.path.dirname(__file__) + "/booking.db"
