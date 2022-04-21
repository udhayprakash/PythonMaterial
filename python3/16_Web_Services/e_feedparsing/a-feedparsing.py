#!/usr/bin/python3
"""
Purpose: Parsing reddit feeds

    RSS -  Really Simple Syndication
        - it will be an XML file

Installation:
    pip install -U feedparser --user
"""
import feedparser
from pprint import pprint

reddit_feed = feedparser.parse("http://www.reddit.com/r/python/.rss")

print(type(reddit_feed))
# <class 'feedparser.util.FeedParserDict'>

import json

with open("reddit_python_feed.rss", "w") as f:
    json.dump(reddit_feed, f, indent=2)
    f.close()

# two ways of parsing values
print(reddit_feed["feed"]["link"])
print(reddit_feed.feed.link)
print()

print(f"{reddit_feed.version      = }")
print(f"{reddit_feed.headers      = }")
print(f"{len(reddit_feed.entries) = }")
print()
for post in reddit_feed.entries[:5]:
    print(post.title + ": " + post.link)
