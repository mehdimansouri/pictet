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

#Setting the variable for the search term
date_since = "2019-01-01"
teams= ['76ers', 'Blazers', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics',
       'Clippers', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz',
       'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets',
       'Nuggets', 'Pacers', 'Pelicans', 'Pistons', 'Raptors', 'Rockets',
       'Spurs', 'Suns', 'Thunder', 'Timberwolves', 'Warriors', 'Wizards']

for team in teams:
    print("Tweets about NBA team {}".format(team))
    word = team
    #Storing Tweets returned from the search. We are using geocode for a city and specifying a radius of 80miles
    tweets = tweepy.Cursor(api.search,q=word, lang="en", since=date_since)
    #Dumping Tweets to a json
    with open('~/Documents/Pictet/data/tweets.json', 'a') as out:
        for tweet in tweets:
            response=json.dumps(tweet._json)
            out.write(response+"\n")
    out.close()