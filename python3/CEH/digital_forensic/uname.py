import twitter

MyAPI = twitter.Api(twitter_app_consumer_key= ** ** ** ** ** ** ** ** ** ** ** ** **,
twitter_consumer_secret = ** ** ** ** ** ** ** ** ** ** ** ** **,
access_token_key = ** ** ** ** ** ** ** ** ** ** ** ** **,
access_token_secret = ** ** ** ** ** ** ** ** ** ** ** ** ** )

# Setup the Handle
Twitterhandle = 'gauravkumarin'

Twitteruser = MyAPI.GetUser(twitter_screen_name=Twitterhandle)
print
Twitteruser.GetName()
print
Twitteruser.GetDescription()
print
Twitteruser.GetFollowersCount()
print
Twitteruser.GetStatusesCount()
print
Twitteruser.GetUrl()
# get a user timeline
Currentstatuses = MyAPI.GetUserTimeline(twitter_screen_name='gauravkumarin', count=1)
print[gk.text
for gk in Currentstatuses]
