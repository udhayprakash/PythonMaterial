# -*- coding: utf-8 -*-
"""
http://dev.maxmind.com/geoip/legacy/geolite/
"""

import pygeoip

myGeoIP = pygeoip.GeoIP('GeoIP.dat')

print(myGeoIP.country_name_by_addr('10.10.10.10'))
