import os
import sys
import json
import requests
import tweepy
from dotenv import load_dotenv
load_dotenv()

wordnik_token = '32ab1d2959900dfbce8390c926f0518ddb193d1a96627a618'

URL = 'http://api.wordnik.com/v4/words.json/randomWords'
PARAMS = {'api_key': wordnik_token}
req = requests.get(url = URL, params = PARAMS) 
data = req.json()
for words in data:
    print(words)

def setup_api():
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
    return tweepy.API(auth)

def post_tweet(self):
    api = setup_api()
    tweet = 'hi'
    status = api.update_status(status=tweet)
    return 'Tweet Posted'