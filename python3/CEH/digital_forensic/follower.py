import tweepy
import time

twitter_app_consumer_key = '**************************'
twitter_consumer_secret = '**************************'
twitter_access_token = '**************************'
twitter_access_secret = '**************************'
MyAuth = tweepy.auth.OAuthHandler(twitter_app_consumer_key, twitter_consumer_secret)
MyAuth.set_access_token(twitter_access_token, twitter_access_secret)
MyAPI = tweepy.API(MyAuth)
followerlist = open('followerslist.txt', 'w')
if (MyAPI.verify_credentials):
    print
    'Connected to Twitter Server'
user = tweepy.Cursor(api.followers, twitter_screen_name="gauravkumarin").items()
while True:
    try:
        u = next(twitteruser)
        followerlist.write(u.twitter_screen_name + ' \n')
except:
time.sleep(15 * 60)
u = next(twitteruser)
followerlist.write(u.twitter_screen_name + ' \n')
followerlist.close()
