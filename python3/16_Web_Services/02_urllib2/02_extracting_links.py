from __future__ import print_function
import urllib2, sys
from HTMLParser import HTMLParser
 
links = []
 
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        attr = dict(attrs)
        links.append(attr)
 
def extract():
    if len(sys.argv) != 2:
        print('Usage: {} URL'.format(sys.argv[0]))
        return
    url = sys.argv[1]
 
    try:
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
    except urllib2.HTTPError as e:
        print(e, 'while fetching', url)
        return
 
    parser = MyHTMLParser()
    parser.links = []
    parser.feed(html)
    for l in links:
        print(l)
 
extract()