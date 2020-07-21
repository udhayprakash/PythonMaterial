#!/usr/bin/python
"""
Purpose: Working with reddit API
    https://praw.readthedocs.io/en/latest/
"""
import praw
reddit = praw.Reddit(client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                     password='PASSWORD', user_agent='USERAGENT',
                     username='USERNAME')

# Create a submission to r/test
reddit.subreddit('test').submit('Test Submission', url='https://reddit.com')

# Comment on a known submission
submission = reddit.submission(url='https://www.reddit.com/comments/5e1az9')
submission.reply('Super rad!')

# Reply to the first comment of a weekly top thread of a moderated community
submission = next(reddit.subreddit('mod').top('week'))
submission.comments[0].reply('An automated reply')

# Output score for the first 256 items on the frontpage
for submission in reddit.front.hot(limit=256):
    print(submission.score)

# Obtain the moderator listing for r/redditdev
for moderator in reddit.subreddit('redditdev').moderator():
    print(moderator)