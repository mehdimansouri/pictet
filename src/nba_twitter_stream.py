#Import the necessary methods from tweepy library
import tweepy
import json
import time
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamListener
from twitter_conf import api_key, api_secret_key,access_token, access_token_secret

#Creating the authentication handler
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Monitor the number of remaining calls and wait if running out of calls
api.wait_on_rate_limit = True
api.wait_on_rate_limit_notify = True

#Creating a new class TweetStream
class TweetStream(StreamListener):
    #Overriding the on_data method
    #on_data receives all messages and calls functions according to the message type
    def on_data(self, data):
        try:
            #Opening new TweetStream.json file in append mode
            with open('~/Documents/Pictet/data/TweetStream.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        return True
 
    def on_error(self, status):
        print(status)
        return True