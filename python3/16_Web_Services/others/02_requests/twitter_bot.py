import time

import tweepy


class Bot:
    def __init__(self):
        # GET below values from twitter
        self.CONSUMER_KEY = ''
        self.CONSUMER_KEY_SECRET = ''
        self.ACCESS_TOKEN = ''
        self.ACCESS_TOKEN_SECRET = ''

        self.api = self.authenticate()
        self.user_list = []

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        try:
            api.verify_credentials()
        except:
            print("The bot was unable to authenticate")
        else:
            print("The bot has been authenticate")
        return api

    def grab_users_followers(self, user):
        for page in tweepy.Cursor(self.api.followers_ids, user).pages():
            self.user_list.extend(page)
            time.sleep(5)
            print(len(self.user_list), "users in list")

    def mass_follow(self, users):
        for user in users:
            self.api.create_friendship(user)
        print("You are following iser ID: {}".format(user))
        time.sleep(1)


twitter_bot = Bot()
twitter_bot.grab_users_followers("")
twitter_bot.mass_follow(twitter_bot.user_list)
