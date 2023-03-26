"""
Usage: python google.py <keyword>
Description: Script googles the keyword and opens top 10(max) search results in separate tabs in the browser
Usage: python filename.py keyword
Tested with Python3
"""

import sys
import webbrowser

import bs4
import pyperclip
import requests


def start():
    if len(sys.argv) > 1:
        keyword = " ".join(sys.argv[1:])
    else:
        # if no keyword is entered, the script would
        # search for the keyword copied in the clipboard
        keyword = pyperclip.paste()

    res = requests.get("https://google.com/search?q=" + keyword)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    links = soup.select(".r a")
    tab_counts = min(10, len(links))

    for i in range(tab_counts):
        webbrowser.open("https://google.com" + links[i].get("href"))


start()
