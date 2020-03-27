#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
access_key = "1149598966897491968-T8FLfpaeWT9HpjbssGiHA4wFkVv8Iy"
access_secret = "u1dbZbkshYkNDivTkmUcWEnwAWSPOdPm6pHsGYtDAMWQD"
consumer_key = "gTOkUJDZajQ8EMyGEHk6Qa4zl"
consumer_secret = "VsXlE4ZQjdZYbVYqxEI8wEGG62Wx2O9AREJc8LMZTH7tW8JEcV"

def get_all_tweets(screen_name):
#Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)

    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before {}".format(oldest))
    
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...{} tweets downloaded so far".format(len(alltweets)))

    #transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    #write the csv
    with open("{}_tweets.csv".format(screen_name),'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id","created_at","text"])
        writer.writerows(outtweets)
    
    pass

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("nba")
    teams= df_att_cost.TEAM.unique()
    for team in teams:
        get_all_tweets(team)