# Bringer - Shopping List Bot for Discord
The Shopping List Bot is a simple Discord bot that allows users to create, manage, and interact with a shopping list within a Discord server. The bot is built using the Discord.py library and deployed on Heroku.

## Features
Add items to the shopping list
Display the shopping list with checkboxes
Check off items from the list by reacting with a "✅" emoji

## Setup
1. Create a new Discord application and bot in the Discord Developer Portal.
2. Invite the bot to your server using the OAuth2 URL.
3. Deploy the bot to Heroku and set the DISCORD_BOT_TOKEN environment variable to your bot's token.

## Usage

### Add an item to the shopping list
Simply send a message in the channel containing the item you want to add. The item must be five words or fewer and cannot be "list" (case-insensitive). The bot will automatically add the item to the shopping list and save it to a JSON file.

### Display the shopping list
To display the shopping list, send a message with the content "list" (case-insensitive). The bot will clear all previous messages from the channel and display the shopping list with checkboxes next to each item.

### Check off items from the list
To mark an item as completed, add a "✅" reaction to the corresponding message. The bot will remove the item from the shopping list, save the updated list, and delete the item message from the channel.

## Code Overview

### Dependencies
````python
import json
import discord
import os
````

### Load and save the shopping list
The shopping list is stored in a JSON file named `shopping_list.json`. Functions `load_shopping_list` and `save_shopping_list` are provided to load and save the list, respectively.

### Create the Discord bot instance
The `create_discord_bot` function creates a new instance of the `discord.Client` with the necessary intents to handle messages and reactions.

### Main event listeners
Two event listeners are implemented in the bot:

- `on_message`: This listener handles incoming messages and performs the following tasks:
    - Add an item to the shopping list if the message content is recognized as an item
    - Display the shopping list if the message content is "list"
- `on_reaction_add`: This listener handles reaction additions and performs the following tasks:
    - Remove an item from the shopping list if the reaction is a "✅" and the reaction message contains an item from the list

### Run the bot
The bot is run using the `discord_bot.run(TOKEN)` command with the bot token obtained from the environment variable `DISCORD_BOT_TOKEN`.

### Customization
You can customize the `is_item` function to better identify items, for example, by using a list of keywords or a regular expression.