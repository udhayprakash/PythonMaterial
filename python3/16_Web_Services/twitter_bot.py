#!/usr/bin/python3
"""
Purpose:
pip install python-twitter
"""
from twitter import Twitter, OAuth, TwitterHTTPError
import time
# enter the corresponding information from your Twitter application:
consumer_key = ''  # keep the quotes, replace this with your consumer key
consumer_secret = ''  # keep the quotes, replace this with your consumer secret key
access_token_key = ''  # keep the quotes, replace this with your access token
access_token_secret = ''  # keep the quotes, replace this with your access token secret


t = Twitter(auth=OAuth(access_token_key, access_token_secret,
            consumer_key, consumer_secret))


def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)


def get_limit():
    try:
        result = t.application.rate_limit_status()
        print(result)
    except TwitterHTTPError as e:
        print('Error: ', e)
        return None


def fav_tweet(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print('Favorited: %s' % (result['text']))
        return result
    # when you have already favourited a tweet
    # this error is thrown
    except TwitterHTTPError as e:
        print('Error: ', e)
        return None


def retweet_tweet(tweet):
    try:
        result = t.statuses.retweet._id(_id=tweet['id'])
        print('Retweeted: %s' % (result['text']))
        return result
    except TwitterHTTPError as e:
        print('Error: ', e)
        return None


def auto_fav(q, count):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print(a)
    success = 0
    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1
    print('We Favorited a total of %i out of %i tweets' % (success,
          len(result['statuses'])))


def auto_retweet(q, count):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print(a)
    success = 0
    for tweet in result['statuses']:
        if retweet_tweet(tweet) is not None:
            success += 1
        time.sleep(10)
    print('We Favorited a total of %i out of %i tweets' %
          (success, len(result['statuses'])))


if __name__ == '__main__':
    while(1):
        try:
            auto_retweet('GameDev', 1)
            auto_retweet('IndieDev', 1)
            auto_retweet('ScreenshotSaturday', 1)
        except Exception as e:
            print(e)

        try:
            auto_fav('IndieDev', 1)
        except Exception as e:
            print(e)
