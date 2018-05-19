import urllib
import re

print "we will try to open this url, in order to get IP Address"

url = "http://checkip.dyndns.org"

print url

response = urllib.urlopen(url).read()
print response
theIP = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", response)

print "your IP Address is: ",  theIP