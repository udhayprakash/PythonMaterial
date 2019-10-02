#!/usr/bin/python
"""
Purpose: Twitter data scrapping
"""
import tweepy
from pprint import pprint
import json


class TwitterLogin:
    def __init__(self):
        consumer_key = 'xxxxxxxxxxxxxxxxxxxxx'
        consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token = '00000-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth,
                              wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)

    def credentials_verification(self):
        result = vars(self.api.verify_credentials())['_json']

        print(f'''Account
        User                : {result['name']}
        Screen Name         : {result['screen_name']}
        Location            : {result['location']}
        Profile description : {result['description']}
        Account Created at  : {result['created_at']}
        Display URL         : {result['entities']['url']['urls'][0]['display_url']}
        ''')


class TwitterScrapping(TwitterLogin):
    def __init__(self):
        TwitterLogin.__init__(self)


# twtr = TwitterLogin()
# twtr.credentials_verification()

twrt_scrp = TwitterScrapping()
twrt_scrp.credentials_verification()

# Latest Public Timeline
tweet = twrt_scrp.api.home_timeline()[0]
print(f''' 
tweet.text                          : {tweet.text}
tweet.contributors                  : {tweet.contributors}
tweet.created_at                    : {tweet.created_at}
tweet.lang                          : {tweet.lang}
tweet.source                        : {tweet.source}
tweet.source_url                    : {tweet.source_url}
tweet.truncated                     : {tweet.truncated}

tweet.retweet_count                 : {tweet.retweet_count}
tweet.retweeted                     : {tweet.retweeted}

tweet.retweet                       : {tweet.retweet}
tweet.retweets                      : {tweet.retweets}
tweet.possibly_sensitive            : {tweet.possibly_sensitive}
tweet.possibly_sensitive_appealable : {tweet.possibly_sensitive_appealable}
''')
