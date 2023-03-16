import json
import discord
import os
import boto3

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
TOKEN = os.environ['DISCORD_BOT_TOKEN']

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


# Initialization
def create_discord_bot():
    intents = discord.Intents.default()
    intents.messages = True
    intents.reactions = True
    intents.message_content = True  # Enable message content intent
    return discord.Client(intents=intents)

discord_bot = create_discord_bot()

# File to store the shopping list
shopping_list_file = "shopping_list.json"

# Load the shopping list from file
def load_shopping_list():
    try:
        s3_client.download_file(S3_BUCKET_NAME, shopping_list_file, shopping_list_file)
        with open(shopping_list_file, "r") as f:
            return json.load(f)
    except Exception:
        return []

# Save the shopping list to file
def save_shopping_list(shopping_list):
    with open(shopping_list_file, "w") as f:
        json.dump(shopping_list, f)
    s3_client.upload_file(shopping_list_file, S3_BUCKET_NAME, shopping_list_file)


# Load the shopping list
shopping_list = load_shopping_list()


def is_item(content):
    # Customize this function to better identify items.
    # For example, you could use a list of keywords or a regular expression.
    return len(content.split()) <= 5 and content.lower() != "list"


def format_shopping_list_with_checkboxes(shopping_list):
    formatted_list = "\n".join(
        f"{i+1}. {item}" for i, item in enumerate(shopping_list))
    return f"**Shopping List**\n{formatted_list}" if shopping_list else "The shopping list is empty."


def create_discord_bot():
    return discord.Client(intents=discord.Intents.default())


async def display_shopping_list(channel):
    await channel.purge(limit=len(shopping_list), check=lambda m: m.author == discord_bot.user)  # Clear previous shopping list messages

    for item in shopping_list:
        item_message = await channel.send(f"- {item}")
        await item_message.add_reaction("✅")

# Event listeners


@discord_bot.event
async def on_message(message):
    content = message.content
    print(f"Received message: {message}")  # Print the received message

    # If the message is from the bot itself, ignore it
    if message.author == discord_bot.user:
        print("Message is from the bot, ignoring.")
        return

    # Add an item to the shopping list
    if is_item(content):
        item = content
        shopping_list.append(item)
        save_shopping_list(shopping_list)
        print(f"Added item: {item}")  # Print the added item
    else:
        print("Message is not an item.")  # Print that the message is not recognized as an item

    # Return the user's shopping list with checkboxes
    if content.lower() == 'list':
        if not shopping_list:
            await message.channel.send("The shopping list is empty.")
            return
        # Clear all previous messages from the channel
        await message.channel.purge(limit=1000)

        # Display the updated shopping list
        await display_shopping_list(message.channel)
    else:    
        print("Message is not 'shopping list'.")  # Print that the message is not the 'shopping list' command    




@discord_bot.event
async def on_reaction_add(reaction, user):
    # Ignore the bot's own reactions
    if user == discord_bot.user:
        return

    # Check if the reaction is on a shopping list item message
    if reaction.emoji == "✅" and reaction.message.author == discord_bot.user:
        item_text = reaction.message.content[2:]  # Remove the "- " prefix from the item text
        if item_text in shopping_list:
            shopping_list.remove(item_text)
            save_shopping_list(shopping_list)

        # Delete the checked item message
        await reaction.message.delete()

# Run the bot
discord_bot.run(TOKEN)
