#! /usr/bin/python3

import requests
from bs4 import BeautifulSoup
import os
import datetime

currentTime = datetime.datetime.now()
currentDate = str(currentTime.year) + '0' + str(currentTime.month) + str(currentTime.day)
if not os.path.exists('C:/BingWallpaper'):
    os.makedirs('C:/BingWallpaper')
bingUrl = 'http://www.bing.com/gallery/'
sc = requests.get(bingUrl)
soup = BeautifulSoup(sc.text, 'lxml')
image = soup.select('.cursor_zoom img')
image_url = image[0].get('src')
res = requests.get(image_url)
with open(os.path.join('Bing', currentDate + '.jpg'), 'wb') as file:
    file.write(res.content)
os.system('gsettings set org.gnome.desktop.background picture-uri http://file:///home/radioactive/Bing/' + currentDate + '.jpg')