import re
import urllib

print "we will try to open this url, in order to get IP Address"

url = "http://checkip.dyndns.org"

print url

response = urllib.urlopen(url).read()
print response
"""
<html><head><title>Current IP Check</title></head><body>Current IP Address: 103.70.129.81</body></html>
<html>
<head>
    <title>Current IP Check</title>
</head>
    <body>
    Current IP Address: 103.70.129.81
    </body>
</html>
"""
# Method 1
# print response.split(': ')
# print response.split(': ')[1]
# theIP =  response.split(': ')[1].split('<')[0]

# Method 2
theIP = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", response)[0]

print "your IP Address is: ", theIP
