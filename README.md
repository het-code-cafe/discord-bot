# Project Name

## Setup

1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.

## Adding Commands

To add a new command:

1. Create a new Folder in the `cogs/` directory. You may use a category here, in that directory please create a Python File. This file will represent a new command group (or "cog").
2. Define your command as a method within a class that inherits from `commands.Cog`.
3. Add your command to the `help.json` file in the `config/` directory. This will ensure that your command is included in the help message.

## Updating the Help Message

The help message is automatically generated from the `help.json` file. To update the help message, simply update the `help.json` file with the new command details.

## Running the Bot

To run the bot, execute the `main.py` file.

## License

This project is licensed under the terms of the LICENSE file.