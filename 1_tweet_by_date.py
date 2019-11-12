# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:40:59 2019

@author: Charina
"""

import tweepy
from tweepy import OAuthHandler, Stream, StreamListener
import datetime

consumer_key="usxRvFGhru7Rqx8aX7ShspYNk"
consumer_secret="f1wCqdDduEy3NAW28fmI6Z35jeRMA9wHDcB6Azom2gEw1eaIm1"
access_token="1802824008-TweKby6X2sYmxQa3cSRa5IbXTnS2OwaWSAvrnoh"
access_token_secret="XLVfN3NBSI39pFBqkKerjqy9fow2DW5jjShxtMo9K1ojQ"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api =  tweepy.API(auth)

the_list = []
tweet_jokowi = api.user_timeline(screen_name='jokowi', count=200, tweet_mode="extended")
start_date = datetime.datetime(2019, 10, 10, 00, 00, 00)
end_date = datetime.datetime(2019, 10, 23, 00, 00, 00)
for tweet in tweet_jokowi:
    if tweet.created_at < end_date and tweet.created_at > start_date:
        the_list.append(tweet)

import pandas
myData = pandas.DataFrame(the_list)
myData