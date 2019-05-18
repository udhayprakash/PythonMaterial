import os
from urllib.request import urlopen
from html.parser import HTMLParser


# Parse xkcd page
class Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.is_comic = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        # If found 'comic' div, then next img has comic link
        if tag == 'div' and 'id' in attrs:
            if attrs['id'] == 'comic':
                self.is_comic = True

        # Set self.url to comic image url
        elif tag == 'img' and self.is_comic:
            self.url = attrs['src']
            self.is_comic = False


def get_xkcd(n=''):
    # Download comic page
    url = 'https://xkcd.com/{}'.format(n)
    print('---', url)
    page = urlopen(url).read().decode('utf-8')

    # Get image url from parser
    parser = Parser()
    parser.feed(page)

    # Path to xkcd folder on Desktop
    folder = os.path.join(os.path.expanduser('~'), 'Desktop/xkcd')

    # If folder doesn't exist, create one
    if not os.path.exists(folder):
        os.makedirs(folder)

    image_name = parser.url.split('/')[-1]
    path = os.path.join(folder, image_name)

    with open(path, 'wb') as f:
        print('======', 'https:' +parser.url)
        f.write(urlopen('https:'+ parser.url).read())

# Get a bunch of comics
for i in range(1200, 1212):
    get_xkcd(i)
    print(('Downloaded xkcd #{}'.format(i)))