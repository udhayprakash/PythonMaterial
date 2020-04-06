#!/usr/bin/python
"""
Purpose:
"""

import os

import twitter

api = twitter.Api(consumer_key=os.getenv('TWITTER_API_KEY'),
                  consumer_secret=os.getenv('TWITTER_API_SECRET_KEY'),
                  access_token_key=os.getenv('TWITTER_ACCESS_TOKEN'),
                  access_token_secret=os.getenv('TWITTER_ACCESS_TOKEN_SECRET'))


print(f'api.base_url    : {api.base_url}')
print(f'api.stream_url  : {api.stream_url}')
print(f'api.chunk_size  : {api.chunk_size}')
print(f'api.tweet_mode  : {api.tweet_mode}')