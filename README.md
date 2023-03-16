# Shopping List Discord Bot

A simple Discord bot that allows users to create and manage a shopping list. The bot is designed to be deployed on Heroku and uses Amazon S3 for data storage.

## Setup

1. Clone this repository.
2. Install the required packages using `pip install -r requirements.txt`.
3. Set up your Amazon S3 bucket and AWS credentials (see the "Amazon S3 Setup" section below).
4. Replace the necessary environment variables (see the "Environment Variables" section below).
5. Create a new Discord bot (see the "Create Discord Bot and Generate Token" section) and invite it to your server using the generated invite link.
6. Run the bot locally using `python bringer_bot.py` or deploy it to Heroku (see the "Deploying to Heroku" section).

### Amazon S3 Setup

Follow these steps to set up an Amazon S3 bucket:

1. Sign up for an AWS account at [aws.amazon.com](https://aws.amazon.com/).
2. Create an S3 bucket in the [AWS Management Console](https://console.aws.amazon.com/).
3. Set up AWS credentials (Access Key ID and Secret Access Key) using the [IAM Management Console](https://console.aws.amazon.com/iam/).

### Environment Variables

Before deploying the bot, you need to replace the following environment variables with your own values:

- `DISCORD_BOT_TOKEN`: Your Discord bot token.
- `AWS_ACCESS_KEY_ID`: Your AWS Access Key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS Secret Access Key.
- `S3_BUCKET_NAME`: The name of the Amazon S3 bucket you created.

To set environment variables locally, create a `.env_variables` file (make sure it's included in the .gitignore) and add the variables as follows:

````bash
export VARIABLE_NAME='VARIABLE_VALUE'
````

Replace `VARIABLE_NAME` and `VARIABLE_VALUE` with the appropriate values.

To set environment variables on Heroku, use the following command:

````bash
heroku config:set VARIABLE_NAME=VARIABLE_VALUE --app YOUR_APP_NAME
````
Replace `VARIABLE_NAME`, `VARIABLE_VALUE`, and `YOUR_APP_NAME` with the appropriate values.

### Create Discord Bot and Generate Token

Follow these steps to create a Discord bot and generate its token:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account.
2. Click on the "New Application" button in the top right corner.
3. Enter a name for your application and click "Create".
4. Navigate to the "Bot" tab in the left sidebar and click the "Add Bot" button.
5. Confirm by clicking "Yes, do it!" in the prompt.
6. Your bot has been created. To get the bot token, click the "Copy" button under the "TOKEN" section. Keep the token secret and do not share it with others.

Now that you have the bot token, use it to replace the `DISCORD_BOT_TOKEN` environment variable in your project. Make sure to invite your bot to your Discord server using the generated invite link.

### Deploy to Heroku

Follow these steps to deploy your Discord bot to Heroku:

1. [Create a Heroku account](https://signup.heroku.com/) if you don't have one.
2. [Install the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and log in to your account.
3. In the terminal, navigate to your bot's root directory and run `heroku create` to create a new Heroku app.
4. Set the necessary environment variables for your Heroku app using the `heroku config:set` command (see the "Environment Variables" section for details).
5. Deploy your bot to Heroku by running `git push heroku main`. Replace `main` with your branch name if you're using a different branch.
6. Scale your bot's dyno to start the bot on Heroku: `heroku ps:scale worker=1 --app YOUR_APP_NAME`. Replace `YOUR_APP_NAME` with the name of your Heroku app and `worker` with the appropriate dyno type if you're using a different type.

## Run Locally

To run the bot locally, follow these steps:

1. Make sure you have Python 3.6 or higher installed on your machine.
2. Create a virtual environment using the following command:
````bash
python3 -m venv env
````
3. Activate the virtual environment:
On macOS and Linux:
````bash
source env/bin/activate
````
On Windows:
````bash
.\env\Scripts\activate
````

4. Install the required packages using `pip install -r requirements.txt`.
5. Set the necessary environment variables in your local environment (see the "Environment Variables" section for details). 
6. Run `source .env_variables` to set the environment variables in your Python environment.
7. Run the Python script by running `python bringer_bot.py` in your terminal.

## Usage

### Add an item to the shopping list
Simply send a message in the channel containing the item you want to add. The item must be five words or fewer and cannot be "list" (case-insensitive). The bot will automatically add the item to the shopping list and save it to a JSON file.

### Display the shopping list
To display the shopping list, send a message with the content "list" (case-insensitive). The bot will clear all previous messages from the channel and display the shopping list with checkboxes next to each item.

### Check off items from the list
To mark an item as completed, add a "✅" reaction to the corresponding message. The bot will remove the item from the shopping list, save the updated list, and delete the item message from the channel.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Customization
You can customize the `is_item` function to better identify items, for example, by using a list of keywords or a regular expression.