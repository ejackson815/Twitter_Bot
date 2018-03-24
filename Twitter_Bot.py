
import tweepy
import time
import json
import random
import os

# Twitter API Keys
consumer_key = os.environ['consumer_key']
sconsumer_key = os.environ['sconsumer_key']
access_token = os.environ['access_token']
saccess_token = os.environ['saccess_token']

#Twitter Authentication
auth = tweepy.OAuthHandler(consumer_key, sconsumer_key)
auth.set_access_token(access_token, saccess_token)
api = tweepy.API(auth)
# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]
def TweetOut(tweet_number):
    random_quote = random.choice(happy_quotes)
    api.update_status(random_quote)

counter = 0
while(True):
    TweetOut(counter)
    time.sleep(60)
    counter = counter + 1
