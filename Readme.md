# Booking Bot

A simple Telegram bot to check the status of the classrooms of the UniPd's 
Mathematic Department. 


## Installation

First install all the python dependencies with this command: 
`pip insatll -r requirements.txt`.  

The second step is to initialize the MySql database where will be saved the
data of the classroom events.
You can create a docker container running the `init_docker_db.sh` script inside
the *scripts* folder or self creating a MySql database with the 
`init_db.sql` script. 

**NOTE**: In case you have edited the database configuration you must update the 
**configuration.py** file!

Last step is to add your Telegram API token in the **configuration.py** file.


## Usage

To start the bot simply run: `python main.py`

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

**Version 1.0.0**
* First release

## Credits

Credit to Noam Meltzer for the [Python telegram library](https://github.com/python-telegram-bot/python-telegram-bot)

## License

This software is release under GNU General Public License, version 2.