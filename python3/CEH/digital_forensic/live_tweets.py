from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

twitter_app_consumer_key = ** ** ** ** ** ** ** ** ** ** ** ** **
twitter_consumer_secret = ** ** ** ** ** ** ** ** ** ** ** ** **
twitter_access_token = '**************************’
twitter_access_secret = ** ** ** ** ** ** ** ** ** ** ** ** **

class MyTweetListener(StreamListener):
    def on_data(self, thisdata):
        print
        thisdata
        return True

    def on_error(self, Currentstatus):
        print
        Currentstatus


MyAuth = OAuthHandler(twitter_app_consumer_key, twitter_consumer_secret)
MyAuth.set_access_token(twitter_access_token, twitter_access_secret)
TwitterStream = Stream(MyAuth, MyTweetListener())
TwitterStream.filter(track=['India'])
