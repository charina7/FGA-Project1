# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:24:36 2019

@author: Charina
"""

import tweepy
import csv
from tweepy import OAuthHandler, Stream, StreamListener
 

consumer_key="usxRvFGhru7Rqx8aX7ShspYNk"
consumer_secret="f1wCqdDduEy3NAW28fmI6Z35jeRMA9wHDcB6Azom2gEw1eaIm1"
access_token="1802824008-TweKby6X2sYmxQa3cSRa5IbXTnS2OwaWSAvrnoh"
access_token_secret="XLVfN3NBSI39pFBqkKerjqy9fow2DW5jjShxtMo9K1ojQ"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api =  tweepy.API(auth)


csvFile = open('file1.csv', 'a')
csvWriter = csv.writer(csvFile)
for tweet in  tweepy.Cursor(api.search,q="#PasukanRebahan", lang="en",count=200, since="2019-10-10").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
