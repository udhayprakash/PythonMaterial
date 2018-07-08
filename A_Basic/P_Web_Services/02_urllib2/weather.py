import json
import urllib2
import ConfigParser
import sys 
from pprint import pprint 

config = ConfigParser.ConfigParser()
config.read('weather.ini')

api_key = config.get('prod', 'APIKEY') 
URL = 'http://api.wunderground.com/api/{apikey}/conditions/q/CA/San_Francisco.json'.format(apikey=api_key)
print 'URL=', URL

try:
    f = urllib2.urlopen(URL)
except urllib2.HTTPError as ex:
    print ex 
    sys.exit(1)

json_string = f.read()
parsed_json = json.loads(json_string)

# pprint(parsed_json)
with open('weather.json', 'wb') as g:
    g.write(json_string)
    g.close()

location = parsed_json['current_observation']['display_location']['city']
temperature_string = parsed_json['current_observation']['temperature_string']
print "Current temperature in %s is: %s" % (location, temperature_string)
f.close()
