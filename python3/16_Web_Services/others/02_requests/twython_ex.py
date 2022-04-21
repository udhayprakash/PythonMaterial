#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython

APP_KEY = '***'
APP_SECRET = '***'
ACCESS_TOKEN = '***'
ACCESS_TOKEN_SECRET = '***'

twitter = Twython(APP_KEY, APP_SECRET,
                  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

user_tweets = twitter.get_user_timeline(screen_name='_true_false', include_rts=True)
tweets = ''
for tweet in user_tweets:
    tweet = Twython.html_for_tweet(tweet)
    tweets += '<li>' + tweet + '</li>'

html = """


    <link rel="stylesheet" href="https://abs.twimg.com/a/1387359134/t1/css/t1_core.bundle.css" type="text/css">
   <meta charset="UTF-8">


   <div class="tweet"><ul>""" + tweets + """</ul></div>


"""

create_html = open('tweets.html', 'w')
create_html.write(html.encode('utf-8').strip())
create_html.close()
