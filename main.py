import os
import sys
import json
import requests
import tweepy
from dotenv import load_dotenv
load_dotenv()

def setup_api():
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
    return tweepy.API(auth)

def post_tweet(self):
    api = setup_api()
    tweet = 'hi'
    status = api.update_status(status=tweet)
    return 'Tweet Posted'