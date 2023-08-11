from flask import Flask, jsonify
import tweepy
import time
import logging

app = Flask(__name__)

# Logging setup
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Set up API keys
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret-key'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

selected_accounts = ['account1', 'account2', 'account3'] #add tokens in the following form: for example, @crypto_website should be included as crypto_website

def like_and_save_tweets():
    messages = []
    for account in selected_accounts:
        try:
            tweets = api.user_timeline(screen_name=account, count=1)
            if tweets:
                tweet = tweets[0]
                if not tweet.favorited:
                    api.create_favorite(tweet.id)
                    messages.append(f"Liked latest tweet from {account}.")
                if tweet.text:
                    with open('tweets_for_review.txt', 'a') as file:
                        file.write(tweet.text + "\n")
                    messages.append(f"Saved tweet from {account}.")
            else:
                messages.append(f"No tweets found for {account}.")
        except Exception as e:
            msg = f"Error for account {account}: {str(e)}"
            logging.error(msg)
            messages.append(msg)
    return messages

@app.route('/')
def status():
    return "The bot is up and running!"

@app.route('/like_and_save')
def trigger_activity():
    messages = like_and_save_tweets()
    return jsonify(messages)

@app.route('/like_latest_tweet')
def trigger_like():
    messages = []
    for account in selected_accounts:
        try:
            tweets = api.user_timeline(screen_name=account, count=1)
            if tweets:
                tweet = tweets[0]
                if not tweet.favorited:
                    api.create_favorite(tweet.id)
                    messages.append(f"Liked latest tweet from {account}.")
            else:
                messages.append(f"No tweets found for {account}.")
        except Exception as e:
            msg = f"Error for account {account}: {str(e)}"
            logging.error(msg)
            messages.append(msg)
    return jsonify(messages)

@app.route('/retrieve_tweets')
def retrieve_tweets():
    with open('tweets_for_review.txt', 'r') as file:
        tweets = file.readlines()
    if tweets:
        return jsonify(tweets)
    else:
        return "No tweets found."

if __name__ == "__main__":
    app.run(debug=True)
    
