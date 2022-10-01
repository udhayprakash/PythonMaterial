#!/usr/bin/python3
"""
I tweaked his script of live scores for windows
notifications because pynotify don't work on Windows.
This requires Growl for Windows to show notifications.
I hope it helps the windows' users.
"""
from time import sleep

import gntp.notifier
import requests
from bs4 import BeautifulSoup

# register

growl = gntp.notifier.GrowlNotifier(
    applicationName="Cricket Scores",
    notifications=["New Updates", "New Messages"],
    defaultNotifications=["New Messages"],
    # hostname = "http://computer.example.com", # Defaults to localhost
    # password = "abc123" # Defaults to a blank password
)
growl.register()


def show_message(score):
    # Send message
    image = open("cric.jpg", "rb").read()
    growl.notify(
        noteType="New Messages",
        title="Match Scores",
        description=score,
        icon=image,
        sticky=False,
        priority=1,
    )
    return


url = "http://static.cricinfo.com/rss/livescores.xml"
while True:
    r = requests.get(url)
    if r.status_code != 200:
        break
    soup = BeautifulSoup(r.text)
    data = soup.find_all("description")
    score = data[1].text
    show_message(str(score))
    sleep(10)
