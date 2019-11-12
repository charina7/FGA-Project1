# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:42:45 2019

@author: Charina
"""

import tweepy
import logging

logger = logging.getLogger()

def create_api():
    consumer_key = "SNQhGk0I7spipDtgCppD6DSOg"
    consumer_secret = "nKCMZCDoREn7jieApHhHEXboC1qCJDfZwsCgdDI99XclQNwvuv"
    access_token = "1802824008-tp3mdOXGkQ0fRxOysjPciTBFBLudmJslsxCCox8"
    access_token_secret = "3nuxJVkfoye2fyomwfePCC7Hyj1eyRUSsJpCtawLuuf6b"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error Creating API",exc_info=True)
        
        raise e
    logger.info("API created")
    
    return api