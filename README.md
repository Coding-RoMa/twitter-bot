# Twitter Bot

A Twitter bot designed to interact with selected Twitter accounts. The bot fetches the latest text tweets, saves them locally, and provides the option to like them. This bot is hosted on PythonAnywhere and uses Flask to handle web requests.

## Features:

- Retrieve Latest Text Tweets: Fetches the latest text tweets from selected Twitter accounts and saves them in a local file.
- Like Tweets: Automatically likes the latest tweet from the selected accounts. Also provides an option to manually like the latest tweet via an endpoint.
- Web Endpoints with Flask: Exposes web endpoints to manually trigger functionalities and check the bot's status.
- PythonAnywhere Deployment: The bot is designed to be easily deployable on PythonAnywhere, a cloud platform that allows Python applications to run in the cloud.
- Logging: Maintains a log of all activities and errors for easy debugging.

## Language and Libraries:

Language: Python

### Main Libraries:
Tweepy: For interacting with the Twitter API.
Flask: To create web endpoints and manage web requests.

## Setup:
### Clone the Repository:

git clone https://github.com/Coding-RoMa/twitter-bot.git
cd twitter-bot

## Install Dependencies:

pip install tweepy flask

## Set Up Twitter API Credentials:

- Create a Twitter Developer account and create an app.
- Fetch the API Key, API Secret Key, Access Token, and Access Token Secret.
- Update the twitterBot.py file with these credentials.

  ### Note:
  The bot doesn't work with the free Twitter Developer account. 


## Run the Bot:

python twitterBot.py


## Endpoints:

/ - Check if the bot is running.

/like_and_save - Like the latest tweet and save text tweets for the selected accounts.

/like_latest_tweet - Like the latest tweets for the selected accounts.

/retrieve_tweets - Retrieve saved tweets.


## Important note

Pay attention to update the last line of your WSGI file: 

from your-app-name import app as application
