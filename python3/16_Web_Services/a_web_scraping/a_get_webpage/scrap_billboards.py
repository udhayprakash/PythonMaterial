import lxml
import requests
from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
r = requests.get(URL)

doc = BeautifulSoup(r.content, "lxml")
structured_doc = doc.prettify()

list = []

first_song = doc.find("h3").text.strip()

song = "1. " + (first_song)
list.append(song)

ss = doc.findAll(
    "h3",
    class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only",
)

num = 2
for i in ss:
    songs = str(num) + "." + " " + (i.text).strip()
    list.append(songs)
    num = num + 1

f = open("Billboard_Hot_100.txt", "w+")
f.write("BILLBOARD HOT 100\n")
for i in list:
    f.write(i)
    f.write("\n")
f.close()
