import json
import urllib2
import ConfigParser
import sys 

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
location = parsed_json['current_observation']['display_location']['city']
temp_f = parsed_json['current_observation']['temp_f']
print "Current temperature in %s is: %s" % (location, temp_f)
f.close()