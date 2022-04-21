#!/usr/bin/python3

from bs4 import BeautifulSoup
from gazpacho import get, Soup
from datetime import datetime

url = 'https://en.wikipedia.org/wiki/Gazpacho'
html = get(url)

st_time = datetime.now()
soup = Soup(html)
soup.find('span', {'class': 'mw-headline'})
print(f'TIME TAKEN- bs - {datetime.now() - st_time}')

st_time = datetime.now()
soup = BeautifulSoup(html, 'lxml')
soup.find('span', {'class': 'mw-headline'})
print(f'TIME TAKEN- gp - {datetime.now() - st_time}')


# gazpacho is often 20-40% faster than BeautifulSoup:
# https://gazpacho.xyz/
