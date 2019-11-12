# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:18:33 2019

@author: Charina
"""

import tweepy
from tweepy import OAuthHandler, Stream, StreamListener
 

consumer_key="usxRvFGhru7Rqx8aX7ShspYNk"
consumer_secret="f1wCqdDduEy3NAW28fmI6Z35jeRMA9wHDcB6Azom2gEw1eaIm1"
access_token="1802824008-TweKby6X2sYmxQa3cSRa5IbXTnS2OwaWSAvrnoh"
access_token_secret="XLVfN3NBSI39pFBqkKerjqy9fow2DW5jjShxtMo9K1ojQ"
auth = OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api =  tweepy.API(auth,wait_on_rate_limit=True)

hastags = ["kirana","Fiersa","Jackson Wang","X1","Stray Kids"]
for hastag in hastags:  
    for tweet in tweepy.Cursor(api.search, q=hastag, count=20, lang="id", since="2019-10-23", until="2019-10-24").items():
        print (tweet.created_at, tweet.text)