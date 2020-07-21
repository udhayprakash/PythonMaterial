#!/usr/bin/env python
"""
    geoipy.py
    A simple IP geolocation python script.
    Uses geody.com geolocation web service.
    Requires BeautifulSoup library.

    Example:
    $ ./geoipy.py 198.117.0.122
    IP: 198.117.0.122 Location: MSFC, ALABAMA, \
    United States (National Aeronautics and Space Administration)

    ksaver, June 18, 2011.
    Public Domain Code.
"""

import re
import sys
from urllib.request import urlopen

from bs4 import BeautifulSoup as Soup


def main(ipaddr):
    """Geo-locates an IP address passed in argv[1]."""

    geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
    print('geody:', geody)
    html_page = urlopen(geody).read()
    soup = Soup(html_page, "lxml")

    # Filter paragraph containing geolocation info.
    paragraph = soup('p')[3]

    # Remove html tags using regex.
    geo_txt = re.sub(r'<.*?>', '', str(paragraph))
    print(geo_txt[32:].strip() + '\n')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main('127.0.0.1')
